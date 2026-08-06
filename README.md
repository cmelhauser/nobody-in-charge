# Nobody in Charge

*How a Fellowship of Drunks Solved a Problem in Mathematics Without Knowing It*

This repository contains a complete 25-chapter manuscript, an academic paper, a technical
appendix, a Steps-and-Traditions primer, the executable model, analysis scripts, cached
results, source ledgers, and reproducible PDF builds.

## Current status

The project is in a release-gate correction round opened 6 August 2026. The principal model
corrections and 400-seed confirmatory analyses are complete. Expanded structural and parameter
sensitivity runs are being regenerated against one model identity before the final notebooks,
appendix, PDFs, and independent verification verdict are closed.

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
research/incorporated/  Local copies of sources already used by the project
research/staged/        Supplied next-round corpus, deliberately not incorporated
reference/              Steps-and-Traditions primer and standalone PDF
appendix/               Technical appendix source
paper/                  LaTeX paper, companion notebook, and PDF
plans/                  Master and part plans plus the release-gate plan
tools/                  Notebook runner, checkers, inventory, summaries, and builders
build/                  Generated whole-book Markdown and PDF
```

## Reproduction and release checks

Run from the repository root after all required caches are complete:

```bash
python3 tools/run_notebook.py
python3 tools/check_book.py
python3 tools/check_chapter.py reference/PRIMER-steps-and-traditions.md
python3 tools/check_portability.py
python3 tools/check_release.py
python3 tools/build_book.py
```

The paper is built from `paper/anonymity-as-an-aggregation-condition.tex`. The standalone
primer is built from `reference/PRIMER-steps-and-traditions.md`. A release also requires
rendering and visually inspecting all three PDFs for overflow, broken tables, duplicate
headings, stale language, and missing pages.

## Source boundary

`research/staged/` contains a supplied corpus reserved for the next iteration. Its presence is
not evidence that an item was read, cited, or incorporated. During this round, staged sources
must not be used to rewrite claims or reported as accidentally missing. Maxwell (1950) and
Golub and Jackson (2010), which were already part of the project, are under
`research/incorporated/`. Current read status and claim support live in `research/SOURCES.md`.

## Limitations that remain

No simulation parameter is fitted to longitudinal AA group data, and the original calibration
fails. The central mapping from specific Traditions to the Golub-Jackson assumptions remains an
author interpretation. The governance and consumption matrices need independent elicitation.
The model does not measure tenure, sponsorship matching, individual recovery, or clinical
outcomes. The composition comparison is not causal evidence about real groups. The staged
reference corpus remains deferred by design.

Nothing in this repository should be used to assess an individual's recovery.
