"""Confidence interval for a mean, plus a repeated-sampling coverage check."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem, t


def calculate_confidence_interval(data, confidence: float = 0.95):
    """Return (lower, mean, upper) for a t-based interval for the mean."""
    n = len(data)
    mean = np.mean(data)
    margin_of_error = sem(data) * t.ppf((1 + confidence) / 2, n - 1)
    return mean - margin_of_error, mean, mean + margin_of_error


def coverage(rng: np.random.Generator, true_mean: float, std_dev: float,
             n: int, confidence: float, replications: int) -> float:
    """Fraction of simulated intervals that contain the true mean."""
    hits = 0
    for _ in range(replications):
        lower, _, upper = calculate_confidence_interval(rng.normal(true_mean, std_dev, n), confidence)
        hits += lower <= true_mean <= upper
    return hits / replications


def main() -> None:
    rng = np.random.default_rng(0)
    sample_size, true_mean, std_dev = 100, 50, 5

    data = rng.normal(true_mean, std_dev, sample_size)
    lower, sample_mean, upper = calculate_confidence_interval(data)
    print(f"Sample mean: {sample_mean:.3f}")
    print(f"95% CI: ({lower:.3f}, {upper:.3f})")
    print(f"Empirical coverage over 2000 samples: "
          f"{coverage(rng, true_mean, std_dev, sample_size, 0.95, 2000):.3f}")

    plt.figure(figsize=(10, 4))
    plt.hist(data, bins=15, alpha=0.7, label="Sample data")
    plt.axvline(sample_mean, color="red", linestyle="dashed", linewidth=2, label="Sample mean")
    plt.axvline(lower, color="green", linestyle="dashed", linewidth=2, label="Lower bound of CI")
    plt.axvline(upper, color="blue", linestyle="dashed", linewidth=2, label="Upper bound of CI")
    plt.title("Confidence interval for the mean (95%)")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
