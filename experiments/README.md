# Experiments

Each run must record:

- experiment ID
- model version
- parameter hash
- random seed
- initial-state hash
- commit SHA
- runtime
- result code
- primary metrics
- notes on numerical errors

Recommended layout:

experiments/
  runs/
  results/
  figures/
  logs/

Raw data and generated figures must never overwrite previous runs.
