# Technical Appendix

*Nobody in Charge.* Released model specification, estimands, numerical checks, sensitivity
designs, source boundaries, and reproduction instructions.

Author: Anonymous. Released to the public domain under The Unlicense. See `../LICENSE`.

This appendix describes the release-gate model identified by SHA-256:

```text
c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952
```

The executable source `model/aa_group_model.py` and hash-linked JSON caches are authoritative.
This document and the PDF are derived artifacts. No simulation parameter is estimated from AA
data.

Part Two uses a published theorem and deterministic arithmetic over authored matrices. The
stochastic group model supports Parts Three and Five and some comparisons in Part Four; it is
not evidence about an individual person's recovery.

---

## A1. Claim classes and scope

The project contains three objects that must not be collapsed.

1. `B = S GOV^T` is raw semantic overlap between two author-coded matrices. It describes which
   Step-resource and Tradition-resource codes overlap.
2. `C = Snorm GOVW^T` is the normalized, no-capacity linear map from effective adherence to Step
   resource bundles.
3. The executable response adds effective-adherence rules, member-side capacity, clipping,
   nonlinear growth gates, stochastic entry and exit, and the current member state.

Neither `B` nor `C` is a transition matrix or a simulated trajectory effect. Part Four's
historical interpretation of the matrices is an authored operationalization, not a theorem and
not something the simulation discovered.

The modeled room has capacity 60. The release did **not** increase membership to 400 or 1,000.
Confirmatory stochastic comparisons use 400 seeds, paired when conditions share a seed.
Robustness was increased by adding parameter points, perturbation distances, structural
variants, horizons, integration steps, and screening trajectories.

---

## A2. Executable model

### A2.1 State and initial condition

At time `t`, `X` is a `cap x 12` matrix with entries in `[0,1]`; row `i` holds one living
member's twelve practice states. `alive` marks occupied rows. Each member has a fixed positive
growth multiplier `h_i`.

The default run begins with 25 founders, all twelve states equal to 0.55. Arrivals enter with
all states equal to 0.02. Time is integrated by explicit Euler in half-week steps. The reported
horizon is 1,560 weeks, or thirty years.

The practice scale is cardinal only inside the model. It has no validated clinical unit and
does not measure sobriety, harm, tenure, sponsorship, or recovery quality.

### A2.2 Step-resource matrix

The eight resources are admission, identification, living proof, confidentiality, counsel,
recipient opportunity, continuity, and gentle pressure. Rows are Steps 1 through 12.

```text
S =
0.8 1.0 0.3 0.0 0.0 0.0 0.2 0.1
0.0 0.4 1.0 0.0 0.1 0.0 0.2 0.0
0.0 0.0 0.2 0.0 0.3 0.0 0.1 0.1
0.0 0.1 0.0 0.0 0.3 0.0 0.0 0.4
0.0 0.1 0.0 1.0 0.3 0.0 0.2 0.1
0.0 0.0 0.1 0.0 0.2 0.0 0.0 0.3
0.0 0.0 0.1 0.0 0.1 0.0 0.0 0.2
0.0 0.0 0.0 0.1 0.4 0.0 0.0 0.3
0.0 0.0 0.0 0.3 0.9 0.0 0.1 0.2
0.0 0.0 0.0 0.1 0.2 0.0 0.5 0.7
0.0 0.0 0.1 0.0 0.1 0.0 0.2 0.4
0.2 0.1 0.1 0.0 0.1 1.0 0.6 0.3
```

For Step `j`, `Snorm[j,:]` divides its row by the row sum. Group dependence is

```text
beta[j] = row_sum(S[j,:]) / max_k row_sum(S[k,:]).
```

Both are re-derived after any perturbation to `S`.

### A2.3 Tradition-governance matrix

Rows are Traditions 1 through 12 and columns are the eight resources in the same order.

```text
GOV =
0.2 0.5 0.3 0.3 0.2 0.1 0.9 0.6
0.0 0.0 0.0 0.1 0.9 0.0 0.2 0.2
1.0 0.4 0.0 0.0 0.0 0.8 0.1 0.0
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
0.1 0.4 0.5 0.0 0.0 0.9 0.3 0.2
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
0.0 0.1 0.1 0.3 0.1 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
0.0 0.2 0.7 0.0 0.0 0.6 0.2 0.0
0.1 0.3 0.0 1.0 0.1 0.0 0.1 0.0
```

`GOVW` divides each column by its positive column sum. Consequently, at full adherence the
governance quality of every resource is exactly one whatever the 35 nonzero magnitudes in
`GOV`. That cancellation is algebra. It does not apply at partial adherence and says nothing
about whether the structural zeros belong where the author placed them.

### A2.4 Effective adherence

Traditions 4, 6, 7, 9, and 10 have zero rows in `GOV` and act only as protective modifiers.
Using one-based Tradition labels:

```text
Te[2] = T[2] * (0.6 + 0.4 * mean(T[9], T[12]))
Te[5] = T[5] * (0.6 + 0.4 * mean(T[6], T[10]))
ext   = 0.7 + 0.3 * mean(T[4], T[7])
Te    = clip(Te * ext, 0, 1)
q     = GOVW^T Te
```

Protective effects are applied once. They are not repeatedly multiplied through the model.

### A2.5 Member-side resource capacity

Let `lv_i` be member `i`'s mean over the twelve states. Established members satisfy
`lv_i > act_thr`; experienced members satisfy `lv_i > exp_thr`. Define

```text
sat(c,k) = c / (c+k)
unity    = clip(1 - 2 * sd(lv among established members), 0, 1)
```

The eight capacity terms are

```text
admission       1
identification  sat(n_established, k_ident) * unity
proof           sat(n_experienced, k_proof)
confidential    sat(n_experienced, k_conf)
counsel         sat(n_experienced, k_couns)
recipient       sat(n_low_practice / max(n_experienced,1), k_recip)
continuity      (0.45 + 0.55 * solvent) * unity
pressure        unity
```

`R = clip(capacity * q, 0, 1)`. Solvency is established-member contributions divided by rent,
clipped at one.

The recipient term is opportunity per high-practice potential helper. Low-practice and
high-practice are state thresholds, not newcomer and veteran cohorts. The model has no tenure
or matching state. The clean recipient experiment replaces only this capacity term.

### A2.6 Step growth and depreciation

For member `i` and Step `j`:

```text
bundle_j = Snorm[j,:] R
order_gate_1 = 1
order_gate_j = X[i,j-1]^p_gate, j > 1
peer_j = (1-beta_j) + beta_j * bundle_j

own_i = M_i^hill_n / (hill_k^hill_n + M_i^hill_n)
M_i   = mean(X[i,9:12])              zero-based slice: Steps 10 through 12
group_capacity = mean(own_i among living members)
capacity_i = own_i + (1-own_i) * omega * group_capacity

w_j = linear sequence from 0.05 at Step 1 to 1 at Step 12
capacity_gate_ij = 1 - w_j * (1-capacity_i)
growth_ij = a_j * order_gate_ij * peer_j * capacity_gate_ij * h_i

decay_ij = delta0 * (1 + psi * (1-X[i,j+1])) for j < 12
decay_i12 = delta0
dX_ij/dt = growth_ij * (1-X_ij) - decay_ij * X_ij
```

Capability uses the mean-one lognormal draw

```text
h_i = exp(N(-het_sd^2/2, het_sd)).
```

Changing `het_sd` therefore changes dispersion without mechanically changing arithmetic mean
capability. The previous uncentred draw did both and all caches from it are retired.

### A2.7 Membership flow and split Tradition paths

Exit hazard is

```text
early_i = mean(X[i,0:3])              zero-based slice: Steps 1 through 3
low_practice_weight_i = exp(-6 * mean(X[i,:]))
t3_friction_i = 1 + (1-dropout_T3) * low_practice_weight_i
hazard_i = drop0 * exp(-drop_k * early_i) * t3_friction_i + churn.
```

Arrivals are Poisson with half-week mean `lambda * dt`, where

```text
lambda = lam_exog + lam0 * sum_i X[i,12] * attraction_T11.
```

Tradition 3 has distinct resource-governance and inverse-practice dropout-friction paths.
Tradition 11 has distinct resource-governance and attraction paths. The main factorials change
each separately and jointly. The headline referral comparison uses pure attraction loss with
Tradition 11 governance held intact.

Exit is evaluated before arrival. Once membership reaches zero, the group closes permanently
and no same-step exogenous arrival can reopen it.

---

## A3. Default values and authored choices

| Quantity | Default |
|---|---:|
| Step speeds `a` | 0.30, 0.25, 0.25, 0.18, 0.22, 0.20, 0.20, 0.18, 0.15, 0.25, 0.20, 0.22 |
| `delta0`, `psi`, `p_gate` | 0.06, 0.20, 1.5 |
| `hill_n`, `hill_k`, `omega` | 3.0, 0.12, 0.75 |
| `k_ident`, `k_proof`, `k_conf`, `k_couns`, `k_recip` | 3, 3, 2, 3, 2 |
| `act_thr`, `exp_thr` | 0.10, 0.50 |
| `lam0`, `lam_exog` | 0.050, 0.12 per week |
| `churn`, `drop0`, `drop_k` | 0.004, 0.035, 4.0 |
| `cap` | 60 |
| `cost`, `contrib` | 50, 2 per week |
| `het_sd` | 0.55 |

The registered sensitivity set contains 22 scalar defaults, 12 step speeds, 49 nonzero `S`
cells, and 35 nonzero `GOV` cells, for 118 values. These are **registered sensitivity values**,
not all parameters or all choices. The separate inventory also records fixed coefficients,
108 structural zeros, equations, thresholds, initial conditions, and experiment-design choices.

The original inflow and exit values were selected to target approximately 45 members and 9
experienced members. That target fails under the corrected capability distribution: mean final
membership is 17.80; among viable endpoints, the mean established count is 14.13 and the mean
experienced count is 1.25. The parameters were not retuned after observing the failure.

