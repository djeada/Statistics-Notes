import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Input data for hours studied (X) and test scores (Y)
data = {'Hours Studied (X)': [1, 2, 3, 4, 5],
        'Test Score (Y)': [50, 60, 70, 80, 90]}
df_pearson = pd.DataFrame(data)

# Step 2: Calculate the means of X and Y
mean_X_pearson = df_pearson['Hours Studied (X)'].mean()
mean_Y_pearson = df_pearson['Test Score (Y)'].mean()

# Step 3: Compute deviations from the mean
df_pearson['X_i - X̄'] = df_pearson['Hours Studied (X)'] - mean_X_pearson
df_pearson['Y_i - Ȳ'] = df_pearson['Test Score (Y)'] - mean_Y_pearson

# Step 4: Compute the product of deviations
df_pearson['(X_i - X̄)(Y_i - Ȳ)'] = df_pearson['X_i - X̄'] * df_pearson['Y_i - Ȳ']

# Step 5: Compute squared deviations for X and Y
df_pearson['(X_i - X̄)^2'] = df_pearson['X_i - X̄'] ** 2
df_pearson['(Y_i - Ȳ)^2'] = df_pearson['Y_i - Ȳ'] ** 2

# Step 6: Compute the Pearson correlation coefficient (r)
sum_product_deviations = df_pearson['(X_i - X̄)(Y_i - Ȳ)'].sum()
sum_squared_X_deviations = df_pearson['(X_i - X̄)^2'].sum()
sum_squared_Y_deviations = df_pearson['(Y_i - Ȳ)^2'].sum()

# Pearson's r formula
pearson_r = sum_product_deviations / (np.sqrt(sum_squared_X_deviations * sum_squared_Y_deviations))

# Display dataframe for reference
import ace_tools as tools; tools.display_dataframe_to_user(name="Pearson Correlation Calculation", dataframe=df_pearson)

# Plotting the data points
plt.figure(figsize=(8, 6))
plt.scatter(df_pearson['Hours Studied (X)'], df_pearson['Test Score (Y)'], color='blue', label='Data points')
plt.plot(df_pearson['Hours Studied (X)'], df_pearson['Test Score (Y)'], color='red', label=f'Y = 10X + 40')

# Adding labels and title
plt.title('Scatter Plot of Hours Studied and Test Scores', fontsize=14)
plt.xlabel('Hours Studied (X)')
plt.ylabel('Test Score (Y)')
plt.axhline(mean_Y_pearson, color='green', linestyle='--', label='Mean Test Score')
plt.axvline(mean_X_pearson, color='green', linestyle='--', label='Mean Hours Studied')

# Display Pearson's r on the plot
plt.text(1, 85, f"Pearson's r = {pearson_r:.2f}", fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

# Display legend
plt.legend()

# Show the plot
plt.show()
