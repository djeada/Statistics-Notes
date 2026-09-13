"""
Spatial regression teaching visualizations
===========================================

Creates the figures used in `spatial_regression.md`.

Dependencies:
    numpy
    matplotlib

Run:
    python scripts/spatial_statistics/spatial_regression_visualizations.py
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = REPO_ROOT / "assets" / "spatial_statistics" / "spatial_regression"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def save_and_close(filename):
    path = FIG_DIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"created: {path}")


def row_standardize(W):
    W = np.asarray(W, dtype=float).copy()
    rs = W.sum(axis=1)
    out = np.zeros_like(W)
    nz = rs > 0
    out[nz] = W[nz] / rs[nz, None]
    return out


def line_weights(n):
    W = np.zeros((n, n), dtype=float)
    for i in range(n - 1):
        W[i, i + 1] = 1.0
        W[i + 1, i] = 1.0
    return row_standardize(W)


def distance_matrix(coords):
    delta = coords[:, None, :] - coords[None, :, :]
    return np.sqrt(np.sum(delta**2, axis=2))


def exponential_covariance(coords,
                           spatial_variance=1.0,
                           scale=2.0,
                           nugget_variance=0.0):
    D = distance_matrix(coords)
    Sigma = spatial_variance * np.exp(-D / scale)
    Sigma += nugget_variance * np.eye(len(coords))
    return Sigma


def ols_fit(X, y):
    XtX_inv = np.linalg.inv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    residual = y - X @ beta
    return beta, residual


def gls_fit(X, y, Sigma):
    Sinv = np.linalg.inv(Sigma)
    beta = np.linalg.inv(X.T @ Sinv @ X) @ X.T @ Sinv @ y
    residual = y - X @ beta
    return beta, residual


def moran_i(x, W):
    x = np.asarray(x, dtype=float)
    z = x - x.mean()
    S0 = W.sum()
    if np.allclose(z @ z, 0):
        return np.nan
    return (len(x) / S0) * (z @ W @ z) / (z @ z)


def figure_01_mean_misspecification():
    s = np.arange(18, dtype=float)
    rng = np.random.default_rng(12)

    true_mean = 5.0 + 0.65 * s
    y = true_mean + rng.normal(0.0, 0.35, size=len(s))

    # Wrong intercept-only model.
    wrong_fit = np.repeat(y.mean(), len(y))
    wrong_resid = y - wrong_fit

    # Correct linear mean.
    X = np.column_stack([np.ones(len(s)), s])
    beta, correct_resid = ols_fit(X, y)
    fitted = X @ beta

    plt.figure(figsize=(9, 5))
    plt.plot(s, y, "o-", label="Observed")
    plt.plot(s, wrong_fit, linestyle=":", label="Intercept-only fit")
    plt.plot(s, fitted, linestyle="--", label="Linear spatial trend fit")
    plt.plot(s, wrong_resid, "o-", label="Residuals from wrong mean")
    plt.xlabel("Spatial position")
    plt.ylabel("Value / residual")
    plt.title("Mean misspecification can create strongly patterned residuals")
    plt.legend()
    save_and_close("01_mean_misspecification.png")


def figure_02_spatially_correlated_errors():
    rng = np.random.default_rng(20)
    coords = np.column_stack([np.arange(40, dtype=float), np.zeros(40)])
    Sigma = exponential_covariance(
        coords,
        spatial_variance=1.0,
        scale=4.5,
        nugget_variance=0.15,
    )

    L = np.linalg.cholesky(Sigma + 1e-10 * np.eye(len(coords)))
    error = L @ rng.standard_normal(len(coords))

    plt.figure(figsize=(9, 5))
    plt.plot(coords[:, 0], error, "o-")
    plt.axhline(0.0, linestyle=":")
    plt.xlabel("Spatial position")
    plt.ylabel("Error realization")
    plt.title("Spatially correlated errors tend to move together over nearby locations")
    save_and_close("02_spatially_correlated_errors.png")


def figure_03_ols_vs_gls_sampling():
    """
    Simulate repeated datasets under the same spatial covariance.
    OLS and GLS are both centered near the truth, but GLS is more efficient.
    """
    rng = np.random.default_rng(30)

    n = 32
    s = np.linspace(0, 10, n)
    coords = np.column_stack([s, np.zeros(n)])
    x = (s - s.mean()) / s.std()
    X = np.column_stack([np.ones(n), x])

    beta_true = np.array([2.0, 1.3])

    Sigma = exponential_covariance(
        coords,
        spatial_variance=1.2,
        scale=2.0,
        nugget_variance=0.25,
    )
    L = np.linalg.cholesky(Sigma + 1e-10 * np.eye(n))

    B_ols = []
    B_gls = []

    for _ in range(1200):
        eps = L @ rng.standard_normal(n)
        y = X @ beta_true + eps
        b_ols, _ = ols_fit(X, y)
        b_gls, _ = gls_fit(X, y, Sigma)
        B_ols.append(b_ols[1])
        B_gls.append(b_gls[1])

    B_ols = np.asarray(B_ols)
    B_gls = np.asarray(B_gls)

    # Compare sorted sampling distributions in one chart.
    q = np.linspace(0.001, 0.999, 250)
    ols_q = np.quantile(B_ols, q)
    gls_q = np.quantile(B_gls, q)

    plt.figure(figsize=(8, 5))
    plt.plot(q, ols_q, label=f"OLS slope, SD={B_ols.std(ddof=1):.3f}")
    plt.plot(q, gls_q, label=f"GLS slope, SD={B_gls.std(ddof=1):.3f}")
    plt.axhline(beta_true[1], linestyle=":", label="True slope")
    plt.xlabel("Sampling-distribution quantile")
    plt.ylabel("Estimated slope")
    plt.title("With the covariance known, GLS is more efficient than OLS")
    plt.legend()
    save_and_close("03_ols_vs_gls_sampling.png")

    print("\nREPEATED-SAMPLE COMPARISON")
    print("OLS mean slope =", B_ols.mean())
    print("GLS mean slope =", B_gls.mean())
    print("OLS slope SD   =", B_ols.std(ddof=1))
    print("GLS slope SD   =", B_gls.std(ddof=1))


def figure_04_spatial_error_propagation():
    n = 9
    W = line_weights(n)
    lam = 0.55

    eps = np.zeros(n)
    eps[2] = 1.0

    u = np.linalg.solve(np.eye(n) - lam * W, eps)

    x = np.arange(n)

    plt.figure(figsize=(8, 5))
    plt.stem(x, eps, linefmt=":", markerfmt="o", basefmt=" ", label="Independent innovation ε")
    plt.plot(x, u, "o-", label="Spatial error u")
    plt.xlabel("Region along line")
    plt.ylabel("Shock magnitude")
    plt.title("Spatial error model: one innovation propagates through the disturbance process")
    plt.legend()
    save_and_close("04_spatial_error_propagation.png")


def figure_05_sar_impacts():
    n = 9
    W = line_weights(n)
    rho = 0.45
    beta = 1.8

    S = np.linalg.inv(np.eye(n) - rho * W)
    impact = beta * S

    source = 3
    response = impact[:, source]

    x = np.arange(n)

    plt.figure(figsize=(8, 5))
    plt.plot(x, response, "o-")
    plt.axvline(source, linestyle=":", label="Predictor change occurs here")
    plt.xlabel("Outcome location")
    plt.ylabel("Change in expected outcome")
    plt.title("SAR multiplier creates direct and indirect effects across locations")
    plt.legend()
    save_and_close("05_sar_impacts.png")


def figure_06_spatial_confounding():
    rng = np.random.default_rng(42)
    s = np.linspace(0, 1, 80)

    predictor = np.sin(2 * np.pi * s) + 0.2 * s
    latent = 0.85 * np.sin(2 * np.pi * s + 0.35) + 0.15 * np.cos(4 * np.pi * s)
    outcome = 1.2 * predictor + latent + rng.normal(0.0, 0.15, len(s))

    # Scale latent for comparable display; the point is visual overlap.
    plt.figure(figsize=(9, 5))
    plt.plot(s, predictor, label="Smooth predictor x(s)")
    plt.plot(s, latent, label="Latent spatial effect u(s)")
    plt.plot(s, outcome / np.std(outcome), label="Scaled outcome")
    plt.xlabel("Spatial position")
    plt.ylabel("Scaled pattern")
    plt.title("Spatial confounding: predictor and latent effect vary on similar scales")
    plt.legend()
    save_and_close("06_spatial_confounding.png")


def figure_07_residual_whitening():
    rng = np.random.default_rng(55)

    n = 45
    s = np.linspace(0, 12, n)
    coords = np.column_stack([s, np.zeros(n)])

    x = np.sin(s / 3.0)
    X = np.column_stack([np.ones(n), x])
    beta_true = np.array([3.0, 1.4])

    Sigma = exponential_covariance(
        coords,
        spatial_variance=1.0,
        scale=2.2,
        nugget_variance=0.25,
    )
    L = np.linalg.cholesky(Sigma + 1e-10 * np.eye(n))

    eps = L @ rng.standard_normal(n)
    y = X @ beta_true + eps

    beta_gls, raw_resid = gls_fit(X, y, Sigma)
    white_resid = np.linalg.solve(L, raw_resid)

    plt.figure(figsize=(9, 5))
    plt.plot(s, raw_resid, "o-", label="Raw GLS residuals")
    plt.plot(s, white_resid, "o-", label="Whitened residuals")
    plt.axhline(0.0, linestyle=":")
    plt.xlabel("Spatial position")
    plt.ylabel("Residual")
    plt.title("A correct GLS model can have correlated raw residuals but uncorrelated innovations")
    plt.legend()
    save_and_close("07_residual_whitening.png")

    W = line_weights(n)
    print("\nRESIDUAL DIAGNOSTIC EXAMPLE")
    print("Raw residual Moran I =", moran_i(raw_resid, W))
    print("Whitened residual Moran I =", moran_i(white_resid, W))


def figure_08_spatial_validation():
    rng = np.random.default_rng(70)

    # Training points in two left-side clusters; a test region on the right.
    train_left = rng.normal(loc=[2.2, 3.2], scale=[0.8, 0.9], size=(25, 2))
    train_mid = rng.normal(loc=[5.0, 6.3], scale=[0.9, 0.8], size=(20, 2))
    train = np.vstack([train_left, train_mid])

    # Random-CV-like held-out points are embedded near training locations.
    random_holdout = train[[3, 9, 15, 28, 34]].copy()

    # Spatial transfer holdout is geographically separate.
    spatial_holdout = rng.normal(loc=[8.5, 4.5], scale=[0.55, 1.0], size=(12, 2))

    plt.figure(figsize=(8, 6))
    plt.scatter(train[:, 0], train[:, 1], s=55, label="Training locations")
    plt.scatter(
        random_holdout[:, 0],
        random_holdout[:, 1],
        s=120,
        marker="x",
        label="Random-CV holdouts",
    )
    plt.scatter(
        spatial_holdout[:, 0],
        spatial_holdout[:, 1],
        s=85,
        marker="^",
        label="Spatial transfer holdouts",
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Random holdouts and geographic transfer test different prediction tasks")
    plt.legend()
    save_and_close("08_spatial_validation.png")


def print_worked_examples():
    print("WORKED NUMERICAL EXAMPLES")
    print("-------------------------")

    # OLS example.
    X = np.array([
        [1.0, 0.0],
        [1.0, 1.0],
        [1.0, 2.0],
    ])
    y = np.array([1.0, 2.0, 4.0])

    beta_ols, _ = ols_fit(X, y)
    print("OLS beta =", beta_ols)

    # A positive definite covariance with strong adjacent correlation.
    Sigma = np.array([
        [1.0, 0.6, 0.2],
        [0.6, 1.0, 0.6],
        [0.2, 0.6, 1.0],
    ])

    beta_gls, _ = gls_fit(X, y, Sigma)
    print("GLS beta =", beta_gls)

    # Spatial error 3-region example.
    W = np.array([
        [0.0, 1.0, 0.0],
        [0.5, 0.0, 0.5],
        [0.0, 1.0, 0.0],
    ])
    lam = 0.4
    eps = np.array([1.0, 0.0, 0.0])
    u = np.linalg.solve(np.eye(3) - lam * W, eps)
    print("Spatial error u =", u)

    # SAR multiplier and impacts.
    rho = 0.4
    beta = 2.0
    S = np.linalg.inv(np.eye(3) - rho * W)
    impacts = beta * S
    print("SAR multiplier S =")
    print(S)
    print("SAR impact matrix beta*S =")
    print(impacts)


def main():
    print_worked_examples()
    figure_01_mean_misspecification()
    figure_02_spatially_correlated_errors()
    figure_03_ols_vs_gls_sampling()
    figure_04_spatial_error_propagation()
    figure_05_sar_impacts()
    figure_06_spatial_confounding()
    figure_07_residual_whitening()
    figure_08_spatial_validation()
    print(f"\nAll figures are in: {FIG_DIR}")


if __name__ == "__main__":
    main()