---

## A4. Estimands and uncertainty

The release distinguishes:

- endpoint existence: `N > 0`;
- endpoint viability: `N > 5`;
- permanent closure: `N = 0`;
- final membership, with closed runs contributing zero;
- first crossing at or below five members;
- first recovery above five after a crossing;
- all-member practice;
- established-member practice, conditional on the stated population.

A run may cross below viability and recover. Endpoint nonviability is not closure. A statement
about members in viable groups is selected on the group remaining viable and is printed beside
the viable fraction.

Principal stochastic estimates use seeds 0 through 399. Continuous condition means use normal
95 per cent intervals. Paired continuous contrasts retain common random numbers. Binary
condition intervals are Wilson intervals; paired binary contrasts use paired risk differences
and exact McNemar tests in the cache. Three- and five-seed parameter points are screens, not
independent replications and not confirmatory estimates.

---

## A5. Confirmatory results

### A5.1 Conditions and mechanism factorials

| Condition | Final N, mean [95% interval] | Exists | Viable | Closed |
|---|---:|---:|---:|---:|
| Baseline | 17.800 [16.917, 18.683] | 1.000 | 0.985 | 0.000 |
| T3 friction loss only | 14.838 [13.910, 15.765] | 0.9925 | 0.940 | 0.0075 |
| T3 governance loss only | 11.773 [11.149, 12.396] | 0.980 | 0.9125 | 0.020 |
| T3 combined loss | 6.755 [6.170, 7.340] | 0.750 | 0.5475 | 0.250 |
| T11 attraction loss only | 12.380 [12.038, 12.722] | 1.000 | 0.985 | 0.000 |
| T11 governance loss only | 15.515 [14.809, 16.221] | 1.000 | 0.980 | 0.000 |
| T11 combined loss | 11.920 [11.584, 12.256] | 1.000 | 0.985 | 0.000 |
| Recipient capacity forced to one | 18.828 [17.782, 19.873] | 1.000 | 0.9875 | 0.000 |

Paired final-membership losses from baseline are 2.962 [1.848, 4.077] for T3 friction,
6.027 [5.043, 7.012] for T3 governance, and 11.045 [10.030, 12.060] jointly. The T3 factorial
interaction is -2.055 [-3.414, -0.696], so path effects are not additive.

The T11 losses are 5.420 [4.515, 6.325] for pure attraction, 2.285 [1.214, 3.356] for
governance, and 5.880 [4.972, 6.788] jointly. The interaction is 1.825 [0.755, 2.895].

Forcing only recipient capacity to one changes final membership by 1.028 [-0.259, 2.314]. The
interval crosses zero, so the clean recipient ablation is unresolved.

### A5.2 Service, composition, and the Tradition ranking

Disabling Step 12 lowers final membership by 5.325 [4.437, 6.213], established practice by
0.01497 [0.00765, 0.02229], and maintenance capacity by 0.01351 [0.00788, 0.01915]. The isolated
Step 9 change is 0.00550 with an interval from -0.00149 to 0.01249 and is unresolved.

The founder-composition experiment holds total initial practice at 13.75 and compares even,
concentrated, and split allocations. Relative to even founders, paired final-membership
differences are 0.2925 [-0.898, 1.483] and -0.3475 [-1.472, 0.777]. No equivalence margin was
specified, so this is unresolved rather than evidence of equality. The model has no mentoring,
sponsorship, clique, or sorting mechanism.

At twenty years with all Traditions at 0.85 and one lowered to 0.50, reference membership is
13.0975 with cross-seed SD 5.666. Seven of twelve paired contrasts exclude zero. Tradition 3
and Tradition 11 are mixed adherence interventions in this ranking; mechanism-specific results
come from the factorials above.

### A5.3 Chapter 14 correction

The original typical-member bistability result used a frozen environment from the retired
capability-inflated model. Recomputed from 400 corrected full-adherence endpoints, capability-one
high and low starts separate by more than 0.05 in only 7 environments, or 1.75 per cent. In the
mean corrected environment both starts converge to negligible maintenance. The architecture can
generate bistability in some environments; typical-member bistability is not a released baseline
result.

### A5.4 Trajectories and selection

Under referral loss, all-run membership is 21.55 at year 5, 11.68 at year 10, 2.50 at year 20,
and 0.51 at year 30. Endpoint viability falls from 0.970 to 0.660, 0.1725, and 0.0275. Membership
among viable groups also falls, from 22.07 to 16.47, 11.39, and 12.27. The last mean is based on
only eleven viable runs and has half-width 3.81. The corrected model therefore shows visible
room-size decline as well as closures. Established practice among selected viable remnants stays
high; that selected quantity is not evidence that the interior has no warning signal.

---

## A6. Numerical resolution and horizon

At the baseline thirty-year horizon, mean final membership is 17.80 at `dt=0.5`. In 200 paired
seeds, changes relative to that step are 1.535 plus or minus 1.777 at `dt=1`, 0.865 plus or minus
1.836 at `dt=0.25`, and -0.405 plus or minus 1.742 at `dt=0.125`. All intervals cross zero. This
supports the tested half-week resolution for the reported comparisons; it does not prove
convergence at arbitrary resolution.

Mean final membership is 29.34 at 10 years, 21.14 at 20, 17.80 at 30, 16.43 at 50, and 15.64 at
100. The 100-year series includes one closure in 200 runs. Because the horizon series continues
to move, the release makes no steady-state or indefinite-persistence claim.

---

## A7. Expanded sensitivity and structural robustness

### A7.1 Design registry

| Design | Size | Seeds per parameter point | Purpose |
|---|---:|---:|---|
| Global simultaneous perturbation | 1,002 draws, 334 at each amplitude | 3 | broad joint screen at 12.5%, 25%, and 50% |
| Tiered perturbation | 1,000 draws | 3 | ranges tied to evidential status |
| Randomized nonzero matrices | 1,000 draws | 3 | magnitude test with sparsity fixed |
| Multi-level one-at-a-time | 944 points | 3 | 118 values, two directions, four distances |
| Morris | 20 trajectories, 2,380 points | 5 | factor screen; interaction or nonlinearity not separated |
| Sobol | 1,024 base rows, 11,264 points | 5 | conditional decomposition on eight Morris leaders |
| Structural variants | 10,000 simulations | 400 | five architectures by five scenarios |
| Decay-ordering confirmation | 4,800 simulations | 400 | referral against attraction loss at four `delta0` levels |

Multiplicative designs cannot move structural zeros. A full-adherence outcome cannot reveal the
35 `GOV` magnitudes because they cancel. The randomized-matrix design holds sparsity fixed and
therefore tests magnitudes, not where zeros belong.

### A7.2 Global screen

Counts are strict/tied/reversed for pure-attraction-loss minus referral-loss outcomes.

| Amplitude | Final N | Endpoint viability | Existence | Full model viable in all 3 seeds |
|---|---:|---:|---:|---:|
| 12.5% | 301/0/33 | 323/10/1 | 318/16/0 | 302/334 |
| 25% | 251/1/82 | 269/64/1 | 262/72/0 | 291/334 |
| 50% | 213/17/104 | 201/117/16 | 215/117/2 | 256/334 |

The comparison is most stable on existence and least stable on final membership. Even at the
mildest amplitude, no blanket statement that every outcome survives is correct.

### A7.3 Structural variants

Four one-choice variants are compared with the base architecture: a flat rather than
step-phased capacity gate; Tradition 3 moved from retention friction to admission; capacity
supplied by all living members; and a piecewise-linear, clipped capacity response in place of
the hyperbolic response. The last variant still saturates at one despite its historical
`no_saturation` filename.

| Architecture | Attraction loss N / exists / viable | Referral loss N / exists / viable |
|---|---:|---:|
| Base | 12.380 / 1.000 / 0.985 | 0.510 / 0.105 / 0.0275 |
| Flat gate | 6.613 / 0.870 / 0.6575 | 0.745 / 0.120 / 0.0550 |
| T3 on admission | 12.380 / 1.000 / 0.985 | 0.510 / 0.105 / 0.0275 |
| Capacity from all members | 14.730 / 1.000 / 1.000 | 2.003 / 0.2575 / 0.1225 |
| Piecewise-linear capacity | 13.038 / 1.000 / 0.995 | 1.020 / 0.145 / 0.0575 |

Referral loss is worse on final membership, existence, and endpoint viability in all five
tested architectures. The earlier three-variant size reversal came from the retired uncentred
capability model and does not reproduce. Five architectures are not every possible architecture.

### A7.4 Tiered and randomized-matrix screens

| Design | Final N | Endpoint viability | Existence | Full viable in all 3 seeds | Full exists in all 3 seeds |
|---|---:|---:|---:|---:|---:|
| Tiered, 1,000 draws | 783/10/207 | 818/165/17 | 821/177/2 | 833/1,000 | 943/1,000 |
| Random nonzero matrices, 1,000 draws | 1,000/0/0 | 1,000/0/0 | 999/1/0 | 784/1,000 | 1,000/1,000 |

Counts are strict/tied/reversed for pure-attraction-loss minus referral-loss. Randomizing every
nonzero matrix magnitude while preserving the zero pattern leaves the comparison intact on all
three outcomes. The tiered design, which also varies scalar defaults and Step speeds over wider
ranges, produces substantial final-membership reversals and smaller numbers of viability and
existence reversals. These are different robustness questions.

### A7.5 Multi-level OAT, Morris, and Sobol results

All five caches, the three screens' and the two decay runs', are complete and match
both the model hash and their generating-script hashes.
The generated tables live in `research/ROBUSTNESS-RESULTS.md`; this section states what they mean
and what they do not license.

