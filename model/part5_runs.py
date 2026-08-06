"""Every figure Part Five needs, at 400 seeds, in one resumable script.

Part Five asks how a group dies. The book already has the endpoint table
(`scenarios_hiseed.py`, notebook section 1), which reports where each failure mode finishes.
What Part Five needs and does not have is three further things:

**(a) The Tradition 3 sweep.** The default model has two T3 paths: resource governance and
inverse-practice-weighted dropout friction. The sweep varies both together. The release-gate
factorial separates them; this file preserves the combined dose-response needed by Chapter 19.

**(b) Trajectories.** Chapter 21's claim is that quality holds while the group dies, so the
endpoint table cannot show it: an endpoint is one number and the claim is about a shape. Runs
here record membership, mean practice and established-core size at every step, sampled yearly.

**(c) The composition experiment.** Three founding-state distributions have the same mean
initial practice. They also change every Step jointly within a founder and therefore change
gates, thresholds, resource supply, dropout, attraction, and initial heterogeneity exposure.
The contrast is paired and unresolved; it does not identify recruitment selection.

**Selection, and it is the threat that matters most in this part.** Quality is measured among
established members of *surviving* groups. A failure mode that kills weak groups will therefore
report higher quality among the ones left, and that is an artefact of conditioning, not a
finding. Every quality figure below is reported with the survival fraction beside it, and the
trajectory runs additionally record quality among **all** runs with deaths carried as zero, so
the conditional and unconditional versions can be compared directly. Appendix A3.4.

Every condition uses seeds 0..399 and the same random stream before paths diverge. Contrasts
are therefore paired common-random-number contrasts; uncertainty is computed on paired
differences rather than inferred from one condition's half-width.

Cached to `../research/part5.json`; resumable, atomic saves, safe to interrupt.

Run:  python3 part5_runs.py [n_workers] [batch]
"""
import hashlib, importlib.util, sys, os, json
import numpy as np
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'aa_group_model.py')
OUT = os.path.abspath(os.path.join(HERE, '..', 'research', 'part5.json'))

NSEED = 400
H = 1560                 # 30 years in half-weeks
DT = 0.5
YEAR = int(52 / DT)      # samples per year

T3_LEVELS = [0.0, 0.25, 0.50, 0.75, 1.0]
TRAJ = ['full', 't11_attraction_loss', 'referral_loss', 't3_combined_loss']
COMPOSITION = ['even', 'concentrated', 'split']


def _load():
    spec = importlib.util.spec_from_file_location('m', MODEL)
    mm = importlib.util.module_from_spec(spec)
    sys.modules['m'] = mm
    spec.loader.exec_module(mm)
    return mm


def _scen_T_P_KW(mm, scen):
    T = mm.FULL.copy(); P = {}; kw = {}
    if scen == 't11_attraction_loss':
        kw['attraction_T11'] = 0.0
    elif scen == 'referral_loss':
        P['lam_exog'] = 0.0
    elif scen == 't3_combined_loss':
        T[2] = 0.0
    elif scen != 'full':
        raise ValueError(scen)
    return T, P, kw


