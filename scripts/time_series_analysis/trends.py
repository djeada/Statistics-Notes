import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Generate time axis
time_points = np.linspace(0, 100, 500)  # 500 points over a period of 100 units

# Generate downward trend with cyclic component and noise
downward_trend = 100 - 0.5 * time_points + 5 * np.sin(2 * np.pi * time_points / 20) + np.random.randn(len(time_points)) * 2

# Generate upward trend with cyclic component and noise
upward_trend = 20 + 0.5 * time_points + 5 * np.sin(2 * np.pi * time_points / 20) + np.random.randn(len(time_points)) * 2

# Calculate linear fits for trends
downward_slope, downward_intercept, _, _, _ = linregress(time_points, downward_trend)
upward_slope, upward_intercept, _, _, _ = linregress(time_points, upward_trend)

# Generate fit lines
downward_fit = downward_slope * time_points + downward_intercept
upward_fit = upward_slope * time_points + upward_intercept

# Plotting with corrected arrow position
fig, axs = plt.subplots(1, 2, figsize=(15, 5), constrained_layout=True)

# Downward trend plot
axs[0].plot(time_points, downward_trend, color='blue', label='Data')
axs[0].plot(time_points, downward_fit, color='red', linestyle='--', label='Trend Line')
axs[0].set_title('Downward Trend with Cyclic Pattern', pad=15)
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Value')
axs[0].grid()
axs[0].annotate('Trend ↓', xy=(30, downward_fit[300]), xytext=(20, downward_fit[300]),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
axs[0].legend()

# Upward trend plot
axs[1].plot(time_points, upward_trend, color='green', label='Data')
axs[1].plot(time_points, upward_fit, color='red', linestyle='--', label='Trend Line')
axs[1].set_title('Upward Trend with Cyclic Pattern', pad=15)
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Value')
axs[1].grid()
axs[1].annotate('Trend ↑', xy=(80, upward_fit[-1]), xytext=(70, upward_fit[-1] - 10),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
axs[1].legend()

plt.show()