**Multi-level one-at-a-time screen** (`research/oat_full.json`). Each of the 118 registered values
is moved alone by 10, 25, 50 and 75 per cent in each direction, giving 944 perturbation points,
with three common seeds per endpoint. This is a screen, not a confirmatory design. Across the 944
points the pure-attraction-loss minus referral-loss ordering is strict in 931, tied in 2 and
reversed in 11 on final membership; 934/10/0 on endpoint viability; and 933/11/0 on existence.
Full adherence is endpoint-viable in all three seeds at 893 of 944 points and exists in all three
at 936. The eleven membership reversals are not scattered: nine are large downward moves of
`p_gate`, `delta0` and `churn` at the 25, 50 and 75 per cent distances, and the remaining two are
the `S:11,5` and `S:11,6` cells. Twenty-six of the 118 values move the referral-starved endpoint
viability on their own, and 32 move the full-adherence endpoint viability.

**Decay-ordering confirmation** (`research/decay_ordering.json`, `model/decay_ordering.py`). The
three `delta0` membership reversals are the ones the reading recorded in A11 item 9 makes most
plausible, so they were re-estimated at 400 seeds. Both channels intact, pure attraction loss with
governance held at one, and referral loss (`lam_exog = 0`) were each run with `delta0` unchanged
and 25, 50 and 75 per cent lower, giving unattended half-lives of 11.6, 15.4, 23.1 and 46.2 weeks,
at full adherence otherwise, over 1,560 weeks at dt 0.5. Seeds 0 to 399 are shared by all twelve
cells, so every contrast is paired by common random numbers. Means carry 95 per cent half-widths,
the referral-loss viability a Wilson interval, and the contrasts paired 95 per cent intervals.

| `delta0` change | Both channels, N | Attraction loss, N | Referral loss, N | Referral loss viable | Referral loss closed |
|----------:|----------------:|----------------:|----------------:|---------------------------:|---------------:|
| 0 | 17.80 ± 0.88 | 12.38 ± 0.34 | 0.51 ± 0.23 | 2.75% [1.54, 4.86] | 358 of 400 |
| -10% | 29.07 ± 1.53 | 13.43 ± 0.36 | 2.50 ± 0.66 | 13.50% [10.50, 17.20] | 291 of 400 |
| -15% | 39.04 ± 1.59 | 13.93 ± 0.36 | 7.58 ± 1.31 | 32.50% [28.10, 37.24] | 225 of 400 |
| -20% | 47.47 ± 1.37 | 14.46 ± 0.37 | 17.25 ± 1.99 | 54.50% [49.60, 59.31] | 123 of 400 |
| -25% | 54.19 ± 0.84 | 15.01 ± 0.37 | 29.98 ± 2.25 | 75.50% [71.06, 79.46] | 64 of 400 |
| -50% | 59.46 ± 0.10 | 18.19 ± 0.40 | 59.21 ± 0.12 | 100% [99.05, 100] | 0 of 400 |
| -75% | 59.81 ± 0.05 | 20.59 ± 0.43 | 59.71 ± 0.07 | 100% [99.05, 100] | 0 of 400 |

| `delta0` change | Final membership | Endpoint viability | Existence |
|---:|---:|---:|---:|
| 0 | 11.87 [11.47, 12.27] | 0.9575 [0.9365, 0.9785] | 0.8950 [0.8649, 0.9251] |
| -10% | 10.92 [10.18, 11.66] | 0.8575 [0.8232, 0.8918] | 0.7275 [0.6838, 0.7712] |
| -15% | 6.35 [5.03, 7.68] | 0.6700 [0.6239, 0.7161] | 0.5625 [0.5138, 0.6112] |
| -20% | -2.79 [-4.77, -0.81] | 0.4550 [0.4061, 0.5039] | 0.3075 [0.2622, 0.3528] |
| -25% | -14.97 [-17.21, -12.73] | 0.2450 [0.2028, 0.2872] | 0.1600 [0.1240, 0.1960] |
| -50% | -41.02 [-41.42, -40.62] | 0 | 0 |
| -75% | -39.12 [-39.55, -38.68] | 0 | 0 |

The second table is pure attraction loss minus referral loss, paired by seed. At the default rate
the cells reproduce the released values. At 25 per cent lower the membership ordering reverses,
with the attraction-loss group smaller in 254 paired runs, tied in 3 and larger in 143, while
referral loss remains worse on endpoint viability and existence. At 50 and 75 per cent lower every
referral-loss run is endpoint-viable, so the two binary contrasts are exactly zero. The run
confirms the screen's direction at all three distances and shows that the reversal is confined to
final membership.

**Locating the membership reversal** (`research/decay_reversal.json`, `model/decay_reversal.py`).
The run above left the rate at which the membership ordering first turns unlocated, somewhere
between the default and 25 per cent lower. A second run fills that interval at 10, 15 and 20 per
cent lower, giving half-lives of 12.8, 13.6 and 14.4 weeks, on the same design with the same seeds
0 to 399; the script differs from `decay_ordering.py` only in its docstring and its level list, and
a test asserts that, so the seven levels read as one series and the rows above are interleaved into
both tables. The membership ordering holds at 10 per cent lower, at 10.92 members [10.18, 11.66],
and at 15 per cent lower, at 6.35 [5.03, 7.68]. At 20 per cent lower it is reversed, at -2.79
[-4.77, -0.81], with the attraction-loss group smaller in 157 paired runs, tied in 10 and larger in
233. The turn is therefore between 15 and 20 per cent lower. Endpoint viability and existence are
not reversed in a single paired run at any of the three, so the reversal remains confined to final
membership throughout.

Against a full-adherence baseline of 18.67 members, 0.2261 practice and 0.0431 maintenance, the
ordering exponent `p_gate` has the largest single influence on all three outcomes. At plus or
minus 25 per cent its maintenance range is 5.45 times baseline, `delta0` 3.27 and the step-10
speed 2.22; over the whole four-distance ladder the figures are 14.64, 12.98 and, for `het_sd`,
4.69.

All 35 governance cells return zero change in every outcome and every scenario, with a maximum
absolute deviation of 5.6e-17. This is a property of the reference point and not evidence of
inertness: the OAT scenarios run at full adherence, where the column-normalised governance quality
is identically 1 regardless of the underlying magnitudes. A multiplicative screen also cannot move
a structural zero. Both facts are why the Morris and Sobol designs are sited at 0.85 adherence.

**Morris screen** (`research/morris.json`). Twenty trajectories over all 118 factors at plus or
minus 25 per cent, four levels, delta 2/3, five common random numbers per point, 2,380 model
evaluations, reference adherence 0.85. Effects are output change per unit proportional change in
the parameter. The membership `mu_star` leaders are `p_gate` 52.44, `delta0` 51.21, `churn` 33.48,
`drop_k` 24.30, `lam_exog` 23.46, `het_sd` 18.90, `a:5` 18.54 and `a:11` 15.87. The ninth factor,
`lam0`, is 14.34, so the eight-factor cut is untied. By share of total membership `mu_star`, the
22 scalars carry 44.9 per cent, the 49 `S` cells 33.7, the 12 step speeds 18.2 and the 35 `GOV`
cells 3.3. Five of the eight leaders have `sigma/mu_star` above one, which indicates interaction
or curvature without separating them; that separation is what the Sobol design is for.

This screen corrects the retired ten-trajectory result. Three of the factors previously carried
into the Sobol design do not survive: `a:8` now ranks fifteenth, `a:4` twenty-seventh and `omega`
thirty-seventh. They are replaced by `lam_exog`, `a:5` and `a:11`.

**Sobol decomposition** (`research/sobol.json`). Saltelli first-order and Jansen total-order
estimators on a 1,024-row base design over the eight Morris membership leaders at plus or minus
25 per cent, reference adherence 0.85, five common random numbers per point. The executed cache is
11,264 evaluations: 1,024 each for A, B and the noise replicate, plus 8,192 cross-matrix rows.
Intervals are 2,000-resample percentile bootstraps over base rows. The noise-replicate total-order
floor is 0.0429 for membership and 0.0728 for practice.

Membership total-order indices are `p_gate` 0.576 [0.510, 0.643], `delta0` 0.373 [0.320, 0.428],
`drop_k` 0.171 [0.145, 0.199], `churn` 0.132 [0.111, 0.155], `het_sd` 0.079 [0.064, 0.095],
`lam_exog` 0.058 [0.049, 0.068], `a:11` 0.038 [0.031, 0.046] and `a:5` 0.029 [0.024, 0.034]. The
last two lie at or below the noise floor and are not separated from Monte Carlo error. The
total-order indices sum to 1.456 for membership and 1.464 for practice; the excess over one is
interaction counted once per participating factor, so interaction is present and is not dominant.

The eight-fold increase in base sample repairs the membership first-order column and not the
practice column. On membership no factor has `S1` above `ST` and the first-order indices sum to
0.693, so the column is admissible: `p_gate` resolves at 0.404 [0.288, 0.525] and `delta0` at
0.238 [0.156, 0.327], and the other six have intervals covering zero and are unresolved rather
than zero. On practice `delta0` returns `S1 = 0.421` against `ST = 0.417`, violating the identity
`ST >= S1`, and the practice first-order indices sum to 1.074, which a first-order sum cannot do.
The practice first-order column is therefore still withheld and no number from it is quoted.

The decomposition is conditional on these eight factors and these ranges. The other 110 registered
values are held at nominal, so this is the variance those eight generate between them and not the
model's total variance. The `mu_star` shares above remain the right place to look for the latter.

### A7.6 Resource-list test

The eight group resources are an author-coded list: admission, identify, proof, confidential,
counsel, recipient, continuity, and pressure. No source proposes them, so the question is whether
Part Four's conclusions depend on that particular eight. `model/resource_list_test.py` rebuilds the
raw semantic overlap `B = S @ GOV.T` under 64 alternative lists and re-runs the index-pairing test
on each, using competition rank and complete maximizing sets. The object is semantic overlap, not
executable coupling, and the test is deterministic, so it carries no interval.

