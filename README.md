# Nobody in Charge

*How a Fellowship of Drunks Solved a Problem in Mathematics Without Knowing It*

This repository contains a complete 25-chapter manuscript, an academic paper, a technical
appendix, a Steps-and-Traditions primer, the executable model, analysis scripts, cached
results, source ledgers, and reproducible PDF builds.

## Current status

The release-gate correction round opened on 6 August 2026 and closed on 9 August 2026. Every
checker passes: `check_release` with 136 checks, `check_book` with none failing, the primer
chapter check clear, and portability clear. Both verification notebooks execute clean, and the
book, paper and primer PDFs are built and visually inspected with no blank pages and no margin
overflow.

The two notebooks verify different things. `model/book-calculations.ipynb` checks the model's
identity and semantics, every cache's completeness and provenance, and the derivation of every
figure the chapters print. `paper/anonymity-as-an-aggregation-condition.ipynb` does all of that
and adds two paper-specific cells: it re-derives the paper's headline tables from the caches, and
it requires every decimal the paper prints to be reachable from the model, a cache, or a shown
derivation. The chapters had that guarantee through `check_book.py`; until 9 August 2026 the paper
had no equivalent. What remains is the unresolved scientific limitations listed at the end of this file,
which the release criteria permit and which must not be written up as though they were settled.

The principal model corrections and 400-seed confirmatory analyses are complete. The expanded
structural and
parameter sensitivity runs are also complete against one model identity: the multi-level
one-at-a-time screen at 944 points, the twenty-trajectory Morris screen at 2,380 points, and the
1,024-row Sobol decomposition at 11,264 evaluations. Their results are generated into
`research/ROBUSTNESS-RESULTS.md` and carried into the appendix, paper, primer, and parameter
ledger.

The Morris screen replaced three of the eight factors previously assumed for the Sobol design:
`a:8`, `a:4`, and `omega` fall to ranks 15, 27, and 37 and are replaced by `lam_exog`, `a:5`, and
`a:11`. The 1,024-row base sample also makes the membership first-order Sobol column admissible
for the first time; the practice first-order column remains withheld.

- Canonical model: `model/aa_group_model.py`
- Current model SHA-256: `c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`
- Modeled room capacity: 60, unchanged
- Confirmatory stochastic design: 400 paired seeds where comparisons permit pairing
- Expanded robustness: more parameter draws, perturbation distances, trajectories, structural
  variants, horizons, and integration steps, not 1,000 modeled members or 1,000 confirmatory
  seeds
- Governing plan: `plans/RELEASE-GATE-PLAN.md`
- Independent verification brief: `AGENT_VERIFY.md`
- Canonical workspace: the current Git checkout; all documented project paths are relative to
  the repository root and the checkout may be placed anywhere

Source files and hash-linked caches are authoritative. Generated Markdown and PDFs are not
authoritative until `tools/check_release.py` passes and their build dates follow every source.

## Corrected model interpretation

The correction round separates objects and estimands that earlier drafts combined:

- `B = S @ GOV.T` is an author-coded semantic overlap matrix. It is not executable coupling.
- `C = Snorm @ GOVW.T` is a normalized no-capacity linear map. It is not a trajectory effect.
- The state-dependent resource map and simulated trajectory contrasts are reported separately.
- Tradition 3 has distinct resource-governance and inverse-practice dropout-friction paths.
- Tradition 11 has distinct resource-governance and attraction paths.
- The recipient resource is opportunity per high-practice potential helper. Low and high
  practice are state proxies, not newcomer and veteran cohorts.
- Zero membership is permanently closed. Endpoint existence is `N > 0`; endpoint viability is
  `N > 5`; first crossing, recovery, final membership, and closure are distinct outcomes.
- Capability heterogeneity uses a mean-one lognormal draw, so changing dispersion does not
  mechanically change average capability.
- The practice scale is cardinal only inside the authored model and has no validated individual
  or clinical unit.

## Main confirmatory results

All rows below use 400 seeds and a 30-year horizon unless noted. Intervals and exact designs are
in `research/RELEASE-GATE-RESULTS.md` and the generating caches.

