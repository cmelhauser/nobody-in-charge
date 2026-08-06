"""Compare independently elicited governance matrices against the book's, and rerun Part Four.

`research/GOVERNANCE-MATRIX-ELICITATION.md` asks a reader to mark which of 96 cells in a
twelve-by-eight table are non-zero, without seeing Part Four. This script is what happens to
the completed forms. It was written before any form came back, so that the analysis is fixed in
advance and cannot be chosen after seeing the answers.

**What it reports, in the order the elicitation form promises:**

1. **Which rows are empty.** Chapters 16, 17 and 18 all rest on five Traditions governing
   nothing any Step consumes. If a respondent leaves a different five empty, or leaves four or
   six, Chapter 18 is wrong and will say so.
2. **Cell-by-cell agreement out of 96**, with the two kinds of disagreement separated: cells
   the respondent filled that the book leaves empty, and cells the book fills that the
   respondent leaves empty. Those are different mistakes and a single agreement rate hides it.
3. **The consequences.** Chapters 16 and 17 recomputed on the respondent's matrix: does
   index-pairing still fail on all twelve, does unity still carry the largest load, do the two
   inversions survive.

**Reading the agreement number.** Chance agreement is high here because the book's matrix is
sparse: 35 of 96 cells are filled, so a respondent who marked cells at random with the same
density would agree on about 55 per cent by luck. The script therefore reports Cohen's kappa
alongside the raw rate, and the raw rate alone should not be quoted.

**A respondent may supply strengths as well as marks.** If they do, the consequence rerun uses
them. If they give only zeros and ones, the rerun substitutes the book's own magnitude in every
cell both agree is non-zero, and 0.5 in cells the respondent filled and the book did not. That
substitution is stated in the output every time, because it means a bare-marks respondent is
testing the *sparsity pattern* and not the magnitudes, which is the intended and more important
half.

Input format: one file per respondent at `research/governance-elicitation-<id>.md`, containing
a markdown table whose first column is the Tradition and whose remaining eight columns are the
resources in the order given in the elicitation form. Blank and "0" both mean empty.

Run:  python3 elicitation_compare.py [--self-test]
"""
import glob, importlib.util, os, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'aa_group_model.py')
RESEARCH = os.path.abspath(os.path.join(HERE, '..', 'research'))
PROTECTIVE = [3, 5, 6, 8, 9]          # T4, T6, T7, T9, T10, zero-indexed


def _load():
    spec = importlib.util.spec_from_file_location('m', MODEL)
    mm = importlib.util.module_from_spec(spec)
    sys.modules['m'] = mm
    spec.loader.exec_module(mm)
    return mm


def parse(path):
    """Pull a 12 by 8 matrix out of a markdown table. Tolerant of alignment rows, of bold, and
    of a respondent writing 'x' or a tick instead of 1."""
    rows = []
    for line in open(path):
        if not line.strip().startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 9:
            continue
        if set(''.join(cells[1:])) <= set('-: '):
            continue                                    # alignment row
        label = cells[0].strip('* ')
        if not re.match(r'T\d', label, re.I):
            continue                                    # header row
        vals = []
        for c in cells[1:9]:
            c = c.strip('* ')
            if c in ('', '0', '0.0', '-', 'n', 'N'):
                vals.append(0.0)
            elif c.lower() in ('x', 'y', 'yes', '1', 'v') or c == '✓':
                vals.append(1.0)
            else:
                try:
                    vals.append(float(c))
                except ValueError:
                    vals.append(0.0)
        rows.append(vals)
    if len(rows) != 12:
        raise ValueError(f'{path}: found {len(rows)} Tradition rows, expected 12')
    return np.array(rows, float)


def kappa(a, b):
    """Cohen's kappa on two binary 12x8 masks."""
    a, b = a.ravel() > 0, b.ravel() > 0
    n = a.size
    po = float((a == b).mean())
    pe = float(a.mean() * b.mean() + (1 - a.mean()) * (1 - b.mean()))
    return (po - pe) / (1 - pe) if pe < 1 else float('nan')


