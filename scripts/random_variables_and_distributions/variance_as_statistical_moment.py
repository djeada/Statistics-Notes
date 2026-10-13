"""Variance as a statistical moment of inertia in two dimensions."""
import matplotlib.pyplot as plt
import numpy as np


def main():
    rng = np.random.default_rng(0)
    n = 200
    mean = np.array([2.0, -1.0])
    cov = np.eye(2)  # isotropic, so the radius circles are natural
    data = rng.multivariate_normal(mean, cov, size=n)

    mu_hat = data.mean(axis=0)

    # Root-mean-square radial distance: the 2-D analogue of the standard deviation.
    radii = np.linalg.norm(data - mu_hat, axis=1)
    sigma_r = np.sqrt(np.mean(radii**2))
    print(f"sigma_r = {sigma_r:.3f} (theory sqrt(2) = {np.sqrt(2):.3f} for unit variance per axis)")
    print(f"Fraction within 1 sigma_r = {np.mean(radii <= sigma_r):.2f}")

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(data[:, 0], data[:, 1], alpha=0.6, label="Data points")
    ax.plot(*mu_hat, marker="x", markersize=10, label="Sample mean $\\hat{\\mu}$")
    for k in (1, 2):
        ax.add_patch(plt.Circle(mu_hat, k * sigma_r, fill=False, linestyle="--",
                                linewidth=1.5, label=f"{k}$\\sigma_r$"))
    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_title("Variance as a Statistical Moment of Inertia")
    ax.legend()
    ax.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
