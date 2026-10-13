"""Log-normal distribution: hand-rolled PDF/CDF checked against scipy.stats."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf
from scipy.stats import lognorm


class LogNormalDistribution:
    """X = exp(Y) with Y ~ N(mu, sigma^2)."""

    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def pdf(self, x):
        x = np.asarray(x, dtype=float)
        prefactor = 1 / (x * self.sigma * np.sqrt(2 * np.pi))
        return prefactor * np.exp(-((np.log(x) - self.mu) ** 2) / (2 * self.sigma**2))

    def cdf(self, x):
        x = np.asarray(x, dtype=float)
        return 0.5 * (1 + erf((np.log(x) - self.mu) / (self.sigma * np.sqrt(2))))

    def mean(self):
        return np.exp(self.mu + self.sigma**2 / 2)

    def var(self):
        return (np.exp(self.sigma**2) - 1) * np.exp(2 * self.mu + self.sigma**2)


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
    mu1, sigma1 = 0.0, 0.5
    mu2, sigma2 = 0.0, 1.0
    x = np.linspace(0.01, 5, 1000)

    # scipy parametrization: shape = sigma, scale = exp(mu)
    pdf1_scipy, pdf2_scipy = lognorm.pdf(x, sigma1, scale=np.exp(mu1)), lognorm.pdf(x, sigma2, scale=np.exp(mu2))
    cdf1_scipy, cdf2_scipy = lognorm.cdf(x, sigma1, scale=np.exp(mu1)), lognorm.cdf(x, sigma2, scale=np.exp(mu2))

    dist1, dist2 = LogNormalDistribution(mu1, sigma1), LogNormalDistribution(mu2, sigma2)
    assert np.allclose(dist1.pdf(x), pdf1_scipy) and np.allclose(dist2.pdf(x), pdf2_scipy)
    assert np.allclose(dist1.cdf(x), cdf1_scipy) and np.allclose(dist2.cdf(x), cdf2_scipy)
    assert np.isclose(dist1.mean(), lognorm.mean(sigma1, scale=np.exp(mu1)))
    assert np.isclose(dist1.var(), lognorm.var(sigma1, scale=np.exp(mu1)))
    print("Custom PDF/CDF/mean/var match scipy.stats.lognorm")
    print(f"LogNormal(mu={mu1}, sigma={sigma1}): mean={dist1.mean():.4f}, var={dist1.var():.4f}")

    lab1 = f"LogNormal(mu={mu1}, sigma={sigma1})"
    lab2 = f"LogNormal(mu={mu2}, sigma={sigma2})"
    plot_curves(x, pdf1_scipy, pdf2_scipy, lab1, lab2,
                "Probability Density Function (PDF) of Log-Normal Distributions", "PDF")
    plot_curves(x, cdf1_scipy, cdf2_scipy, lab1, lab2,
                "Cumulative Distribution Function (CDF) of Log-Normal Distributions", "CDF")
    plot_comparison(x, pdf1_scipy, dist1.pdf(x), "scipy.stats", "hand-rolled",
                    f"scipy vs hand-rolled PDF, {lab1}", "PDF")


if __name__ == "__main__":
    main()
