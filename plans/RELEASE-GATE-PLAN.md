# Release-Gate Correction Plan

Date opened: 6 August 2026

Status: **implementation complete except for one checker; this plan supersedes conflicting
quantitative or status language in the older part plans until the final verification pass closes
it.**

As of 9 August 2026 every analysis in section 2 is complete and hash-current, including the 944
multi-level OAT points, the 20-trajectory Morris screen, and the 1,024-row Sobol design.
`tools/check_release.py` passes with 136 checks, portability passes, the primer chapter check is
clear, and both notebooks execute clean. `tools/check_book.py` does not pass: it reports 102
failures, of which 100 are manuscript figures no longer traceable to the regenerated notebook.
That is the sole blocking item and it is documented in `../HANDOFF.md` section 5. The release
criteria in section 4 below are therefore not yet met.

The original V1-V18 audit findings were resolved into the decisions below. The current
`../AGENT_VERIFY.md` is the independent, fail-closed verification brief for the corrected
release rather than the historical backlog. This plan records the authorized decisions and
execution order. Source files remain authoritative over caches and rendered artifacts.

## 1. Approved model and interpretation decisions

1. **Formal theorem.** Define `A_ij` as attention member i gives member j. Direct attention
   received is column/in-degree information; long-run DeGroot influence is the normalized left
   stationary vector. State the Golub-Jackson result only in terms of maximum stationary
   influence under its assumptions. Add an iid Gaussian premise wherever the exact
   `sqrt(2/pi)` mean-absolute-error expression is used. A Tradition violation is not sufficient
   for failure unless it produces persistent stationary-influence concentration.
2. **Coupling.** Keep raw `B = S @ GOV.T` as an author-coded **semantic overlap matrix**. It is
   not the executable model's coupling. Name the normalized no-capacity diagnostic
   `C = Snorm @ GOVW.T` and the state-specific capacity map separately. Part Four's raw ranks,
   loads and threshold experiments remain semantic analyses and must be labeled as such. Never
   mix `B`, `C`, a fixed-state coefficient map, or a trajectory finite difference under one
   name. Remove the unsupported literal weight-1 versus beta transmission ratio.
3. **Recipient resource.** Retain the current monotone low-practice-to-high-practice ratio as
   **recipient opportunity per high-practice potential helper**. It is not helper capacity and
   neither class is a tenure cohort. Rename `new`/`exp` outputs as low-practice/high-practice
   proxies. Replace the structural `norecip` experiment with a one-mechanism relaxation that
   holds `S`, normalized weights and `BETA` fixed and sets recipient opportunity to its
   unconstrained level. Report paired contrasts.
4. **Tradition 3.** Retain both executable paths: governance of resources and inverse-practice
   dropout friction. Describe the latter as low-practice protection, not newcomer retention.
   Add separate resource and friction controls and a paired 2x2 factorial. Any admission test
   must separately control governance, friction and arrival and must not force zero inflow by
   construction.
5. **Tradition 11.** Retain both executable paths: resource governance and attraction. Add
   separate controls and a paired 2x2 factorial. Call the old `T11=0` condition mixed T11 loss.
   Use pure attraction loss, with governance held at baseline, in any referral-versus-attraction
   comparison.
6. **Closure and outcomes.** Keep `N=0` permanently closed. Replace ambiguous survival language
   with separate endpoint existence `N>0`, endpoint viability `N>5`, actual final N, first
   half-week crossing of `N<=5`, recovery above 5, and first closure. The viability threshold is
   an analysis choice, not a model parameter. Retain nonabsorbing small groups and run threshold
   sensitivity rather than recoding them to zero.
7. **Heterogeneity.** Mean-center all lognormal capability draws as
   `exp(N(-het_sd**2/2, het_sd))` for founders and arrivals, including duplicated simulators.
   This makes `het_sd` a dispersion parameter with mean capability fixed at one. All dependent
   caches must be regenerated.
8. **Rho exercise.** Keep it as a modest output-proxy-averaging demonstration under oracle-known
   regressors. It does not identify a nonlinear latent-variable estimator and cannot establish
   a practical three-instruments-per-latent rule. Retain endogeneity as unresolved.
