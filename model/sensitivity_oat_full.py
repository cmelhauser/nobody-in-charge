"""One-at-a-time screen over the 118 registered numeric values.

The earlier OAT sweep in `sensitivity_uniform.py` covered 21 of the 118: the continuous
scalars only, excluding room capacity, and it scored a single outcome (survival of a
referral-starved group). That left 97 parameters never varied alone, including every step
speed and every cell of both matrices, and it could not say whether a claim about a
*healthy* group rested on a knife-edge.

This script varies each of the 118 alone at plus and minus 10, 25, 50 and 75 per cent,
holding everything else at default, and scores three scenarios. That is 944 registered
one-at-a-time perturbation points rather than the former 236-point star:

    full        all twelve Traditions at 1.0
    attraction  the Tradition 11 attraction path set to 0, with governance held at 1
    referral    lam_exog set to 0 (no courts, no treatment centres)

For each it records endpoint viability and existence, mean final membership, mean
practice across all twelve steps, and mean maintenance (Steps 10 to 12, which is what
Chapter 14 turns on).

Results are written incrementally to `../research/oat_full.json`, keyed by parameter id,
so an interrupted run resumes. Ids are:

    scalar:<name>     one of the 22 continuous scalars, cap included this time
    a:<i>             step speed for step i, zero-indexed
    S:<i>,<j>         non-zero cell of the step-consumption matrix
    GOV:<i>,<j>       non-zero cell of the tradition-governance matrix

Run:  python3 sensitivity_oat_full.py [n_workers]
"""
import hashlib, importlib.util, sys, os, json
import numpy as np
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'aa_group_model.py')
OUT = os.path.abspath(os.path.join(HERE, '..', 'research', 'oat_full.json'))
H, SEEDS, DELTAS = 1560, 3, (0.10, 0.25, 0.50, 0.75)


def _load():
    spec = importlib.util.spec_from_file_location('m', MODEL)
    m = importlib.util.module_from_spec(spec)
    sys.modules['m'] = m
    spec.loader.exec_module(m)
    return m


def param_ids(m):
    ids = [f'scalar:{k}' for k, v in m.DEFAULTS.items() if np.isscalar(v)]
    ids += [f'a:{i}' for i in range(len(m.DEFAULTS['a']))]
    ids += [f'S:{i},{j}' for i, j in zip(*np.nonzero(m.S))]
    ids += [f'GOV:{i},{j}' for i, j in zip(*np.nonzero(m.GOV))]
    return ids


def _rederive(m):
    m.GOVW[:] = m.GOV / np.maximum(m.GOV.sum(0, keepdims=True), 1e-12)
    m.BETA[:] = m.S.sum(1) / m.S.sum(1).max()
    m.Snorm[:] = m.S / m.S.sum(1, keepdims=True)


def _apply(m, pid, mult):
    """Return the P override dict, having mutated matrices in place where needed."""
    kind, rest = pid.split(':', 1)
    P = {}
    if kind == 'scalar':
        v = m.DEFAULTS[rest] * mult
        if rest == 'cap':
            v = max(int(round(v)), 5)
        P[rest] = v
    elif kind == 'a':
        a = m.DEFAULTS['a'].copy()
        a[int(rest)] *= mult
        P['a'] = a
    else:
        i, j = (int(x) for x in rest.split(','))
        M = m.S if kind == 'S' else m.GOV
        M[i, j] *= mult
        _rederive(m)
    return P


def _scenarios(m, P):
    out = {}
    for name, T, extra, kw in (('full', m.FULL, {}, {}),
                               ('attraction', m.FULL, {}, {'attraction_T11': 0.0}),
                               ('referral', m.FULL, {'lam_exog': 0.0}, {})):
        Pf = {**P, **extra}
        runs = [m.simulate(T, P=Pf, seed=s, T_end=H, **kw) for s in range(SEEDS)]
        ok = [r for r in runs if r['endpoint_viable']]
        out[name] = dict(
            surv=len(ok) / SEEDS,  # legacy key: endpoint viability, not an absorbing event
            exists=float(np.mean([r['endpoint_exists'] for r in runs])),
            N=float(np.mean([r['N'] for r in runs])),
            N_viable=float(np.mean([r['N'] for r in ok])) if ok else 0.0,
            practice=float(np.mean([r['mean'] for r in runs])),
            practice_viable=float(np.mean([r['mean'] for r in ok])) if ok else 0.0,
            maint=float(np.mean([
                r['X'][r['alive']][:, 9:12].mean() if r['N'] else 0.0 for r in runs])),
        )
    return out


def one(pid):
    """Worker. Rebuilds the model from source so nothing leaks between parameters."""
    m = _load()
    res = {}
    for delta in DELTAS:
        for direction, mult in (('minus', 1 - delta), ('plus', 1 + delta)):
            tag = f'{direction}_{int(round(delta * 100))}'
            m2 = _load()
            res[tag] = _scenarios(m2, _apply(m2, pid, mult))
    return pid, res


def baseline():
    m = _load()
    return _scenarios(m, {})


def _save(out):
    tmp = OUT + '.tmp'
    json.dump(out, open(tmp, 'w'))
    os.replace(tmp, OUT)          # atomic, so an interrupted run cannot corrupt the file


if __name__ == '__main__':
    nw = int(sys.argv[1]) if sys.argv[1:] else 4
    batch = int(sys.argv[2]) if sys.argv[2:] else 10**9
    model_hash = hashlib.sha256(open(MODEL, 'rb').read()).hexdigest()
    script_hash = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    if (out.get('meta', {}).get('model_sha256') != model_hash or
            out.get('meta', {}).get('script_sha256') != script_hash):
        out = {}
    m = _load()
    ids = param_ids(m)
    assert len(ids) == 118, f'expected 118 parameters, got {len(ids)}'
    out['meta'] = dict(schema_version=2, status='incomplete', model_sha256=model_hash,
                       script_sha256=script_hash, script='model/sensitivity_oat_full.py',
                       registered_values=118, decomposition='22 scalar + 12 a + 49 S + 35 GOV',
                       seeds=SEEDS, seed_range=[0,SEEDS-1], horizon=H, dt=0.5,
                       deltas=list(DELTAS), perturbations_expected=118*2*len(DELTAS),
                       role='multi-level one-at-a-time screening; three seeds per endpoint',
                       attraction_intervention='pure T11 attraction path; governance held at one',
                       conditioning='N and practice are all-run; *_viable conditions on endpoint N > 5')
    if 'baseline' not in out:
        out['baseline'] = baseline()
        _save(out)
    todo = [p for p in ids if p not in out][:batch]
    print(f'{sum(1 for p in ids if p in out)} of 118 done, running {len(todo)} now', flush=True)
    if todo:
        with ProcessPoolExecutor(nw) as ex:
            for pid, res in ex.map(one, todo):
                out[pid] = res
                _save(out)
    n = sum(1 for p in ids if p in out)
    out['meta']['parameter_jobs_completed'] = n
    out['meta']['perturbations_completed'] = n*2*len(DELTAS)
    out['meta']['status'] = 'complete' if n == 118 else 'incomplete'
    _save(out)
    print(f'{n} of 118 complete', flush=True)
    print('ALL DONE' if n == 118 else 'PARTIAL', flush=True)
