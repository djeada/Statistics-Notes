import numpy as np
import scipy.stats as stats

# Set the seed for reproducibility
np.random.seed(42)

# Generating random weight data for apples from Farm A and Farm B
farm_a_apple_weights = np.random.normal(loc=150, scale=10, size=50)
farm_b_apple_weights = np.random.normal(loc=155, scale=10, size=50)

# Calculate the means of the apple weights
mean_farm_a = np.mean(farm_a_apple_weights)
mean_farm_b = np.mean(farm_b_apple_weights)

print(f"Mean weight of apples from Farm A: {mean_farm_a:.2f} g")
print(f"Mean weight of apples from Farm B: {mean_farm_b:.2f} g")

# Perform a two-sample t-test
t_stat, p_value = stats.ttest_ind(farm_a_apple_weights, farm_b_apple_weights)

print(f"t-statistic: {t_stat:.2f}")
print(f"p-value: {p_value:.4f}")

# Set significance level
alpha = 0.05

# Interpret the results
if p_value < alpha:
    print(
        "We reject the null hypothesis. There is a significant difference in the average apple weights between the two farms."
    )
else:
    print(
        "We fail to reject the null hypothesis. There is no significant difference in the average apple weights between the two farms."
    )
