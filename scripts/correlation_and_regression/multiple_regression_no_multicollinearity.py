import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Input data for hours studied (x1), attendance rate (x2), and test scores (y)
data = {'Hours_Studied (x1)': [2, 3, 5, 7, 9],
        'Attendance_Rate (x2)': [70, 80, 60, 90, 95],
        'Test_Score (y)': [65, 70, 75, 85, 95]}
df = pd.DataFrame(data)

# Step 2: Prepare data for the regression model
X = df[['Hours_Studied (x1)', 'Attendance_Rate (x2)']].values
y = df['Test_Score (y)'].values

# Step 3: Fit a multiple linear regression model
model = LinearRegression()
model.fit(X, y)

# Coefficients and intercept
coefficients = model.coef_
intercept = model.intercept_

# Step 4: Create a grid for visualization (only hours studied for x-axis)
x1_range = np.linspace(df['Hours_Studied (x1)'].min(), df['Hours_Studied (x1)'].max(), 10)
x2_range = np.linspace(df['Attendance_Rate (x2)'].min(), df['Attendance_Rate (x2)'].max(), 10)
x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)

# Predict y values over the grid for 3D plane visualization
y_pred_grid = model.predict(np.c_[x1_grid.ravel(), x2_grid.ravel()]).reshape(x1_grid.shape)

# Step 5: Plot the actual data and the regression plane
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of actual data points
ax.scatter(df['Hours_Studied (x1)'], df['Attendance_Rate (x2)'], df['Test_Score (y)'], color='blue', label='Actual Data')

# Plot the fitted regression plane
ax.plot_surface(x1_grid, x2_grid, y_pred_grid, color='red', alpha=0.5, rstride=100, cstride=100)

# Labels and title
ax.set_title('3D Multiple Linear Regression: Test Scores, Hours Studied, and Attendance Rate', fontsize=14)
ax.set_xlabel('Hours Studied ($x_1$)')
ax.set_ylabel('Attendance Rate ($x_2$)')
ax.set_zlabel('Test Score ($y$)')

# Display the plot
plt.show()

# Step 6: Analyze the model
regression_equation = f"y = {intercept:.3f} + {coefficients[0]:.3f} * x1 + {coefficients[1]:.3f} * x2"
regression_equation, coefficients, intercept
