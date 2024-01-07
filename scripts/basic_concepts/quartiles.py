import matplotlib.pyplot as plt
import numpy as np

# Define datasets
data1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 100, 110, 120])  # Wide range in 4th quartile
data2 = np.array([1, 2, 50, 60, 70, 80, 90, 100, 101, 102]) # Wide interquartile range
data3 = np.array([50, 51, 52, 53, 54, 55, 56, 57, 58, 59])  # Narrow interquartile range
data4 = np.array([1, 1, 2, 2, 3, 3, 4, 4, 50, 100])         # Data with outliers

# Create a figure and axes
fig, axs = plt.subplots(4, 1, figsize=(10, 8))

# Plot each dataset as a boxplot
axs[0].boxplot(data1, vert=False)
axs[0].set_title('Wide Range in 4th Quartile')

axs[1].boxplot(data2, vert=False)
axs[1].set_title('Wide Interquartile Range')

axs[2].boxplot(data3, vert=False)
axs[2].set_title('Narrow Interquartile Range')

axs[3].boxplot(data4, vert=False)
axs[3].set_title('Data with Outliers')

# Improve layout
plt.tight_layout()

# Show the plot
plt.show()
