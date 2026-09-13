"""
Kriging teaching visualizations
===============================

This script creates all figures referenced in `kriging.md`.

Dependencies:
    numpy
    matplotlib

Run:
    python scripts/spatial_statistics/kriging_visualizations.py

The code is intentionally explicit rather than highly optimized so students
can connect each matrix operation to the equations in the notes.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = REPO_ROOT / "assets" / "spatial_statistics" / "kriging"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def save_and_close(filename):
    """Save the current figure and close it."""
    path = FIG_DIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"created: {path}")


def exponential_semivariogram(h, nugget=0.2, partial_sill=2.8, scale=1.5):
    """
    Exponential semivariogram.

    gamma(h) = nugget + partial_sill * (1 - exp(-h / scale)), h > 0
    gamma(0) = 0
    """
    h = np.asarray(h, dtype=float)
    gamma = nugget + partial_sill * (1.0 - np.exp(-h / scale))
    return np.where(np.isclose(h, 0.0), 0.0, gamma)


def exponential_covariance(h, partial_sill=2.8, scale=1.5):
    """
    Structured exponential covariance without independent measurement error.

    C(h) = partial_sill * exp(-h / scale)
    """
    h = np.asarray(h, dtype=float)
    return partial_sill * np.exp(-h / scale)


def distance_matrix(a, b):
    """Pairwise Euclidean distances between rows of a and b."""
    delta = a[:, None, :] - b[None, :, :]
    return np.sqrt(np.sum(delta**2, axis=2))


def ordinary_kriging_variogram(coords, values, target,
                               nugget=0.2,
                               partial_sill=2.8,
                               scale=1.5):
    """
    Ordinary kriging using the variogram system

        [Gamma  1] [lambda] = [gamma0]
        [1^T    0] [mu    ]   [1     ]

    and variance convention

        sigma_K^2 = lambda^T gamma0 + mu
    """
    coords = np.asarray(coords, dtype=float)
    values = np.asarray(values, dtype=float)
    target = np.asarray(target, dtype=float)

    n = len(values)

    obs_dist = distance_matrix(coords, coords)
    Gamma = exponential_semivariogram(
        obs_dist,
        nugget=nugget,
        partial_sill=partial_sill,
        scale=scale,
    )

    target_dist = np.sqrt(np.sum((coords - target) ** 2, axis=1))
    gamma0 = exponential_semivariogram(
        target_dist,
        nugget=nugget,
        partial_sill=partial_sill,
        scale=scale,
    )

    A = np.zeros((n + 1, n + 1), dtype=float)
    A[:n, :n] = Gamma
    A[:n, n] = 1.0
    A[n, :n] = 1.0

    rhs = np.zeros(n + 1, dtype=float)
    rhs[:n] = gamma0
    rhs[n] = 1.0

    solution = np.linalg.solve(A, rhs)
    weights = solution[:n]
    multiplier = solution[n]

    prediction = weights @ values
    variance = weights @ gamma0 + multiplier

    return prediction, variance, weights, multiplier, Gamma, gamma0


def ordinary_kriging_covariance(coords, values, target,
                                process_variance=3.0,
                                scale=2.5,
                                diagonal_noise=0.0):
    """
    Ordinary kriging in covariance form.

    This version is useful for smooth prediction surfaces. A diagonal_noise
    term may be added to the observation covariance matrix.
    """
    coords = np.asarray(coords, dtype=float)
    values = np.asarray(values, dtype=float)
    target = np.asarray(target, dtype=float)
    n = len(values)

    obs_dist = distance_matrix(coords, coords)
    C = process_variance * np.exp(-obs_dist / scale)
    C = C + diagonal_noise * np.eye(n)

    d0 = np.sqrt(np.sum((coords - target) ** 2, axis=1))
    c0 = process_variance * np.exp(-d0 / scale)

    A = np.zeros((n + 1, n + 1), dtype=float)
    A[:n, :n] = C
    A[:n, n] = 1.0
    A[n, :n] = 1.0

    rhs = np.zeros(n + 1, dtype=float)
    rhs[:n] = c0
    rhs[n] = 1.0

    sol = np.linalg.solve(A, rhs)
    weights = sol[:n]
    lagrange = sol[n]

    pred = weights @ values

    # With this covariance-system sign convention:
    # C lambda + 1*lagrange = c0
    # variance = C(0) - lambda^T c0 - lagrange
    var = process_variance - weights @ c0 - lagrange

    return pred, max(var, 0.0), weights


def simple_kriging(coords, values, target, mean,
                   process_variance=3.0,
                   scale=2.5,
                   measurement_variance=0.0):
    """
    Simple kriging of the latent spatial process.

    Observation covariance:
        process covariance + measurement variance on the diagonal

    Target-observation covariance contains only process covariance because
    the target is the latent error-free field.
    """
    coords = np.asarray(coords, dtype=float)
    values = np.asarray(values, dtype=float)
    target = np.asarray(target, dtype=float)

    D = distance_matrix(coords, coords)
    C = process_variance * np.exp(-D / scale)
    C = C + measurement_variance * np.eye(len(values))

    d0 = np.sqrt(np.sum((coords - target) ** 2, axis=1))
    c0 = process_variance * np.exp(-d0 / scale)

    weights = np.linalg.solve(C, c0)
    prediction = mean + weights @ (values - mean)

    variance = process_variance - c0 @ np.linalg.solve(C, c0)

    return prediction, max(variance, 0.0), weights


def print_worked_ordinary_example():
    """Print every important number in the chapter's worked example."""
    coords = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0],
    ])
    values = np.array([10.0, 12.0, 11.0])
    target = np.array([0.5, 0.5])

    pred, var, weights, mu, Gamma, gamma0 = ordinary_kriging_variogram(
        coords,
        values,
        target,
        nugget=0.2,
        partial_sill=2.8,
        scale=1.5,
    )

    print("\nWORKED ORDINARY-KRIGING EXAMPLE")
    print("--------------------------------")
    print("Observation coordinates:")
    print(coords)
    print("Observation values:", values)
    print("Target:", target)

    print("\nGamma matrix:")
    print(np.round(Gamma, 4))

    print("\ngamma0 vector:")
    print(np.round(gamma0, 4))

    print("\nWeights:")
    print(np.round(weights, 6))
    print("sum(weights) =", weights.sum())
    print("Lagrange multiplier =", round(mu, 6))
    print("Prediction =", round(pred, 6))
    print("Kriging variance =", round(var, 6))
    print("Kriging standard deviation =", round(np.sqrt(var), 6))


