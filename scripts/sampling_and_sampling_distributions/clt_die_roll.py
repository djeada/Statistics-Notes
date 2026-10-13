"""CLT for a fair die: sample means for several sample sizes versus normal curves."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def sample_means(rng, sides, size, replications=1000):
    """Return ``replications`` sample means, each from ``size`` die rolls."""
    return rng.choice(sides, size=(replications, size)).mean(axis=1)


def main() -> None:
    rng = np.random.default_rng(0)
    die_sides = np.arange(1, 7)
    sample_sizes = [2, 4, 8, 16, 32]
    sigma = die_sides.std()  # population standard deviation, sqrt(35/12)

    for size in sample_sizes:
        means = sample_means(rng, die_sides, size)
        mean, std = means.mean(), means.std(ddof=1)
        print(f"n={size:2d}  mean of means={mean:.3f}  "
              f"empirical SE={std:.3f}  sigma/sqrt(n)={sigma / np.sqrt(size):.3f}")
        x = np.linspace(means.min(), means.max(), 100)
        plt.plot(x, norm.pdf(x, mean, std), label=f"Sample Size = {size}")

    plt.title("Die Roll CLT Sample Size Variation")
    plt.xlabel("Sample Means")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
