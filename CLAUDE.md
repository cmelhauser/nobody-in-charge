# Project instructions

Read this file, `plans/RELEASE-GATE-PLAN.md`, and `AGENT_VERIFY.md` before changing the
project. Work directly in this repository. Do not delete source material or caches without
explicit user authorization. Preserve unrelated user work.

## Authority and current state

The source hierarchy is:

1. `model/aa_group_model.py` for executable semantics;
2. hash-linked analysis scripts and complete caches for numerical results;
3. manuscript, paper, appendix, primer, plans, and ledgers for interpretation;
4. generated Markdown and PDFs.

Do not make prose agree with a stale cache or make a cache agree with prose by hand. The current
canonical model SHA-256 is
`c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`.

The modeled room capacity remains 60. Confirmatory stochastic claims use 400 seeds, paired by
common random numbers where possible. The expanded robustness round increases parameter draws,
perturbation distances, structural variants, trajectories, horizons, and integration-step
checks. It does not increase room size or replace the 400-seed confirmatory rule with 1,000
seeds.

## Model language that must remain exact

- `B = S @ GOV.T` is semantic overlap, not executable coupling.
- `C = Snorm @ GOVW.T` is the normalized no-capacity linear map, not a trajectory effect.
- State-dependent resource maps and simulated finite differences are separate objects.
- Tradition 3 has resource-governance and inverse-practice dropout-friction paths.
- Tradition 11 has resource-governance and attraction paths.
- Ordinary changes in T3 or T11 adherence move both paths and are mixed interventions.
- The recipient resource is low-practice opportunity per high-practice potential helper.
  Low and high practice are not tenure cohorts.
- Capability uses a mean-one lognormal draw. `het_sd` changes dispersion, not average
  capability by construction.
- Zero membership is absorbing closure. Existence is `N > 0`; endpoint viability is `N > 5`;
  first crossing, recovery, final membership, and closure are different estimands.
- The constructed practice scale is cardinal only inside this model and has no validated
  clinical or individual unit.
- The Chapter 13 rho exercise is proxy averaging under oracle-known inputs and loadings. It is
  not validation of a latent-variable estimator and does not establish a required instrument
  count.
- Founding composition changes all state-dependent channels. Its paired contrasts are
  unresolved without a prespecified equivalence margin.
- Chapter 14's old frozen-environment high state, separatrix, and hysteresis are retired
  diagnostics. In corrected endpoint environments, high and low starts separate in only 7 of
  400 cases.

## Statistical rules

Every confirmatory stochastic statement must give the estimand, conditioning rule, seed count,
horizon, integration step, pairing, and interval. Use Wilson intervals for one-condition binary
fractions and paired intervals or paired tests for contrasts. A common-random-number design is
more efficient; it is not fewer replications.

Three- and five-seed parameter-point designs are screens. Report strict support, ties, and
reversals separately. Do not call parameter points independent replications of the stochastic
model. Do not use absence of an OAT effect as evidence that a parameter is irrelevant. A
multiplicative screen cannot move a structural zero.

The release designs are:

- 1,002 global draws across 12.5%, 25%, and 50% amplitudes;
- 1,000 tiered draws and 1,000 randomized-matrix draws;
- 944 multi-level OAT points over 118 registered values;
- 20 Morris trajectories;
- a 1,024-row Sobol base design on eight post-Morris leaders;
- 10,000 structural simulations;
- 400-seed principal T3, T11, recipient, service, trajectory, and composition contrasts;
- 200-seed integration-step and horizon checks.

The 118-value decomposition is 22 scalar defaults, 12 step speeds, 49 nonzero `S` cells, and
35 nonzero `GOV` cells. Call these registered sensitivity values, not all parameters or all
choices. Use competition rank `1 + count(values greater than the indexed value)` and preserve
ties.

## Synchronization rule

Any change to the model or a public number must be propagated in the same work session to every
affected layer:

- analysis scripts and caches;
- both notebooks;
- manuscript chapters and preface;
- `appendix/APPENDIX.md`;
- `paper/anonymity-as-an-aggregation-condition.tex`;
- `reference/PRIMER-steps-and-traditions.md`, including its plain-language paragraph;
- `research/PARAMETERS.md`, `research/SOURCES.md`, and claim registers;
- `README.md`, all applicable plans, `research/progress-log.md`, and `AGENT_VERIFY.md`;
- the book, paper, and primer PDFs.

Search the whole repository for retired values and phrases. The release checker supplements
that search; it does not replace reading the surrounding claim.

## Source boundary

`research/staged/` is an intentionally unincorporated next-round corpus. File presence does not
make a source read, cited, or current evidence. Do not use staged material to repair claims in
this round and do not recommend it as accidentally missing. Maxwell (1950) and Golub and
Jackson (2010) are already-used sources stored under `research/incorporated/`. The current
authority for read status, provenance, and claim support is `research/SOURCES.md`.

Verify quotations against an original page image when available. OCR and retyped texts are
search aids. Distinguish read in full, abstract-only, cited at a remove, referenced but not
reproduced, and not obtained.

## Manuscript conventions

- No em dashes in the author's prose. Preserve punctuation inside quotations.
- Use plain-language equations in manuscript Markdown; the paper remains LaTeX.
- No subheadings or tables in a chapter's narrative. Use horizontal rules between narrative
  sections; tables belong in The Machinery.
- Every chapter ends with The Machinery and five reference-status headings in this order:
  Read in full; Cited at a remove; Referenced but not reproduced; Internal, and reproducible
  from this repository; What was not read.
- A number from a stochastic run carries its uncertainty and design. Deterministic algebra is
  labeled deterministic.
- Nothing in the project may be written as advice about an individual's recovery.

## Reproduction

Run from the repository root:

```bash
python3 tools/run_notebook.py
python3 tools/check_book.py
python3 tools/check_chapter.py reference/PRIMER-steps-and-traditions.md
python3 tools/check_release.py
python3 tools/build_book.py
```

The standalone primer must be rebuilt from its Markdown and the paper from its LaTeX source.
Render and visually inspect all three PDFs. Confirm that each artifact is newer than every
source that feeds it, has no clipping or broken tables, and contains no retired language.

## Release discipline

Do not claim steady state, indefinite persistence, universal sensitivity, causal composition
effects, or path-specific T3/T11 effects from mixed interventions. Do not describe an interval
crossing zero as no effect. Do not retune the failed 45-member and 9-experienced-member targets
after seeing the correction. Do not approve release until every required cache is complete and
hash-current, both notebooks execute cleanly, all checkers pass, and an independent verifier can
return the documented release verdict using `AGENT_VERIFY.md`.
