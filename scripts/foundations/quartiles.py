import matplotlib.pyplot as plt
import numpy as np


def plot_data_boxplots(datasets, titles, figsize=(10, 8)):
    """
    Plots a series of boxplots for given datasets.
    """
    fig, axs = plt.subplots(len(datasets), 1, figsize=figsize)

    for idx, data in enumerate(datasets):
        axs[idx].boxplot(data, vert=False)
        axs[idx].set_title(titles[idx])

    plt.tight_layout()
    plt.show()


# Define datasets
data1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 100, 110, 120])  # Wide range in 4th quartile
data2 = np.array([1, 2, 50, 60, 70, 80, 90, 100, 101, 102])  # Wide interquartile range
data3 = np.array([50, 51, 52, 53, 54, 55, 56, 57, 58, 59])  # Narrow interquartile range
data4 = np.array([1, 1, 2, 2, 3, 3, 4, 4, 50, 100])  # Data with outliers

# Titles for each dataset
titles = [
    "Wide Range in 4th Quartile",
    "Wide Interquartile Range",
    "Narrow Interquartile Range",
    "Data with Outliers",
]

# Plot the boxplots
plot_data_boxplots([data1, data2, data3, data4], titles)
