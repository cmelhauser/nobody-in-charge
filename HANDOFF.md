# Project handoff — expanded robustness complete, one checker still failing

**Written:** 2026-08-09
**Canonical project:** the Git checkout containing this file; its repository root is `.`
**Status:** All analysis is complete. `check_release`, `check_portability`, and `check_chapter`
pass. `check_book` does not. The release is therefore **not** closeable yet, and the remaining
work is documentation-side, not computational.

## 1. Objective and decisions that must not change

Finish a rigorous, internally synchronized release of the model, manuscript, paper, primer,
appendix, notebooks, plans, PDFs, and independent verification brief.

- Modeled room capacity stays **60**.
- Confirmatory stochastic analyses stay at **400 paired seeds**.
- Expanded robustness comes from more draws, distances, variants, trajectories, horizons, and
  integration steps. Not from 1,000 modeled members and not from a blanket 1,000-seed rule.

The executable model remains frozen:

```text
model/aa_group_model.py
SHA-256 c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952
```

All interpretation decisions recorded in `CLAUDE.md` continue to hold unchanged. Nothing in this
round altered the model, the confirmatory estimands, or any 400-seed result.

## 2. Source boundary

`research/staged/` remains intentionally unincorporated and reserved for the next round. Maxwell
(1950) and Golub and Jackson (2010) remain under `research/incorporated/`. Nothing in this round
used staged material.

## 3. What this round completed

The three screens that were outstanding are done, hash-current, and `complete`:

- `research/oat_full.json`: 118 parameter jobs, 944 perturbation points, 19,824 finite values.
- `research/morris.json`: 20 trajectories, 118 factors, 2,380 points, reference adherence 0.85.
- `research/sobol.json`: 1,024-row base, 11,264 evaluations, eight factors, 2,000-resample
  bootstrap intervals, noise replicate included.

`research/ROBUSTNESS-RESULTS.md` is generated from them by `tools/summarize_robustness.py`.

### Findings that changed the project

1. **Three of the eight Sobol factors were wrong.** `model/sobol_indices.py` carried a `FACTORS`
   list from the retired ten-trajectory screen. At twenty trajectories `a:8` falls to rank 15,
   `a:4` to 27, and `omega` to 37. They are replaced by `lam_exog`, `a:5`, and `a:11`. The cut is
   untied, 15.87 against 14.34 at the ninth factor. The list was corrected before the Sobol run.
2. **The Sobol evaluator could not have handled a matrix factor.** It wrote every non-`a:` id into
   the parameter dictionary, which is a silent no-op for an `S` or `GOV` cell. It now mutates the
   matrix, rebuilds every derived quantity, matches the OAT and Morris evaluators, and raises on an
   unknown id. No matrix cell reached the top eight; the highest is `S:8,6` at rank 17.
3. **The membership first-order Sobol column became usable.** At the retired 128 rows it failed
   three diagnostics and was withheld. At 1,024 rows no membership factor has `S1` above its `ST`
   and the sum is 0.693. The practice column is still withheld: `delta0` gives `S1 = 0.421` against
   `ST = 0.417`, and the practice sum is 1.074.
4. **The OAT screen resolved much more strongly than the global designs**, 931/2/11 on membership
   across 944 points, with nine of the eleven reversals concentrated in large downward moves of
   `p_gate`, `delta0`, and `churn`.
5. **Two older claims were wrong and are corrected.** Chapter One said more than half the
   parameters could move referral-starved survival alone; it is 26 of 118. Chapters One and Six
   said the ordering held in all 236 one-at-a-time cases, which was the retired design.
6. **The primer miscounted unresolved Tradition rows.** Seven of twelve resolve, so five are
   unresolved, of which three are protective. It said four.
7. **The appendix rewrite had left eleven dangling cross-references.** All prose references were
   retargeted and `A10.1` now records the mapping, because the docstrings of hash-linked analysis
   scripts cannot be edited without invalidating their caches.
8. **The appendix had silently dropped the resource-list test.** It is restored as `A7.6`.

## 4. Current checker state

| Command | Result |
|---|---|
| `tools/check_release.py` | **136 checks passed, 0 failed** |
| `tools/check_portability.py` | pass |
| `tools/check_chapter.py` on the primer | all clear, 9 long-sentence warnings |
| `tools/run_notebook.py` and `--paper` | both CLEAN, 7 cells, 70 assertions each |
| `tools/check_book.py` | **102 failures, 39 warnings** |

## 5. The one blocking defect

`tools/check_book.py` fails with 100 `figures` failures, 2 `intervals` failures, and 1 other.

**Cause.** `check_figures` requires every decimal in a chapter to be traceable to the notebook
source or output, the model, or a cache. `tools/regenerate_notebooks.py` builds a compact
seven-cell cache-identity notebook that prints far fewer figures than the 38-cell notebook it
replaced. At `HEAD` the same checker reported 55 failures, so the checker was already failing
before this round; regenerating the notebooks raised it to 102.

