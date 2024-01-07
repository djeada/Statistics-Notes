import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


class PoissonDistribution:
    def __init__(self, lambd):
        self.lambd = lambd
        self.mean = self.lambd
        self.variance = self.lambd

    def pmf(self, k):
        return (np.exp(-self.lambd) * self.lambd ** k) / np.math.factorial(k)

    def cdf(self, k):
        return stats.poisson.cdf(k, self.lambd)


# Define lambda values to plot
lambda_values = [1, 3, 5, 7, 9]

# Define range of values for x axis
x_values = np.arange(0, 20, 1)

# Initialize plot for PDFs
fig, ax1 = plt.subplots()
ax1.set_xlabel("k")
ax1.set_ylabel("PDF")

# Initialize plot for CDFs
fig, ax2 = plt.subplots()
ax2.set_xlabel("k")
ax2.set_ylabel("CDF")

# Plot PDFs and CDFs for each lambda value
for lambd in lambda_values:
    # Initialize PoissonDistribution object
    dist = PoissonDistribution(lambd)

    # Calculate PDF and CDF values for range of x values
    pdf_values = [dist.pmf(k) for k in x_values]
    cdf_values = [dist.cdf(k) for k in x_values]

    # Plot PDF
    ax1.plot(x_values, pdf_values, label=f"lambda = {lambd}")

    # Plot CDF
    ax2.plot(x_values, cdf_values, label=f"lambda = {lambd}")

# Add legend to plots
ax1.legend()
ax2.legend()

# Show plots
plt.show()
