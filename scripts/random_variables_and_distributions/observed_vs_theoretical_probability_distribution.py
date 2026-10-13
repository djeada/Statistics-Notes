"""Observed relative frequencies of die rolls versus the theoretical pmf."""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def roll_dice(n, rng):
    """Simulate rolling a fair 6-sided die n times."""
    return rng.integers(1, 7, size=n)


def compute_relative_frequencies(roll_results):
    """Relative frequency of each outcome 1..6."""
    counts = pd.Series(roll_results).value_counts().sort_index()
    return counts / len(roll_results)


def main():
    rng = np.random.default_rng(42)
    n_rolls = 10000
    rolls = roll_dice(n_rolls, rng)

    relative_frequencies = compute_relative_frequencies(rolls)
    theoretical = pd.Series(1 / 6, index=np.arange(1, 7))

    plt.figure(figsize=(10, 6))
    plt.bar(relative_frequencies.index - 0.2, relative_frequencies.values, width=0.4,
            label="Observed relative frequencies", color="lightgreen", edgecolor="black")
    plt.bar(theoretical.index + 0.2, theoretical.values, width=0.4,
            label="Theoretical probabilities", color="orange", edgecolor="black")
    plt.title(f"Observed vs Theoretical Probability Distribution ({n_rolls} Rolls)", fontsize=14)
    plt.xlabel("Dice Outcome", fontsize=12)
    plt.ylabel("Probability / Relative Frequency", fontsize=12)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

    print(f"Sample mean     = {rolls.mean():.4f}  (theory 3.5)")
    print(f"Sample variance = {rolls.var():.4f}  (theory {35 / 12:.4f})")
    print(f"Max |observed - theoretical| = {np.abs(relative_frequencies - theoretical).max():.4f}")


if __name__ == "__main__":
    main()
