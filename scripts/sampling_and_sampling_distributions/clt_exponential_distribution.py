"""CLT demo: means of samples from a skewed exponential population."""

import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    rng = np.random.default_rng(0)
    n_samples = 1000
    sample_size = 50

    population_data = rng.exponential(scale=1.0, size=10000)
    sample_means = rng.choice(population_data, size=(n_samples, sample_size),
                              replace=True).mean(axis=1)

    plt.figure(figsize=(10, 6))
    plt.hist(sample_means, bins=30, color="blue", edgecolor="black", alpha=0.7)
    plt.axvline(population_data.mean(), color="red", linestyle="dashed", linewidth=2)
    plt.title("Distribution of Sample Means (Central Limit Theorem)")
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")
    plt.show()

    print(f"Population mean:        {population_data.mean():.4f}")
    print(f"Mean of sample means:   {sample_means.mean():.4f}")
    print(f"Empirical SE:           {sample_means.std(ddof=1):.4f}")
    print(f"Theoretical SE:         {population_data.std() / np.sqrt(sample_size):.4f}")


if __name__ == "__main__":
    main()
