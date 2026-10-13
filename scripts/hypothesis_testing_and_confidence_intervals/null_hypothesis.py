"""Rejection regions and an observed test statistic under a normal null distribution."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def calculate_critical_value(alpha: float = 0.05) -> float:
    """Critical value of a two-tailed z test."""
    return norm.ppf(1 - alpha / 2)


def plot_null_hypothesis(ax, sample_statistic: float, critical_value: float) -> None:
    """Plot the null distribution, rejection regions, and the observed statistic."""
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x)

    ax.plot(x, y, color="green", label="Null distribution")
    ax.axvline(-critical_value, color="blue", linestyle="dashed", linewidth=2,
               label=f"Critical value\n{-critical_value:.2f}")
    ax.axvline(critical_value, color="blue", linestyle="dashed", linewidth=2,
               label=f"Critical value\n{critical_value:.2f}")
    ax.fill_between(x, 0, y, where=(x < -critical_value) | (x > critical_value),
                    color="orange", alpha=0.5, label="Rejection region")
    ax.axvline(sample_statistic, color="red", linestyle="dashed", linewidth=2)
    ax.text(sample_statistic, 0.02, f"Sample statistic\n{sample_statistic:.2f}",
            horizontalalignment="center", color="red",
            bbox=dict(facecolor="none", edgecolor="red", boxstyle="round,pad=0.5"))
    ax.set_title("Null distribution and rejection regions")
    ax.set_xlabel("Test statistic")
    ax.set_ylabel("Probability density")
    ax.legend()


def main() -> None:
    alpha = 0.05
    sample_statistic = 2.0

    critical_value = calculate_critical_value(alpha)
    p_value = 2 * norm.sf(abs(sample_statistic))
    print(f"Critical value: +/-{critical_value:.3f}")
    print(f"Two-tailed p-value for z = {sample_statistic}: {p_value:.4f}")

    fig, ax = plt.subplots(figsize=(10, 5))
    plot_null_hypothesis(ax, sample_statistic, critical_value)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
