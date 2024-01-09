import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, multivariate_normal

# PDF for a single variable
def plot_single_variable_pdf():
    x = np.linspace(-5, 5, 100)
    y = norm.pdf(x, 0, 1)  # Normal distribution with mean=0 and std=1

    plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.title('Probability Density Function of a Normal Distribution')
    plt.xlabel('x')
    plt.ylabel('PDF')
    plt.grid(True)
    plt.show()

# Joint PDF for two variables
def plot_joint_variable_pdf():
    x, y = np.mgrid[-5:5:.1, -5:5:.1]
    pos = np.dstack((x, y))
    rv = multivariate_normal([0, 0], [[1, 0], [0, 1]])  # Mean=[0,0] and Covariance=[[1, 0], [0, 1]]

    plt.figure(figsize=(8, 6))
    plt.contourf(x, y, rv.pdf(pos))
    plt.title('Joint Probability Density Function of Two Normal Distributions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar()
    plt.grid(True)
    plt.show()

# Run the functions
plot_single_variable_pdf()
plot_joint_variable_pdf()
