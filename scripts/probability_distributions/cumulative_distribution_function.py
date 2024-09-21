import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Function to plot CDF for a single continuous variable
def plot_single_variable_cdf(x, cdf, title, xlabel, ylabel):
    plt.figure(figsize=(8, 4))
    plt.plot(x, cdf)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Function to plot CDF for a discrete variable
def plot_discrete_variable_cdf(outcomes, probabilities, title, xlabel, ylabel):
    plt.figure(figsize=(8, 4))
    plt.step(outcomes, probabilities, where='post')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(outcomes - 0.5)
    plt.yticks(np.linspace(0, 1, len(outcomes)))
    plt.grid(True)
    plt.show()

# Data generation for a continuous variable CDF (e.g., normal distribution)
x_continuous = np.linspace(-5, 5, 1000)
cdf_continuous = norm.cdf(x_continuous, 0, 1)  # Normal distribution with mean=0 and std=1

# Data generation for a discrete variable CDF (e.g., rolling a six-sided die)
outcomes_discrete = np.arange(1, 8)  # Outcomes: 1 to 6
probabilities_discrete = np.cumsum(np.full(6, 1/6))  # Cumulative sum of probabilities
probabilities_discrete = np.append([0], probabilities_discrete)  # To include CDF starting from 0

# Plotting the CDF for a single continuous variable
plot_single_variable_cdf(x_continuous, cdf_continuous, 
                         title='Cumulative Distribution Function of a Normal Distribution', 
                         xlabel='x', ylabel='CDF')

# Plotting the CDF for a discrete variable
plot_discrete_variable_cdf(outcomes_discrete, probabilities_discrete, 
                           title='Cumulative Distribution Function of a Six-Sided Die', 
                           xlabel='Outcome', ylabel='CDF')
