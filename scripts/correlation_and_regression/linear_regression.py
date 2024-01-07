import matplotlib.pyplot as plt
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Constants
NUM_SAMPLES = 1000
X_MIN = 0
X_MAX = 1
TRUE_SLOPE = 2.0
TRUE_INTERCEPT = 1.0
NOISE_SCALE = 0.073

# Generate synthetic data
x = np.random.uniform(X_MIN, X_MAX, NUM_SAMPLES)
y_true = TRUE_SLOPE * x + TRUE_INTERCEPT
y_noise = np.max(y_true) * NOISE_SCALE
y = y_true + np.random.normal(0, y_noise, NUM_SAMPLES)

# Calculate coefficients using statistics formulas
# slope = (y_std / x_std) * r
# intercept = y_mean - slope * x_mean
x_std = np.std(x)
y_std = np.std(y)
r = np.corrcoef(x, y)
slope = y_std / x_std * r[0, 1]
intercept = np.mean(y) - slope * np.mean(x)

# Visualize the data and fitted line
plt.figure(figsize=(10, 5))
plt.scatter(x, y, s=2)
plt.plot(x, slope * x + intercept, color="black")

# Add formula to legend
legend_text = f"y = {slope:.2f}x + {intercept:.2f}"

plt.legend([legend_text])

plt.ylim((0, 3.5))
plt.title("Linear Regression Using Statistics Formulas")
plt.show()
