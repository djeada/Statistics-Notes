"""Global and local Moran statistics with permutation inference."""

from __future__ import annotations

import numpy as np
from scipy.spatial.distance import cdist

from spatial_weights import knn_weights, row_standardize


def moran_i(values, weights):
    """Global Moran's I for a general spatial weight matrix."""
    values = np.asarray(values, dtype=float)
    weights = np.asarray(weights, dtype=float)
    z = values - values.mean()
    s0 = weights.sum()
    if s0 <= 0:
        raise ValueError("weights must contain at least one positive connection")
    return len(values) / s0 * (z @ weights @ z) / (z @ z)


def local_moran(values, weights):
    """Local Moran statistic using m2 = sum(z_i^2)/n."""
    values = np.asarray(values, dtype=float)
    weights = np.asarray(weights, dtype=float)
    z = values - values.mean()
    m2 = np.mean(z**2)
    return z * (weights @ z) / m2


def permutation_test(values, weights, permutations=999, seed=42):
    """Two-sided randomization test around E[I] = -1/(n-1)."""
    rng = np.random.default_rng(seed)
    observed = moran_i(values, weights)
    expected = -1.0 / (len(values) - 1)

    simulated = np.empty(permutations)
    for b in range(permutations):
        simulated[b] = moran_i(rng.permutation(values), weights)

    observed_distance = abs(observed - expected)
    simulated_distance = np.abs(simulated - expected)
    p_value = (1 + np.count_nonzero(simulated_distance >= observed_distance)) / (
        permutations + 1
    )
    return observed, expected, p_value, simulated


def simulate_spatial_field(coordinates, correlation_range=0.22, seed=7):
    """Gaussian field with exponential covariance for demonstration."""
    rng = np.random.default_rng(seed)
    distances = cdist(coordinates, coordinates)
    covariance = np.exp(-distances / correlation_range) + 1e-10 * np.eye(len(coordinates))
    return rng.multivariate_normal(np.zeros(len(coordinates)), covariance)


def main():
    xx, yy = np.meshgrid(np.linspace(0, 1, 12), np.linspace(0, 1, 12))
    coordinates = np.column_stack([xx.ravel(), yy.ravel()])
    values = simulate_spatial_field(coordinates)

    weights = row_standardize(knn_weights(coordinates, k=4))
    observed, expected, p_value, _ = permutation_test(values, weights)

    local = local_moran(values, weights)
    z = values - values.mean()
    lag = weights @ z
    quadrants = {
        "high-high": int(np.sum((z > 0) & (lag > 0))),
        "low-low": int(np.sum((z < 0) & (lag < 0))),
        "high-low": int(np.sum((z > 0) & (lag < 0))),
        "low-high": int(np.sum((z < 0) & (lag > 0))),
    }

    print(f"Moran's I:            {observed:.3f}")
    print(f"Randomization E[I]:   {expected:.3f}")
    print(f"Permutation p-value:  {p_value:.4f}")
    print("Moran-scatterplot quadrants:", quadrants)
    print("Largest |local I| values:", np.round(np.sort(np.abs(local))[-5:], 3))


if __name__ == "__main__":
    main()
