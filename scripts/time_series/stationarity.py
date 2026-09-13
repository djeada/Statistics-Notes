import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate synthetic stock prices data (with a linear trend + seasonal component)
time = np.arange(2000, 2020, step=0.1)
linear_trend = 50 + 5 * (time - 2000)  # Linear upward trend
seasonal_component = np.sin(2 * np.pi * time) * 10  # Seasonal component
stock_prices = linear_trend + seasonal_component

# Fit a linear model to the data
time_reshaped = time.reshape(-1, 1)  # Reshape for sklearn
model = LinearRegression()
model.fit(time_reshaped, stock_prices)
predicted_trend = model.predict(time_reshaped)

# De-trend the data
residuals = stock_prices - predicted_trend

# Plot the original data with the fitted trend
plt.figure(figsize=(8, 12))

# Original data with trend
plt.subplot(2, 1, 1)
plt.plot(time, stock_prices, label='Original Data')
plt.plot(time, predicted_trend, label='Fitted Trend', color='red', linestyle='--')
plt.title('Stock Prices with Linear Trend')
plt.xlabel('Time')
plt.ylabel('Stock Prices')
plt.legend()
plt.grid(True)

# De-trended data
plt.subplot(2, 1, 2)
plt.plot(time, residuals, label='De-trended Data', color='black')
plt.title('Stock Prices with Linear Trend Removed')
plt.xlabel('Time')
plt.ylabel('Residuals')
plt.grid(True)

plt.tight_layout()
plt.show()
