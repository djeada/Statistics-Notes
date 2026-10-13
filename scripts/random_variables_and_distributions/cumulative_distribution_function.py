"""CDFs of a continuous (normal) and a discrete (fair die) random variable."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def plot_single_variable_cdf(x, cdf, title, xlabel, ylabel):
    plt.figure(figsize=(8, 4))
    plt.plot(x, cdf)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def plot_discrete_variable_cdf(x, cdf, title, xlabel, ylabel):
    plt.figure(figsize=(8, 4))
    plt.step(x, cdf, where="post")  # right-continuous: F jumps at each outcome
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(x)
    plt.grid(True)
    plt.show()


def main():
    # Continuous: standard normal
    x_continuous = np.linspace(-5, 5, 1000)
    cdf_continuous = norm.cdf(x_continuous, 0, 1)

    # Discrete: fair six-sided die, F(x) = floor(x) / 6 clipped to [0, 1]
    x_discrete = np.arange(0, 8)
    cdf_discrete = np.clip(np.floor(x_discrete) / 6, 0, 1)
    assert np.isclose(cdf_discrete[3], 0.5)  # P(X <= 3) = 1/2

    plot_single_variable_cdf(x_continuous, cdf_continuous,
                             "Cumulative Distribution Function of a Normal Distribution", "x", "CDF")
    plot_discrete_variable_cdf(x_discrete, cdf_discrete,
                               "Cumulative Distribution Function of a Six-Sided Die", "Outcome", "CDF")


if __name__ == "__main__":
    main()
