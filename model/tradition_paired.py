"""The twelve-Tradition degradation comparison, at 400 paired replications instead of 30.

Why this exists, and it is two problems in one cell.

Notebook section 3 degrades each Tradition alone from 0.85 to 0.50 and measures the loss in
membership at a 20-year horizon, under common random numbers so that the same seed drives the
reference run and the degraded run and the cross-seed noise differences out. Chapter 5's
Machinery reports the result.

**Problem one: it used 30 replications.** `CLAUDE.md` rule 0 says any figure from a stochastic
run needs at least 400 seeds and a stated interval, and it says so because three separate
errors in this project came from reporting statistics computed from samples too small to
support the digits printed. A paired CRN design is far more efficient than an unpaired one and
30 pairs is not obviously wrong, but "more efficient" is not "exempt", and the cell was the
last place in the project still reporting from a small sample.

**Problem two: it took longer than the notebook could run.** 13 conditions times 30 seeds was
already the slowest cell after the rotation sweep, and the notebook was never being executed
end to end, which is how a different cell came to sit broken and unnoticed. Caching the result
here lets the notebook read it in milliseconds and run start to finish.

Design. Reference is all twelve Traditions at 0.85. For each Tradition j in turn, set T[j] to
0.50 and leave the rest. Horizon 1040 half-weeks, twenty years. Common random numbers: run s of
the reference and run s of every degraded condition use seed s, so the paired difference
removes the shared noise. Reported per Tradition: the mean paired difference in final
membership, its standard error, and t. The estimand is the expected membership loss from
degrading one Tradition alone, at that reference point, at that horizon.

Cached to `../research/tradition_paired.json`; resumable.

Run:  python3 tradition_paired.py [n_workers] [batch]
"""
import hashlib, importlib.util, sys, os, json
import numpy as np
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'aa_group_model.py')
OUT = os.path.abspath(os.path.join(HERE, '..', 'research', 'tradition_paired.json'))

NSEED = 400
HZ = 1040          # twenty years, matching the cell this replaces
REF = 0.85
LOW = 0.50


def _load():
    spec = importlib.util.spec_from_file_location('m', MODEL)
    mm = importlib.util.module_from_spec(spec)
    sys.modules['m'] = mm
    spec.loader.exec_module(mm)
    return mm


def _one(job):
    """cond is -1 for the reference, else the index of the Tradition held at LOW."""
    cond, seed = job
    mm = _load()
    T = np.full(12, REF)
    if cond >= 0:
        T[cond] = LOW
    return float(mm.simulate(T, seed=seed, T_end=HZ)['N'])


def _save(out):
    tmp = OUT + '.tmp'
    json.dump(out, open(tmp, 'w'))
    os.replace(tmp, OUT)


if __name__ == '__main__':
    nw = int(sys.argv[1]) if sys.argv[1:] else 4
    batch = int(sys.argv[2]) if sys.argv[2:] else 10 ** 9
    jobs = [(c, s) for c in range(-1, 12) for s in range(NSEED)]
    model_hash=hashlib.sha256(open(MODEL,'rb').read()).hexdigest()
    script_hash=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    if (out.get('meta',{}).get('model_sha256') != model_hash or
            out.get('meta',{}).get('script_sha256') != script_hash): out={}
    out['meta'] = dict(schema_version=2,status='incomplete',model_sha256=model_hash,
                       script_sha256=script_hash,script='model/tradition_paired.py',
                       nseed=NSEED,seed_range=[0,NSEED-1],horizon=HZ,dt=0.5,
                       ref=REF,low=LOW,jobs_expected=len(jobs),
                       design='paired, common random numbers; each degraded Tradition uses all default paths')
    key = lambda j: f'{j[0]}|{j[1]}'
    todo = [j for j in jobs if key(j) not in out][:batch]
    print(f'{len(out)-1} of {len(jobs)} done, running {len(todo)}', flush=True)
    if todo:
        n = 0
        with ProcessPoolExecutor(nw) as ex:
            for j, r in zip(todo, ex.map(_one, todo)):
                out[key(j)] = r
                n += 1
                if n % 60 == 0: _save(out)
        _save(out)
    done = sum(1 for j in jobs if key(j) in out)
    out['meta']['jobs_completed']=done
    out['meta']['status']='complete' if done==len(jobs) else 'incomplete'
    print(f'{done} of {len(jobs)} complete', flush=True)
    if done == len(jobs):
        base = np.array([out[f'-1|{s}'] for s in range(NSEED)])
        res = dict(base_mean=float(base.mean()), base_sd=float(base.std(ddof=1)), rows=[])
        for j in range(12):
            deg = np.array([out[f'{j}|{s}'] for s in range(NSEED)])
            d = base - deg
            se = float(d.std(ddof=1) / np.sqrt(NSEED))
            res['rows'].append(dict(tradition=j + 1, loss=float(d.mean()), se=se,
                                    t=float(d.mean() / se) if se > 1e-12 else 0.0,
                                    lo=float(d.mean() - 1.96 * se),
                                    hi=float(d.mean() + 1.96 * se)))
        out['result'] = res
        out['meta']['status']='complete'
        _save(out)
        print('ALL DONE', flush=True)
        print(f"reference N = {res['base_mean']:.1f}, cross-seed SD = {res['base_sd']:.1f}")
        for r in sorted(res['rows'], key=lambda r: -r['loss']):
            print(f"  T{r['tradition']:<3}{r['loss']:>7.2f} +/- {1.96*r['se']:>5.2f}  t={r['t']:>6.1f}")
    else:
        print('PARTIAL', flush=True)
