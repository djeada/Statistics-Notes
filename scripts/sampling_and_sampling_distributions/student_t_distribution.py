"""Student's t density and CDF: hand-built formulas checked against scipy.stats."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.special import betainc, gammaln


class TDistribution:
    """Student's t distribution built from its closed-form density and the
    regularized incomplete beta function."""

    def __init__(self, df):
        self.df = df

    def pdf(self, x):
        x = np.asarray(x, dtype=float)
        v = self.df
        log_coef = gammaln((v + 1) / 2) - gammaln(v / 2) - 0.5 * np.log(v * np.pi)
        return np.exp(log_coef - (v + 1) / 2 * np.log1p(x ** 2 / v))

    def cdf(self, x):
        x = np.asarray(x, dtype=float)
        v = self.df
        tail = 0.5 * betainc(v / 2, 0.5, v / (v + x ** 2))  # P(T > |x|)
        return np.where(x > 0, 1 - tail, tail)


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
    df1, df2 = 5, 10
    x = np.linspace(-5, 5, 1000)
    t1, t2 = TDistribution(df1), TDistribution(df2)

    assert np.allclose(t1.pdf(x), stats.t.pdf(x, df1))
    assert np.allclose(t2.cdf(x), stats.t.cdf(x, df2))
    print(f"t({df2}): variance={stats.t.var(df2):.3f} (nu/(nu-2) = {df2 / (df2 - 2):.3f})")

    plot_curves(x, [(stats.t.pdf(x, df1), f"t(nu={df1}) PDF", "b-"),
                    (stats.t.pdf(x, df2), f"t(nu={df2}) PDF", "r-"),
                    (stats.norm.pdf(x), "N(0,1) PDF", "k:")],
                "PDF", "PDF of t Distributions")
    plot_curves(x, [(stats.t.cdf(x, df1), f"t(nu={df1}) CDF", "b-"),
                    (stats.t.cdf(x, df2), f"t(nu={df2}) CDF", "r-")],
                "CDF", "CDF of t Distributions")
    plot_curves(x, [(stats.t.pdf(x, df1), "scipy.stats", "b--"),
                    (t1.pdf(x), "hand-built formula", "orange")],
                "PDF", f"Theoretical vs Custom PDF, t(nu={df1})")


if __name__ == "__main__":
    main()
