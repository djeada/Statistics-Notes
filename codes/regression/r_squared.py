import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Set seed for reproducibility
np.random.seed(42)

# Constants
NUM_SAMPLES = 100
X_MIN = 0
X_MAX = 1
TRUE_SLOPE = 2.0
TRUE_INTERCEPT = 1.0
NOISE_SCALE = 0.1

# Generate synthetic data
x = np.random.uniform(X_MIN, X_MAX, NUM_SAMPLES)
y_true = TRUE_SLOPE * x + TRUE_INTERCEPT
y_noise = np.max(y_true) * NOISE_SCALE
y = y_true + np.random.normal(0, y_noise, NUM_SAMPLES)

# Fit linear regression model
model = LinearRegression().fit(x.reshape(-1, 1), y)

# Calculate R-squared
r_squared = r2_score(y, model.predict(x.reshape(-1, 1)))

# Visualize the data and fitted line
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Plot data and regression line with low r-squared
y_low_r2 = y_true + np.random.normal(0, 2 * y_noise, NUM_SAMPLES)
model_low_r2 = LinearRegression().fit(x.reshape(-1, 1), y_low_r2)
r_squared_low = r2_score(y_low_r2, model_low_r2.predict(x.reshape(-1, 1)))

ax1.scatter(x, y_low_r2, s=2)
ax1.plot(x, model_low_r2.predict(x.reshape(-1, 1)), color='black')
ax1.set_ylim((0, 4))
ax1.set_title(f"Low R-squared ({r_squared_low:.2f})")

# Plot data and regression line with high r-squared
y_high_r2 = y_true + np.random.normal(0, 0.1 * y_noise, NUM_SAMPLES)
model_high_r2 = LinearRegression().fit(x.reshape(-1, 1), y_high_r2)
r_squared_high = r2_score(y_high_r2, model_high_r2.predict(x.reshape(-1, 1)))

ax2.scatter(x, y_high_r2, s=2)
ax2.plot(x, model_high_r2.predict(x.reshape(-1, 1)), color='black')
ax2.set_ylim((0, 4))
ax2.set_title(f"High R-squared ({r_squared_high:.2f})")

fig.suptitle(f"R-squared Comparison: Low vs High ({r_squared:.2f})")
plt.show()
