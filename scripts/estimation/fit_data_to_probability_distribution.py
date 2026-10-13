"""Fit candidate distributions by maximum likelihood and compare them."""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss


def generate_sample_data(rng: np.random.Generator, size: int = 1000) -> np.ndarray:
    """Generate positive, right-skewed data (a gamma distribution)."""
    return rng.gamma(shape=3.0, scale=2.0, size=size)


def fit_distribution(data: np.ndarray, distributions: list):
    """Fit each distribution by maximum likelihood and pick the best by SSE.

    The sum of squared errors compares the fitted density with a density
    histogram of the data, evaluated at the bin centres.
    """
    hist, edges = np.histogram(data, bins=30, density=True)
    centres = (edges[:-1] + edges[1:]) / 2

    results = []
    for distribution in distributions:
        params = distribution.fit(data)
        pdf = distribution.pdf(centres, *params)
        sse = float(np.sum((hist - pdf) ** 2))
        loglik = float(np.sum(distribution.logpdf(data, *params)))
        results.append((distribution, params, sse, loglik))

    best = min(results, key=lambda r: r[2])
    return best[0], best[1], results


def plot_data_and_fit(ax, data: np.ndarray, distribution, params) -> None:
    """Plot a histogram of the data and the fitted density."""
    ax.hist(data, bins=30, density=True, alpha=0.5, color="g", label="Data")
    x = np.linspace(data.min(), data.max(), 200)
    ax.plot(x, distribution.pdf(x, *params), "k", linewidth=2, label=distribution.name)
    ax.set_xlabel("Data")
    ax.set_ylabel("Density")
    ax.legend()


def main() -> None:
    rng = np.random.default_rng(0)
    data = generate_sample_data(rng)

    distributions = [ss.norm, ss.lognorm, ss.gamma]
    best_dist, best_params, results = fit_distribution(data, distributions)

    for dist, params, sse, loglik in results:
        print(f"{dist.name:8s} SSE={sse:.5f}  log-likelihood={loglik:.1f}")
    print(f"Best fit by SSE: {best_dist.name}")

    fig, ax = plt.subplots(figsize=(8, 6))
    plot_data_and_fit(ax, data, best_dist, best_params)
    plt.show()


if __name__ == "__main__":
    main()
