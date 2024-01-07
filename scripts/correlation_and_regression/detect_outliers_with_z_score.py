import numpy as np


def detect_outliers_with_zscore(data, threshold=1):
    """
    Detects outliers in the data using z-scores.

    Parameters:
    data (list or numpy array): The data to analyze for outliers.
    threshold (float): The z-score threshold to consider as an outlier.

    Returns:
    outliers (list): A list of detected outliers.
    """
    data = np.array(data)
    mean = np.mean(data)
    std = np.std(data)
    z_scores = (data - mean) / std

    outliers = data[np.abs(z_scores) > threshold]

    return outliers.tolist()


# Example usage:
data = [12, 15, 18, 20, 24, 28, 30, 110, 130]
outliers = detect_outliers_with_zscore(data)
print("Outliers:", outliers)
