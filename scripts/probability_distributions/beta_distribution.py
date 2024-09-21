import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Parameters for two beta distributions
alpha1, beta1 = 2, 5
alpha2, beta2 = 5, 2

# Generate x values (in the range [0, 1])
x_beta = np.linspace(0, 1, 1000)

# Calculate the PDF and CDF for the beta distributions
pdf1 = beta.pdf(x_beta, alpha1, beta1)
pdf2 = beta.pdf(x_beta, alpha2, beta2)

cdf1 = beta.cdf(x_beta, alpha1, beta1)
cdf2 = beta.cdf(x_beta, alpha2, beta2)

# Create two separate plots for the PDF and CDF

# Plot 1: PDF of Beta Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_beta, pdf1, label=f'Beta(α={alpha1}, β={beta1}) PDF', color='blue')
plt.plot(x_beta, pdf2, label=f'Beta(α={alpha2}, β={beta2}) PDF', color='red')
plt.title('Probability Density Function (PDF) of Beta Distributions')
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of Beta Distributions
plt.figure(figsize=(10, 6))
plt.plot(x_beta, cdf1, label=f'Beta(α={alpha1}, β={beta1}) CDF', color='blue')
plt.plot(x_beta, cdf2, label=f'Beta(α={alpha2}, β={beta2}) CDF', color='red')
plt.title('Cumulative Distribution Function (CDF) of Beta Distributions')
plt.xlabel('x')
plt.ylabel('CDF')
plt.legend()
plt.grid(True)
plt.show()
