# Ω-PLASMA-001 — Production Preregistration v2

This version starts a new production run. Earlier exploratory runs are not counted as confirmatory evidence.

## Frozen model
N=25; T=1000; deletion at t=500; dt=0.01; noise=0.0015.
R0=0.70; hard-core threshold=0.25; sigma=0.35.
Adaptive coupling=0.18; decay=0.015; spring=0.22; repulsion=0.45; confinement=0.035.

## Primary hypothesis
After spontaneous formation of a collective connected state, deletion of one internal node can leave a persistent localized vacancy without loss of global connectivity.

## Null
The vacancy disappears before the observation window ends, or the collective state loses global connectivity.

## Fixed PASS rule
For a run to PASS:
- nearest-survivor distance from the deleted node's pre-deletion position must be >= 0.25 for at least 80% of post-deletion snapshots;
- algebraic connectivity lambda2 must be >= 0.01 for at least 80% of post-deletion snapshots.

A single run is PASS only if both conditions pass.

## Repetitions
20 independent seeds: 0–19.

## Controls
Matched no-deletion baseline will be evaluated separately for stability of lambda2.

## Interpretation boundary
A PASS concerns only the synthetic model. It does not demonstrate a physical plasma mechanism, dark matter, gravity, or any astrophysical claim.

## Data discipline
The model, thresholds and seeds are frozen before the production run. Exploratory results are retained but excluded from confirmatory statistics.
