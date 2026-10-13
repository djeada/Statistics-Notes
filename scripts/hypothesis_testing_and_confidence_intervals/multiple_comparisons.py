"""Holm-Bonferroni and Benjamini-Hochberg procedures on a small set of p-values."""

import matplotlib.pyplot as plt
import numpy as np


def holm(p_values: np.ndarray, alpha: float = 0.05):
    """Return (thresholds, reject) for the Holm step-down procedure on sorted p-values."""
    m = len(p_values)
    thresholds = alpha / (m - np.arange(m))  # alpha/m, alpha/(m-1), ..., alpha/1
    passes = p_values <= thresholds
    reject = np.zeros(m, dtype=bool)
    for i in range(m):
        if not passes[i]:
            break  # step-down procedure stops at the first non-rejection
        reject[i] = True
    return thresholds, reject


def benjamini_hochberg(p_values: np.ndarray, alpha: float = 0.05):
    """Return (thresholds, reject) for the BH step-up procedure on sorted p-values."""
    m = len(p_values)
    thresholds = alpha * np.arange(1, m + 1) / m
    below = np.where(p_values <= thresholds)[0]
    reject = np.zeros(m, dtype=bool)
    if below.size:
        reject[: below.max() + 1] = True
    return thresholds, reject


def main() -> None:
    p_values = np.sort(np.array([0.001, 0.008, 0.039, 0.041, 0.042, 0.06]))
    alpha = 0.05
    m = len(p_values)

    holm_thr, holm_reject = holm(p_values, alpha)
    bh_thr, bh_reject = benjamini_hochberg(p_values, alpha)

    print(f"Bonferroni threshold: {alpha / m:.5f}")
    for i, p in enumerate(p_values):
        print(f"Test {i + 1}: p = {p:.3f} | Holm thr = {holm_thr[i]:.5f} "
              f"({'reject' if holm_reject[i] else 'keep'}) | BH thr = {bh_thr[i]:.5f} "
              f"({'reject' if bh_reject[i] else 'keep'})")
    print(f"Holm rejects {holm_reject.sum()} hypotheses; BH rejects {bh_reject.sum()}.")

    ranks = np.arange(1, m + 1)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(ranks, p_values, marker="o", label="Ordered p-values", color="blue")
    ax.plot(ranks, holm_thr, marker="x", linestyle="--", label="Holm thresholds", color="red")
    ax.plot(ranks, bh_thr, marker="s", linestyle=":", label="BH thresholds", color="green")
    ax.set_title("Holm-Bonferroni and Benjamini-Hochberg thresholds")
    ax.set_xlabel("Rank of p-value")
    ax.set_ylabel("p-value / threshold")
    ax.legend()
    ax.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
