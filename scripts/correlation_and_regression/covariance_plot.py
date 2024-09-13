import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Input data
data = {'X': [1, 2, 3],
        'Y': [2, 4, 6]}
df = pd.DataFrame(data)

# Step 2: Calculate the means of X and Y
mean_X = df['X'].mean()
mean_Y = df['Y'].mean()

# Step 3: Compute deviations from the mean
df['X_i - X̄'] = df['X'] - mean_X
df['Y_i - Ȳ'] = df['Y'] - mean_Y

# Step 4: Compute product of deviations
df['(X_i - X̄)(Y_i - Ȳ)'] = df['X_i - X̄'] * df['Y_i - Ȳ']

# Step 5: Calculate covariance
n = len(df)
covariance = df['(X_i - X̄)(Y_i - Ȳ)'].sum() / (n - 1)

# Step 6: Calculate variance of X and Y
df['(X_i - X̄)^2'] = df['X_i - X̄'] ** 2
df['(Y_i - Ȳ)^2'] = df['Y_i - Ȳ'] ** 2
variance_X = df['(X_i - X̄)^2'].sum() / (n - 1)
variance_Y = df['(Y_i - Ȳ)^2'].sum() / (n - 1)

# Step 7: Calculate correlation coefficient
correlation_coefficient = covariance / (np.sqrt(variance_X * variance_Y))

# Display dataframe for reference
import ace_tools as tools; tools.display_dataframe_to_user(name="Covariance Calculation", dataframe=df)

# Plotting the data points
plt.figure(figsize=(8, 6))
plt.scatter(df['X'], df['Y'], color='blue', label='Data points')
plt.plot(df['X'], df['Y'], color='red', label=f'Y = 2X')

# Adding labels and title
plt.title('Scatter Plot of X and Y with Covariance Calculation', fontsize=14)
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(mean_Y, color='green', linestyle='--', label='Mean Y')
plt.axvline(mean_X, color='green', linestyle='--', label='Mean X')

# Display covariance and correlation on the plot
plt.text(1, 5, f"Cov(X, Y) = {covariance:.2f}\nCorr(X, Y) = {correlation_coefficient:.2f}", 
         fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

# Display legend
plt.legend()

# Show the plot
plt.show()
