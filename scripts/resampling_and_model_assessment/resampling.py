"""Monte Carlo estimate of the standard error of a sample mean."""

import numpy as np
import matplotlib.pyplot as plt


def monte_carlo_sample_means(population_mean: float, population_std: float,
                             sample_size: int, B: int) -> np.ndarray:
    """Draw B independent samples and return their means."""
    return np.array([
        np.mean(np.random.normal(loc=population_mean, scale=population_std, size=sample_size))
        for _ in range(B)
    ])


def main() -> None:
    population_mean = 100
    population_std = 15
    sample_size = 30
    B = 1000

    np.random.seed(42)
    sample_means = monte_carlo_sample_means(population_mean, population_std, sample_size, B)

    # SE ~ sqrt( sum( (theta_b - theta_bar)^2 ) / (B - 1) )
    theta_bar = np.mean(sample_means)
    standard_error_estimate = np.sqrt(np.sum((sample_means - theta_bar) ** 2) / (B - 1))
    print(f"Estimated Standard Error (Monte Carlo): {standard_error_estimate:.4f}")
    print(f"Theoretical standard error sigma/sqrt(n): {population_std / np.sqrt(sample_size):.4f}")

    plt.figure(figsize=(10, 6))
    plt.hist(sample_means, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.axvline(theta_bar, color='red', linestyle='dashed', linewidth=2,
                label=f"Mean of Sample Means = {theta_bar:.4f}")
    plt.axvline(population_mean, color='green', linestyle='dotted', linewidth=2,
                label=f"Population Mean = {population_mean}")
    plt.title('Distribution of Sample Means (Monte Carlo Simulation)', fontsize=16)
    plt.xlabel('Sample Mean', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
