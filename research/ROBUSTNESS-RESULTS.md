# Expanded Robustness Results

Generated from the JSON caches by `tools/summarize_robustness.py`. Screening
parameter points use three or five common seeds and are not confirmatory replications.
The principal condition contrasts remain the separate 400-seed analyses, and the
decay-ordering section below is one of them rather than a screen.

## Provenance

- Model SHA-256: `c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`
- `mc_error.json`: complete, script `model/mc_error.py`
- `tradition_paired.json`: complete, script `model/tradition_paired.py`
- `structural.json`: complete, script `model/structural_variants.py`
- `sens3.json`: complete, script `model/sensitivity_uniform.py`
- `tiered.json`: complete, script `model/sensitivity_tiered.py`
- `oat_full.json`: complete, script `model/sensitivity_oat_full.py`
- `decay_ordering.json`: complete, script `model/decay_ordering.py`
- `decay_reversal.json`: complete, script `model/decay_reversal.py`
- `morris.json`: complete, script `model/morris_screen.py`
- `sobol.json`: complete, script `model/sobol_indices.py`

## Integration and horizon

| Scenario | dt | Horizon years | Seeds | Mean N [95% half-width] | Existence | Viability | Closure |
|---|---:|---:|---:|---:|---:|---:|---:|
| attraction | 0.5 | 30 | 400 | 12.380 [0.342] | 1.000 | 0.985 | 0.000 |
| full | 0.5 | 10 | 200 | 29.340 [1.713] | 1.000 | 1.000 | 0.000 |
| full | 0.5 | 20 | 200 | 21.140 [1.600] | 1.000 | 0.995 | 0.000 |
| full | 0.125 | 30 | 200 | 16.910 [1.241] | 0.995 | 0.980 | 0.005 |
| full | 0.25 | 30 | 200 | 18.180 [1.375] | 1.000 | 0.980 | 0.000 |
| full | 0.5 | 30 | 400 | 17.800 [0.883] | 1.000 | 0.985 | 0.000 |
| full | 1 | 30 | 200 | 18.850 [1.486] | 1.000 | 0.985 | 0.000 |
| full | 0.5 | 50 | 200 | 16.425 [1.080] | 1.000 | 0.995 | 0.000 |
| full | 0.5 | 100 | 200 | 15.640 [0.990] | 0.995 | 0.985 | 0.005 |
| referral | 0.5 | 30 | 400 | 0.510 [0.229] | 0.105 | 0.028 | 0.895 |

Paired final-N differences relative to `dt=0.5`:

- `dt=1` minus `dt=0.5`: 1.535 [-0.242, 3.312].
- `dt=0.25` minus `dt=0.5`: 0.865 [-0.971, 2.701].
- `dt=0.125` minus `dt=0.5`: -0.405 [-2.146, 1.336].
None resolves. The horizon series continues to move and is not a steady-state proof.

## Paired Tradition degradation

Reference membership is 13.0975; cross-seed SD is 5.6664. T3 and T11 are mixed adherence interventions.

| Tradition | Loss [95% interval] | t |
|---:|---:|---:|
| T3 | 2.993 [2.345, 3.640] | 9.06 |
| T11 | 1.880 [1.276, 2.484] | 6.10 |
| T1 | 1.647 [0.994, 2.301] | 4.94 |
| T12 | 0.993 [0.408, 1.577] | 3.33 |
| T5 | 0.958 [0.347, 1.568] | 3.07 |
| T4 | 0.880 [0.260, 1.500] | 2.78 |
| T7 | 0.880 [0.260, 1.500] | 2.78 |
| T2 | 0.477 [-0.140, 1.095] | 1.51 |
| T6 | 0.225 [-0.237, 0.687] | 0.95 |
| T10 | 0.225 [-0.237, 0.687] | 0.95 |
| T9 | 0.022 [-0.411, 0.456] | 0.10 |
| T8 | -0.200 [-0.710, 0.310] | -0.77 |

