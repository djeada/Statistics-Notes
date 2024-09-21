from scipy.stats import t

# Parameters for two t-distributions (degrees of freedom ν)
df1 = 5  # degrees of freedom for the first distribution
df2 = 10  # degrees of freedom for the second distribution

# Generate x values
x_t = np.linspace(-5, 5, 1000)

# Calculate the PDF and CDF for the t-distributions
pdf_t_1 = t.pdf(x_t, df1)
pdf_t_2 = t.pdf(x_t, df2)

cdf_t_1 = t.cdf(x_t, df1)
cdf_t_2 = t.cdf(x_t, df2)

# Create two separate plots for the PDF and CDF

# Plot 1: PDF of t-Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_t, pdf_t_1, label=f"t-distribution(ν={df1}) PDF", color="blue")
plt.plot(x_t, pdf_t_2, label=f"t-distribution(ν={df2}) PDF", color="red")
plt.title("Probability Density Function (PDF) of t-Distributions")
plt.xlabel("x")
plt.ylabel("PDF")
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of t-Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_t, cdf_t_1, label=f"t-distribution(ν={df1}) CDF", color="blue")
plt.plot(x_t, cdf_t_2, label=f"t-distribution(ν={df2}) CDF", color="red")
plt.title("Cumulative Distribution Function (CDF) of t-Distributions")
plt.xlabel("x")
plt.ylabel("CDF")
plt.legend()
plt.grid(True)
plt.show()
