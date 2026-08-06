"""Chapter 14's decay-rate sweep at 400 seeds instead of 10."""
import hashlib, importlib.util, sys, os, json
import numpy as np
from concurrent.futures import ProcessPoolExecutor
HERE=os.path.dirname(os.path.abspath(__file__)); MODEL=os.path.join(HERE,'aa_group_model.py')
OUT=os.path.abspath(os.path.join(HERE,'..','research','ch14_sweep.json'))
LEV=[-30,-20,-10,0,5,10,30,50]; NSEED=400
def _load():
    sp=importlib.util.spec_from_file_location('m',MODEL); mm=importlib.util.module_from_spec(sp)
    sys.modules['m']=mm; sp.loader.exec_module(mm); return mm
def _one(j):
    pc,s=j; mm=_load()
    r=mm.simulate(mm.FULL,P=dict(delta0=mm.DEFAULTS['delta0']*(1+pc/100)),seed=s,T_end=1560)
    return dict(pc=pc,seed=s,N=r['N'],alive=int(r['endpoint_viable']),
                exists=int(r['endpoint_exists']),viable=int(r['endpoint_viable']),
                closed=int(r['closed']),
                maint=float(r['X'][r['alive']][:,9:12].mean()) if r['N'] else 0.0)
def _save(o):
    t=OUT+'.tmp'; json.dump(o,open(t,'w')); os.replace(t,OUT)
if __name__=='__main__':
    nw=int(sys.argv[1]) if sys.argv[1:] else 4
    b=int(sys.argv[2]) if sys.argv[2:] else 10**9
    model_hash=hashlib.sha256(open(MODEL,'rb').read()).hexdigest()
    script_hash=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
    out=json.load(open(OUT)) if os.path.exists(OUT) else {}
    if (out.get('meta',{}).get('model_sha256') != model_hash or
            out.get('meta',{}).get('script_sha256') != script_hash): out={}
    J=[(pc,s) for pc in LEV for s in range(NSEED)]
    out['meta']=dict(schema_version=2,status='incomplete',model_sha256=model_hash,
                     script_sha256=script_hash,script='model/ch14_sweep.py',
                     nseed=NSEED,seed_range=[0,NSEED-1],horizon=1560,dt=0.5,
                     levels=LEV,jobs_expected=len(J),
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
    out['meta']['jobs_completed']=done; out['meta']['status']='complete' if done==len(J) else 'incomplete'
    _save(out)
    print(done,'of',len(J)); print('ALL DONE' if done==len(J) else 'PARTIAL',flush=True)
