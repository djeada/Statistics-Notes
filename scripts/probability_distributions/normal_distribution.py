import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

class NormalDistribution:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def pdf(self, x):
        return (1 / (self.sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - self.mu) / self.sigma) ** 2)

    def cdf(self, x):
        return 0.5 * (1 + np.erf((x - self.mu) / (self.sigma * np.sqrt(2))))

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

# Parameters for two normal distributions (mean μ and standard deviation σ)
mu1, sigma1 = 0, 1
mu2, sigma2 = 2, 1.5

# Generate x values
x_norm = np.linspace(-5, 7, 1000)

# Calculate PDF and CDF using scipy
pdf_norm_1_scipy = norm.pdf(x_norm, mu1, sigma1)
pdf_norm_2_scipy = norm.pdf(x_norm, mu2, sigma2)
cdf_norm_1_scipy = norm.cdf(x_norm, mu1, sigma1)
cdf_norm_2_scipy = norm.cdf(x_norm, mu2, sigma2)

# Create instances of NormalDistribution
norm_dist_1 = NormalDistribution(mu1, sigma1)
norm_dist_2 = NormalDistribution(mu2, sigma2)

# Calculate PDF and CDF using custom class
pdf_norm_1_custom = np.array([norm_dist_1.pdf(x) for x in x_norm])
pdf_norm_2_custom = np.array([norm_dist_2.pdf(x) for x in x_norm])

cdf_norm_1_custom = norm_dist_1.cdf(x_norm)
cdf_norm_2_custom = norm_dist_2.cdf(x_norm)

# Plot 1: PDF of Normal Distributions (Original)
plot_pdf(x_norm, pdf_norm_1_scipy, pdf_norm_2_scipy,
         label1=f'Normal(μ={mu1}, σ={sigma1}) PDF', 
         label2=f'Normal(μ={mu2}, σ={sigma2}) PDF',
         title='Probability Density Function (PDF) of Normal Distributions')

# Plot 2: CDF of Normal Distributions (Original)
plot_cdf(x_norm, cdf_norm_1_scipy, cdf_norm_2_scipy, 
         label1=f'Normal(μ={mu1}, σ={sigma1}) CDF', 
         label2=f'Normal(μ={mu2}, σ={sigma2}) CDF', 
         title='Cumulative Distribution Function (CDF) of Normal Distributions')

# Plot 3: Comparison of Theoretical and Custom PDFs
plot_comparison(x_norm, pdf_norm_1_scipy, pdf_norm_1_custom, 
                label1=f'Theoretical Normal(μ={mu1}, σ={sigma1}) PDF', 
                label2=f'Custom Normal(μ={mu1}, σ={sigma1}) PDF', 
                title='Comparison of Theoretical and Custom PDF for Normal Distribution')
