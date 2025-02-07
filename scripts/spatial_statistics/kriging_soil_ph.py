#!/usr/bin/env python3
"""
This script generates synthetic soil pH data that mimics a realistic scenario:
a nearly uniform baseline (around 6.0) with small random noise plus a few localized high pH hotspots.
Ordinary kriging interpolation is applied to predict pH at unsampled locations, and the result is visualized
as a realistic 3D surface map with high red peaks representing the hotspots.
"""

import numpy as np
import matplotlib
# If you need an interactive backend (e.g., in PyCharm), uncomment the following line:
# matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting
from pykrige.ok import OrdinaryKriging
import matplotlib.colors as mcolors  # For creating custom colormaps


def generate_synthetic_soil_ph_data(n_points=150, x_range=(0, 100), y_range=(0, 100)):
    """
    Generate synthetic soil pH data with a baseline value and localized high pH hotspots.

    The baseline soil pH is near 6.0 with a little random noise.
    Two hotspots are added to simulate areas with much higher pH (red peaks).

    Parameters:
        n_points (int): Number of sample points.
        x_range (tuple): Range of x coordinates.
        y_range (tuple): Range of y coordinates.

    Returns:
        x (ndarray): x coordinates of sample points.
        y (ndarray): y coordinates of sample points.
        soil_pH (ndarray): Synthetic soil pH measurements.
    """
    np.random.seed(42)

    # Generate random coordinates within the study area.
    x = np.random.uniform(x_range[0], x_range[1], n_points)
    y = np.random.uniform(y_range[0], y_range[1], n_points)

    # Baseline pH value with slight noise.
    baseline = 6.0
    noise = np.random.normal(0, 0.1, n_points)
    soil_pH = baseline + noise

    # Define hotspots (simulate high pH anomalies):
    # Each hotspot is defined by a center, an amplitude, and a standard deviation (spread).
    hotspots = [
        {'center': (30, 30), 'amplitude': 2.0, 'sigma': 10},  # Will push pH to ~8.0 nearby
        {'center': (70, 80), 'amplitude': 2.5, 'sigma': 8}     # Will push pH even higher near this spot
    ]

    # Add the Gaussian influence of each hotspot to the baseline.
    for hs in hotspots:
        cx, cy = hs['center']
        amplitude = hs['amplitude']
        sigma = hs['sigma']
        # Compute squared distances from the hotspot center.
        distance_sq = (x - cx) ** 2 + (y - cy) ** 2
        # Gaussian decay: high effect near the center, diminishing with distance.
        hotspot_effect = amplitude * np.exp(-distance_sq / (2 * sigma ** 2))
        soil_pH += hotspot_effect

    return x, y, soil_pH


def perform_kriging(x, y, soil_pH, grid_size=150, variogram_model='spherical'):
    """
    Perform ordinary kriging interpolation on the synthetic soil pH data.

    Parameters:
        x (ndarray): x coordinates of sample points.
        y (ndarray): y coordinates of sample points.
        soil_pH (ndarray): Soil pH measurements.
        grid_size (int): Number of points along each axis for the interpolation grid.
        variogram_model (str): Variogram model to use ('spherical', 'exponential', or 'gaussian').

    Returns:
        grid_xx (ndarray): Meshgrid of x coordinates.
        grid_yy (ndarray): Meshgrid of y coordinates.
        grid_z (ndarray): Interpolated soil pH values on the grid.
    """
    # Create a grid covering the study area.
    grid_x = np.linspace(np.min(x), np.max(x), grid_size)
    grid_y = np.linspace(np.min(y), np.max(y), grid_size)
    grid_xx, grid_yy = np.meshgrid(grid_x, grid_y)

    # Set up ordinary kriging using the specified variogram model.
    OK = OrdinaryKriging(
        x, y, soil_pH,
        variogram_model=variogram_model,
        verbose=False,
        enable_plotting=False
    )
    grid_z, ss = OK.execute('grid', grid_x, grid_y)

    return grid_xx, grid_yy, grid_z


def plot_3d_soil_ph_map(grid_xx, grid_yy, grid_z, sample_x, sample_y, sample_pH):
    """
    Plot a 3D surface of the kriging-interpolated soil pH map and overlay the sample points.

    The plot uses a custom colormap that transitions from dark green (low pH), through yellow, to dark red (high pH).

    Parameters:
        grid_xx (ndarray): x coordinates of the grid.
        grid_yy (ndarray): y coordinates of the grid.
        grid_z (ndarray): Interpolated soil pH values.
        sample_x (ndarray): x coordinates of the sample points.
        sample_y (ndarray): y coordinates of the sample points.
        sample_pH (ndarray): Soil pH measurements at the sample points.
    """
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Create a custom colormap that transitions from dark green to yellow and finally to dark red.
    custom_cmap = mcolors.LinearSegmentedColormap.from_list(
        "CustomGreenYellowRed", ['#006400', '#FFFF00', '#8B0000']
    )

    # Plot the kriging surface with the custom colormap.
    surf = ax.plot_surface(grid_xx, grid_yy, grid_z, cmap=custom_cmap, edgecolor='none', alpha=0.9)

    # Overlay the original sample points.
    ax.scatter(sample_x, sample_y, sample_pH, color='blue', marker='o', s=50, label='Sample Points')

    ax.set_title('Kriging Interpolated Soil pH Map')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Soil pH')

    # Add a color bar to indicate pH values.
    fig.colorbar(surf, shrink=0.5, aspect=5, label='Soil pH')
    ax.legend()
    plt.savefig("soil_ph_map.png")
    plt.show()


def main():
    # Generate synthetic soil pH data with realistic features.
    sample_x, sample_y, sample_pH = generate_synthetic_soil_ph_data(n_points=150)

    # Perform kriging interpolation on the generated data.
    grid_xx, grid_yy, grid_z = perform_kriging(sample_x, sample_y, sample_pH, grid_size=150)

    # Plot the resulting 3D soil pH map.
    plot_3d_soil_ph_map(grid_xx, grid_yy, grid_z, sample_x, sample_y, sample_pH)


if __name__ == '__main__':
    main()
