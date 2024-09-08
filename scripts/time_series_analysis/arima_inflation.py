import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import pandas_datareader.data as web
from datetime import datetime

# Step 1: Fetch Inflation Data (from FRED or yfinance)
# Using CPI (Consumer Price Index) from FRED
start_date = '1980-01-01'
end_date = '2023-01-01'

# Fetch CPI data (monthly)
cpi_data = web.DataReader('CPIAUCSL', 'fred', start_date, end_date)

# Step 2: Exploratory Data Analysis
plt.figure(figsize=(10, 6))
plt.plot(cpi_data, label="CPI (Inflation Index)")
plt.title('Consumer Price Index (CPI) Over Time')
plt.xlabel('Year')
plt.ylabel('CPI')
plt.legend()
plt.show()

# Step 3: Check for Stationarity using ADF Test
def adf_test(series):
    result = adfuller(series)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    for key, value in result[4].items():
        print(f'Critical Value ({key}): {value}')

adf_test(cpi_data['CPIAUCSL'])

# Step 4: Differencing (if non-stationary)
# We apply differencing if p-value > 0.05, suggesting non-stationarity
cpi_diff = cpi_data.diff().dropna()

plt.figure(figsize=(10, 6))
plt.plot(cpi_diff, label="Differenced CPI (Inflation Index)")
plt.title('Differenced CPI Over Time')
plt.xlabel('Year')
plt.ylabel('Differenced CPI')
plt.legend()
plt.show()

adf_test(cpi_diff['CPIAUCSL'])

# Step 5: Fit ARIMA Model
# Using ARIMA(p, d, q) where p, q are determined based on ACF and PACF plots

# Plot ACF and PACF
fig, ax = plt.subplots(1, 2, figsize=(16, 6))
sm.graphics.tsa.plot_acf(cpi_diff, lags=40, ax=ax[0])
sm.graphics.tsa.plot_pacf(cpi_diff, lags=40, ax=ax[1])
plt.show()

# Fit ARIMA Model
# Initial guess based on ACF/PACF plots: ARIMA(1,1,1)
model = ARIMA(cpi_data, order=(1, 1, 1))
fitted_model = model.fit()

# Step 6: Evaluate Model
print(fitted_model.summary())

# Step 7: Forecast Future Values
forecast = fitted_model.get_forecast(steps=12)  # Forecast next 12 months
forecast_values = forecast.predicted_mean
forecast_ci = forecast.conf_int()

# Plot Forecast
plt.figure(figsize=(10, 6))
plt.plot(cpi_data, label='Historical CPI')
plt.plot(forecast_values.index, forecast_values, label='Forecasted CPI', color='red')
plt.fill_between(forecast_ci.index, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color='pink', alpha=0.3)
plt.title('CPI Forecast for Next 12 Months')
plt.xlabel('Year')
plt.ylabel('CPI')
plt.legend()
plt.show()
