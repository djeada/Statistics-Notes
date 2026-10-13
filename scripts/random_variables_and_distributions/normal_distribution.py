"""Normal distribution: hand-rolled PDF/CDF checked against scipy.stats."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf
from scipy.stats import norm


class NormalDistribution:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def pdf(self, x):
        x = np.asarray(x, dtype=float)
        return np.exp(-0.5 * ((x - self.mu) / self.sigma) ** 2) / (self.sigma * np.sqrt(2 * np.pi))

    def cdf(self, x):
        x = np.asarray(x, dtype=float)
        return 0.5 * (1 + erf((x - self.mu) / (self.sigma * np.sqrt(2))))


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
    mu1, sigma1 = 0, 1
    mu2, sigma2 = 2, 1.5
    x = np.linspace(-5, 7, 1000)

    pdf1_scipy, pdf2_scipy = norm.pdf(x, mu1, sigma1), norm.pdf(x, mu2, sigma2)
    cdf1_scipy, cdf2_scipy = norm.cdf(x, mu1, sigma1), norm.cdf(x, mu2, sigma2)

    dist1, dist2 = NormalDistribution(mu1, sigma1), NormalDistribution(mu2, sigma2)
    assert np.allclose(dist1.pdf(x), pdf1_scipy) and np.allclose(dist2.pdf(x), pdf2_scipy)
    assert np.allclose(dist1.cdf(x), cdf1_scipy) and np.allclose(dist2.cdf(x), cdf2_scipy)
    print("Custom PDF/CDF match scipy.stats.norm")
    print(f"P(|Z| < 1.96) = {dist1.cdf(1.96) - dist1.cdf(-1.96):.4f}")

    lab1 = f"Normal(mu={mu1}, sigma={sigma1})"
    lab2 = f"Normal(mu={mu2}, sigma={sigma2})"
    plot_curves(x, pdf1_scipy, pdf2_scipy, lab1, lab2,
                "Probability Density Function (PDF) of Normal Distributions", "PDF")
    plot_curves(x, cdf1_scipy, cdf2_scipy, lab1, lab2,
                "Cumulative Distribution Function (CDF) of Normal Distributions", "CDF")
    plot_comparison(x, pdf1_scipy, dist1.pdf(x), "scipy.stats", "hand-rolled",
                    f"scipy vs hand-rolled PDF, {lab1}", "PDF")


if __name__ == "__main__":
    main()