def figure_01_kriging_geometry():
    """Plot the three observations and the target from the hand example."""
    coords = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0],
    ])
    values = np.array([10.0, 12.0, 11.0])
    names = ["A", "B", "C"]
    target = np.array([0.5, 0.5])

    plt.figure(figsize=(7, 5))
    pts = plt.scatter(coords[:, 0], coords[:, 1], c=values, s=220)
    plt.colorbar(pts, label="Observed value")
    plt.scatter([target[0]], [target[1]], marker="*", s=300, label="Target s0")

    for xy, name, value in zip(coords, names, values):
        plt.annotate(
            f"{name}: {value:.0f}",
            xy,
            xytext=(8, 8),
            textcoords="offset points",
        )

    plt.annotate(
        "prediction target",
        target,
        xytext=(8, -18),
        textcoords="offset points",
    )

    plt.xlabel("x coordinate")
    plt.ylabel("y coordinate")
    plt.title("Kriging combines sampled values to predict an unsampled target")
    plt.legend()
    plt.xlim(-0.25, 1.25)
    plt.ylim(-0.25, 1.25)
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("01_kriging_geometry.png")


def figure_02_ordinary_kriging_weights():
    """Visualize the ordinary-kriging weights from the worked example."""
    coords = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0],
    ])
    values = np.array([10.0, 12.0, 11.0])
    names = ["A", "B", "C"]
    target = np.array([0.5, 0.5])

    pred, var, weights, mu, _, _ = ordinary_kriging_variogram(
        coords,
        values,
        target,
    )

    plt.figure(figsize=(7, 5))

    # Line width is proportional to absolute kriging weight.
    for xy, w, name in zip(coords, weights, names):
        plt.plot(
            [xy[0], target[0]],
            [xy[1], target[1]],
            linewidth=1.0 + 8.0 * abs(w),
        )
        midpoint = (xy + target) / 2.0
        plt.annotate(
            f"{name}: λ={w:.3f}",
            midpoint,
            xytext=(5, 4),
            textcoords="offset points",
        )

    plt.scatter(coords[:, 0], coords[:, 1], s=170, label="Observations")
    plt.scatter([target[0]], [target[1]], marker="*", s=270, label="Target")
    plt.xlabel("x coordinate")
    plt.ylabel("y coordinate")
    plt.title(
        f"Ordinary-kriging weights; prediction = {pred:.3f}, "
        f"variance = {var:.3f}"
    )
    plt.legend()
    plt.xlim(-0.25, 1.25)
    plt.ylim(-0.25, 1.25)
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("02_ordinary_kriging_weights.png")


