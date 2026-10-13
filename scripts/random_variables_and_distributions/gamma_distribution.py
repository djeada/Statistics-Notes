"""Gamma distribution (shape alpha, rate beta): hand-rolled PDF/CDF vs scipy.stats."""
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.stats import gamma


class GammaDistribution:
    def __init__(self, alpha, beta):
        self.alpha = alpha  # shape
        self.beta = beta    # rate (scipy's scale = 1 / beta)

    def pdf(self, x):
        x = np.asarray(x, dtype=float)
        coef = self.beta**self.alpha / math.gamma(self.alpha)
        return np.where(x >= 0, coef * x ** (self.alpha - 1) * np.exp(-self.beta * x), 0.0)

    def cdf(self, x):
        """Numerical integral of the PDF (no closed form); x must be a sorted grid from 0."""
        x = np.asarray(x, dtype=float)
        return cumulative_trapezoid(self.pdf(x), x, initial=0.0)


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
    alpha1, beta1 = 2, 2
    alpha2, beta2 = 5, 1
    x = np.linspace(0, 20, 4001)

    pdf1_scipy, pdf2_scipy = gamma.pdf(x, alpha1, scale=1 / beta1), gamma.pdf(x, alpha2, scale=1 / beta2)
    cdf1_scipy, cdf2_scipy = gamma.cdf(x, alpha1, scale=1 / beta1), gamma.cdf(x, alpha2, scale=1 / beta2)

    dist1, dist2 = GammaDistribution(alpha1, beta1), GammaDistribution(alpha2, beta2)
    assert np.allclose(dist1.pdf(x), pdf1_scipy) and np.allclose(dist2.pdf(x), pdf2_scipy)
    assert np.allclose(dist1.cdf(x), cdf1_scipy, atol=1e-4)
    assert np.allclose(dist2.cdf(x), cdf2_scipy, atol=1e-4)
    print("Custom PDF matches scipy.stats.gamma; numerically integrated CDF within 1e-4")
    print(f"Gamma({alpha1}, rate={beta1}): mean={alpha1 / beta1}, var={alpha1 / beta1**2}")

    lab1 = f"Gamma(alpha={alpha1}, beta={beta1})"
    lab2 = f"Gamma(alpha={alpha2}, beta={beta2})"
    plot_curves(x, pdf1_scipy, pdf2_scipy, lab1, lab2,
                "Probability Density Function (PDF) of Gamma Distributions", "PDF")
    plot_curves(x, cdf1_scipy, cdf2_scipy, lab1, lab2,
                "Cumulative Distribution Function (CDF) of Gamma Distributions", "CDF")
    plot_comparison(x, pdf1_scipy, dist1.pdf(x), "scipy.stats", "hand-rolled",
                    f"scipy vs hand-rolled PDF, {lab1}", "PDF")


if __name__ == "__main__":
    main()
