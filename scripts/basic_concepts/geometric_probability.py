import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def calculate_probability(r):
    """
    Calculate the probability that a randomly chosen point inside the square
    is at a distance less than r from the bottom left corner (0,0).
    """
    if r < 1:
        # When the circle is completely within the square
        probability = (np.pi * r ** 2) / 4
    elif r == np.sqrt(2):
        # When the circle exactly covers the square
        probability = 1
    else:
        # When the circle extends outside the square
        # Integral from 0 to 1 for the area within the square
        area_within_square, _ = quad(lambda x: np.sqrt(r ** 2 - x ** 2), 0, 1)
        probability = area_within_square

    return probability


def plot_square_and_circle(r):
    """
    Plot the square and the quarter circle to visualize the problem.
    """
    # Create a figure
    fig, ax = plt.subplots()

    # Plot square
    square = plt.Rectangle((0, 0), 1, 1, edgecolor="black", facecolor="none")
    ax.add_patch(square)

    # Plot quarter circle
    theta = np.linspace(0, np.pi / 2, 100)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, color="red")

    # Setting the limits of the plot
    ax.set_xlim(0, max(1.1 * r, 1))
    ax.set_ylim(0, max(1.1 * r, 1))
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"Quarter Circle with radius {r} in a Square")

    return fig, ax


# Example radius
r = 0.8
probability = calculate_probability(r)
plot_square_and_circle(r)
probability
