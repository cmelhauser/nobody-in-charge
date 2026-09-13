# Parameter and Robustness Audit

This file records what was chosen, what was tested, and what the current release licenses.
The canonical model is `model/aa_group_model.py`, SHA-256
`c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`.
`research/ROBUSTNESS-RESULTS.md` is the generated numeric companion.

## 1. What the count of 118 means

The registered sensitivity set contains:

| Kind | Count |
|---|---:|
| scalar defaults, room capacity included | 22 |
| Step growth speeds | 12 |
| nonzero Step-resource cells | 49 |
| nonzero Tradition-governance cells | 35 |
| **total registered values** | **118** |

This is not the number of all parameters or choices. The inventory in
`research/model-choice-inventory.json` separately records fixed constants, 108 structural
zeros, equations, thresholds, founders, arrival states, the viability cutoff, time step,
horizon, random-number design, and intervention definitions.

No value is fitted to longitudinal AA group data. The inflow and exit rates were originally
chosen to target roughly 45 members and 9 experienced members. After correcting capability to
have arithmetic mean one, 400 runs end at 17.80 members and the viable endpoints contain 1.25
experienced members on average. The target fails and was not retuned.

## 2. Provenance tiers

The tiers describe how tightly a perturbation range is constrained; they are not grades of
truth.

- Tier 1: inflow, exit, rent, and contribution values with at least an analogous empirical
  literature. The release screen varies these by 25 per cent.
- Tier 2: decay, step ordering, Hill shape, substitution, thresholds, and dropout protection.
  The tiered screen varies these by 25 per cent.
- Tier 3: resource saturation and member heterogeneity. The tiered screen varies these by 50
  per cent.
- Step speeds and nonzero matrix magnitudes receive 50 per cent ranges in the tiered screen.

The decay rate `delta0 = 0.06` per week is the Tier 2 value with the most riding on it, second
only to `p_gate` in every screen. On 13 September 2026 it was set against the only estimates read
for anything comparable, Dinerstein, Megalokonomou and Yannelis (2022) on teaching skill and
Cohen, Johnston and Lindner (2023) on general skills during unemployment. Both measure skills
rather than practices, and both are one to two orders of magnitude slower. The value was not
changed: no source measures how fast a practice lapses, and a new authored value chosen after
reading papers about a different quantity would not be an improvement. Section 8.1 records that
large downward moves of it reverse the attraction-versus-referral ordering on final membership;
`research/SOURCES.md` has the reading.

Borrowing a functional form from a literature does not validate the numeric value in this
application. The two matrices remain author elicitations. Their structural zeros are choices
that multiplicative perturbation cannot test.

## 3. Design registry

The room capacity remains 60 and principal stochastic estimates remain at 400 paired seeds.
Expanded robustness means more parameter-space coverage, not a 1,000-member group and not
1,000 confirmatory seeds.

| Design | Registered size | Seeds per point | Interpretation |
|---|---:|---:|---|
| confirmatory condition and mechanism contrasts | 400 per condition | 400 | estimates and paired intervals |
| global joint perturbation | 334 draws at each of 12.5%, 25%, 50%; 1,002 total | 3 | broad screen |
| tiered joint perturbation | 1,000 draws | 3 | evidence-tiered screen |
| randomized nonzero matrices | 1,000 draws | 3 | magnitude test with zeros fixed |
| multi-level one-at-a-time | 118 x 2 x 4 = 944 points | 3 | local and larger-distance effects |
| Morris | 20 trajectories; 2,380 points | 5 | factor screen; interaction or nonlinearity |
| Sobol | 1,024 base rows; 11,264 points | 5 | conditional decomposition on eight leaders |
| structural variants | 5 architectures x 5 scenarios x 400 = 10,000 | 400 | one-choice architecture audit |
| numerical and horizon | 2,600 runs | 200 or 400 | tested integration step and finite horizon |

Parameter points using three or five common seeds are not independent replications of the
stochastic model. They classify robustness over the registered design. They do not estimate a
real-world probability.

## 4. Global simultaneous perturbation

Each draw independently perturbs all scalar defaults, Step speeds, and nonzero cells, then
re-derives normalized consumption, governance weights, and group-dependence coefficients. Each
point scores full adherence, pure Tradition 11 attraction loss with governance intact, and
exogenous-referral loss.

Counts are strict/tied/reversed for pure-attraction-loss minus referral-loss outcomes.

| Amplitude | Final N | Endpoint viability | Existence | Full viable in all 3 seeds | Full exists in all 3 seeds |
|---|---:|---:|---:|---:|---:|
| 12.5% | 301/0/33 | 323/10/1 | 318/16/0 | 302/334 | 334/334 |
| 25% | 251/1/82 | 269/64/1 | 262/72/0 | 291/334 | 325/334 |
| 50% | 213/17/104 | 201/117/16 | 215/117/2 | 256/334 | 287/334 |

