import matplotlib.pyplot as plt
import matplotlib_venn as venn

def calculate_probabilities(P_A, P_B_given_A, P_B):
    """
    Calculate the intersection and exclusive probabilities based on given values.
    """
    if not all(0 <= p <= 1 for p in [P_A, P_B_given_A, P_B]):
        raise ValueError("Probabilities must be between 0 and 1.")

    P_A_and_B = P_A * P_B_given_A
    P_A_without_B = P_A - P_A_and_B
    P_B_without_A = P_B - P_A_and_B
    P_neither_A_nor_B = 1 - P_A - P_B_without_A

    return P_A_without_B, P_B_without_A, P_A_and_B, P_neither_A_nor_B

def plot_venn_diagram(P_A_without_B, P_B_without_A, P_A_and_B):
    """
    Plot a Venn diagram based on the calculated probabilities.
    """
    plt.figure(figsize=(8, 8))
    venn_diagram = venn.venn2(subsets=(P_A_without_B, P_B_without_A, P_A_and_B), 
                              set_labels=('Event A', 'Event B'))

    venn_diagram.get_label_by_id('10').set_text(f'P(A) without B\n= {P_A_without_B:.2f}')
    venn_diagram.get_label_by_id('01').set_text(f'P(B) without A\n= {P_B_without_A:.2f}')
    venn_diagram.get_label_by_id('11').set_text(f'P(A and B)\n= {P_A_and_B:.2f}')

    plt.title("Venn Diagram for Bayes' Theorem")
    plt.show()

# Example probabilities for demonstration
P_A = 0.3  # Probability of Event A
P_B_given_A = 0.8  # Probability of Event B given A
P_B = 0.4  # Total probability of Event B

# Calculate and Plot
try:
    P_A_without_B, P_B_without_A, P_A_and_B, _ = calculate_probabilities(P_A, P_B_given_A, P_B)
    plot_venn_diagram(P_A_without_B, P_B_without_A, P_A_and_B)
except ValueError as e:
    print(e)
