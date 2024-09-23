import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem, t

# Function to calculate confidence interval
def calculate_confidence_interval(data, confidence=0.95):
    """
    Calculate the confidence interval for a given data sample.
    
    Parameters:
    - data: array-like, sample data
    - confidence: float, confidence level for the interval (default is 0.95)
    
    Returns:
    - lower_bound: float, lower bound of the confidence interval
    - mean: float, sample mean
    - upper_bound: float, upper bound of the confidence interval
    """
    n = len(data)
    mean = np.mean(data)
    std_err = sem(data)
    margin_of_error = std_err * t.ppf((1 + confidence) / 2, n - 1)
    
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    
    return lower_bound, mean, upper_bound

# Parameters for data generation
sample_size = 100
true_mean = 50
std_dev = 5

# Generate random sample data
np.random.seed(0)
data = np.random.normal(true_mean, std_dev, sample_size)

# Calculate the confidence interval
lower_bound, sample_mean, upper_bound = calculate_confidence_interval(data)

# Plotting the data and confidence interval
plt.figure(figsize=(10, 4))
plt.hist(data, bins=15, alpha=0.7, label='Sample Data')

# Plot the sample mean and confidence interval bounds
plt.axvline(sample_mean, color='red', linestyle='dashed', linewidth=2, label='Sample Mean')
plt.axvline(lower_bound, color='green', linestyle='dashed', linewidth=2, label='Lower Bound of CI')
plt.axvline(upper_bound, color='blue', linestyle='dashed', linewidth=2, label='Upper Bound of CI')

# Add labels and title
plt.title("Confidence Interval for Mean (95%)")
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Show the plot
plt.show()
