# Failure-mode diagnostic — v2

## Purpose
Inspect the five production failures without changing the frozen confirmatory protocol.

## Failed seeds
1, 11, 15, 17, 18.

All five retained connectivity PASS (post-deletion lambda2 criterion = 1.00). Their failures are exclusively vacancy persistence.

| seed | vacancy fraction | max distance | final distance |
|---:|---:|---:|---:|
| 1 | 0.76 | 0.951 | 0.951 |
| 11 | 0.76 | 1.291 | 1.291 |
| 15 | 0.62 | 1.085 | 1.085 |
| 17 | 0.54 | 0.529 | 0.529 |
| 18 | 0.00 | 0.134 | 0.134 |

## Important distinction
Seeds 1, 11, 15 and 17 eventually produce a persistent displacement above the vacancy threshold, but not for the required 80% of post-deletion snapshots. Seed 18 never reaches the 0.25 threshold.

This means the failure set is not homogeneous:
- 1/11/15/17: delayed or intermittent vacancy formation.
- 18: no observed vacancy formation under the frozen criterion.

## Pre-deletion observations
The deleted node is selected as the node nearest the instantaneous center. Its pre-deletion local connectivity and position vary substantially between seeds. This suggests initial-state dependence is a plausible diagnostic hypothesis, but the current 20 runs are insufficient to establish causality.

## Next diagnostic
Do not change PREREGISTRATION_V2. Run a separate diagnostic sweep that records:
1. pre-deletion local weighted degree of the removed node;
2. nearest-neighbor distance;
3. distance of removed node from system center;
4. pre-deletion lambda2;
5. post-deletion distance trajectory;
6. time to first sustained crossing of 0.25.

The diagnostic experiment must remain separate from confirmatory PASS/FAIL statistics.
