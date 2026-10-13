"""Compare biased (divide by n) and unbiased (divide by n - 1) sample variances."""

import matplotlib.pyplot as plt
import numpy as np


def generate_population(rng: np.random.Generator, mean: float, std: float, size: int) -> np.ndarray:
    """Generate a finite population from a normal distribution."""
    return rng.normal(mean, std, size)


def take_sample(
    rng: np.random.Generator, population: np.ndarray, sample_size: int, replace: bool = True
) -> np.ndarray:
    """Take a simple random sample with or without replacement."""
    return rng.choice(population, size=sample_size, replace=replace)


def calculate_variances(sample: np.ndarray) -> dict:
    """Return the biased (ddof=0) and unbiased (ddof=1) sample variances."""
    return {
        "biased": np.var(sample, ddof=0),
        "unbiased": np.var(sample, ddof=1),
    }


def average_variances(
    rng: np.random.Generator, population: np.ndarray, sample_size: int, replications: int
) -> dict:
    """Average both variance estimators over many samples drawn with replacement."""
    biased = np.empty(replications)
    unbiased = np.empty(replications)
    for i in range(replications):
        v = calculate_variances(take_sample(rng, population, sample_size, replace=True))
        biased[i], unbiased[i] = v["biased"], v["unbiased"]
    return {"biased": biased.mean(), "unbiased": unbiased.mean()}


def plot_statistics(means, biased, unbiased, real_mean, real_variance) -> None:
    """Bar charts of one sample's mean and variances against the population values."""
    categories = list(means.keys())
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))

    ax[0].bar(categories, [means[c] for c in categories], color=["tab:blue", "tab:green"], alpha=0.7)
    ax[0].axhline(real_mean, color="red", linestyle="--", label="Population mean")
    ax[0].set_title("Sample means of heights")
    ax[0].set_ylabel("Mean (cm)")
    ax[0].legend()

    ax[1].bar(categories, [biased[c] for c in categories], color=["tab:orange", "tab:purple"], alpha=0.7)
    ax[1].axhline(real_variance, color="red", linestyle="--", label="Population variance")
    ax[1].set_title("Biased sample variances (divisor n)")
    ax[1].set_ylabel("Variance (cm^2)")
    ax[1].legend()

    ax[2].bar(categories, [unbiased[c] for c in categories], color=["tab:cyan", "tab:pink"], alpha=0.7)
    ax[2].axhline(real_variance, color="red", linestyle="--", label="Population variance")
    ax[2].set_title("Unbiased sample variances (divisor n-1)")
    ax[2].set_ylabel("Variance (cm^2)")
    ax[2].legend()

    plt.tight_layout()
    plt.show()


def main() -> None:
    rng = np.random.default_rng(42)

    population = generate_population(rng, mean=170, std=10, size=500)
    sample_size = 20

    means, biased, unbiased = {}, {}, {}
    for label, replace in [("With replacement", True), ("Without replacement", False)]:
        sample = take_sample(rng, population, sample_size, replace=replace)
        variances = calculate_variances(sample)
        means[label] = sample.mean()
        biased[label] = variances["biased"]
        unbiased[label] = variances["unbiased"]

    real_mean = population.mean()
    real_variance = population.var(ddof=0)
    print(f"Population mean: {real_mean:.2f}, population variance: {real_variance:.2f}")
    for label in means:
        print(f"{label}: mean={means[label]:.2f}, biased var={biased[label]:.2f}, unbiased var={unbiased[label]:.2f}")

    averages = average_variances(rng, population, sample_size, replications=5000)
    print(f"Average over 5000 samples (n={sample_size}): "
          f"biased={averages['biased']:.2f}, unbiased={averages['unbiased']:.2f}, "
          f"theory for biased={(sample_size - 1) / sample_size * real_variance:.2f}")

    plot_statistics(means, biased, unbiased, real_mean, real_variance)


if __name__ == "__main__":
    main()
