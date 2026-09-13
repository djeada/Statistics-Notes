"""
Spatial autocorrelation teaching visualizations
================================================

Creates the figures used in `spatial_autocorrelation.md`.

Dependencies:
    numpy
    matplotlib

Run:
    python scripts/spatial_statistics/spatial_autocorrelation_visualizations.py
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = REPO_ROOT / "assets" / "spatial_statistics" / "spatial_autocorrelation"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def save_and_close(filename):
    path = FIG_DIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"created: {path}")


def row_standardize(W):
    W = np.asarray(W, dtype=float).copy()
    row_sums = W.sum(axis=1)
    out = np.zeros_like(W)
    nonzero = row_sums > 0
    out[nonzero] = W[nonzero] / row_sums[nonzero, None]
    return out


def moran_i(x, W):
    x = np.asarray(x, dtype=float)
    W = np.asarray(W, dtype=float)
    z = x - x.mean()
    S0 = W.sum()
    return (len(x) / S0) * (z @ W @ z) / (z @ z)


def geary_c(x, W):
    x = np.asarray(x, dtype=float)
    W = np.asarray(W, dtype=float)
    n = len(x)
    S0 = W.sum()
    D2 = (x[:, None] - x[None, :]) ** 2
    numerator = np.sum(W * D2)
    denominator = np.sum((x - x.mean()) ** 2)
    return ((n - 1) / (2 * S0)) * numerator / denominator


def local_moran(x, W):
    x = np.asarray(x, dtype=float)
    z = x - x.mean()
    m2 = np.mean(z**2)
    lag = W @ z
    Ii = z * lag / m2
    return Ii, z, lag


def line_weights(n):
    W = np.zeros((n, n), dtype=float)
    for i in range(n - 1):
        W[i, i + 1] = 1.0
        W[i + 1, i] = 1.0
    return row_standardize(W)


def grid_coordinates(nx=6, ny=6):
    coords = np.array([(x, y) for y in range(ny) for x in range(nx)], dtype=float)
    return coords


def rook_weights(nx=6, ny=6):
    n = nx * ny
    W = np.zeros((n, n), dtype=float)

    def idx(x, y):
        return y * nx + x

    for y in range(ny):
        for x in range(nx):
            i = idx(x, y)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < nx and 0 <= yy < ny:
                    W[i, idx(xx, yy)] = 1.0

    return row_standardize(W)


def distance_weights(coords, threshold):
    D = np.sqrt(np.sum((coords[:, None, :] - coords[None, :, :]) ** 2, axis=2))
    W = ((D > 0) & (D <= threshold)).astype(float)
    return row_standardize(W)


def clustered_grid_values(coords, seed=5):
    rng = np.random.default_rng(seed)
    x = coords[:, 0]
    y = coords[:, 1]

    # Broad spatial pattern plus mild noise.
    values = (
        5.0
        + 1.2 * (x >= 3)
        + 1.0 * (y >= 3)
        - 1.0 * (x <= 1)
        - 0.8 * (y <= 1)
        + rng.normal(0.0, 0.28, size=len(coords))
    )
    return values


def permutation_distribution(x, W, permutations=999, seed=123):
    rng = np.random.default_rng(seed)
    observed = moran_i(x, W)
    sims = np.empty(permutations)

    for k in range(permutations):
        sims[k] = moran_i(rng.permutation(x), W)

    R = np.sum(sims >= observed)
    p = (R + 1) / (permutations + 1)
    return observed, sims, p


def figure_01_spatial_weights():
    coords = grid_coordinates(4, 4)
    W = rook_weights(4, 4)

    plt.figure(figsize=(6, 6))

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            if W[i, j] > 0 or W[j, i] > 0:
                plt.plot(
                    [coords[i, 0], coords[j, 0]],
                    [coords[i, 1], coords[j, 1]],
                    linewidth=1,
                )

    plt.scatter(coords[:, 0], coords[:, 1], s=100)

    for i, (x, y) in enumerate(coords):
        plt.annotate(str(i + 1), (x, y), xytext=(5, 5), textcoords="offset points")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Rook-style spatial weights: connected locations are neighbors")
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("01_spatial_weights.png")


def figure_02_clustered_values_map():
    coords = grid_coordinates(6, 6)
    values = clustered_grid_values(coords)

    plt.figure(figsize=(6.5, 6))
    pts = plt.scatter(
        coords[:, 0],
        coords[:, 1],
        c=values,
        s=260,
    )
    plt.colorbar(pts, label="Observed value")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("A spatial arrangement with locally similar values")
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("02_clustered_values_map.png")


def figure_03_moran_scatterplot():
    coords = grid_coordinates(6, 6)
    x = clustered_grid_values(coords)
    W = rook_weights(6, 6)

    z = x - x.mean()
    scale = np.sqrt(np.mean(z**2))
    z_std = z / scale
    lag_std = (W @ z) / scale

    I = moran_i(x, W)

    xx = np.linspace(z_std.min() - 0.3, z_std.max() + 0.3, 100)

    plt.figure(figsize=(7, 6))
    plt.scatter(z_std, lag_std, s=75)
    plt.axhline(0.0, linestyle=":")
    plt.axvline(0.0, linestyle=":")
    plt.plot(xx, I * xx, linestyle="--", label=f"slope = Moran I = {I:.3f}")
    plt.xlabel("Standardized centered value")
    plt.ylabel("Spatial lag on same scale")
    plt.title("Moran scatterplot")
    plt.legend()
    save_and_close("03_moran_scatterplot.png")


def figure_04_permutation_distribution():
    coords = grid_coordinates(6, 6)
    x = clustered_grid_values(coords)
    W = rook_weights(6, 6)

    observed, sims, p = permutation_distribution(x, W, 999, seed=222)

    plt.figure(figsize=(8, 5))
    plt.hist(sims, bins=32, alpha=0.8, label="Permuted Moran I")
    plt.axvline(
        observed,
        linestyle="--",
        linewidth=2,
        label=f"Observed I={observed:.3f}, p={p:.3f}",
    )
    plt.xlabel("Moran's I")
    plt.ylabel("Permutation frequency")
    plt.title("Permutation distribution under exchangeability")
    plt.legend()
    save_and_close("04_permutation_distribution.png")


def figure_05_moran_geary_sensitivity():
    """
    Start with an ordered 1D pattern, then increase one local outlier.
    Plot Moran I and 1-C on a common 'positive association' direction.
    """
    W = line_weights(9)
    base = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=float)
    shocks = np.linspace(0, 12, 80)

    moran_vals = []
    geary_assoc = []

    for shock in shocks:
        x = base.copy()
        x[4] += shock
        moran_vals.append(moran_i(x, W))
        geary_assoc.append(1.0 - geary_c(x, W))

    plt.figure(figsize=(8, 5))
    plt.plot(shocks, moran_vals, label="Moran I")
    plt.plot(shocks, geary_assoc, label="1 - Geary C")
    plt.axhline(0.0, linestyle=":")
    plt.xlabel("Size of local disturbance added to center location")
    plt.ylabel("Positive-association scale")
    plt.title("Moran and Geary react differently to a strong local contrast")
    plt.legend()
    save_and_close("05_moran_geary_sensitivity.png")


def classify_local(z, lag):
    categories = []
    for zi, li in zip(z, lag):
        if zi >= 0 and li >= 0:
            categories.append("HH")
        elif zi < 0 and li < 0:
            categories.append("LL")
        elif zi >= 0 and li < 0:
            categories.append("HL")
        else:
            categories.append("LH")
    return np.array(categories)


def figure_06_local_moran_categories():
    coords = grid_coordinates(6, 6)
    x = clustered_grid_values(coords, seed=12)

    # Force two obvious local contrasts for teaching.
    x[7] += 3.0
    x[28] -= 3.0

    W = rook_weights(6, 6)
    _, z, lag = local_moran(x, W)
    cats = classify_local(z, lag)

    markers = {"HH": "o", "LL": "s", "HL": "^", "LH": "v"}

    plt.figure(figsize=(7, 6))
    for cat in ["HH", "LL", "HL", "LH"]:
        use = cats == cat
        plt.scatter(
            coords[use, 0],
            coords[use, 1],
            s=150,
            marker=markers[cat],
            label=cat,
        )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Local Moran sign categories: cluster and spatial-outlier patterns")
    plt.legend()
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("06_local_moran_categories.png")


def figure_07_trend_vs_residual():
    """
    Show raw values and residual behavior along a line in one axes:
    raw series plus fitted trend and residuals shifted around zero.
    """
    rng = np.random.default_rng(51)
    s = np.arange(20, dtype=float)

    residual = rng.normal(0.0, 0.65, size=len(s))
    trend = 5.0 + 0.7 * s
    observed = trend + residual

    W = line_weights(len(s))
    raw_I = moran_i(observed, W)

    X = np.column_stack([np.ones(len(s)), s])
    beta = np.linalg.lstsq(X, observed, rcond=None)[0]
    fitted = X @ beta
    resid = observed - fitted
    resid_I = moran_i(resid, W)

    plt.figure(figsize=(9, 5))
    plt.plot(s, observed, "o-", label=f"Raw values: I={raw_I:.3f}")
    plt.plot(s, fitted, "--", label="Fitted linear trend")
    plt.plot(s, resid, "o-", label=f"Residuals: I={resid_I:.3f}")
    plt.axhline(0.0, linestyle=":")
    plt.xlabel("Spatial position")
    plt.ylabel("Value / residual")
    plt.title("A smooth mean trend can create strong raw spatial autocorrelation")
    plt.legend()
    save_and_close("07_trend_vs_residual.png")


def figure_08_weights_scale_sensitivity():
    rng = np.random.default_rng(71)
    coords = rng.uniform(0.0, 10.0, size=(70, 2))

    # Smooth radial signal plus noise.
    center = np.array([5.0, 5.0])
    dist_center = np.sqrt(np.sum((coords - center) ** 2, axis=1))
    values = 8.0 - 0.7 * dist_center + rng.normal(0.0, 0.55, len(coords))

    thresholds = np.linspace(1.3, 5.5, 28)
    I_values = []

    for threshold in thresholds:
        W = distance_weights(coords, threshold)
        if np.any(W.sum(axis=1) == 0):
            I_values.append(np.nan)
        else:
            I_values.append(moran_i(values, W))

    plt.figure(figsize=(8, 5))
    plt.plot(thresholds, I_values, "o-")
    plt.xlabel("Distance threshold used to define neighbors")
    plt.ylabel("Moran's I")
    plt.title("The measured spatial association depends on the neighborhood scale")
    save_and_close("08_weights_scale_sensitivity.png")


def print_worked_example():
    x = np.array([2, 3, 4, 8, 9], dtype=float)
    W = line_weights(5)

    z = x - x.mean()
    lag = W @ z
    numerator = z @ lag
    denominator = z @ z
    I = moran_i(x, W)
    C = geary_c(x, W)
    Ii, _, _ = local_moran(x, W)

    print("WORKED FIVE-LOCATION EXAMPLE")
    print("----------------------------")
    print("x =", x)
    print("mean =", x.mean())
    print("z =", z)
    print("\nW =")
    print(W)
    print("S0 =", W.sum())
    print("Wz =", lag)
    print("z'Wz =", numerator)
    print("z'z =", denominator)
    print("Moran I =", I)
    print("Null expectation =", -1.0 / (len(x) - 1))
    print("Geary C =", C)
    print("Local Moran =", Ii)


def main():
    print_worked_example()
    figure_01_spatial_weights()
    figure_02_clustered_values_map()
    figure_03_moran_scatterplot()
    figure_04_permutation_distribution()
    figure_05_moran_geary_sensitivity()
    figure_06_local_moran_categories()
    figure_07_trend_vs_residual()
    figure_08_weights_scale_sensitivity()
    print(f"\nAll figures are in: {FIG_DIR}")


if __name__ == "__main__":
    main()
