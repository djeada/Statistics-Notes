"""
Geostatistics teaching visualizations
=====================================

This script creates the figures used in `geostatistics.md`.

Dependencies:
    numpy
    matplotlib

Run:
    python scripts/spatial_statistics/geostatistics_visualizations.py

The script intentionally uses simple formulas and explicit intermediate steps
so that students can connect the code to the equations in the notes.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = REPO_ROOT / "assets" / "spatial_statistics" / "geostatistics"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def save_and_close(filename):
    """Save the current figure and close it."""
    path = FIG_DIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"created: {path}")


def figure_01_spatial_samples():
    """Plot the five-point dataset used in the hand calculation."""
    x = np.array([0.0, 1.0, 0.0, 1.0, 2.0])
    y = np.array([0.0, 0.0, 1.0, 1.0, 0.0])
    z = np.array([10.0, 12.0, 11.0, 14.0, 13.0])
    labels = ["A", "B", "C", "D", "E"]

    plt.figure(figsize=(7, 5))
    points = plt.scatter(x, y, c=z, s=220)
    plt.colorbar(points, label="Observed value Z(s)")

    for xi, yi, zi, label in zip(x, y, z, labels):
        plt.annotate(
            f"{label}: {zi:.0f}",
            (xi, yi),
            xytext=(7, 7),
            textcoords="offset points",
        )

    plt.xlabel("x coordinate")
    plt.ylabel("y coordinate")
    plt.title("Sampled locations: values are only known at observed coordinates")
    plt.xlim(-0.35, 2.35)
    plt.ylim(-0.35, 1.35)
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("01_spatial_samples.png")


def figure_02_trend_and_residuals():
    """Show that a spatial trend can look like spatial dependence."""
    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    observed = np.array([10.2, 12.9, 16.1, 19.0, 22.2])

    # The teaching trend is m(x) = 10 + 3x.
    trend = 10.0 + 3.0 * x
    residual = observed - trend

    plt.figure(figsize=(7, 5))
    plt.plot(x, observed, "o-", label="Observed Z(x)")
    plt.plot(x, trend, "--", label="Trend m(x) = 10 + 3x")
    plt.axhline(observed.mean(), linestyle=":", label="Constant-mean assumption")
    plt.xlabel("x coordinate")
    plt.ylabel("Value")
    plt.title("A large-scale trend should not be mistaken for residual dependence")
    plt.legend()
    save_and_close("02_trend_and_residuals.png")

    # Also print residuals to the terminal for teaching.
    print("\nTrend example")
    print("x        =", x)
    print("observed =", observed)
    print("trend    =", trend)
    print("residual =", np.round(residual, 3))


def figure_03_covariance_and_variogram():
    """
    Compare C(h) = 4 exp(-h/10) with gamma(h) = C(0) - C(h).

    Their sum is C(0)=4, so as covariance falls, semivariance rises.
    """
    h = np.linspace(0, 40, 300)
    covariance = 4.0 * np.exp(-h / 10.0)
    semivariogram = 4.0 - covariance

    plt.figure(figsize=(7, 5))
    plt.plot(h, covariance, label=r"$C(h)=4e^{-h/10}$")
    plt.plot(h, semivariogram, label=r"$\gamma(h)=4-C(h)$")
    plt.xlabel("Separation distance h")
    plt.ylabel("Covariance / semivariance")
    plt.title("Under stationarity: falling covariance means rising semivariance")
    plt.legend()
    save_and_close("03_covariance_and_variogram.png")


def pairwise_distances_and_semivariances(coords, values):
    """
    Return every unique pair's distance and pair semivariance.

    For pair i,j:
        distance = ||s_i - s_j||
        pair semivariance = 0.5 * (Z_i - Z_j)^2
    """
    distances = []
    semivariances = []

    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            distance = np.linalg.norm(coords[i] - coords[j])
            semi = 0.5 * (values[i] - values[j]) ** 2
            distances.append(distance)
            semivariances.append(semi)

    return np.asarray(distances), np.asarray(semivariances)


def empirical_variogram(coords, values, bin_edges):
    """
    Calculate a binned empirical variogram.

    For each bin:
        gamma_hat = mean( 0.5 * (Z_i - Z_j)^2 )

    This is algebraically identical to:
        [1 / (2 N(h))] * sum((Z_i - Z_j)^2)
    """
    distances, pair_semivars = pairwise_distances_and_semivariances(coords, values)

    centers = []
    gamma_hat = []
    pair_counts = []

    for lower, upper in zip(bin_edges[:-1], bin_edges[1:]):
        in_bin = (distances >= lower) & (distances < upper)
        count = int(in_bin.sum())

        if count > 0:
            centers.append((lower + upper) / 2.0)
            gamma_hat.append(pair_semivars[in_bin].mean())
            pair_counts.append(count)

    return np.asarray(centers), np.asarray(gamma_hat), np.asarray(pair_counts)


def simulate_spatial_data(seed=7):
    """
    Simulate a small Gaussian spatial field using an exponential covariance.

    Covariance model:
        C(h) = partial_sill * exp(-h / scale)

    An independent nugget term is added to the diagonal of the covariance
    matrix before drawing the random field.
    """
    rng = np.random.default_rng(seed)

    n = 55
    coords = rng.uniform(0.0, 100.0, size=(n, 2))

    partial_sill = 3.5
    scale = 22.0
    nugget = 0.35

    delta = coords[:, None, :] - coords[None, :, :]
    distance_matrix = np.sqrt(np.sum(delta**2, axis=2))

    covariance = partial_sill * np.exp(-distance_matrix / scale)
    covariance = covariance + nugget * np.eye(n)

    # Numerical jitter makes the Cholesky factorization robust to rounding.
    covariance = covariance + 1e-10 * np.eye(n)
    L = np.linalg.cholesky(covariance)
    residual = L @ rng.standard_normal(n)

    # Add a small linear trend so students can experiment with detrending.
    mean = 8.0 + 0.015 * coords[:, 0] - 0.01 * coords[:, 1]
    values = mean + residual

    return coords, values


def figure_04_empirical_variogram():
    """Compute and plot an empirical variogram from simulated spatial data."""
    coords, values = simulate_spatial_data(seed=7)

    # Remove the known teaching trend before calculating the variogram.
    fitted_mean = 8.0 + 0.015 * coords[:, 0] - 0.01 * coords[:, 1]
    residuals = values - fitted_mean

    bin_edges = np.arange(0.0, 75.0, 7.5)
    centers, gamma_hat, counts = empirical_variogram(
        coords, residuals, bin_edges
    )

    plt.figure(figsize=(7, 5))
    plt.plot(centers, gamma_hat, "o-")
    plt.xlabel("Lag distance")
    plt.ylabel(r"Empirical semivariance $\hat{\gamma}(h)$")
    plt.title("Empirical semivariogram: half the average squared pair difference")

    for x, y, count in zip(centers, gamma_hat, counts):
        plt.annotate(
            f"n={count}",
            (x, y),
            xytext=(0, 7),
            textcoords="offset points",
            ha="center",
            fontsize=8,
        )

    save_and_close("04_empirical_variogram.png")

    print("\nEmpirical variogram bins")
    for center, gamma, count in zip(centers, gamma_hat, counts):
        print(
            f"lag center={center:6.2f}, "
            f"gamma_hat={gamma:7.3f}, "
            f"pairs={count:3d}"
        )


def exponential_variogram(h, nugget, partial_sill, scale):
    """Exponential semivariogram with gamma(0)=0 by convention."""
    h = np.asarray(h, dtype=float)
    gamma = nugget + partial_sill * (1.0 - np.exp(-h / scale))
    return np.where(h == 0.0, 0.0, gamma)


def gaussian_variogram(h, nugget, partial_sill, scale):
    """Gaussian semivariogram with gamma(0)=0 by convention."""
    h = np.asarray(h, dtype=float)
    gamma = nugget + partial_sill * (1.0 - np.exp(-(h / scale) ** 2))
    return np.where(h == 0.0, 0.0, gamma)


def spherical_variogram(h, nugget, partial_sill, range_parameter):
    """Spherical semivariogram with finite range."""
    h = np.asarray(h, dtype=float)
    r = h / range_parameter

    structured = np.where(
        h <= range_parameter,
        partial_sill * (1.5 * r - 0.5 * r**3),
        partial_sill,
    )

    gamma = nugget + structured
    return np.where(h == 0.0, 0.0, gamma)


def figure_05_variogram_models():
    """Compare exponential, Gaussian, and spherical shapes."""
    h = np.linspace(0.0, 80.0, 400)

    nugget = 0.5
    partial_sill = 4.5
    scale = 20.0

    exp_gamma = exponential_variogram(h, nugget, partial_sill, scale)
    gauss_gamma = gaussian_variogram(h, nugget, partial_sill, scale)
    sph_gamma = spherical_variogram(h, nugget, partial_sill, 60.0)

    plt.figure(figsize=(7, 5))
    plt.plot(h, exp_gamma, label="Exponential: scale a = 20")
    plt.plot(h, gauss_gamma, label="Gaussian: scale a = 20")
    plt.plot(h, sph_gamma, label="Spherical: range a = 60")
    plt.axhline(nugget + partial_sill, linestyle=":", label="Sill = 5")
    plt.xlabel("Lag distance h")
    plt.ylabel(r"Semivariance $\gamma(h)$")
    plt.title("Valid model families imply different near-origin behavior")
    plt.legend()
    save_and_close("05_variogram_models.png")


def figure_06_anisotropy():
    """
    Plot anisotropic correlation around a reference point.

    Major scale = 30 in x direction
    Minor scale = 10 in y direction

    rho(x,y) = exp(-sqrt((x/30)^2 + (y/10)^2))
    """
    x = np.linspace(-60.0, 60.0, 240)
    y = np.linspace(-40.0, 40.0, 180)
    xx, yy = np.meshgrid(x, y)

    scaled_distance = np.sqrt((xx / 30.0) ** 2 + (yy / 10.0) ** 2)
    correlation = np.exp(-scaled_distance)

    plt.figure(figsize=(7, 5))
    contour = plt.contourf(xx, yy, correlation, levels=12)
    plt.colorbar(contour, label="Correlation")
    plt.scatter([0.0], [0.0], s=90)
    plt.xlabel("x direction")
    plt.ylabel("y direction")
    plt.title("Anisotropy: dependence extends farther along the major axis")
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("06_anisotropy.png")


def figure_07_sampling_design():
    """
    Compare clustered local sampling with a broad space-filling design.

    The visual overlays both designs in one coordinate system using different
    marker shapes, avoiding multiple subplots.
    """
    rng = np.random.default_rng(11)

    # Clustered design: many nearby points, useful for short lags.
    cluster = rng.normal(loc=[28.0, 32.0], scale=[7.0, 7.0], size=(45, 2))
    cluster = np.clip(cluster, 0.0, 100.0)

    # Broad design: fewer points but good regional coverage.
    grid_x = np.linspace(10.0, 90.0, 5)
    grid_y = np.linspace(10.0, 90.0, 5)
    broad = np.array([(x, y) for x in grid_x for y in grid_y], dtype=float)
    broad = broad + rng.normal(0.0, 2.0, size=broad.shape)

    plt.figure(figsize=(7, 6))
    plt.scatter(
        cluster[:, 0],
        cluster[:, 1],
        marker="o",
        label="Dense local cluster: many short-distance pairs",
    )
    plt.scatter(
        broad[:, 0],
        broad[:, 1],
        marker="x",
        label="Broad coverage: more long-distance information",
    )
    plt.xlabel("x coordinate")
    plt.ylabel("y coordinate")
    plt.title("Sampling design determines which spatial scales are estimable")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.legend()
    save_and_close("07_sampling_design.png")


def hand_calculation_check():
    """
    Reproduce the hand-calculated gamma_hat(1)=1.9 example.

    Pairs exactly 1 unit apart:
        A-B, A-C, B-D, B-E, C-D

    Squared differences:
        4, 1, 4, 1, 9

    Sum = 19
    gamma_hat = 19 / (2 * 5) = 1.9
    """
    names = np.array(["A", "B", "C", "D", "E"])
    coords = np.array(
        [
            [0.0, 0.0],
            [1.0, 0.0],
            [0.0, 1.0],
            [1.0, 1.0],
            [2.0, 0.0],
        ]
    )
    values = np.array([10.0, 12.0, 11.0, 14.0, 13.0])

    squared_differences = []
    pair_names = []

    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            distance = np.linalg.norm(coords[i] - coords[j])
            if np.isclose(distance, 1.0):
                diff_sq = (values[i] - values[j]) ** 2
                pair_names.append(f"{names[i]}-{names[j]}")
                squared_differences.append(diff_sq)

    squared_differences = np.asarray(squared_differences)
    gamma_hat = squared_differences.sum() / (2.0 * len(squared_differences))

    print("\nHand calculation check for h = 1")
    for pair, diff_sq in zip(pair_names, squared_differences):
        print(f"{pair}: squared difference = {diff_sq:.0f}")
    print(f"sum of squared differences = {squared_differences.sum():.0f}")
    print(f"N(h) = {len(squared_differences)}")
    print(f"gamma_hat(1) = {gamma_hat:.3f}")


def main():
    hand_calculation_check()
    figure_01_spatial_samples()
    figure_02_trend_and_residuals()
    figure_03_covariance_and_variogram()
    figure_04_empirical_variogram()
    figure_05_variogram_models()
    figure_06_anisotropy()
    figure_07_sampling_design()
    print(f"\nAll figures are in: {FIG_DIR}")


if __name__ == "__main__":
    main()
