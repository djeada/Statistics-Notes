import numpy as np
import matplotlib.pyplot as plt

# Generate MA(q) process
np.random.seed(42)
n = 1000  # Number of data points
q = 2  # Order of the MA process
beta = [1.0, 0.5, 0.3]  # Coefficients for MA(q)
white_noise = np.random.normal(0, 1, n + q)  # Generate white noise
ma_process = np.convolve(white_noise, beta, mode='valid')  # Generate MA(q) process

# Compute autocovariance and autocorrelation
lags = np.arange(-50, 51)
autocovariance = np.correlate(ma_process, ma_process, mode='full') / len(ma_process)
autocovariance = autocovariance[len(ma_process) - 1 - 50:len(ma_process) + 50]  # Extract values for lags

autocorrelation = autocovariance / autocovariance[len(lags) // 2]  # Normalize by variance

# Plot MA(q) process and its properties
plt.figure(figsize=(12, 10))

# MA(q) time series
plt.subplot(3, 1, 1)
plt.plot(ma_process, label='MA(q) Process', color='black')
plt.title('Moving Average (MA) Process Time Series')
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
