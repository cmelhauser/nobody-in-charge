# Independent Agent Verification Brief

## Purpose

Verify the release of *Nobody in Charge* independently. Do not repair, reinterpret, or retune
the project while verifying it. Report discrepancies with file and line references, preserve
the source boundary below, and distinguish a failed check from an unresolved scientific claim.

Canonical project:

`<repository root>`

Canonical model SHA-256:

`c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`

The modeled room capacity is 60. Confirmatory stochastic comparisons use 400 seeds. Expanded
robustness comes from additional parameter draws, perturbation distances, structural variants,
trajectories, horizons, and integration steps, not from 1,000 modeled members or a blanket
1,000-seed confirmatory rule.

## Source boundary

Three statuses must remain distinct.

1. **Used/current project.** Current claim support and read status are in
   `research/SOURCES.md`.
2. **Incorporated local copies.** Maxwell (1950) and Golub and Jackson (2010) are under
   `research/incorporated/` because both were already used before the acquired corpus arrived.
3. **Staged/not incorporated.** `research/staged/` is the remaining next-round corpus. Its
   presence does not make a source read, cited, or available as current evidence.

Do not use staged material to fix a claim during this verification. If a staged item might
answer a finding, label the finding `deferred corpus may resolve`. Do not recommend the staged
item as an accidentally omitted source. The user has explicitly reserved it for the next
iteration.

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

The final tiered, randomized-matrix, OAT, Morris, and Sobol expectations are printed in
`research/ROBUSTNESS-RESULTS.md` after the caches complete. Verify that public prose copies those
results rather than the retired 30-draw, 236-point, 10-trajectory, or 128-row analyses. Confirm
that the eight Sobol factors exactly match the corrected Morris membership leaders after
normalizing `scalar:` prefixes, and report the Sobol noise diagnostic.

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

### 9. Verify the mirrored review copy

After the canonical release passes, compare it with:

`<review copy>`

The mirror must contain the same current project files and built artifacts. Exclude unrelated
workspace metadata from the comparison. A stale file in the mirror is a failed handoff even if
the canonical project is correct.

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
8. mirror comparison result;
9. unresolved scientific limitations, kept separate from release defects.

Expected unresolved limitations are not failures: no fitted group data, failed calibration,
unverified matrix elicitation, unverified mapping from Traditions to theorem assumptions,
unresolved recipient and composition contrasts, rare rather than typical Chapter 14 separation,
finite horizons, and the intentionally deferred staged corpus. Any contradictory number,
stale cache, failed assertion, source-status upgrade, or uninspected PDF is a release failure.