## Structural variants

| Variant | Scenario | Mean N | Existence | Viability |
|---|---|---:|---:|---:|
| base | full | 17.800 | 1.000 | 0.985 |
| base | attraction | 12.380 | 1.000 | 0.985 |
| base | referral | 0.510 | 0.105 | 0.028 |
| base | both | 0.003 | 0.003 | 0.000 |
| base | gatekeeping | 6.755 | 0.750 | 0.547 |
| gate_flat | full | 15.047 | 0.975 | 0.868 |
| gate_flat | attraction | 6.612 | 0.870 | 0.657 |
| gate_flat | referral | 0.745 | 0.120 | 0.055 |
| gate_flat | both | 0.003 | 0.003 | 0.000 |
| gate_flat | gatekeeping | 1.222 | 0.177 | 0.098 |
| t3_admission | full | 17.800 | 1.000 | 0.985 |
| t3_admission | attraction | 12.380 | 1.000 | 0.985 |
| t3_admission | referral | 0.510 | 0.105 | 0.028 |
| t3_admission | both | 0.003 | 0.003 | 0.000 |
| t3_admission | gatekeeping | 0.000 | 0.000 | 0.000 |
| capacity_all | full | 29.285 | 1.000 | 1.000 |
| capacity_all | attraction | 14.730 | 1.000 | 1.000 |
| capacity_all | referral | 2.002 | 0.258 | 0.122 |
| capacity_all | both | 0.003 | 0.003 | 0.000 |
| capacity_all | gatekeeping | 16.015 | 0.995 | 0.965 |
| no_saturation | full | 22.008 | 0.998 | 0.990 |
| no_saturation | attraction | 13.037 | 1.000 | 0.995 |
| no_saturation | referral | 1.020 | 0.145 | 0.058 |
| no_saturation | both | 0.003 | 0.003 | 0.000 |
| no_saturation | gatekeeping | 10.810 | 0.855 | 0.670 |

Attraction-minus-referral structural ordering by variant:

- `base`: mean-N difference 11.870; viability difference 0.958; existence difference 0.895.
- `gate_flat`: mean-N difference 5.867; viability difference 0.602; existence difference 0.750.
- `t3_admission`: mean-N difference 11.870; viability difference 0.958; existence difference 0.895.
- `capacity_all`: mean-N difference 12.728; viability difference 0.877; existence difference 0.742.
- `no_saturation`: mean-N difference 12.018; viability difference 0.938; existence difference 0.855.

## Global, tiered, and randomized-matrix screens

Positive strict counts below mean the pure-attraction-loss condition ends larger or
more viable than referral loss. Ties are reported separately.

| Design | Draws | N strict/tie/reversal | Viability strict/tie/reversal | Existence strict/tie/reversal | Full viable in all 3 seeds |
|---|---:|---:|---:|---:|---:|
| g125 | 334 | 301/0/33 | 323/10/1 | 318/16/0 | 302/334 |
| g250 | 334 | 251/1/82 | 269/64/1 | 262/72/0 | 291/334 |
| g500 | 334 | 213/17/104 | 201/117/16 | 215/117/2 | 256/334 |
| tiered | 1000 | 783/10/207 | 818/165/17 | 821/177/2 | 833/1000 |
| randmat | 1000 | 1000/0/0 | 1000/0/0 | 999/1/0 | 784/1000 |

## Multi-level one-at-a-time screen

Across 944 points, the attraction-minus-referral final-N ordering is strict/tie/reversal 931/2/11. Endpoint-viability ordering is 934/10/0.
Existence ordering is 933/11/0.
Full adherence is viable in all three seeds at 893 of 944 points and exists in all three at 936 points.

## Decay-ordering confirmation

