import numpy as np
import matplotlib.pyplot as plt

def calculate_variance_and_std_dev(data):
    """
    Calculates the variance and standard deviation of the given data.
    """
    variance = np.var(data)
    std_dev = np.sqrt(variance)
    return variance, std_dev

def plot_data_with_statistics(data, arithmetic_mean, std_dev):
    """
    Plots the data points, mean, and standard deviation range on a graph.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data, np.zeros_like(data), 'o', label='Data Points')
    plt.axvline(arithmetic_mean, color='r', linestyle='--', label=f'Mean: {arithmetic_mean:.2f}')
    plt.axvspan(arithmetic_mean - std_dev, arithmetic_mean + std_dev, alpha=0.3, color='yellow', label=f'Std Dev Range: {std_dev:.2f}')

    plt.text(arithmetic_mean, 0.02, 'Mean', rotation=90, color='r')
    plt.text(arithmetic_mean - std_dev, 0.02, '-1 Std Dev', rotation=90, verticalalignment='bottom')
    plt.text(arithmetic_mean + std_dev, 0.02, '+1 Std Dev', rotation=90, verticalalignment='bottom')

    plt.ylim(-0.05, 0.05)
    plt.xlabel('Values')
    plt.yticks([])
    plt.title('Visualization of Variance and Standard Deviation')
    plt.legend()
    plt.show()

# Example usage
data = np.random.normal(0, 1, 1000)  # Example data
arithmetic_mean = np.mean(data)
variance, std_dev = calculate_variance_and_std_dev(data)
plot_data_with_statistics(data, arithmetic_mean, std_dev)
