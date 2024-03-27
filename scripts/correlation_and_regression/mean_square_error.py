import numpy as np
import matplotlib.pyplot as plt

def generate_data(slope: float, intercept: float, noise_scale: float, num_points: int, x_range: tuple) -> tuple:
    """
    Generates linear data with added Gaussian noise.

    Args:
        slope (float): Slope of the linear relationship.
        intercept (float): Intercept of the linear relationship.
        noise_scale (float): Standard deviation of the Gaussian noise.
        num_points (int): Number of data points to generate.
        x_range (tuple): The range of x values.

    Returns:
        tuple: x values and y values of the generated data.
    """
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = slope * x + intercept + np.random.normal(0, noise_scale, num_points)
    return x, y

def calculate_mse(y_actual: np.ndarray, y_predicted: np.ndarray) -> float:
    """
    Calculates the Mean Squared Error (MSE) between actual and predicted values.

    Args:
        y_actual (np.ndarray): Actual y values.
        y_predicted (np.ndarray): Predicted y values.

    Returns:
        float: Calculated MSE.
    """
    return np.mean((y_actual - y_predicted) ** 2)

def plot_data_with_mse(x: np.ndarray, y: np.ndarray, true_slope: float, true_intercept: float, ax: plt.Axes, title: str) -> None:
    """
    Plots the data and a line representing the true relationship, annotating the plot with MSE.

    Args:
        x (np.ndarray): x values of the data.
        y (np.ndarray): y values of the data.
        true_slope (float): Slope of the true relationship.
        true_intercept (float): Intercept of the true relationship.
        ax (plt.Axes): The axes to plot on.
        title (str): Title for the subplot.
    """
    ax.scatter(x, y, label=f"MSE = {calculate_mse(y, true_slope * x + true_intercept):.2f}")
    ax.plot(x, true_slope * x + true_intercept, color="r", label="True Line")
    ax.legend()
    ax.set_title(title)

# Generating two sets of data
x = np.linspace(0, 10, 100)
y1, y2 = generate_data(3, 1, 1, 100, (0, 10)), generate_data(3, 1, 5, 100, (0, 10))

# Creating two subplots
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Plotting the data sets
plot_data_with_mse(x, y1, 3, 1, ax[0], "Data with Small MSE")
plot_data_with_mse(x, y2, 3, 1, ax[1], "Data with Large MSE")

plt.show()
