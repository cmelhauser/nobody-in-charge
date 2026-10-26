# Function reference for the frozen analysis scripts

The Python files in this directory are hash-frozen. Each analysis script records its SHA-256 in
the cache it produced, and `aa_group_model.py` is the release identity, so adding a docstring or
a comment to any of them would invalidate results that took hours to compute (see `ERRATA.md` and
the hash rules in `CLAUDE.md`). Their functions therefore cannot carry the docstrings they lack.

This file describes every function, nested function and class in `model/*.py` that has no
docstring of its own. Definitions that already have a docstring are not repeated here. It is
documentation only: no script, test, cache or checker reads it, nothing depends on its bytes, and
it can be edited freely. Descriptions were written from the code as it stands; the line number
after each name is the line of the `def` statement in the current file, and will drift only if a
frozen script is ever rerun and edited, in which case this file should be regenerated.

Conventions used below. Time is in weeks: `dt` is 0.5 weeks and a horizon of 1560 is thirty years
at 52 weeks a year. A practice vector `X` has one row per room slot (capacity 60) and 12 columns,
one per Step; Steps 10 to 12 are the maintenance steps (columns 9 to 11). "Endpoint viable" means
`N > 5` at the end of the run, "exists" means `N > 0`, and "closed" means `N == 0`. Several
helpers recur in nearly every cache script and are described once here, then referred to by name:

- `_load`: the loader. It executes a fresh copy of `aa_group_model.py` (path built from
  `__file__`) as a module registered in `sys.modules` under the name `m` and returns it. A fresh
  copy per call means that in-place edits to `S` or `GOV` made while running one job do not leak
  into the next.
- `_save`: the atomic cache writer. It dumps the dictionary as JSON to the script's output path
  plus `.tmp` and renames it over the output path with `os.replace`, so an interrupted run leaves
  either the old file or the new one, never a half-written one.
- `_rederive`: rebuilds `GOVW`, `BETA` and `Snorm` in place (with `[:]`, so every reference to the
  arrays sees the change) from the current `S` and `GOV`. It is needed because the model reads
  those derived arrays, not `S` and `GOV`, so a perturbed matrix cell has no effect until they are
  rebuilt.

## aa_group_model.py

