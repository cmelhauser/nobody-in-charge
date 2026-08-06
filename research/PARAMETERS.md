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

## 8. Remaining screens pending final generated summary

The multi-level OAT, Morris, and Sobol caches must have `complete` status and match both the model
and analysis-script hashes. Their exact results will be inserted from
`research/ROBUSTNESS-RESULTS.md` after generation. Until then, no older 30-draw, 236-point,
10-trajectory, or 128-row Sobol result is authorized for public prose.

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