def consequences(S, G):
    B = S @ G.T
    load = B.sum(0)
    return dict(all12=bool(all(int(np.argmax(B[i])) != i for i in range(12))),
                t1_top=bool(int(np.argmax(load)) == 0),
                s5_to_t12=bool(int(np.argmax(B[4])) == 11),
                s12_to_t5=bool(int(np.argmax(B[11])) == 4),
                empty_rows=[j for j in range(12) if G[j].sum() == 0],
                load_top=float(load.max()), leader=int(np.argmax(load)) + 1)


def hydrate(Gr, Gb):
    """Give a bare-marks matrix magnitudes so the consequences can be computed at all."""
    if np.any((Gr > 0) & (Gr != 1.0)):
        return Gr, False                    # respondent supplied strengths; use them
    out = np.where((Gr > 0) & (Gb > 0), Gb, 0.0)
    out = np.where((Gr > 0) & (Gb == 0), 0.5, out)
    return out, True


def report(name, Gr, mm):
    Gb, S = mm.GOV, mm.S
    both = ((Gr > 0) & (Gb > 0)).sum()
    only_r = ((Gr > 0) & (Gb == 0)).sum()
    only_b = ((Gr == 0) & (Gb > 0)).sum()
    neither = ((Gr == 0) & (Gb == 0)).sum()
    agree = both + neither
    print(f'\n=== {name} ===')
    print(f'  cells agreed {agree}/96 ({100*agree/96:.0f} per cent), kappa {kappa(Gr, Gb):+.3f}')
    print(f'    both filled {both}   respondent only {only_r}   book only {only_b}   both empty {neither}')
    er = [j for j in range(12) if Gr[j].sum() == 0]
    same = er == PROTECTIVE
    print(f'  empty rows: {[f"T{j+1}" for j in er]}')
    print(f'  book\'s five: {[f"T{j+1}" for j in PROTECTIVE]}   -> {"SAME" if same else "DIFFERENT"}')
    if not same:
        print('    ** Chapter 18 is contradicted by this respondent. **')
    Gh, substituted = hydrate(Gr, Gb)
    c = consequences(S, Gh)
    if substituted:
        print('  consequences below use the BOOK\'s magnitudes in agreed cells and 0.5 elsewhere,')
        print('  because this respondent gave marks only. They test the sparsity pattern, not the magnitudes.')
    print(f"  index-pairing fails on all twelve: {c['all12']}")
    print(f"  largest column sum: T{c['leader']} at {c['load_top']:.2f}   (book: T1 at 6.52)")
    print(f"  Step 5 -> T12: {c['s5_to_t12']}   Step 12 -> T5: {c['s12_to_t5']}")
    return dict(name=name, agree=int(agree), kappa=kappa(Gr, Gb), empty_same=bool(same), **c)


def self_test(mm):
    """Run the script against matrices whose answers are known, so that a real respondent's
    output can be trusted. Three synthetic respondents:

      identical   the book's own matrix. Everything must agree.
      noisy       the book's sparsity with six cells flipped, none in a protective row.
      dissenter   the book's matrix plus a filled T7 row. Must report a DIFFERENT empty set
                  and must contradict Chapter 18.
    """
    Gb = mm.GOV
    rng = np.random.default_rng(20260802)
    out = {}
    out['identical'] = report('self-test: identical', Gb.copy(), mm)
    noisy = Gb.copy()
    live = [(j, r) for j in range(12) for r in range(8) if j not in PROTECTIVE]
    for j, r in [live[i] for i in rng.choice(len(live), 6, replace=False)]:
        noisy[j, r] = 0.0 if noisy[j, r] > 0 else 0.4
    out['noisy'] = report('self-test: six cells flipped, protective rows intact', noisy, mm)
    diss = Gb.copy(); diss[6] = np.array([0.0, 0.3, 0.0, 0.0, 0.2, 0.0, 0.5, 0.3])
    out['dissenter'] = report('self-test: a respondent who fills T7', diss, mm)
    ok = (out['identical']['agree'] == 96 and out['identical']['empty_same']
          and out['noisy']['empty_same'] and not out['dissenter']['empty_same'])
    print(f"\nself-test {'PASSED' if ok else 'FAILED'}")
    return 0 if ok else 1


