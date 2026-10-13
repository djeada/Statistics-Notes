import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def calculate_probabilities(P_A, P_B_given_A, P_B):
    """
    Calculate the intersection and exclusive probabilities based on given values.

    Returns (P(A only), P(B only), P(A and B), P(neither)).
    """
    if not all(0 <= p <= 1 for p in [P_A, P_B_given_A, P_B]):
        raise ValueError("Probabilities must be between 0 and 1.")

    P_A_and_B = P_A * P_B_given_A
    P_A_without_B = P_A - P_A_and_B
    P_B_without_A = P_B - P_A_and_B
    P_neither_A_nor_B = 1 - P_A - P_B_without_A

    if P_B_without_A < 0 or P_neither_A_nor_B < 0:
        raise ValueError("Inconsistent probabilities: P(A and B) cannot exceed P(B).")

    return P_A_without_B, P_B_without_A, P_A_and_B, P_neither_A_nor_B


def plot_venn_diagram(P_A_without_B, P_B_without_A, P_A_and_B, P_neither):
    """
    Plot a two-set diagram with matplotlib only (regions are labelled; the
    circle sizes are illustrative rather than area-proportional).
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.add_patch(Rectangle((-2.2, -1.6), 5.9, 3.2, fill=False, edgecolor="gray"))
    ax.add_patch(Circle((0, 0), 1.2, alpha=0.4, color="tab:blue"))
    ax.add_patch(Circle((1.5, 0), 1.2, alpha=0.4, color="tab:orange"))

    ax.text(-0.5, 0, f"A only\n{P_A_without_B:.2f}", ha="center", va="center")
    ax.text(0.75, 0, f"A and B\n{P_A_and_B:.2f}", ha="center", va="center")
    ax.text(2.0, 0, f"B only\n{P_B_without_A:.2f}", ha="center", va="center")
    ax.text(3.0, -1.3, f"neither: {P_neither:.2f}", ha="center")
    ax.text(0, 1.35, "Event A", ha="center")
    ax.text(1.5, 1.35, "Event B", ha="center")

    ax.set_xlim(-2.4, 3.9)
    ax.set_ylim(-1.8, 1.8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Venn Diagram for Bayes' Theorem")
    plt.show()


def main():
    # Example probabilities for demonstration
    P_A = 0.3  # Probability of Event A
    P_B_given_A = 0.8  # Probability of Event B given A
    P_B = 0.4  # Total probability of Event B

    a_only, b_only, a_and_b, neither = calculate_probabilities(P_A, P_B_given_A, P_B)
    print(f"P(A only) = {a_only:.2f}, P(B only) = {b_only:.2f}")
    print(f"P(A and B) = {a_and_b:.2f}, P(neither) = {neither:.2f}")

    # Bayes: P(A|B) = P(B|A) P(A) / P(B)
    print(f"P(A|B) = {P_B_given_A * P_A / P_B:.2f}")

    plot_venn_diagram(a_only, b_only, a_and_b, neither)


if __name__ == "__main__":
    main()
