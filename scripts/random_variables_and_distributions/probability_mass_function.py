"""PMFs: a fair die and the joint pmf of two fair dice."""
import matplotlib.pyplot as plt
import numpy as np


def plot_single_variable_pmf(outcomes, probabilities, title, xlabel, ylabel):
    plt.figure(figsize=(8, 4))
    plt.bar(outcomes, probabilities)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(outcomes)
    plt.grid(axis="y")
    plt.show()


def plot_joint_variable_pmf(outcomes, joint_probabilities, title, xlabel, ylabel, zlabel):
    x, y = np.meshgrid(outcomes, outcomes)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.bar3d(x.flatten(), y.flatten(), np.zeros_like(x.flatten()), 1, 1, joint_probabilities.flatten())
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_xticks(outcomes)
    ax.set_yticks(outcomes)
    plt.show()


def main():
    outcomes_die = np.arange(1, 7)
    probabilities_die = np.full(6, 1 / 6)
    joint_probabilities_dice = np.full((6, 6), 1 / 36)

    # A pmf must sum to one; the marginal of the joint is the single-die pmf.
    assert np.isclose(probabilities_die.sum(), 1.0)
    assert np.isclose(joint_probabilities_dice.sum(), 1.0)
    assert np.allclose(joint_probabilities_dice.sum(axis=1), probabilities_die)
    print("pmf sums to 1; joint marginals equal the single-die pmf")

    plot_single_variable_pmf(outcomes_die, probabilities_die,
                             "Probability Mass Function of a Six-Sided Die", "Outcome", "Probability")
    plot_joint_variable_pmf(outcomes_die, joint_probabilities_dice,
                            "Joint Probability Mass Function of Two Six-Sided Dice",
                            "Die 1 Outcome", "Die 2 Outcome", "Probability")


if __name__ == "__main__":
    main()