def _one(job):
    kind, arg, seed = job
    mm = _load()

    if kind == 't3':
        T = mm.FULL.copy(); T[2] = float(arg)
        r = mm.simulate(T, seed=seed, T_end=H)
        return dict(N=r['N'], exists=int(r['endpoint_exists']),
                    viable=int(r['endpoint_viable']), alive=int(r['endpoint_viable']),
                    est_mean=r['est_mean'], n_est=r['n_est'],
                    low_practice_fraction=r['newcomer_frac'],
                    first_nonviable_week=r['first_nonviable_week'],
                    recovered=int(r['recovered_after_first_crossing']), closed=int(r['closed']))

    if kind == 'traj':
        T, P, kw = _scen_T_P_KW(mm, arg)
        r = mm.simulate(T, P=P, seed=seed, T_end=H, record=True, **kw)
        h = r['history']
        idx = list(range(0, len(h['N']), YEAR))
        if idx[-1] != len(h['N']) - 1:
            idx.append(len(h['N']) - 1)
        return dict(N=r['N'], exists=int(r['endpoint_exists']),
                    viable=int(r['endpoint_viable']), alive=int(r['endpoint_viable']),
                    est_mean=r['est_mean'],
                    sample_weeks=[float(h['time_weeks'][i]) for i in idx],
                    yrN=[float(h['N'][i]) for i in idx],
                    yrQ_all_living=[float(h['all_member_practice'][i]) for i in idx],
                    yrQ_established=[float(h['established_practice'][i]) for i in idx],
                    yrE=[float(h['established_count'][i]) for i in idx],
                    yrLowPractice=[float(h['low_practice_fraction'][i]) for i in idx],
                    first_nonviable_week=r['first_nonviable_week'],
                    first_recovery_week=r['first_recovery_week'],
                    recovered=int(r['recovered_after_first_crossing']),
                    closure_week=r['closure_week'], closed=int(r['closed']))

    if kind == 'comp':
        # Same total initial practice, distributed three ways across 25 founders.
        # even:         every founder at 0.55
        # concentrated: five founders at 1.0, twenty at 0.4375  (mean 0.55)
        # split:        twelve at 0.9, thirteen at 0.226923...  (mean 0.55)
        n0 = 25
        if arg == 'even':
            x0 = np.full(n0, 0.55)
        elif arg == 'concentrated':
            x0 = np.concatenate([np.full(5, 1.0), np.full(20, (0.55 * n0 - 5.0) / 20)])
        else:
            x0 = np.concatenate([np.full(12, 0.9), np.full(13, (0.55 * n0 - 12 * 0.9) / 13)])
        assert np.isclose(x0.mean(), 0.55)
        r = mm.simulate(mm.FULL, seed=seed, T_end=H, dt=DT, initial_practice=x0)
        return dict(N=r['N'], exists=int(r['endpoint_exists']),
                    viable=int(r['endpoint_viable']), alive=int(r['endpoint_viable']),
                    est_mean=r['est_mean'], n_est=r['n_est'], mean=r['mean'],
                    x0_mean=float(x0.mean()), x0_sd=float(x0.std()),
                    founders_above_act=int((x0 > mm.DEFAULTS['act_thr']).sum()),
                    founders_above_exp=int((x0 > mm.DEFAULTS['exp_thr']).sum()),
                    first_nonviable_week=r['first_nonviable_week'],
                    recovered=int(r['recovered_after_first_crossing']), closed=int(r['closed']))

    raise ValueError(kind)


def _save(out):
    tmp = OUT + '.tmp'
    json.dump(out, open(tmp, 'w'))
    os.replace(tmp, OUT)


if __name__ == '__main__':
    nw = int(sys.argv[1]) if sys.argv[1:] else 4
    batch = int(sys.argv[2]) if sys.argv[2:] else 10 ** 9

    jobs = []
    for lv in T3_LEVELS:
        jobs += [('t3', lv, s) for s in range(NSEED)]
    for sc in TRAJ:
        jobs += [('traj', sc, s) for s in range(NSEED)]
    for c in COMPOSITION:
        jobs += [('comp', c, s) for s in range(NSEED)]

    model_hash=hashlib.sha256(open(MODEL,'rb').read()).hexdigest()
    script_hash=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    if (out.get('meta',{}).get('model_sha256') != model_hash or
            out.get('meta',{}).get('script_sha256') != script_hash):
        out = {}
    out['meta'] = dict(schema_version=2,status='incomplete',model_sha256=model_hash,
                       script_sha256=script_hash,script='model/part5_runs.py',
                       nseed=NSEED, seed_range=[0,NSEED-1], horizon=H, dt=DT,
                       t3_levels=T3_LEVELS, t3_sweep='governance and friction varied together',
                       traj=TRAJ, composition=COMPOSITION, jobs_expected=len(jobs),
                       year_samples=YEAR, first_sample_week=0,
                       pairing='common seed and random stream across conditions',
                       viability='endpoint N > 5; existence N > 0; N=0 closed')

    key = lambda j: f'{j[0]}|{j[1]}|{j[2]}'
    todo = [j for j in jobs if key(j) not in out][:batch]
    print(f'{len(out)-1} of {len(jobs)} done, running {len(todo)}', flush=True)
    if todo:
        n = 0
        with ProcessPoolExecutor(nw) as ex:
            for j, r in zip(todo, ex.map(_one, todo)):
                out[key(j)] = r
                n += 1
                if n % 40 == 0:
                    _save(out)
        _save(out)
    done = sum(1 for j in jobs if key(j) in out)
    out['meta']['jobs_completed']=done
    out['meta']['status']='complete' if done==len(jobs) else 'incomplete'
    _save(out)
    print(f'{done} of {len(jobs)} complete', flush=True)
    print('ALL DONE' if done == len(jobs) else 'PARTIAL', flush=True)
