import matplotlib.pyplot as plt
import numpy as np


def calculate_variance_and_std_dev(data, ddof=0):
    """
    Calculates the variance and standard deviation of the given data.
    ddof=0 gives the population formulas, ddof=1 the sample formulas.
    """
    variance = np.var(data, ddof=ddof)
    std_dev = np.sqrt(variance)
    return variance, std_dev


def plot_data_with_statistics(data, arithmetic_mean, std_dev):
    """
    Plots the data points, mean, and standard deviation range on a graph.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data, np.zeros_like(data), "o", label="Data Points")
    plt.axvline(
        arithmetic_mean, color="r", linestyle="--", label=f"Mean: {arithmetic_mean:.2f}"
    )
    plt.axvspan(
        arithmetic_mean - std_dev,
        arithmetic_mean + std_dev,
        alpha=0.3,
        color="yellow",
        label=f"Std Dev Range: {std_dev:.2f}",
    )

    plt.text(arithmetic_mean, 0.02, "Mean", rotation=90, color="r")
    plt.text(
        arithmetic_mean - std_dev,
        0.02,
        "-1 Std Dev",
        rotation=90,
        verticalalignment="bottom",
    )
    plt.text(
        arithmetic_mean + std_dev,
        0.02,
        "+1 Std Dev",
        rotation=90,
        verticalalignment="bottom",
    )

    plt.ylim(-0.05, 0.05)
    plt.xlabel("Values")
    plt.yticks([])
    plt.title("Visualization of Variance and Standard Deviation")
    plt.legend()
    plt.show()


def main():
    rng = np.random.default_rng(0)
    data = rng.normal(0, 1, 1000)
    arithmetic_mean = np.mean(data)

    pop_var, pop_std = calculate_variance_and_std_dev(data, ddof=0)
    samp_var, samp_std = calculate_variance_and_std_dev(data, ddof=1)
    print(f"Mean: {arithmetic_mean:.4f}")
    print(f"Population variance / std: {pop_var:.4f} / {pop_std:.4f}")
    print(f"Sample variance / std:     {samp_var:.4f} / {samp_std:.4f}")

    plot_data_with_statistics(data, arithmetic_mean, samp_std)


if __name__ == "__main__":
    main()