The multi-level screen's `delta0` membership reversals, re-estimated at 400 seeds shared by
all twenty-one cells, so every contrast is paired by common random numbers. Full adherence
otherwise, 1,560 weeks, dt 0.5. Attraction is the pure T11 attraction path with governance
held at one; referral is `lam_exog = 0`. The default rate and 25, 50 and 75 per cent lower
come from `decay_ordering.json`; 10, 15 and 20 per cent lower, which locate the membership
reversal, from `decay_reversal.json`, whose design differs only in its level list.

| delta0 change | Condition | Mean N [95% half-width] | Existence | Viability | Closure |
|---:|---|---:|---:|---:|---:|
| 0% | full | 17.800 [0.883] | 1.000 | 0.985 | 0.000 |
| 0% | attraction | 12.380 [0.342] | 1.000 | 0.985 | 0.000 |
| 0% | referral | 0.510 [0.229] | 0.105 | 0.028 | 0.895 |
| -10% | full | 29.067 [1.531] | 1.000 | 0.993 | 0.000 |
| -10% | attraction | 13.425 [0.356] | 1.000 | 0.993 | 0.000 |
| -10% | referral | 2.502 [0.655] | 0.273 | 0.135 | 0.728 |
| -15% | full | 39.042 [1.593] | 1.000 | 1.000 | 0.000 |
| -15% | attraction | 13.930 [0.358] | 1.000 | 0.995 | 0.000 |
| -15% | referral | 7.577 [1.307] | 0.438 | 0.325 | 0.562 |
| -20% | full | 47.470 [1.367] | 1.000 | 1.000 | 0.000 |
| -20% | attraction | 14.457 [0.367] | 1.000 | 1.000 | 0.000 |
| -20% | referral | 17.247 [1.992] | 0.693 | 0.545 | 0.307 |
| -25% | full | 54.188 [0.835] | 1.000 | 1.000 | 0.000 |
| -25% | attraction | 15.008 [0.371] | 1.000 | 1.000 | 0.000 |
| -25% | referral | 29.977 [2.247] | 0.840 | 0.755 | 0.160 |
| -50% | full | 59.460 [0.097] | 1.000 | 1.000 | 0.000 |
| -50% | attraction | 18.192 [0.398] | 1.000 | 1.000 | 0.000 |
| -50% | referral | 59.212 [0.124] | 1.000 | 1.000 | 0.000 |
| -75% | full | 59.810 [0.054] | 1.000 | 1.000 | 0.000 |
| -75% | attraction | 20.593 [0.429] | 1.000 | 1.000 | 0.000 |
| -75% | referral | 59.708 [0.067] | 1.000 | 1.000 | 0.000 |

Attraction-minus-referral paired differences:

| delta0 change | Outcome | Mean [95% paired interval] | Strict | Tied | Reversed |
|---:|---|---:|---:|---:|---:|
| 0% | N | 11.870 [11.466, 12.274] | 394 | 1 | 5 |
| 0% | viable | 0.958 [0.937, 0.978] | 384 | 15 | 1 |
| 0% | exists | 0.895 [0.865, 0.925] | 358 | 42 | 0 |
| -10% | N | 10.922 [10.181, 11.664] | 373 | 0 | 27 |
| -10% | viable | 0.858 [0.823, 0.892] | 343 | 57 | 0 |
| -10% | exists | 0.728 [0.684, 0.771] | 291 | 109 | 0 |
| -15% | N | 6.353 [5.029, 7.676] | 317 | 3 | 80 |
| -15% | viable | 0.670 [0.624, 0.716] | 268 | 132 | 0 |
| -15% | exists | 0.562 [0.514, 0.611] | 225 | 175 | 0 |
| -20% | N | -2.790 [-4.768, -0.812] | 233 | 10 | 157 |
| -20% | viable | 0.455 [0.406, 0.504] | 182 | 218 | 0 |
| -20% | exists | 0.307 [0.262, 0.353] | 123 | 277 | 0 |
| -25% | N | -14.970 [-17.214, -12.726] | 143 | 3 | 254 |
| -25% | viable | 0.245 [0.203, 0.287] | 98 | 302 | 0 |
| -25% | exists | 0.160 [0.124, 0.196] | 64 | 336 | 0 |
| -50% | N | -41.020 [-41.416, -40.624] | 0 | 0 | 400 |
| -50% | viable | 0.000 [0.000, 0.000] | 0 | 400 | 0 |
| -50% | exists | 0.000 [0.000, 0.000] | 0 | 400 | 0 |
| -75% | N | -39.115 [-39.551, -38.679] | 0 | 0 | 400 |
| -75% | viable | 0.000 [0.000, 0.000] | 0 | 400 | 0 |
| -75% | exists | 0.000 [0.000, 0.000] | 0 | 400 | 0 |

