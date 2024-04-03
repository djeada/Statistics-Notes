# Define the plot for the null hypothesis illustration
def plot_null_hypothesis(ax, sample_statistic):
    # X values
    x = np.linspace(-4, 4, 1000)
    # Y values for the normal distribution under the null hypothesis
    y = norm.pdf(x)

    # Plot the normal distribution
    ax.plot(x, y, color='green')

    # Add line and text for the sample statistic
    ax.axvline(sample_statistic, color='red', linestyle='dashed', linewidth=2)
    ax.text(sample_statistic, 0.02, f'Sample Statistic\n{sample_statistic:.2f}',
            horizontalalignment='center', color='red', bbox=dict(facecolor='none', edgecolor='red', boxstyle='round,pad=0.5'))

    # Highlight the region that would be more extreme than the sample statistic
    extreme_region = x[x > np.abs(sample_statistic)]
    ax.fill_between(extreme_region, norm.pdf(extreme_region), color='orange', alpha=0.5)

    # Set title and labels
    ax.set_title('Null Hypothesis Distribution')
    ax.set_xlabel('Sample Statistic')
    ax.set_ylabel('Probability Density')

# Create figure and axes
fig, ax = plt.subplots(1, figsize=(10, 5))

# Example sample statistic for illustration
sample_statistic = 2.0  # A value indicating the observed test statistic

# Plot the null hypothesis illustration
plot_null_hypothesis(ax, sample_statistic)

# Show plot
plt.tight_layout()
plt.show()
