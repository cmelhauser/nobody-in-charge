"""Structural sensitivity: perturbing the model's CHOICES rather than its numbers.

Why this exists. Appendix A5.6, "What no design covers", opens by saying that structural
choices were not perturbed and lists four: whether the capacity gate phases in by step index,
whether Tradition 3 acts on retention rather than admission, whether carrying capacity comes
from the established core, and whether the resource list has eight entries. Every sensitivity
design in this project varies the 118 hand-chosen *numbers*. None varies the shape.

That distinction matters because the book's surviving claims are orderings, and an ordering can
be robust to every number in a model and still be an artefact of its architecture.

Four variants, each a single structural change with everything else held at nominal:

  A  gate_flat        The capacity gate does not phase in by step index. Every step is gated
                      identically rather than later steps being gated behind earlier ones.
  B  t3_admission     Tradition 3 acts on ARRIVAL rather than on retention: a closed group
                      receives fewer newcomers instead of losing them faster. This is the
                      reading Chapter 19 argues against, and it is the one most readers will
                      reach for, so it is the most important variant here.
  C  capacity_all     Carrying capacity is supplied by ALL members rather than by the
                      established core alone.
  D  no_saturation    Capacity is PIECEWISE-LINEAR in its argument rather than hyperbolic.
                      The name is a shorthand and is inaccurate on its own: the linear form is
                      clipped at 1, so it still saturates, it just reaches the ceiling abruptly
                      at c = 2k instead of approaching it asymptotically. Above c = 2k it is
                      MORE saturating than c/(c+k), not less. The two forms are matched at
                      c = k, where both equal 0.5, so the change is of shape and not of level.

Each variant is run against the same five decline scenarios as `scenarios_hiseed.py`, at 400
seeds, so the question asked is not "does the number change" but **"does the ordering that the
book actually claims survive the change in architecture?"** The book's two surviving simulation
claims are that a fully adherent group persists, and that losing referrals is worse than losing
attraction. Both are orderings and both are checked here for every variant.

Implementation note. The variants are applied by monkey-patching the loaded model module rather
than by adding switches to `aa_group_model.py`, because eleven other scripts import that file
and their cached results must remain reproducible from the version they were run against.

Cached to `../research/structural.json`; resumable.

Run:  python3 structural_variants.py [n_workers] [batch]
"""
import hashlib, importlib.util, sys, os, json
import numpy as np
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'aa_group_model.py')
OUT = os.path.abspath(os.path.join(HERE, '..', 'research', 'structural.json'))

NSEED = 400
H = 1560
VARIANTS = ['base', 'gate_flat', 't3_admission', 'capacity_all', 'no_saturation']
SCEN = ['full', 'attraction', 'referral', 'both', 'gatekeeping']


def _load():
    spec = importlib.util.spec_from_file_location('m', MODEL)
    mm = importlib.util.module_from_spec(spec)
    sys.modules['m'] = mm
    spec.loader.exec_module(mm)
    return mm


