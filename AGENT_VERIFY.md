# Independent Agent Verification Brief

## Run the tests first

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest
```

This needs no source document and finishes in seconds. It asserts the canonical model hash,
room capacity 60, viability threshold 5, the 22 + 12 + 49 + 35 = 118 decomposition, and the
semantics the appendix describes, at 100 per cent coverage of `model/aa_group_model.py`. A
failure here tells you the model or its invariants moved, which is worth establishing before
reading anything else. GitHub Actions runs the same suite plus, on `main`, a job that rebuilds
the PDFs and runs the release gate.


## Purpose

Verify the release of *Nobody in Charge* independently. Do not repair, reinterpret, or retune
the project while verifying it. Report discrepancies with file and line references, preserve
the source boundary below, and distinguish a failed check from an unresolved scientific claim.

Canonical project: the Git checkout containing this file. Treat its repository root as `.` and
resolve every project path relative to that root. No verification step depends on the checkout's
parent directory or on a particular user account, host, or workspace layout.

Canonical model SHA-256:

`c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`

The modeled room capacity is 60. Confirmatory stochastic comparisons use 400 seeds. Expanded
robustness comes from additional parameter draws, perturbation distances, structural variants,
trajectories, horizons, and integration steps, not from 1,000 modeled members or a blanket
1,000-seed confirmatory rule.

The current tag is `v0.9.0`, at this SHA-256, published as a GitHub pre-release on 23 August
2026. `RELEASING.md` and `CHANGELOG.md` are authoritative on what that tag and that publication
required and recorded; do not treat a passing verification here as license to cut a new one.

## Source boundary

Three statuses must remain distinct.

1. **Used/current project.** Current claim support and read status are in
   `research/SOURCES.md`.
2. **Incorporated local copies.** `research/incorporated/` holds 40 sources: those the project
   used before the acquired corpus arrived, the six promoted out of the staged corpus, six
   added on 10 August 2026, the April 1946 *A.A. Grapevine* article, DeGroot (1974), the 1939
   Big Book text in a 1999 reprint, AAWS *Twelve Steps and Twelve Traditions* (1953), Rohr (2011)
   and the Kurtz talk of about 1984, Recovery Dharma (2023) added on 16 August 2026 for
   appendix A12, and four added on 17 August 2026: AAWS service material SMF-132, the Twelve
   Concepts for World Service in short form, *Tricycle* on the 2019 Recovery Dharma schism, and
   the fourth edition of the Big Book, which supports Appendix A13.7; and, added on 12 September
   2026, Hazelden's facsimile of the annotated 1939 working manuscript; and, added on 13 September
   2026, the 2024-26 *A.A. Service Manual* with Bill W.'s full Twelve Concepts. A directory's leading token
   must be at least three characters and distinctive, because `check_book.py` identifies a
   source in prose by that token.
   `TwelveAndTwelve` and `KurtzTalk` are deliberately distinct tokens: `AAWS` and `Kurtz` were
   already taken by P-17 and by Kurtz (1991), and two directories sharing a leading token would
   collide.
3. **Staged/nothing outstanding.** `research/staged/` no longer holds any unread source. Both
   journal articles were obtained by hand on 10 August 2026 and read in full, and are under
   `research/incorporated/`. What remains staged is the acquisition report and metadata, which are
   provenance rather than evidence. If new material is ever staged, presence does not make a
   source read, cited, or available as evidence, and a finding it might answer should be labelled
   `deferred corpus may resolve`.

**No source document is committed, and their absence is intentional.** This repository is public.
As of 9 August 2026 `.gitignore` excludes every `.pdf`, `.txt`, `.djvu` and `.epub` under
`research/incorporated/` and `research/staged/`. Sources live in
`research/incorporated/<ShortAuthor>_<Year>/`, and what is published for each is `citation.md`,
`metadata.json` with rights, provenance URL and SHA-256, `source_summary.md`, and a
vocabulary-only verification index.

**Do not report a missing document as a missing source, and do not restore one.** To check a
source, re-acquire it from the URL in its `metadata.json` and compare the recorded SHA-256.

**Five sources are held as record only, with no document at any time.** This is a distinct
category from the git-ignored documents, and a verifier should not report either as a missing
source. They are Kurtz (1991), in copyright; DeGroot (1974) and the April 1946 *A.A. Grapevine*
article, consulted on 10 August 2026 from scans whose posting authorization is unverified, which
the project's own rights review directs be cited and quoted within limits rather than archived;
Rohr (2011), whose consulted copy was an unauthorized posting; and *Tricycle* on the 2019 Recovery
Dharma schism, paywalled past its opening. That is the full five, and `"record_only": true` in
each `metadata.json` is the authority. Six others were record only until 13 September 2026, when
the Human Author directed that the corpus hold a lawful copy of every source it can: AAWS pamphlet
P-17, *Twelve Steps and Twelve Traditions*, the Kurtz talk, SMF-132, the short-form Twelve
Concepts and the fourth edition of the Big Book. Each record keeps the citation, the rights position, the hash
of the copy consulted, and the passages verified from it.

`RecoveryDharma_2023`, added 16 August 2026, is **not** in that category. It is an ordinary
git-ignored source with a document, a SHA-256 and a verification index. It is worth one line here
only because its licence, CC BY-NC-SA 4.0, is the single licence in the corpus that would permit
committing the document; the project git-ignores it anyway, so the uniform rule holds without
exception.

Rohr (2011) carries the corpus's strongest provenance objection, recorded in its `metadata.json`:
the copy consulted was an unauthorized posting of a current in-print title. It was not retained,
its bibliographic record was confirmed independently, and both claims drawn from it are absence
claims. Confirm any Rohr citation against a lawfully obtained edition before release.

**Citation checking must still pass with no documents present.** Each verification index records
the source's vocabulary and, because a vocabulary set has no word order, which registered subjects
the document contains, decided against the real text at build time and stamped with that file's
SHA-256. Confirm this rather than assume it: move the documents aside and rerun
`tools/check_book.py`. It reported 55 citation-subject pairs across 18 indexed sources, all supported,
with zero documents present. If a re-acquired file's hash differs from its index, the index is stale;
rebuild with `python3 tools/build_corpus.py` rather than trusting it, and `--check` reports drift.

Two limitations are declared rather than hidden: the subject matcher is deliberately tolerant of
OCR noise, so short subjects can match spuriously, which was equally true when the check ran
against full text; and an index shows a word occurs somewhere in a work, which is weaker than a
page reference. Quotations are verified against page images, as the ATU 1841 and P-17 records
show.

The Maxwell copy remains a retyped reproduction with visible transcription errors, not a scan
of the journal. Moving the original project PDF and text to `research/incorporated/Maxwell_1950/`
did not upgrade that status. The later staged Maxwell PDF was byte-identical and was removed.
The complete Golub-Jackson package is under `research/incorporated/Golub_Jackson_2010/`.

## Authority order

When two artifacts disagree, use this order:

1. `model/aa_group_model.py` for executable semantics;
2. complete JSON caches whose model and analysis hashes match;
3. generated `research/RELEASE-GATE-RESULTS.md` and
   `research/ROBUSTNESS-RESULTS.md`;
4. executed verification notebooks;
5. appendix, paper, primer, manuscript, plans, README, and PDFs.

A PDF or Markdown table cannot override a hash-linked cache. A cache from the retired
uncentred-capability model is not current evidence.

## Verification sequence

### 1. Confirm identity and inventory

From the project root:

```bash
shasum -a 256 model/aa_group_model.py
jq '{model_sha256, registered_set, authored_structural_zeros,
     protective_index_step_consumption_cells}' research/model-choice-inventory.json
