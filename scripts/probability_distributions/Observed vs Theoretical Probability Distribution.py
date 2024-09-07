import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to simulate dice rolls
def roll_dice(n: int) -> np.ndarray:
    """
    Simulate rolling a fair 6-sided die 'n' times.
    
    Parameters:
        n (int): The number of times to roll the die.
        
    Returns:
        np.ndarray: An array of integers representing the outcomes of the dice rolls.
    """
    return np.random.randint(1, 7, size=n)

# Function to plot the frequency distribution of dice rolls
def plot_distribution(roll_results: np.ndarray, n_rolls: int) -> None:
    """
    Plot the frequency distribution of dice roll outcomes.
    
    Parameters:
        roll_results (np.ndarray): An array of dice roll outcomes.
        n_rolls (int): The number of dice rolls.
    """
    # Count frequency of each outcome (1 through 6)
    outcome_counts = pd.Series(roll_results).value_counts().sort_index()

    # Create the bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(outcome_counts.index, outcome_counts.values, color='skyblue', edgecolor='black')
    plt.title(f'Distribution of {n_rolls} Dice Rolls', fontsize=14)
    plt.xlabel('Dice Outcome', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.xticks(outcome_counts.index)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Function to compute relative frequencies of dice rolls
def compute_relative_frequencies(roll_results: np.ndarray) -> pd.Series:
    """
    Compute the relative frequencies of each dice outcome (1 to 6).
    
    Parameters:
        roll_results (np.ndarray): An array of dice roll outcomes.
        
    Returns:
        pd.Series: A series containing the relative frequencies for each outcome.
    """
    outcome_counts = pd.Series(roll_results).value_counts().sort_index()
    relative_frequencies = outcome_counts / len(roll_results)
    return relative_frequencies

# Function to calculate the mean of dice rolls
def calculate_mean(roll_results: np.ndarray) -> float:
    """
    Calculate the mean of dice roll outcomes.
    
    Parameters:
        roll_results (np.ndarray): An array of dice roll outcomes.
        
    Returns:
        float: The mean (average) of the outcomes.
    """
    return np.mean(roll_results)

# Function to calculate the variance of the dice rolls
def calculate_variance(roll_results: np.ndarray) -> float:
    """
    Calculate the variance of dice roll outcomes.
    
    Parameters:
        roll_results (np.ndarray): An array of dice roll outcomes.
        
    Returns:
        float: The variance of the outcomes.
    """
    return np.var(roll_results)

# Simulating_sample_size_variation a larger number of rolls (10,000 rolls)
n_rolls_large = 10000
large_roll_results = roll_dice(n_rolls_large)

# Computing the relative frequencies
relative_frequencies = compute_relative_frequencies(large_roll_results)

# Theoretical probability distribution for a fair die
theoretical_distribution = pd.Series([1/6]*6, index=np.arange(1, 7))

# Plotting the relative frequencies and comparing with the theoretical distribution
plt.figure(figsize=(10, 6))
plt.bar(relative_frequencies.index - 0.2, relative_frequencies.values, width=0.4, 
        label='Observed Relative Frequencies', color='lightgreen', edgecolor='black')
plt.bar(theoretical_distribution.index + 0.2, theoretical_distribution.values, width=0.4, 
        label='Theoretical Probabilities', color='orange', edgecolor='black')
plt.title(f'Observed vs Theoretical Probability Distribution ({n_rolls_large} Rolls)', fontsize=14)
plt.xlabel('Dice Outcome', fontsize=12)
plt.ylabel('Probability / Relative Frequency', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Calculating the mean and variance of the results
mean_result = calculate_mean(large_roll_results)
variance_result = calculate_variance(large_roll_results)

# Display the results
mean_result, variance_result
