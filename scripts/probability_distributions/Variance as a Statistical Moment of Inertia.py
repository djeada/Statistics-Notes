import numpy as np
import matplotlib.pyplot as plt

# Generate a synthetic 2-D dataset
np.random.seed(0)
n = 200
mean = np.array([2.0, -1.0])
cov = np.array([[1.0, 0.0],
                [0.0, 1.0]])  # isotropic for nice circular std-dev
data = np.random.multivariate_normal(mean, cov, size=n)

# Sample mean
mu_hat = data.mean(axis=0)

# Root-mean-square radial distance (analogue of std-dev for radius)
radii = np.linalg.norm(data - mu_hat, axis=1)
sigma_r = np.sqrt(np.mean(radii**2))

# Figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(data[:, 0], data[:, 1], alpha=0.6, label="Data points")

# Mark sample mean
ax.plot(*mu_hat, marker="x", markersize=10, label="Sample mean $\\hat{\\mu}$")

# Concentric circles at 1σ and 2σ
for k in [1, 2]:
    circle = plt.Circle(mu_hat, k * sigma_r, fill=False, linestyle="--",
                        linewidth=1.5, label=f"{k}$\\sigma$")
    ax.add_patch(circle)

ax.set_aspect("equal")
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_title("Variance as a Statistical Moment of Inertia")
ax.legend()
ax.grid(True)

plt.show()