| Variant family | Count | All-twelve rejection holds | Unity leads | Protective set unchanged |
|---|---:|---:|---:|---:|
| Leave one resource out | 8 | 7 | 8 | 8 |
| Merge a pair of resources | 28 | 20 | 28 | 28 |
| Drop two resources | 28 | 21 | 27 | 28 |

Unity leads on 63 of the 64 variants. The single failure is the drop-two variant that removes
continuity and pressure together, which is the same pair the reassignment test in A8 identifies as
the only transfer able to flip the result. Two instruments built for different purposes fail on the
same two columns, which is worth more than either alone because it localizes the point of failure.

The all-twelve rejection of index-pairing survives in 48 of the 64 variants. The five protective
Traditions keep empty governance rows in all 64, which is a structural consequence of the authored
zeros rather than an independent confirmation. Where the all-twelve rejection fails it is almost
always Step 1 regaining its index-mate, in 15 variants across the three families. The finding is
therefore that the pairing verdict is not an artifact of any single resource, and not that the list
is correct.

---

## A8. Part Two and deterministic coupling tests

Golub and Jackson's theorem concerns the maximum stationary influence weight in a sequence of
networks. Under its regularity conditions, naive learning aggregates information if and only if
that maximum influence vanishes as group size grows. The theorem is published mathematics. The
claim that Traditions 2, 9, and 12 operationalize its assumptions is this project's unverified
reading.

The deterministic Part Two notebook checks finite-group influence, scaling of rotation pools,
the three obstruction constructions, and random-network controls. These are not runs of the
stochastic membership model. The matrices in Part Four reject index-pairing on the authored
values, but five of the twelve rejections are forced by structural zeros. Threshold and sparsity
tests are required where multiplicative perturbation is blind. Under wholesale randomization of
nonzero coupling magnitudes, the all-twelve index-pairing rejection holds in 40.6 per cent of
draws. The magnitude claim therefore needs substantive defense and independent elicitation.

---

## A9. Source and corpus boundary

`research/SOURCES.md` is the current evidence ledger. Maxwell (1950) and Golub and Jackson
(2010) were already used by the project and are stored under `research/incorporated/`. The
Maxwell copy remains a retyped reproduction with visible transcription errors, not a journal
scan; moving it did not upgrade its source status.

`research/staged/` is a supplied next-round corpus. Its remaining items have intentionally not
been incorporated into the manuscript or paper. File presence is not evidence that a source was
read or used. A verifier may mark a finding `deferred corpus may resolve`, but must not silently
use staged material to repair this release or recommend it as an accidentally overlooked source.

---

## A10. Reproduction and release gate

Principal files:

```text
model/aa_group_model.py                    canonical model
model/book-calculations.ipynb              book verification notebook
paper/anonymity-as-an-aggregation-condition.ipynb
                                           paper verification notebook
research/RELEASE-GATE-RESULTS.md           generated confirmatory report
research/ROBUSTNESS-RESULTS.md             expanded-sensitivity report
research/model-choice-inventory.json       values, zeros, and constants
tools/check_release.py                     fail-closed release gate
```

From the repository root, after every cache is complete. All three PDFs are built before the
release check, because that check requires each rendered artifact to postdate every source that
feeds it:

```bash
python3 tools/summarize_robustness.py
python3 tools/regenerate_notebooks.py
python3 tools/run_notebook.py
python3 tools/run_notebook.py --paper
python3 tools/check_book.py
python3 tools/check_chapter.py reference/PRIMER-steps-and-traditions.md
python3 tools/check_portability.py
python3 tools/build_book.py
tectonic --outdir paper \
  paper/anonymity-as-an-aggregation-condition.tex
python3 tools/build_primer.py
python3 tools/check_release.py
```

`build_book.py` and `build_primer.py` each report an overfull-box count, and release requires
zero from both. A nonzero count means text is sitting outside the type block. All three PDFs use
one inch margins, the book at 1.05 inches.

Release also requires rendering all three PDFs to page images and inspecting them for overflow,
clipped tables, broken references, duplicated headings, blank pages, and stale text.

### A10.1 Renumbering note

This appendix was consolidated during the release-gate round and several section identifiers used
by earlier drafts no longer exist. Manuscript, paper, and primer references were retargeted. The
docstrings of completed analysis scripts still carry the old identifiers, because those scripts are
hash-linked to caches that would be invalidated by editing them, so the mapping is recorded here
instead.

| Retired identifier | Current location |
|---|---|
| A3.3, A3.3b, A3.4 | A4, estimands, seed counts, and the selection threat |
| A4.6, A5.5 | A7.5, Morris and Sobol |
| A5.4b, A5.4c, A5.4e | A8, threshold, reassignment, and sparsity-pricing tests |
| A5.4d | A5.2, the degradation ranking |
| A5.6 | A7.1, the design registry and what no design covers |
| A9 as structural variants | A7.3 |
| A9.5 | A7.6, the resource-list test |

---

## A11. Threats to validity

1. No simulation parameter is fitted to longitudinal AA group data, and the original calibration
   fails after the mean-one correction.
2. The `S` and `GOV` matrices are author judgments. Their magnitudes and sparsity need independent
   elicitation.
3. The mapping from three Traditions to the Golub-Jackson conditions is an interpretation, not a
   theorem or historical fact.
4. The model has no tenure, sponsorship, pair matching, cliques, attendance networks, relapse
   outcome, harm measure, competing organization, or regional ecology.
5. The practice scale is internal and unvalidated. Threshold names such as established and
   experienced do not create empirical categories.
6. Finite-horizon persistence is not indefinite survival; endpoint viability is not closure;
   selected member quality is not a population outcome.
7. Sensitivity screens cover stated ranges and architectures only. Low-replication parameter
   points rank robustness; they do not estimate real-world probabilities.
8. The staged corpus is deliberately outside this release's evidence record.
9. The decay rate `delta0` is authored and, after the ordering exponent, the most influential
   registered value. Nothing measures the quantity it represents. Four papers read for
   comparable quantities bracket it: two on skill depreciation, read on 13 September 2026,
   are one to two orders of magnitude slower; one on habit decay in daily life, read on 22
   September, is an order of magnitude faster and measures an unwanted habit being
   deliberately weakened; and one on seven-year AA attendance trajectories, read the same day,
   finds participation falling away over years while abstinence does not follow it down. Large
   downward moves of `delta0` are among the few that reverse the pure-attraction-loss minus
   referral-loss ordering in the A7.5 screen, and the 400-seed confirmations there place the
   membership reversal between 15 and 20 per cent lower while the ordering still holds on endpoint
   viability and existence; at 50 per cent lower or more, referral loss leaves every run viable.
   The released value is unchanged, because no source measures how fast a practice lapses.

The model's proper use is to make assumptions and comparisons explicit enough to test against
real group data. It cannot evaluate or advise any individual person's recovery.

---

## A12. A second fellowship: Recovery Dharma read against the model

This section answers a question put to the project from outside it, rather than one the model was
built for. It is deterministic and textual. It adds no cache, no seed, no interval, and no
stochastic claim, and nothing elsewhere in the release depends on it. The source is
`research/incorporated/RecoveryDharma_2023/`, read in full in two passes: Section I, Section II
with its fourteen personal stories, the meeting format, the glossary and the dedication of merit
on 16 August 2026, and the selected meditations and the inquiry questions on 13 September 2026.

### A12.1 The question, and what the model cannot answer

The question was whether the model shows the Twelve Steps simplified into the Dharma. It does not,
and three separate obstacles stand in the way before any evidence is weighed.

The first is chronology. The Eightfold Path predates the Twelve Steps by roughly two and a half
thousand years. The source dates Siddhartha to about 2,500 years ago and the writing down of the
teachings to the centuries after his death in the fifth century BCE, and it presents its program as
an application of early Buddhist teaching rather than as a rewriting of anything. A claim that one
document is a simplification of the other is available in neither direction, and in the direction
asked it is ruled out by dates alone.

The second is that the model has no parameterization for this fellowship. Applying it would require
a step-resource matrix and a governance matrix elicited for Recovery Dharma. Neither exists. A11
item 2 already records that the two matrices the project does have are author judgments in need of
independent elicitation, so authoring two more here, for a fellowship the author does not belong
to, would compound the existing weakness rather than test anything.

The third is that the model contains no object corresponding to a comparison of fellowships. A11
item 4 records the absence of a competing organization, and there is no comparative estimand, no
second room, and no shared population.

What remains available is a structural reading: taking the model's eight resources as a vocabulary
and asking, of each program's own documents, where each resource is carried. That is a coding
exercise on text, and it is registered here as a reading rather than a result.

### A12.2 The count test

The count comparison that makes simplification look true is eight against twelve, and it compares
one Recovery Dharma list against one AA list.

| Program | Enumerated lists | Items |
|---|---:|---:|
| AA as this model codes it: Steps and Traditions | 2 | 24 |
| Recovery Dharma: jewels, Noble Truths, path factors, precepts, heart practices, foundations of mindfulness, commitments of The Practice | 7 | 35 |

The Recovery Dharma items are three jewels, four Noble Truths, eight path factors, five precepts,
four heart practices, four foundations of mindfulness, and seven commitments in the section called
The Practice. On count the program is larger, not smaller, and its commitments are distributed
across seven enumerated lists rather than concentrated in two.

There is a real simplification in the source, and it is of grouping rather than of count. The eight
path factors are gathered under three headings, wisdom, ethics and concentration, and the Path is
not worked in sequence. The Steps are numbered and ordered. That difference is genuine and is not
what the word simplification is usually taken to mean.

### A12.3 Where the eight resources are carried

