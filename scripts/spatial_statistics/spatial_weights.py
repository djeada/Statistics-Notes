"""Construct spatial weights and compute spatial lags."""

from __future__ import annotations

import numpy as np
from scipy.spatial.distance import cdist


def knn_weights(coordinates, k=4, symmetric=True):
    """Binary k-nearest-neighbor weights with zero diagonal."""
    coordinates = np.asarray(coordinates, dtype=float)
    n = len(coordinates)
    if not 1 <= k < n:
        raise ValueError("k must satisfy 1 <= k < number of observations")

    distances = cdist(coordinates, coordinates)
    np.fill_diagonal(distances, np.inf)

    weights = np.zeros((n, n), dtype=float)
    neighbors = np.argpartition(distances, kth=k - 1, axis=1)[:, :k]
    rows = np.repeat(np.arange(n), k)
    weights[rows, neighbors.ravel()] = 1.0

    if symmetric:
        weights = np.maximum(weights, weights.T)
    return weights


def distance_band_weights(coordinates, threshold):
    """Binary weights joining observations no farther apart than threshold."""
    coordinates = np.asarray(coordinates, dtype=float)
    distances = cdist(coordinates, coordinates)
    weights = ((distances > 0.0) & (distances <= threshold)).astype(float)
    return weights


def row_standardize(weights):
    """Scale each non-island row to sum to one."""
    weights = np.asarray(weights, dtype=float)
    row_sums = weights.sum(axis=1)
    standardized = np.zeros_like(weights)
    non_islands = row_sums > 0
    standardized[non_islands] = weights[non_islands] / row_sums[non_islands, None]
    return standardized


def spatial_lag(weights, values):
    """Weighted average/sum of neighboring values according to weights."""
    return np.asarray(weights, dtype=float) @ np.asarray(values, dtype=float)


def main():
    xx, yy = np.meshgrid(np.arange(5), np.arange(5))
    coordinates = np.column_stack([xx.ravel(), yy.ravel()])
    values = coordinates[:, 0] + 0.5 * coordinates[:, 1]

    binary = knn_weights(coordinates, k=4)
    weights = row_standardize(binary)
    lag = spatial_lag(weights, values)

    print("First five binary neighbor counts:", binary.sum(axis=1)[:5].astype(int))
    print("First five row sums after standardization:", weights.sum(axis=1)[:5])
    print("First five values:", values[:5])
    print("First five spatial lags:", np.round(lag[:5], 3))


if __name__ == "__main__":
    main()
