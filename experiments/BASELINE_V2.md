# Matched no-deletion baseline — v2

## Protocol
Same model constants, seeds 0–19, T=1000, dt=0.01, noise=0.0015. The only intervention removed is the deletion at t=500.

## Result
All 20 baseline runs remained above the preregistered connectivity threshold lambda2 >= 0.01 throughout the post-t=500 evaluation window.

| seed | min_lambda2 |
|---:|---:|
| 0 | 1.4996 |
| 1 | 0.9033 |
| 2 | 1.3126 |
| 3 | 0.6714 |
| 4 | 1.2024 |
| 5 | 1.5859 |
| 6 | 1.4115 |
| 7 | 1.6027 |
| 8 | 1.4044 |
| 9 | 1.4483 |
| 10 | 1.9142 |
| 11 | 1.8744 |
| 12 | 1.6484 |
| 13 | 0.9796 |
| 14 | 0.6258 |
| 15 | 1.1713 |
| 16 | 1.5415 |
| 17 | 1.0815 |
| 18 | 0.8627 |
| 19 | 1.5839 |

## Interpretation
The baseline establishes that the model's connectivity metric is not intrinsically below threshold in these seeds. It does not by itself prove that deletion causes the observed vacancy behavior.

## Status
Control result only. No final scientific conclusion is fixed here.
