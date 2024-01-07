import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


class NormalDistribution:
    def __init__(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev

    def pdf(self, x):
        return norm.pdf(x, loc=self.mean, scale=self.std_dev)

    def cdf(self, x):
        return norm.cdf(x, loc=self.mean, scale=self.std_dev)


def plot_normal_distribution(means, std_devs):
    X = np.arange(-10, 10, 0.01)

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

    for i, (mean, std_dev) in enumerate(zip(means, std_devs)):
        nd = NormalDistribution(mean, std_dev)
        Y_pdf = [nd.pdf(x) for x in X]
        Y_cdf = [nd.cdf(x) for x in X]

        # plot PDF
        axs[0].plot(X, Y_pdf, label=f"mean={mean}, std_dev={std_dev}")
        axs[0].set_title("Normal Distribution PDF")
        axs[0].set_xlabel("Values")
        axs[0].set_ylabel("Probabilities")
        axs[0].legend()

        # plot CDF
        axs[1].plot(X, Y_cdf, label=f"mean={mean}, std_dev={std_dev}")
        axs[1].set_title("Normal Distribution CDF")
        axs[1].set_xlabel("Values")
        axs[1].set_ylabel("Probabilities")
        axs[1].legend()

    plt.show()


# Example usage
means = [-2, 0, 2, 4, 6]
std_devs = [0.5, 1, 1.5, 2, 2.5]
plot_normal_distribution(means, std_devs)
