import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import expit  # Sigmoid function

# Step 1: Input data for hours studied (x1), practice exams (x2), and pass/fail outcomes (y)
data = {'Hours Studied (x1)': [2, 4, 5, 6, 8],
        'Practice Exams (x2)': [1, 2, 2, 3, 4],
        'Pass (y)': [0, 0, 1, 1, 1]}
df_logistic = pd.DataFrame(data)

# Step 2: Design matrix X and response vector y
X = np.column_stack((np.ones(df_logistic.shape[0]), df_logistic['Hours Studied (x1)'], df_logistic['Practice Exams (x2)']))
y = df_logistic['Pass (y)'].values

# Step 3: Initialize coefficients (beta_0, beta_1, beta_2)
beta_hat = np.array([-9.28, 1.23, 0.98])  # Pre-computed coefficients from your example

# Logistic function for predicted probabilities
def logistic_function(X, beta):
    return expit(np.dot(X, beta))

# Step 4: Generate the decision boundary
# Create a mesh grid for plotting the decision boundary
x1_range = np.linspace(df_logistic['Hours Studied (x1)'].min() - 1, df_logistic['Hours Studied (x1)'].max() + 1, 200)
x2_range = np.linspace(df_logistic['Practice Exams (x2)'].min() - 1, df_logistic['Practice Exams (x2)'].max() + 1, 200)
X1, X2 = np.meshgrid(x1_range, x2_range)

# Compute the logistic regression predictions on the mesh grid
Z = logistic_function(np.column_stack((np.ones(X1.ravel().shape[0]), X1.ravel(), X2.ravel())), beta_hat)
Z = Z.reshape(X1.shape)

# Plotting the decision boundary
plt.figure(figsize=(10, 6))
# Contour plot for the decision boundary (probability = 0.5 line)
plt.contourf(X1, X2, Z, levels=[0, 0.5, 1], alpha=0.2, colors=['red', 'green'])

# Step 5: Plotting the dataset
# Students who failed
plt.scatter(df_logistic[df_logistic['Pass (y)'] == 0]['Hours Studied (x1)'],
            df_logistic[df_logistic['Pass (y)'] == 0]['Practice Exams (x2)'], 
            color='red', label='Fail (y=0)', s=100)

# Students who passed
plt.scatter(df_logistic[df_logistic['Pass (y)'] == 1]['Hours Studied (x1)'],
            df_logistic[df_logistic['Pass (y)'] == 1]['Practice Exams (x2)'], 
            color='green', label='Pass (y=1)', s=100)

# Step 6: Add labels, title, and decision boundary
plt.title("Logistic Regression: Hours Studied vs Practice Exams\nwith Decision Boundary", fontsize=14)
plt.xlabel("Hours Studied (x1)", fontsize=12)
plt.ylabel("Practice Exams (x2)", fontsize=12)

# Display legend
plt.legend()

# Show the plot
plt.show()
