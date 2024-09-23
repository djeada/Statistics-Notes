import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Generate noisy sine wave data
def generate_sine_data(num_samples: int, noise_scale: float) -> tuple:
    """
    Generates noisy sine wave data.

    Args:
        num_samples (int): Number of data points.
        noise_scale (float): Standard deviation of Gaussian noise added to sine wave.

    Returns:
        tuple: x values (np.ndarray), y values (np.ndarray).
    """
    X = 2 * np.pi * np.random.rand(num_samples)
    y = np.sin(X) + np.random.normal(0, noise_scale, num_samples)
    return X, y

# Step 2: Fit a linear regression model
def fit_linear_model(X: np.ndarray, y: np.ndarray) -> LinearRegression:
    """
    Fits a linear regression model to the data.

    Args:
        X (np.ndarray): Feature matrix.
        y (np.ndarray): Target vector.

    Returns:
        LinearRegression: Fitted linear model.
    """
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y)
    return model

# Step 3: Plot the data, regression line, and error lines
def plot_results_with_error_lines(X: np.ndarray, y: np.ndarray, model: LinearRegression, num_points_fit: int) -> None:
    """
    Plots the original data, regression line, and error lines.

    Args:
        X (np.ndarray): Original x values.
        y (np.ndarray): Original y values.
        model (LinearRegression): Fitted linear model.
        num_points_fit (int): Number of points for fitting line.
    """
    plt.figure(figsize=(10, 6))

    # Scatter plot of actual data
    plt.scatter(X, y, label='Actual Data', color='blue')

    # Plot regression line
    X_fit = np.linspace(0, 2 * np.pi, num_points_fit)
    y_pred = model.predict(X_fit.reshape(-1, 1))
    plt.plot(X_fit, y_pred, label='Regression Line', color='red')

    # Draw error lines
    y_pred_actual = model.predict(X.reshape(-1, 1))
    for xp, yp, y_hat in zip(X, y, y_pred_actual):
        plt.plot([xp, xp], [yp, y_hat], color='gray', linestyle='dotted')

    # Calculate and display regression metrics
    mse = mean_squared_error(y, y_pred_actual)
    rmse = np.sqrt(mse)
    r2 = r2_score(y, y_pred_actual)
    plt.title(f'Linear Regression with Error Lines\nMSE: {mse:.2f}, RMSE: {rmse:.2f}, R²: {r2:.2f}')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# Main execution function to bring everything together
def main():
    # Step 1: Generate data
    X, y = generate_sine_data(100, 0.15)

    # Step 2: Fit the linear regression model
    model = fit_linear_model(X, y)

    # Step 3: Plot the data and results
    plot_results_with_error_lines(X, y, model, 100)

# Execute the main function
if __name__ == "__main__":
    main()
