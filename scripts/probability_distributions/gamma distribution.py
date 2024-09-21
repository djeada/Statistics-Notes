from scipy.stats import gamma

# Parameters for two gamma distributions (shape α and rate β)
alpha1, beta1 = 2, 2  # parameters for the first distribution
alpha2, beta2 = 5, 1  # parameters for the second distribution

# Generate x values
x_gamma = np.linspace(0, 20, 1000)

# Calculate the PDF and CDF for the gamma distributions
pdf_gamma_1 = gamma.pdf(x_gamma, alpha1, scale=1/beta1)
pdf_gamma_2 = gamma.pdf(x_gamma, alpha2, scale=1/beta2)

cdf_gamma_1 = gamma.cdf(x_gamma, alpha1, scale=1/beta1)
cdf_gamma_2 = gamma.cdf(x_gamma, alpha2, scale=1/beta2)

# Create two separate plots for the PDF and CDF

# Plot 1: PDF of Gamma Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_gamma, pdf_gamma_1, label=f'Gamma(α={alpha1}, β={beta1}) PDF', color='blue')
plt.plot(x_gamma, pdf_gamma_2, label=f'Gamma(α={alpha2}, β={beta2}) PDF', color='red')
plt.title('Probability Density Function (PDF) of Gamma Distributions')
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of Gamma Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_gamma, cdf_gamma_1, label=f'Gamma(α={alpha1}, β={beta1}) CDF', color='blue')
plt.plot(x_gamma, cdf_gamma_2, label=f'Gamma(α={alpha2}, β={beta2}) CDF', color='red')
plt.title('Cumulative Distribution Function (CDF) of Gamma Distributions')
plt.xlabel('x')
plt.ylabel('CDF')
plt.legend()
plt.grid(True)
plt.show()
