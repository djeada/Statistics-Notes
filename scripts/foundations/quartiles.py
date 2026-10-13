import matplotlib.pyplot as plt
import numpy as np


def plot_data_boxplots(datasets, titles, figsize=(10, 8)):
    """
    Plots a series of horizontal boxplots for given datasets.
    """
    _, axs = plt.subplots(len(datasets), 1, figsize=figsize)

    for ax, data, title in zip(axs, datasets, titles):
        try:
            ax.boxplot(data, orientation="horizontal")
        except TypeError:  # Matplotlib < 3.10
            ax.boxplot(data, vert=False)
        ax.set_title(title)

    plt.tight_layout()
    plt.show()


def main():
    data1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 100, 110, 120])  # Wide range in 4th quartile
    data2 = np.array([1, 2, 50, 60, 70, 80, 90, 100, 101, 102])  # Wide interquartile range
    data3 = np.array([50, 51, 52, 53, 54, 55, 56, 57, 58, 59])  # Narrow interquartile range
    data4 = np.array([1, 1, 2, 2, 3, 3, 4, 4, 50, 100])  # Data with outliers

    titles = [
        "Wide Range in 4th Quartile",
        "Wide Interquartile Range",
        "Narrow Interquartile Range",
        "Data with Outliers",
    ]
    datasets = [data1, data2, data3, data4]

    for title, data in zip(titles, datasets):
        q1, q2, q3 = np.percentile(data, [25, 50, 75])
        print(f"{title}: Q1={q1}, median={q2}, Q3={q3}, IQR={q3 - q1}")

    plot_data_boxplots(datasets, titles)


if __name__ == "__main__":
    main()