def _apply(mm, variant):
    """Replace one structural choice by monkey-patching the loaded module.

    The variants live inside `resources` and `step_growth`, so each is implemented as a
    replacement for one of those functions, written to differ from the original in exactly
    one place and marked with a VARIANT comment there.
    """
    if variant == 'base':
        return
    np_ = np

    if variant == 'gate_flat':
        NSTEP = mm.NSTEP; Snorm = mm.Snorm; BETA = mm.BETA
        def step_growth(X, alive, R, T, P, het=None):
            hill = lambda M: M**P['hill_n']/(P['hill_k']**P['hill_n']+M**P['hill_n'])
            G = Snorm @ R
            gate = np_.ones_like(X); gate[:, 1:] = np_.clip(X[:, :-1], 0, 1)**P['p_gate']
            peer = (1-BETA) + BETA*G
            own = hill(X[:, 9:12].mean(axis=1))
            Gcap = own[alive].mean() if alive.sum() else 0.0
            C = own + (1-own)*P['omega']*Gcap
            # VARIANT A: the capacity gate does NOT phase in by step index. The original is
            # np.linspace(0.05, 1.0, NSTEP); this is that array's mean, held constant, so
            # total gate exposure across the twelve steps is unchanged and only its
            # distribution across them differs.
            wgt = np_.full(NSTEP, float(np_.mean(np_.linspace(0.05, 1.0, NSTEP))))
            Cm = 1.0 - wgt[None, :]*(1.0 - C[:, None])
            g = P['a']*gate*peer*Cm
            if het is not None: g = g*het[:, None]
            d = np_.full(X.shape, P['delta0']); d[:, :11] *= (1+P['psi']*(1-X[:, 1:12]))
            return g*(1-X) - d*X
        mm.step_growth = step_growth
        return

    if variant in ('capacity_all', 'no_saturation'):
        RES = mm.RES; GOVW = mm.GOVW; eff = mm.effective_adherence
        cap_all = (variant == 'capacity_all')
        def resources(X, alive, T, P, solvent, resource_T=None, recipient_override=None,
                      return_components=False):
            if cap_all:
                sat = lambda c, k: c/(c+k)                    # unchanged
            else:
                # VARIANT D: capacity is PIECEWISE-LINEAR rather than hyperbolic. Clipped at
                # 1, so it still saturates; it reaches the ceiling at c = 2k instead of
                # approaching it. The divisor of 2k makes the two forms agree at c = k, where
                # both are 0.5, so the change is of shape and not of level. Verified: at
                # c = 2k the linear form is 1.000 and the hyperbolic 0.667, so above that
                # point this variant is the MORE saturating of the two.
                sat = lambda c, k: min(float(c)/(2.0*max(k, 1e-9)), 1.0)
            if alive.sum() == 0: return np_.zeros(len(RES)), 0.0
            lv = X[alive].mean(axis=1)
            core = lv > P['act_thr']; exp = lv > P['exp_thr']; low_practice = ~core
            Tr = T if resource_T is None else resource_T
            Te = eff(Tr)
            q = GOVW.T @ Te
            unity = 1-2*lv[core].std() if core.sum() > 1 else (1.0 if core.sum() == 1 else 0.0)
            unity = float(np_.clip(unity, 0, 1))
            # VARIANT C: capacity is supplied by ALL living members rather than by the
            # established core and the experienced subset.
            n_core = float(alive.sum()) if cap_all else float(core.sum())
            n_exp = float(alive.sum()) if cap_all else float(exp.sum())
            recipient = sat(low_practice.sum()/max(n_exp, 1.0), P['k_recip'])
            if recipient_override is not None:
                recipient = float(np_.clip(recipient_override, 0, 1))
            cap = np_.array([
                1.0,
                sat(n_core, P['k_ident']) * unity,
                sat(n_exp,  P['k_proof']),
                sat(n_exp,  P['k_conf']),
                sat(n_exp,  P['k_couns']),
                recipient,
                (0.45+0.55*solvent) * unity,
                unity,
            ])
            result = np_.clip(cap*q, 0, 1)
            if return_components:
                comp = dict(capacity=cap.copy(), governance=q.copy(),
                            effective_adherence=Te.copy(),
                            low_practice=int(low_practice.sum()),
                            high_practice=int(exp.sum()),
                            recipient_ratio=float(low_practice.sum()/max(n_exp, 1.0)))
                return result, unity, comp
            return result, unity
        mm.resources = resources
        return

    if variant == 't3_admission':
        mm._T3_ON_ARRIVAL = True
        return


