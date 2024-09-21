import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

class ExponentialDistribution:
    def __init__(self, rate):
        self.rate = rate

    def pdf(self, x):
        return self.rate * np.exp(-self.rate * x)

    def cdf(self, x):
        return 1 - np.exp(-self.rate * x)

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

# Parameters for two exponential distributions (rate parameters)
lambda1 = 0.5
lambda2 = 1.5

# Generate x values
x_exp = np.linspace(0, 10, 1000)

# Calculate PDF and CDF using scipy
pdf_exp_1_scipy = expon.pdf(x_exp, scale=1/lambda1)
pdf_exp_2_scipy = expon.pdf(x_exp, scale=1/lambda2)
cdf_exp_1_scipy = expon.cdf(x_exp, scale=1/lambda1)
cdf_exp_2_scipy = expon.cdf(x_exp, scale=1/lambda2)

# Create instances of ExponentialDistribution
exp_dist_1 = ExponentialDistribution(lambda1)
exp_dist_2 = ExponentialDistribution(lambda2)

# Calculate PDF and CDF using custom class
pdf_exp_1_custom = np.array([exp_dist_1.pdf(x) for x in x_exp])
pdf_exp_2_custom = np.array([exp_dist_2.pdf(x) for x in x_exp])

cdf_exp_1_custom = exp_dist_1.cdf(x_exp)
cdf_exp_2_custom = exp_dist_2.cdf(x_exp)

# Plot 1: PDF of Exponential Distributions (Original)
plot_pdf(x_exp, pdf_exp_1_scipy, pdf_exp_2_scipy,
         label1=f'Exponential(λ={lambda1}) PDF', 
         label2=f'Exponential(λ={lambda2}) PDF',
         title='Probability Density Function (PDF) of Exponential Distributions')

# Plot 2: CDF of Exponential Distributions (Original)
plot_cdf(x_exp, cdf_exp_1_scipy, cdf_exp_2_scipy, 
         label1=f'Exponential(λ={lambda1}) CDF', 
         label2=f'Exponential(λ={lambda2}) CDF', 
         title='Cumulative Distribution Function (CDF) of Exponential Distributions')

# Plot 3: Comparison of Theoretical and Custom PDFs
plot_comparison(x_exp, pdf_exp_1_scipy, pdf_exp_1_custom, 
                label1=f'Theoretical Exponential(λ={lambda1}) PDF', 
                label2=f'Custom Exponential(λ={lambda1}) PDF', 
                title='Comparison of Theoretical and Custom PDF for Exponential Distribution')