The model's own structure first, computed from the canonical `S` and `GOV` and carrying no
interval. Group dependence `beta` is maximal and equal at 1.000 for Steps 1 and 12. Step 12 is the
only Step with a nonzero recipient-opportunity entry, so it is the sole carrier of that resource.
Step 1 holds 0.800 of the admission column and 0.588 of the identification column, Step 5 holds
0.667 of the confidentiality column, and the two diffuse resources, counsel and gentle pressure,
are spread across eleven Steps each with top shares of 0.300 and 0.226. In `GOV`, recipient
opportunity carries the largest governance mass of the eight columns at 2.40.

| Resource | AA carrier in `S` | Recovery Dharma carrier, with printed page |
|---|---|---|
| admission | Step 1, 0.800 of column | First Noble Truth, "Addiction **is** suffering" (9); Renunciation in The Practice (xv) |
| identify | Step 1, 0.588 of column | made optional by design: introductions need no identification beyond a name (150); no requirement to identify yourself in any way (43) |
| proof | Step 2, 0.526 of column | the fourteen personal stories (57-121); those who have made it to the other side (2, 48) |
| confidential | Step 5, 0.667 of column | the closing of the meeting script (151) |
| counsel | diffuse, Step 9 top at 0.300 | Wise Friends and Mentors (49-50); Reaching Out (46-48); the inquiry questions, which suggest working through them with a mentor, wise friend or group and ask whether the reader has one to turn to (136, 139, 143) |
| recipient | Step 12, sole carrier | Sangha, Wise Friends, Mentors in The Practice (xvi, 148); Service and Generosity (50-52); the newcomer question in the closing (151) |
| continuity | Step 12 top at 0.286 | Meetings and Growth in The Practice (xv-xvi); the announcements (151) |
| pressure | diffuse, Step 10 top at 0.226 | the Five Precepts (29); cut against by the group-sharing rule that shares carry no advice (151) |

Two things follow. The carriers scatter across four documents rather than one, so the counterpart of
the Twelve Steps is not the Eightfold Path but the union of the Path, The Practice, the Sangha
chapter and the meeting script. And three of the eight resources, confidentiality, recipient
opportunity and gentle pressure, are not carried in the Eightfold Path at all. A reading that sets
the Path beside the Steps and counts eight against twelve is comparing a practice taxonomy with a
document that does a different job.

One entry deserves separate notice because it runs opposite to the model's coding. Identification
is the resource AA loads most heavily onto Step 1, and Recovery Dharma removes the ritual that
carries it, twice and explicitly. The model gives that resource a column mass of 1.70 and a
governance mass of 1.90. It cannot say what removing the ritual would do, because there is no
parameterization, but it locates the question precisely, which is the most this exercise supports.

### A12.4 Governance, the sangha, and a schism

This book's argument is about the Traditions rather than the Steps, so this is the section that
matters most, and it is the one a first pass got wrong. That pass claimed the fellowship had no
Traditions-equivalent object at all. It has one. Correcting the error is what produced the strongest
finding in this section.

**The sangha is the group-conscience analogue, and it is constitutional rather than procedural.**
The meeting script has every member affirm that they "trust in the wisdom of" the Buddha, the
Dharma, and the Sangha, glossed there as the community of wise friends (147). Refuge in the three
jewels is doctrinal, recited at every meeting, and is not among the things the script invites a
meeting to edit. The Sangha chapter states that the fellowship is "decentralized and peer-led" and
that its own advice is offered "in the spirit of friendly guidance rather than direction" (42),
which is close in both content and tone to Tradition 2's account of leaders who do not govern. AA
locates ultimate authority in a group conscience; Recovery Dharma locates trust in a sangha. Those
are the same move.

| Function in AA's Traditions | Recovery Dharma location |
|---|---|
| ultimate authority in the group, Tradition 2 | refuge in the Sangha and trust in its wisdom, recited at every meeting (147); "friendly guidance rather than direction" (42) |
| openness of membership, Tradition 3 | no requirement to believe anything or to identify yourself in any way (43) |
| autonomy, Tradition 4 | the script is "meant to serve as a suggested template" and meetings may edit it (147) |
| self-support, Tradition 7 | the dāna basket in the announcements (151) |
| no governing hierarchy, Tradition 9 | peer-led, following no one leader or teacher; the facilitator disclaims any particular authority (147) |
| confidentiality, Tradition 12 | the closing (151) |
| singleness of purpose and no outside issues, Traditions 5 and 10 | **inverted.** "In the Dharma, there's no such thing as an 'outside issue' to my recovery when all things are interdependent" (103) |
| attraction rather than promotion, Tradition 11 | partial only: the program presents itself as not the only path and as compatible with other programs (xi, 147) |

What is genuinely absent is narrower than a charter and easy to state. A mechanical search of the
full text returns no occurrence of "group conscience", "consensus", "business meeting", "trusted
servant", "quorum", "rotation", "bylaw" or "governance". The fellowship names an authority and
supplies no written procedure by which that authority reaches a decision. That is the real
asymmetry, and it is a difference in the *specification* of governance rather than in its presence.

**The fellowship exists because of a governance failure of exactly the kind this book models.**
Recovery Dharma is a 2019 schism from Refuge Recovery, and the personal stories, written by people
who were officers of the predecessor, say so plainly. One contributor followed the predecessor's
founding teacher, whose meditation organization was the hub from which Refuge Recovery grew, and
became Refuge Recovery's Executive Director (84). Another managed its retreats and co-hosted
its conferences (98). Her account of what happened is the passage to read twice: the
community "was
heavily influenced by unhealthy masculinity and inequities among leaders", and "Great heartache
ensued as people were harmed and a sangha was fractured" (98). A third contributor describes
arriving at the 2019 Refuge Recovery conference and "walking into division", and calls it the
moment Recovery Dharma was born (119).

Two things follow, and both bear directly on Part Two.

The successor's constitutional commitment was chosen in response to that failure, deliberately and
by people who had lived it. The Executive Director's account of the founding is explicit about the
design: "We wanted to be intentional in our framework — it had to be peer-led and trauma-informed"
(84). The predecessor was organized around a named founding teacher. The successor's first stated
commitment, recited in every meeting, is that it follows no one leader or teacher. A fellowship with
no knowledge of this model, and no interest in Golub and Jackson, responded to concentrated
influence by abolishing the office that concentrated it. That is Traditions 2 and 9 arrived at
independently, in 2019, under pressure.

**An independent account corrects where that line falls, and the correction improves the fit.**
Everything above comes from the successor's own literature, written by people who left, which is
the weakest possible evidential position for a claim about why a schism happened. *Tricycle*
covered the split on 13 July 2019 and was read at source on 17 August 2026. It confirms the
structural fact from outside: two nonprofits came out of 2019, the continuing body retained
associated teacher-led retreats and professional treatment options, the successor was formed
without them, and individual sanghas chose between them. It also corrects the contrast. Both
organizations describe their *meetings* as peer-led and democratically run, and the predecessor's
own book did so before the split, so the difference was never that one had peer-led meetings and
the other did not. What separates them is the layer above the meeting.

That is a better fit to what this book models, not a worse one. The model has no representation of
a meeting's internal democracy, which both fellowships share and always did. What it has is a
governance layer that can be concentrated or diffuse, and the split is precisely about whether
such a layer exists above the group at all. The independent source therefore narrows the claim to
the one the model can actually speak to.

And there *is* a decision procedure, at least once, even though none is written down. The
transition was not decreed: "all of the meetings in our area voted to switch from Refuge to RD"
(119). A vote across meetings is a group-conscience act in everything but name, and its existence
in practice alongside its absence in the literature is the sharpest single observation in this
section.

The model-relevant consequence should be stated carefully, because the first pass overstated it.
A2.4 gives five Traditions empty governance rows and uses them as protective modifiers, and the
effective-adherence construction needs provisions whose adherence can vary independently while the
constitution stands still. Recovery Dharma does have a fixed constitution: the three jewels, the
Four Noble Truths, the Eightfold Path and the Five Precepts are not what a meeting edits. What it
lacks is *differentiation*. Its governance commitment is a single undivided act of refuge rather
than twelve separately adherable provisions, so there is no set of rows to vary one at a time and
no counterpart to the Tradition ranking of A5.2. That is a statement about the shape of the object,
not about its absence, and it is weaker and truer than what this section said before.

None of this compares the two fellowships for quality of governance. It observes that one of them
was founded, within living memory and at considerable cost to the people who did it, on the
proposition this book spends twenty-five chapters arguing for.

### A12.5 What the fourteen personal stories show

Section II was not read in the first pass and was described then as the one place the source might
carry anything resembling evidence about what members do. It was read in full afterwards, and it
does. What follows is testimony, written by participants in their own program literature, which is
the genre most likely to tidy a history in hindsight. It is reported here as testimony and supports
no rate, no proportion and no outcome.

**Arrival is almost entirely exogenous, which inverts the model's arrival term.** A2.7 makes
endogenous arrivals scale with members' Step 12 state and a single attraction multiplier, with a
separate constant `lam_exog` for everything else. Across the fourteen stories the reported routes in
are a flier on a coffee shop noticeboard (59), an existing meditation community (63), the Buddhist
Recovery Network website and a book available free online (70), an internet search during the 2020
pandemic (80), online meetings joined from a thousand miles away (88), a therapist's referral (92),
a Buddhist chaplain visiting a treatment unit (106), a stranger's message on a meditation app (114)
and, in three cases, founding a group rather than finding one. Only one route resembles a member
carrying the message to a stranger. For this fellowship the exogenous constant would carry nearly
all of the arrivals and the endogenous term would be close to idle, which is the reverse of the
weighting the model uses and the reason inference 6 of A12.7 cannot be carried over unchanged.

**Membership overlaps rather than substitutes.** Several contributors describe attending Recovery
Dharma and a Twelve Step fellowship at the same time, one naming a sponsor, wise friends and a
therapist in the same sentence (88), and one arriving after a suggestion to attend a second meeting
on a day they had already been to a first (70). The model has one room and no representation of a
member belonging to two fellowships, so it cannot express the most common pattern in this sample.