| Result | Corrected finding |
|---|---|
| Baseline | Mean final membership 17.80, 98.5% endpoint viable, no closures |
| Tradition 3 | Friction loss costs 2.96 members; governance loss 6.03; combined loss 11.05; combined loss closes 25.0% of groups |
| Tradition 11 | Pure attraction loss costs 5.42 members; governance loss 2.29; combined loss 5.88; none closes a group in these runs |
| Recipient override | Final-membership contrast 1.03, 95% interval -0.26 to 2.31; unresolved |
| Step 12 ablation | Costs 5.33 members and lowers maintenance capacity; the isolated Step 9 change is unresolved |
| Calibration | Original targets of 45 members and 9 experienced members fail: 17.80 and 1.25 are observed; no post-hoc retuning |
| Chapter 14 | High/low starts separate in 7 of 400 corrected endpoint environments; typical-member bistability is not a released baseline result |
| Composition | Both paired membership contrasts cross zero and no equivalence margin was specified; unresolved, not equality |
| Tradition comparison | At 20 years and adherence 0.85 to 0.50, seven of twelve contrasts resolve; T3 and T11 rows are mixed interventions |

The baseline integration-step comparison is unresolved at 200 paired seeds for all tested
steps from 1.0 to 0.125 weeks. Horizon checks continue to move from mean membership 29.34 at
10 years to 15.64 at 100 years. These are finite-horizon results, not a demonstrated steady
state or indefinite persistence.

## Robustness designs

The principal estimates stay at 400 seeds. Screens intentionally trade seeds per parameter
point for much broader parameter-space coverage and must not be called confirmatory.

| Design | Registered size | Role |
|---|---:|---|
| Global simultaneous perturbation | 1,002 independent draws | Three amplitudes, three common seeds per draw |
| Tiered parameter screen | 1,000 draws | Evidence-tiered ranges, three common seeds per draw |
| Randomized nonzero matrix screen | 1,000 draws | Magnitude robustness with sparsity held fixed |
| Multi-level OAT | 944 points | 118 registered values, two directions, four distances |
| Morris | 20 trajectories, 2,380 points | Screening interaction or nonlinearity, not separating them |
| Sobol | 1,024-row base, 11,264 points | Conditional variance decomposition on eight Morris leaders |
| Structural variants | 10,000 simulations | Five architectures by five scenarios by 400 seeds |

The registered set is 22 scalar defaults, 12 step speeds, 49 nonzero consumption cells, and
35 nonzero governance cells. These 118 values are not all model choices. The separate inventory
also records fixed constants, 108 structural zeros, equations, thresholds, initial conditions,
and experiment-design choices.

## Repository map

```text
manuscript/             Preface, introduction, and Chapters 1 to 25
model/                  Canonical model and all analysis scripts
research/               Caches, parameters, source ledger, claim register, and results
research/incorporated/  One directory per source: records committed, documents git-ignored
research/staged/        Two unread articles that could not be lawfully retrieved
reference/              Steps-and-Traditions primer and standalone PDF
appendix/               Technical appendix source
paper/                  LaTeX paper, companion notebook, and PDF
plans/                  Master and part plans plus the release-gate plan
tools/                  Notebook runner, checkers, inventory, summaries, and builders
build/                  Generated whole-book Markdown and PDF
```

## Reproduction and release checks

Run from the repository root after all required caches are complete. All three PDFs are built
before the final release check, because that check requires each rendered artifact to be newer
than every source feeding it:

```bash
python3 tools/inventory_model_choices.py
python3 tools/summarize_release_gate.py
python3 tools/summarize_robustness.py
python3 tools/build_corpus.py
python3 tools/regenerate_notebooks.py
python3 tools/run_notebook.py
python3 tools/run_notebook.py --paper
python3 tools/check_book.py
python3 tools/check_chapter.py reference/PRIMER-steps-and-traditions.md
python3 tools/check_portability.py
python3 tools/build_book.py
latexmk -pdf -interaction=nonstopmode paper/anonymity-as-an-aggregation-condition.tex
pandoc reference/PRIMER-steps-and-traditions.md \
  -o reference/PRIMER-steps-and-traditions.pdf --pdf-engine=xelatex
python3 tools/check_release.py
```

