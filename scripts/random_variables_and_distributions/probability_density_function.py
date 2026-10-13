"""PDFs: a univariate normal density and a bivariate normal joint density."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import trapezoid
from scipy.stats import multivariate_normal, norm


def plot_single_variable_pdf(x, y, title, xlabel, ylabel):
    plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def plot_joint_variable_pdf(x, y, z, title, xlabel, ylabel):
    plt.figure(figsize=(8, 6))
    plt.contourf(x, y, z)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar()
    plt.grid(True)
    plt.show()


def main():
    x_single = np.linspace(-5, 5, 100)
    y_single = norm.pdf(x_single, 0, 1)

    x_joint, y_joint = np.mgrid[-5:5:0.1, -5:5:0.1]
    pos_joint = np.dstack((x_joint, y_joint))
    rv_joint = multivariate_normal([0, 0], [[1, 0], [0, 1]])
    z_joint = rv_joint.pdf(pos_joint)

    # A density integrates to 1 (Riemann sum on the grid)
    print(f"Area under univariate pdf  ~ {trapezoid(y_single, x_single):.4f}")
    print(f"Volume under joint pdf     ~ {z_joint.sum() * 0.1 * 0.1:.4f}")

    plot_single_variable_pdf(x_single, y_single,
                             "Probability Density Function of a Normal Distribution", "x", "PDF")
    plot_joint_variable_pdf(x_joint, y_joint, z_joint,
                            "Joint Probability Density Function of Two Normal Distributions", "x", "y")


if __name__ == "__main__":
    main()
