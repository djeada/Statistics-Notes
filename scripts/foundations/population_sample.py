import matplotlib.pyplot as plt
import numpy as np


def draw_sample(population, sample_size, rng):
    """Draws a simple random sample without replacement."""
    return rng.choice(population, size=sample_size, replace=False)


def main():
    rng = np.random.default_rng(42)

    # Population data (e.g., heights in inches)
    population_data = np.array(
        [68, 70, 72, 66, 74, 71, 69, 75, 73, 67, 70, 72, 68, 70, 71, 69, 72, 74, 68, 70]
    )
    sample = draw_sample(population_data, sample_size=5, rng=rng)

    # Parameters use the population formulas (ddof=0); the sample statistics
    # use n - 1 (ddof=1), as in the note.
    print("Population mean (mu):", population_data.mean())
    print("Population std (sigma):", population_data.std(ddof=0))
    print("Sample mean (x-bar):", sample.mean())
    print("Sample std (s):", sample.std(ddof=1))
    print("Sample variance (s^2):", sample.var(ddof=1))

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.hist(population_data, bins=10, edgecolor="black", alpha=0.7)
    plt.title("Population Data")
    plt.xlabel("Height (inches)")
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    plt.hist(sample, bins=5, edgecolor="black", alpha=0.7, color="green")
    plt.title("Random Sample")
    plt.xlabel("Height (inches)")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
