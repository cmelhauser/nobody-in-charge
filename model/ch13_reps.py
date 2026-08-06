"""Chapter 13's proxy-averaging exercise, replicated.

This is not a latent-variable identification design. The four regressors are supplied
without error and only the output receives one or three noisy proxies. It tests the
modest claim that rescaling and averaging output proxies can improve resolution when
the regressors and loadings are oracle-known. It does not establish a requirement for
three instruments per latent, solve measurement error in regressors, or address
endogenous group input.
"""
import hashlib, numpy as np, json, os, sys
from concurrent.futures import ProcessPoolExecutor
OUT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','research','ch13_reps.json'))
GAM=np.array([.30,.30,.25,.15]); REPS=400; TRUE=[-4.,-1.,0.,0.5]
def ces(x,g,rho):
    x=np.asarray(x,float); g=np.asarray(g,float)
    if abs(rho)<1e-8: return float(np.prod(x**g))
    if rho<-60: return float(x.min())
    with np.errstate(divide='ignore',invalid='ignore'): return float((g@(x**rho))**(1/rho))
def panel(rt,rng,n=1200,npx=3,noise=.35):
    xo,xp,G,M=(rng.uniform(.1,.95,n) for _ in range(4))
    y=np.array([ces([xo[i],xp[i],G[i],M[i]],GAM,rt) for i in range(n)])
    lam=np.linspace(.8,1.2,npx)
    return (xo,xp,G,M),np.array([l*np.log(y)+noise*rng.standard_normal(n) for l in lam]),lam
def est(inp,Z,lam):
    sc=(Z/lam[:,None]).mean(0)
    X=np.column_stack(inp)
    grid=np.linspace(-8,.95,300)
    # Vectorized CES predictions for all rho values. The grid does not contain
    # zero exactly; the stable exp/log form avoids the former Python inner loop.
    with np.errstate(over='ignore',under='ignore',divide='ignore',invalid='ignore'):
        sums=np.sum(GAM[None,None,:]*np.exp(grid[:,None,None]*np.log(X)[None,:,:]),axis=2)
        pred=np.log(sums)/grid[:,None]
    pc=pred-pred.mean(axis=1,keepdims=True)
    yc=sc-sc.mean()
    var=np.sum(pc*pc,axis=1)
    cov=pc@yc
    sse=np.sum(yc*yc)-np.divide(cov*cov,var,out=np.zeros_like(var),where=var>0)
    return float(grid[int(np.nanargmin(sse))])
def _one(j):
    rt,rep,npx=j; rng=np.random.default_rng(abs(1000*rep+int(rt*10)+npx)+7)
    return dict(rt=rt,rep=rep,npx=npx,est=float(est(*panel(rt,rng,npx=npx))))
def _save(o):
    t=OUT+'.tmp'; json.dump(o,open(t,'w')); os.replace(t,OUT)
if __name__=='__main__':
    nw=int(sys.argv[1]) if sys.argv[1:] else 4
    b=int(sys.argv[2]) if sys.argv[2:] else 10**9
    script_hash=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
    old=json.load(open(OUT)) if os.path.exists(OUT) else {}
    # Migrate the former numeric-index cache to stable estimand keys. This lets
    # the 400 completed replications per cell remain valid when the registered
    # design expands to 1,000; only replications 400..999 are new work.
    out={}
    for k,v in old.items():
        if k == 'meta' or not isinstance(v,dict) or not {'rt','rep','npx','est'} <= set(v):
            continue
        out[f"{v['rt']}|{v['npx']}|{v['rep']}"]=v
    J=[(rt,rep,npx) for rt in TRUE for npx in (1,3) for rep in range(REPS)]
    out['meta']=dict(schema_version=2,status='incomplete',script_sha256=script_hash,
                     reps=REPS,true_rho=TRUE,proxy_counts=[1,3],panel_n=1200,
                     jobs_expected=len(J),role='proxy-averaging demonstration',
                     limitations='oracle-known regressors and loadings; noise only in output proxies')
    key=lambda j:f'{j[0]}|{j[2]}|{j[1]}'
    todo=[j for j in J if key(j) not in out][:b]
    print(f'{sum(key(j) in out for j in J)} of {len(J)}, running {len(todo)}',flush=True)
    if todo:
        n=0
        with ProcessPoolExecutor(nw) as ex:
            for j,res in zip(todo,ex.map(_one,todo)):
                out[key(j)]=res; n+=1
                if n%10==0: _save(out)
        _save(out)
    done=sum(key(j) in out for j in J)
    out['meta']['jobs_completed']=done; out['meta']['status']='complete' if done==len(J) else 'incomplete'
    _save(out)
    print(done,'of',len(J)); print('ALL DONE' if done==len(J) else 'PARTIAL',flush=True)
