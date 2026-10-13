"""F density and CDF: hand-built formulas checked against scipy.stats."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.special import betainc, betaln


class FDistribution:
    """F distribution built from its closed-form density and the regularized
    incomplete beta function."""

    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def pdf(self, x):
        x = np.asarray(x, dtype=float)
        a, b = self.d1 / 2, self.d2 / 2
        out = np.zeros_like(x)
        pos = x > 0
        xp = x[pos]
        log_pdf = (a * np.log(self.d1 / self.d2) + (a - 1) * np.log(xp)
                   - (a + b) * np.log1p(self.d1 * xp / self.d2) - betaln(a, b))
        out[pos] = np.exp(log_pdf)
        return out

    def cdf(self, x):
        x = np.asarray(x, dtype=float)
        return betainc(self.d1 / 2, self.d2 / 2, self.d1 * x / (self.d1 * x + self.d2))


def plot_curves(x, curves, ylabel, title):
    """Plot several (values, label, style) curves against ``x``."""
    plt.figure(figsize=(10, 6))
    for values, label, style in curves:
        plt.plot(x, values, style, label=label)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()


def main() -> None:
    d1_1, d2_1 = 5, 10
    d1_2, d2_2 = 10, 5
    x = np.linspace(0, 5, 1000)
    f1, f2 = FDistribution(d1_1, d2_1), FDistribution(d1_2, d2_2)

    assert np.allclose(f1.pdf(x), stats.f.pdf(x, d1_1, d2_1))
    assert np.allclose(f2.cdf(x), stats.f.cdf(x, d1_2, d2_2))
    print(f"F({d1_1},{d2_1}): mean={stats.f.mean(d1_1, d2_1):.3f}")

    plot_curves(x, [(stats.f.pdf(x, d1_1, d2_1), f"F({d1_1}, {d2_1}) PDF", "b-"),
                    (stats.f.pdf(x, d1_2, d2_2), f"F({d1_2}, {d2_2}) PDF", "r-")],
                "PDF", "PDF of F Distributions")
    plot_curves(x, [(stats.f.cdf(x, d1_1, d2_1), f"F({d1_1}, {d2_1}) CDF", "b-"),
                    (stats.f.cdf(x, d1_2, d2_2), f"F({d1_2}, {d2_2}) CDF", "r-")],
                "CDF", "CDF of F Distributions")
    plot_curves(x, [(stats.f.pdf(x, d1_1, d2_1), "scipy.stats", "b--"),
                    (f1.pdf(x), "hand-built formula", "orange")],
                "PDF", f"Theoretical vs Custom PDF, F({d1_1}, {d2_1})")


if __name__ == "__main__":
    main()
