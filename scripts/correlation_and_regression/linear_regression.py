import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple

def generate_synthetic_data(num_samples: int, x_min: float, x_max: float, 
                            true_slope: float, true_intercept: float, 
                            noise_scale: float) -> Tuple[np.ndarray, np.ndarray]:
    """Generates synthetic linear data with noise.

    Args:
        num_samples (int): Number of data points.
        x_min (float): Minimum value for x.
        x_max (float): Maximum value for x.
        true_slope (float): Slope of the true linear relationship.
        true_intercept (float): Intercept of the true linear relationship.
        noise_scale (float): Scale of noise to be added.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Tuple of x values and corresponding y values.
    """
    x = np.random.uniform(x_min, x_max, num_samples)
    y_true = true_slope * x + true_intercept
    noise = np.random.normal(0, np.max(y_true) * noise_scale, num_samples)
    return x, y_true + noise

def compute_linear_regression(x: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
    """Computes the slope and intercept for linear regression using statistics formulas.

    Args:
        x (np.ndarray): Independent variable.
        y (np.ndarray): Dependent variable.

    Returns:
        Tuple[float, float]: Slope and intercept of the regression line.
    """
    x_mean, y_mean = np.mean(x), np.mean(y)
    x_std, y_std = np.std(x), np.std(y)
    correlation = np.corrcoef(x, y)[0, 1]
    slope = (y_std / x_std) * correlation
    intercept = y_mean - slope * x_mean
    return slope, intercept

def plot_data_with_fit(x: np.ndarray, y: np.ndarray, slope: float, intercept: float) -> None:
    """Plots the data points and the fitted linear regression line.

    Args:
        x (np.ndarray): Independent variable.
        y (np.ndarray): Dependent variable.
        slope (float): Slope of the fitted line.
        intercept (float): Intercept of the fitted line.
    """
    plt.figure(figsize=(10, 5))
    plt.scatter(x, y, s=2, label='Data Points')
    plt.plot(x, slope * x + intercept, color="black", label=f'Fit: y = {slope:.2f}x + {intercept:.2f}')
    plt.ylim((0, 3.5))
    plt.title("Linear Regression Using Statistics Formulas")
    plt.legend()
    plt.show()

# Set random seed for reproducibility
np.random.seed(42)

# Constants
NUM_SAMPLES = 1000
X_MIN, X_MAX = 0, 1
TRUE_SLOPE, TRUE_INTERCEPT = 2.0, 1.0
NOISE_SCALE = 0.073

# Generate data
x, y = generate_synthetic_data(NUM_SAMPLES, X_MIN, X_MAX, TRUE_SLOPE, TRUE_INTERCEPT, NOISE_SCALE)

# Compute coefficients
slope, intercept = compute_linear_regression(x, y)

# Visualize
plot_data_with_fit(x, y, slope, intercept)
