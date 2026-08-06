"""The two membership thresholds, computed at 400 seeds, because the book was using one
word for both of them.

Why this exists. `aa_group_model.py` carries two thresholds on a member's mean practice:

    act_thr = 0.1   an ESTABLISHED member. This is what `simulate()` returns as `n_est`,
                    and it is what the Part Five tables have been printing under the
                    heading "core".
    exp_thr = 0.5   an EXPERIENCED member. This is what appendix A6 and Chapter 4 mean by
                    "an established core near nine." Whether the corrected model still
                    meets that target is an output of this run, not an assumption.

Those are different quantities differing by a factor of four, and until 2 August 2026 the
book used the word "core" for both. Notebook cell 4 was written to check the second and had
never run, because it referenced an undefined name and produced no output, which no checker
caught: the status check looks for stored failures and an empty output is not one.

This script computes both at 400 seeds with Monte Carlo error so the two can be named
separately and each can be asserted. It also records the full membership count so the
calibration statement can be checked as a whole rather than in halves.

Cached to `../research/core_thresholds.json`; resumable.

Run:  python3 core_thresholds.py [n_workers] [batch]
"""
import hashlib, importlib.util, sys, os, json
import numpy as np
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'aa_group_model.py')
OUT = os.path.abspath(os.path.join(HERE, '..', 'research', 'core_thresholds.json'))
NSEED = 400
H = 1560


def _load():
    spec = importlib.util.spec_from_file_location('m', MODEL)
    mm = importlib.util.module_from_spec(spec)
    sys.modules['m'] = mm
    spec.loader.exec_module(mm)
    return mm


def _one(seed):
    mm = _load()
    r = mm.simulate(mm.FULL, seed=seed, T_end=H)
    if r['N'] == 0:
        return dict(N=0, alive=0, exists=0, viable=0, established=0, experienced=0)
    lv = r['X'][r['alive']].mean(axis=1)
    return dict(N=int(r['N']), alive=int(r['endpoint_viable']),
                exists=int(r['endpoint_exists']), viable=int(r['endpoint_viable']),
                established=int((lv > mm.DEFAULTS['act_thr']).sum()),
                experienced=int((lv > mm.DEFAULTS['exp_thr']).sum()))


def _save(out):
    tmp = OUT + '.tmp'
    json.dump(out, open(tmp, 'w'))
    os.replace(tmp, OUT)


if __name__ == '__main__':
    nw = int(sys.argv[1]) if sys.argv[1:] else 4
    batch = int(sys.argv[2]) if sys.argv[2:] else 10 ** 9
    model_hash=hashlib.sha256(open(MODEL,'rb').read()).hexdigest()
    script_hash=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    if (out.get('meta',{}).get('model_sha256') != model_hash or
            out.get('meta',{}).get('script_sha256') != script_hash): out={}
    mm = _load()
    out['meta'] = dict(schema_version=2,status='incomplete',model_sha256=model_hash,
                       script_sha256=script_hash,script='model/core_thresholds.py',
                       nseed=NSEED,seed_range=[0,NSEED-1],horizon=H,dt=0.5,
                       jobs_expected=NSEED,act_thr=mm.DEFAULTS['act_thr'],
                       exp_thr=mm.DEFAULTS['exp_thr'],
                       viability='endpoint N > 5; existence N > 0; N=0 closed')
    todo = [s for s in range(NSEED) if str(s) not in out][:batch]
    print(f'{len(out)-1} of {NSEED} done, running {len(todo)}', flush=True)
    if todo:
        n = 0
        with ProcessPoolExecutor(nw) as ex:
            for s, r in zip(todo, ex.map(_one, todo)):
                out[str(s)] = r
                n += 1
                if n % 40 == 0: _save(out)
        _save(out)
    done = sum(1 for s in range(NSEED) if str(s) in out)
    print(f'{done} of {NSEED} complete', flush=True)
    if done == NSEED:
        rows = [out[str(s)] for s in range(NSEED)]
        alive = [r for r in rows if r['alive']]
        f = lambda k, src: (float(np.mean([r[k] for r in src])),
                            float(1.96 * np.std([r[k] for r in src], ddof=1) / np.sqrt(len(src))))
        out['result'] = dict(
            n_alive=len(alive), survival=len(alive) / NSEED,
            N=f('N', rows), N_alive=f('N', alive),
            established=f('established', alive), experienced=f('experienced', alive))
        _save(out)
        out['meta']['jobs_completed']=done; out['meta']['status']='complete'
        _save(out)
        print('ALL DONE', flush=True)
        r = out['result']
        print(f"  survival {r['survival']:.3f}  N(all) {r['N'][0]:.1f}+-{r['N'][1]:.1f}  "
              f"N(alive) {r['N_alive'][0]:.1f}+-{r['N_alive'][1]:.1f}")
        print(f"  established (>{out['meta']['act_thr']}) {r['established'][0]:.1f}+-{r['established'][1]:.1f}")
        print(f"  experienced (>{out['meta']['exp_thr']}) {r['experienced'][0]:.1f}+-{r['experienced'][1]:.1f}")
    else:
        print('PARTIAL', flush=True)