9. **Composition.** Treat the three founding-state designs as paired under shared random streams
   and as changing every state-dependent channel. The contrast is unresolved unless its
   confidence interval excludes a prespecified equivalence margin; do not call the current null
   equality or “nothing.”

## 2. Methodology decisions

- Report strict support, ties, reversals and weak orderings separately. Three- and five-seed
  parameter-point analyses are screens, not confirmatory replications. Use 400 paired seeds for
  the principal baseline, T3, T11, recipient and Part Five contrasts; give Wilson intervals for
  proportions and paired intervals for continuous contrasts. Expand perturbation coverage,
  not modeled group size or the confirmatory seed rule: 1,002 global draws across three
  amplitudes, 1,000 tiered draws, 1,000 randomized-matrix draws, 944 multi-level OAT points,
  20 Morris trajectories, and a 1,024-row Sobol base design.
- Preserve the registered decomposition 22 scalars + 12 step speeds + 49 nonzero `S` cells +
  35 nonzero `GOV` cells, but call it **118 registered sensitivity values**, not all choices.
  Inventory fixed, derived, structural-zero and experiment-design choices separately and report
  scenario-specific effective dimension.
- Use competition/minimum rank `1 + count(values > own_value)` and display all tied principals.
- Treat the constructed practice scale as cardinal inside the model for within-model arithmetic,
  while stating that it has no external empirical unit and is not an individual recovery scale.
- Use endpoint viability language for current 30-year tables, add first-passage/recovery
  diagnostics, and reserve death/kill/survival event language for actual closure or explicitly
  defined event-time outcomes.
- Store code hash, model hash, dependency hashes, job IDs, seed coverage, horizon, step size,
  completion counts and cache schema version with every regenerated cache. Scripts must run
  from the repository root and write the exact files the notebooks load.

## 3. Correction order

1. Freeze the pre-correction manifest and complete a verdict table for V1-V18.
2. Refactor the model API for split T3/T11 controls, recipient override, mean-centered
   heterogeneity and complete trajectory/event records; add unit-level algebra and monotonicity
   assertions before running simulations.
3. Regenerate the principal 400-seed factorials and Part Five contrasts, then horizon,
   sensitivity, composition and uncertainty caches under one code identity. Re-estimate the
   state-dependent resource environment used by Chapter Fourteen; its individual-attractor
   calculation may not reuse constants obtained under the retired uncentred heterogeneity draw.
4. Rebuild the book notebook from those caches. Replace or explicitly retire the stale paper
   notebook; no public artifact may contain superseded ten-seed, thirty-pair or single-draw
   results.
5. Correct the appendix, manuscript, paper and primer from verified outputs. The appendix must
   include the actual matrices, founder conditions, hard-coded choices, complete dependency map
   and nonduplicated numbering.
6. Reconcile the parameter ledger, source ledger, claim register, README, CLAUDE and progress
   log. Staged sources remain unincorporated unless separately authorized.
7. Build a cross-artifact release checker covering cache completeness, provenance, bibliography,
   stochastic claim design/intervals, superseded phrases and artifact freshness.
8. Rebuild and visually inspect the book, paper and standalone primer PDFs.

## 4. Release criteria

- Every identity, cache, numeric, prose, source-boundary, notebook, PDF, repository-identity,
  and portability check in
  `AGENT_VERIFY.md` has a reproducible result.
- No public prose calls semantic `B` executable, calls low practice tenure, calls mixed T11 loss
  pure attraction, or calls endpoint `N>5` an absorbing death event.
- Every stochastic headline gives its estimand, conditioning, horizon, step, seeds, pairing and
  interval; screening results are labeled screening.
- All regenerated caches pass completeness, uniqueness, finite-value and hash checks.
- Both notebooks execute cleanly or the paper notebook is explicitly retired everywhere.
- The source ledger covers book and paper references with read/status and claim support.
- Book, paper and primer sources agree, their PDFs are newer than the sources, and rendered-page
  inspection finds no new clipping, broken references or stale results.