def figure_03_redundancy_and_weights():
    """
    Show that two almost colocated observations split influence because
    they are redundant with one another.
    """
    coords = np.array([
        [0.0, 0.0],
        [0.12, 0.05],
        [0.0, 1.0],
        [1.1, 0.5],
    ])
    values = np.array([10.0, 10.5, 13.0, 12.0])
    target = np.array([0.45, 0.35])

    pred, var, weights = ordinary_kriging_covariance(
        coords,
        values,
        target,
        process_variance=3.0,
        scale=0.8,
    )

    plt.figure(figsize=(7, 5))

    for i, (xy, w) in enumerate(zip(coords, weights), start=1):
        plt.plot(
            [xy[0], target[0]],
            [xy[1], target[1]],
            linewidth=1.0 + 7.0 * abs(w),
        )
        plt.annotate(
            f"P{i}\nλ={w:.3f}",
            xy,
            xytext=(7, 7),
            textcoords="offset points",
        )

    plt.scatter(coords[:, 0], coords[:, 1], s=170, label="Observations")
    plt.scatter([target[0]], [target[1]], marker="*", s=270, label="Target")
    plt.xlabel("x coordinate")
    plt.ylabel("y coordinate")
    plt.title("Kriging accounts for redundancy among nearby observations")
    plt.legend()
    plt.xlim(-0.2, 1.35)
    plt.ylim(-0.2, 1.25)
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("03_redundancy_and_weights.png")

    print("\nREDUNDANCY EXAMPLE")
    for i, w in enumerate(weights, start=1):
        print(f"P{i} weight = {w:.6f}")
    print("prediction =", pred)
    print("variance =", var)


def synthetic_surface_dataset():
    """Small deterministic dataset used for prediction-surface figures."""
    coords = np.array([
        [0.5, 0.8],
        [1.2, 3.8],
        [2.0, 1.8],
        [3.2, 4.5],
        [4.2, 1.0],
        [5.1, 3.4],
        [6.2, 1.7],
        [6.8, 4.8],
        [7.8, 2.8],
        [8.7, 0.9],
        [9.0, 4.3],
    ])

    # A broad trend plus deterministic local variation.
    x = coords[:, 0]
    y = coords[:, 1]
    values = (
        8.0
        + 0.35 * x
        - 0.15 * y
        + 1.8 * np.sin(0.8 * x)
        + 0.7 * np.cos(1.2 * y)
    )
    return coords, values


def build_prediction_grid(coords, values, nx=85, ny=55):
    """Predict ordinary kriging over a rectangular grid."""
    xs = np.linspace(0.0, 9.5, nx)
    ys = np.linspace(0.0, 5.3, ny)
    xx, yy = np.meshgrid(xs, ys)

    pred = np.empty_like(xx)
    var = np.empty_like(xx)

    for row in range(ny):
        for col in range(nx):
            target = np.array([xx[row, col], yy[row, col]])
            p, v, _ = ordinary_kriging_covariance(
                coords,
                values,
                target,
                process_variance=4.0,
                scale=2.3,
            )
            pred[row, col] = p
            var[row, col] = v

    return xx, yy, pred, var


def figure_04_prediction_surface():
    """Create an ordinary-kriging prediction surface."""
    coords, values = synthetic_surface_dataset()
    xx, yy, pred, _ = build_prediction_grid(coords, values)

    plt.figure(figsize=(8, 5))
    image = plt.contourf(xx, yy, pred, levels=16)
    plt.colorbar(image, label="Ordinary-kriging prediction")
    plt.scatter(coords[:, 0], coords[:, 1], c=values, s=85, edgecolors="none")
    plt.xlabel("x coordinate")
    plt.ylabel("y coordinate")
    plt.title("Ordinary-kriging prediction surface")
    save_and_close("04_prediction_surface.png")


def figure_05_variance_surface():
    """Create the kriging variance surface for the same sample geometry."""
    coords, values = synthetic_surface_dataset()
    xx, yy, _, var = build_prediction_grid(coords, values)

    plt.figure(figsize=(8, 5))
    image = plt.contourf(xx, yy, var, levels=16)
    plt.colorbar(image, label="Kriging variance")
    plt.scatter(coords[:, 0], coords[:, 1], s=85)
    plt.xlabel("x coordinate")
    plt.ylabel("y coordinate")
    plt.title("Kriging uncertainty is controlled strongly by sampling geometry")
    save_and_close("05_variance_surface.png")


