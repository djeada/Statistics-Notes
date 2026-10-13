import matplotlib.pyplot as plt
import numpy as np


def calculate_probability(r):
    """
    Probability that a point chosen uniformly in the unit square is at a
    distance less than r from the corner (0, 0).

    The area of {x^2 + y^2 < r^2} intersected with the unit square is
        pi r^2 / 4                                        for 0 <= r <= 1,
        r^2 (arcsin(1/r) - pi/4) + sqrt(r^2 - 1)          for 1 < r <= sqrt(2),
        1                                                 for r > sqrt(2).
    """
    if r <= 0:
        return 0.0
    if r <= 1:
        return np.pi * r**2 / 4
    if r <= np.sqrt(2):
        return r**2 * (np.arcsin(1 / r) - np.pi / 4) + np.sqrt(r**2 - 1)
    return 1.0


def simulate_probability(r, n=200_000, seed=0):
    """Monte Carlo estimate of the same probability."""
    rng = np.random.default_rng(seed)
    x, y = rng.random(n), rng.random(n)
    return np.mean(np.hypot(x, y) < r)


def plot_square_and_circle(r):
    """
    Plot the square and the quarter circle to visualize the problem.
    """
    fig, ax = plt.subplots()

    square = plt.Rectangle((0, 0), 1, 1, edgecolor="black", facecolor="none")
    ax.add_patch(square)

    theta = np.linspace(0, np.pi / 2, 100)
    ax.plot(r * np.cos(theta), r * np.sin(theta), color="red")

    ax.set_xlim(0, max(1.1 * r, 1.1))
    ax.set_ylim(0, max(1.1 * r, 1.1))
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"Quarter circle with radius {r} in the unit square")

    return fig, ax


def main():
    for r in (0.8, 1.0, 1.2, np.sqrt(2), 1.5):
        exact = calculate_probability(r)
        approx = simulate_probability(r)
        print(f"r = {r:.4f}: exact = {exact:.4f}, simulated = {approx:.4f}")

    plot_square_and_circle(0.8)
    plt.show()


if __name__ == "__main__":
    main()
