from scipy.stats import expon

# Parameters for two exponential distributions (rate parameters)
lambda1 = 0.5  # rate parameter for the first distribution
lambda2 = 1.5  # rate parameter for the second distribution

# Generate x values
x_exp = np.linspace(0, 10, 1000)

# Calculate the PDF and CDF for the exponential distributions
pdf_exp_1 = expon.pdf(x_exp, scale=1/lambda1)
pdf_exp_2 = expon.pdf(x_exp, scale=1/lambda2)

cdf_exp_1 = expon.cdf(x_exp, scale=1/lambda1)
cdf_exp_2 = expon.cdf(x_exp, scale=1/lambda2)

# Create two separate plots for the PDF and CDF

# Plot 1: PDF of Exponential Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_exp, pdf_exp_1, label=f'Exponential(λ={lambda1}) PDF', color='blue')
plt.plot(x_exp, pdf_exp_2, label=f'Exponential(λ={lambda2}) PDF', color='red')
plt.title('Probability Density Function (PDF) of Exponential Distributions')
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of Exponential Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_exp, cdf_exp_1, label=f'Exponential(λ={lambda1}) CDF', color='blue')
plt.plot(x_exp, cdf_exp_2, label=f'Exponential(λ={lambda2}) CDF', color='red')
plt.title('Cumulative Distribution Function (CDF) of Exponential Distributions')
plt.xlabel('x')
plt.ylabel('CDF')
plt.legend()
plt.grid(True)
plt.show()