def figure_06_simple_vs_ordinary():
    """
    Compare predictions along a 1D transect.

    Simple kriging returns toward the known mean far from the data.
    Ordinary kriging must satisfy the unknown-constant-mean constraint.
    """
    x_obs = np.array([0.0, 1.5, 3.0, 4.5])
    coords = np.column_stack([x_obs, np.zeros_like(x_obs)])
    values = np.array([8.0, 11.0, 12.0, 10.0])
    known_mean = 9.5

    x_targets = np.linspace(-4.0, 10.0, 260)
    simple_pred = []
    ordinary_pred = []

    for x0 in x_targets:
        target = np.array([x0, 0.0])

        sp, _, _ = simple_kriging(
            coords,
            values,
            target,
            mean=known_mean,
            process_variance=3.0,
            scale=1.7,
        )
        op, _, _ = ordinary_kriging_covariance(
            coords,
            values,
            target,
            process_variance=3.0,
            scale=1.7,
        )

        simple_pred.append(sp)
        ordinary_pred.append(op)

    plt.figure(figsize=(8, 5))
    plt.plot(x_targets, simple_pred, label="Simple kriging")
    plt.plot(x_targets, ordinary_pred, label="Ordinary kriging")
    plt.axhline(known_mean, linestyle=":", label="Known simple-kriging mean")
    plt.scatter(x_obs, values, s=90, label="Observations")
    plt.xlabel("x coordinate")
    plt.ylabel("Predicted value")
    plt.title("Simple kriging returns toward the known mean far from observations")
    plt.legend()
    save_and_close("06_simple_vs_ordinary.png")


def figure_07_nugget_interpolation():
    """
    Compare latent-process prediction with and without measurement error.

    When measurement variance is zero, simple kriging reproduces the observed
    value at a sampled coordinate. With measurement error, prediction of the
    latent field smooths the noisy observations.
    """
    x_obs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    coords = np.column_stack([x_obs, np.zeros_like(x_obs)])
    values = np.array([10.0, 12.8, 10.9, 13.4, 12.1, 14.0])
    mean = 12.0

    x_grid = np.linspace(0.0, 5.0, 280)
    zero_noise = []
    noisy_latent = []

    for x0 in x_grid:
        target = np.array([x0, 0.0])

        p0, _, _ = simple_kriging(
            coords,
            values,
            target,
            mean=mean,
            process_variance=3.0,
            scale=1.25,
            measurement_variance=0.0,
        )

        p1, _, _ = simple_kriging(
            coords,
            values,
            target,
            mean=mean,
            process_variance=3.0,
            scale=1.25,
            measurement_variance=0.9,
        )

        zero_noise.append(p0)
        noisy_latent.append(p1)

    plt.figure(figsize=(8, 5))
    plt.plot(x_grid, zero_noise, label="No measurement error: exact at samples")
    plt.plot(x_grid, noisy_latent, label="Latent process with measurement error")
    plt.scatter(x_obs, values, s=90, label="Observed noisy values")
    plt.xlabel("x coordinate")
    plt.ylabel("Predicted value")
    plt.title("Nugget interpretation determines whether sampled values are smoothed")
    plt.legend()
    save_and_close("07_nugget_interpolation.png")


def leave_one_out_ordinary(coords, values,
                           process_variance=4.0,
                           scale=2.3):
    """Leave-one-out ordinary-kriging predictions and standard deviations."""
    predictions = []
    standard_deviations = []

    for i in range(len(values)):
        keep = np.arange(len(values)) != i

        pred, var, _ = ordinary_kriging_covariance(
            coords[keep],
            values[keep],
            coords[i],
            process_variance=process_variance,
            scale=scale,
        )

        predictions.append(pred)
        standard_deviations.append(np.sqrt(max(var, 1e-12)))

    return np.asarray(predictions), np.asarray(standard_deviations)


def figure_08_cross_validation():
    """Observed versus leave-one-out-predicted values."""
    coords, values = synthetic_surface_dataset()
    pred, sd = leave_one_out_ordinary(coords, values)

    errors = values - pred
    standardized = errors / sd

    low = min(values.min(), pred.min())
    high = max(values.max(), pred.max())

    plt.figure(figsize=(6, 6))
    plt.scatter(values, pred, s=95)
    plt.plot([low, high], [low, high], linestyle="--", label="Perfect prediction")
    plt.xlabel("Observed value")
    plt.ylabel("Leave-one-out prediction")
    plt.title("Leave-one-out cross-validation")
    plt.legend()
    save_and_close("08_cross_validation.png")

    me = errors.mean()
    rmse = np.sqrt(np.mean(errors**2))
    mean_std = standardized.mean()
    std_std = standardized.std(ddof=1)

    print("\nLEAVE-ONE-OUT CROSS-VALIDATION")
    print("--------------------------------")
    print("Mean error =", round(me, 6))
    print("RMSE =", round(rmse, 6))
    print("Mean standardized error =", round(mean_std, 6))
    print("SD of standardized errors =", round(std_std, 6))


def main():
    print_worked_ordinary_example()
    figure_01_kriging_geometry()
    figure_02_ordinary_kriging_weights()
    figure_03_redundancy_and_weights()
    figure_04_prediction_surface()
    figure_05_variance_surface()
    figure_06_simple_vs_ordinary()
    figure_07_nugget_interpolation()
    figure_08_cross_validation()
    print(f"\nAll figures are in: {FIG_DIR}")


if __name__ == "__main__":
    main()
