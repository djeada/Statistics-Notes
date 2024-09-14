import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Input data for hours studied (x) and test scores (y)
data = {'Hours_Studied (x)': [2, 4, 6, 8],
        'Test_Score (y)': [50, 60, 70, 80]}
df = pd.DataFrame(data)

# Step 2: Prepare the data for regression model
X = df[['Hours_Studied (x)']].values  # Predictor (hours studied)
y = df['Test_Score (y)'].values  # Dependent variable (test scores)

# Step 3: Fit a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Step 4: Get the regression coefficients
slope = model.coef_[0]
intercept = model.intercept_

# Step 5: Make predictions
y_pred = model.predict(X)

# Step 6: Calculate residuals
residuals = y - y_pred

# Step 7: Calculate sums of squares
SST = np.sum((y - np.mean(y)) ** 2)  # Total sum of squares
SSE = np.sum((residuals) ** 2)  # Sum of squared errors
SSR = SST - SSE  # Regression sum of squares

# Step 8: Calculate R-squared
R_squared = SSR / SST

# Step 9: Plot the actual data, regression line, and residuals
plt.figure(figsize=(8, 6))
plt.scatter(df['Hours_Studied (x)'], df['Test_Score (y)'], color='blue', label='Actual Data')
plt.plot(df['Hours_Studied (x)'], y_pred, color='red', label=f'Regression Line: y = {intercept:.2f} + {slope:.2f}x')

# Add legend with the key results
plt.legend(title=f'Regression Results\n'
                 f'y = {intercept:.2f} + {slope:.2f}x\n'
                 f'R² = {R_squared:.2f}\n'
                 f'SST = {SST:.2f}\n'
                 f'SSR = {SSR:.2f}\n'
                 f'SSE = {SSE:.2f}',
           loc='upper left')

# Labels and title
plt.title('Simple Linear Regression: Hours Studied vs Test Score')
plt.xlabel('Hours Studied ($x$)')
plt.ylabel('Test Score ($y$)')

# Show plot
plt.show()

# Return key results for reference
slope, intercept, R_squared, SST, SSR, SSE
