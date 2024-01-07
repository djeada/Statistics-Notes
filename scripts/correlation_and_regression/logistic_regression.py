import numpy as np
import matplotlib.pyplot as plt

# Generate some data
np.random.seed(42)
x = np.random.normal(0, 1, (100, 2))
w_true = np.array([1, -1])
b_true = 0.5
z = np.dot(x, w_true) + b_true
y_true = (z > 0).astype(int)
y = y_true + np.random.normal(0, 0.1, 100)
    
# Define sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Define gradient function
def gradient(x, y, w):
    z = np.dot(x, w)
    return np.dot(x.T, y - sigmoid(z))

# Initialize weights and learning rate
w = np.zeros(2, dtype=np.float64)
b = 0.0
lr = 0.1

# Perform gradient descent
for i in range(1000):
    w += lr * gradient(x, y, w)
    b += lr * np.sum(y - sigmoid(np.dot(x, w) + b))

# Calculate predicted probabilities
p_pred = sigmoid(np.dot(x, w) + b)

# Visualize data and decision boundary
plt.figure(figsize=(8, 6))
plt.scatter(x[:, 0], x[:, 1], c=y_true, cmap='bwr', alpha=0.6)
plt.contourf(x[:, 0], x[:, 1], p_pred.reshape(100, 100), cmap='bwr', alpha=0.4)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Logistic Regression with Gradient Descent')
plt.show()