**Why the old notebook cannot simply be restored.** It is stale and invalid. Executed against the
current caches it reports `Morris trajectories: got 20.0000, book says 10.0`, has three cells
producing no output, never contained the required `CLEAN CACHE-BACKED VERIFICATION NOTEBOOK`
sentinel, and finishes `NOT CLEAN`. `AGENT_VERIFY.md` section 6 and `check_release` both require
the regenerated form, and they pass with it.

**The fix.** Extend `tools/regenerate_notebooks.py` with a public-figures cell that derives and
prints, from the caches, the figures the chapters actually quote, then regenerate and re-run. The
missing figures by chapter are listed by running the checker; they are all cache-derivable, for
example the ch14 decay sweep from `ch14_sweep.json`, the ch20 to ch22 values from `part5.json`,
the ch15 values from `ch15_service.json`, and the ch12 values 12.98 and 14.64 from `oat_full.json`.
**Derive them; do not paste literals.** The point of the check is that no figure in the book is
untraceable, and satisfying it with hard-coded constants would defeat it.

The 2 `intervals` failures, in ch13 and ch14, are separate: those chapters present simulation
output without an interval, which is a house-style violation predating this round.

## 6. PDF state

Built and visually inspected. Page images were rendered at 55 to 110 dpi and scanned
programmatically for blank pages and margin overflow, with contact sheets and full-resolution
inspection of every flagged page.

| Artifact | Pages | Size | Result |
|---|---:|---|---|
| `build/nobody-in-charge.pdf` | 259 | A4 | 0 blank; 1 clipped table remains |
| `paper/anonymity-as-an-aggregation-condition.pdf` | 32 | A4 | clean; no undefined references |
| `reference/PRIMER-steps-and-traditions.pdf` | 17 | Letter | clean |

Fixed this round, all in `tools/build_book.py` unless noted:

- long typewriter filenames overflowed the right margin and were cut mid-word, for example
  `research/krout-1925-origins-of-prohibit`; fixed with `hyphenat[htt]` and `xurl`;
- the 64-character model hash overflowed the appendix's first page; reformatted as a code block
  in `appendix/APPENDIX.md`;
- Table 48 in the decline chapter lost its final two columns; fixed by setting `longtable` in
  `\footnotesize` via `etoolbox`;
- the book printed dead cross-references `[eq:err]` and `[prop:one]` where the paper prints
  numbers, because the paper's LaTeX labels do not survive the LaTeX to markdown to LaTeX round
  trip; now resolved to plain wording by `resolve_paper_crossrefs`;
- the paper's mapping table lost the `1.` from its Common welfare row, because pandoc's LaTeX
  reader treats a leading `1.` as an ordered-list marker and drops it; now restored.

**Still open.** Table 41, the paper's mapping table as reproduced inside the book, is clipped on
the right on book page 230; its caption and second column are cut. The paper's own PDF renders it
correctly, so this is a book-build defect only. Cause: pandoc converts it to a 211-character
multiline table and computes relative column widths against the default 72-column reference, so
the widths sum to roughly 2.9 line widths. Setting `--columns` on either pandoc pass was tried and
rejected: on the conversion pass it does not change the emitted width, and on the PDF pass it
rescales every table in the book and took the count of overflowing pages from 2 to 9. A per-table
fix is needed, such as wrapping over-wide tables in `adjustbox` with `max width=\textwidth`.

## 7. Repository state

Working tree is **not** clean; this round's changes are uncommitted and unpushed. `HEAD` is
`de7a70b8a4ad96d1d632cf52fd3a52159bdefebf` and equals `origin/main`.

A stale `.git/index.lock` is present. It blocks `git add` and `git commit`. Remove it with
`rm .git/index.lock` before committing. It could not be removed from the analysis sandbox, which
has create and write but not unlink permission on the mount.

`research/ROBUSTNESS-RESULTS.md` is new and untracked and must be added. `.gitignore` now excludes
the LaTeX build artifacts the paper emits.

## 8. Generating-platform note

The three screens ran on Linux x86-64 under NumPy 2.2.6; earlier caches were generated on macOS.
Re-executing a macOS-generated OAT job on Linux reproduced every discrete outcome exactly and
differed on continuous outcomes only in the last representable digit, about 1e-16. No
classification changed. Provenance is recorded in `research/PARAMETERS.md` section 8.4 and in
`AGENT_VERIFY.md`. Expect agreement to reported precision, not bit-identical reproduction.

## 9. Next agent, in order

1. Fix `check_book` as described in section 5. This is the only blocking item.
2. Decide the ch13 and ch14 interval failures: either add the interval and design, or move the
   figure into The Machinery where the house style allows it.
3. Fix the Table 41 clipping in section 6.
4. Re-run the full sequence in `README.md`, rebuild all three PDFs, re-inspect.
5. Remove the stale lock, commit, and confirm `HEAD` against `origin/main`.
6. Close the verdict using `AGENT_VERIFY.md`.

Do not restart any completed analysis. Every cache in `research/` is complete and hash-current,
and rerunning the Sobol design alone costs about four hours.
