import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree

def generate_random_points(num_points: int, area_bounds: tuple) -> np.ndarray:
    """
    Generates random points within specified bounds.
    """
    x_min, x_max, y_min, y_max = area_bounds
    x_coords = np.random.uniform(x_min, x_max, num_points)
    y_coords = np.random.uniform(y_min, y_max, num_points)
    return np.column_stack((x_coords, y_coords))

def nearest_neighbor_analysis(points: np.ndarray) -> float:
    """
    Calculates the average nearest neighbor distance among the points.
    """
    tree = KDTree(points)
    distances, _ = tree.query(points, k=2)  # The nearest neighbor to each point (excluding itself)
    return np.mean(distances[:, 1])  # Exclude distance to self (always 0)

def plot_points(points: np.ndarray, title: str) -> None:
    """
    Plots the generated points on a scatter plot.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(points[:, 0], points[:, 1], marker='o', c='blue', edgecolor='k')
    plt.title(title)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()

# Generate and analyze random points
num_points = 100
area_bounds = (0, 100, 0, 100)  # Example: 100x100 square area
random_points = generate_random_points(num_points, area_bounds)
avg_nn_distance = nearest_neighbor_analysis(random_points)

# Plot the points and print the average nearest neighbor distance
plot_points(random_points, "Random Point Process in Geostatistics")
print(f"Average Nearest Neighbor Distance: {avg_nn_distance:.2f}")
