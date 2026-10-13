"""Negative binomial (trial of the r-th success): hand-rolled PMF/CDF vs scipy.stats."""
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import nbinom


class NegativeBinomialDistribution:
    """X = total number of trials needed for r successes, X in {r, r+1, ...}.

    scipy.stats.nbinom counts failures Y = X - r instead.
    """

    def __init__(self, r, p):
        self.r = r
        self.p = p

    def pmf(self, k):
        k = np.asarray(k)
        return np.array([
            math.comb(int(i) - 1, self.r - 1) * self.p**self.r * (1 - self.p) ** (i - self.r)
            if i >= self.r else 0.0
            for i in k.ravel()
        ]).reshape(k.shape)

    def cdf(self, k):
        k = np.asarray(k)
        grid = np.arange(self.r, int(k.max()) + 1)
        cum = np.cumsum(self.pmf(grid))
        return np.array([cum[int(i) - self.r] if i >= self.r else 0.0 for i in k.ravel()]).reshape(k.shape)


def plot_pmf(x1, y1, x2, y2, label1, label2, title):
    plt.figure(figsize=(10, 6))
    plt.stem(x1, y1, basefmt=" ", linefmt="blue", markerfmt="bo", label=label1)
    plt.stem(x2, y2, basefmt=" ", linefmt="red", markerfmt="ro", label=label2)
    plt.title(title)
    plt.xlabel("Number of trials (k)")
    plt.ylabel("PMF")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_cdf(x1, y1, x2, y2, label1, label2, title):
    plt.figure(figsize=(10, 6))
    plt.step(x1, y1, where="post", label=label1, color="blue")
    plt.step(x2, y2, where="post", label=label2, color="red")
    plt.title(title)
    plt.xlabel("Number of trials (k)")
    plt.ylabel("CDF")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    r1, p1 = 5, 0.5
    r2, p2 = 3, 0.7
    k1 = np.arange(r1, r1 + 30)
    k2 = np.arange(r2, r2 + 30)

    custom1, custom2 = NegativeBinomialDistribution(r1, p1), NegativeBinomialDistribution(r2, p2)
    # Shift by r: scipy counts failures before the r-th success.
    pmf1_scipy, pmf2_scipy = nbinom.pmf(k1 - r1, r1, p1), nbinom.pmf(k2 - r2, r2, p2)
    cdf1_scipy, cdf2_scipy = nbinom.cdf(k1 - r1, r1, p1), nbinom.cdf(k2 - r2, r2, p2)

    assert np.allclose(custom1.pmf(k1), pmf1_scipy) and np.allclose(custom2.pmf(k2), pmf2_scipy)
    assert np.allclose(custom1.cdf(k1), cdf1_scipy) and np.allclose(custom2.cdf(k2), cdf2_scipy)
    print("Custom PMF/CDF match scipy.stats.nbinom (shifted by r)")
    for r, p in ((r1, p1), (r2, p2)):
        print(f"NegBinomial(r={r}, p={p}): mean={r / p:.3f}, var={r * (1 - p) / p**2:.3f}")

    plot_pmf(k1, pmf1_scipy, k2, pmf2_scipy,
             f"NegBinomial(r={r1}, p={p1})", f"NegBinomial(r={r2}, p={p2})",
             "Probability Mass Function (PMF) of Negative Binomial Distributions")
    plot_cdf(k1, cdf1_scipy, k2, cdf2_scipy,
             f"NegBinomial(r={r1}, p={p1})", f"NegBinomial(r={r2}, p={p2})",
             "Cumulative Distribution Function (CDF) of Negative Binomial Distributions")
    plot_pmf(k1, pmf1_scipy, k1, custom1.pmf(k1), "scipy.stats", "hand-rolled",
             f"scipy vs hand-rolled PMF, NegBinomial(r={r1}, p={p1})")


if __name__ == "__main__":
    main()