| Definition | What it does |
|---|---|
| `step_growth (164)` | Returns the per-week rate of change of practice, `dX/dt`, as an array shaped like `X` (room slots by 12 Steps); the caller multiplies by `dt`. Growth is `a * gate * peer * Cm` (times each member's capability `het` if given) applied to `(1 - X)`, minus decay applied to `X`. `gate` is the previous Step's practice raised to `p_gate` (Step 1 is ungated); `peer` blends the Step's resource bundle `Snorm @ R` with an own-effort share set by `BETA`; `Cm` is the capacity gate, built from a Hill function of the member's mean Step 10 to 12 practice and the group's mean of it, phased in by Step index from 0.05 to 1.0. Decay is `delta0`, raised for Steps 1 to 11 when the next Step is weak (factor `1 + psi * (1 - X_next)`). The argument `T` is accepted but not used here. |
| `snapshot (215)` | Nested in `simulate`. Reads the current `X` and `alive` through the enclosing scope and returns a dictionary for one time point: `time_weeks`, `N`, `all_member_practice` (mean of members' mean practice), `established_count` and `established_practice` (members with mean practice above `act_thr`, and their mean), `experienced_count` (above `exp_thr`) and `low_practice_fraction` (members at or below `act_thr`). With no living member every field is zero. It is called only when `record` is true, once at week 0 and once per step. |

## ch13_reps.py

| Definition | What it does |
|---|---|
| `ces (14)` | Constant-elasticity aggregator of the four regressors `x` with weights `g` and exponent `rho`: `(sum g_i x_i^rho)^(1/rho)`. For `abs(rho) < 1e-8` it returns the Cobb-Douglas limit `prod x_i^g_i`, and for `rho < -60` it returns `min(x)`. Returns a float. |
| `panel (19)` | Simulates one synthetic panel of `n` observations at true exponent `rt`. Draws four regressors uniformly on 0.1 to 0.95 (in order `xo`, `xp`, `G`, `M`), computes the true output `y` with `ces` and the weights `GAM`, then builds `npx` noisy log-output proxies `lam * log(y) + noise * N(0,1)` with loadings `lam` spaced from 0.8 to 1.2. Returns `((xo, xp, G, M), Z, lam)`, where `Z` has shape (`npx`, `n`). The regressors are noise-free; only the output proxies carry noise. |
| `est (24)` | Estimates `rho` from a panel. Divides each proxy by its (known) loading, averages across proxies, then evaluates the model's predicted log output on a 300-point grid of `rho` from -8 to 0.95 and returns the grid value whose centred least-squares fit to the averaged proxy has the smallest residual sum of squares (slope is fitted freely, so only shape matters). Returns a float. |
| `_one (39)` | Worker for one job `(rt, rep, npx)`. Seeds a generator with `abs(1000*rep + int(10*rt) + npx) + 7`, draws a panel, estimates `rho`, and returns `{rt, rep, npx, est}`. |
| `_save (42)` | The atomic cache writer, to `research/ch13_reps.json`. |

## ch14_individual.py

| Definition | What it does |
|---|---|
| `_load (26)` | The loader. |
| `_environment (34)` | Worker for one seed. Runs a full-adherence group to week 1560 (`dt` 0.5), then computes the endpoint's resource vector with `resources(..., return_components=True)`, using solvency from the count of established members. Returns `seed`, `N`, `endpoint_viable` (0 or 1), the 8-element `resources` list, `group_capacity` (mean over living members of the Hill function of their Step 10 to 12 practice, 0.0 if none) and `experienced` (count above `exp_thr`). If the endpoint group is empty, `resources` returns an empty component dictionary and the lookup of `high_practice` would raise a `KeyError`. |
| `_settle (59)` | Integrates `n` independent test members forward by explicit Euler, with no births, deaths or noise, inside a frozen environment. `initial` is a (12,) or (n, 12) starting practice; `resources` is the frozen (8,) or (n, 8) resource vector and `group_capacity` the frozen group term; `capability` (default 1) and `decay` (default `delta0`) may vary by member. Each step applies the same gate, capacity and decay terms as `step_growth` and clips to [0, 1]. Runs `horizon` weeks (default 800) at `dt` (default 0.5) and returns the final (n, 12) practice array. |
| `_save (91)` | The atomic cache writer, to `research/ch14_individual.json`. |

## ch14_sweep.py

| Definition | What it does |
|---|---|
| `_load (8)` | The loader. |
| `_one (11)` | Worker for one job `(pc, seed)`. Runs full adherence to week 1560 with `delta0` scaled by `1 + pc/100` and returns `pc`, `seed`, `N`, `alive` (the same as `viable`), `exists`, `viable`, `closed` and `maint` (mean practice over living members and Steps 10 to 12, 0.0 if the group is empty). |
| `_save (18)` | The atomic cache writer, to `research/ch14_sweep.json`. |

## ch15_service.py

| Definition | What it does |
|---|---|
| `_load (18)` | The loader. |
| `_one (21)` | Worker for one job `(cfg, seed)`, full adherence, 1560 weeks. Configuration `no12` sets the Step 12 growth speed `a[11]` to zero on a copy of the default speeds; `recipient_unconstrained` passes `recipient_override=1.0`; `base` changes nothing. Returns `N`, `exists`, `viable`, `practice` (mean of members' mean practice), `est` (established count), `s12`, `s9` and `s1` (mean practice at Steps 12, 9 and 1 among living members), `maint` (Steps 10 to 12), `low_practice_fraction`, `first_nonviable_week`, `recovered` and `closed`; the per-step and maintenance means are 0.0 for an empty group. |
| `_save (38)` | The atomic cache writer, to `research/ch15_service.json`. |

## core_thresholds.py

| Definition | What it does |
|---|---|
| `_load (37)` | The loader. |
| `_one (45)` | Worker for one seed, full adherence, 1560 weeks. Returns `N`, `alive` (the same as `viable`), `exists`, `viable`, `established` (members whose mean practice exceeds `act_thr`) and `experienced` (exceeds `exp_thr`). An empty group returns zeros for all of them. |
| `_save (57)` | The atomic cache writer, to `research/core_thresholds.json`. |

## decay_ordering.py

| Definition | What it does |
|---|---|
| `_load (34)` | The loader. |
| `_save (64)` | The atomic cache writer, to `research/decay_ordering.json`. |

## decay_reversal.py

| Definition | What it does |
|---|---|
| `_load (37)` | The loader. |
| `_save (67)` | The atomic cache writer, to `research/decay_reversal.json`. |

## elicitation_compare.py

| Definition | What it does |
|---|---|
| `_load (47)` | The loader. |
| `consequences (97)` | Recomputes the Part Four claims on a Step matrix `S` and a governance matrix `G`. Forms `B = S @ G.T` (Steps by Traditions) and its column sums `load`. Returns `all12` (no Step's largest entry is in its own index column), `t1_top` (Tradition 1 has the largest column sum), `s5_to_t12` and `s12_to_t5` (Step 5's largest entry is Tradition 12, Step 12's is Tradition 5), `empty_rows` (zero-indexed Traditions whose row of `G` sums to zero), `load_top` (the largest column sum) and `leader` (that Tradition, one-indexed). Ties go to the first index because `argmax` is used. |
| `report (117)` | Compares one respondent's 12 by 8 matrix `Gr` with the model's `GOV`. Prints and returns the count of cells agreeing on zero versus non-zero out of 96, Cohen's kappa, the four cell categories (both filled, respondent only, book only, both empty), whether the respondent's empty rows equal the five protective Traditions, and the `consequences` on the matrix after `hydrate`. Returns a dictionary of `name`, `agree`, `kappa`, `empty_same` and the `consequences` fields. The printed "T1 at 6.52" is a fixed string, not computed. |
| `main (213)` | Entry point. With `--self-test` runs `self_test`, with `--sparsity` runs `sparsity_sweep`; otherwise reads every `research/governance-elicitation-*.md`, runs `parse` and `report` on each, and prints the across-respondent counts. With no forms present it runs the self-test instead. Returns a process exit code (0, or the self-test's result). |

## mc_error.py

| Definition | What it does |
|---|---|
| `_load (28)` | The loader. |
| `_save (56)` | The atomic cache writer, to `research/mc_error.json`. |

## morris_screen.py

| Definition | What it does |
|---|---|
| `_load (54)` | The loader. |
| `param_ids (62)` | Returns the ordered list of the 118 registered sensitivity ids for a loaded model: `scalar:<name>` for each scalar entry of `DEFAULTS` (22, including `cap`), `a:<i>` for the 12 step speeds, `S:<i>,<j>` for each non-zero cell of `S` in row-major order (49) and `GOV:<i>,<j>` likewise (35). The order fixes the column meaning of every point in the unit hypercube. |
| `_rederive (70)` | Rebuilds `GOVW`, `BETA` and `Snorm` in place from the current `S` and `GOV`. |
| `_save (127)` | The atomic cache writer, to `research/morris.json`. |

## part2_influence.py

| Definition | What it does |
|---|---|
| `flat (60)` | Returns the n by n matrix with every entry `1/n`: equal attention from every member to every member, including self. |
| `main (173)` | Runs the whole Part Two study and writes `research/part2_influence.json` (indent 1), then prints the row count of each list block. The blocks are `dominance`, `clique`, `imbalance`, `speakers`, `scaling`, `rotation`, `elders`, `elders_vs_prescription`, `random_control` and `identity`, each over the group sizes in `NS` (10 to 1000). Each cell stores the largest influence and the expected absolute consensus error `err(s)`, plus a block-specific extra. Everything is deterministic except the random-matrix control, which uses a generator seeded 20260802 with 200 draws per cell. It is not resumable; it recomputes and overwrites. |

## part5_runs.py

| Definition | What it does |
|---|---|
| `_load (53)` | The loader. |
| `_scen_T_P_KW (61)` | Maps a trajectory scenario name to `(T, P, kw)`: adherence vector, parameter overrides and `simulate` keyword arguments. `full` changes nothing, `t11_attraction_loss` sets `attraction_T11=0`, `referral_loss` sets `lam_exog=0`, and `t3_combined_loss` sets `T[2]=0` (both Tradition 3 paths). Any other name raises `ValueError`. |
| `_one (74)` | Worker for one job `(kind, arg, seed)`, 1560 weeks. Kind `t3` sets Tradition 3 adherence to `arg` (both paths together) and returns endpoint outcomes. Kind `traj` runs a scenario with `record=True` and returns yearly samples (every `YEAR` = 104 steps, which is 52 weeks, plus the last recorded step) of membership, mean practice of all living members, mean practice of established members, established count and low-practice fraction, with the first-passage, recovery and closure outcomes; a run that closes early has a shorter history. Kind `comp` starts 25 founders with mean practice 0.55 distributed as `even`, `concentrated` (five at 1.0) or `split` (twelve at 0.9), asserts the mean, and returns endpoint outcomes with the founders' mean, SD and counts above `act_thr` and `exp_thr`; any `arg` other than `even` or `concentrated` is treated as `split`. An unknown kind raises `ValueError`. |
| `_save (135)` | The atomic cache writer, to `research/part5.json`. |

## release_gate_analysis.py

| Definition | What it does |
|---|---|
| `sha256 (49)` | Returns the hexadecimal SHA-256 of the file at `path`, read in 1 MiB blocks. |
| `load_model (57)` | The loader, but registering the module as `release_model` rather than `m`. |
| `settings (65)` | Maps a condition name to `(T, kw)`: full adherence plus the `simulate` keywords for that condition. Friction loss sets `dropout_T3=0`; governance loss passes a `resource_T` with the Tradition's adherence zeroed (index 2 for Tradition 3, index 10 for Tradition 11); combined loss does both; `t11_attraction_loss` sets `attraction_T11=0`; `recipient_unconstrained` sets `recipient_override=1.0`; `base` changes nothing. An unknown name raises `ValueError`. |
| `one (95)` | Worker for one job `(condition, seed)`: runs 1560 weeks at `dt` 0.5 and returns the per-seed record (`N`, endpoint existence and viability, mean and established practice, low-practice fraction, first non-viable week, recovery flag and week, closed flag and closure week). |
| `normal_summary (117)` | Returns `n`, `mean`, `se` (sample SD over root n, 0.0 when n is 1) and a normal-approximation 95 per cent interval `lo`, `hi` = mean plus or minus 1.96 se. |
| `wilson (125)` | Wilson score interval, z = 1.96, for a list of 0/1 outcomes. Returns `n`, `count`, `proportion`, `lo`, `hi` and a `method` label. |
| `paired_continuous (138)` | `normal_summary` of the elementwise difference `a - b` (first minus second), with an `estimand` label. |
| `exact_binomial_two_sided (144)` | Exact two-sided binomial p-value at probability one half: twice the lower tail up to `min(k, n - k)`, capped at 1. Used with `k` the smaller discordant count and `n` the number of discordant pairs; returns 1.0 when `n` is 0. |
| `paired_binary (151)` | Paired risk difference for two lists of 0/1 outcomes: the `normal_summary` of `a - b` plus `first_only` (a is 1, b is 0), `second_only`, `discordant`, and the exact McNemar p-value from `exact_binomial_two_sided`. |
| `rows_by_condition (168)` | Returns, for each condition in `CONDITIONS`, the list of its 400 per-seed records in seed order, read from the cache under the key built as condition, a vertical bar, then seed. A missing key raises `KeyError`. |
| `summarize (175)` | Builds the `summary` block from a complete cache. `conditions`: per condition, normal summaries of `N`, mean practice, established practice and low-practice fraction; Wilson intervals for endpoint existence, endpoint viability, recovery and closure; the count and mean week of first non-viable crossings and the closure week among closed runs (null if none). `paired_contrasts`: six base-minus-loss contrasts and recipient-unconstrained minus base, with `paired_continuous` for the four continuous outcomes and `paired_binary` for existence, viability and closure. `factorials`: for Traditions 3 and 11 and each of those outcomes, the path-loss effect with governance intact, the governance-loss effect with the other path intact, and the interaction `base - path - gov + both`, each as a normal summary of the paired per-seed values. All intervals are normal approximations. |
| `save (235)` | Atomic cache writer for `research/release_gate_results.json`: writes pretty-printed JSON (indent 2, sorted keys, trailing newline) to a `.json.tmp` file and renames it into place. |
| `main (241)` | Entry point. Reads optional worker and batch counts from the command line, discards the cache if its model hash, condition list, horizon or `dt` differ (a changed script hash alone keeps completed seeds), writes the `meta` block, runs the missing (condition, seed) jobs in a process pool, checkpoints every 40 results, and when all 3,200 jobs are present adds `summary`. Returns 0 if complete and 2 if not; the module passes this to `SystemExit`. |

## resource_list_test.py

| Definition | What it does |
|---|---|
| `_load (46)` | The loader. |
| `drop (73)` | Deletes the resource columns whose indices are in the set `cols` from both `S` and `G`; returns the pair `(S, G)` with the remaining columns in their original order. |
| `merge (78)` | Replaces resource columns `r` and `s` by their sum in both matrices: removes both, then appends the sum as the last column of each. Returns `(S, G)`. |
| `main (85)` | Runs the three deterministic designs against the model's matrices: leave-one-out (8 variants), pairwise merge (28) and drop-two (28), evaluates `claims` on each, adds per-design summary counts and the Steps that regain their index-mate, writes `research/resource_list.json` (indent 1) and prints the base result, summary lines and any variant that fails claim A or B. Not resumable. |

## scenarios_hiseed.py

| Definition | What it does |
|---|---|
| `_load (36)` | The loader. |
| `_one (44)` | Worker for one job `(scen, seed)`, 1560 weeks. Scenario `t11_attraction` sets `attraction_T11=0`; `t11_mixed` sets `T[10]=0` (governance and attraction together); `referral` sets `lam_exog=0`; `referral_and_t11_attraction` does both of those two path removals; `t3_combined` sets `T[2]=0`; `full` changes nothing. Returns the endpoint record (`N`, `exists`, `viable`, `alive`, established-member practice, mean practice, established count, low-practice fraction, first non-viable week, recovery and closure flags). |
| `_save (67)` | The atomic cache writer, to `research/scenarios_hiseed.json`. |
| `jobs (73)` | Returns the job list as `(scenario, seed)` pairs, scenario-major in `SCEN` order with seeds 0 to 399, so a job's index is `SCEN.index(scenario) * 400 + seed`. The cache is keyed by that index. |

## sensitivity_oat_full.py

| Definition | What it does |
|---|---|
| `_load (41)` | The loader. |
| `param_ids (49)` | Returns the ordered list of 118 registered ids for the model passed in (the same construction as `morris_screen.param_ids`). |
| `_rederive (57)` | Rebuilds `GOVW`, `BETA` and `Snorm` in place from the model's current `S` and `GOV`. |
| `_scenarios (84)` | Runs three scenarios with seeds 0 to 2 (`SEEDS` = 3) at 1560 weeks, with `P` as parameter overrides: `full`, `attraction` (`attraction_T11=0`) and `referral` (`lam_exog` set to 0 on top of `P`). For each, returns `surv` (fraction of runs with endpoint viability; a legacy key name), `exists`, `N` (mean over all runs), `N_viable` and `practice_viable` (means over viable runs, 0.0 if none), `practice` (mean over all runs) and `maint` (mean Step 10 to 12 practice over living members, 0.0 for an empty group, averaged over runs). |
| `baseline (117)` | Returns `_scenarios` for the unperturbed model. |
| `_save (122)` | The atomic cache writer, to `research/oat_full.json`. |

## sensitivity_tiered.py

This script loads the model once at import time into the module-level name `m` rather than through
a `_load` function, and its helpers edit that shared module in place.

| Definition | What it does |
|---|---|
| `_rederive (35)` | Rebuilds `GOVW`, `BETA` and `Snorm` in place on the module-level model `m`. |
| `_run (41)` | Runs full adherence for 3 seeds (0 to 2), 1560 weeks, with parameter overrides `P` and an optional `attraction_T11`. Returns a tuple: fraction of runs endpoint viable, mean established-member practice over the viable runs (0.0 if none), mean final `N` over all runs, and fraction of runs where the group still exists. |
| `_jitter (55)` | Returns `value` multiplied by a uniform draw on `1 - level` to `1 + level`, where `level` is 0.25 for the Tier 1 and Tier 2 names, 0.50 for Tier 3 and for any name not listed (such as `cap`), then clamped to the limits in `BOUNDS` where one exists. |
| `_tiered_one (71)` | Worker for one draw index. Seeds a generator from `SeedSequence([11, 1, draw])`, jitters every scalar default (`cap` is rounded and floored at 5), scales the 12 step speeds by uniform 0.5 to 1.5, overwrites `S` and `GOV` as their base values times uniform 0.5 to 1.5 per cell (zeros stay zero; assigning from the base copies prevents draws accumulating), rederives, and returns `_row(P)`. |
| `_randmat_one (90)` | Worker for one draw index. Seeds from `SeedSequence([7, 2, draw])`, replaces every non-zero cell of `S` and `GOV` by a uniform draw on 0.05 to 1.0 (zero cells stay zero), rederives, and returns `_row(None)` with default parameters. |
| `_row (98)` | Runs the three conditions for the current model state and returns one record: `full_*` from the full run, `att_*` with `attraction_T11=0`, `ref_*` with `lam_exog=0`. Fields are `*_s` (fraction viable), `*_N`, `*_exists`, and for full and referral also `*_q` (mean established-member practice over viable runs); `att_q` is not recorded. |
| `_save (112)` | The atomic cache writer, to `research/tiered.json`. |

## sensitivity_uniform.py

This script also loads the model once at import time into the module-level name `m`.

| Definition | What it does |
|---|---|
| `_rederive (30)` | Rebuilds `GOVW`, `BETA` and `Snorm` in place on the module-level model `m`. |
| `_run (36)` | Same as `sensitivity_tiered._run`: 3 seeds (0 to 2) of full adherence for 1560 weeks, returning the tuple (fraction viable, mean established-member practice over viable runs, mean `N`, fraction existing). |
| `_one (50)` | Worker for one job `(level_code, draw)`. The amplitude is `level_code / 1000` (125, 250 and 500 mean 12.5, 25 and 50 per cent). Seeds from `SeedSequence([11, level_code, draw])`, multiplies each scalar default (`cap` rounded, floor 5), each step speed and each cell of `S` and `GOV` by an independent uniform draw on `1 - level` to `1 + level`, rederives, then runs full, attraction-removed and referral-removed conditions. Returns the same 11-field record as `sensitivity_tiered._row`. |
| `_save (82)` | The atomic cache writer, to `research/sens3.json`. |

## sobol_indices.py

| Definition | What it does |
|---|---|
| `_load (79)` | The loader. |
| `_save (146)` | The atomic cache writer, to `research/sobol.json`. |
| `_one (163)` | Nested in `indices`. Given an array of row indices `idx`, computes the Saltelli (2010) first-order and Jansen total-order estimates for all `k` factors on those rows of `fA`, `fB` and `fAB` (taken from the enclosing scope). The variance is taken over the concatenated `a` and `b` samples with `ddof=1`; if it is not positive, both outputs are arrays of NaN. Returns the pair `(S1, ST)`, each of length `k`. It is called once on all rows and then once per bootstrap resample. |

## structural_variants.py

| Definition | What it does |
|---|---|
| `_load (57)` | The loader. |
| `step_growth (78)` | Nested in `_apply`, defined only for the `gate_flat` variant and then assigned over `mm.step_growth`. It is a copy of the model's `step_growth` in which the per-Step gate weights are held at the mean of the original ramp (the mean of 0.05 to 1.0 spaced over 12 Steps) instead of rising from 0.05 to 1.0, so total gate exposure is unchanged but spread evenly. Same arguments and return shape as the original; `T` is unused. |
| `resources (102)` | Nested in `_apply`, defined for the `capacity_all` and `no_saturation` variants and assigned over `mm.resources`. A copy of the model's `resources` with one change: under `capacity_all` the counts feeding capacity are all living members instead of the established and experienced subsets; under `no_saturation` the saturation curve is `min(c / (2k), 1)` instead of `c / (c + k)`. Differences from the original: with no living member it returns `(zeros, 0.0)` even when `return_components` is requested, and `resource_T` is not converted to a float array. Otherwise it returns `(result, unity)` or, with `return_components`, `(result, unity, components)`. |
| `_one (207)` | Worker for one job `(variant, scen, seed)`. Applies the variant to a fresh model copy, builds the scenario (`attraction` and `both` set `attraction_T11=0`; `referral` and `both` set `lam_exog=0`; `gatekeeping` sets `T[2]=0`; `full` changes nothing), runs the local `_simulate`, and returns `N`, `exists`, `viable` and `alive` (both `N > 5`), `est_mean` and `n_est`. |
| `_save (220)` | The atomic cache writer, to `research/structural.json`. |

## tradition_paired.py

| Definition | What it does |
|---|---|
| `_load (47)` | The loader. |
| `_save (65)` | The atomic cache writer, to `research/tradition_paired.json`. |
