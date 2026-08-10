"""Sensitivity analysis for Part Two, which had none.

Why this exists. Parts Three, Four and Five carry five sensitivity designs between them.
Part Two, which contains the book's central claim, carried none: its four chapters have no
robustness or sensitivity language anywhere, and `appendix/APPENDIX.md` did not mention the
mapping at all. The theorem itself needs no sensitivity, being a theorem. What needs it is
everything between the theorem and the Traditions:

  1. The claim that concentration of influence is what matters, illustrated in Chapter 8 by
     exactly two matrices, flat and one dominant member at alpha = 0.35. Two points is not a
     dose-response and cannot say where the damage begins.
  2. The claim that Golub and Jackson's three obstructions map onto three failure modes a
     fellowship can suffer, which is asserted in prose and never computed.
  3. The bipartite touring-speaker structure of Chapter 11, which that chapter explicitly
     flags as argued rather than simulated. This script simulates it.
  4. Whether any of the above is an artefact of using three hand-built matrix families. A
     random-structure control answers that.

Influence is the normalised left dominant eigenvector of a row-stochastic matrix. Under
iid Gaussian initial errors with common standard deviation sigma, expected absolute
consensus error is exactly sigma * ||s||_2 * sqrt(2/pi). Independence and variance alone
do not imply this identity; outside the Gaussian premise it is a benchmark or requires
an explicit approximation. Everything is deterministic except the seeded random-matrix
control, where 200 draws per cell describe the chosen matrix distribution.

Cached to `../research/part2_influence.json`. Fast enough to run in one go.

Run:  python3 part2_influence.py
"""
import hashlib, json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, '..', 'research', 'part2_influence.json'))
ROOT2PI = np.sqrt(2.0 / np.pi)
NS = [10, 25, 50, 100, 250, 500, 1000]


def influence(A, tol=1e-13, itmax=100000):
    """Normalised left dominant eigenvector by power iteration on A'. Row-stochastic A has
    dominant eigenvalue 1, so this converges for strongly connected aperiodic A."""
    n = A.shape[0]
    s = np.full(n, 1.0 / n)
    for _ in range(itmax):
        t = s @ A
        t = t / t.sum()
        if np.abs(t - s).max() < tol:
            return t
        s = t
    return s


def err(s, sigma=1.0):
    """Expected absolute consensus error under iid Gaussian initial errors."""
    return float(sigma * np.linalg.norm(s) * ROOT2PI)


# ---------------------------------------------------------------- matrix families

def flat(n):
    return np.full((n, n), 1.0 / n)


def dominant(n, alpha):
    """One member receives share alpha of every row; the rest split the remainder evenly."""
    A = np.full((n, n), (1.0 - alpha) / (n - 1))
    A[:, 0] = alpha
    np.fill_diagonal(A, A.diagonal())          # self-weight is allowed and is not special
    return A / A.sum(1, keepdims=True)


def clique(n, k, inward):
    """`k` members form a clique that gives share `inward` of its attention to itself. The
    rest of the group attends flat. Golub and Jackson's third obstruction, insufficient
    dispersion: a subgroup that does not attend to the wider society."""
    A = np.full((n, n), 1.0)
    A[:k, :] = (1.0 - inward) / (n - k)
    A[:k, :k] = inward / k
    A[k:, :] = 1.0 / n
    return A / A.sum(1, keepdims=True)


def imbalanced(n, k, ratio):
    """`k` members receive `ratio` times the attention they give. Golub and Jackson's second
    obstruction. Implemented by scaling the columns of a flat matrix and renormalising rows,
    which is the smallest change that produces the asymmetry."""
    A = np.full((n, n), 1.0)
    A[:, :k] *= ratio
    return A / A.sum(1, keepdims=True)


def rotation(n, pool, alpha):
    """Chapter 10's construction, reproduced here so the four families are comparable: over a
    cycle of `pool` terms, one member at a time holds share alpha, averaged across terms."""
    A = np.zeros((n, n))
    for r in range(pool):
        M = np.full((n, n), (1.0 - alpha) / (n - 1))
        M[:, r] = alpha
        A += M / pool
    return A / A.sum(1, keepdims=True)


def elders(n, e, alpha_elder, pool=0, alpha_office=0.0):
    """A non-rotating class of `e` elder statesmen alongside an optional rotating office pool.

    Added 10 August 2026, after reading what AA's own commentary says about Tradition Two.
    The Twelve and Twelve describes the group's rotating committee as "sharply limited" in
    authority, unable in any sense to govern or direct, and then locates the fellowship's real
    influence in a different set of people: deposed founders who mature into "elder statesmen",
    who are called "the real and permanent leadership of A.A.", who "become the voice of the
    group conscience", and to whom a perplexed group "inevitably turns". Those people do not
    rotate, because they hold no office to rotate out of.

    That is a different structure from anything Chapter 10 modelled, and it is worth computing
    rather than arguing about. `e` members hold `alpha_elder` of every row's attention between
    them and never change. Separately, `pool` members rotate through an office carrying
    `alpha_office`, time-averaged over the cycle exactly as `rotation` does. Setting
    alpha_office low is the case the source text actually describes.

    The point of the construction is that the elders' share does not depend on n, so maximum
    influence floors at roughly alpha_elder / e however large the group grows and however wide
    the rotation pool is. Widening the pool cannot fix a concentration that is not in the pool.
    """
    rest = 1.0 - alpha_elder - alpha_office
    if rest < 0:
        raise ValueError('alpha_elder + alpha_office must not exceed 1')
    A = np.full((n, n), rest / n)
    if e:
        A[:, :e] += alpha_elder / e
    elif alpha_elder:
        raise ValueError('alpha_elder requires at least one elder')
    if pool:
        # Time-averaged over a cycle: each of `pool` members holds the office for one term.
        A[:, e:e + pool] += alpha_office / pool
    return A / A.sum(1, keepdims=True)


