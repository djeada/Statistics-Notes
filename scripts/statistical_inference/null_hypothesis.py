import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Step 1: Calculation of critical values and rejection regions
def calculate_critical_values(alpha=0.05):
    """
    Calculate the critical values for a two-tailed hypothesis test.
    
    Parameters:
        alpha (float): The significance level for the hypothesis test.
        
    Returns:
        float: The critical value for a two-tailed test.
    """
    return norm.ppf(1 - alpha / 2)

# Step 2: Plotting the null hypothesis distribution and the test result
def plot_null_hypothesis(ax, sample_statistic, critical_value):
    """
    Plot the null hypothesis distribution, critical values, rejection regions, and the sample statistic.
    
    Parameters:
        ax (matplotlib.axes._axes.Axes): Axes object to plot on.
        sample_statistic (float): The observed test statistic.
        critical_value (float): The critical value for the two-tailed test.
    """
    # X values for the standard normal distribution
    x = np.linspace(-4, 4, 1000)
    
    # Y values for the standard normal distribution under the null hypothesis
    y = norm.pdf(x)

    # Plot the null hypothesis normal distribution
    ax.plot(x, y, color='green', label='Null Hypothesis')

    # Plot the critical values (boundaries for the rejection region)
    ax.axvline(-critical_value, color='blue', linestyle='dashed', linewidth=2, label=f'Critical Value\n{-critical_value:.2f}')
    ax.axvline(critical_value, color='blue', linestyle='dashed', linewidth=2, label=f'Critical Value\n{critical_value:.2f}')
    
    # Fill in the rejection regions in the left and right tails
    ax.fill_between(x, 0, y, where=(x < -critical_value) | (x > critical_value), color='orange', alpha=0.5, label='Rejection Region')

    # Plot the sample statistic
    ax.axvline(sample_statistic, color='red', linestyle='dashed', linewidth=2, label=f'Sample Statistic\n{sample_statistic:.2f}')
    
    # Add text to highlight the sample statistic
    ax.text(sample_statistic, 0.02, f'Sample Statistic\n{sample_statistic:.2f}',
            horizontalalignment='center', color='red', bbox=dict(facecolor='none', edgecolor='red', boxstyle='round,pad=0.5'))

    # Set the title and labels
    ax.set_title('Null Hypothesis Distribution and Rejection Regions')
    ax.set_xlabel('Test Statistic')
    ax.set_ylabel('Probability Density')

    # Add a legend
    ax.legend()

# Main execution
def main():
    # Parameters
    alpha = 0.05
    sample_statistic = 2.0  # Example sample statistic

    # Step 1: Calculate the critical value for a two-tailed test
    critical_value = calculate_critical_values(alpha)

    # Step 2: Create figure and axes
    fig, ax = plt.subplots(1, figsize=(10, 5))

    # Step 3: Plot the null hypothesis illustration with the calculated critical value
    plot_null_hypothesis(ax, sample_statistic, critical_value)

    # Show the plot
    plt.tight_layout()
    plt.show()

# Execute the main function
if __name__ == "__main__":
    main()
