import numpy as np
import matplotlib.pyplot as plt

def generate_random_data(seed: int, num_samples: int) -> np.ndarray:
    """Generates random data for correlation analysis.

    Args:
        seed (int): Seed for random number generation for reproducibility.
        num_samples (int): Number of samples to generate.

    Returns:
        np.ndarray: Generated data matrix.
    """
    np.random.seed(seed)
    x1 = np.random.normal(0, 1, num_samples)
    x2 = np.random.normal(0, 1, num_samples)
    x3 = x1 + x2 + np.random.normal(0, 0.5, num_samples)
    x4 = 2 * x1 - x2 + np.random.normal(0, 0.5, num_samples)
    return np.array([x1, x2, x3, x4])

def calculate_correlation_matrix(data: np.ndarray) -> np.ndarray:
    """Calculates the correlation matrix from the data.

    Args:
        data (np.ndarray): Data matrix.

    Returns:
        np.ndarray: Correlation matrix.
    """
    return np.corrcoef(data)

def visualize_correlation_matrix(corr_matrix: np.ndarray) -> None:
    """Visualizes the correlation matrix as a heatmap.

    Args:
        corr_matrix (np.ndarray): Correlation matrix to visualize.
    """
    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix, cmap="coolwarm")

    # Customize plot
    num_variables = corr_matrix.shape[0]
    ax.set_xticks(np.arange(num_variables))
    ax.set_yticks(np.arange(num_variables))
    ax.set_xticklabels([f"X{i+1}" for i in range(num_variables)])
    ax.set_yticklabels([f"X{i+1}" for i in range(num_variables)])
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    ax.set_title("Correlation Matrix")

    # Add text annotations to heatmap
    for i in range(num_variables):
        for j in range(num_variables):
            text = ax.text(j, i, f"{corr_matrix[i, j]:.2f}", ha="center", va="center", color="w")

    plt.show()

# Generate, calculate, and visualize data
data = generate_random_data(42, 100)
corr_matrix = calculate_correlation_matrix(data)
visualize_correlation_matrix(corr_matrix)
