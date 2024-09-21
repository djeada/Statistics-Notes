from scipy.stats import f

# Parameters for two F-distributions (degrees of freedom for numerator and denominator)
d1_1, d2_1 = 5, 10  # degrees of freedom for the first distribution
d1_2, d2_2 = 10, 5  # degrees of freedom for the second distribution

# Generate x values
x_f = np.linspace(0, 5, 1000)

# Calculate the PDF and CDF for the F-distributions
pdf_f_1 = f.pdf(x_f, d1_1, d2_1)
pdf_f_2 = f.pdf(x_f, d1_2, d2_2)

cdf_f_1 = f.cdf(x_f, d1_1, d2_1)
cdf_f_2 = f.cdf(x_f, d1_2, d2_2)

# Create two separate plots for the PDF and CDF

# Plot 1: PDF of F-Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_f, pdf_f_1, label=f'F({d1_1}, {d2_1}) PDF', color='blue')
plt.plot(x_f, pdf_f_2, label=f'F({d1_2}, {d2_2}) PDF', color='red')
plt.title('Probability Density Function (PDF) of F-Distributions')
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of F-Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_f, cdf_f_1, label=f'F({d1_1}, {d2_1}) CDF', color='blue')
plt.plot(x_f, cdf_f_2, label=f'F({d1_2}, {d2_2}) CDF', color='red')
plt.title('Cumulative Distribution Function (CDF) of F-Distributions')
plt.xlabel('x')
plt.ylabel('CDF')
plt.legend()
plt.grid(True)
plt.show()