**Two contributors left Twelve Step fellowships over the Traditions themselves.** One found the
singleness-of-purpose rule "stifling" because the presenting problem was not the only problem (70);
another describes being asked to avoid discussing addictions deemed unrelated to the meeting, and
sets against it the claim that in the Dharma nothing is an outside issue because everything is
interdependent (103). The book's own reading of Traditions 5 and 10 is that they protect a group's
capacity to do one thing well. These two accounts are the cost side of that protection, reported by
people who paid it. A model in which Tradition adherence only ever helps has no place to put them.

**Service is described as load-bearing, and one contributor states the mechanism in the model's own
shape.** Reported service includes chairing and facilitating meetings, hosting, mentoring, finding
locations, organizing retreats, serving as an intersangha representative, and sitting on the global
board. One account moves from observation to practice in two sentences: the people who served most
seemed most at ease, so the writer began serving too, and later concluded that nothing helped more
than helping other people (106). That is the helper-therapy proposition the corpus already holds in
Pagano et al. (2004), arrived at here by noticing it in a room. It is an observed association
reported by one person and is not evidence of direction.

**The order gate is contradicted in the source's own words.** A12.7 argues that two of the model's
core inferences depend on practices being worked in sequence, and that Recovery Dharma's path is
not. A contributor puts it more sharply than this appendix did: the Eightfold Path is supportive
precisely "because it's not a consecutive sequence", and the Dharma is "kaleidoscopic", each part of
the path reflecting the others (65). That is a member describing the absence of the order gate as a
feature.

**Affinity meetings spawn cheaply, and a member reports the homogeneity benefit directly.** A12.7
names a trade the model cannot score, between within-room homogeneity and room size. One account
supplies both halves: noticing that no meeting existed for a particular process addiction, the
writer and others simply created a sangha and meetings for it, and reports that although every
addiction is welcome at every meeting, connection and healing deepened among people concentrating on
the same topic (103). The same contributor draws the structural contrast explicitly, that this
fellowship does not have to spawn a new fellowship for each new process addiction. Cheap
within-fellowship segmentation is an architecture the model has no way to represent, since it has one
room of capacity 60.

**Growth outran the founders, and one of them says so.** A founding contributor describes the
fellowship going from the same five people doing everything to a point where she knows neither half
the board nor most of the group's online administrators, alongside a main online group of more than
ten thousand people (84). That is the scaling problem of Part Two stated from the inside, by someone
watching it happen, and it is offered here only as a description and not as a measurement of
anything.

---

### A12.6 What an actual comparison would require

Registered so that the gap is explicit rather than implied.

1. A step-resource matrix for Recovery Dharma over the same eight resources, elicited from people
   in the fellowship rather than authored here.
2. A governance matrix, which cannot be built until it is decided what plays the Traditions' part:
   the meeting script, the commitments of The Practice, or neither.
3. A prespecified equivalence margin, because the interesting claims are absence-of-difference
   claims, and A5.2 already records that the founding-composition contrasts are unresolved for
   exactly this reason.
4. Membership data for both fellowships, which the project has for neither.

Absent all four, what is above is a reading of two sets of documents in a shared vocabulary. It
supports no comparative claim about outcomes, effectiveness, or persistence, and it must not be
cited as though it did.

### A12.7 The model's core inferences, and which of them travel

A12.3 and A12.4 read two sets of documents. This subsection does something weaker and more general:
it states what the model infers about groups of this kind, stripped of AA vocabulary, and then asks
which inferences depend on features Recovery Dharma shares. Everything here is theme-level. A theme
that travels is a hypothesis about a fellowship the model has never been fitted to, not a result.

**The six core inferences, stated without reference to any fellowship.**

1. *The causal chain runs one way and through the room.* Member practice states produce group
   resources; resources feed back into individual growth. There is no direct member-to-member
   coupling anywhere in the model. Whatever a group provides, it manufactures out of the aggregate
   practice of the people currently in it.
2. *Growth is gated multiplicatively, not added up.* Three gates multiply: an order gate making each
   practice depend on the one before it, a peer gate weighted by `beta`, and a capacity gate whose
   weight `w` rises linearly from 0.05 at the first practice to 1 at the last. Late practice is
   therefore both the most group-dependent and the most capacity-limited thing a member does.
3. *Retention and reproduction load on opposite ends of the sequence.* Exit hazard falls with early
   practice, the mean of Steps 1 to 3. Endogenous arrivals scale with late practice, the Step 12
   state alone. A group keeps people through its cheapest practice and reproduces through its most
   expensive one.
4. *Dispersion is a multiplier, not a detail.* The `unity` term, one minus twice the standard
   deviation of practice level among established members, multiplies three of the eight resources:
   identification, continuity and gentle pressure. Spread degrades a room independently of level.
5. *Openness compounds across its channels.* Losing Tradition 3's friction path costs
   2.962 [1.848, 4.077] in final membership and its governance path 6.027 [5.043, 7.012], but losing
   both costs 11.045 [10.030, 12.060], with interaction -2.055 [-3.414, -0.696]. The joint loss
   exceeds the sum of the parts.
6. *Referral loss is slow and it is disguised.* Under pure attraction loss, membership runs 21.55 at
   year 5, 11.68 at year 10, 2.50 at year 20 and 0.51 at year 30, while endpoint viability falls
   from 0.970 to 0.0275. In these runs a group losing its referral channel looks healthy for years
   before the decline is legible.

**Which of these depend on features Recovery Dharma shares.**

| Inference | Travels? | Why |
|---|---|---|
| one-way causal chain | yes | the source describes the sangha as where the teachings find expression and are put into action, which is the same one-way shape |
| multiplicative gating | **no** | the gating rests on the order gate, and the Eightfold Path is explicitly not worked in sequence |
| retention and reproduction on opposite ends | **no**, and this is the interesting failure | it is a corollary of the order gate; remove the sequence and the two ends are no longer far apart |
| dispersion as multiplier | yes, and it becomes sharper | see the affinity-meeting note below |
| openness compounds | untested either way | Recovery Dharma is open by construction, so the model's loss conditions have no counterpart to switch off |
| referral loss is slow and disguised | partially | the arrival channel differs in kind; see below |

**The sequence is where the two programs part company, and it is load-bearing.** Inferences 2 and 3
are not independent findings. Both descend from the order gate, which makes each Step's growth
depend on the state of the one before it. That gate is why the practice driving arrivals is also the
most expensive to reach, and it is why a group's reproduction lags its retention. Recovery Dharma's
Path is grouped under three headings and practiced simultaneously, and the source states that each
person practices each aspect in their own way. A program without a sequence has no structural reason
for its reproduction-driving practice to be its costliest one. That is the single largest difference
between the two, larger than any count, and the model can identify it precisely because the order
gate is an explicit term rather than an assumption buried in prose.

**Dispersion, and the one place the model has something uncomfortable to offer.** Affinity meetings
are encouraged by the source, including the instruction to start one where none exists. In the
model's vocabulary that is deliberate management of within-room dispersion: it raises homogeneity
inside each room while reducing the number of people in it. The `unity` term says the first effect
raises three resources, and the saturation terms say the second lowers several. The model cannot
score the trade, because it has one room of capacity 60 and no representation of a fellowship split
across rooms. What it can do is name the trade as a real one with effects in both directions, which
is more than the source does and less than a recommendation. Nothing here evaluates affinity
meetings, and nothing here should be read as advice about them.

**The arrival channel is a scope limit rather than a difference.** Endogenous arrivals in the model
scale with members' Step 12 state and a single attraction term, which presumes members belong to one
group. Recovery Dharma presents itself as not the only path, compatible with other programs, and
commits members to attending recovery meetings whether with Recovery Dharma, other Buddhist
communities, or other fellowships. The model has no representation of shared or overlapping
membership at all, so inference 6 cannot be carried over as stated. This belongs with A11 item 4,
the absence of a competing organization, and it is the same gap seen from the other side.

**The helper threshold is a hypothesis the model generates and cannot settle.** The recipient
capacity term is opportunity per high-practice potential helper, so widening the pool of eligible
helpers enlarges the denominator. Recovery Dharma widens it deliberately: the mentor role is not a
formal position, nobody is certified or authorized, and anyone with any period of renunciation and
practice may serve. The model therefore predicts a lower recipient resource per helper under that
rule, which sounds like a finding and is not one. The clean recipient ablation is unresolved: forcing
recipient capacity to one changes final membership by 1.028 [-0.259, 2.314], an interval crossing
zero, which is not the same as no effect. Disabling Step 12 does cost 5.325 [4.437, 6.213], but that
is the whole Step, not the recipient path, and A5.1 is explicit that the mechanism-specific version
of this question has no released answer. Anyone tempted to read the helper threshold as a finding
should stop at the ablation.

**What none of this licenses.** No comparison of effectiveness, persistence or outcome between the
two fellowships. No claim that either program's structure is better suited to the mechanisms above,
since the mechanisms are authored. No advice about how a meeting of either kind should be run, and
nothing whatever about an individual's recovery.

### A12.8 The Machinery

This section was written to be self-contained and is now depended on in one place. Chapter
Twenty-Four cites the 2019 schism described in A12.4 as the closest thing to a live case the book
has, and states there that it corroborates rather than confirms. Nothing else in Parts One through
Five, in A1 through A11, or in the paper depends on this section; the primer carries a short
follow-up of its own. Removing A12 would require removing four paragraphs of Chapter Twenty-Four
with it.

**1. What the comparison says.** Four findings, in descending order of how well they are supported.

The word simplification does not survive a count: the program carries thirty-five enumerated items
across seven lists against twenty-four across two, and the eight-against-twelve reading compares one
list with one list.

Two of the model's six core inferences, multiplicative gating and the loading of retention and
reproduction on opposite ends of the sequence, both descend from the order gate and therefore do not
travel to a program whose path is not worked in sequence. A member of the fellowship states the same
thing independently, calling the path kaleidoscopic rather than consecutive.

