"""Chi-square density and CDF: hand-built formulas checked against scipy.stats."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.special import gammainc, gammaln


class ChiSquareDistribution:
    """Chi-square distribution built from its closed-form density and the
    regularized lower incomplete gamma function."""

    def __init__(self, df):
        self.df = df

    def pdf(self, x):
        x = np.asarray(x, dtype=float)
        k = self.df / 2
        coef = 1.0 / (2 ** k * np.exp(gammaln(k)))
        with np.errstate(divide="ignore"):
            out = coef * np.power(x, k - 1) * np.exp(-x / 2)
        return np.where(x >= 0, out, 0.0)

    def cdf(self, x):
        return gammainc(self.df / 2, np.asarray(x, dtype=float) / 2)


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
    df1, df2 = 2, 5
    x = np.linspace(0, 20, 1000)
    d1, d2 = ChiSquareDistribution(df1), ChiSquareDistribution(df2)

    # The hand-built formulas should agree with scipy.stats.
    assert np.allclose(d1.pdf(x), stats.chi2.pdf(x, df1))
    assert np.allclose(d2.cdf(x), stats.chi2.cdf(x, df2))
    print(f"Chi-square({df2}): mean={stats.chi2.mean(df2)}, var={stats.chi2.var(df2)}")

    plot_curves(x, [(stats.chi2.pdf(x, df1), f"Chi-Square(k={df1}) PDF", "b-"),
                    (stats.chi2.pdf(x, df2), f"Chi-Square(k={df2}) PDF", "r-")],
                "PDF", "PDF of Chi-Square Distributions")
    plot_curves(x, [(stats.chi2.cdf(x, df1), f"Chi-Square(k={df1}) CDF", "b-"),
                    (stats.chi2.cdf(x, df2), f"Chi-Square(k={df2}) CDF", "r-")],
                "CDF", "CDF of Chi-Square Distributions")
    plot_curves(x, [(stats.chi2.pdf(x, df1), "scipy.stats", "b--"),
                    (d1.pdf(x), "hand-built formula", "orange")],
                "PDF", f"Theoretical vs Custom PDF, Chi-Square(k={df1})")


if __name__ == "__main__":
    main()