def sparsity_sweep(mm, ndraw=2000, seed=20260802):
    """How many cells would a second reader have to differ on before Part Four changes?

    The perturbation designs in A5.4 vary the MAGNITUDES and hold the sparsity pattern fixed.
    A second reader disagrees about the pattern. This sweeps the number of flipped cells and
    reports how often each Part Four claim survives.

    **A random flip is not a plausible reader and this is a bound, not a prediction.** A real
    disagreement would be structured: somebody who thinks self-support governs continuity would
    change one cell for a reason, and their other cells would be correlated with that reason.
    Random flips are both harsher than that, because they respect no reason at all, and gentler,
    because they will not concentrate on the cells that matter. The number below answers "how
    much disagreement, counted in cells", and nothing about which cells a reader would pick.

    Flips are restricted to the enabling rows, so that the two-tier split is held fixed and the
    question is about the rest of the matrix. Flipping a protective row is the separate and more
    serious disagreement the self-test's third respondent represents.
    """
    Gb, S = mm.GOV, mm.S
    rng = np.random.default_rng(seed)
    live = [(j, r) for j in range(12) for r in range(8) if j not in PROTECTIVE]
    base = consequences(S, Gb)
    print(f'base: all12={base["all12"]} T1 top={base["t1_top"]} '
          f'S5={base["s5_to_t12"]} S12={base["s12_to_t5"]}\n')
    print(f'{"flips":>6}{"all 12":>10}{"T1 top":>10}{"S5->T12":>10}{"S12->T5":>10}')
    rows = []
    for k in (1, 2, 3, 4, 6, 8, 12, 16):
        c = dict(all12=0, t1=0, s5=0, s12=0)
        for _ in range(ndraw):
            G = Gb.copy()
            for i in rng.choice(len(live), k, replace=False):
                j, r = live[i]
                G[j, r] = 0.0 if G[j, r] > 0 else 0.5
            q = consequences(S, G)
            c['all12'] += q['all12']; c['t1'] += q['t1_top']
            c['s5'] += q['s5_to_t12']; c['s12'] += q['s12_to_t5']
        rows.append((k, c))
        print(f'{k:>6}{100*c["all12"]/ndraw:>9.1f}%{100*c["t1"]/ndraw:>9.1f}%'
              f'{100*c["s5"]/ndraw:>9.1f}%{100*c["s12"]/ndraw:>9.1f}%')
    print(f'\n{ndraw} draws per row, flips confined to the seven enabling rows (56 cells).')
    return rows


def main():
    mm = _load()
    if '--self-test' in sys.argv:
        return self_test(mm)
    if '--sparsity' in sys.argv:
        sparsity_sweep(mm)
        return 0
    files = sorted(glob.glob(os.path.join(RESEARCH, 'governance-elicitation-*.md')))
    if not files:
        print('No completed elicitation forms found in research/.')
        print('Expected: research/governance-elicitation-<id>.md')
        print('The blank form is research/GOVERNANCE-MATRIX-ELICITATION.md.')
        print('\nRunning the self-test instead, so the script is known to work when they arrive.\n')
        return self_test(mm)
    rows = [report(os.path.basename(f), parse(f), mm) for f in files]
    print('\n=== across respondents ===')
    n_same = sum(r['empty_same'] for r in rows)
    print(f'  respondents leaving the same five rows empty: {n_same} of {len(rows)}')
    print(f'  index-pairing fails on all twelve for: {sum(r["all12"] for r in rows)} of {len(rows)}')
    print(f'  T1 carries the largest load for:       {sum(r["t1_top"] for r in rows)} of {len(rows)}')
    if n_same < len(rows):
        print('\n  ** At least one respondent contradicts the two-tier split. Chapter 18 and the')
        print('     five trivial counts in Chapter 16 both depend on it. **')
    return 0


if __name__ == '__main__':
    sys.exit(main())
