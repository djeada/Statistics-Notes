import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Constants
NUM_SAMPLES = 1000
X_MIN = 0
X_MAX = 1
TRUE_INTERCEPT = 1.0
TRUE_COEFFICIENTS = np.array([2.0, -3.0, 0.5])
NOISE_SCALE = 0.5

# Generate synthetic data
X = np.random.uniform(X_MIN, X_MAX, size=(NUM_SAMPLES, len(TRUE_COEFFICIENTS)))
Y_true = TRUE_INTERCEPT + X.dot(TRUE_COEFFICIENTS)
Y_noise = np.max(Y_true) * NOISE_SCALE
Y = Y_true + np.random.normal(0, Y_noise, size=NUM_SAMPLES)

# Calculate coefficients using numpy
X_with_bias = np.hstack([np.ones((NUM_SAMPLES, 1)), X])
coefficients, _, _, _ = np.linalg.lstsq(X_with_bias, Y, rcond=None)

# Visualize the data and fitted plane
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X[:, 0], X[:, 1], Y, s=2)
x_surf, y_surf = np.meshgrid(np.linspace(X_MIN, X_MAX, 10), np.linspace(X_MIN, X_MAX, 10))
z_surf = coefficients[0] + coefficients[1] * x_surf + coefficients[2] * y_surf
ax.plot_surface(x_surf, y_surf, z_surf, alpha=0.2)

# Add formula to legend
legend_text = f"y = {coefficients[0]:.2f} + {coefficients[1]:.2f}x1 + {coefficients[2]:.2f}x2"
              
ax.legend([legend_text])

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')
ax.set_title('Multiple Linear Regression Using Numpy')

plt.show()