def bipartite_speakers(n, k, share, back=0.0):
    """Chapter 11's unsimulated structure, simulated.

    A movement of `n` members in local societies attending flat to each other, plus `k`
    touring speakers who receive `share` of every member's attention. `back` is the fraction
    of a speaker's own attention that flows back to the general membership.

    **The back-flow parameter is not decoration and the first version of this function did not
    have it.** With back = 0 the speakers are a closed communicating class: they attend only to
    each other, so the chain is not strongly connected, Golub and Jackson's theorem does not
    apply, and the speakers hold ALL the influence at every n and every share, including
    share = 0.1. That is a true statement about an absorbing class and a useless one about a
    fellowship, and reporting it as a finding would be the vacuous-robustness error this
    project has made twice. With back > 0 the chain is strongly connected, the theorem applies,
    and the question becomes quantitative: how much attention must flow back before the
    speakers' influence vanishes as the movement grows?
    """
    A = np.zeros((n + k, n + k))
    A[:n, :n] = (1.0 - share) / n
    A[:n, n:] = share / k
    A[n:, n:] = (1.0 - back) / k
    A[n:, :n] = back / n if back > 0 else 0.0
    return A / A.sum(1, keepdims=True)


def random_stochastic(n, conc, rng):
    """Control. Dirichlet rows with concentration `conc`: large conc gives near-flat rows,
    small conc gives rows that put most of their weight on one or two members. This produces
    concentration without any of the three hand-built structures."""
    A = rng.dirichlet(np.full(n, conc), size=n)
    return A


# ---------------------------------------------------------------- the study

