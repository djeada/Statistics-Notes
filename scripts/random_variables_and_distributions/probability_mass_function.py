import matplotlib.pyplot as plt
import numpy as np

# Function to plot PMF for a single discrete variable
def plot_single_variable_pmf(outcomes, probabilities, title, xlabel, ylabel):
    plt.figure(figsize=(8, 4))
    plt.bar(outcomes, probabilities)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(outcomes)
    plt.grid(axis='y')
    plt.show()

# Function to plot joint PMF for two discrete variables
def plot_joint_variable_pmf(outcomes, joint_probabilities, title, xlabel, ylabel, zlabel):
    X, Y = np.meshgrid(outcomes, outcomes)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(X.flatten(), Y.flatten(), np.zeros_like(X.flatten()), 1, 1, joint_probabilities.flatten())
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    plt.xticks(outcomes)
    plt.yticks(outcomes)
    plt.show()

# Data generation for the single variable PMF (e.g., rolling a six-sided die)
outcomes_die = np.arange(1, 7)  # Possible outcomes: 1, 2, 3, 4, 5, 6
probabilities_die = np.full(6, 1/6)  # Equal probability for each outcome

# Data generation for the joint variable PMF (e.g., two six-sided dice)
joint_probabilities_dice = np.full((6, 6), 1/36)  # Equal probability for each pair of outcomes

# Plotting the single variable PMF
plot_single_variable_pmf(outcomes_die, probabilities_die, 
                         title='Probability Mass Function of a Six-Sided Die', 
                         xlabel='Outcome', ylabel='Probability')

# Plotting the joint variable PMF for two dice
plot_joint_variable_pmf(outcomes_die, joint_probabilities_dice, 
                        title='Joint Probability Mass Function of Two Six-Sided Dice', 
                        xlabel='Die 1 Outcome', ylabel='Die 2 Outcome', zlabel='Probability')