The first four commands regenerate files the release check requires but that are otherwise easy
to forget: `inventory_model_choices.py` writes `research/model-choice-inventory.json`, which
`check_release.py` reads for the registered-value counts; `summarize_release_gate.py` writes
`research/RELEASE-GATE-RESULTS.md`; `summarize_robustness.py` writes
`research/ROBUSTNESS-RESULTS.md`; and `build_corpus.py` normalizes the source corpus and rebuilds
any verification index whose stored SHA-256 no longer matches its file.
`tools/freeze_release_manifest.py` is separate: it snapshots hashes and JSON shapes for an audit
trail and is not part of the build.

`tools/build_book.py` prefers XeLaTeX and falls back to Tectonic. The paper's own header
documents two `pdflatex` passes, which is what `latexmk` performs; Tectonic also works if it is
the available engine. The paper emits auxiliary files that `.gitignore` excludes, so a build does
not dirty the working tree.

The paper is built from `paper/anonymity-as-an-aggregation-condition.tex`. The standalone
primer is built from `reference/PRIMER-steps-and-traditions.md`. A release also requires
rendering and visually inspecting all three PDFs for overflow, broken tables, duplicate
headings, stale language, and missing pages.

## Source boundary

The supplied corpus was worked through on 9 August 2026. Four of its six items are now under
`research/incorporated/`, alongside Maxwell (1950) and Golub and Jackson (2010): three American
Temperance Union documents and the source record for AA pamphlet P-17. The 1841 ATU annual report
is the earliest contemporary account the project holds of the Washingtonian founding, and is
independent of the three later narratives Chapter 1 had been relying on.

`research/staged/` now holds two journal articles only. Both are `verified_online` and unread,
because open-access retrieval returned a reCAPTCHA challenge and the project does not work around
access controls. They are not evidence and are not cited.

**No source document is committed.** This repository is public, several sources are in copyright,
and the public-domain ones are large scans that are not project outputs. Every source lives in
`research/incorporated/<ShortAuthor>_<Year>/`, and what is published for each is its citation, its
rights position, its provenance URL, the SHA-256 of each file, a short summary, and a
vocabulary-only verification index. The documents are local working files, excluded by
`.gitignore`. Re-acquire any of them from the recorded URL and check the hash.

That does not weaken citation checking. `tools/check_book.py` confirms that a chapter citing a
source for a subject is citing a work that contains it, using the indexes; with no documents
present at all, every citation-subject pair still verifies. Rebuild the corpus and its indexes
with `python3 tools/build_corpus.py`, or audit it with `--check`.

Current read status and claim support live in `research/SOURCES.md`.

## Limitations that remain

No simulation parameter is fitted to longitudinal AA group data, and the original calibration
fails: targets of 45 members and 9 experienced members return 17.80 and 1.25, and were not
retuned. The central mapping from specific Traditions to the Golub-Jackson assumptions remains an
author interpretation and is the book's least verified step. The governance and consumption
matrices are one person's judgment and need independent elicitation; the form and its
preregistered analysis exist at `research/GOVERNANCE-MATRIX-ELICITATION.md` and
`model/elicitation_compare.py`, and are waiting on respondents. Part Four's conclusions degrade
smoothly with disagreement about magnitudes and are largely gone under structural randomization,
where index-pairing fails on all twelve in 40.6 per cent of draws.

The model does not measure tenure, sponsorship matching, individual recovery, or clinical
outcomes. The recipient and both founder-composition contrasts are unresolved rather than null.
Chapter 14's separation is rare, 7 of 400 endpoint environments, not typical. Two Sobol factors
sit at or below the Monte Carlo noise floor, and the practice first-order column is withheld.
Every horizon is finite and membership is still moving at 100 years, so no steady-state or
indefinite-persistence claim is available.

Two journal articles remain unread under `research/staged/`: retrieval returned an access
challenge and this project does not work around access controls. Pagano et al. (2004) is the
consequential one, because it bears on Chapter 15 and on the recipient resource.

Nothing in this repository should be used to assess an individual's recovery.
