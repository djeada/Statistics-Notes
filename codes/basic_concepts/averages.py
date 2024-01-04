import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Sample data
data = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Arithmetic Mean
arithmetic_mean = np.mean(data)

# Weighted Mean
weights = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2])  # arbitrary weights
weighted_mean = np.average(data, weights=weights)

# Geometric Mean
geometric_mean = stats.gmean(data)

# Median
median = np.median(data)

# Mode
mode = stats.mode(data)[0][0]

# Plotting
plt.figure(figsize=(10, 6))

# Plotting data points
plt.plot(data, np.zeros_like(data), 'o', label='Data Points')

# Marking the Arithmetic Mean
plt.axvline(arithmetic_mean, color='r', linestyle='--', label=f'Arithmetic Mean: {arithmetic_mean:.2f}')

# Marking the Weighted Mean
plt.axvline(weighted_mean, color='g', linestyle='-.', label=f'Weighted Mean: {weighted_mean:.2f}')

# Marking the Geometric Mean
plt.axvline(geometric_mean, color='b', linestyle=':', label=f'Geometric Mean: {geometric_mean:.2f}')

# Marking the Median
plt.axvline(median, color='y', linestyle='-', label=f'Median: {median}')

# Marking the Mode
plt.axvline(mode, color='m', linestyle='-', label=f'Mode: {mode}', linewidth=2)

# Annotations
plt.text(arithmetic_mean, 0.02, 'Arithmetic Mean', rotation=90, color='r')
plt.text(weighted_mean, 0.02, 'Weighted Mean', rotation=90, color='g')
plt.text(geometric_mean, 0.02, 'Geometric Mean', rotation=90, color='b')
plt.text(median, 0.02, 'Median', rotation=90, color='y')
plt.text(mode, 0.02, 'Mode', rotation=90, color='m')

# Enhancing the plot
plt.ylim(-0.05, 0.05)
plt.xlabel('Values')
plt.yticks([])
plt.title('Visualization of Different Types of Averages')
plt.legend()

# Displaying the plot
plt.show()
