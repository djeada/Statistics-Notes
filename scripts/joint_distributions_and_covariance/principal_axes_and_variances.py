"""Principal axes of a correlated 2-D cloud from the covariance matrix."""

import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    rng = np.random.default_rng(1)
    n = 300
    mean = np.array([1.5, -0.5])
    cov = np.array([[3.0, 1.2],
                    [1.2, 0.8]])  # correlated, unequal variances
    data = rng.multivariate_normal(mean, cov, size=n)

    # Sample mean and covariance matrix (divide by n - 1).
    mu_hat = data.mean(axis=0)
    sigma_hat = np.cov(data.T)

    # Eigen-decomposition, sorted from largest to smallest eigenvalue.
    eigvals, eigvecs = np.linalg.eigh(sigma_hat)
    order = np.argsort(eigvals)[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]
    print("Eigenvalues (variances along principal axes):", np.round(eigvals, 3))
    print("Eigenvectors (columns):\n", np.round(eigvecs, 3))

    # Arrow length: k standard deviations along each axis.
    k = 2
    axes_vectors = eigvecs * (k * np.sqrt(eigvals))

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(data[:, 0], data[:, 1], alpha=0.6, label="Data points")

    for i in range(2):
        vec = axes_vectors[:, i]
        ax.annotate("", xy=mu_hat + vec, xytext=mu_hat,
                    arrowprops=dict(arrowstyle="->", linewidth=2),
                    annotation_clip=False)
        ax.text(*(mu_hat + vec * 1.1), f"$\\lambda_{i + 1} = {eigvals[i]:.2f}$",
                ha="left", va="center", fontsize=10)

    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_title("Principal Axes and Their Variances")
    ax.legend()
    ax.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
