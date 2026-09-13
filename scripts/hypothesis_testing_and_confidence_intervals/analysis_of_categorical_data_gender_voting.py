import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Gender and Voting Preference data summary
# Observed data: [Liberal, Conservative] counts for each gender
observed_data_voting = np.array([
    [40, 60],  # Male
    [70, 30],  # Female
])

# Gender totals (row sums)
row_totals_voting = np.array([100, 100])  # 100 males, 100 females

# Voting preference totals (column sums)
col_totals_voting = np.array([110, 90])  # 110 liberals, 90 conservatives

# Grand total (sum of all individuals)
grand_total_voting = 200

# Step 1: Calculate expected counts using the formula: (row_total * col_total) / grand_total
expected_data_voting = np.outer(row_totals_voting, col_totals_voting) / grand_total_voting

# Step 2: Compute the chi-square statistic with Yates' correction for continuity
chi_square_stat_voting, p_value_voting = stats.chi2_contingency(observed_data_voting, correction=True)[:2]

# Step 3: Degrees of freedom and critical value for the chi-square test
df_voting = (observed_data_voting.shape[0] - 1) * (observed_data_voting.shape[1] - 1)  # df = (rows - 1) * (columns - 1)
alpha_voting = 0.05
critical_value_voting = stats.chi2.ppf(1 - alpha_voting, df_voting)

# Step 4: Decision rule based on the chi-square statistic and critical value
if chi_square_stat_voting > critical_value_voting:
    decision_voting = "Reject the null hypothesis: There is a significant association between gender and voting preference."
else:
    decision_voting = "Fail to reject the null hypothesis: No significant association between gender and voting preference."

# Step 5: Output results in a dictionary for easy access
results_voting = {
    'Chi-square statistic': chi_square_stat_voting,
    'p-value': p_value_voting,
    'Critical value': critical_value_voting,
    'Decision': decision_voting
}

# Display results
for key, value in results_voting.items():
    print(f"{key}: {value}")

# Step 6: Plot the observed vs expected counts for visual comparison
groups_voting = ['Male', 'Female']
categories_voting = ['Liberal', 'Conservative']

fig, ax = plt.subplots(figsize=(8, 5))

bar_width = 0.35
index_voting = np.arange(len(groups_voting))

# Define colors for observed and expected bars
color_observed_voting = '#4682B4'  # Steel blue for observed
color_expected_voting = '#A9A9A9'  # Dark gray for expected

# Plot bars for 'Liberal' (Observed vs Expected)
bar1_voting = ax.bar(index_voting - bar_width/2, observed_data_voting[:, 0], bar_width, label='Observed Liberal', color=color_observed_voting, alpha=0.8)
bar3_voting = ax.bar(index_voting + bar_width/2, expected_data_voting[:, 0], bar_width, label='Expected Liberal', color=color_expected_voting, alpha=0.8)

# Plot bars for 'Conservative' (Observed vs Expected), stacked on top of 'Liberal'
bar2_voting = ax.bar(index_voting - bar_width/2, observed_data_voting[:, 1], bar_width, bottom=observed_data_voting[:, 0], label='Observed Conservative', color=color_observed_voting, alpha=0.5)
bar4_voting = ax.bar(index_voting + bar_width/2, expected_data_voting[:, 1], bar_width, bottom=expected_data_voting[:, 0], label='Expected Conservative', color=color_expected_voting, alpha=0.5)

# Add labels and title with better font size and styling
ax.set_xlabel('Gender', fontsize=14, weight='bold')
ax.set_ylabel('Counts', fontsize=14, weight='bold')
ax.set_title('Observed vs Expected Voting Preferences by Gender', fontsize=16, weight='bold')

# Improve xticks for better readability
ax.set_xticks(index_voting)
ax.set_xticklabels(groups_voting, fontsize=12)

# Add grid for better separation of bars
ax.grid(True, linestyle='--', alpha=0.6, axis='y')

# Display the legend in a cleaner location
ax.legend(loc='upper right', fontsize=12)

# Optimize layout and display the plot
plt.tight_layout()
plt.show()
