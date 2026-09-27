# Early-response validation — v2 diagnostic

## Scope
Independent seeds 120–319 (200 new runs), frozen v2 simulator and frozen confirmatory PASS/FAIL rule.

This is a diagnostic analysis. It does not modify PREREGISTRATION_V2 and does not introduce a new confirmatory criterion.

## Overall result
- 147/200 runs PASS (73.5%).
- Connectivity criterion: 200/200.
- Dense pre-deletion subset, defined as nearest-neighbor distance < 0.05: 140 runs.
- Dense subset: 87/140 PASS (62.1%).

## Early response
For dense cases, the first 50 post-deletion steps strongly separate eventual PASS from FAIL.

Mean slope of vacancy distance from tau=10 to tau=50:
- PASS: 0.00502
- FAIL: 0.00123

Correlation with final run-level PASS:
- slope 0–10: +0.685
- slope 10–50: +0.751
- slope 0–50: +0.753
- angular resultant: -0.212
- center distance: -0.170
- local weighted degree: +0.006

## Held-out validation
The 200-run diagnostic set was split by seed:
- training/discovery: seeds 120–219
- held-out validation: seeds 220–319

A threshold on slope_10_50 was selected using the training half only:
- threshold = 0.002373

Applied unchanged to the held-out half:
- accuracy: 94.5%
- sensitivity: 95.8%
- specificity: 92.0%
- AUC: 0.981

For comparison on the same held-out dense subset:
- angular resultant alone AUC: 0.596
- center distance alone AUC: 0.405
- early slope AUC: 0.981

## Interpretation
The early post-deletion expansion rate is a substantially stronger diagnostic of the frozen model's eventual PASS/FAIL outcome than the tested static pre-deletion variables.

This supports a dynamical-regime interpretation: after deletion, the key discriminator may be whether the local defect enters a sufficiently strong early expansion regime.

The threshold above is diagnostic only and must not be promoted to a new confirmatory criterion without a separate preregistered experiment.

## Limitations
- The analysis is entirely synthetic.
- PASS/FAIL remains defined by PREREGISTRATION_V2.
- Dense-case filtering is diagnostic, not confirmatory.
- No claim is made about real plasma, dark matter, gravity, or astrophysical systems.
