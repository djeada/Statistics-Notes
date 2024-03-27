import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

def find_outliers_using_z_score(data: List[float], threshold: float = 1.0) -> Tuple[List[float], np.ndarray]:
    """
    Identifies outliers in a dataset based on z-scores and visualizes the results.

    Parameters:
    data (List[float]): The dataset to analyze for outliers.
    threshold (float, optional): The z-score threshold to classify outliers. Defaults to 1.0.

    Returns:
    Tuple[List[float], np.ndarray]: A tuple containing the list of outliers and the z-scores of the data.

    Raises:
    ValueError: If the provided data list is empty or contains a single element.
    """
    if len(data) < 2:
        raise ValueError("Data must contain at least two elements to detect outliers.")

    data_array = np.array(data)
    mean, std = np.mean(data_array), np.std(data_array)
    z_scores = (data_array - mean) / std

    outliers = data_array[np.abs(z_scores) > threshold]

    return outliers.tolist(), z_scores

def plot_data_with_outliers(data: List[float], outliers: List[float], z_scores: np.ndarray) -> None:
    """
    Plots the data, highlighting outliers.

    Parameters:
    data (List[float]): The original dataset.
    outliers (List[float]): List of detected outliers.
    z_scores (np.ndarray): The computed z-scores for the data.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(data)), data, label='Data Points', color='blue')
    outlier_indices = [i for i, point in enumerate(data) if point in outliers]
    plt.scatter(outlier_indices, outliers, label='Outliers', color='red')
    plt.axhline(y=np.mean(data), color='green', linestyle='--', label='Mean')
    plt.title('Data Points and Detected Outliers')
    plt.xlabel('Index')
    plt.ylabel('Data Value')
    plt.legend()
    plt.show()

    # Optional: Plot Z-scores if desired for educational purposes
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(z_scores)), z_scores, color='gray')
    plt.axhline(y=threshold, color='red', linestyle='--', label='Positive Threshold')
    plt.axhline(y=-threshold, color='red', linestyle='--', label='Negative Threshold')
    plt.title('Z-scores of Data Points')
    plt.xlabel('Index')
    plt.ylabel('Z-score')
    plt.legend()
    plt.show()

# Example usage
data = [12, 15, 18, 20, 24, 28, 30, 110, 130]
try:
    outliers, z_scores = find_outliers_using_z_score(data)
    print("Outliers:", outliers)
    plot_data_with_outliers(data, outliers, z_scores)
except ValueError as e:
    print("Error:", e)
