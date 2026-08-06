# Corrected Release-Gate Results

This is the human-readable view of research/release_gate_results.json. It is generated
from the cache, not copied by hand.

## Provenance and design

- Model SHA-256: c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952
- Analysis SHA-256: 2b2918ff755c5f70e8eecb484ca67226d633405053b9c67a2028a0524400133f
- Jobs: 3200 of 3200
- Seeds: 0-399, paired across conditions
- Horizon: 1560 weeks; dt=0.5 week; 3,120 integration steps
- Endpoint existence is N>0. Endpoint viability is N>5. N=0 is permanent closure.
- Crossing N<=5 is not absorbing; recovery above 5 is recorded.
- Continuous intervals are normal 95% intervals for paired or unpaired means as labelled.
- Binary condition intervals are Wilson intervals; binary contrasts retain pairing and report exact McNemar p-values in the cache.

## Condition outcomes

| Condition | Final N, mean [95% CI] | P(N>0) [95% CI] | P(N>5) [95% CI] | Ever crossed N<=5 | Recovered after crossing | P(N=0) |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | 17.800 [16.917, 18.683] | 100.0% [99.0%, 100.0%] | 98.5% [96.8%, 99.3%] | 91/400 | 91/91 | 0.0% [0.0%, 1.0%] |
| T3 friction loss only | 14.838 [13.910, 15.765] | 99.2% [97.8%, 99.7%] | 94.0% [91.2%, 95.9%] | 184/400 | 181/184 | 0.8% [0.3%, 2.2%] |
| T3 governance loss only | 11.773 [11.149, 12.396] | 98.0% [96.1%, 99.0%] | 91.2% [88.1%, 93.6%] | 241/400 | 237/241 | 2.0% [1.0%, 3.9%] |
| T3 combined loss | 6.755 [6.170, 7.340] | 75.0% [70.5%, 79.0%] | 54.8% [49.9%, 59.6%] | 347/400 | 340/347 | 25.0% [21.0%, 29.5%] |
| T11 attraction loss only | 12.380 [12.038, 12.722] | 100.0% [99.0%, 100.0%] | 98.5% [96.8%, 99.3%] | 206/400 | 205/206 | 0.0% [0.0%, 1.0%] |
| T11 governance loss only | 15.515 [14.809, 16.221] | 100.0% [99.0%, 100.0%] | 98.0% [96.1%, 99.0%] | 123/400 | 122/123 | 0.0% [0.0%, 1.0%] |
| T11 combined loss | 11.920 [11.584, 12.256] | 100.0% [99.0%, 100.0%] | 98.5% [96.8%, 99.3%] | 247/400 | 247/247 | 0.0% [0.0%, 1.0%] |
| Recipient capacity forced to one | 18.828 [17.782, 19.873] | 100.0% [99.0%, 100.0%] | 98.8% [97.1%, 99.5%] | 65/400 | 65/65 | 0.0% [0.0%, 1.0%] |

A crossing followed by recovery does not imply the run remained viable thereafter.
Endpoint viability and first passage answer different questions.

## Paired mechanism contrasts

Positive final-N contrasts below mean the intact or unconstrained first condition ends larger.

| Contrast | Paired final-N difference [95% CI] | Paired viability risk difference [95% CI] |
|---|---:|---:|
| T3 friction: baseline minus loss | 2.962 [1.848, 4.077] | 0.045 [0.020, 0.070] |
| T3 governance: baseline minus loss | 6.027 [5.043, 7.012] | 0.072 [0.042, 0.103] |
| T3 combined: baseline minus loss | 11.045 [10.030, 12.060] | 0.438 [0.388, 0.487] |
| T11 attraction: baseline minus loss | 5.420 [4.515, 6.325] | 0.000 [-0.017, 0.017] |
| T11 governance: baseline minus loss | 2.285 [1.214, 3.356] | 0.005 [-0.011, 0.021] |
| T11 combined: baseline minus loss | 5.880 [4.972, 6.788] | 0.000 [-0.017, 0.017] |
| Recipient unconstrained minus baseline | 1.028 [-0.259, 2.314] | 0.003 [-0.010, 0.015] |

