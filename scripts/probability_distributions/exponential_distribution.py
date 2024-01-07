import numpy as np
import matplotlib.pyplot as plt


class Exponential:
    def __init__(self, rate):
        self.rate = rate

    def pdf(self, x):
        return self.rate * np.exp(-self.rate * x)

    def cdf(self, x):
        return 1 - np.exp(-self.rate * x)


# Set up exponential distributions with different rates
exponential_1 = Exponential(0.5)
exponential_2 = Exponential(1)
exponential_3 = Exponential(2)

# Generate data for x-axis
x = np.linspace(0, 5, 1000)

# Plot PDFs
plt.plot(x, exponential_1.pdf(x), label="rate=0.5")
plt.plot(x, exponential_2.pdf(x), label="rate=1")
plt.plot(x, exponential_3.pdf(x), label="rate=2")

# Add legend and labels
plt.legend()
plt.title("Exponential Probability Density Function")
plt.xlabel("x")
plt.ylabel("PDF(x)")

# Show plot
plt.show()

# Plot CDFs
plt.plot(x, exponential_1.cdf(x), label="rate=0.5")
plt.plot(x, exponential_2.cdf(x), label="rate=1")
plt.plot(x, exponential_3.cdf(x), label="rate=2")

# Add legend and labels
plt.legend()
plt.title("Exponential Cumulative Density Function")
plt.xlabel("x")
plt.ylabel("CDF(x)")

# Show plot
plt.show()
