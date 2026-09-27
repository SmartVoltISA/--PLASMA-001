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

## Provenance
The earlier exploratory run is not counted as confirmatory evidence. It is retained separately in the experiment history.

## Next
1. Run the separate diagnostic sweep for pre-deletion state variables and vacancy onset time.
2. Compare successful and failed seeds without changing PREREGISTRATION_V2.
3. Identify whether a reproducible regime boundary exists.
4. Only after diagnostics and controls, issue the final RESULT/DECISION.
