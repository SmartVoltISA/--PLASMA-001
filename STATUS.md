# Status

## Current
- Repository initialized.
- Production preregistration v2 frozen.
- Simulator implemented.
- Production run: 20 seeds.
- Reproduction check: committed model reproduces the stored v2 result table.
- Production result: 15/20 run-level PASS; 5/20 FAIL.
- Connectivity criterion passed in all 20 production runs.
- Matched no-deletion baseline: 20/20 remained above lambda2 threshold.

## Failure structure
- Seeds 1, 11, 15, 17 fail only because vacancy persistence is below the 80% criterion.
- Seed 18 does not cross the vacancy threshold.
- No production run was discarded.

## Diagnostic mechanism result
A controlled matched-seed ablation was completed on seeds 120–179 (60 seeds per variant), without changing the confirmatory protocol.

- FULL: 42/60 PASS (70.0%).
- NO_ADAPT: 43/60 (71.7%).
- NO_REPULSION: 45/60 (75.0%).
- NO_ADAPT_NO_REPULSION: 46/60 (76.7%).
- NO_SPRING: 1/60 (1.7%).
- Connectivity remained 60/60 in every ablation variant.

The dominant diagnostic result is that removing the relation-weighted spring almost eliminates the vacancy response while leaving connectivity intact. Removing adaptation or repulsion does not produce the same collapse. This is model-internal mechanism evidence only; it is not an astrophysical claim.

See experiments/MECHANISM_ABLATION_V2.md.

## Provenance
The earlier exploratory run is not counted as confirmatory evidence. It is retained separately in the experiment history.

## Next
1. Freeze the mechanism interpretation as diagnostic, not confirmatory.
2. Consolidate the early-response and mechanism diagnostics.
3. Define the final RESULT/DECISION layer without changing PREREGISTRATION_V2.
