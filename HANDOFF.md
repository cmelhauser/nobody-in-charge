# Project handoff — expanded robustness complete, all checkers passing

**Written:** 2026-08-09
**Canonical project:** the Git checkout containing this file; its repository root is `.`
**Status:** All analysis is complete and every checker passes. Both notebooks execute clean, all
three PDFs are rebuilt and visually inspected with no blank pages and no margin overflow. What
remains is the unresolved *scientific* limitations listed in section 9, which are expected and are
not release defects.

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
| `tools/run_notebook.py` and `--paper` | both CLEAN, 8 cells, 70 assertions each |
| `tools/check_book.py` | **0 failures, 39 warnings** |

## 5. How the figure traceability failure was closed

`tools/check_book.py` had been failing since before this round: 55 failures at the starting
commit, rising to 102 once the notebooks were regenerated. `check_figures` requires every decimal
in a chapter to be reachable from the notebook, the model source, or a cache, and the compact
regenerated notebook printed far fewer figures than the 38-cell notebook it replaced.

The old notebook could not be restored. Executed against the current caches it reported
`Morris trajectories: got 20.0000, book says 10.0`, had three cells producing no output, never
contained the required `CLEAN CACHE-BACKED VERIFICATION NOTEBOOK` sentinel, and finished
`NOT CLEAN`.

`tools/regenerate_notebooks.py` now emits a published-figures cell that **derives** the quoted
values from the caches and the model matrices rather than restating them. It covers the part5
trajectories and dose sweeps, the ch14 decay sweep and its environment-matched individual test,
ch15 service, ch13 proxy averaging with Wilson intervals, the OAT influence ranges, the release
gate with Wilson intervals and paired contrasts, the Chapter 7 DeGroot worked example, the
Chapter 13 CES cross-partials, the Part Four semantic-overlap algebra with its seeded jitter and
structural tests, the Chapter 17 reassignment test, and the Chapter 22 founder constants.

Three things had to be handled to reach zero, and they are worth knowing before editing that cell:

1. **Rounding convention.** The prose rounds half away from zero; Python rounds half to even. The
   book prints 57.71 for a cached 57.705, which `round()` renders 57.70. The cell prints a half-up
   rendering alongside the plain one.
2. **Percentages.** Chapters quote a stored proportion as a percentage, so both are printed.
3. **Scientific notation.** The Chapter 14 maintenance figures are stored as `3.03e-08`, which no
   decimal search can match, so they are also printed in plain decimal.

Do not satisfy this check by pasting literals. Its purpose is that no published figure is
untraceable, and hard-coded constants would defeat it.

**One genuine error surfaced.** Chapter 20 and the paper both printed the invisible condition's
year-ten membership as 12.99. Every other cell in that row reproduces exactly, and the correct
derivation is 12.9849, so both now read 12.98.

The two `intervals` failures were real house-style violations predating this round. Chapter 13's
Machinery now labels the substitution table and cross-partials as exact algebra and gives Wilson
intervals for the proxy-averaging proportions; Chapter 14's decay sweep now carries the 95 per
cent half-widths beside its membership series.

## 6. PDF state

Built and visually inspected. Page images were rendered at 55 to 110 dpi and scanned
programmatically for blank pages and margin overflow, with contact sheets and full-resolution
inspection of every flagged page.

| Artifact | Pages | Size | Result |
|---|---:|---|---|
| `build/nobody-in-charge.pdf` | 259 | A4 | 0 blank, 0 margin overflow |
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

Table 41, the paper's mapping table reproduced inside the book, was clipped on page 230 with its
caption and second column cut. The cause was that pandoc emitted it as a **simple** table, one
line per row, which cannot wrap; it therefore converted to a 211-character table whose relative
column widths were computed against the default 72-column reference, putting it about three line
widths wide. `--columns` on either pass does not fix it: on the conversion pass the simple-table
width is unaffected, and on the PDF pass it rescales every table in the book and took the count of
overflowing pages from 2 to 9. The fix is `-t markdown-simple_tables --columns=90` on the
conversion, which emits a wrapping grid table. Book margin overflow is now zero pages.

That change moved table cells from an indented opening to a pipe opening, so the enumerator
restoration described above had to accept both.

## 7. Repository state

The working tree is clean and this round is committed on `main`. Nothing has been pushed; `main`
is ahead of `origin/main`. Push is deliberately left to the author.

`research/ROBUSTNESS-RESULTS.md` is tracked. `.gitignore` now excludes the LaTeX build artifacts
the paper emits, so a paper build no longer dirties the tree.

## 8. Generating-platform note

The three screens ran on Linux x86-64 under NumPy 2.2.6; earlier caches were generated on macOS.
Re-executing a macOS-generated OAT job on Linux reproduced every discrete outcome exactly and
differed on continuous outcomes only in the last representable digit, about 1e-16. No
classification changed. Provenance is recorded in `research/PARAMETERS.md` section 8.4 and in
`AGENT_VERIFY.md`. Expect agreement to reported precision, not bit-identical reproduction.

## 9. Unresolved scientific limitations

These are expected and are not release defects. They are the honest boundary of what the project
may claim.

- No simulation parameter is fitted to longitudinal AA group data, and the original calibration
  targets of 45 members and 9 experienced members fail at 17.80 and 1.25. They were not retuned.
- The `S` and `GOV` matrices are one person's judgment. Part Four's conclusions degrade smoothly
  with disagreement about the magnitudes and are essentially gone under structural randomization,
  where index-pairing fails on all twelve in only 40.6 per cent of draws.
- The mapping from the Traditions to the theorem's assumptions is a reading of three sentences.
  Nobody has a method for testing it.
- The recipient contrast, 1.028 [-0.259, 2.314], and both founder-composition contrasts remain
  unresolved. No equivalence margin was prespecified.
- Chapter 14 separation is rare rather than typical: 7 of 400 endpoint environments.
- `a:5` and `a:11` sit at or below the Sobol membership noise floor and are not separated from
  Monte Carlo error. The practice first-order column remains withheld.
- Every horizon is finite and the membership series is still moving at 100 years. No steady-state
  or indefinite-persistence claim is available.
- `research/staged/` is intentionally deferred and was not used.

## 10. Notes for the next agent

The paper verification notebook is byte-identical to the book notebook apart from its title, and
both are generated from one cell set by `tools/regenerate_notebooks.py`. That satisfies the
release gate, which asks only that both execute clean with stored output, but it is not a distinct
verification of the paper's own claims. Making it one, or explicitly retiring it as the release
plan's section 3.4 allows, is the obvious next editorial decision.

Do not restart any completed analysis. Every cache in `research/` is complete and hash-current,
and rerunning the Sobol design alone costs about four hours.
