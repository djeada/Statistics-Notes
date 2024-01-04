# Calculating Variance and Standard Deviation
variance = np.var(data)
std_dev = np.sqrt(variance)

# Creating a figure for the plot
plt.figure(figsize=(10, 6))

# Plotting the data points
plt.plot(data, np.zeros_like(data), 'o', label='Data Points')

# Marking the mean
plt.axvline(arithmetic_mean, color='r', linestyle='--', label=f'Mean: {arithmetic_mean:.2f}')

# Highlighting the range for standard deviation
plt.axvspan(arithmetic_mean - std_dev, arithmetic_mean + std_dev, alpha=0.3, color='yellow', label=f'Std Dev Range: {std_dev:.2f}')

# Annotations
plt.text(arithmetic_mean, 0.02, 'Mean', rotation=90, color='r')
plt.text(arithmetic_mean - std_dev, 0.02, '-1 Std Dev', rotation=90, verticalalignment='bottom')
plt.text(arithmetic_mean + std_dev, 0.02, '+1 Std Dev', rotation=90, verticalalignment='bottom')

# Enhancing the plot
plt.ylim(-0.05, 0.05)
plt.xlabel('Values')
plt.yticks([])
plt.title('Visualization of Variance and Standard Deviation')
plt.legend()

# Displaying the plot
plt.show()