The existence ordering is the most stable of the three and final membership the least stable.
The screen does not license the older claim that one undifferentiated ordering holds in every
draw.

## 5. Exact cancellation and blind spots

`GOVW` is column-normalized. At full adherence,

```text
q = GOVW^T 1 = 1
```

for every resource. The 35 nonzero `GOV` magnitudes therefore cannot affect a fully adherent
group. A screen that perturbs them and scores only full adherence has found an identity, not
robustness. At partial adherence those cells are live.

Multiplicative designs preserve every zero in both matrices. They cannot test the two-tier
division, index-pairing cells that are zero, or whether the sparsity pattern is defensible.
Threshold, cell-flip, resource-list, and independent-elicitation designs are needed for those
questions.

## 6. Structural variants

The base architecture is compared with four one-choice changes at 400 paired seeds per
scenario:

1. equal exposure of every Step to the capacity gate;
2. Tradition 3 on admission rather than retention friction;
3. resource capacity supplied by all living members;
4. a clipped piecewise-linear rather than hyperbolic capacity response.

| Architecture | Attraction loss N / exists / viable | Referral loss N / exists / viable |
|---|---:|---:|
| base | 12.380 / 1.000 / 0.985 | 0.510 / 0.105 / 0.0275 |
| flat gate | 6.613 / 0.870 / 0.6575 | 0.745 / 0.120 / 0.0550 |
| T3 on admission | 12.380 / 1.000 / 0.985 | 0.510 / 0.105 / 0.0275 |
| capacity from all members | 14.730 / 1.000 / 1.000 | 2.003 / 0.2575 / 0.1225 |
| piecewise-linear capacity | 13.038 / 1.000 / 0.995 | 1.020 / 0.145 / 0.0575 |

Referral loss is worse on all three outcomes in all five tested architectures. The older result
in which final size reversed under three variants was generated by the retired uncentred
capability model and is not a current result.

## 7. Tiered and randomized-matrix screens

| Design | Final N | Endpoint viability | Existence | Full viable in all 3 seeds | Full exists in all 3 seeds |
|---|---:|---:|---:|---:|---:|
| tiered, 1,000 draws | 783/10/207 | 818/165/17 | 821/177/2 | 833/1,000 | 943/1,000 |
| random nonzero matrices, 1,000 draws | 1,000/0/0 | 1,000/0/0 | 999/1/0 | 784/1,000 | 1,000/1,000 |

Counts are strict/tied/reversed for pure-attraction-loss minus referral-loss. Holding sparsity
fixed and replacing every nonzero matrix magnitude does not reverse the comparison. The broader
tiered design does, especially for final membership. This does not validate the zero pattern.

## 8. Multi-level OAT, Morris, and Sobol screens

All three caches are `complete` and match the model hash and their generating-script hashes. The
generated tables are in `research/ROBUSTNESS-RESULTS.md`. The retired 30-draw, 236-point,
10-trajectory, and 128-row Sobol results are correction history and are not authorized for public
prose.

### 8.1 Multi-level one-at-a-time screen

118 registered values, each moved alone by 10, 25, 50 and 75 per cent in each direction, three
common seeds per endpoint, 944 perturbation points. Screening design.

| Outcome | Strict | Tied | Reversed |
|---|---:|---:|---:|
| final membership | 931 | 2 | 11 |
| endpoint viability | 934 | 10 | 0 |
| existence | 933 | 11 | 0 |

Counts are pure-attraction-loss minus referral-loss. Full adherence is endpoint-viable in all
three seeds at 893 of 944 points and exists in all three at 936. Nine of the eleven membership
reversals are large downward moves of `p_gate`, `delta0` and `churn`; the other two are `S:11,5`
and `S:11,6`. Twenty-six of 118 values move referral-starved endpoint viability alone; 32 move
full-adherence endpoint viability alone.

Influence on maintenance, against a full-adherence baseline of 0.0431, as range over baseline:

| Parameter | At plus or minus 25% | Over the full ladder |
|---|---:|---:|
| `p_gate` | 5.45 | 14.64 |
| `delta0` | 3.27 | 12.98 |
| `a:10` | 2.22 | 2.76 |
| `het_sd` | - | 4.69 |

All 35 `GOV` cells return zero change in every outcome and scenario, maximum absolute deviation
5.6e-17, because the sweep runs at full adherence where column-normalised governance quality is
identically 1. That is a property of the reference point, not evidence of inertness.

### 8.2 Morris screen

Twenty trajectories, all 118 factors, plus or minus 25 per cent, four levels, delta 2/3, five
common random numbers per point, 2,380 evaluations, reference adherence 0.85.

