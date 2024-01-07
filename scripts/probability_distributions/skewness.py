import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt

# Generate random data with a skewed distribution
data1 = np.random.gamma(4, 1, 1000)
data2 = np.random.normal(6, 2, 1000)

# Calculate the skewness of the data
skewness1 = skew(data1)
skewness2 = skew(data2)

# Plot a histogram of the data
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(data1, bins=30, alpha=0.5, color="blue")
ax1.axvline(np.mean(data1), color="red", linestyle="dashed", linewidth=1)
ax1.axvline(np.median(data1), color="green", linestyle="dashed", linewidth=1)
ax1.set_title(f"Skewness: {skewness1:.2f}", fontsize=16)
ax1.set_xlabel("Data Values")
ax1.set_ylabel("Frequency")

ax2.hist(data2, bins=30, alpha=0.5, color="orange")
ax2.axvline(np.mean(data2), color="red", linestyle="dashed", linewidth=1)
ax2.axvline(np.median(data2), color="green", linestyle="dashed", linewidth=1)
ax2.set_title(f"Skewness: {skewness2:.2f}", fontsize=16)
ax2.set_xlabel("Data Values")
ax2.set_ylabel("Frequency")

# Show the plot
plt.show()
