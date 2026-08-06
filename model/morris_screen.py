"""Morris elementary-effects screen over all 118 hand-chosen parameters.

Why this exists. Every sensitivity design run before it is either a global jitter, which
confounds all interactions together and reports only whether a claim survives, or a
one-at-a-time star around the nominal point, which cannot see interactions at all. Neither
yields a variance decomposition, and neither can say whether a parameter matters because of
its own effect or because of how it combines with others.

Morris (1991), in the improved sampling of Campolongo, Cariboni and Saltelli (2007), is the
standard screening design for this many factors. It computes, for each factor:

    mu*    the mean ABSOLUTE elementary effect. How much the factor moves the output.
    mu     the mean signed elementary effect. Direction, and whether it is consistent.
    sigma  the standard deviation of the elementary effects. High sigma means the factor's
           effect depends on where the other factors are, which is interaction or
           non-linearity. It cannot distinguish the two, and this script does not claim to.

Design. r trajectories, each visiting k+1 points and changing one factor at a time, so the
cost is r*(k+1) model evaluations rather than the r*2*k of a naive scheme. Factors are
mapped to the unit hypercube over plus or minus 25 per cent of nominal, matching the
targeted OAT sweep so the two are comparable. p = 4 levels, delta = 2/3.

Reference point. Traditions are held at 0.85, not 1.0. At full adherence the governance
matrix cancels exactly (appendix A5.3), so 35 of the 118 factors would have identically
zero effect and a third of the design would be wasted. At 0.85 every factor is live.

Stochastic scope. Every evaluation uses the same five seeds, so common random numbers reduce
noise in within-trajectory differences. Five seeds do not make this a confirmatory design:
the output is a factor screen, and apparent small effects are not evidence of inertness.
Variation across the twenty trajectories describes dependence on location in the parameter
space; it is not a Monte Carlo confidence interval for the stochastic simulation.

Cached to `../research/morris.json`; resumable.

Run:  python3 morris_screen.py [n_workers] [batch]
"""
import hashlib, importlib.util, sys, os, json
import numpy as np
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'aa_group_model.py')
OUT = os.path.abspath(os.path.join(HERE, '..', 'research', 'morris.json'))

R_TRAJ = 20          # trajectories; expanded from 10 for the release gate
P_LEV = 4            # levels
DELTA = P_LEV / (2.0 * (P_LEV - 1))     # = 2/3 in unit-hypercube coordinates
SPREAD = 0.25        # plus or minus 25 per cent of nominal, matching the OAT sweep
NSEED = 5
H = 1560
T_REF = 0.85


def _load():
    spec = importlib.util.spec_from_file_location('m', MODEL)
    mm = importlib.util.module_from_spec(spec)
    sys.modules['m'] = mm
    spec.loader.exec_module(mm)
    return mm


def param_ids(mm):
    ids = [f'scalar:{k}' for k, v in mm.DEFAULTS.items() if np.isscalar(v)]
    ids += [f'a:{i}' for i in range(len(mm.DEFAULTS['a']))]
    ids += [f'S:{i},{j}' for i, j in zip(*np.nonzero(mm.S))]
    ids += [f'GOV:{i},{j}' for i, j in zip(*np.nonzero(mm.GOV))]
    return ids


def _rederive(mm):
    mm.GOVW[:] = mm.GOV / np.maximum(mm.GOV.sum(0, keepdims=True), 1e-12)
    mm.BETA[:] = mm.S.sum(1) / mm.S.sum(1).max()
    mm.Snorm[:] = mm.S / mm.S.sum(1, keepdims=True)


def evaluate(x):
    """x is a point in the unit hypercube, length 118. Returns the two outcomes."""
    mm = _load()
    ids = param_ids(mm)
    P = {'a': mm.DEFAULTS['a'].copy()}
    touched = False
    for xi, pid in zip(x, ids):
        mult = 1.0 + SPREAD * (2.0 * xi - 1.0)          # xi in [0,1] -> [1-s, 1+s]
        kind, rest = pid.split(':', 1)
        if kind == 'scalar':
            v = mm.DEFAULTS[rest] * mult
            P[rest] = max(int(round(v)), 5) if rest == 'cap' else v
        elif kind == 'a':
            P['a'][int(rest)] *= mult
        else:
            i, j = (int(t) for t in rest.split(','))
            (mm.S if kind == 'S' else mm.GOV)[i, j] *= mult
            touched = True
    if touched:
        _rederive(mm)
    T = np.full(12, T_REF)
    runs = [mm.simulate(T, P=P, seed=s, T_end=H) for s in range(NSEED)]
    return [float(np.mean([r['N'] for r in runs])),
            float(np.mean([r['mean'] for r in runs]))]