def main():
    out = {'meta': {
               'schema_version': 2,
               'status': 'complete',
               'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
               'deterministic_except': 'seeded random-matrix control, 200 draws per cell',
               'matrix_convention': 'A[i,j] is attention i gives j; s is normalized left stationary vector',
               'error_premise': 'iid Gaussian initial errors with common standard deviation sigma',
           },
           'note': 'deterministic except the random control; see module docstring'}

    # 1. Dose-response on dominance. Chapter 8 gives alpha = 0.35 only.
    rows = []
    for a in [0.0, 0.02, 0.05, 0.10, 0.20, 0.35, 0.50, 0.75]:
        r = {'alpha': a}
        for n in NS:
            s = influence(flat(n) if a == 0 else dominant(n, a))
            r[str(n)] = [float(s.max()), err(s)]
        rows.append(r)
    out['dominance'] = rows

    # 2. Clique isolation, the third obstruction.
    rows = []
    for k, inw in [(3, 0.5), (3, 0.9), (3, 0.99), (5, 0.9), (5, 0.99), (10, 0.9), (25, 0.9)]:
        r = {'k': k, 'inward': inw}
        for n in NS:
            if n <= k * 2: continue
            s = influence(clique(n, k, inw))
            r[str(n)] = [float(s.max()), err(s), float(s[:k].sum())]
        rows.append(r)
    out['clique'] = rows

    # 3. Imbalance, the second obstruction.
    rows = []
    for k, ratio in [(1, 2), (1, 5), (1, 20), (5, 5), (5, 20), (25, 5)]:
        r = {'k': k, 'ratio': ratio}
        for n in NS:
            if n <= k * 2: continue
            s = influence(imbalanced(n, k, ratio))
            r[str(n)] = [float(s.max()), err(s), float(s[:k].sum())]
        rows.append(r)
    out['imbalance'] = rows

    # 4. The bipartite touring-speaker structure Chapter 11 flags as unsimulated.
    rows = []
    for k, share, back in [(5, 0.3, 0.0), (5, 0.3, 0.01), (5, 0.3, 0.05), (5, 0.3, 0.20),
                           (5, 0.3, 0.50), (5, 0.1, 0.20), (5, 0.5, 0.20), (2, 0.3, 0.20),
                           (20, 0.3, 0.20)]:
        r = {'speakers': k, 'share': share, 'back': back}
        for n in NS:
            s = influence(bipartite_speakers(n, k, share, back))
            r[str(n)] = [float(s.max()), err(s), float(s[n:].sum())]
        rows.append(r)
    out['speakers'] = rows

    # 4b. Does the obstruction depend on the LEVEL of a practice or on how it SCALES with the
    #     group? Chapter 8 maps the three obstructions onto three fellowship failure modes at
    #     fixed magnitude. The fixed-magnitude clique and imbalance rows above show their
    #     influence vanishing as n grows, which means at fixed magnitude they are not
    #     obstructions at all. These rows let the parameter grow with n instead.
    rows = []
    for kind in ('clique_scaling', 'imbalance_scaling'):
        r = {'kind': kind}
        for n in NS:
            if kind == 'clique_scaling':
                inw = 1.0 - 3.0 / n          # inwardness approaches 1 as the group grows
                s = influence(clique(n, 3, min(inw, 0.9999)))
            else:
                s = influence(imbalanced(n, 1, n / 5.0))   # ratio grows linearly in n
            r[str(n)] = [float(s.max()), err(s)]
        rows.append(r)
    out['scaling'] = rows

    # 5. Rotation, for comparability with Chapter 10.
    rows = []
    for pool in [3, 6, 12, 25, 50, 100]:
        r = {'pool': pool}
        for n in NS:
            if n <= pool: continue
            s = influence(rotation(n, pool, 0.35))
            r[str(n)] = [float(s.max()), err(s)]
        rows.append(r)
    out['rotation'] = rows

    # 5b. The elder-statesman structure. Chapter 10 prices a rotation pool that is too narrow;
    #     this prices the case where the rotation is irrelevant because the influence is not in
    #     the rotating positions. Both the level sweep and the "does the prescription help"
    #     contrast are computed, because the second is the decision-relevant one.
    rows = []
    for e, a in [(1, 0.10), (1, 0.20), (1, 0.35), (3, 0.10), (3, 0.20), (3, 0.35),
                 (5, 0.20), (5, 0.35), (10, 0.35), (25, 0.35)]:
        r = {'elders': e, 'alpha_elder': a, 'floor_predicted': a / e}
        for n in NS:
            if n <= e * 2: continue
            s = influence(elders(n, e, a))
            flat_err = err(influence(flat(n)))
            # The error RATIO is quoted in Chapter 8, the primer and the paper, so it is
            # stored rather than left to be divided out of two other numbers. A figure a
            # reader has to compute is a figure tools/check_book.py cannot trace.
            r[str(n)] = [float(s.max()), err(s), float(s[:e].sum()),
                         float(err(s) / flat_err)]
        rows.append(r)
    out['elders'] = rows

    # 5c. Does Chapter 10's twenty-six per cent prescription rescue a group that has an elder
    #     class? The pool is set to 26 per cent of the group at every size, which is the
    #     chapter's own recommendation, and the officeholder's share is set low because the
    #     source text says the rotating committee cannot govern or direct.
    rows = []
    for e, a_eld, a_off in [(0, 0.0, 0.35), (3, 0.10, 0.05), (3, 0.20, 0.05),
                            (3, 0.10, 0.35), (5, 0.20, 0.05)]:
        r = {'elders': e, 'alpha_elder': a_eld, 'alpha_office': a_off,
             'pool_rule': 'twenty-six per cent of the group, per Chapter 10'}
        for n in NS:
            pool = max(1, int(round(0.26 * n)))
            if n <= (e + pool) * 2: continue
            s = influence(elders(n, e, a_eld, pool=pool, alpha_office=a_off))
            flat_s = influence(flat(n))
            r[str(n)] = [float(s.max()), err(s), float(s.max() / flat_s.max())]
        rows.append(r)
    out['elders_vs_prescription'] = rows

    # 6. Random control: is the relationship between max influence and error an artefact of
    #    the hand-built families? Under the closed form it cannot be, since error depends only
    #    on ||s||, but max influence and ||s|| are different statistics and the book uses the
    #    first as a proxy for the second throughout.
    rng = np.random.default_rng(20260802)
    ctrl = []
    for n in [25, 100, 250]:
        for conc in [0.05, 0.2, 1.0, 5.0, 50.0]:
            mx, er, l2 = [], [], []
            for _ in range(200):
                s = influence(random_stochastic(n, conc, rng))
                mx.append(float(s.max())); er.append(err(s)); l2.append(float(np.linalg.norm(s)))
            ctrl.append(dict(n=n, conc=conc,
                             max_mean=float(np.mean(mx)), max_sd=float(np.std(mx, ddof=1)),
                             err_mean=float(np.mean(er)), err_sd=float(np.std(er, ddof=1)),
                             l2_mean=float(np.mean(l2)),
                             corr_max_err=float(np.corrcoef(mx, er)[0, 1])))
    out['random_control'] = ctrl

    # 7. The identity check the book relies on: flat error is exactly sqrt(2/pi)/sqrt(N).
    out['identity'] = [{'n': n,
                        'computed': err(influence(flat(n))),
                        'closed_form': float(ROOT2PI / np.sqrt(n))} for n in NS]

    json.dump(out, open(OUT, 'w'), indent=1)
    print(f'wrote {OUT}')
    for k, v in out.items():
        if isinstance(v, list): print(f'  {k}: {len(v)} rows')


if __name__ == '__main__':
    main()
