"""Time series, ACF, and PACF for common process types."""

import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import acf, pacf

N = 100
NLAGS = 20


def generate_ar(rng, phis, n=N):
    """AR(p): x_t = sum_j phi_j x_{t-j} + e_t, with a burn-in period."""
    burn = 100
    p = len(phis)
    e = rng.normal(size=n + burn)
    x = np.zeros(n + burn)
    for t in range(p, n + burn):
        x[t] = sum(phi * x[t - j - 1] for j, phi in enumerate(phis)) + e[t]
    return x[burn:]


def generate_ma(rng, thetas, n=N):
    """MA(q): x_t = e_t + sum_j theta_j e_{t-j} (no wrap-around)."""
    q = len(thetas)
    e = rng.normal(size=n + q)
    x = e[q:].copy()
    for j, theta in enumerate(thetas, start=1):
        x += theta * e[q - j : n + q - j]
    return x


def build_series(rng, n=N):
    return [
        ("AR(1)", generate_ar(rng, [0.5], n)),
        ("AR(2)", generate_ar(rng, [0.5, -0.25], n)),
        ("MA(1)", generate_ma(rng, [0.5], n)),
        ("MA(2)", generate_ma(rng, [0.5, 0.3], n)),
        ("Linear Growing", np.arange(n, dtype=float)),
        ("Constant", np.full(n, 10.0)),
        ("Sine with Noise", np.sin(np.linspace(0, 4 * np.pi, n)) + rng.normal(scale=0.1, size=n)),
        ("White Noise", rng.normal(size=n)),
    ]


def main():
    rng = np.random.default_rng(42)
    types = build_series(rng)

    fig, axes = plt.subplots(len(types), 3, figsize=(15, 3 * len(types)))
    fig.suptitle("Time Series, ACF, and PACF", fontsize=16)

    for i, (title, series) in enumerate(types):
        axes[i, 0].plot(series)
        axes[i, 0].set_title(f"{title} - Time Series")

        if np.ptp(series) == 0:
            # Zero variance: the ACF/PACF are undefined.
            for col, name in ((1, "ACF"), (2, "PACF")):
                axes[i, col].text(0.5, 0.5, f"{name} undefined\n(zero variance)", ha="center", va="center")
                axes[i, col].set_title(f"{title} - {name}")
            continue

        axes[i, 1].stem(acf(series, nlags=NLAGS))
        axes[i, 1].set_title(f"{title} - ACF")
        axes[i, 2].stem(pacf(series, nlags=NLAGS))
        axes[i, 2].set_title(f"{title} - PACF")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
