import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from sklearn.preprocessing import scale

# Step 1: Generate synthetic data for trees with heights
np.random.seed(42)
n_trees = 100
x_coords = np.random.uniform(0, 100, n_trees)
y_coords = np.random.uniform(0, 100, n_trees)

# Simulate tree heights with spatial autocorrelation (influenced by proximity)
heights = np.random.normal(loc=50, scale=10, size=n_trees)

# Introduce positive spatial autocorrelation by modifying heights based on proximity
# Trees close to each other have more similar heights
distance_matrix = squareform(pdist(np.column_stack([x_coords, y_coords])))
weights_matrix = np.exp(-distance_matrix / 20)  # Decay function for distance influence
autocorrelated_heights = np.dot(weights_matrix, heights) / np.sum(weights_matrix, axis=1)

# Scale heights to make them comparable (mean-centered)
scaled_heights = scale(autocorrelated_heights)

# Step 2: Create a DataFrame to store tree data
tree_data = pd.DataFrame({
    'x_coords': x_coords,
    'y_coords': y_coords,
    'heights': scaled_heights
})

# Step 3: Plot the spatial distribution of tree heights
plt.figure(figsize=(8, 6))
plt.scatter(tree_data['x_coords'], tree_data['y_coords'], c=tree_data['heights'], cmap='coolwarm', s=100)
plt.colorbar(label='Tree Height (scaled)')
plt.title("Spatial Distribution of Tree Heights with Positive Spatial Autocorrelation")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True)
plt.show()

# Now the spatial autocorrelation calculations

# Step 4: Install required libraries in your local environment if not already installed
# pip install libpysal esda splot geopandas

import libpysal as ps
from esda.moran import Moran, Moran_Local
from esda.geary import Geary
import geopandas as gpd
from splot.esda import lisa_cluster

# Step 5: Create a spatial weights matrix using the coordinates
gdf = gpd.GeoDataFrame(tree_data, geometry=gpd.points_from_xy(tree_data.x_coords, tree_data.y_coords))
w = ps.weights.DistanceBand.from_dataframe(gdf, threshold=20, binary=True)

# Step 6: Calculate Moran's I
moran = Moran(tree_data['heights'], w)
print(f"Moran's I: {moran.I}")

# Step 7: Calculate Geary's C
geary = Geary(tree_data['heights'], w)
print(f"Geary's C: {geary.C}")

# Step 8: Calculate LISA (Local Moran's I)
moran_local = Moran_Local(tree_data['heights'], w)

# Step 9: Plot LISA Clusters
fig, ax = plt.subplots(figsize=(8, 6))
lisa_cluster(moran_local, gdf, p=0.05, ax=ax)
plt.title("LISA Cluster Map for Tree Heights")
plt.show()
