import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# 1. SARIMA Model Parameters
p, d, q = 1, 1, 1  # Non-seasonal AR, differencing, and MA orders
P, D, Q, S = 1, 1, 1, 12  # Seasonal AR, differencing, MA orders, and seasonal period (S = 12 for monthly seasonality)

# 2. Generate Mock Time Series Data with Seasonal Component
np.random.seed(42)
n = 120  # 10 years of monthly data

# Simulating a seasonal time series: a linear trend + seasonal pattern + noise
time = np.arange(n)
seasonal_pattern = 10 * np.sin(2 * np.pi * time / S)  # Seasonal component
trend = 0.5 * time  # Linear trend
noise = np.random.normal(scale=3, size=n)  # Random noise

# Combine trend, seasonality, and noise to create the time series
time_series = trend + seasonal_pattern + noise
time_series = pd.Series(time_series)

# 3. Fit SARIMA Model to the Generated Data
sarima_model = SARIMAX(time_series, order=(p, d, q), seasonal_order=(P, D, Q, S))
sarima_model_fit = sarima_model.fit(disp=False)
predictions = sarima_model_fit.predict(start=12, end=n-1)

# 4. Plot the Generated Data and SARIMA Model Predictions
plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Generated Data', color='blue')
plt.plot(predictions, label='SARIMA Predictions', color='red', linestyle='dashed')
plt.title('Generated Time Series with Seasonality and SARIMA Model Predictions')
plt.xlabel('Time Point')
plt.ylabel('Value')
plt.legend()
plt.show()
