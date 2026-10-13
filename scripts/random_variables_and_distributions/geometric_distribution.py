"""Geometric distribution (trial of first success): hand-rolled PMF/CDF vs scipy.stats."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import geom


class GeometricDistribution:
    """Number of trials X in {1, 2, ...} up to and including the first success."""

    def __init__(self, p):
        self.p = p

    def pmf(self, k):
        k = np.asarray(k)
        return (1 - self.p) ** (k - 1) * self.p

    def cdf(self, k):
        k = np.asarray(k)
        return 1 - (1 - self.p) ** k


def plot_pmf(x, y1, y2, label1, label2, title):
    plt.figure(figsize=(10, 6))
    plt.stem(x, y1, basefmt=" ", linefmt="blue", markerfmt="bo", label=label1)
    plt.stem(x, y2, basefmt=" ", linefmt="red", markerfmt="ro", label=label2)
    plt.title(title)
    plt.xlabel("Number of trials (k)")
    plt.ylabel("PMF")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_cdf(x, y1, y2, label1, label2, title):
    plt.figure(figsize=(10, 6))
    plt.step(x, y1, where="post", label=label1, color="blue")
    plt.step(x, y2, where="post", label=label2, color="red")
    plt.title(title)
    plt.xlabel("Number of trials (k)")
    plt.ylabel("CDF")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    p1, p2 = 0.3, 0.5
    k = np.arange(1, 20)

    custom1, custom2 = GeometricDistribution(p1), GeometricDistribution(p2)
    # scipy.stats.geom uses the same trial-count convention (support starts at 1).
    pmf1_scipy, pmf2_scipy = geom.pmf(k, p1), geom.pmf(k, p2)
    cdf1_scipy, cdf2_scipy = geom.cdf(k, p1), geom.cdf(k, p2)

    assert np.allclose(custom1.pmf(k), pmf1_scipy) and np.allclose(custom2.pmf(k), pmf2_scipy)
    assert np.allclose(custom1.cdf(k), cdf1_scipy) and np.allclose(custom2.cdf(k), cdf2_scipy)
    print("Custom PMF/CDF match scipy.stats.geom")
    for p in (p1, p2):
        print(f"Geometric({p}): mean={1 / p:.3f}, var={(1 - p) / p**2:.3f}")

    plot_pmf(k, pmf1_scipy, pmf2_scipy, f"Geometric(p={p1})", f"Geometric(p={p2})",
             "Probability Mass Function (PMF) of Geometric Distributions")
    plot_cdf(k, cdf1_scipy, cdf2_scipy, f"Geometric(p={p1})", f"Geometric(p={p2})",
             "Cumulative Distribution Function (CDF) of Geometric Distributions")
    plot_pmf(k, pmf1_scipy, custom1.pmf(k), "scipy.stats", "hand-rolled",
             f"scipy vs hand-rolled PMF, Geometric(p={p1})")


if __name__ == "__main__":
    main()
