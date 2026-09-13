"""Poisson and clustered point processes with nearest-neighbor and Ripley K summaries."""

from __future__ import annotations

import numpy as np
from scipy.spatial.distance import cdist


def window_area(bounds):
    xmin, xmax, ymin, ymax = bounds
    return (xmax - xmin) * (ymax - ymin)


def homogeneous_poisson_process(intensity, bounds, rng):
    """Homogeneous Poisson point process in a rectangular window."""
    xmin, xmax, ymin, ymax = bounds
    n = rng.poisson(intensity * window_area(bounds))
    x = rng.uniform(xmin, xmax, n)
    y = rng.uniform(ymin, ymax, n)
    return np.column_stack([x, y])


def thomas_cluster_process(parent_intensity, mean_offspring, cluster_sd, bounds, rng):
    """Simple Thomas cluster process, simulated with an expanded parent window."""
    xmin, xmax, ymin, ymax = bounds
    margin = 4.0 * cluster_sd
    expanded = (xmin - margin, xmax + margin, ymin - margin, ymax + margin)

    parents = homogeneous_poisson_process(parent_intensity, expanded, rng)
    offspring = []
    for parent in parents:
        n_children = rng.poisson(mean_offspring)
        if n_children:
            offspring.append(
                parent + rng.normal(scale=cluster_sd, size=(n_children, 2))
            )

    if not offspring:
        return np.empty((0, 2))

    points = np.vstack(offspring)
    inside = (
        (points[:, 0] >= xmin)
        & (points[:, 0] <= xmax)
        & (points[:, 1] >= ymin)
        & (points[:, 1] <= ymax)
    )
    return points[inside]


def mean_nearest_neighbor_distance(points):
    distances = cdist(points, points)
    np.fill_diagonal(distances, np.inf)
    return np.min(distances, axis=1).mean()


def distance_to_boundary(points, bounds):
    xmin, xmax, ymin, ymax = bounds
    return np.min(
        np.column_stack(
            [
                points[:, 0] - xmin,
                xmax - points[:, 0],
                points[:, 1] - ymin,
                ymax - points[:, 1],
            ]
        ),
        axis=1,
    )


def ripley_k_border(points, radii, bounds):
    """Border-corrected K estimate for a rectangular window."""
    points = np.asarray(points, dtype=float)
    radii = np.asarray(radii, dtype=float)
    n = len(points)
    area = window_area(bounds)
    intensity_hat = n / area

    pair_distances = cdist(points, points)
    np.fill_diagonal(pair_distances, np.inf)
    boundary = distance_to_boundary(points, bounds)

    estimates = np.full(len(radii), np.nan)
    for idx, radius in enumerate(radii):
        eligible = boundary >= radius
        m = eligible.sum()
        if m == 0:
            continue
        neighbor_count = np.sum(pair_distances[eligible] <= radius)
        estimates[idx] = neighbor_count / (intensity_hat * m)
    return estimates


def csr_envelope(n, radii, bounds, simulations=199, seed=123):
    """Pointwise Monte Carlo envelope under CSR conditional on the observed count."""
    rng = np.random.default_rng(seed)
    xmin, xmax, ymin, ymax = bounds
    simulated = np.empty((simulations, len(radii)))

    for b in range(simulations):
        points = np.column_stack(
            [
                rng.uniform(xmin, xmax, n),
                rng.uniform(ymin, ymax, n),
            ]
        )
        simulated[b] = ripley_k_border(points, radii, bounds)

    return (
        np.nanquantile(simulated, 0.025, axis=0),
        np.nanquantile(simulated, 0.975, axis=0),
    )


def main():
    rng = np.random.default_rng(17)
    bounds = (0.0, 1.0, 0.0, 1.0)

    csr = homogeneous_poisson_process(intensity=100.0, bounds=bounds, rng=rng)
    clustered = thomas_cluster_process(
        parent_intensity=8.0,
        mean_offspring=12.0,
        cluster_sd=0.035,
        bounds=bounds,
        rng=rng,
    )

    print(f"CSR point count:       {len(csr)}")
    print(f"Clustered point count: {len(clustered)}")
    print(
        f"Mean nearest neighbor (CSR):       {mean_nearest_neighbor_distance(csr):.3f}"
    )
    print(
        f"Mean nearest neighbor (clustered): {mean_nearest_neighbor_distance(clustered):.3f}"
    )

    radii = np.linspace(0.025, 0.18, 8)
    observed_k = ripley_k_border(clustered, radii, bounds)
    lower, upper = csr_envelope(len(clustered), radii, bounds)

    print("\nr      K_cluster   pi*r^2   above_95%_CSR")
    for r, k, hi in zip(radii, observed_k, upper):
        print(f"{r:0.3f}   {k:0.4f}     {np.pi*r*r:0.4f}    {bool(k > hi)}")


if __name__ == "__main__":
    main()
