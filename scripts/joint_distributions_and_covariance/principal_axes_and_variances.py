import numpy as np
import matplotlib.pyplot as plt

# Generate an anisotropic 2-D cloud so PCA directions are distinct
np.random.seed(1)
n = 300
mean = np.array([1.5, -0.5])
cov = np.array([[3.0, 1.2],
                [1.2, 0.8]])  # correlated, unequal variances
data = np.random.multivariate_normal(mean, cov, size=n)

# Sample mean and covariance matrix
mu_hat = data.mean(axis=0)
Sigma_hat = np.cov(data.T, bias=True)  # bias=True: divide by n for population covariance

# Eigen-decomposition (principal components)
eigvals, eigvecs = np.linalg.eigh(Sigma_hat)  # eigh since Sigma_hat is symmetric
# Sort from largest to smallest eigenvalue
order = np.argsort(eigvals)[::-1]
eigvals = eigvals[order]
eigvecs = eigvecs[:, order]

# Scale eigenvectors for plotting: k * sqrt(eigenvalue)
k = 2  # controls arrow length
axes_vectors = eigvecs * (k * np.sqrt(eigvals))

# Plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(data[:, 0], data[:, 1], alpha=0.6, label="Data points")

# Plot principal axes as arrows originating at the mean
for i in range(2):
    vec = axes_vectors[:, i]
    ax.annotate("", xy=mu_hat + vec, xytext=mu_hat,
                arrowprops=dict(arrowstyle="->", linewidth=2),
                annotation_clip=False)
    # Annotate eigenvalue (variance) at arrow tip
    text_offset = vec * 0.1
    ax.text(*(mu_hat + vec + text_offset),
            f"$\\lambda_{i+1} = {eigvals[i]:.2f}$",
            ha="left", va="center", fontsize=10)

# Formatting
ax.set_aspect("equal")
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_title("PCA: Principal Axes and Their Variances")
ax.legend()
ax.grid(True)

plt.show()
