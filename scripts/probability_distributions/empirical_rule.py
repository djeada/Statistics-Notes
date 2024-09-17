# Parameters for the normal distribution representing the heights of fathers
mu_height = 68.3  # mean height in inches
sigma_height = 1.8  # standard deviation in inches

# Generate x values (heights)
x_heights = np.linspace(mu_height - 4*sigma_height, mu_height + 4*sigma_height, 1000)

# Calculate the PDF for the normal distribution
pdf_height = (1 / (sigma_height * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_heights - mu_height) / sigma_height) ** 2)

# Plot the normal distribution
plt.figure(figsize=(10, 6))
plt.plot(x_heights, pdf_height, label=f'Normal Distribution: μ={mu_height}, σ={sigma_height}', color='green')

# Empirical rule intervals
plt.axvline(mu_height, color='black', linestyle='--', label=f'Mean μ={mu_height}')

# 68% interval (1 sigma)
plt.axvline(mu_height - sigma_height, color='blue', linestyle='--', label=f'μ - σ = {mu_height - sigma_height:.1f}')
plt.axvline(mu_height + sigma_height, color='blue', linestyle='--', label=f'μ + σ = {mu_height + sigma_height:.1f}')

# 95% interval (2 sigma)
plt.axvline(mu_height - 2*sigma_height, color='orange', linestyle='--', label=f'μ - 2σ = {mu_height - 2*sigma_height:.1f}')
plt.axvline(mu_height + 2*sigma_height, color='orange', linestyle='--', label=f'μ + 2σ = {mu_height + 2*sigma_height:.1f}')

# 99.7% interval (3 sigma)
plt.axvline(mu_height - 3*sigma_height, color='red', linestyle='--', label=f'μ - 3σ = {mu_height - 3*sigma_height:.1f}')
plt.axvline(mu_height + 3*sigma_height, color='red', linestyle='--', label=f'μ + 3σ = {mu_height + 3*sigma_height:.1f}')

# Highlight the empirical rule percentages on the plot
plt.fill_between(x_heights, 0, pdf_height, where=((x_heights >= mu_height - sigma_height) & (x_heights <= mu_height + sigma_height)), color='blue', alpha=0.2, label='68% of data')
plt.fill_between(x_heights, 0, pdf_height, where=((x_heights >= mu_height - 2*sigma_height) & (x_heights <= mu_height + 2*sigma_height)), color='orange', alpha=0.2, label='95% of data')
plt.fill_between(x_heights, 0, pdf_height, where=((x_heights >= mu_height - 3*sigma_height) & (x_heights <= mu_height + 3*sigma_height)), color='red', alpha=0.2, label='99.7% of data')

plt.title('Empirical Rule (68-95-99.7 Rule) for Heights of Fathers')
plt.xlabel('Height (inches)')
plt.ylabel('Probability Density Function (PDF)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
