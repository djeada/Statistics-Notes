import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Parameters for the Poisson process
n_trees = 100  # Number of trees
x_min, x_max = 0, 100  # Boundaries of the forest in x direction
y_min, y_max = 0, 100  # Boundaries of the forest in y direction

# Generate Poisson process data: random uniform points
x_poisson = np.random.uniform(x_min, x_max, n_trees)
y_poisson = np.random.uniform(y_min, y_max, n_trees)

# Plot the Poisson process (random uniform distribution)
plt.figure(figsize=(8, 8))
plt.scatter(x_poisson, y_poisson, c='green', label='Poisson Process (random)')
plt.title('Tree Locations (Poisson Process)')
plt.xlim([x_min, x_max])
plt.ylim([y_min, y_max])
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.legend()
plt.grid(True)
plt.show()

# Now, simulate a clustered process: randomly place cluster centers and generate points around them
n_clusters = 5  # Number of clusters
n_points_per_cluster = 20  # Points per cluster
cluster_std = 5  # Standard deviation within each cluster

# Generate cluster centers
x_cluster_centers = np.random.uniform(x_min, x_max, n_clusters)
y_cluster_centers = np.random.uniform(y_min, y_max, n_clusters)

# Generate points around each cluster center
x_cluster = []
y_cluster = []
for i in range(n_clusters):
    x_cluster.extend(np.random.normal(x_cluster_centers[i], cluster_std, n_points_per_cluster))
    y_cluster.extend(np.random.normal(y_cluster_centers[i], cluster_std, n_points_per_cluster))

x_cluster = np.array(x_cluster)
y_cluster = np.array(y_cluster)

# Plot the clustered process
plt.figure(figsize=(8, 8))
plt.scatter(x_cluster, y_cluster, c='blue', label='Cluster Process')
plt.title('Tree Locations (Cluster Process)')
plt.xlim([x_min, x_max])
plt.ylim([y_min, y_max])
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.legend()
plt.grid(True)
plt.show()

