# Heights for the example
x1 = 71.9  # father's height 71.9 inches
x2 = 67.4  # father's height 67.4 inches

# Calculate the z-scores for these heights
z1 = (x1 - mu_height) / sigma_height  # z-score for 71.9 inches
z2 = (x2 - mu_height) / sigma_height  # z-score for 67.4 inches

# Generate x values for standard normal distribution
x_standard = np.linspace(-4, 4, 1000)

# Calculate PDF for the standard normal distribution
pdf_standard = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x_standard**2)

# Plot the standard normal distribution
plt.figure(figsize=(10, 6))
plt.plot(x_standard, pdf_standard, label='Standard Normal Distribution', color='green')

# Mark z-scores on the plot
plt.axvline(z1, color='blue', linestyle='--', label=f'z-score for 71.9 inches: z = {z1:.1f}')
plt.axvline(z2, color='red', linestyle='--', label=f'z-score for 67.4 inches: z = {z2:.1f}')

# Shade the area between z1 and z2
plt.fill_between(x_standard, 0, pdf_standard, where=((x_standard >= z2) & (x_standard <= z1)), color='orange', alpha=0.3, label='Area between z-scores')

# Highlight important points
plt.title('Standard Normal Distribution and Z-Scores')
plt.xlabel('z')
plt.ylabel('Probability Density Function (PDF)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
