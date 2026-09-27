# Diagnostic result — v2

The frozen production protocol was not changed. A diagnostic-only run recorded pre-deletion state and vacancy onset for seeds 0–19.

## Key observation

The failures are heterogeneous.

- Seeds 1, 11, 15, 17 eventually form a sustained vacancy, but only after 120, 120, 190 and 230 post-deletion time units respectively. Because the confirmatory criterion requires 80% of snapshots above threshold, these delayed cases fail.
- Seed 18 never crosses the 0.25 vacancy threshold; maximum observed distance is 0.134.
- Seeds 8, 9, 10, 13, 14, 19 already have a nearest-neighbor distance above 0.25 at deletion. In these cases the deleted position is already spatially separated from the remaining structure, so the diagnostic 'vacancy formation' metric is partly measuring a pre-existing empty region rather than a vacancy created by the intervention.

## Important methodological finding

The original vacancy metric is therefore not sufficient to distinguish:

1. a vacancy created by deletion,
2. a pre-existing hole around the deleted node,
3. delayed separation after deletion.

This is a useful model-design finding. It does not invalidate the production run, but it limits the interpretation of its vacancy metric.

## Seed 18

Seed 18 is the cleanest non-vacancy case among the initially occupied cases:
- nearest-neighbor distance before deletion: 0.004
- distance of deleted node from system center: 0.111
- local weighted degree: 7.629
- pre-deletion lambda2: 2.210
- maximum post-deletion vacancy distance: 0.134

Thus the failure is not explained by an initially isolated deleted node. It is a genuine diagnostic target for the next experiment.

## Next experiment

Keep PREREGISTRATION_V2 frozen. Add a second, independent vacancy definition based on a local empty-region observable that is normalized to the pre-deletion state. Then compare:
- initially occupied vs pre-existing-hole cases;
- immediate vs delayed separation;
- seed 18 against successful seeds with similar local degree/connectivity.

No confirmatory conclusion should be changed from this diagnostic alone.
