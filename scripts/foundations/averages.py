import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def calculate_averages(data, weights):
    """
    Calculates various types of averages for the given data.
    """
    mode_result = stats.mode(data, keepdims=False)
    averages = {
        "arithmetic_mean": np.mean(data),
        "weighted_mean": np.average(data, weights=weights),
        "geometric_mean": stats.gmean(data),
        "median": np.median(data),
        "mode": mode_result.mode,
    }
    return averages


def plot_averages(data, averages):
    """
    Plots the data points and marks various types of averages.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data, np.zeros_like(data), "o", label="Data Points")

    # Plotting each type of average
    for mean_type, value in averages.items():
        plt.axvline(value, label=f"{mean_type.capitalize()}: {value:.2f}")

    # Adding annotations
    for mean_type, value in averages.items():
        plt.text(value, 0.02, mean_type.capitalize(), rotation=90)

    plt.ylim(-0.05, 0.05)
    plt.xlabel("Values")
    plt.yticks([])
    plt.title("Visualization of Different Types of Averages")
    plt.legend()
    plt.show()


def main():
    # Positive data (needed for the geometric mean) with a repeated value
    # so that the mode is meaningful.
    data = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12])
    weights = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])  # arbitrary weights
    averages = calculate_averages(data, weights)
    for name, value in averages.items():
        print(f"{name}: {value:.3f}")
    plot_averages(data, averages)


if __name__ == "__main__":
    main()