## Morris screen

Twenty trajectories; values are output change per unit proportional parameter change.
High sigma indicates interaction or nonlinearity and does not separate them.

| Membership rank | Factor | mu | mu* | sigma |
|---:|---|---:|---:|---:|
| 1 | scalar:p_gate | -51.780 | 52.440 | 57.611 |
| 2 | scalar:delta0 | -51.210 | 51.210 | 54.039 |
| 3 | scalar:churn | -33.000 | 33.480 | 32.726 |
| 4 | scalar:drop_k | 24.300 | 24.300 | 23.068 |
| 5 | scalar:lam_exog | 22.680 | 23.460 | 24.579 |
| 6 | scalar:het_sd | 18.600 | 18.900 | 17.323 |
| 7 | a:5 | 15.960 | 18.540 | 25.250 |
| 8 | a:11 | 8.190 | 15.870 | 25.005 |
| 9 | scalar:lam0 | 12.000 | 14.340 | 19.472 |
| 10 | a:6 | 13.020 | 14.040 | 17.814 |
| 11 | a:9 | 10.380 | 13.320 | 19.406 |
| 12 | scalar:drop0 | -12.540 | 12.660 | 14.938 |
| 13 | a:0 | 4.920 | 12.420 | 17.268 |
| 14 | a:1 | 10.470 | 12.390 | 12.687 |
| 15 | a:8 | 8.670 | 11.310 | 16.128 |

## Sobol decomposition

The decomposition is conditional on the eight listed Morris leaders and the stated
plus-or-minus 25 per cent ranges. First-order and total-order intervals are bootstrap
intervals over base rows.

| Factor | Membership S1 [95%] | Membership ST [95%] | Practice S1 [95%] | Practice ST [95%] |
|---|---:|---:|---:|---:|
| p_gate | 0.404 [0.288, 0.525] | 0.576 [0.510, 0.643] | 0.535 [0.357, 0.710] | 0.573 [0.519, 0.629] |
| delta0 | 0.238 [0.156, 0.327] | 0.373 [0.320, 0.428] | 0.421 [0.285, 0.569] | 0.417 [0.373, 0.463] |
| churn | 0.023 [-0.020, 0.068] | 0.132 [0.111, 0.155] | 0.030 [-0.030, 0.094] | 0.094 [0.082, 0.107] |
| drop_k | 0.032 [-0.014, 0.079] | 0.171 [0.145, 0.199] | 0.001 [-0.066, 0.071] | 0.103 [0.090, 0.116] |
| lam_exog | -0.015 [-0.048, 0.018] | 0.058 [0.049, 0.068] | 0.008 [-0.055, 0.069] | 0.079 [0.070, 0.090] |
| het_sd | 0.022 [-0.015, 0.061] | 0.079 [0.064, 0.095] | 0.092 [0.019, 0.166] | 0.108 [0.095, 0.121] |
| a:5 | -0.016 [-0.037, 0.004] | 0.029 [0.024, 0.034] | -0.016 [-0.060, 0.025] | 0.041 [0.035, 0.048] |
| a:11 | 0.005 [-0.018, 0.029] | 0.038 [0.031, 0.046] | 0.004 [-0.041, 0.046] | 0.049 [0.042, 0.057] |

Noise-replicate total-order diagnostics: [0.04291410620627524, 0.07283254960551121].
