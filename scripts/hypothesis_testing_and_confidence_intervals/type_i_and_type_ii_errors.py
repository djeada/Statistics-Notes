"""Illustrate Type I and Type II errors, and estimate both rates by simulation."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind


def rejection_rate(rng: np.random.Generator, mean_difference: float, std: float,
                   n: int, alpha: float, replications: int) -> float:
    """Fraction of simulated two-sample t-tests that reject H0."""
    rejections = 0
    for _ in range(replications):
        control = rng.normal(100, std, n)
        experimental = rng.normal(100 + mean_difference, std, n)
        rejections += ttest_ind(control, experimental).pvalue <= alpha
    return rejections / replications


def plot_groups(control, experimental, title: str) -> None:
    plt.figure(figsize=(10, 5))
    plt.hist(control, alpha=0.7, label="Control group")
    plt.hist(experimental, alpha=0.7, label="Experimental group")
    plt.axvline(np.mean(control), color="blue", linestyle="dashed", linewidth=2)
    plt.axvline(np.mean(experimental), color="orange", linestyle="dashed", linewidth=2)
    plt.title(title)
    plt.legend()
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


def main() -> None:
    rng = np.random.default_rng(0)
    n, std, alpha = 100, 10, 0.05

    # One example when H0 is true (a rejection here would be a Type I error).
    control = rng.normal(100, std, n)
    same = rng.normal(100, std, n)
    p_null = ttest_ind(control, same).pvalue
    plot_groups(control, same, f"H0 true: equal means (p-value: {p_null:.2f})")

    # One example when H0 is false (failing to reject would be a Type II error).
    shifted = rng.normal(110, std, n)
    p_alt = ttest_ind(control, shifted).pvalue
    plot_groups(control, shifted, f"H0 false: mean shifted by 10 (p-value: {p_alt:.2g})")

    # Repeat many times to estimate the error rates.
    type_i = rejection_rate(rng, 0, std, n, alpha, 2000)
    print(f"Type I error rate with n={n} per group: {type_i:.3f} (alpha = {alpha})")
    for n_small in (10, 20, 100):
        power = rejection_rate(rng, 10, std, n_small, alpha, 2000)
        print(f"Power for a shift of 10 with n={n_small} per group: {power:.3f} "
              f"(Type II error rate {1 - power:.3f})")


if __name__ == "__main__":
    main()
