import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Step 1: Generate Mock Monthly Temperature Data
np.random.seed(42)
years = 5
months_per_year = 12
total_months = years * months_per_year

# Simulate average monthly temperature (in degrees Celsius) with seasonality and trend
time_index = pd.date_range(start='2015-01-01', periods=total_months, freq='M')
temperature = 10 + 0.5 * np.arange(total_months)  # Gradual increase to simulate global warming
seasonal_effect = np.sin(np.linspace(0, 2 * np.pi, months_per_year)) * 5  # Seasonal variation
random_noise = np.random.normal(0, 1, total_months)  # Random noise
temperature = temperature + np.tile(seasonal_effect, years) + random_noise

# Create a pandas Series for the temperature data
temperature_data = pd.Series(temperature, index=time_index)

# Step 2: Fit an Exponential Smoothing Model (Holt-Winters)
model = ExponentialSmoothing(temperature_data, trend='additive', seasonal='additive', seasonal_periods=12)
model_fit = model.fit()

# Step 3: Forecast Future Values (next 2 years)
forecast_length = 24  # Forecast for the next 24 months (2 years)
forecast = model_fit.forecast(forecast_length)

# Step 4: Plot the Results
plt.figure(figsize=(15, 6))
plt.plot(temperature_data, label='Actual Temperature', color='blue')
plt.plot(forecast, label='Forecasted Temperature', color='green', linestyle='dashed')
plt.title('Temperature Time Series and Forecast (Holt-Winters Exponential Smoothing)')
plt.xlabel('Year')
plt.ylabel('Temperature (Celsius)')
plt.legend()
plt.show()
