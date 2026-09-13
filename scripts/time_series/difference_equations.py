import numpy as np
import matplotlib.pyplot as plt

# Function to solve a second-order difference equation
def solve_difference_equation(initial_conditions, coefficients, n_terms):
    """
    Solve a second-order linear difference equation of the form:
    a_n = β1 * a_(n-1) + β2 * a_(n-2)

    Args:
        initial_conditions (tuple): Initial conditions (a_0, a_1)
        coefficients (tuple): Coefficients (β1, β2)
        n_terms (int): Number of terms to compute

    Returns:
        np.ndarray: Array of sequence values
    """
    a_0, a_1 = initial_conditions
    β1, β2 = coefficients

    sequence = [a_0, a_1]
    for n in range(2, n_terms):
        next_term = β1 * sequence[-1] + β2 * sequence[-2]
        sequence.append(next_term)

    return np.array(sequence)

# Function to plot the sequence
def plot_sequence(sequence, title):
    n = np.arange(len(sequence))
    plt.figure(figsize=(8, 5))
    plt.stem(n, sequence, use_line_collection=True)
    plt.title(title)
    plt.xlabel("n (term index)")
    plt.ylabel("a_n (sequence value)")
    plt.grid(True)
    plt.show()

# Function to compute the general solution from characteristic equation
def general_solution(coefficients, initial_conditions, n_terms):
    """
    Compute the general solution of a second-order difference equation.

    Args:
        coefficients (tuple): Coefficients (β1, β2)
        initial_conditions (tuple): Initial conditions (a_0, a_1)
        n_terms (int): Number of terms to compute

    Returns:
        np.ndarray: General solution values
    """
    β1, β2 = coefficients

    # Solve the characteristic equation
    char_eq = [1, -β1, -β2]  # λ^2 - β1λ - β2 = 0
    roots = np.roots(char_eq)

    # General solution: a_n = c1 * λ1^n + c2 * λ2^n
    λ1, λ2 = roots
    a_0, a_1 = initial_conditions

    # Solve for c1 and c2 using the initial conditions
    A = np.array([[1, 1], [λ1, λ2]])
    B = np.array([a_0, a_1])
    c1, c2 = np.linalg.solve(A, B)

    # Generate the terms using the general solution
    n = np.arange(n_terms)
    sequence = c1 * (λ1 ** n) + c2 * (λ2 ** n)
    return sequence

# Main function
def main():
    print("Difference Equation Demonstration")

    # Example 1: Solve a second-order difference equation
    print("Example 1: Solving a_n = 4 * a_(n-1) - 5 * a_(n-2)")
    initial_conditions = (4, 10)
    coefficients = (4, -5)
    n_terms = 10

    sequence = solve_difference_equation(initial_conditions, coefficients, n_terms)
    plot_sequence(sequence, title="Second-Order Difference Equation Solution")

    # Example 2: General solution for the same equation
    print("Example 2: General solution with a_0 = 4, a_1 = 10")
    general_sol = general_solution(coefficients, initial_conditions, n_terms)
    plot_sequence(general_sol, title="General Solution for Difference Equation")

    # Example 3: Fibonacci sequence
    print("Example 3: Fibonacci Sequence")
    fibonacci_initial_conditions = (2, 3)
    fibonacci_coefficients = (1, 1)
    fibonacci_sequence = solve_difference_equation(fibonacci_initial_conditions, fibonacci_coefficients, n_terms)
    plot_sequence(fibonacci_sequence, title="Fibonacci Sequence")

if __name__ == "__main__":
    main()
