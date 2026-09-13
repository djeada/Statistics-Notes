"""Empirical variograms, model fitting, and ordinary kriging from first principles."""

from __future__ import annotations

import numpy as np
from scipy.optimize import curve_fit
from scipy.spatial.distance import cdist, pdist


def exponential_semivariogram(h, nugget, partial_sill, range_parameter):
    """Exponential semivariogram; gamma(0)=0, nugget applies at positive lags."""
    h = np.asarray(h, dtype=float)
    gamma = nugget + partial_sill * (1.0 - np.exp(-h / range_parameter))
    return np.where(h == 0.0, 0.0, gamma)


def empirical_variogram(coordinates, values, n_bins=12, max_distance=None):
    """Classical method-of-moments empirical semivariogram."""
    coordinates = np.asarray(coordinates, dtype=float)
    values = np.asarray(values, dtype=float)

    distances = pdist(coordinates)
    semivariances = 0.5 * pdist(values[:, None], metric="sqeuclidean")

    if max_distance is None:
        max_distance = np.quantile(distances, 0.65)

    edges = np.linspace(0.0, max_distance, n_bins + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    gamma = np.full(n_bins, np.nan)
    counts = np.zeros(n_bins, dtype=int)

    for b in range(n_bins):
        mask = (distances >= edges[b]) & (distances < edges[b + 1])
        counts[b] = mask.sum()
        if counts[b] > 0:
            gamma[b] = semivariances[mask].mean()

    return centers, gamma, counts


def fit_exponential_variogram(centers, gamma, counts):
    """Weighted nonlinear least squares fit to binned semivariances."""
    valid = np.isfinite(gamma) & (counts > 0)
    x = centers[valid]
    y = gamma[valid]
    weights = np.sqrt(counts[valid])

    variance = max(float(np.nanmax(y)), 1e-6)
    p0 = (0.05 * variance, 0.95 * variance, max(np.median(x), 1e-3))
    lower = (0.0, 1e-8, 1e-6)
    upper = (3 * variance, 5 * variance, max(10 * np.max(x), 1.0))

    params, _ = curve_fit(
        exponential_semivariogram,
        x,
        y,
        p0=p0,
        bounds=(lower, upper),
        sigma=1.0 / weights,
        absolute_sigma=False,
        maxfev=20_000,
    )
    return params


def ordinary_kriging(train_coordinates, train_values, targets, variogram_params):
    """Ordinary kriging using the semivariogram linear system."""
    train_coordinates = np.asarray(train_coordinates, dtype=float)
    train_values = np.asarray(train_values, dtype=float)
    targets = np.atleast_2d(np.asarray(targets, dtype=float))

    nugget, partial_sill, range_parameter = variogram_params
    train_distances = cdist(train_coordinates, train_coordinates)
    gamma_matrix = exponential_semivariogram(
        train_distances, nugget, partial_sill, range_parameter
    )

    n = len(train_coordinates)
    system = np.empty((n + 1, n + 1))
    system[:n, :n] = gamma_matrix
    system[:n, n] = 1.0
    system[n, :n] = 1.0
    system[n, n] = 0.0

    predictions = np.empty(len(targets))
    variances = np.empty(len(targets))

    for t, target in enumerate(targets):
        distances = cdist(train_coordinates, target[None, :]).ravel()
        gamma_target = exponential_semivariogram(
            distances, nugget, partial_sill, range_parameter
        )
        rhs = np.concatenate([gamma_target, [1.0]])
        solution = np.linalg.solve(system, rhs)
        weights = solution[:n]
        lagrange = solution[n]

        predictions[t] = weights @ train_values
        variances[t] = max(weights @ gamma_target + lagrange, 0.0)

    return predictions, variances


def simulate_field(n=70, seed=9):
    """Stationary Gaussian random field with a small independent nugget component."""
    rng = np.random.default_rng(seed)
    coordinates = rng.uniform(0.0, 1.0, size=(n, 2))
    distances = cdist(coordinates, coordinates)

    process_variance = 0.8
    correlation_range = 0.18
    nugget_variance = 0.06

    covariance = process_variance * np.exp(-distances / correlation_range)
    latent = rng.multivariate_normal(
        np.full(n, 6.5), covariance + 1e-10 * np.eye(n)
    )
    observed = latent + rng.normal(scale=np.sqrt(nugget_variance), size=n)
    return coordinates, observed


def leave_one_out(coordinates, values, params):
    predictions = np.empty(len(values))
    variances = np.empty(len(values))

    for i in range(len(values)):
        keep = np.arange(len(values)) != i
        pred, var = ordinary_kriging(
            coordinates[keep], values[keep], coordinates[i], params
        )
        predictions[i] = pred[0]
        variances[i] = var[0]
    return predictions, variances


def main():
    coordinates, values = simulate_field()
    centers, gamma, counts = empirical_variogram(coordinates, values)
    params = fit_exponential_variogram(centers, gamma, counts)

    predictions, variances = leave_one_out(coordinates, values, params)
    errors = values - predictions
    rmse = np.sqrt(np.mean(errors**2))
    mean_baseline_rmse = np.sqrt(np.mean((values - values.mean()) ** 2))
    standardized = errors / np.sqrt(np.maximum(variances, 1e-12))

    nugget, partial_sill, range_parameter = params
    print(f"Fitted nugget:          {nugget:.3f}")
    print(f"Fitted partial sill:    {partial_sill:.3f}")
    print(f"Fitted range parameter: {range_parameter:.3f}")
    print(f"LOO kriging RMSE:       {rmse:.3f}")
    print(f"Mean-baseline RMSE:     {mean_baseline_rmse:.3f}")
    print(f"Mean standardized err:  {standardized.mean():.3f}")
    print(f"SD standardized err:    {standardized.std(ddof=1):.3f}")


if __name__ == "__main__":
    main()
