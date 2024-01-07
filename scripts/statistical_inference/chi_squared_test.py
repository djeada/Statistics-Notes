import numpy as np
from scipy.stats import chi2_contingency

# Set the random seed for reproducibility
np.random.seed(42)

# Generate a random dataset of 100 individuals
n = 1000
males = np.random.choice(["Tee", "Coffee"], size=n, p=[0.6, 0.4])
females = np.random.choice(["Tee", "Coffee"], size=n, p=[0.4, 0.6])

# Modify probabilities
males[males == "Coffee"] = "Tee"
females[females == "Tee"] = "Coffee"

# Create a contingency table
contingency_table = np.array(
    [
        [sum(males == "Tee"), sum(males == "Coffee")],
        [sum(females == "Tee"), sum(females == "Coffee")],
    ]
)


# Perform chi-square test for independence
chi2, p, dof, expected = chi2_contingency(contingency_table)

print(f"Chi-square statistic: {chi2:.2f}")
print(f"p-value: {p:.4f}")

# Set the significance level
alpha = 0.05

# Interpret the results
if p < alpha:
    print("There is a significant association between gender and beverage preference.")
else:
    print("There is no significant association between gender and beverage preference.")
