"""Chapter 15: Step 12 and recipient-opportunity mechanisms, at 400 paired seeds.

Three configurations, all at full Tradition adherence:
  base                     the model as specified
  no12                     Step 12 growth is disabled
  recipient_unconstrained  recipient capacity is forced to one

The last comparison is a clean one-mechanism override: S, Snorm, BETA, governance,
and every other resource remain unchanged. Conditions share seed and random stream,
so contrasts are paired.
"""
import hashlib, importlib.util, sys, os, json
import numpy as np
from concurrent.futures import ProcessPoolExecutor
HERE=os.path.dirname(os.path.abspath(__file__)); MODEL=os.path.join(HERE,'aa_group_model.py')
OUT=os.path.abspath(os.path.join(HERE,'..','research','ch15_service.json'))
NSEED=400; H=1560
def _load():
    sp=importlib.util.spec_from_file_location('m',MODEL); mm=importlib.util.module_from_spec(sp)
    sys.modules['m']=mm; sp.loader.exec_module(mm); return mm
def _one(j):
    cfg,s=j; mm=_load(); P={}
    if cfg=='no12':
        a=mm.DEFAULTS['a'].copy(); a[11]=0.0; P['a']=a
    kw={'recipient_override': 1.0} if cfg=='recipient_unconstrained' else {}
    r=mm.simulate(mm.FULL,P=P,seed=s,T_end=H,**kw)
    X,al=r['X'],r['alive']
    return dict(cfg=cfg,seed=s,N=r['N'],exists=int(r['endpoint_exists']),
                viable=int(r['endpoint_viable']), practice=r['mean'],
                est=r['n_est'],
                s12=float(X[al][:,11].mean()) if r['N'] else 0.0,
                s9=float(X[al][:,8].mean()) if r['N'] else 0.0,
                s1=float(X[al][:,0].mean()) if r['N'] else 0.0,
                maint=float(X[al][:,9:12].mean()) if r['N'] else 0.0,
                low_practice_fraction=r['newcomer_frac'],
                first_nonviable_week=r['first_nonviable_week'],
                recovered=int(r['recovered_after_first_crossing']), closed=int(r['closed']))
def _save(o):
    t=OUT+'.tmp'; json.dump(o,open(t,'w')); os.replace(t,OUT)
if __name__=='__main__':
    nw=int(sys.argv[1]) if sys.argv[1:] else 4
    b=int(sys.argv[2]) if sys.argv[2:] else 10**9
    model_hash=hashlib.sha256(open(MODEL,'rb').read()).hexdigest()
    script_hash=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
    out=json.load(open(OUT)) if os.path.exists(OUT) else {}
    if (out.get('meta',{}).get('model_sha256') != model_hash or
            out.get('meta',{}).get('script_sha256') != script_hash):
        out={}
    cfgs=('base','no12','recipient_unconstrained')
    J=[(c,s) for c in cfgs for s in range(NSEED)]
    out['meta']=dict(schema_version=2,status='incomplete',model_sha256=model_hash,
                     script_sha256=script_hash,script='model/ch15_service.py',
                     nseed=NSEED,seed_range=[0,NSEED-1],horizon=H,dt=0.5,
                     conditions=list(cfgs),jobs_expected=len(J),
                     pairing='common seed and random stream across conditions',
                     viability='endpoint N > 5; existence N > 0; N=0 closed')
    todo=[(i,j) for i,j in enumerate(J) if str(i) not in out][:b]
    print(f'{sum(str(i) in out for i in range(len(J)))} of {len(J)}, running {len(todo)}',flush=True)
    if todo:
        n=0
        with ProcessPoolExecutor(nw) as ex:
            for (i,j),res in zip(todo,ex.map(_one,[j for _,j in todo])):
                out[str(i)]=res; n+=1
                if n%40==0: _save(out)
        _save(out)
    done=sum(str(i) in out for i in range(len(J)))
    out['meta']['jobs_completed']=done
    out['meta']['status']='complete' if done==len(J) else 'incomplete'
    _save(out)
    print(done,'of',len(J)); print('ALL DONE' if done==len(J) else 'PARTIAL',flush=True)