def _simulate(mm, T, P, seed, attraction_T11=None):
    """Re-implements simulate() so the Tradition 3 variant can be applied. Kept line for line
    comparable with aa_group_model.simulate; the only differences are guarded by the variant
    flag and are marked VARIANT B. The other three variants are patches to `resources` and
    `step_growth` and need no change here."""
    P = {**mm.DEFAULTS, **(P or {})}
    dt = 0.5
    rng = np.random.default_rng(seed)
    cap = P['cap']
    X = np.zeros((cap, mm.NSTEP)); alive = np.zeros(cap, bool)
    het = mm.mean_one_lognormal(rng, P['het_sd'], cap)
    X[:25] = 0.55; alive[:25] = True
    t3_arrival = getattr(mm, '_T3_ON_ARRIVAL', False)
    for _ in range(int(H / dt)):
        n = alive.sum()
        if n == 0: break
        lv = X[alive].mean(axis=1)
        established = (lv > P['act_thr']).sum()
        solvent = 1.0 if established * P['contrib'] >= P['cost'] else \
            float(np.clip(established * P['contrib'] / P['cost'], 0, 1))
        R, unity = mm.resources(X, alive, T, P, solvent)
        X = np.clip(X + dt * mm.step_growth(X, alive, R, T, P, het), 0, 1)
        X[~alive] = 0.0
        early = X[:, :3].mean(axis=1)
        newness = np.exp(-6.0 * X.mean(axis=1))
        # VARIANT B: with Tradition 3 acting on arrival there is no retention friction.
        t3_frict = 1.0 if t3_arrival else (1.0 + (1.0 - T[2]) * newness)
        h = P['drop0'] * np.exp(-P['drop_k'] * early) * t3_frict + P['churn']
        die = alive & (rng.random(cap) < h * dt)
        alive[die] = False; X[die] = 0.0
        # Match the canonical absorbing-boundary rule: a group with no
        # remaining members is closed before any same-step arrival is drawn.
        if alive.sum() == 0:
            break
        att = X[alive, 11].sum() if alive.sum() else 0.0
        att_t11 = T[10] if attraction_T11 is None else attraction_T11
        lam = P['lam_exog'] + P['lam0'] * att * att_t11
        # VARIANT B: a closed group receives fewer people instead of keeping fewer.
        if t3_arrival: lam *= T[2]
        k = rng.poisson(max(lam * dt, 0))
        free = np.where(~alive)[0][:k]
        alive[free] = True; X[free] = 0.02
        het[free] = mm.mean_one_lognormal(rng, P['het_sd'], len(free))
    n = alive.sum()
    lv = X[alive].mean(axis=1) if n else np.array([])
    est = lv > P['act_thr'] if n else np.array([], bool)
    return dict(N=int(n), mean=float(lv.mean()) if n else 0.0,
                n_est=int(est.sum()) if n else 0,
                est_mean=float(lv[est].mean()) if n and est.sum() else 0.0)


def _one(job):
    variant, scen, seed = job
    mm = _load()
    _apply(mm, variant)
    T = mm.FULL.copy(); P = {}
    attraction_T11 = 0.0 if scen in ('attraction', 'both') else None
    if scen in ('referral', 'both'):   P['lam_exog'] = 0.0
    if scen == 'gatekeeping':          T[2] = 0.0
    r = _simulate(mm, T, P, seed, attraction_T11=attraction_T11)
    return dict(N=r['N'], exists=int(r['N'] > 0), viable=int(r['N'] > 5),
                alive=int(r['N'] > 5), est_mean=r['est_mean'], n_est=r['n_est'])


def _save(out):
    tmp = OUT + '.tmp'
    json.dump(out, open(tmp, 'w'))
    os.replace(tmp, OUT)


if __name__ == '__main__':
    nw = int(sys.argv[1]) if sys.argv[1:] else 4
    batch = int(sys.argv[2]) if sys.argv[2:] else 10 ** 9
    jobs = [(v, s, sd) for v in VARIANTS for s in SCEN for sd in range(NSEED)]
    model_hash=hashlib.sha256(open(MODEL,'rb').read()).hexdigest()
    script_hash=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    if (out.get('meta',{}).get('model_sha256') != model_hash or
            out.get('meta',{}).get('script_sha256') != script_hash): out={}
    out['meta'] = dict(schema_version=2,status='incomplete',model_sha256=model_hash,
                       script_sha256=script_hash,script='model/structural_variants.py',
                       variants=VARIANTS,scenarios=SCEN,nseed=NSEED,
                       seed_range=[0,NSEED-1],horizon=H,dt=0.5,
                       jobs_expected=len(jobs),
                       attraction_intervention='pure T11 attraction path; governance held at one',
                       t3_admission='replaces dropout friction but retains the scenario governance value',
                       viability='endpoint N > 5; existence N > 0')
    key = lambda j: f'{j[0]}|{j[1]}|{j[2]}'
    todo = [j for j in jobs if key(j) not in out][:batch]
    print(f'{len(out)-1} of {len(jobs)} done, running {len(todo)}', flush=True)
    if todo:
        n = 0
        with ProcessPoolExecutor(nw) as ex:
            for j, r in zip(todo, ex.map(_one, todo)):
                out[key(j)] = r
                n += 1
                if n % 40 == 0: _save(out)
        _save(out)
    done = sum(1 for j in jobs if key(j) in out)
    out['meta']['jobs_completed']=done
    out['meta']['status']='complete' if done==len(jobs) else 'incomplete'
    _save(out)
    print(f'{done} of {len(jobs)} complete', flush=True)
    print('ALL DONE' if done == len(jobs) else 'PARTIAL', flush=True)
