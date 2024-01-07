import matplotlib.pyplot as plt
import matplotlib_venn as venn

# Example probabilities for demonstration
P_A = 0.3  # Probability of Event A (e.g., having a disease)
P_B_given_A = 0.8  # Probability of Event B given A (e.g., testing positive if having the disease)
P_B = 0.4  # Total probability of Event B (e.g., testing positive)

# Calculating the Intersection probability (P(A and B))
P_A_and_B = P_A * P_B_given_A

# Probability of A without B (just A, not B)
P_A_without_B = P_A - P_A_and_B

# Probability of B without A (just B, not A)
P_B_without_A = P_B - P_A_and_B

# Probability of neither A nor B
P_neither_A_nor_B = 1 - P_A - P_B_without_A

# Creating the Venn diagram
plt.figure(figsize=(8, 8))
venn_diagram = venn.venn2(subsets=(P_A_without_B, P_B_without_A, P_A_and_B), 
                          set_labels=('Event A', 'Event B'))

# Assigning labels for each section with detailed calculations
venn_diagram.get_label_by_id('10').set_text(f'P(A) without B\n= P(A) - P(A and B)\n= {P_A_without_B:.2f}')
venn_diagram.get_label_by_id('01').set_text(f'P(B) without A\n= P(B) - P(A and B)\n= {P_B_without_A:.2f}')
venn_diagram.get_label_by_id('11').set_text(f'P(A and B)\n= {P_A_and_B:.2f}')

# Adding conditional probabilities with calculations as annotations
plt.text(-0.8, 0.5, f'P(B|A) = P(A and B) / P(A)\n= {P_B_given_A:.2f}', fontsize=10)
plt.text(0.6, 0.5, f'P(A|B) = P(A and B) / P(B)\n= {P_A_given_B:.2f}', fontsize=10)

# Display the Venn diagram
plt.title("Venn Diagram for Bayes' Theorem")
plt.show()
