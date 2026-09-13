"""Bias, variance, MSE, method of moments, and maximum-likelihood estimation."""

import numpy as np

rng = np.random.default_rng(123)
true_rate = 0.4
sample_size = 80
replications = 10_000

samples = rng.exponential(scale=1 / true_rate, size=(replications, sample_size))
rate_estimates = 1.0 / samples.mean(axis=1)

bias = rate_estimates.mean() - true_rate
variance = rate_estimates.var(ddof=1)
mse = np.mean((rate_estimates - true_rate) ** 2)

one_sample = samples[0]
mom_estimate = 1.0 / one_sample.mean()
mle_estimate = 1.0 / one_sample.mean()

print(f"True rate: {true_rate:.3f}")
print(f"One-sample method-of-moments estimate: {mom_estimate:.3f}")
print(f"One-sample maximum-likelihood estimate: {mle_estimate:.3f}")
print(f"Monte Carlo bias: {bias:.4f}")
print(f"Monte Carlo variance: {variance:.4f}")
print(f"Monte Carlo MSE: {mse:.4f}")
print(f"bias^2 + variance: {bias**2 + variance:.4f}")
