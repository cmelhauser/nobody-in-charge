"""The referral-versus-attraction ordering at slower decay rates, at 400 paired seeds.

The multi-level one-at-a-time screen (`research/oat_full.json`, three common seeds per endpoint)
reverses the pure-attraction-loss minus referral-loss ordering on final membership when `delta0`
is moved down by 25, 50 or 75 per cent. This design re-estimates that ordering at 400 paired
seeds, at the default decay rate and at those three lower rates, so that a screen becomes an
estimate. It changes no released number.

Conditions, each at full Tradition adherence otherwise:

  full         both arrival channels intact
  attraction   pure T11 attraction path removed (attraction_T11 = 0); governance held at one
  referral     exogenous referral removed (lam_exog = 0)

Decay levels: `delta0` changed by 0, -25, -50 and -75 per cent. Seeds 0-399 are shared across all
twelve cells, so every contrast is paired by common random numbers. Horizon 1,560 weeks, dt 0.5.

Results cached to `../research/decay_ordering.json`; resumable.

Run:  python3 decay_ordering.py [n_workers] [batch]
"""
import hashlib, importlib.util, sys, os, json
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'aa_group_model.py')
OUT = os.path.abspath(os.path.join(HERE, '..', 'research', 'decay_ordering.json'))
LEV = [0, -25, -50, -75]
SCEN = ['full', 'attraction', 'referral']
NSEED = 400
HORIZON = 1560


def _load():
    spec = importlib.util.spec_from_file_location('m', MODEL)
    mm = importlib.util.module_from_spec(spec)
    sys.modules['m'] = mm
    spec.loader.exec_module(mm)
    return mm


def _one(job):
    """job = (decay change in per cent, scenario, seed) -> the reported outcomes."""
    pc, scen, seed = job
    mm = _load()
    P = dict(delta0=mm.DEFAULTS['delta0'] * (1 + pc / 100))
    kw = {}
    if scen == 'attraction':
        kw['attraction_T11'] = 0.0
    elif scen == 'referral':
        P['lam_exog'] = 0.0
    r = mm.simulate(mm.FULL.copy(), P=P, seed=seed, T_end=HORIZON, **kw)
    return dict(pc=pc, scen=scen, seed=seed, N=r['N'],
                exists=int(r['endpoint_exists']), viable=int(r['endpoint_viable']),
                closed=int(r['closed']), practice=r['mean'],
                maint=float(r['X'][r['alive']][:, 9:12].mean()) if r['N'] else 0.0)


def jobs():
    """The full job list, in a stable order so caching by index is safe."""
    return [(pc, scen, s) for pc in LEV for scen in SCEN for s in range(NSEED)]


def _save(out):
    tmp = OUT + '.tmp'
    json.dump(out, open(tmp, 'w'))
    os.replace(tmp, OUT)


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
                       script_sha256=script_hash, script='model/decay_ordering.py',
                       nseed=NSEED, seed_range=[0, NSEED - 1], horizon=HORIZON, dt=0.5,
                       levels=LEV, scenarios=SCEN, jobs_expected=len(J),
                       pairing='common random numbers: seeds 0-399 shared across all cells',
                       attraction_intervention='pure T11 attraction path; governance held at one',
                       referral_intervention='lam_exog = 0',
                       viability='endpoint N > 5; existence N > 0; N=0 closed')
    todo = [(i, j) for i, j in enumerate(J) if str(i) not in out][:batch]
    print(f'{sum(str(i) in out for i in range(len(J)))} of {len(J)} done, running {len(todo)}', flush=True)
    if todo:
        done = 0
        with ProcessPoolExecutor(nw) as ex:
            for (i, j), res in zip(todo, ex.map(_one, [j for _, j in todo])):
                out[str(i)] = {'job': list(j), **res}
                done += 1
                if done % 40 == 0:
                    _save(out)
        _save(out)
    done = sum(str(i) in out for i in range(len(J)))
    out['meta']['jobs_completed'] = done
    out['meta']['status'] = 'complete' if done == len(J) else 'incomplete'
    _save(out)
    print(done, 'of', len(J))
    print('ALL DONE' if done == len(J) else 'PARTIAL', flush=True)
