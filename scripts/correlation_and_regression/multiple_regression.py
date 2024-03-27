import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_synthetic_data(num_samples: int, x_min: float, x_max: float, 
                            true_coefficients: np.ndarray, true_intercept: float, 
                            noise_scale: float) -> tuple:
    """Generates synthetic data for multiple linear regression.

    Args:
        num_samples (int): Number of data points.
        x_min (float): Minimum value for x.
        x_max (float): Maximum value for x.
        true_coefficients (np.ndarray): True coefficients for the linear model.
        true_intercept (float): True intercept for the linear model.
        noise_scale (float): Scale of the Gaussian noise.

    Returns:
        tuple: Tuple of feature matrix X and response vector Y.
    """
    X = np.random.uniform(x_min, x_max, size=(num_samples, len(true_coefficients)))
    Y_true = true_intercept + X.dot(true_coefficients)
    Y = Y_true + np.random.normal(0, noise_scale, size=num_samples)
    return X, Y

def fit_linear_model(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """Fits a linear model using least squares.

    Args:
        X (np.ndarray): Feature matrix.
        Y (np.ndarray): Response vector.

    Returns:
        np.ndarray: Fitted coefficients.
    """
    X_with_bias = np.hstack([np.ones((X.shape[0], 1)), X])
    coefficients, _, _, _ = np.linalg.lstsq(X_with_bias, Y, rcond=None)
    return coefficients

def visualize_model(X: np.ndarray, Y: np.ndarray, coefficients: np.ndarray) -> None:
    """Visualizes the data and the fitted plane.

    Args:
        X (np.ndarray): Feature matrix.
        Y (np.ndarray): Response vector.
        coefficients (np.ndarray): Fitted coefficients.
    """
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(X[:, 0], X[:, 1], Y, s=2, label='Data Points')

    x_surf, y_surf = np.meshgrid(
        np.linspace(X[:, 0].min(), X[:, 0].max(), 20),
        np.linspace(X[:, 1].min(), X[:, 1].max(), 20)
    )
    z_surf = coefficients[0] + coefficients[1] * x_surf + coefficients[2] * y_surf
    ax.plot_surface(x_surf, y_surf, z_surf, alpha=0.2, label='Fitted Plane')

    ax.set_xlabel("X1")
    ax.set_ylabel("X2")
    ax.set_zlabel("Y")
    ax.set_title("Multiple Linear Regression Using Numpy")
    ax.legend()
    plt.show()

# Set random seed for reproducibility
np.random.seed(42)

# Constants
NUM_SAMPLES = 1000
X_MIN, X_MAX = 0, 1
TRUE_INTERCEPT = 1.0
TRUE_COEFFICIENTS = np.array([2.0, -3.0, 0.5])
NOISE_SCALE = 0.5

# Generate synthetic data
X, Y = generate_synthetic_data(NUM_SAMPLES, X_MIN, X_MAX, TRUE_COEFFICIENTS, TRUE_INTERCEPT, NOISE_SCALE)

# Calculate coefficients using numpy
coefficients = fit_linear_model(X, Y)

# Visualize the data and fitted plane
visualize_model(X, Y, coefficients)
