# Model Specification

## State

Each node i has position x_i in R² and a weighted relational state W_ij >= 0.

## Interaction

A local interaction kernel K(d_ij) determines the instantaneous coupling from pair distance d_ij. The exact kernel and all numerical constants must be frozen in the first executable implementation before production runs.

## Link adaptation

W_ij is updated from interaction/co-activation and decays when unsupported. Updates are continuous, not binary.

## Position dynamics

Node motion is driven by the weighted local interaction field, confinement and bounded stochastic noise.

## Structural observables

The implementation must expose:
- node coordinates x_i(t);
- W_ij(t);
- degree/strength distribution;
- connected components;
- pair-distance distribution;
- order parameter;
- vacancy indicator;
- displacement field.

## Anti-prediction constraint

The implementation must not contain a rule whose explicit purpose is to create a vacancy, chain, ring, spiral or any other target morphology.

## Required controls

A conventional distance-based interaction model with fixed/non-adaptive coupling should be implemented as a control where practical. The Ω model must not be declared successful merely because it produces a visually similar image.

## Numerical requirements

- deterministic replay from a recorded seed;
- bounded timestep;
- explicit parameter file;
- no hidden adaptive parameters;
- save snapshots and summary metrics;
- detect numerical divergence separately from scientific FAIL.