| Rank | Factor | mu | mu* | sigma |
|---:|---|---:|---:|---:|
| 1 | `scalar:p_gate` | -51.780 | 52.440 | 57.611 |
| 2 | `scalar:delta0` | -51.210 | 51.210 | 54.039 |
| 3 | `scalar:churn` | -33.000 | 33.480 | 32.726 |
| 4 | `scalar:drop_k` | 24.300 | 24.300 | 23.068 |
| 5 | `scalar:lam_exog` | 22.680 | 23.460 | 24.579 |
| 6 | `scalar:het_sd` | 18.600 | 18.900 | 17.323 |
| 7 | `a:5` | 15.960 | 18.540 | 25.250 |
| 8 | `a:11` | 8.190 | 15.870 | 25.005 |
| 9 | `scalar:lam0` | 12.000 | 14.340 | 19.472 |

The eight-factor cut is untied: 15.87 against 14.34. Membership `mu_star` shares by kind are
scalars 44.9 per cent, `S` cells 33.7, step speeds 18.2 and `GOV` cells 3.3. The retired
ten-trajectory leaders `a:8`, `a:4` and `omega` now rank 15th, 27th and 37th.

### 8.3 Sobol decomposition

1,024-row base design over the eight Morris membership leaders, plus or minus 25 per cent,
reference adherence 0.85, five common random numbers per point, 11,264 executed evaluations,
2,000-resample bootstrap intervals. Noise-replicate total-order floor is 0.0429 for membership and
0.0728 for practice.

| Factor | Membership S1 [95%] | Membership ST [95%] |
|---|---:|---:|
| `p_gate` | 0.404 [0.288, 0.525] | 0.576 [0.510, 0.643] |
| `delta0` | 0.238 [0.156, 0.327] | 0.373 [0.320, 0.428] |
| `drop_k` | 0.032 [-0.014, 0.079] | 0.171 [0.145, 0.199] |
| `churn` | 0.023 [-0.020, 0.068] | 0.132 [0.111, 0.155] |
| `het_sd` | 0.022 [-0.015, 0.061] | 0.079 [0.064, 0.095] |
| `lam_exog` | -0.015 [-0.048, 0.018] | 0.058 [0.049, 0.068] |
| `a:11` | 0.005 [-0.018, 0.029] | 0.038 [0.031, 0.046] |
| `a:5` | -0.016 [-0.037, 0.004] | 0.029 [0.024, 0.034] |

`a:5` and `a:11` sit at or below the membership noise floor. Total-order sums are 1.456 for
membership and 1.464 for practice, so interaction is present and not dominant. The membership
first-order column is admissible at this base sample: no `S1` exceeds its `ST` and the sum is
0.693. The practice first-order column is not: `delta0` gives `S1 = 0.421` against `ST = 0.417`
and the practice first-order sum is 1.074. No practice first-order number is quoted in public
prose. Every index is conditional on these eight factors and these ranges, not on the model's
total variance.

### 8.4 Generating-platform provenance

Caches are hash-linked to the model and the generating script, not to a platform. The screens in
this section were executed on Linux x86-64 under NumPy 2.2.6, while the eight `oat_full.json`
parameter jobs completed before the pause, and the 400-seed confirmatory caches, were generated on
macOS. Re-executing a macOS-generated job on Linux reproduced every discrete outcome exactly and
differed on continuous outcomes only in the last representable digit, for example a mean practice
of 0.22608366753387557 against 0.22608366753387563. That is a difference of order 1e-16, far below
any reported precision, and it changed no classification. An independent verifier on a different
operating system should expect agreement to reported precision rather than bit-identical
reproduction.

## 9. Numerical and finite-horizon limits

At 200 paired seeds, final-membership differences relative to `dt=0.5` have intervals crossing
zero for `dt=1`, `0.25`, and `0.125`. The tested half-week step is adequate for the reported
comparisons; arbitrary-resolution convergence is not proved.

Mean membership continues to move from 29.34 at 10 years to 21.14 at 20, 17.80 at 30, 16.43 at
50, and 15.64 at 100. The release claims no equilibrium or indefinite persistence.

## 10. Reporting rules

1. Name the outcome: final membership, existence, endpoint viability, first crossing, recovery,
   or closure.
2. Name conditioning. Member quality in viable groups is selected on viability.
3. Report strict support, ties, and reversals separately.
4. Use intervals for 400-seed contrasts. A confidence interval crossing zero is unresolved, not
   evidence of equality.
5. Call the 118 entries registered sensitivity values, not all model parameters.
6. Keep semantic overlap, normalized linear coupling, state-dependent resources, and trajectory
   effects separate.
7. Do not describe finite-horizon endpoint viability as permanent survival.
8. Do not use the intentionally staged next-round corpus as current evidence.

The release gate enforcing these rules is `tools/check_release.py`.
