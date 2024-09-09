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

# Function to plot the distribution of dice rolls
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

# Simulating 1000 rolls of the dice
n_rolls_large = 1000
large_roll_results = roll_dice(n_rolls_large)

# Plotting the distribution of the results
plot_distribution(large_roll_results, n_rolls_large)

# Calculate and display the mean of the results
mean_result = calculate_mean(large_roll_results)
mean_result
