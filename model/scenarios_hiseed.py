"""Core decline scenarios at 400 paired seeds, with distinct mechanism paths.

The book's decline table was computed from 10 seeds. The cross-seed standard deviation of
final membership is about 15 members against a mean near 42, so a 10-seed mean carries a
standard error near 5 and a 10-seed survival fraction is quantised to tenths. Both are far
coarser than the three significant figures the book prints.

This script recomputes the same table at 400 seeds, using the same definitions as the
notebook's section 1 so the two are directly comparable:

    survival   fraction of runs ending with more than 5 members
    N          mean final membership over ALL runs, deaths counted as zero
    quality    mean practice among established members, over surviving runs only

and adds a standard error or Wilson interval to each.

Cached to `../research/scenarios_hiseed.json`; resumable.

Run:  python3 scenarios_hiseed.py [n_workers] [batch]
"""
import hashlib, importlib.util, sys, os, json
import numpy as np
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'aa_group_model.py')
OUT = os.path.abspath(os.path.join(HERE, '..', 'research', 'scenarios_hiseed.json'))
RELEASE = os.path.abspath(os.path.join(HERE, '..', 'research', 'release_gate_results.json'))
NSEED = 400
H = 1560

SCEN = ['full', 't11_attraction', 't11_mixed', 'referral',
        'referral_and_t11_attraction', 't3_combined']


def _load():
    spec = importlib.util.spec_from_file_location('m', MODEL)
    mm = importlib.util.module_from_spec(spec)
    sys.modules['m'] = mm
    spec.loader.exec_module(mm)
    return mm


def _one(job):
    scen, seed = job
    mm = _load()
    T = mm.FULL.copy()
    P = {}
    kw = {}
    if scen in ('t11_attraction', 'referral_and_t11_attraction'):
        kw['attraction_T11'] = 0.0        # clean attraction path only
    if scen == 't11_mixed':
        T[10] = 0.0                       # governance and attraction together
    if scen in ('referral', 'referral_and_t11_attraction'):
        P['lam_exog'] = 0.0               # no courts, no treatment centres
    if scen == 't3_combined':
        T[2] = 0.0                        # governance and friction together
    r = mm.simulate(T, P=P, seed=seed, T_end=H, **kw)
    return dict(scen=scen, seed=seed, N=r['N'], exists=int(r['endpoint_exists']),
                viable=int(r['endpoint_viable']), alive=int(r['endpoint_viable']),
                est_mean=r['est_mean'], practice=r['mean'], n_est=r['n_est'],
                low_practice_fraction=r['newcomer_frac'],
                first_nonviable_week=r['first_nonviable_week'],
                recovered=int(r['recovered_after_first_crossing']), closed=int(r['closed']))


def _save(out):
    tmp = OUT + '.tmp'
    json.dump(out, open(tmp, 'w'))
    os.replace(tmp, OUT)


def jobs():
    return [(s, i) for s in SCEN for i in range(NSEED)]


if __name__ == '__main__':
    nw = int(sys.argv[1]) if sys.argv[1:] else 4
    batch = int(sys.argv[2]) if sys.argv[2:] else 10**9
    model_hash=hashlib.sha256(open(MODEL,'rb').read()).hexdigest()
    script_hash=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    if (out.get('meta',{}).get('model_sha256') != model_hash or
            out.get('meta',{}).get('script_sha256') != script_hash):
        out = {}
    J = jobs()
    out['meta']=dict(schema_version=2,status='incomplete',model_sha256=model_hash,
                     script_sha256=script_hash,script='model/scenarios_hiseed.py',
                     nseed=NSEED,seed_range=[0,NSEED-1],horizon=H,dt=0.5,
                     conditions=SCEN,jobs_expected=len(J),
                     pairing='common seed and random stream across conditions',
                     viability='endpoint N > 5; existence N > 0; N=0 closed')
    # Reuse rows already computed by the larger mechanism-factorial analysis.
    # The release cache lacks established-member counts, so that unused field is
    # recorded as null rather than simulated again under a second authority.
    if os.path.exists(RELEASE):
        rel=json.load(open(RELEASE)); rm=rel.get('meta',{})
        if rm.get('status')=='complete' and rm.get('model_sha256')==model_hash:
            mapping={'full':'base','t11_attraction':'t11_attraction_loss',
                     't11_mixed':'t11_combined_loss','t3_combined':'t3_combined_loss'}
            for scen,cond in mapping.items():
                offset=SCEN.index(scen)*NSEED
                for seed in range(NSEED):
                    rr=rel[f'{cond}|{seed}']
                    out[str(offset+seed)]=dict(
                        scen=scen,seed=seed,N=rr['N'],exists=rr['endpoint_exists'],
                        viable=rr['endpoint_viable'],alive=rr['endpoint_viable'],
                        est_mean=rr['established_practice'],practice=rr['mean_practice'],
                        n_est=None,low_practice_fraction=rr['low_practice_fraction'],
                        first_nonviable_week=rr['first_nonviable_week'],
                        recovered=rr['recovered_after_first_crossing'],closed=rr['closed'])
            out['meta']['derived_from_release_gate_sha256']=hashlib.sha256(open(RELEASE,'rb').read()).hexdigest()
    todo = [(i, j) for i, j in enumerate(J) if str(i) not in out][:batch]
    print(f'{sum(str(i) in out for i in range(len(J)))} of {len(J)} done, running {len(todo)}', flush=True)
    if todo:
        n = 0
        with ProcessPoolExecutor(nw) as ex:
            for (i, j), res in zip(todo, ex.map(_one, [j for _, j in todo])):
                out[str(i)] = res
                n += 1
                if n % 40 == 0:
                    _save(out)
        _save(out)
    done=sum(str(i) in out for i in range(len(J)))
    out['meta']['jobs_completed']=done
    out['meta']['status']='complete' if done==len(J) else 'incomplete'
    _save(out)
    print(f'{done} of {len(J)} complete', flush=True)
    print('ALL DONE' if done == len(J) else 'PARTIAL', flush=True)
