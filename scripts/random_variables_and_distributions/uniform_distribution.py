import numpy as np
import matplotlib.pyplot as plt

class UniformDistribution:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pdf(self, x):
        return np.where((x >= self.a) & (x <= self.b), 1 / (self.b - self.a), 0)

    def cdf(self, x):
        return np.piecewise(x, 
                            [x < self.a, (x >= self.a) & (x <= self.b), x > self.b], 
                            [0, lambda x: (x - self.a) / (self.b - self.a), 1])

def plot_pdf(x_values, pdf1, pdf2, label1, label2, title):
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, pdf1, label=label1, color='blue')
    plt.plot(x_values, pdf2, label=label2, color='red')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('PDF')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_cdf(x_values, cdf1, cdf2, label1, label2, title):
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, cdf1, label=label1, color='blue')
    plt.plot(x_values, cdf2, label=label2, color='red')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('CDF')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_comparison(x_values, pdf_scipy, pdf_custom, label1, label2, title):
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, pdf_scipy, label=label1, color='blue', linestyle='--')
    plt.plot(x_values, pdf_custom, label=label2, color='orange')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('PDF')
    plt.legend()
    plt.grid(True)
    plt.show()

# Parameters for two uniform distributions
a1, b1 = 0, 5
a2, b2 = 2, 7

# Generate x values
x_uniform = np.linspace(-1, 8, 1000)

# Calculate PDF and CDF using numpy
pdf_uniform_1_scipy = np.where((x_uniform >= a1) & (x_uniform <= b1), 1/(b1 - a1), 0)
pdf_uniform_2_scipy = np.where((x_uniform >= a2) & (x_uniform <= b2), 1/(b2 - a2), 0)
cdf_uniform_1_scipy = np.piecewise(x_uniform, 
                                   [x_uniform < a1, (x_uniform >= a1) & (x_uniform <= b1), x_uniform > b1], 
                                   [0, lambda x: (x - a1)/(b1 - a1), 1])
cdf_uniform_2_scipy = np.piecewise(x_uniform, 
                                   [x_uniform < a2, (x_uniform >= a2) & (x_uniform <= b2), x_uniform > b2], 
                                   [0, lambda x: (x - a2)/(b2 - a2), 1])

# Create instances of UniformDistribution
uniform1 = UniformDistribution(a1, b1)
uniform2 = UniformDistribution(a2, b2)

# Calculate PDF and CDF using custom class
pdf_uniform_1_custom = uniform1.pdf(x_uniform)
pdf_uniform_2_custom = uniform2.pdf(x_uniform)
cdf_uniform_1_custom = uniform1.cdf(x_uniform)
cdf_uniform_2_custom = uniform2.cdf(x_uniform)

# Plot 1: PDF of Uniform Distributions (Original)
plot_pdf(x_uniform, pdf_uniform_1_scipy, pdf_uniform_2_scipy,
         label1=f'Uniform({a1}, {b1}) PDF', 
         label2=f'Uniform({a2}, {b2}) PDF',
         title='Probability Density Function (PDF) of Uniform Distributions')

# Plot 2: CDF of Uniform Distributions (Original)
plot_cdf(x_uniform, cdf_uniform_1_scipy, cdf_uniform_2_scipy, 
         label1=f'Uniform({a1}, {b1}) CDF', 
         label2=f'Uniform({a2}, {b2}) CDF', 
         title='Cumulative Distribution Function (CDF) of Uniform Distributions')

# Plot 3: Comparison of Theoretical and Custom PDFs
plot_comparison(x_uniform, pdf_uniform_1_scipy, pdf_uniform_1_custom, 
                label1=f'Theoretical Uniform({a1}, {b1}) PDF', 
                label2=f'Custom Uniform({a1}, {b1}) PDF', 
                title='Comparison of Theoretical and Custom PDF for Uniform Distribution')
