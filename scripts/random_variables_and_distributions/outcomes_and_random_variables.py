"""Outcomes of a die roll as a random variable: simulated frequencies and mean."""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def roll_dice(n, rng):
    """Simulate rolling a fair 6-sided die n times."""
    return rng.integers(1, 7, size=n)


def plot_distribution(roll_results, n_rolls):
    """Bar chart of the frequency of each outcome."""
    outcome_counts = pd.Series(roll_results).value_counts().sort_index()
    plt.figure(figsize=(8, 6))
    plt.bar(outcome_counts.index, outcome_counts.values, color="skyblue", edgecolor="black")
    plt.title(f"Distribution of {n_rolls} Dice Rolls", fontsize=14)
    plt.xlabel("Dice Outcome", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(outcome_counts.index)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


def main():
    rng = np.random.default_rng(42)
    n_rolls = 1000
    rolls = roll_dice(n_rolls, rng)
    plot_distribution(rolls, n_rolls)
    print(f"Sample mean of {n_rolls} rolls = {rolls.mean():.3f} (theoretical 3.5)")


if __name__ == "__main__":
    main()
