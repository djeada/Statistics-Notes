import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Generate Mock Data for Linear Regression
np.random.seed(42)
X = 2 * np.pi * np.random.rand(100)  # 100 random data points between 0 and 2pi
y = np.sin(X) + np.random.normal(0, 0.15, 100)  # Sine wave with noise

# Step 2: Fit a Linear Regression Model
model = LinearRegression()
model.fit(X.reshape(-1, 1), y)

# Step 3: Make Predictions for Plotting and Error Calculation
X_fit = np.linspace(0, 2 * np.pi, 100)
y_pred = model.predict(X_fit.reshape(-1, 1))
y_pred_actual = model.predict(X.reshape(-1, 1))

# Step 4: Calculate Regression Metrics
mse = mean_squared_error(y, y_pred_actual)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred_actual)

# Step 5: Plot the Results with Error Lines
plt.figure(figsize=(10, 6))
plt.scatter(X, y, label='Actual Data', color='blue')
plt.plot(X_fit, y_pred, label='Regression Line', color='red')

# Drawing error lines
for xp, yp, y_hat in zip(X, y, y_pred_actual):
    plt.plot([xp, xp], [yp, y_hat], color='gray', linestyle='dotted')

plt.title(f'Linear Regression with Error Lines\nMSE: {mse:.2f}, RMSE: {rmse:.2f}, R²: {r2:.2f}')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
