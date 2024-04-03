from scipy.stats import norm

# Define the plot for p-values
def plot_p_value(ax, test_type, sample_statistic, alpha=0.05):
    # X values
    x = np.linspace(-4, 4, 1000)
    # Y values for the normal distribution
    y = norm.pdf(x)

    # Plot the normal distribution
    ax.plot(x, y, color='green')

    # Calculate the p-value based on the test type and sample statistic
    if test_type == 'left-tailed':
        # Shade the area of the left tail up to the sample statistic
        p_value_area = x[x <= sample_statistic]
        p_value = norm.cdf(sample_statistic)
    else:  # right-tailed
        # Shade the area of the right tail from the sample statistic
        p_value_area = x[x >= sample_statistic]
        p_value = 1 - norm.cdf(sample_statistic)

    # Fill the p-value area
    ax.fill_between(p_value_area, norm.pdf(p_value_area), color='purple' if test_type == 'left-tailed' else 'blue', alpha=0.5)

    # Add line and text for sample statistic
    ax.axvline(sample_statistic, color='black', linestyle='dashed', linewidth=1)
    ax.text(sample_statistic, 0.02, f'sample statistic\n{sample_statistic:.2f}', horizontalalignment='center', color='black')
    
    # Add annotations for p-value
    ax.annotate('p-value', xy=(sample_statistic, 0.02), xytext=(sample_statistic - 1 if test_type == 'left-tailed' else sample_statistic + 1, 0.1),
                arrowprops=dict(facecolor='black', shrink=0.05), horizontalalignment='center', color='black')

    # Set title based on the test type
    ax.set_title(f"{test_type.capitalize()} Test")

    # Set labels
    ax.set_xlabel('sample statistic')
    ax.set_ylabel('density')

    # Return the calculated p-value
    return p_value

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Example sample statistics for illustration
left_sample_statistic = -1.65  # Typically, a value for a left-tailed test
right_sample_statistic = 1.65  # Typically, a value for a right-tailed test

# Plot p-values
left_p_value = plot_p_value(ax1, 'left-tailed', left_sample_statistic)
right_p_value = plot_p_value(ax2, 'right-tailed', right_sample_statistic)

# Show plot
plt.tight_layout()
plt.show()

# Print calculated p-values
print(f"Calculated p-value for the left-tailed test: {left_p_value:.4f}")
print(f"Calculated p-value for the right-tailed test: {right_p_value:.4f}")