## Factorial interactions

The interaction is baseline - path-loss - governance-loss + combined-loss.

| Tradition | Outcome | Path loss with governance intact [95% CI] | Governance loss with other path intact [95% CI] | Interaction [95% CI] |
|---|---|---:|---:|---:|
| T3 | N | 2.962 [1.848, 4.077] | 6.027 [5.043, 7.012] | -2.055 [-3.414, -0.696] |
| T3 | endpoint_viable | 0.045 [0.020, 0.070] | 0.072 [0.042, 0.103] | -0.320 [-0.379, -0.261] |
| T11 | N | 5.420 [4.515, 6.325] | 2.285 [1.214, 3.356] | 1.825 [0.755, 2.895] |
| T11 | endpoint_viable | 0.000 [-0.017, 0.017] | 0.005 [-0.011, 0.021] | 0.005 [-0.011, 0.021] |

The two paths for each Tradition are reported separately and jointly; the interaction
term shows why their contrasts must not be added. The recipient intervention changes only
recipient capacity and gives a paired final-N contrast of 1.028 
[-0.259, 2.314]. That interval includes zero, so the clean recipient-capacity ablation is unresolved.

## Viability-threshold sensitivity

| Condition | P(N>0) | P(N>1) | P(N>3) | P(N>5) | P(N>10) |
|---|---:|---:|---:|---:|---:|
| Baseline | 100.0% | 100.0% | 100.0% | 98.5% | 82.2% |
| T3 combined loss | 75.0% | 75.0% | 69.2% | 54.8% | 23.0% |
| T11 attraction loss only | 100.0% | 100.0% | 100.0% | 98.5% | 68.0% |
| T11 combined loss | 100.0% | 100.0% | 100.0% | 98.5% | 61.5% |

## Semantic overlap versus executable linear coupling

B = S GOV^T is the raw author-coded semantic overlap. C = Snorm GOVW^T is the
no-capacity linear map from effective adherence to Step resource bundles. Neither is
the full state-update map or a trajectory effect.

| Step | Raw B maximizing Tradition set | Raw own-index competition rank | C maximizing Tradition set | C own-index competition rank |
|---:|---:|---:|---:|---:|
| 1 | [3] | 2 | [3] | 2 |
| 2 | [11] | 7 | [11] | 5 |
| 3 | [2] | 7 | [2] | 7 |
| 4 | [1, 2] | 8 | [1] | 8 |
| 5 | [12] | 5 | [12] | 5 |
| 6 | [1] | 7 | [1] | 7 |
| 7 | [1] | 7 | [1] | 7 |
| 8 | [2] | 4 | [2] | 5 |
| 9 | [2] | 8 | [2] | 8 |
| 10 | [1] | 8 | [1] | 8 |
| 11 | [1] | 4 | [1] | 4 |
| 12 | [5] | 6 | [1] | 6 |

Raw loads: T1=6.5200, T2=3.8900, T3=2.6900, T4=0.0000, T5=3.8800, T6=0.0000, T7=0.0000, T8=1.1100, T9=0.0000, T10=0.0000, T11=2.6900, T12=2.6200.

Linear executable loads: T1=3.9291, T2=2.9699, T3=0.6969, T4=0.0000, T5=1.7608, T6=0.0000, T7=0.0000, T8=0.5505, T9=0.0000, T10=0.0000, T11=1.0401, T12=1.0528.

Step 4 has a raw T1/T2 tie. Competition ranks preserve exact ties and structural zeros.

## Heterogeneity correction

Capability is drawn as exp(N(-sigma^2/2, sigma)), so its arithmetic expectation is one.
Changing het_sd now changes dispersion without mechanically changing mean capability.
