import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as plt
import numpy as np

def generate_sample_data(size=1000):
    """
    Generate sample data for demonstration.
    :param size: Number of data points to generate.
    :return: Array of sample data.
    """
    # Example: Generating data from a normal distribution
    return np.random.normal(loc=0, scale=1, size=size)

def fit_distribution(data, distributions):
    """
    Fit data to specified distributions and find the best fit.
    :param data: The data to fit.
    :param distributions: List of scipy.stats distribution objects.
    :return: Best fitting distribution and its parameters.
    """
    best_distribution = None
    best_params = None
    best_sse = np.inf

    for distribution in distributions:
        try:
            params = distribution.fit(data)
            arg = params[:-2]
            loc = params[-2]
            scale = params[-1]

            # Calculate the Sum of Squared Errors
            pdf = distribution.pdf(data, loc=loc, scale=scale, *arg)
            sse = np.sum(np.power(data - pdf, 2))

            if best_sse > sse > 0:
                best_distribution = distribution
                best_params = params
                best_sse = sse
        except Exception:
            pass

    return best_distribution, best_params

def plot_data_and_fit(ax, data, distribution, params):
    """
    Plot the data and the best fitted distribution.
    :param ax: The axes object to plot on.
    :param data: The data used for the plot.
    :param distribution: The best fit scipy.stats distribution object.
    :param params: Parameters of the best fit distribution.
    """
    ax.hist(data, bins=30, density=True, alpha=0.5, color='g', label='Data')

    # Plot the best fit distribution
    xmin, xmax = min(data), max(data)
    x = np.linspace(xmin, xmax, 100)
    p = distribution.pdf(x, *params)
    ax.plot(x, p, 'k', linewidth=2, label=distribution.name)

    ax.set_xlabel('Data')
    ax.set_ylabel('Density')
    ax.legend()

def main():
    # Generate sample data
    data = generate_sample_data()

    # Define distributions to test
    distributions = [ss.norm, ss.lognorm, ss.gamma]

    # Fit data to distributions
    best_dist, best_params = fit_distribution(data, distributions)

    # Create plot
    fig, ax = plt.subplots(figsize=(8, 6))
    plot_data_and_fit(ax, data, best_dist, best_params)

    # Show plot
    plt.show()

if __name__ == '__main__':
    main()
