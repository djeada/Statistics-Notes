# Parameters for two uniform distributions
a1, b1 = 0, 5  # interval for the first distribution
a2, b2 = 2, 7  # interval for the second distribution

# Generate x values
x_uniform = np.linspace(-1, 8, 1000)

# Calculate the PDF and CDF for the uniform distributions
pdf_uniform_1 = np.where((x_uniform >= a1) & (x_uniform <= b1), 1/(b1 - a1), 0)
pdf_uniform_2 = np.where((x_uniform >= a2) & (x_uniform <= b2), 1/(b2 - a2), 0)

cdf_uniform_1 = np.piecewise(x_uniform, 
                             [x_uniform < a1, (x_uniform >= a1) & (x_uniform <= b1), x_uniform > b1], 
                             [0, lambda x: (x - a1)/(b1 - a1), 1])
cdf_uniform_2 = np.piecewise(x_uniform, 
                             [x_uniform < a2, (x_uniform >= a2) & (x_uniform <= b2), x_uniform > b2], 
                             [0, lambda x: (x - a2)/(b2 - a2), 1])

# Create two separate plots for the PDF and CDF

# Plot 1: PDF of Uniform Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_uniform, pdf_uniform_1, label=f'Uniform({a1}, {b1}) PDF', color='blue')
plt.plot(x_uniform, pdf_uniform_2, label=f'Uniform({a2}, {b2}) PDF', color='red')
plt.title('Probability Density Function (PDF) of Uniform Distributions')
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of Uniform Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_uniform, cdf_uniform_1, label=f'Uniform({a1}, {b1}) CDF', color='blue')
plt.plot(x_uniform, cdf_uniform_2, label=f'Uniform({a2}, {b2}) CDF', color='red')
plt.title('Cumulative Distribution Function (CDF) of Uniform Distributions')
plt.xlabel('x')
plt.ylabel('CDF')
plt.legend()
plt.grid(True)
plt.show()
