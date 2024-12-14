import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Generate synthetic AR(2) process data
np.random.seed(42)
n = 500  # Number of data points
phi1 = 0.6  # AR(1) coefficient
phi2 = -0.3  # AR(2) coefficient
noise = np.random.normal(0, 1, n)  # White noise

data = np.zeros(n)
for t in range(2, n):
    data[t] = phi1 * data[t - 1] + phi2 * data[t - 2] + noise[t]

# Plot the time series, ACF, and PACF
plt.figure(figsize=(10, 15))

# Time series plot
plt.subplot(3, 1, 1)
plt.plot(data, color='black')
plt.title('Synthetic AR(2) Process Time Series')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid(True)

# Autocorrelation function (ACF)
plt.subplot(3, 1, 2)
plot_acf(data, lags=40, ax=plt.gca(), color='black')
plt.title('Autocorrelation Function (ACF)')

# Partial autocorrelation function (PACF)
plt.subplot(3, 1, 3)
plot_pacf(data, lags=40, ax=plt.gca(), method='ywmle', color='black')
plt.title('Partial Autocorrelation Function (PACF)')

plt.tight_layout()
plt.show()
