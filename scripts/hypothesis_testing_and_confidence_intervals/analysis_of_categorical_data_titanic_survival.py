import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Titanic survival data summary
# Observed data: [Survived, Died] counts for each ticket class
observed_data = np.array([
    [203, 122],  # First Class
    [118, 167],  # Second Class
    [178, 528],  # Third Class
    [212, 673],  # Crew
])

# Class totals (row sums)
row_totals = np.array([325, 285, 706, 885])

# Survival totals (column sums)
col_totals = np.array([711, 1490])

# Grand total (sum of all passengers)
grand_total = 2201

# Step 1: Calculate the expected counts for each cell
# Expected data using the formula: (row_total * col_total) / grand_total
expected_data = np.outer(row_totals, col_totals) / grand_total

# Step 2: Compute the chi-square statistic and p-value
chi_square_stat, p_value, _, _ = stats.chi2_contingency(observed_data)

# Step 3: Degrees of freedom and critical value for the chi-square test
df = (observed_data.shape[0] - 1) * (observed_data.shape[1] - 1)  # df = (rows - 1) * (columns - 1)
alpha = 0.05
critical_value = stats.chi2.ppf(1 - alpha, df)

# Step 4: Decision rule based on the chi-square statistic and critical value
if chi_square_stat > critical_value:
    decision = "Reject the null hypothesis: Survival rates differ across ticket classes."
else:
    decision = "Fail to reject the null hypothesis: No significant difference in survival rates among classes."

# Step 5: Output results in a dictionary for easy access
results = {
    'Chi-square statistic': chi_square_stat,
    'p-value': p_value,
    'Critical value': critical_value,
    'Decision': decision
}

# Display results
for key, value in results.items():
    print(f"{key}: {value}")

# Step 6: Plot the observed vs expected counts for visual comparison
classes = ['First Class', 'Second Class', 'Third Class', 'Crew']
categories = ['Survived', 'Died']

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.35
index = np.arange(len(classes))

# Plot bars for 'Survived' (Observed vs Expected)
bar1 = ax.bar(index, observed_data[:, 0], bar_width, label='Observed Survived', color='blue', alpha=0.7)
bar2 = ax.bar(index + bar_width, expected_data[:, 0], bar_width, label='Expected Survived', color='orange', alpha=0.7)

# Plot bars for 'Died' (Observed vs Expected)
bar3 = ax.bar(index, observed_data[:, 1], bar_width, bottom=observed_data[:, 0], label='Observed Died', color='green', alpha=0.7)
bar4 = ax.bar(index + bar_width, expected_data[:, 1], bar_width, bottom=expected_data[:, 0], label='Expected Died', color='red', alpha=0.7)

# Labeling and title
ax.set_xlabel('Ticket Class', fontsize=12)
ax.set_ylabel('Counts', fontsize=12)
ax.set_title('Observed vs Expected Titanic Survival by Ticket Class', fontsize=14)
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(classes)
ax.legend()

# Optimize layout and display the plot
plt.tight_layout()
plt.show()
