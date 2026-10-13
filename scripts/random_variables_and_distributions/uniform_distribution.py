"""Uniform distribution: hand-rolled PDF/CDF checked against scipy.stats."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform


class UniformDistribution:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pdf(self, x):
        x = np.asarray(x, dtype=float)
        return np.where((x >= self.a) & (x <= self.b), 1 / (self.b - self.a), 0.0)

    def cdf(self, x):
        x = np.asarray(x, dtype=float)
        return np.clip((x - self.a) / (self.b - self.a), 0.0, 1.0)


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
    a1, b1 = 0, 5
    a2, b2 = 2, 7
    x = np.linspace(-1, 8, 1001)

    # scipy parametrization: loc = a, scale = b - a
    pdf1_scipy, pdf2_scipy = uniform.pdf(x, a1, b1 - a1), uniform.pdf(x, a2, b2 - a2)
    cdf1_scipy, cdf2_scipy = uniform.cdf(x, a1, b1 - a1), uniform.cdf(x, a2, b2 - a2)

    dist1, dist2 = UniformDistribution(a1, b1), UniformDistribution(a2, b2)
    assert np.allclose(dist1.pdf(x), pdf1_scipy) and np.allclose(dist2.pdf(x), pdf2_scipy)
    assert np.allclose(dist1.cdf(x), cdf1_scipy) and np.allclose(dist2.cdf(x), cdf2_scipy)
    print("Custom PDF/CDF match scipy.stats.uniform")
    print(f"Uniform({a1}, {b1}): mean={(a1 + b1) / 2}, var={(b1 - a1) ** 2 / 12:.4f}")

    lab1, lab2 = f"Uniform({a1}, {b1})", f"Uniform({a2}, {b2})"
    plot_curves(x, pdf1_scipy, pdf2_scipy, lab1, lab2,
                "Probability Density Function (PDF) of Uniform Distributions", "PDF")
    plot_curves(x, cdf1_scipy, cdf2_scipy, lab1, lab2,
                "Cumulative Distribution Function (CDF) of Uniform Distributions", "CDF")
    plot_comparison(x, pdf1_scipy, dist1.pdf(x), "scipy.stats", "hand-rolled",
                    f"scipy vs hand-rolled PDF, {lab1}", "PDF")


if __name__ == "__main__":
    main()
