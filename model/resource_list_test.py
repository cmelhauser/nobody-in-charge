"""The fourth structural choice: does the resource list have to have eight entries?

Appendix A5.6 lists four structural choices that were never perturbed. A9 perturbed three of
them. This is the fourth, and it was left because changing the number of resources changes the
column count of both matrices and looked like a different model rather than a variant.

It is not, for the coupling. The coupling B = S G' is exact algebra on two matrices whose
columns are resources, and dropping or merging a column is a well-defined operation on both at
once. What cannot be done without fresh judgement is *splitting* a resource or inventing a new
one, and that limitation is stated in the result rather than worked around.

Three designs, all deterministic.

  leave-one-out   Delete resource r from both matrices, 8 variants. Asks whether any single
                  resource is carrying a Part Four result on its own.
  pairwise merge  Replace resources r and s by their sum in both matrices, 28 variants. Asks
                  whether the eight-way split is finer than it needs to be. Summing is the
                  right operation: if two resources were really one, a Step consuming 0.3 of
                  each consumes 0.6 of the merged thing, and a Tradition governing both
                  governs the merged thing at the sum of its coefficients.
  drop-two        Delete two resources at once, 28 variants, as a harder version of the first.

For each variant, the three Part Four claims are re-tested:

  A  index-pairing fails for all twelve Steps
  B  Tradition 1 has the largest column sum
  C  the five protective Traditions still have zero columns

**Claim C is invariant by construction and is reported as such rather than as a result.** The
protective rows of G are zero across every resource, so deleting or merging columns cannot make
them non-zero. That is the same vacuity A5.4 records for the multiplicative designs, and the
threshold test in A5.4b remains the only design in the project that can reach it.

Cached to `../research/resource_list.json`. Runs in under a second.

Run:  python3 resource_list_test.py
"""
import hashlib, importlib.util, itertools, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'aa_group_model.py')
OUT = os.path.abspath(os.path.join(HERE, '..', 'research', 'resource_list.json'))


def _load():
    spec = importlib.util.spec_from_file_location('m', MODEL)
    mm = importlib.util.module_from_spec(spec)
    sys.modules['m'] = mm
    spec.loader.exec_module(mm)
    return mm


def claims(S, G):
    """The three Part Four claims, evaluated on a given pair of matrices."""
    B = S @ G.T
    top_sets = [[int(j)+1 for j in np.flatnonzero(np.isclose(row, row.max()))] for row in B]
    own_ranks = [int(1 + np.sum(row > row[i])) for i, row in enumerate(B)]
    all12 = all((i+1) not in top_sets[i] for i in range(12))
    loads = B.sum(0)
    load_top = [int(j)+1 for j in np.flatnonzero(np.isclose(loads, loads.max()))]
    t1 = 1 in load_top
    prot = [j for j in range(12) if G[j].sum() == 0]
    held = [i + 1 for i in range(12) if (i+1) in top_sets[i]]
    return dict(all12=bool(all12), t1=bool(t1), protective=prot, held=held,
                top_sets=top_sets, own_competition_ranks=own_ranks,
                load_top_set=load_top, tie_rule='competition rank: 1 + count(values > own)',
                load_t1=float(loads[0]),
                margin=float(np.sort(loads)[-1] - np.sort(loads)[-2]),
                s5=int(np.argmax(B[4])) == 11, s12=int(np.argmax(B[11])) == 4)


def drop(S, G, cols):
    keep = [r for r in range(S.shape[1]) if r not in cols]
    return S[:, keep], G[:, keep]


def merge(S, G, r, s):
    keep = [c for c in range(S.shape[1]) if c not in (r, s)]
    Sn = np.column_stack([S[:, keep], S[:, r] + S[:, s]])
    Gn = np.column_stack([G[:, keep], G[:, r] + G[:, s]])
    return Sn, Gn


def main():
    mm = _load()
    S, G, RES = mm.S.copy(), mm.GOV.copy(), list(mm.RES)
    base = claims(S, G)
    out = {'meta': {
               'schema_version': 2,
               'status': 'complete',
               'model_sha256': hashlib.sha256(open(MODEL, 'rb').read()).hexdigest(),
               'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
               'object': 'raw semantic overlap B = S @ GOV.T, not executable coupling',
               'tie_rule': 'competition rank and complete maximizing sets',
               'deterministic': True,
           },
           'resources': RES, 'base': base, 'leave_one_out': [], 'merge': [], 'drop_two': []}

    for r in range(8):
        c = claims(*drop(S, G, {r}))
        out['leave_one_out'].append(dict(dropped=RES[r], **c))
    for r, s in itertools.combinations(range(8), 2):
        c = claims(*merge(S, G, r, s))
        out['merge'].append(dict(merged=[RES[r], RES[s]], **c))
    for r, s in itertools.combinations(range(8), 2):
        c = claims(*drop(S, G, {r, s}))
        out['drop_two'].append(dict(dropped=[RES[r], RES[s]], **c))

    for k in ('leave_one_out', 'merge', 'drop_two'):
        rows = out[k]
        out[k + '_summary'] = dict(
            n=len(rows),
            all12=sum(r['all12'] for r in rows),
            t1=sum(r['t1'] for r in rows),
            s5=sum(r['s5'] for r in rows),
            s12=sum(r['s12'] for r in rows),
            protective_unchanged=sum(r['protective'] == [3, 5, 6, 8, 9] for r in rows))
        from collections import Counter
        cc = Counter(s for r in rows for s in r['held'])
        out[k + '_summary']['steps_regaining'] = dict(sorted(cc.items()))
    json.dump(out, open(OUT, 'w'), indent=1)
    print(f'wrote {OUT}\n')
    print(f"base: all12={base['all12']} t1={base['t1']} s5={base['s5']} s12={base['s12']} "
          f"load_t1={base['load_t1']:.2f} margin={base['margin']:.2f}")
    for k in ('leave_one_out', 'merge', 'drop_two'):
        s = out[k + '_summary']
        print(f"\n{k:<14} n={s['n']:<4} all12 {s['all12']}/{s['n']}   T1 top {s['t1']}/{s['n']}"
              f"   S5->T12 {s['s5']}/{s['n']}   S12->T5 {s['s12']}/{s['n']}"
              f"   protective unchanged {s['protective_unchanged']}/{s['n']}")
        for r in out[k]:
            if not (r['all12'] and r['t1']):
                lab = r.get('dropped', r.get('merged'))
                print(f"    FAILS: {lab}  all12={r['all12']} t1={r['t1']} "
                      f"steps regaining their index-mate={r['held']}  "
                      f"load_t1={r['load_t1']:.2f} margin={r['margin']:.2f}")
        print(f"    steps that EVER regain their index-mate: {s['steps_regaining']}")


if __name__ == '__main__':
    main()
