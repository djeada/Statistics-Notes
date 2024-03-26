import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Step 1: Generate mock monthly airline passenger data.
np.random.seed(42)
date_range = pd.date_range(start='2000-01-01', end='2024-01-01', freq='M')
trend = np.linspace(50, 300, len(date_range))
seasonality = 50 * np.sin(np.linspace(0, 3.14*8, len(date_range)))
noise = np.random.normal(0, 20, len(date_range))
data = trend + seasonality + noise
ts_data = pd.Series(data, index=date_range)

# Step 2: Decompose Time Series
decomposition = seasonal_decompose(ts_data, model='additive')
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Step 3: Detrending using Differencing
ts_data_diff = ts_data - ts_data.shift(12)

# Step 4: Fit a Seasonal ARIMA model
# Note: Parameters (p,d,q) and seasonal (P,D,Q,s) should be optimized
model = SARIMAX(ts_data, order=(1,1,1), seasonal_order=(1,1,1,12))
results = model.fit()

# Step 5: Forecast
forecast = results.get_forecast(steps=12)
forecast_index = pd.date_range(start=ts_data.index[-1], periods=13, freq='M')[1:]
forecast_mean = forecast.predicted_mean
confidence_intervals = forecast.conf_int()

# Step 6: Plot the Results
# Adjusting the plot with different colors for the original series and the forecast for better readability

plt.figure(figsize=(15, 12))

plt.subplot(4, 1, 1)
plt.plot(ts_data, label='Original', color='blue')
plt.plot(trend_component, label='Trend', alpha=0.7, color='orange')
plt.title('Time Series with Trend')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(seasonal_component, label='Seasonality', color='green')
plt.title('Seasonal Component')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(ts_data_diff.dropna(), label='Differenced Series', color='purple')  # Dropping NA values
plt.title('Differenced Series')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(ts_data, label='Original', color='blue')
plt.plot(forecast_index, forecast_mean, label='Forecast', color='red')
# Ensure confidence intervals are in a suitable format
lower_bounds = confidence_intervals['lower y'].values
upper_bounds = confidence_intervals['upper y'].values
plt.fill_between(forecast_index, lower_bounds, upper_bounds, color='k', alpha=0.1)
plt.title('Forecast vs Actual')
plt.legend()

plt.tight_layout()
plt.show()
