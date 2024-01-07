import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Set the seed for reproducibility
np.random.seed(42)

# Generating random weight data for apples from Farm A, B and C
farm_a_apple_weights = np.random.normal(loc=148, scale=10, size=50)
farm_b_apple_weights = np.random.normal(loc=150, scale=10, size=50)
farm_c_apple_weights = np.random.normal(loc=152, scale=10, size=50)

# Combine all data into one array
apple_weights = np.concatenate(
    (farm_a_apple_weights, farm_b_apple_weights, farm_c_apple_weights)
)

# Create an array to store the group labels
group_a = np.full_like(farm_a_apple_weights, 0)
group_b = np.full_like(farm_b_apple_weights, 1)
group_c = np.full_like(farm_c_apple_weights, 2)
groups = np.concatenate((group_a, group_b, group_c))

# Perform one-way ANOVA
f_stat, p_value = stats.f_oneway(
    farm_a_apple_weights, farm_b_apple_weights, farm_c_apple_weights
)

print(f"F-statistic: {f_stat:.2f}")
print(f"p-value: {p_value:.4f}")

# Set significance level
alpha = 0.05

# Interpret the results
if p_value < alpha:
    print(
        "We reject the null hypothesis. There is a significant difference in the average apple weights between the groups."
    )
else:
    print(
        "We fail to reject the null hypothesis. There is no significant difference in the average apple weights between the groups."
    )

# Plot the boxplots
plt.boxplot(
    [farm_a_apple_weights, farm_b_apple_weights, farm_c_apple_weights],
    labels=["Farm A", "Farm B", "Farm C"],
)
plt.title("Boxplots of Apple Weights for Three Farms")
plt.ylabel("Weight (g)")
plt.show()