The fellowship has a group-conscience analogue, the sangha, which is constitutional rather than
procedural, and it has no written decision procedure. An earlier draft of this section claimed it
had no Traditions-equivalent object at all, which was wrong, and correcting it produced the finding
below. What the governance object lacks is not existence but differentiation: it is one undivided
act of refuge rather than twelve separately adherable provisions, so there is nothing for A5.2's
Tradition ranking to range over.

And the fellowship is a 2019 schism from a predecessor organized around a single named founding
teacher, which fractured over inequities among its leaders. Its successor's first stated commitment,
recited at every meeting, is that it follows no one leader or teacher. That is Traditions 2 and 9
reached independently and under cost, and it is the only contemporary case of the kind the project
has.

One threat to validity belongs to this section rather than to A11, because it is visible only from
here. The architecture encodes AA's document structure rather than recovery-group structure in
general: it requires one Step matrix and one differentiated Tradition matrix, and this comparison
exhibits a functioning fellowship that distributes the same functions across a practice taxonomy, a
commitments list, a community chapter and a meeting script, and whose governance commitment does not
decompose into rows at all. A12.5 adds a second: the model's arrival term is weighted for a
fellowship that recruits through its members, and this one recruits mostly through the internet,
professionals and its own free book.

**2. The technical version.** Every quantity attributed to the model here is deterministic algebra
on the two authored matrices at the canonical hash, and carries no interval. For Step `j`,
group dependence is

```text
beta[j] = row_sum(S[j,:]) / max_k row_sum(S[k,:])
```

which is 1.000 at Steps 1 and 12 and below 0.71 everywhere else. Column shares are
`S[j,k] / col_sum(S[:,k])`: Step 1 holds 0.800 of admission and 0.588 of identification, Step 2
holds 0.526 of proof, Step 5 holds 0.667 of confidentiality, Step 12 is the sole nonzero entry in
recipient opportunity, and counsel and gentle pressure spread over eleven Steps each with top shares
of 0.300 and 0.226. Governance mass is `col_sum(GOV[:,k])`, largest at 2.40 for recipient
opportunity and smallest at 1.00 for gentle pressure.

The interval-bearing figures quoted in A12.7 are not recomputed here. They are the released
confirmatory results reported in A5.1, A5.2 and A5.4, at 400 seeds paired by common random numbers,
and they are quoted rather than re-derived so that this section adds no cache and no seed. The one
figure a reader should not over-read is the clean recipient ablation, 1.028 [-0.259, 2.314], whose
interval crosses zero and which is therefore unresolved rather than null.

The counting exercise is arithmetic on the source's own lists: three jewels, four Noble Truths,
eight path factors, five precepts, four heart practices, four foundations of mindfulness and seven
commitments in The Practice, totalling thirty-five across seven lists.

**3. Notes on sources.** One source does all the work, and all of it has now been read. Sections I
and II were read in full on 16 August 2026, as were the glossary, the meeting format and the
dedication of merit. The selected meditations and the inquiry questions, which are practice material
rather than description, were read on 13 September 2026 and hold no governance text. Page references
are the printed pagination, which runs sixteen behind the PDF pagination in the arabic range.

**A first pass got the central question wrong, and the record should show how.** That pass read
Section I and the meeting format, did not read the personal stories, and concluded that the
fellowship had no Traditions-equivalent object. Two things were missed. The meeting script has every
member affirm trust in the wisdom of the Sangha, which is a group-conscience analogue sitting in
plain sight in a document that had been read. And the stories, which had not been read, contain the
fellowship's founding history, the schism that produced it, and the one recorded instance of
meetings voting. The error was corrected by reading the rest, and the correction is the reason this
section now has a finding worth citing in a chapter. The general lesson is the one the corpus rules
already state: file presence is not reading, and a partial read is a place where an absence claim
can go wrong.

The absence claim that survives is narrow and was tested mechanically over the full text rather than
by reading alone. No occurrence of "group conscience", "consensus", "business meeting", "trusted
servant", "quorum", "rotation", "bylaw" or "governance" appears anywhere in the document. The single
"committee" and the references to an elected board occur inside personal stories and describe the
global nonprofit rather than a rule binding a meeting.

The individual at the centre of the predecessor organization's collapse is named in the source and
is deliberately not named in this project. The structural claim does not require the name, and
nothing here can adjudicate an allegation about a living person. Chapter Twenty-Four carries the
same restriction.

Provenance took two steps. The copy first read was an ephemeral session attachment removed from
disk before it could be stored; the same document was then located locally and confirmed by page
count, byte size and verbatim spot-checks against passages already read. That copy is the one
hashed and indexed. The bibliographic record was taken from the file's own title and copyright
pages rather than from an independent catalogue entry, which is the one open item on this source.

**4. References.**

**Read in full:**

Recovery Dharma Global (2023). *Recovery Dharma: How to use Buddhist practices and principles to
heal the suffering of addiction.* Second edition. Recovery Dharma Inc. CC BY-NC-SA 4.0. Read in
full: the contents and front matter through The Practice (ix to xvi); Section I entire (1 to 54);
Section II entire, the fourteen personal recovery stories (57 to 121); and Section III entire, the
selected meditations (122 to 135), the inquiry questions (136 to 144), the glossary (145 to 146),
the meeting format (147 to 151) and the dedication of merit (152). The meditations and inquiry
questions were read on 13 September 2026 and the rest on 16 August 2026. Source of every page
reference in this section and of the four paragraphs in Chapter Twenty-Four. Stored as
`research/incorporated/RecoveryDharma_2023/`, git-ignored with a SHA-256 and a verification index.
It is the one source in the corpus whose licence would permit committing the document; the project
git-ignores it anyway, because the rule is uniform.

Jensen, K., and M. Abrahams (2019). "Buddha Buzz Weekly: Refuge Recovery Splits." *Tricycle: The
Buddhist Review*, 13 July 2019. Read at source on the publisher's site on 17 August 2026 and held
as record only. The one independent account A12.4 uses, for the structure of the split and for the
correction that both organizations describe their meetings as peer-led.

**Referenced but not reproduced:**

The Pali canon and the early Buddhist teachings from which the Four Noble Truths, the Eightfold
Path, the Five Precepts and the four foundations of mindfulness derive. This section takes all of
them at second hand, as Recovery Dharma presents them, and consulted no primary Buddhist text. Any
claim here about what the Dharma says is therefore a claim about what this fellowship's literature
says the Dharma says, and the distinction matters for the chronology argument in A12.1, which rests
on the source's own dating rather than on independent scholarship.

**Internal, and reproducible from this repository:**

`model/aa_group_model.py` at the canonical hash, for `S`, `GOV`, the group-dependence coefficients,
the column shares and the governance masses. The interval-bearing figures are quoted from A5.1,
A5.2 and A5.4 and their registered caches; this section computes none of them and adds no cache of
its own. The source record, read scope and rights position are in
`research/incorporated/RecoveryDharma_2023/` and in `research/SOURCES.md`.

**What was not read:**

Little that is independent about the 2019 schism. Beyond the successor organization's own
literature, written by people who left the predecessor, A12.4 rests on one contemporaneous press
account, *Tricycle*'s. No court record or statement from the predecessor was sought, and the
predecessor's own account of the same events has not been read. The record still leans to one side,
and Chapter Twenty-Four's use of it inherits the weakness.

The empirical literature on Buddhist and mindfulness-based recovery programs, which was not searched
at all. This section compares program documents and one fellowship's account of its own history. It
does not know what either fellowship's outcomes are, and no part of it should be cited as though it
had looked.

---

## A13. The personal stories read against the model's arrival term

A12 compared program documents. This section does something narrower and evidentially stronger: it
reads the thirty first-person accounts of 1939 against one specific modelling choice, the arrival term in
A2.7, and asks whether the fellowship the model was built from actually recruits the way the model
says. It is a coding exercise on text. It adds no cache, no seed and no interval, and it changes no
number in the release.

### A13.1 What the source is, and a correction to the record

The document read here was supplied as the fourth edition of *Alcoholics Anonymous*. It is not.
Its title page reads "The 4th Edition of Alcoholics Anonymous" and immediately below, "This book
contains a complete reprint of the 1st edition 1939", published by the Alcoholics Anonymous Big
Book Study Group and marked "No Copyright 1999". The fourth edition is the numbering of the
reprinter's own printing, not of AA's editions. Its contents are the 1939 first edition: the
Foreword, the Doctor's Opinion, the eleven chapters of the basic text, and the thirty personal
stories of that edition, from "The Doctor's Nightmare" through "Ace Full Seven-Eleven". An earlier
version of this section counted twenty-nine. The contents page lists thirty, and the 1939 working
manuscript accounts for all of them: nineteen in the circulated draft, a twentieth struck through
there and printed anyway, and ten added after the draft went out. AA's actual
fourth edition of 2001 carries an entirely different set of stories and roughly four hundred more
pages.

This matters twice. The stories analyzed below are the 1939 stories, contemporaneous with the
founding period Part One is about, and not a 2001 selection. And the work was already in the corpus
as `BigBook_1939`, whose record notes the same reprint and the same contested rights position. The
uploaded file differs from the stored one by a few bytes and 99.91 per cent of its extracted text is
identical, so this is a second copy of a source the project already held and had recorded as
"acquired; not yet used as claim support". That last clause is what this section changes.

### A13.2 The estimand and the coding rule

A2.7 makes arrivals Poisson with mean `lambda * dt`, where

```text
lambda = lam_exog + lam0 * sum_i X[i,12] * attraction_T11.
```

The first term is arrival that does not pass through a member. The second is arrival carried by
members, scaled by their Step 12 state. The model gives the endogenous term the dominant role, and
that is an authored choice. The question here is whether the fellowship's own accounts of how people
arrived support it.