def trajectories(k, r, seed=20260802):
    """Campolongo-style trajectories: start at a random grid point, then step each factor
    once by +/- delta in random order. Returns r arrays of shape (k+1, k)."""
    rng = np.random.default_rng(seed)
    grid = np.linspace(0.0, 1.0 - DELTA, P_LEV // 2 + 1)
    out = []
    for _ in range(r):
        base = rng.choice(grid, size=k)
        order = rng.permutation(k)
        signs = rng.choice([1.0, -1.0], size=k)
        pts = [base.copy()]
        actual_steps = np.zeros(k)
        cur = base.copy()
        for idx in order:
            step = DELTA * signs[idx]
            if cur[idx] + step > 1.0 or cur[idx] + step < 0.0:
                step = -step
            cur = cur.copy()
            cur[idx] = np.clip(cur[idx] + step, 0.0, 1.0)
            actual_steps[idx] = step
            pts.append(cur)
        out.append((np.array(pts), order, actual_steps))
    return out


def _save(out):
    tmp = OUT + '.tmp'
    json.dump(out, open(tmp, 'w'))
    os.replace(tmp, OUT)


if __name__ == '__main__':
    nw = int(sys.argv[1]) if sys.argv[1:] else 4
    batch = int(sys.argv[2]) if sys.argv[2:] else 10**9
    mm = _load()
    ids = param_ids(mm)
    k = len(ids)
    assert k == 118, f'expected 118 factors, got {k}'
    trajs = trajectories(k, R_TRAJ)

    jobs = []
    for t, (pts, order, steps) in enumerate(trajs):
        for s in range(len(pts)):
            jobs.append((t, s))
    model_hash = hashlib.sha256(open(MODEL, 'rb').read()).hexdigest()
    script_hash = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    if (out.get('meta', {}).get('model_sha256') != model_hash or
            out.get('meta', {}).get('script_sha256') != script_hash):
        out = {}
    out['meta'] = dict(schema_version=2, status='incomplete', model_sha256=model_hash,
                       script_sha256=script_hash, script='model/morris_screen.py',
                       k=k, r=R_TRAJ, p=P_LEV, delta=DELTA, spread=SPREAD,
                       nseed=NSEED, seed_range=[0,NSEED-1], horizon=H, dt=0.5,
                       T_ref=T_REF, ids=ids, jobs_expected=len(jobs),
                       role='screening only; five common-random-number seeds per point')
    todo = [j for j in jobs if f'{j[0]}_{j[1]}' not in out][:batch]
    print(f'{len(out)-1} of {len(jobs)} points done, running {len(todo)}', flush=True)
    if todo:
        n = 0
        with ProcessPoolExecutor(nw) as ex:
            pts = [trajs[t][0][s] for t, s in todo]
            for (t, s), res in zip(todo, ex.map(evaluate, pts)):
                out[f'{t}_{s}'] = res
                n += 1
                if n % 20 == 0:
                    _save(out)
        _save(out)
    done = sum(1 for j in jobs if f'{j[0]}_{j[1]}' in out)
    out['meta']['jobs_completed'] = done
    out['meta']['status'] = 'complete' if done == len(jobs) else 'incomplete'
    if done == len(jobs):
        effects = np.empty((R_TRAJ, k, 2))
        for t, (pts, order, actual_steps) in enumerate(trajs):
            y = np.asarray([out[f'{t}_{s}'] for s in range(k + 1)], float)
            for sequence_index, factor_index in enumerate(order):
                relative_parameter_step = 2.0 * SPREAD * actual_steps[factor_index]
                effects[t, factor_index] = (
                    y[sequence_index + 1] - y[sequence_index]
                ) / relative_parameter_step
        rows = []
        for factor_index, pid in enumerate(ids):
            row = {'id': pid}
            for outcome_index, outcome in enumerate(('membership', 'mean_practice')):
                values = effects[:, factor_index, outcome_index]
                row[outcome] = dict(
                    mu=float(values.mean()),
                    mu_star=float(np.abs(values).mean()),
                    sigma=float(values.std(ddof=1)),
                    n_effects=R_TRAJ,
                )
            rows.append(row)
        out['result'] = dict(
            outcomes=['membership', 'mean_practice'],
            effect_scale='output change per unit proportional change in the parameter',
            rows=rows,
        )
    _save(out)
    print(f'{done} of {len(jobs)} complete', flush=True)
    print('ALL DONE' if done == len(jobs) else 'PARTIAL', flush=True)
