import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the normal distributions
mu1, sigma1 = 0, 1  # mean and standard deviation for distribution 1
mu2, sigma2 = 2, 1.5  # mean and standard deviation for distribution 2

# Generate x values
x = np.linspace(-10, 10, 1000)

# Calculate the PDF of both distributions
pdf1 = (1 / (sigma1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu1) / sigma1) ** 2)
pdf2 = (1 / (sigma2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu2) / sigma2) ** 2)

# Plot both distributions
plt.figure(figsize=(10, 6))
plt.plot(x, pdf1, label=f'Normal Distribution: μ={mu1}, σ={sigma1}', color='blue')
plt.plot(x, pdf2, label=f'Normal Distribution: μ={mu2}, σ={sigma2}', color='red')

# Annotate mu and sigma on the graph
plt.axvline(mu1, color='blue', linestyle='--', label=f'Mean μ1={mu1}')
plt.axvline(mu2, color='red', linestyle='--', label=f'Mean μ2={mu2}')
plt.text(mu1 - 0.5, 0.1, f'μ={mu1}', color='blue', fontsize=12)
plt.text(mu2 + 0.5, 0.1, f'μ={mu2}', color='red', fontsize=12)

plt.title('Normal Distributions with Different Parameters')
plt.xlabel('x')
plt.ylabel('Probability Density Function (PDF)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
