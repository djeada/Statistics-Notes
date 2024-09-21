from scipy.stats import chi2

# Parameters for two chi-square distributions (degrees of freedom)
df1 = 2  # degrees of freedom for the first distribution
df2 = 5  # degrees of freedom for the second distribution

# Generate x values
x_chi2 = np.linspace(0, 20, 1000)

# Calculate the PDF and CDF for the chi-square distributions
pdf_chi2_1 = chi2.pdf(x_chi2, df1)
pdf_chi2_2 = chi2.pdf(x_chi2, df2)

cdf_chi2_1 = chi2.cdf(x_chi2, df1)
cdf_chi2_2 = chi2.cdf(x_chi2, df2)

# Create two separate plots for the PDF and CDF

# Plot 1: PDF of Chi-Square Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_chi2, pdf_chi2_1, label=f'Chi-Square(k={df1}) PDF', color='blue')
plt.plot(x_chi2, pdf_chi2_2, label=f'Chi-Square(k={df2}) PDF', color='red')
plt.title('Probability Density Function (PDF) of Chi-Square Distributions')
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of Chi-Square Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_chi2, cdf_chi2_1, label=f'Chi-Square(k={df1}) CDF', color='blue')
plt.plot(x_chi2, cdf_chi2_2, label=f'Chi-Square(k={df2}) CDF', color='red')
plt.title('Cumulative Distribution Function (CDF) of Chi-Square Distributions')
plt.xlabel('x')
plt.ylabel('CDF')
plt.legend()
plt.grid(True)
plt.show()
