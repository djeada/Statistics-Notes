import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def generate_data(num_samples: int, x_min: float, x_max: float, true_slope: float, true_intercept: float, noise_scale: float) -> tuple:
    """
    Generates synthetic data for linear regression with added noise.

    Args:
        num_samples (int): Number of data points.
        x_min (float): Minimum value for x.
        x_max (float): Maximum value for x.
        true_slope (float): True slope of the linear relationship.
        true_intercept (float): True intercept of the linear relationship.
        noise_scale (float): Scale of the Gaussian noise.

    Returns:
        tuple: x values (np.ndarray) and y values (np.ndarray).
    """
    x = np.random.uniform(x_min, x_max, num_samples)
    y_true = true_slope * x + true_intercept
    y = y_true + np.random.normal(0, np.max(y_true) * noise_scale, num_samples)
    return x, y

def fit_and_score(x: np.ndarray, y: np.ndarray) -> tuple:
    """
    Fits a linear regression model and calculates R-squared.

    Args:
        x (np.ndarray): x values of the data.
        y (np.ndarray): y values of the data.

    Returns:
        tuple: LinearRegression model and its R-squared value.
    """
    model = LinearRegression().fit(x.reshape(-1, 1), y)
    r_squared = r2_score(y, model.predict(x.reshape(-1, 1)))
    return model, r_squared

def plot_regression_results(ax: plt.Axes, x: np.ndarray, y: np.ndarray, model: LinearRegression, title: str) -> None:
    """
    Plots the regression results on the given Axes.

    Args:
        ax (plt.Axes): Axes to plot on.
        x (np.ndarray): x values of the data.
        y (np.ndarray): y values of the data.
        model (LinearRegression): Fitted linear regression model.
        title (str): Title of the subplot.
    """
    ax.scatter(x, y, s=2)
    ax.plot(x, model.predict(x.reshape(-1, 1)), color="black")
    ax.set_ylim((0, 4))
    ax.set_title(title)

# Set random seed for reproducibility
np.random.seed(42)

# Constants
NUM_SAMPLES = 100
X_MIN, X_MAX = 0, 1
TRUE_SLOPE, TRUE_INTERCEPT = 2.0, 1.0
NOISE_SCALE_LOW, NOISE_SCALE_HIGH = 0.1, 0.5

# Generate synthetic data and fit models
x, y_low_noise = generate_data(NUM_SAMPLES, X_MIN, X_MAX, TRUE_SLOPE, TRUE_INTERCEPT, NOISE_SCALE_LOW)
_, y_high_noise = generate_data(NUM_SAMPLES, X_MIN, X_MAX, TRUE_SLOPE, TRUE_INTERCEPT, NOISE_SCALE_HIGH)
model_low_noise, r_squared_low = fit_and_score(x, y_low_noise)
model_high_noise, r_squared_high = fit_and_score(x, y_high_noise)

# Create subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Plot results
plot_regression_results(ax1, x, y_low_noise, model_low_noise, f"Low Noise (R² = {r_squared_low:.2f})")
plot_regression_results(ax2, x, y_high_noise, model_high_noise, f"High Noise (R² = {r_squared_high:.2f})")

fig.suptitle("Linear Regression: Impact of Noise on R-squared")
plt.show()
