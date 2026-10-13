"""Beta distribution: hand-rolled PDF/CDF checked against scipy.stats."""
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta


class BetaDistribution:
    def __init__(self, alpha, beta_param):
        self.alpha = alpha
        self.beta = beta_param

    def pdf(self, x):
        x = np.asarray(x, dtype=float)
        norm = math.gamma(self.alpha) * math.gamma(self.beta) / math.gamma(self.alpha + self.beta)
        return x ** (self.alpha - 1) * (1 - x) ** (self.beta - 1) / norm

    def cdf(self, x):
        """Closed form for integer shapes: P(Binomial(a+b-1, x) >= a)."""
        x = np.asarray(x, dtype=float)
        n = self.alpha + self.beta - 1
        return sum(math.comb(n, j) * x**j * (1 - x) ** (n - j) for j in range(self.alpha, n + 1))


def plot_curves(x, y1, y2, label1, label2, title, ylabel):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label=label1, color="blue")
    plt.plot(x, y2, label=label2, color="red")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_comparison(x, y_scipy, y_custom, label1, label2, title, ylabel):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_scipy, label=label1, color="blue", linestyle="--")
    plt.plot(x, y_custom, label=label2, color="orange")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    alpha1, beta1 = 2, 5
    alpha2, beta2 = 5, 2
    x = np.linspace(0, 1, 1000)

    pdf1_scipy, pdf2_scipy = beta.pdf(x, alpha1, beta1), beta.pdf(x, alpha2, beta2)
    cdf1_scipy, cdf2_scipy = beta.cdf(x, alpha1, beta1), beta.cdf(x, alpha2, beta2)

    dist1, dist2 = BetaDistribution(alpha1, beta1), BetaDistribution(alpha2, beta2)
    assert np.allclose(dist1.pdf(x), pdf1_scipy) and np.allclose(dist2.pdf(x), pdf2_scipy)
    assert np.allclose(dist1.cdf(x), cdf1_scipy) and np.allclose(dist2.cdf(x), cdf2_scipy)
    print("Custom PDF/CDF match scipy.stats.beta")
    print(f"Beta({alpha1}, {beta1}): mean={alpha1 / (alpha1 + beta1):.4f}, "
          f"var={alpha1 * beta1 / ((alpha1 + beta1) ** 2 * (alpha1 + beta1 + 1)):.4f}")

    lab1, lab2 = f"Beta(alpha={alpha1}, beta={beta1})", f"Beta(alpha={alpha2}, beta={beta2})"
    plot_curves(x, pdf1_scipy, pdf2_scipy, lab1, lab2,
                "Probability Density Function (PDF) of Beta Distributions", "PDF")
    plot_curves(x, cdf1_scipy, cdf2_scipy, lab1, lab2,
                "Cumulative Distribution Function (CDF) of Beta Distributions", "CDF")
    plot_comparison(x, pdf1_scipy, dist1.pdf(x), "scipy.stats", "hand-rolled",
                    f"scipy vs hand-rolled PDF, {lab1}", "PDF")


if __name__ == "__main__":
    main()
