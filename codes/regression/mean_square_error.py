import numpy as np
import matplotlib.pyplot as plt

# Generate two sets of data
x = np.linspace(0, 10, 100)
y1 = 3 * x + 1 + np.random.normal(0, 1, 100)
y2 = 3 * x + 1 + np.random.normal(0, 5, 100)

# Calculate the mean squared error for each set of data
mse1 = np.mean((y1 - (3 * x + 1)) ** 2)
mse2 = np.mean((y2 - (3 * x + 1)) ** 2)

# Create two subplots, one for each set of data
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Plot the first set of data with small MSE
ax[0].scatter(x, y1, label=f"MSE = {mse1:.2f}")
ax[0].plot(x, 3 * x + 1, color="r", label="True Line")
ax[0].legend()
ax[0].set_title("Data with Small MSE")

# Plot the second set of data with large MSE
ax[1].scatter(x, y2, label=f"MSE = {mse2:.2f}")
ax[1].plot(x, 3 * x + 1, color="r", label="True Line")
ax[1].legend()
ax[1].set_title("Data with Large MSE")

plt.show()
