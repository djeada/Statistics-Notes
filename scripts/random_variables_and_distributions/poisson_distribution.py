"""Poisson distribution: hand-rolled PMF/CDF checked against scipy.stats."""
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson


class PoissonDistribution:
    def __init__(self, lam):
        self.lam = lam

    def pmf(self, k):
        k = np.asarray(k)
        return np.array([self.lam**i * math.exp(-self.lam) / math.factorial(int(i))
                         for i in k.ravel()]).reshape(k.shape)

    def cdf(self, k):
        k = np.asarray(k)
        cum = np.cumsum(self.pmf(np.arange(int(k.max()) + 1)))
        return cum[k.astype(int)]


def plot_pmf(x, y1, y2, label1, label2, title):
    plt.figure(figsize=(10, 6))
    plt.stem(x, y1, basefmt=" ", linefmt="blue", markerfmt="bo", label=label1)
    plt.stem(x, y2, basefmt=" ", linefmt="red", markerfmt="ro", label=label2)
    plt.title(title)
    plt.xlabel("Number of events (k)")
    plt.ylabel("PMF")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_cdf(x, y1, y2, label1, label2, title):
    plt.figure(figsize=(10, 6))
    plt.step(x, y1, where="post", label=label1, color="blue")
    plt.step(x, y2, where="post", label=label2, color="red")
    plt.title(title)
    plt.xlabel("Number of events (k)")
    plt.ylabel("CDF")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    lambda1, lambda2 = 3, 5
    k = np.arange(0, 15)

    custom1, custom2 = PoissonDistribution(lambda1), PoissonDistribution(lambda2)
    pmf1_scipy, pmf2_scipy = poisson.pmf(k, lambda1), poisson.pmf(k, lambda2)
    cdf1_scipy, cdf2_scipy = poisson.cdf(k, lambda1), poisson.cdf(k, lambda2)

    assert np.allclose(custom1.pmf(k), pmf1_scipy) and np.allclose(custom2.pmf(k), pmf2_scipy)
    assert np.allclose(custom1.cdf(k), cdf1_scipy) and np.allclose(custom2.cdf(k), cdf2_scipy)
    print("Custom PMF/CDF match scipy.stats.poisson")
    print(f"P(X=3 | lambda=5) = {custom2.pmf(3):.4f}, P(X>7 | lambda=5) = {1 - custom2.cdf(7):.4f}")

    plot_pmf(k, pmf1_scipy, pmf2_scipy, f"Poisson(lambda={lambda1})", f"Poisson(lambda={lambda2})",
             "Probability Mass Function (PMF) of Poisson Distributions")
    plot_cdf(k, cdf1_scipy, cdf2_scipy, f"Poisson(lambda={lambda1})", f"Poisson(lambda={lambda2})",
             "Cumulative Distribution Function (CDF) of Poisson Distributions")
    plot_pmf(k, pmf1_scipy, custom1.pmf(k), "scipy.stats", "hand-rolled",
             f"scipy vs hand-rolled PMF, Poisson(lambda={lambda1})")


if __name__ == "__main__":
    main()
