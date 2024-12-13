import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from datetime import timedelta

# Generate mock data
np.random.seed(42)
dates = pd.date_range(start='2021-01-01', end='2022-12-31', freq='D')
electricity_consumption = 500 + 20 * np.sin(2 * np.pi * dates.dayofyear / 365) + np.random.normal(0, 10, len(dates))
data = pd.DataFrame({'Date': dates, 'Consumption': electricity_consumption})

# Fit a regression model
X = np.arange(len(data)).reshape(-1, 1)
y = data['Consumption'].values
reg_model = LinearRegression()
reg_model.fit(X, y)

# Predict next 3 months using regression
future_dates = pd.date_range(start='2023-01-01', end='2023-03-31', freq='D')
future_X = np.arange(len(data), len(data) + len(future_dates)).reshape(-1, 1)
reg_predictions = reg_model.predict(future_X)

# Fit a time series model (Exponential Smoothing)
ts_model = ExponentialSmoothing(data['Consumption'], seasonal='add', seasonal_periods=365).fit()
ts_predictions = ts_model.forecast(len(future_dates))

# Combine historical and predicted data for plotting
future_data = pd.DataFrame({'Date': future_dates, 'Regression_Prediction': reg_predictions, 'TS_Prediction': ts_predictions})
data = data.set_index('Date')
future_data = future_data.set_index('Date')

# Plot historical data and predictions
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Consumption'], label='Historical Data', linewidth=2)
plt.plot(future_data.index, future_data['Regression_Prediction'], label='Regression Prediction', color='blue', linestyle='--')
plt.plot(future_data.index, future_data['TS_Prediction'], label='Time Series Prediction', linestyle='--')

# Add legend and labels
plt.title('Electricity Consumption Forecast', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Electricity Consumption', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
