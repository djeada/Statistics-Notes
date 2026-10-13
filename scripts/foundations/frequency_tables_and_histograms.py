import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_frequency_table(data):
    """
    Takes a list of data points and returns a frequency table with relative
    and cumulative relative frequencies as a pandas DataFrame.
    """
    frequency = pd.Series(data).value_counts().sort_index()

    table = frequency.reset_index()
    table.columns = ["Value", "Frequency"]
    table["Relative Frequency"] = table["Frequency"] / table["Frequency"].sum()
    table["Cumulative Relative Frequency"] = table["Relative Frequency"].cumsum()
    return table


def plot_bar_chart(frequency_table):
    """
    Plots a bar chart of a frequency table.
    """
    plt.figure()
    plt.bar(frequency_table["Value"], frequency_table["Frequency"])
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Bar Chart of Frequencies")
    plt.show()


def plot_histogram(data, bins):
    """
    Plots a histogram for continuous data with the given bin edges.
    """
    plt.figure()
    plt.hist(data, bins=bins, edgecolor="black")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of Data")
    plt.show()


def main():
    # Discrete data
    data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    freq_table = create_frequency_table(data)
    print("Frequency Table:")
    print(freq_table)
    plot_bar_chart(freq_table)

    # Continuous data grouped into half-open bins [a, b) as in the note.
    # np.histogram treats all bins except the last as half-open; the last
    # bin is closed, which does not matter here (no value equals 177).
    heights = [170.2, 165.5, 172.3, 168.7, 171.6, 167.4, 169.5, 174.2, 166.1, 173.5]
    bin_edges = [165, 168, 171, 174, 177]
    counts, _ = np.histogram(heights, bins=bin_edges)
    print("\nHeight bin counts:", dict(zip(bin_edges[:-1], counts.tolist())))
    plot_histogram(heights, bins=bin_edges)


if __name__ == "__main__":
    main()
