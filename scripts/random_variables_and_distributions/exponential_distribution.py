"""Exponential distribution: hand-rolled PDF/CDF checked against scipy.stats."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon


class ExponentialDistribution:
    def __init__(self, rate):
        self.rate = rate

    def pdf(self, x):
        x = np.asarray(x, dtype=float)
        return np.where(x >= 0, self.rate * np.exp(-self.rate * x), 0.0)

    def cdf(self, x):
        x = np.asarray(x, dtype=float)
        return np.where(x >= 0, 1 - np.exp(-self.rate * x), 0.0)


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
    lambda1, lambda2 = 0.5, 1.5
    x = np.linspace(0, 10, 1000)

    # scipy uses scale = 1 / rate
    pdf1_scipy, pdf2_scipy = expon.pdf(x, scale=1 / lambda1), expon.pdf(x, scale=1 / lambda2)
    cdf1_scipy, cdf2_scipy = expon.cdf(x, scale=1 / lambda1), expon.cdf(x, scale=1 / lambda2)

    dist1, dist2 = ExponentialDistribution(lambda1), ExponentialDistribution(lambda2)
    assert np.allclose(dist1.pdf(x), pdf1_scipy) and np.allclose(dist2.pdf(x), pdf2_scipy)
    assert np.allclose(dist1.cdf(x), cdf1_scipy) and np.allclose(dist2.cdf(x), cdf2_scipy)
    print("Custom PDF/CDF match scipy.stats.expon")
    print(f"Exp({lambda1}): mean={1 / lambda1}, var={1 / lambda1**2}, "
          f"P(X>2)={1 - dist1.cdf(2.0):.4f}")

    lab1, lab2 = f"Exponential(lambda={lambda1})", f"Exponential(lambda={lambda2})"
    plot_curves(x, pdf1_scipy, pdf2_scipy, lab1, lab2,
                "Probability Density Function (PDF) of Exponential Distributions", "PDF")
    plot_curves(x, cdf1_scipy, cdf2_scipy, lab1, lab2,
                "Cumulative Distribution Function (CDF) of Exponential Distributions", "CDF")
    plot_comparison(x, pdf1_scipy, dist1.pdf(x), "scipy.stats", "hand-rolled",
                    f"scipy vs hand-rolled PDF, {lab1}", "PDF")


if __name__ == "__main__":
    main()
