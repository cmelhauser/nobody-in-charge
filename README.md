# Nobody in Charge

*How a Fellowship of Drunks Solved a Problem in Mathematics Without Knowing It*

Human Author: Christopher Melhauser (christopher.melhauser@gmail.com)
AI Writing Collaborator: theonlymuffinbot (theonlymuffinbot@outlook.com), using a mix of
Anthropic Claude Opus 5 and OpenAI GPT-5.6 Sol and Terra models

See [ATTRIBUTION.md](ATTRIBUTION.md) for the authorship and rights statement, and
[LICENSE](LICENSE) for the public-domain dedication and courtesy-credit request.

This repository contains a complete 25-chapter manuscript, an academic paper, a technical
appendix, a Steps-and-Traditions primer, the executable model, analysis scripts, cached
results, source ledgers, and reproducible PDF builds.

## Current status

The release-gate correction round opened on 6 August 2026 and closed on 9 August 2026. Every
checker passes: `check_release` with 148 checks, `check_book` with none failing, the primer
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
- Current tag: `v0.9.0`, published 23 August 2026 as a GitHub
  [pre-release](https://github.com/cmelhauser/nobody-in-charge/releases/tag/v0.9.0) with the
  three rendered PDFs attached, marked pre-release because the elicitation round is open, not
  because anything in it is provisional. See `RELEASING.md` and `CHANGELOG.md`.

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
| Decay-ordering confirmation | 4,800 simulations | Referral against attraction loss at four decay rates by 400 paired seeds |
| Decay-reversal location | 3,600 simulations | The same design at three more decay rates, locating the membership reversal |

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
research/staged/        Acquisition report and metadata: provenance, not evidence
research/elicitation/   The elicitation packet: LaTeX sources, style, and build script
reference/              Steps-and-Traditions primer and standalone PDF
appendix/               Technical appendix source
paper/                  LaTeX paper, companion notebook, and PDF
plans/                  Master and part plans plus the release-gate plan
tools/                  Notebook runner, checkers, inventory, summaries, and builders
build/                  Generated whole-book Markdown and PDF
```

## Tests and CI

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest
```

The suite runs without any source document, because every source under
`research/incorporated/` is git-ignored and citation checking works from the committed
verification indexes.

The coverage gate is 100 per cent of `model/aa_group_model.py`, the canonical model, enforced
by `.coveragerc`. That file is hash-frozen and is pure computation, so it is tested
exhaustively; `tests/test_release_invariants.py` also pins its SHA-256, the room capacity of
60, the viability threshold of 5, and the 22 + 12 + 49 + 35 = 118 decomposition. The scripts
under `tools/` are batch jobs and entry points rather than libraries, so they sit outside the
coverage gate and are covered by `tests/test_tools_integration.py`, which runs each one for
real.

Work happens on a branch and merges through a pull request; `main` takes no direct commits.
`RELEASING.md` covers branch naming, the version scheme and what a tag has to have earned;
`CHANGELOG.md` records what changed between tags.
`lint`, `unit-tests` and `checkers` run on every pull request, `documents` only on `main`, so a green pull
request is not a green release and the local runner below is what closes that gap.

To run what CI runs, in the same order, on this machine:

```bash
tools/run_ci_locally.sh
```

It takes an optional `lint`, `unit-tests`, `checkers`, `checks` or `documents` argument to run one job.
The workflow file is the authority and nothing enforces that the two stay in step, so change both
together. The one thing the script cannot check is the one thing that has actually broken CI:
whether a fresh runner can obtain pandoc, tectonic and the font.

GitHub Actions runs four jobs, split by what can be checked without a network and by what depends
on the Python version. `lint` runs ruff, actionlint and shellcheck, and asserts that the canonical
model takes no lint waiver. `unit-tests` runs pytest and the model hash: on pull requests it uses
Python 3.12 only; on `main` it runs 3.11, 3.12 and 3.13. `checkers` runs once on 3.12: corpus
drift, portability, the book-level checks, `check_docs.py`, and 142 of the 148 release-gate
checks, reporting the other six as skipped. `documents` runs on `main`, installs a pinned pandoc, tectonic and the book font, rebuilds
all three PDFs, requires zero overfull boxes, checks the rendered PDFs with `tools/check_pdfs.py`,
and runs the full fail-closed gate. See `.github/workflows/ci.yml`.

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
python3 tools/check_docs.py
python3 tools/build_book.py
latexmk -pdf -interaction=nonstopmode paper/anonymity-as-an-aggregation-condition.tex
python3 tools/build_primer.py
python3 tools/check_pdfs.py
python3 tools/check_release.py
```

Building the book and the primer needs **pandoc 3.10.2**, a TeX engine, and the **TeX Gyre
Pagella** font, which both builds request from fontconfig by name.

The pandoc version is not incidental. Pandoc computes the column widths of every table in the
book, and it does not compute them the same way across versions: a different release gave the
paper's seven-column scenario table a first column of 0.1154 where 3.10.2 gives 0.2577, which put
a row outside the type block. Continuous integration installs 3.10.2 for that reason, and a local
build with a different pandoc may place tables differently. Raise the pin deliberately, in
`.github/workflows/ci.yml`, and re-read the rendered PDFs when you do. On Debian or Ubuntu that font is
`fonts-texgyre`; on macOS install the OTFs from the TeX Gyre project or a TeX distribution.
Without it XeTeX stops with an unrecoverable error before it typesets anything, which is what
CI did on 17 August 2026 when the font turned out to be present only in the author's personal
font library.

The primer is built by `tools/build_primer.py` and not by a hand-typed pandoc command. The
script holds the one inch margins and the line-breaking settings that keep long file paths
inside the type block, so the Markdown source stays free of LaTeX and
`tools/check_chapter.py` can read it as prose. A bare `pandoc` call renders the primer at
LaTeX's default article margins and is not the release artifact.

The typeset copy of the 1939 working-manuscript note,
`build/WorkingManuscript_1939-edits-and-suggested-uses.pdf`, is built the same way by
`tools/build_note.py` from `research/incorporated/WorkingManuscript_1939/edits_and_suggested_uses.md`,
with the primer's typography. It cannot sit beside its source, because every PDF under
`research/incorporated/` is treated as a source document and never committed. It is a reading
copy rather than a release artifact, and the release gate does not check it.

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

The two journal articles that could not be retrieved automatically were obtained by hand on
10 August 2026 and read in full, so the staged corpus is now fully incorporated. What remains
under `research/staged/` is the acquisition report and metadata, which are provenance rather than
evidence.

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

Five of the 44 sources are held as record only, with no document at any time: Kurtz (1991), in
copyright; DeGroot (1974) and the April 1946 *A.A. Grapevine* article, whose located scans have
unverified posting authorization and which the project's rights review directs be cited within
limits rather than archived; Rohr (2011), whose consulted copy was an unauthorized posting; and
*Tricycle* on the 2019 Recovery Dharma schism, paywalled past its opening. The authority for the
category is `"record_only": true` in each source's `metadata.json`. Six others were record only
until 13 September 2026, when the Human Author directed that the corpus hold a lawful copy of
every source it can: AAWS pamphlet P-17, *Twelve Steps and Twelve Traditions*, the Kurtz talk (in
the Human Author's own transcription), SMF-132, the short-form Twelve Concepts and the fourth
edition of the Big Book. The same day added the 2024-26 *A.A. Service Manual* with the full
Twelve Concepts.

Recovery Dharma (2023), added 16 August 2026 for appendix A12, is held on the ordinary footing:
document present locally, git-ignored, hashed, and indexed. It is the one source in the corpus
whose licence, CC BY-NC-SA 4.0, would permit committing the document outright. It is git-ignored
anyway, because the rule is uniform.

The 1939 working manuscript (`WorkingManuscript_1939`, Hazelden's 2010 facsimile), added 12
September 2026, is held on the same footing at the Human Author's direction, although it is in
copyright and in print: its reading copy was made from the Human Author's photographs of their own
copy, and like every document here it is git-ignored and never committed.

**Reading a copyrighted work and holding one are different acts, and the rule here is about
holding.** Several chapters formerly declined to read AA literature on copyright grounds. That was
a category error, and correcting it on 10 August 2026 changed Chapters 8, 10, 16, 17 and 25: the
1953 commentary supplied the book's own thesis in Wilson's words, the strongest objection to it,
and the disproof of the index-pairing conjecture.

Current read status and claim support live in `research/SOURCES.md`.

## Limitations that remain

No simulation parameter is fitted to longitudinal AA group data, and the original calibration
fails: targets of 45 members and 9 experienced members return 17.80 and 1.25, and were not
retuned. The central mapping from specific Traditions to the Golub-Jackson assumptions remains an
author interpretation and is the book's least verified step. The governance and consumption
matrices are one person's judgment and need independent elicitation; the form and its
preregistered analysis exist at `research/GOVERNANCE-MATRIX-ELICITATION.md` and
`model/elicitation_compare.py`, and are waiting on respondents. The packet to send is
`research/elicitation/`, five typeset documents built by `sh research/elicitation/build.sh`.
Send `1-respondent-form.pdf`; **never send `4-collator-notes.pdf`**, which states how many rows
the book leaves empty and which they are, and so destroys the round for anyone who reads it. Part Four's conclusions degrade
smoothly with disagreement about magnitudes and are largely gone under structural randomization,
where index-pairing fails on all twelve in 40.6 per cent of draws.

The model does not measure tenure, sponsorship matching, individual recovery, or clinical
outcomes. The recipient and both founder-composition contrasts are unresolved rather than null.
Chapter 14's separation is rare, 7 of 400 endpoint environments, not typical. Two Sobol factors
sit at or below the Monte Carlo noise floor, and the practice first-order column is withheld.
Every horizon is finite and membership is still moving at 100 years, so no steady-state or
indefinite-persistence claim is available.

Greenfield and Tonigan (2013) raise a limitation no sensitivity analysis in this project can
reach: the model gives each step one practice level, while their factor analysis separates
behavioural from spiritual step-work, with different predictors, different time paths, and only
the spiritual component predicting abstinence. Every design here varies the values of the dials;
none varies the decision to have one dial. Chapter 12 states the objection.

Nothing in this repository should be used to assess an individual's recovery.
