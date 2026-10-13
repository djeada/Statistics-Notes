"""Binomial distribution: hand-rolled PMF/CDF checked against scipy.stats."""
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom


class BinomialDistribution:
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def pmf(self, k):
        k = np.asarray(k)
        return np.array([math.comb(self.n, int(i)) * self.p**i * (1 - self.p) ** (self.n - i)
                         for i in k.ravel()]).reshape(k.shape)

    def cdf(self, k):
        k = np.asarray(k)
        support = np.arange(self.n + 1)
        cum = np.cumsum(self.pmf(support))
        return cum[np.clip(k, 0, self.n).astype(int)]


def plot_pmf(x1, y1, x2, y2, label1, label2, title):
    plt.figure(figsize=(10, 6))
    plt.stem(x1, y1, basefmt=" ", linefmt="blue", markerfmt="bo", label=label1)
    plt.stem(x2, y2, basefmt=" ", linefmt="red", markerfmt="ro", label=label2)
    plt.title(title)
    plt.xlabel("Number of successes (k)")
    plt.ylabel("PMF")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_cdf(x1, y1, x2, y2, label1, label2, title):
    plt.figure(figsize=(10, 6))
    plt.step(x1, y1, where="post", label=label1, color="blue")
    plt.step(x2, y2, where="post", label=label2, color="red")
    plt.title(title)
    plt.xlabel("Number of successes (k)")
    plt.ylabel("CDF")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    n1, p1 = 10, 0.5
    n2, p2 = 15, 0.7
    k1 = np.arange(0, n1 + 1)
    k2 = np.arange(0, n2 + 1)

    custom1, custom2 = BinomialDistribution(n1, p1), BinomialDistribution(n2, p2)
    pmf1_scipy, pmf2_scipy = binom.pmf(k1, n1, p1), binom.pmf(k2, n2, p2)
    cdf1_scipy, cdf2_scipy = binom.cdf(k1, n1, p1), binom.cdf(k2, n2, p2)

    # The hand-rolled formulas must agree with scipy.stats.
    assert np.allclose(custom1.pmf(k1), pmf1_scipy) and np.allclose(custom2.pmf(k2), pmf2_scipy)
    assert np.allclose(custom1.cdf(k1), cdf1_scipy) and np.allclose(custom2.cdf(k2), cdf2_scipy)
    print("Custom PMF/CDF match scipy.stats.binom")
    print(f"Binomial({n1}, {p1}): mean={n1 * p1}, var={n1 * p1 * (1 - p1):.3f}")

    plot_pmf(k1, pmf1_scipy, k2, pmf2_scipy,
             f"Binomial(n={n1}, p={p1})", f"Binomial(n={n2}, p={p2})",
             "Probability Mass Function (PMF) of Binomial Distributions")
    plot_cdf(k1, cdf1_scipy, k2, cdf2_scipy,
             f"Binomial(n={n1}, p={p1})", f"Binomial(n={n2}, p={p2})",
             "Cumulative Distribution Function (CDF) of Binomial Distributions")
    plot_pmf(k1, pmf1_scipy, k1, custom1.pmf(k1),
             "scipy.stats", "hand-rolled",
             f"scipy vs hand-rolled PMF, Binomial(n={n1}, p={p1})")


if __name__ == "__main__":
    main()
