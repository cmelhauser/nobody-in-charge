"""Monte Carlo error budget for the group simulation.

Everything the book quotes from the simulation is a mean over seeds, and final membership
varies substantially across random streams. The number of seeds is therefore a first-order
question; this script measures the uncertainty rather than assuming its old magnitude.

Three things are measured:

  seeds     how the standard error of each reported quantity falls with seed count, and
            how many seeds are needed to pin each to the precision the book prints
  dt        whether the Euler step of 0.5 half-weeks is converged, tested at matched
            seed counts so the comparison is not swamped by Monte Carlo noise
  horizon   a paired finite-horizon comparison; it does not prove a steady state

Results cached to `../research/mc_error.json`; resumable.

Run:  python3 mc_error.py [n_workers] [batch]
"""
import hashlib, importlib.util, sys, os, json
import numpy as np
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'aa_group_model.py')
OUT = os.path.abspath(os.path.join(HERE, '..', 'research', 'mc_error.json'))


def _load():
    spec = importlib.util.spec_from_file_location('m', MODEL)
    mm = importlib.util.module_from_spec(spec)
    sys.modules['m'] = mm
    spec.loader.exec_module(mm)
    return mm


def _one(job):
    """job = (scenario, dt, horizon, seed) -> the four reported outcomes."""
    scen, dt, H, seed = job
    mm = _load()
    T = mm.FULL.copy()
    P = {}
    kw = {}
    if scen == 'attraction':
        kw['attraction_T11'] = 0.0
    elif scen == 'referral':
        P['lam_exog'] = 0.0
    r = mm.simulate(T, P=P, seed=seed, T_end=H, dt=dt, **kw)
    return dict(seed=seed, alive=int(r['endpoint_viable']),
                exists=int(r['endpoint_exists']), viable=int(r['endpoint_viable']),
                closed=int(r['closed']), N=r['N'], practice=r['mean'],
                maint=float(r['X'][r['alive']][:, 9:12].mean()) if r['N'] else 0.0,
                est=r['n_est'], first_nonviable_week=r['first_nonviable_week'],
                recovered=int(r['recovered_after_first_crossing']))


def _save(out):
    tmp = OUT + '.tmp'
    json.dump(out, open(tmp, 'w'))
    os.replace(tmp, OUT)


def jobs():
    """The full job list, in a stable order so caching by index is safe."""
    J = []
    # A. 400 seeds at the default settings, for each scenario
    for scen in ('full', 'attraction', 'referral'):
        for s in range(400):
            J.append((scen, 0.5, 1560, s))
    # B. integration step, 200 seeds each, full adherence
    for dt in (1.0, 0.25, 0.125):
        for s in range(200):
            J.append(('full', dt, 1560, s))
    # C. horizon, 200 seeds each
    for H in (520, 1040, 2600, 5200):
        for s in range(200):
            J.append(('full', 0.5, H, s))
    return J


if __name__ == '__main__':
    nw = int(sys.argv[1]) if sys.argv[1:] else 4
    batch = int(sys.argv[2]) if sys.argv[2:] else 10**9
    model_hash = hashlib.sha256(open(MODEL, 'rb').read()).hexdigest()
    script_hash = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    if (out.get('meta', {}).get('model_sha256') != model_hash or
            out.get('meta', {}).get('script_sha256') != script_hash):
        out = {}
    J = jobs()
    out['meta'] = dict(schema_version=2, status='incomplete', model_sha256=model_hash,
                       script_sha256=script_hash, script='model/mc_error.py',
                       jobs_expected=len(J), horizon_jobs='200 paired seeds at each horizon',
                       seed_blocks='0-399 scenarios; 0-199 integration and horizons',
                       attraction_intervention='pure T11 attraction path; governance held at one',
                       viability='endpoint N > 5; existence N > 0; N=0 closed')
    todo = [(i, j) for i, j in enumerate(J) if str(i) not in out][:batch]
    print(f'{sum(str(i) in out for i in range(len(J)))} of {len(J)} done, running {len(todo)}', flush=True)
    if todo:
        done = 0
        with ProcessPoolExecutor(nw) as ex:
            for (i, j), res in zip(todo, ex.map(_one, [j for _, j in todo])):
                out[str(i)] = {'job': list(j), **res}
                done += 1
                if done % 40 == 0:          # checkpoint often; the runner is time-limited
                    _save(out)
        _save(out)
    done=sum(str(i) in out for i in range(len(J)))
    out['meta']['jobs_completed']=done
    out['meta']['status']='complete' if done==len(J) else 'incomplete'
    _save(out)
    print(f'{done} of {len(J)} complete', flush=True)
    print('ALL DONE' if done == len(J) else 'PARTIAL', flush=True)
