"""Monte Carlo view of sampling distributions and standard errors."""

import numpy as np

rng = np.random.default_rng(42)
population_mean = 2.0
population_sd = 2.0
replications = 20_000

for n in (5, 30, 100):
    samples = rng.exponential(scale=population_mean, size=(replications, n))
    sample_means = samples.mean(axis=1)

    empirical_mean = sample_means.mean()
    empirical_se = sample_means.std(ddof=1)
    theoretical_se = population_sd / np.sqrt(n)

    print(
        f"n={n:3d}  "
        f"E[xbar]≈{empirical_mean:.3f}  "
        f"empirical SE={empirical_se:.3f}  "
        f"theoretical SE={theoretical_se:.3f}"
    )
