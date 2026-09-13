import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

# Step 1: Input data
data = {'Hours_Studied (x1)': [2, 4, 6, 8],
        'Practice_Exams (x2)': [1, 2, 3, 4],
        'Test_Score (y)': [50, 60, 70, 80]}
df = pd.DataFrame(data)

# Step 2: Prepare 3D data for regression model
X = df[['Hours_Studied (x1)', 'Practice_Exams (x2)']].values
y = df['Test_Score (y)'].values

# Step 3: Fit a 3D linear regression model
model = LinearRegression()
model.fit(X, y)

# Create a grid for plotting the plane
x1_range = np.linspace(df['Hours_Studied (x1)'].min(), df['Hours_Studied (x1)'].max(), 10)
x2_range = np.linspace(df['Practice_Exams (x2)'].min(), df['Practice_Exams (x2)'].max(), 10)
x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)

# Predict y values over the grid to plot the plane
y_pred_grid = model.predict(np.c_[x1_grid.ravel(), x2_grid.ravel()]).reshape(x1_grid.shape)

# Step 4: Plot the 3D scatter plot with the fitted plane
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of the actual data points
ax.scatter(df['Hours_Studied (x1)'], df['Practice_Exams (x2)'], df['Test_Score (y)'], color='blue', label='Actual Data')

# Plot the fitted plane
ax.plot_surface(x1_grid, x2_grid, y_pred_grid, color='red', alpha=0.5, rstride=100, cstride=100)

# Labels and title
ax.set_title('3D Linear Regression: Hours Studied, Practice Exams, and Test Scores', fontsize=14)
ax.set_xlabel('Hours Studied ($x_1$)')
ax.set_ylabel('Practice Exams ($x_2$)')
ax.set_zlabel('Test Score ($y$)')

# Display the plot
plt.show()

# Step 5: Analyze the regression model
coefficients = model.coef_
intercept = model.intercept_

# Print model results
coefficients, intercept