```

Expected:

- model hash exactly as printed above;
- room capacity 60;
- 22 scalar defaults, 12 Step speeds, 49 nonzero `S` cells, and 35 nonzero `GOV` cells;
- 118 registered sensitivity values, not all model choices;
- 108 structural zeros across `S` and `GOV`;
- 17 protective index-Step consumption cells, not 35.

### 2. Inspect executable semantics

Verify directly in `model/aa_group_model.py`:

- `semantic_overlap()` returns raw `S @ GOV.T` and is documented as semantic only;
- `executable_linear_coupling()` returns normalized `Snorm @ GOVW.T`;
- resource supply is state-dependent and distinct from both matrices;
- capability is `exp(N(-sigma^2/2, sigma))`, with arithmetic expectation one;
- the recipient capacity uses low-practice members per high-practice potential helper;
- `recipient_override` changes only recipient capacity;
- Tradition 3 exposes separate resource-governance and dropout-friction controls;
- Tradition 11 exposes separate resource-governance and attraction controls;
- the base model has no Tradition 3 arrival path;
- dropout is keyed to early-step practice, with low-practice friction;
- exit is evaluated before arrival and zero membership is permanently absorbing;
- existence is `N > 0` and endpoint viability is `N > 5`;
- histories contain time zero and record first crossing, recovery, and closure separately.

### 3. Validate every registered cache

Run:

```bash
python3 tools/check_release.py
```

If this fails because PDFs are older than their sources, build and visually verify the PDFs,
then rerun it. Do not waive any cache-status, model-hash, analysis-hash, expected-job-count,
notebook, source-boundary, or stale-language failure.

`tools/check_docs.py` is a separate question from the gate and worth running early: it re-derives
the counts this repository states about itself, so a failure there means a document disagrees with
the tree rather than with a cache.

`tools/run_ci_locally.sh` runs all four continuous-integration jobs here, which is the quickest
way to reach the same 148 checks along with the tests, the builds and the overfull gate. Verifying a
release means running `check_release.py` with the artifacts built, not `--skip-artifacts`: that
flag omits the six rendered-artifact checks and exists only for a fresh clone, where every file
carries one checkout timestamp.

Expected major cache sizes:

| Cache | Required work |
|---|---:|
| `release_gate_results.json` | 3,200 jobs |
| `scenarios_hiseed.json` | 2,400 |
| `ch13_reps.json` | 3,200 |
| `ch14_individual.json` | 400 endpoint environments |
| `ch14_sweep.json` | 3,200 |
| `ch15_service.json` | 1,200 |
| `core_thresholds.json` | 400 |
| `part5.json` | 4,800 |
| `mc_error.json` | 2,600 |
| `tradition_paired.json` | 5,200 |
| `structural.json` | 10,000 |
| `sens3.json` | 1,002 global draws |
| `tiered.json` | 1,000 tiered plus 1,000 randomized-matrix draws |
| `oat_full.json` | 944 perturbation points |
| `morris.json` | 2,380 points, 20 trajectories |
| `sobol.json` | 11,264 points, 1,024-row base |
| `decay_ordering.json` | 4,800 |
| `decay_reversal.json` | 3,600 |

Every applicable cache must say `complete` and match both the model hash and its generating
script hash. Parameter screens with three or five common seeds are screens, not confirmatory
replications.

### 4. Recompute the principal release values

The independent recomputation should recover the following 400-seed values.

| Condition | Mean final N | Exists | Endpoint viable | Closed |
|---|---:|---:|---:|---:|
| baseline | 17.8000 | 1.0000 | 0.9850 | 0.0000 |
| T3 friction loss | 14.8375 | 0.9925 | 0.9400 | 0.0075 |
| T3 governance loss | 11.7725 | 0.9800 | 0.9125 | 0.0200 |
| T3 combined loss | 6.7550 | 0.7500 | 0.5475 | 0.2500 |
| T11 pure attraction loss | 12.3800 | 1.0000 | 0.9850 | 0.0000 |
| T11 governance loss | 15.5150 | 1.0000 | 0.9800 | 0.0000 |
| T11 combined loss | 11.9200 | 1.0000 | 0.9850 | 0.0000 |
| recipient capacity forced to one | 18.8275 | 1.0000 | 0.9875 | 0.0000 |

Paired final-membership effects and 95 per cent intervals:

| Contrast | Effect [95% interval] |
|---|---:|
| baseline minus T3 friction loss | 2.962 [1.848, 4.077] |
| baseline minus T3 governance loss | 6.027 [5.043, 7.012] |
| baseline minus T3 combined loss | 11.045 [10.030, 12.060] |
| baseline minus T11 pure attraction loss | 5.420 [4.515, 6.325] |
| baseline minus T11 governance loss | 2.285 [1.214, 3.356] |
| baseline minus T11 combined loss | 5.880 [4.972, 6.788] |
| forced recipient capacity minus baseline | 1.028 [-0.259, 2.314] |

The recipient interval crosses zero and must be called unresolved. The T3 interaction is
-2.055 [-3.414, -0.696]; the T11 interaction is 1.825 [0.755, 2.895]. Do not add single-path
effects as though interactions were zero.

Additional expected corrections:

- original calibration targets 45 members and 9 experienced members fail; observed values are
  17.80 and 1.25, with no post-hoc retuning;
- disabling Step 12 costs 5.325 members [4.437, 6.213] and lowers maintenance capacity by
  0.01351 [0.00788, 0.01915]; the isolated Step 9 change is unresolved;
- high/low capability-one starts separate in only 7 of 400 corrected Chapter 14 endpoint
  environments;
- founder-composition membership contrasts are 0.2925 [-0.898, 1.483] and
  -0.3475 [-1.472, 0.777], with no equivalence margin; both are unresolved;
- the Tradition degradation reference is 13.0975 members with cross-seed SD 5.6664; seven of
  twelve contrasts resolve; Tradition 3 and Tradition 11 are mixed rows.

### 5. Verify the expanded robustness classifications

For `sens3.json`, strict/tied/reversed counts for pure-attraction-loss minus referral-loss must
be:

| Amplitude | Final N | Endpoint viability | Existence | Full viable in all 3 seeds |
|---|---:|---:|---:|---:|
| 12.5% | 301/0/33 | 323/10/1 | 318/16/0 | 302/334 |
| 25% | 251/1/82 | 269/64/1 | 262/72/0 | 291/334 |
| 50% | 213/17/104 | 201/117/16 | 215/117/2 | 256/334 |

Do not compress these into one percentage or call all three outcomes robust.

The 1,000-draw joint screens must report:

| Design | Final N | Endpoint viability | Existence | Full viable in all 3 seeds |
|---|---:|---:|---:|---:|
| tiered | 783/10/207 | 818/165/17 | 821/177/2 | 833/1,000 |
| randomized nonzero matrices | 1,000/0/0 | 1,000/0/0 | 999/1/0 | 784/1,000 |

The randomized-matrix result validates the referral-versus-pure-attraction comparison over
nonzero magnitudes with the authored zero pattern held fixed. It does not validate sparsity and
does not imply that the fully adherent group is viable at every parameter point.

For the structural cache, referral loss must have lower mean final N, existence, and endpoint
viability than pure attraction loss in the base model and all four variants. The old claim that
size reverses under three variants is retired and must appear only as correction history.

All three remaining screens are now complete and their expectations are fixed. Verify that public
prose copies these results rather than the retired 30-draw, 236-point, 10-trajectory, or 128-row
analyses.

**Multi-level OAT**, `oat_full.json`: 118 parameter jobs, 944 perturbation points, three common
seeds per endpoint. Pure-attraction-loss minus referral-loss counts must be 931/2/11 on final
membership, 934/10/0 on endpoint viability, and 933/11/0 on existence. Full adherence is
endpoint-viable in all three seeds at 893 of 944 points and exists in all three at 936. All 35
`GOV` cells must return zero change in every outcome, to a maximum absolute deviation of order
1e-17, because the sweep runs at full adherence. That is a property of the reference point. A
verifier must not record it as evidence that governance is inert.

**Morris**, `morris.json`: 20 trajectories, 118 factors, 2,380 points, reference adherence 0.85.
Membership `mu_star` leaders in order must be `p_gate` 52.44, `delta0` 51.21, `churn` 33.48,
`drop_k` 24.30, `lam_exog` 23.46, `het_sd` 18.90, `a:5` 18.54, `a:11` 15.87, with `lam0` ninth at
14.34 so the cut is untied. Confirm that the eight Sobol factors exactly match these leaders after
normalizing `scalar:` prefixes. The retired leaders `a:8`, `a:4`, and `omega` must appear at ranks
15, 27, and 37 and nowhere as current Sobol factors.

**Sobol**, `sobol.json`: 1,024-row base, 11,264 evaluations, eight factors, reference adherence
0.85. Membership total-order indices must be `p_gate` 0.576 [0.510, 0.643], `delta0` 0.373
[0.320, 0.428], `drop_k` 0.171, `churn` 0.132, `het_sd` 0.079, `lam_exog` 0.058, `a:11` 0.038, and
`a:5` 0.029. Report the noise diagnostic: the total-order floor is 0.0429 for membership and
0.0728 for practice, and `a:5` and `a:11` sit at or below it. Total-order sums are 1.456 and
1.464. The membership first-order column is admissible at this base sample, with no `S1` above its
`ST` and a sum of 0.693; only `p_gate` 0.404 [0.288, 0.525] and `delta0` 0.238 [0.156, 0.327]
resolve, and the other six are unresolved rather than zero. The practice first-order column must
remain withheld: `delta0` returns `S1 = 0.421` against `ST = 0.417` and the practice first-order
sum is 1.074. Quoting any practice first-order index in public prose is a release failure.

**Generating platform.** Caches are hash-linked to the model and generating script, not to a
platform. The three screens above were executed on Linux x86-64 under NumPy 2.2.6; the eight
`oat_full.json` jobs completed before the pause and the 400-seed confirmatory caches were
generated on macOS. Cross-platform re-execution reproduces discrete outcomes exactly and
continuous outcomes to within about 1e-16, which changed no classification. Expect agreement to
reported precision, not bit-identical reproduction. A last-digit difference is not a release
defect; a difference at reported precision is.

### 6. Execute both notebooks

```bash
python3 tools/regenerate_notebooks.py
python3 tools/run_notebook.py
python3 tools/run_notebook.py --paper
```

Both notebooks must execute from a clean process, store output for every code cell, contain no
traceback or failed assertion, check model/cache identities, and finish with:

`CLEAN CACHE-BACKED VERIFICATION NOTEBOOK`

The notebooks verify committed caches; they do not pretend to rerun the entire expensive Monte
Carlo suite interactively.

**The two notebooks are no longer the same artifact, and a verifier should confirm that.** Until
9 August 2026 the paper notebook was byte-identical to the book notebook apart from its title,
which satisfied this section mechanically while verifying nothing specific to the paper. The book
notebook now runs 8 cells and about 78 assertions; the paper notebook runs 10 and about 102. Its
two extra cells:

1. **Paper headline claims.** Re-derives the paper's principal tables from the caches: all eight
   release-gate conditions, the paired T3 and T11 contrasts, the recipient contrast's interval
   crossing zero, the Sobol first-order admissibility split between membership and practice, and
   the structural ordering in all five architectures.
2. **Paper traceability.** Every decimal the paper prints, currently 420 of them after excluding
   DOIs and the five figures quoted from cited literature, must be reachable from the model
   source, a hash-linked cache, or a derivation shown in the notebook. This is the paper's
   equivalent of the figure check `tools/check_book.py` performs for the chapters, which the paper
   previously had no counterpart for. It fails closed and names the offending numbers.

If a verifier finds the two notebooks identical again, that is a regression, not a simplification.

### 7. Audit public prose

Check every file under `manuscript/`, the paper TeX, the primer, the appendix, README, plans,
`research/PARAMETERS.md`, and this brief. At minimum reject any live claim that:

- treats raw semantic overlap as executable coupling;
- calls 118 the number of all model parameters or choices;
- calls 35 the protective index-Step count;
- calls a low-practice member a measured newcomer or a high-practice member a veteran;
- describes endpoint `N <= 5` as death or closure;
- treats the recipient override as changing several mechanisms;
- reports mixed Tradition 11 loss as pure attraction loss;
- calls the proxy-averaging exercise a nonlinear latent-state estimator or a three-proxy rule;
- claims typical-member bistability from the corrected Chapter 14 endpoints;
- treats an unresolved interval as equality or no effect;
- says viable referral-starved rooms do not shrink;
- claims the final-size ordering reverses in three structural variants;
- quotes 41.7 baseline members, 7.7 experienced members, a 23.4 Tradition reference, 236 OAT
  points, 10 Morris trajectories, or a 128-row Sobol base as current results;
- says a finite-horizon result proves steady state or indefinite persistence;
- uses the staged corpus as current evidence.

Run the text and source checkers:

```bash
python3 tools/check_book.py
python3 tools/check_chapter.py reference/PRIMER-steps-and-traditions.md
```

### 8. Build and visually inspect the deliverables

Required PDFs:

- `build/nobody-in-charge.pdf`
- `paper/anonymity-as-an-aggregation-condition.pdf`
- `reference/PRIMER-steps-and-traditions.pdf`

Build each only after all prose and notebooks are final. Render every PDF to page images and
inspect for clipped tables, margin overflow, broken equations, unresolved references, blank or
duplicated pages, malformed headings, stale generated dates, and unreadable type. Machine
success is not visual verification.

### 9. Verify repository identity and portability

Run from the repository root:

```bash
git status --short --branch
git rev-parse --show-toplevel
git rev-parse HEAD
git rev-parse origin/main
python3 tools/check_portability.py
```

The working tree must be clean, `HEAD` must equal `origin/main`, and the portability check must
find no tracked machine-specific absolute paths. The checkout may live anywhere. Separate
non-Git copies are reference copies, not release authorities, and are not part of the release
gate.

## Required verifier report

Return one of `PASS`, `PASS WITH UNRESOLVED SCIENTIFIC LIMITATIONS`, or `FAIL`.

The report must include:

1. model hash and cache-identity result;
2. notebook execution result;
3. release-check totals;
4. confirmatory-value comparison;
5. expanded-screen classification comparison;
6. prose/source-boundary findings with exact file and line references;
7. PDF page counts and visual-QA result;
8. repository-identity and portability result;
9. unresolved scientific limitations, kept separate from release defects.

Expected unresolved limitations are not failures: no fitted group data, failed calibration,
unverified matrix elicitation, unverified mapping from Traditions to theorem assumptions,
unresolved recipient and composition contrasts, rare rather than typical Chapter 14 separation,
finite horizons, and the intentionally deferred staged corpus. Any contradictory number,
stale cache, failed assertion, source-status upgrade, or uninspected PDF is a release failure.
