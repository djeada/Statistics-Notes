from scipy.stats import norm

# Parameters for two normal distributions (mean μ and standard deviation σ)
mu1, sigma1 = 0, 1  # parameters for the first distribution
mu2, sigma2 = 2, 1.5  # parameters for the second distribution

# Generate x values
x_norm = np.linspace(-5, 7, 1000)

# Calculate the PDF and CDF for the normal distributions
pdf_norm_1 = norm.pdf(x_norm, mu1, sigma1)
pdf_norm_2 = norm.pdf(x_norm, mu2, sigma2)

cdf_norm_1 = norm.cdf(x_norm, mu1, sigma1)
cdf_norm_2 = norm.cdf(x_norm, mu2, sigma2)

# Create two separate plots for the PDF and CDF

# Plot 1: PDF of Normal Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_norm, pdf_norm_1, label=f'Normal(μ={mu1}, σ={sigma1}) PDF', color='blue')
plt.plot(x_norm, pdf_norm_2, label=f'Normal(μ={mu2}, σ={sigma2}) PDF', color='red')
plt.title('Probability Density Function (PDF) of Normal Distributions')
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of Normal Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_norm, cdf_norm_1, label=f'Normal(μ={mu1}, σ={sigma1}) CDF', color='blue')
plt.plot(x_norm, cdf_norm_2, label=f'Normal(μ={mu2}, σ={sigma2}) CDF', color='red')
plt.title('Cumulative Distribution Function (CDF) of Normal Distributions')
plt.xlabel('x')
plt.ylabel('CDF')
plt.legend()
plt.grid(True)
plt.show()
