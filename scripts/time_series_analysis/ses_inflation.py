import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Fetch CPI data from FRED
start_date = '1980-01-01'
end_date = '2023-01-01'
cpi_data = web.DataReader('CPIAUCSL', 'fred', start_date, end_date)

# Define SES forecast function
def ses_forecast(data, alpha):
    forecast_values = [data[0]]  # First forecast is the first data point
    for i in range(1, len(data)):
        forecast = alpha * data[i-1] + (1 - alpha) * forecast_values[i-1]
        forecast_values.append(forecast)
    return forecast_values

# Plot original data
plt.figure(figsize=(10,6))
plt.plot(cpi_data, label='CPI Data')
plt.title('CPI Data from 1980 to 2023')
plt.xlabel('Year')
plt.ylabel('CPI')
plt.show()

# Calculate SES for a given alpha
alpha = 0.2
forecast_values = ses_forecast(cpi_data['CPIAUCSL'].values, alpha)

# Plot SES with alpha=0.2
plt.figure(figsize=(10,6))
plt.plot(cpi_data.index, cpi_data, label='Original Data')
plt.plot(cpi_data.index, forecast_values, label=f'SES Forecast (alpha={alpha})', color='red')
plt.title('SES Forecast for CPI Data')
plt.legend()
plt.show()

# Define SSE calculation
def calculate_sse(data, forecast_values):
    return np.sum((data - forecast_values[:-1])**2)

# Find optimal alpha by minimizing SSE
alpha_values = np.linspace(0.001, 0.999, 100)
sse_values = []
for alpha in alpha_values:
    forecast_values = ses_forecast(cpi_data['CPIAUCSL'].values, alpha)
    sse = calculate_sse(cpi_data['CPIAUCSL'].values, forecast_values)
    sse_values.append(sse)

# Plot SSE vs Alpha
plt.figure(figsize=(10,6))
plt.plot(alpha_values, sse_values, color='purple')
plt.title('SSE vs Alpha for SES')
plt.xlabel('Alpha')
plt.ylabel('Sum of Squared Errors (SSE)')
plt.show()

# Find the optimal alpha
optimal_alpha = alpha_values[np.argmin(sse_values)]
print(f"Optimal Alpha: {optimal_alpha}")

# Calculate forecast with optimal alpha
optimal_forecast = ses_forecast(cpi_data['CPIAUCSL'].values, optimal_alpha)

# Plot forecast with optimal alpha
plt.figure(figsize=(10,6))
plt.plot(cpi_data.index, cpi_data, label='Original Data')
plt.plot(cpi_data.index, optimal_forecast, label=f'Optimal SES Forecast (alpha={optimal_alpha})', color='green')
plt.title('SES Forecast with Optimal Alpha for CPI Data')
plt.legend()
plt.show()
