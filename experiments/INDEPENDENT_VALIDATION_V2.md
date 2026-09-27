# Independent validation — diagnostic map v2

## Purpose
Test whether the diagnostic structure observed in seeds 0–19 repeats on independent seeds without changing the frozen v2 model or the diagnostic zone boundaries.

## Frozen diagnostic zones
The boundaries were fixed before evaluating seeds 20–119:
- radial: center < 1; mid 1–2; outer > 2
- angular resultant: balanced < 0.50; mixed 0.50–0.65; directed > 0.65

These are diagnostic bins only. They are not added to the original confirmatory PASS criterion.

## Independent validation
- Seeds: 20–119
- N = 100
- Frozen v2 simulator parameters unchanged
- Original run-level PASS criterion unchanged

Overall:
- 75/100 PASS = 75%
- 25/100 FAIL

## Zone results

| Radial zone | Direction zone | N | PASS | PASS rate |
|---|---|---:|---:|---:|
| center <1 | balanced <.5 | 2 | 2 | 100% |
| center <1 | mixed .5–.65 | 4 | 3 | 75% |
| center <1 | directed >.65 | 4 | 0 | 0% |
| mid 1–2 | balanced <.5 | 8 | 7 | 87.5% |
| mid 1–2 | mixed .5–.65 | 5 | 4 | 80% |
| mid 1–2 | directed >.65 | 1 | 0 | 0% |
| outer >2 | balanced <.5 | 51 | 43 | 84.3% |
| outer >2 | mixed .5–.65 | 20 | 12 | 60% |
| outer >2 | directed >.65 | 5 | 4 | 80% |

## Comparison with original 0–19 set

The original frozen production set was 15/20 PASS = 75%.
The independent set is also 75/100 PASS.

The broad pass rate therefore repeats exactly, but this alone does not establish a mechanism.

The strongest repeated observation is that highly directed local states in the central region have poor vacancy persistence:
- center <1 and angular resultant >0.65: 0/4 PASS in the independent set.

However, the outer directed region has 4/5 PASS, so angular directionality is not a universal failure condition.

## Interpretation
The independent sweep supports the existence of state dependence, but it does not justify a simple two-variable deterministic boundary. The diagnostic map is therefore retained as a candidate regime description, not as a confirmed mechanism.

## Next
Use a larger independent sample and/or a continuous multivariate analysis, while keeping the confirmatory v2 protocol unchanged.
