#!/usr/bin/env python3
"""Ω-PLASMA-001 synthetic simulator.
Frozen model for preregistered production runs.
"""
import argparse, csv, hashlib, json
import numpy as np

N=25; T=1000; DELETE_T=500
DT=0.01; NOISE=0.0015
R0=0.70; CORE=0.25; SIGMA=0.35
ADAPT=0.18; DECAY=0.015; SPRING=0.22; REPULSION=0.45; CONFINEMENT=0.035
VACANCY_THRESHOLD=0.25; LAMBDA2_THRESHOLD=0.01; WINDOW_FRACTION=0.80

def run(seed):
    rng=np.random.default_rng(seed)
    x=rng.normal(0,0.5,(N,2))
    W=np.exp(-np.sum((x[:,None,:]-x[None,:,:])**2,axis=2)/(2*0.9**2))
    np.fill_diagonal(W,0)
    deleted_pos=None; rows=[]
    for t in range(T):
        valid=np.isfinite(x[:,0])
        if t==DELETE_T:
            center=np.mean(x[valid],axis=0)
            removed=int(np.argmin(np.linalg.norm(x-center,axis=1)))
            deleted_pos=x[removed].copy()
            x[removed]=np.nan; W[removed,:]=0; W[:,removed]=0
            valid[removed]=False
        ids=np.where(valid)[0]; xi=x[ids]
        dv=xi[None,:,:]-xi[:,None,:]
        D=np.linalg.norm(dv,axis=2)+1e-9
        A=W[np.ix_(ids,ids)]
        f=-SPRING*A*(D-R0)+(D<CORE)*REPULSION*(CORE-D)
        np.fill_diagonal(f,0)
        F=np.sum(f[:,:,None]*dv/D[:,:,None],axis=1)-CONFINEMENT*xi
        norms=np.linalg.norm(F,axis=1)
        F*=np.minimum(1,norms/0.25)[:,None]/(norms[:,None]+1e-12)
        x[ids]+=DT*F+np.sqrt(DT)*NOISE*rng.normal(size=(len(ids),2))
        x[ids]=np.clip(x[ids],-3,3)
        target=np.exp(-((D-R0)/SIGMA)**2)
        np.fill_diagonal(target,0)
        W[np.ix_(ids,ids)] += DT*(ADAPT*(target-A)-DECAY*A)
        W=np.clip((W+W.T)/2,0,1); np.fill_diagonal(W,0)
        if t>=DELETE_T and t%10==0:
            md=float(np.min(np.linalg.norm(x[ids]-deleted_pos,axis=1)))
            L=np.diag(A.sum(1))-A
            lam2=float(np.linalg.eigvalsh(L)[1])
            rows.append((t,md,lam2))
    a=np.asarray(rows)
    vacancy_fraction=float(np.mean(a[:,1]>=VACANCY_THRESHOLD))
    connectivity_fraction=float(np.mean(a[:,2]>=LAMBDA2_THRESHOLD))
    passed=(vacancy_fraction>=WINDOW_FRACTION and connectivity_fraction>=WINDOW_FRACTION)
    return dict(seed=seed,vacancy_fraction=vacancy_fraction,connectivity_fraction=connectivity_fraction,
                final_distance=float(a[-1,1]),final_lambda2=float(a[-1,2]),passed=passed)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--seeds",default="0:20")
    p.add_argument("--output",default="results.csv")
    args=p.parse_args()
    lo,hi=map(int,args.seeds.split(":"))
    rows=[run(s) for s in range(lo,hi)]
    with open(args.output,"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(json.dumps({"runs":len(rows),"passes":sum(r["passed"] for r in rows),
                      "pass_rate":sum(r["passed"] for r in rows)/len(rows)}))

if __name__=="__main__":
    main()
