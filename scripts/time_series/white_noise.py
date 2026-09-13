import numpy as np
import matplotlib.pyplot as plt

# Generate white noise
np.random.seed(42)
n = 1000  # Number of data points
sigma = 1  # Standard deviation
white_noise = np.random.normal(0, sigma, n)

# Compute autocovariance and autocorrelation
lags = np.arange(-50, 51)
autocovariance = np.correlate(white_noise, white_noise, mode='full') / n
autocovariance = autocovariance[n - 1 - 50:n + 50]  # Extract values for lags

autocorrelation = autocovariance / autocovariance[len(lags) // 2]  # Normalize by variance

# Plot white noise and its properties
plt.figure(figsize=(12, 10))

# White noise time series
plt.subplot(3, 1, 1)
plt.plot(white_noise, label='White Noise', color='black')
plt.title('White Noise Time Series')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid(True)
plt.legend()

# Autocovariance function
plt.subplot(3, 1, 2)
plt.stem(lags, autocovariance, linefmt='black', markerfmt='o', basefmt=" ", use_line_collection=True)
plt.title('Autocovariance Function')
plt.xlabel('Lag')
plt.ylabel('$\gamma(k)$')
plt.grid(True)

# Autocorrelation function
plt.subplot(3, 1, 3)
plt.stem(lags, autocorrelation, linefmt='black', markerfmt='o', basefmt=" ", use_line_collection=True)
plt.title('Autocorrelation Function')
plt.xlabel('Lag')
plt.ylabel('$\rho(k)$')
plt.grid(True)

plt.tight_layout()
plt.show()
