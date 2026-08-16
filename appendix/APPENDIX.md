# Technical Appendix

*Nobody in Charge.* Released model specification, estimands, numerical checks, sensitivity
designs, source boundaries, and reproduction instructions.

Human Author: Christopher Melhauser (christopher.melhauser@gmail.com). AI Writing Collaborator:
theonlymuffinbot (theonlymuffinbot@outlook.com). Released to the public domain under The
Unlicense. See `../ATTRIBUTION.md` and `../LICENSE`.

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

All three caches are complete and match both the model hash and their generating-script hashes.
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
model/aa_group_model.py                         canonical model
model/book-calculations.ipynb                   book verification notebook
paper/anonymity-as-an-aggregation-condition.ipynb  paper verification notebook
research/RELEASE-GATE-RESULTS.md                generated confirmatory report
research/ROBUSTNESS-RESULTS.md                  generated expanded-sensitivity report
research/model-choice-inventory.json            values, zeros, constants, and choices
tools/check_release.py                          independent fail-closed release gate
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
tectonic --outdir paper paper/anonymity-as-an-aggregation-condition.tex
pandoc reference/PRIMER-steps-and-traditions.md \
  -o reference/PRIMER-steps-and-traditions.pdf --pdf-engine=tectonic
python3 tools/check_release.py
```

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

The model's proper use is to make assumptions and comparisons explicit enough to test against
real group data. It cannot evaluate or advise any individual person's recovery.
