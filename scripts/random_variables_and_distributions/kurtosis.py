"""Sample (excess) kurtosis of normal data: it does not depend on sigma."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis as kurt


def main():
    rng = np.random.default_rng(42)
    sigmas = [1, 2, 3]

    plt.figure(figsize=(8, 5))
    plt.title(r"Kurtosis For Normal Data With Different $\sigma$ Values", fontsize=16)
    for sigma in sigmas:
        x = rng.normal(0, sigma, 1000)
        k = kurt(x)  # excess kurtosis (normal = 0)
        print(f"sigma={sigma}: excess kurtosis = {k:.4f}")
        plt.hist(x, alpha=0.5, label=rf"$\sigma$={sigma}, k={k:.4f}")
    plt.legend(fontsize=14)
    plt.show()


if __name__ == "__main__":
    main()
