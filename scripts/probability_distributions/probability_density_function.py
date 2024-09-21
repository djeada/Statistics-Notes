import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, multivariate_normal

# Function to plot the PDF of a single variable
def plot_single_variable_pdf(x, y, title, xlabel, ylabel):
    plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Function to plot the joint PDF of two variables
def plot_joint_variable_pdf(x, y, z, title, xlabel, ylabel):
    plt.figure(figsize=(8, 6))
    plt.contourf(x, y, z)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar()
    plt.grid(True)
    plt.show()

# Data generation for single variable PDF (e.g., normal distribution)
x_single = np.linspace(-5, 5, 100)
y_single = norm.pdf(x_single, 0, 1)  # Normal distribution with mean=0 and std=1

# Data generation for joint variable PDF (e.g., bivariate normal distribution)
x_joint, y_joint = np.mgrid[-5:5:.1, -5:5:.1]
pos_joint = np.dstack((x_joint, y_joint))
rv_joint = multivariate_normal([0, 0], [[1, 0], [0, 1]])  # Mean=[0,0], Covariance=[[1, 0], [0, 1]]
z_joint = rv_joint.pdf(pos_joint)

# Plotting the single variable PDF
plot_single_variable_pdf(x_single, y_single, 
                         title='Probability Density Function of a Normal Distribution', 
                         xlabel='x', ylabel='PDF')

# Plotting the joint variable PDF
plot_joint_variable_pdf(x_joint, y_joint, z_joint, 
                        title='Joint Probability Density Function of Two Normal Distributions', 
                        xlabel='x', ylabel='y')
