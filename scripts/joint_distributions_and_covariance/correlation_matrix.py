"""Correlation matrix of four related variables, shown as an annotated heatmap."""

import numpy as np
import matplotlib.pyplot as plt


def generate_random_data(seed: int, num_samples: int) -> np.ndarray:
    """Generate four variables where x3 and x4 depend on x1 and x2.

    Args:
        seed: Seed for the random number generator.
        num_samples: Number of observations per variable.

    Returns:
        Array of shape (4, num_samples); each row is one variable.
    """
    rng = np.random.default_rng(seed)
    x1 = rng.normal(0, 1, num_samples)
    x2 = rng.normal(0, 1, num_samples)
    x3 = x1 + x2 + rng.normal(0, 0.5, num_samples)
    x4 = 2 * x1 - x2 + rng.normal(0, 0.5, num_samples)
    return np.array([x1, x2, x3, x4])


def calculate_correlation_matrix(data: np.ndarray) -> np.ndarray:
    """Return the sample correlation matrix of the rows of ``data``."""
    return np.corrcoef(data)


def visualize_correlation_matrix(matrix: np.ndarray) -> None:
    """Show the correlation matrix as an annotated heatmap."""
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap="coolwarm")

    num_variables = matrix.shape[0]
    labels = [f"X{i + 1}" for i in range(num_variables)]
    ax.set_xticks(np.arange(num_variables))
    ax.set_yticks(np.arange(num_variables))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    ax.set_title("Correlation Matrix")

    for i in range(num_variables):
        for j in range(num_variables):
            ax.text(j, i, f"{matrix[i, j]:.2f}", ha="center", va="center", color="w")

    fig.tight_layout()
    plt.show()


def main() -> None:
    data = generate_random_data(42, 100)
    matrix = calculate_correlation_matrix(data)
    print(np.round(matrix, 3))
    visualize_correlation_matrix(matrix)


if __name__ == "__main__":
    main()
