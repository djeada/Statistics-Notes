import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg

# 1. AR(2) Model Parameters
alpha = 3        # Constant term
beta1 = 0.6      # Coefficient for X_{t-1}
beta2 = -0.2     # Coefficient for X_{t-2}

# 2. Generate Mock Time Series Data
np.random.seed(42)  # Ensure reproducibility
n = 100  # Number of data points

# Start with initial values
X = [10, 5]  # Initial values: X_{t-1} = 10, X_{t-2} = 5

# Generate time series using the AR(2) equation
for t in range(2, n):
    epsilon_t = np.random.normal()  # Random noise (white noise)
    X_t = alpha + beta1 * X[t-1] + beta2 * X[t-2] + epsilon_t  # AR(2) equation
    X.append(X_t)

# Convert to pandas Series for convenience
time_series = pd.Series(X)

# 3. Fit AR(2) Model to the Generated Data
model = AutoReg(time_series, lags=2)
model_fit = model.fit()
predictions = model_fit.predict(start=2, end=n-1)

# 4. Plot the Generated Data and AR(2) Predictions
plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Generated Data', color='blue')
plt.plot(predictions, label='AR(2) Predictions', color='red', linestyle='dashed')
plt.title('Generated Time Series and AR(2) Model Predictions')
plt.xlabel('Time Point')
plt.ylabel('Value')
plt.legend()
plt.show()