The coding rule is: for each story, does the account describe a person who was themselves a recovered
alcoholic making contact with the subject before the subject stopped drinking? A family member
hearing of the fellowship and then arranging such a contact is coded as member-carried, because the
arrival still passes through a member; the family is the broker, not the channel.

### A13.3 The census

Twenty-seven segments were recovered automatically from the running heads. One of them, "A Vision
For You", is Chapter 11 of the basic text rather than a story, and is excluded, leaving twenty-six
story segments out of the book's thirty stories. The automatic split did not separate the other
four, and it was not retained, so which four is not recorded; they are outside the count rather than
coded. Explicit personal-contact language appears in twenty of the twenty-six.

That count is a **lower bound and should be read as one**, because the matcher keys on a fixed
phrase list and misses accounts describing the same event in other words. The six segments without a
match are named so a reader can check them: "The Doctor's Nightmare", "The Unbeliever", "Our
Southern Friend", "Fired Again", "Smile With Me, At Me" and "Hindsight". At least two are certainly
false negatives. Dr Bob's account, the first story in the book, describes his wife being telephoned
by a woman who wanted him to meet a friend who might help, then six hours in that friend's company,
and finally the observation that the man "talked my language"; none of that matches a listed phrase.
"Fired Again" describes a neighbour who had heard of a recovered alcoholic doctor "busily engaged in
passing on the benefits he had received", which is the same channel reported at one remove. The true
figure is therefore above twenty and the method cannot say by how much.

The recurring shape is a visit, and often several. One writer records that while he was in hospital
"about twenty men called on me" and told him their experiences. Another was seen by a doctor who
"sent two of the members" to him. A third describes men who came to him "one by one and told me"
what had happened to them. A fourth met his first recovered alcoholic as a fellow patient. What the
accounts do not describe is somebody reading their way in.

### A13.4 The exception, and what the fellowship said about it

One story is the exception and the fellowship marked it as one. "Lone Endeavor" is the account of a
man in the far west reached only by correspondence and a pre-publication copy of the book, and the
narrative frame around it is the fellowship describing its own experiment. It calls the attempt
"our initial effort to help others through the book alone", says it was "the first time we have had
an opportunity of trying to help an alcoholic at long distance", and records that during the silence
that followed "we began to think this book was inadequate without personal contact".

That is the strongest single piece of evidence in this section, and it is strong because it runs
against the interest of the people writing it. A fellowship publishing a book had every reason to
believe the book would be sufficient. Its own literature says it doubted that, and that the doubt
was based on the absence of a personal visit.

### A13.5 What this supports, and what it bounds

**It supports the architecture of the arrival term for the fellowship the model was built from.**
The dominant endogenous channel is not an artifact of convenience. It is what the source describes,
in the twenty-six accounts the census covers, and the one case of arrival without a member is presented by
the fellowship as an untested experiment about which it recorded doubt.

**It bounds that architecture to that fellowship, and A12.5 is the other half of the bound.** The
fourteen Recovery Dharma accounts report arrival through a noticeboard flier, a website, a free
online book, internet searches, online meetings, a therapist and a prison chaplain, with almost no
member-carried arrival at all. Two fellowships, eighty-four years apart, sit at opposite ends of the
same parameter. A model that fixes the weighting between `lam_exog` and the endogenous term is
therefore making a claim about a period and an organization rather than about mutual-aid groups, and
the pair of censuses is the evidence for saying so.

**Two smaller observations, both weaker.** Dr Bob's account gives four reasons for passing on what he
learned, of which the fourth is that each time he does it he takes out "a little more insurance for
myself" against a slip. That is the helper-therapy proposition the corpus holds in Pagano et al.
(2004), stated by the fellowship's co-founder in 1939 and consistent with the model's treatment of
Step 12, though a single retrospective statement of motive is not evidence of direction. And Dr Bob
describes what moved him as a man who "talked my language", after reading widely and consulting
many non-alcoholic experts to no effect. That is the identification resource of A2.2, which the
matrix loads most heavily onto Step 1, described from the inside.

**What it does not do.** It does not validate any numerical value. `lam_exog`, `lam0` and the
attraction multiplier remain three of the hundred and eighteen registered values, fitted to nothing.
A census of how people say they arrived cannot set a rate. It also cannot speak to survivorship: the
thirty accounts are of people who recovered and were chosen for a book intended to persuade, so
they are the least representative sample imaginable of everyone the fellowship met. Nothing here
touches retention, dropout or group survival.

### A13.7 The same census on the fourth edition, and what moves

The 1939 reading was carried on this list as unextendable, because the fourth edition of
2001 carries a different set of stories and the project did not hold it. The Human Author owns
several copies and supplied the text on 17 August 2026, and AAWS also posts the book in per-section
PDFs, so the obstacle was never as solid as this appendix said.

The fourth edition has forty-two personal stories in three parts: ten Pioneers, seventeen They
Stopped in Time, fifteen They Lost Nearly All.

**The coding rule had to be extended, and the reason is itself the finding.** A13.2 asks whether a
recovered alcoholic made contact with the subject before the subject stopped drinking. In 1939 that
question had two answers, because a person who wanted to find the fellowship had almost no way to
do so: it was small, unadvertised, and not yet in any telephone directory. By 2001 there are three
answers, and the middle one could not have existed in 1939.

| Initiating channel | Stories | Share of classifiable |
|---|---:|---:|
| A member sought the subject out | 13 | 43% |
| The subject contacted the fellowship | 6 | 20% |
| A professional or an institution referred | 11 | 37% |
| Channel not stated plainly enough to code | 12 | |

Thirty of the forty-two state the channel plainly. Twelve do not, and they are reported as
unresolved rather than assigned, on the same principle the release gate applies to an interval
crossing zero.

**What this supports.** The model's arrival term has two parts, an exogenous rate and a
member-carried rate scaled by Step 12 practice, and the fourth edition shows both operating. The
exogenous term is not a modelling convenience: its code comment names courts, treatment and
desperation, and the stories supply a judge sending a man to A.A. for a month, a college requiring
attendance as a condition of readmission, counsellors producing meeting lists, and repeated arrival
through treatment centres. In 1939 that term had almost nothing to point at. It now has more than a
third of the classifiable stories.

**What this bounds.** The member-initiated share falls from twenty of twenty-six in 1939, seventy-
seven per cent, to thirteen of thirty here, forty-three per cent. The model holds `lam_exog` fixed
at 0.12 per week for every run, so it cannot represent that shift at all. A fellowship large enough
to be found in a telephone book, and embedded in courts and treatment systems that refer to it, has
an exogenous arrival rate that grew with its own institutional presence. That is a mechanism the
model does not contain, and the two censuses together are the clearest evidence in this appendix
that it should be treated as a limitation rather than a detail.

**What it is not.** Neither census is a sample. The stories are selected by the fellowship for
publication, and selection on outcome is total: every subject recovered. Nothing here estimates
the arrival mix in the population, and the comparison between editions is a comparison between two
edited collections sixty-two years apart, not a time series.

### A13.6 The Machinery

**1. What the census says.** The model's arrival term gives the member-carried channel the dominant
role. The 1939 accounts describe arrival that way, with a lower bound of twenty of the twenty-six
story segments recovered from the thirty stories carrying explicit personal-contact language, and the single
counter-case is one the fellowship itself flagged as an untested experiment about which it recorded
doubt. Read beside A12.5, where a modern fellowship arrives almost entirely without members, the
pair localizes the arrival weighting as a property of a fellowship and a period rather than of
mutual-aid groups in general.

**2. The technical version.** The estimand is the arrival intensity of A2.7. The coding rule is in
A13.2 and treats a family broker as member-carried. Segmentation was automatic from running heads
and recovered twenty-seven segments, of which one is a chapter and is excluded, leaving twenty-six
of the thirty stories. The phrase matcher is a lower bound; A13.3 names all six segments it
failed to match and identifies two as certain false negatives, so a reader can see the size and
direction of the error rather than take the figure on trust.
No number in the release changes. No cache, seed, horizon or interval is involved, and nothing here
is a stochastic claim.

**3. Notes on sources.** The file supplied as the fourth edition is the 1939 first edition in the
1999 Big Book Study Group reprint, and A13.1 sets out how that was established. It duplicates
`research/incorporated/BigBook_1939/`, whose SOURCES.md entry previously read "acquired; not yet
used as claim support"; this section is the first use. The reprint asserts no copyright and the
1939 rights position is contested, which is why the project holds the document git-ignored rather
than as record only. Quotations here are short phrases with attribution, per the project rule that
nothing is quoted at length.

The stories are testimony selected for a persuasive purpose, and the survivorship problem in A13.5
is the governing limitation on everything in this section.

**4. References.**

**Read in full:**

*Alcoholics Anonymous*, first edition, 1939, in the Alcoholics Anonymous Big Book Study Group
reprint of 1999. The thirty personal stories, printed pages 183 to 400, read for this section;
the Foreword, the Doctor's Opinion and the eleven chapters of the basic text were read for context.
Stored as `research/incorporated/BigBook_1939/`, git-ignored with a SHA-256 and a verification
index.

**Internal, and reproducible from this repository:**

`model/aa_group_model.py` at the canonical hash for the arrival term of A2.7 and the identification
column of A2.2. A12.5 for the Recovery Dharma census that forms the other half of the bound. No
cache is read or written by this section.

**What was not read:**

AA's actual fourth edition of 2001, which was the document requested and which the project does not
hold. Its stories are a different selection made sixty-two years later, and a census of them would
be a genuinely separate finding: it would show how the fellowship's recruitment channel had changed
across the period in which telephone, treatment referral and eventually the internet became
available. That comparison is the obvious next piece of work and this section does not attempt it.

Any systematic literature on referral pathways into mutual-aid groups, which was not searched. The
census here is of one book's self-selected accounts and is not a study.
