import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate synthetic data
np.random.seed(42)
time = np.arange(1, 26)
data = np.random.randint(5, 25, size=len(time))

# Plot setup
plt.figure(figsize=(8, 12))

# Plot time series (top subplot)
plt.subplot(2, 1, 1)
plt.plot(time, data, marker='o', linestyle='-', color='black')
plt.title('Time Series')
plt.xlabel('Time Period, t')
plt.ylabel('X')
plt.grid(True)

# Compute histogram and fit normal distribution
mu, sigma = np.mean(data), np.std(data)
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
pdf = norm.pdf(x, mu, sigma)

# Plot normal distribution with points (bottom subplot)
plt.subplot(2, 1, 2)
plt.plot(x, pdf, color='black', label='Best Fit Curve')
plt.scatter(data, norm.pdf(data, mu, sigma), color='red', label='Data Points')
plt.title('Normal Distribution with Data Points')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.axvline(mu, color='black', linestyle='--', label='Mean ($\mu$)')
plt.axvline(mu - sigma, color='gray', linestyle='--', label='$\mu - 1\sigma$')
plt.axvline(mu + sigma, color='gray', linestyle='--', label='$\mu + 1\sigma$')
plt.axvline(mu - 2 * sigma, color='gray', linestyle=':')
plt.axvline(mu + 2 * sigma, color='gray', linestyle=':')
plt.axvline(mu - 3 * sigma, color='gray', linestyle='-.')
plt.axvline(mu + 3 * sigma, color='gray', linestyle='-.')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
