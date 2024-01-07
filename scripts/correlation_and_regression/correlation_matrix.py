
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(42)
x1 = np.random.normal(0, 1, 100)
x2 = np.random.normal(0, 1, 100)
x3 = x1 + x2 + np.random.normal(0, 0.5, 100)
x4 = 2 * x1 - x2 + np.random.normal(0, 0.5, 100)

# Calculate correlation matrix
corr_matrix = np.corrcoef([x1, x2, x3, x4])

# Visualize correlation matrix as heatmap
fig, ax = plt.subplots()
im = ax.imshow(corr_matrix, cmap='coolwarm')

# Customize plot
ax.set_xticks(np.arange(4))
ax.set_yticks(np.arange(4))
ax.set_xticklabels(['X1', 'X2', 'X3', 'X4'])
ax.set_yticklabels(['X1', 'X2', 'X3', 'X4'])
ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
ax.set_title("Correlation Matrix")

# Add text annotations to heatmap
for i in range(4):
    for j in range(4):
        text = ax.text(j, i, f"{corr_matrix[i, j]:.2f}",
                       ha="center", va="center", color="w")

# Show the plot
plt.show()
