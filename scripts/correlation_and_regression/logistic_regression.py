import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

def generate_data(seed: int, num_samples: int, w_true: np.ndarray, b_true: float) -> Tuple[np.ndarray, np.ndarray]:
    """Generates synthetic data for logistic regression.

    Args:
        seed (int): Random seed for reproducibility.
        num_samples (int): Number of samples to generate.
        w_true (np.ndarray): True weights.
        b_true (float): True bias.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Feature matrix and labels.
    """
    np.random.seed(seed)
    x = np.random.normal(0, 1, (num_samples, 2))
    z = np.dot(x, w_true) + b_true
    y_true = (z > 0).astype(int)
    y = y_true + np.random.normal(0, 0.1, num_samples)
    return x, y

def sigmoid(z: np.ndarray) -> np.ndarray:
    """Sigmoid activation function.

    Args:
        z (np.ndarray): Input array.

    Returns:
        np.ndarray: Sigmoid of input array.
    """
    return 1 / (1 + np.exp(-z))

def gradient(x: np.ndarray, y: np.ndarray, w: np.ndarray) -> np.ndarray:
    """Computes the gradient for logistic regression.

    Args:
        x (np.ndarray): Feature matrix.
        y (np.ndarray): Labels.
        w (np.ndarray): Weights.

    Returns:
        np.ndarray: Gradient vector.
    """
    z = np.dot(x, w)
    return np.dot(x.T, y - sigmoid(z))

def fit_logistic_regression(x: np.ndarray, y: np.ndarray, lr: float, num_iterations: int) -> np.ndarray:
    """Fits a logistic regression model using gradient descent.

    Args:
        x (np.ndarray): Feature matrix.
        y (np.ndarray): Labels.
        lr (float): Learning rate.
        num_iterations (int): Number of iterations for gradient descent.

    Returns:
        np.ndarray: Optimized weights.
    """
    w = np.zeros(x.shape[1], dtype=np.float64)
    for i in range(num_iterations):
        w += lr * gradient(x, y, w)
    return w

def visualize_decision_boundary(x: np.ndarray, y: np.ndarray, w: np.ndarray) -> None:
    """Visualizes the decision boundary of the logistic regression.

    Args:
        x (np.ndarray): Feature matrix.
        y (np.ndarray): Labels.
        w (np.ndarray): Weights.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap="bwr", alpha=0.6)

    # Create a mesh to plot the decision boundary
    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = sigmoid(np.dot(np.c_[xx.ravel(), yy.ravel()], w)).reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.4, cmap="bwr")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("Logistic Regression with Gradient Descent")
    plt.show()

# Constants
NUM_SAMPLES = 100
W_TRUE = np.array([1, -1])
B_TRUE = 0.5
LEARNING_RATE = 0.1
NUM_ITERATIONS = 1000

# Generate synthetic data
x, y = generate_data(42, NUM_SAMPLES, W_TRUE, B_TRUE)

# Perform gradient descent
w = fit_logistic_regression(x, y, LEARNING_RATE, NUM_ITERATIONS)

# Visualize the results
visualize_decision_boundary(x, y, w)
