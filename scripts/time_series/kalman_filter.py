"""Minimal scalar Kalman filter for a local-level model."""

import numpy as np

rng = np.random.default_rng(21)
n = 120
process_variance = 0.08
measurement_variance = 0.8

state = np.zeros(n)
for t in range(1, n):
    state[t] = state[t - 1] + rng.normal(scale=np.sqrt(process_variance))
observation = state + rng.normal(scale=np.sqrt(measurement_variance), size=n)

filtered = np.zeros(n)
a = 0.0
P = 1.0

for t, y_t in enumerate(observation):
    # Prediction
    a_pred = a
    P_pred = P + process_variance

    # Update
    innovation = y_t - a_pred
    innovation_variance = P_pred + measurement_variance
    kalman_gain = P_pred / innovation_variance
    a = a_pred + kalman_gain * innovation
    P = (1.0 - kalman_gain) * P_pred
    filtered[t] = a

raw_rmse = np.sqrt(np.mean((observation - state) ** 2))
filtered_rmse = np.sqrt(np.mean((filtered - state) ** 2))
print(f"Observation RMSE: {raw_rmse:.3f}")
print(f"Filtered RMSE:    {filtered_rmse:.3f}")
