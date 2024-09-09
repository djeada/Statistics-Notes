import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Number of steps in the random walk
N = 1000

# Generate white noise (Z_t ~ N(0, 1))
Z = np.random.normal(loc=0, scale=1, size=N)

# Initialize the random walk (X_0 = 0)
X = np.cumsum(np.insert(Z, 0, 0))  # Insert X_0 = 0 and compute cumulative sum

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(X, label='Random Walk')
plt.title('Simulation of a Random Walk')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

# Plot the autocorrelation function (ACF) of the random walk
plot_acf(X, lags=50)
plt.show()

# Difference the random walk to remove the trend
diff_X = np.diff(X)

# Plot the differenced time series
plt.figure(figsize=(10, 6))
plt.plot(diff_X, label='Differenced Random Walk')
plt.title('Differenced Time Series (White Noise)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

# Plot the autocorrelation function (ACF) of the differenced series
plot_acf(diff_X, lags=50)
plt.show()
