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
    plt.stem(n, sequence)
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
    return np.real_if_close(sequence)

def main():
    print("Difference Equation Demonstration")
    n_terms = 10

    # Example 1: distinct real roots (the worked example in the notes)
    print("Example 1: a_n = 5 a_(n-1) - 6 a_(n-2), a_0 = 4, a_1 = 10")
    recursive = solve_difference_equation((4, 10), (5, -6), n_terms)
    closed = general_solution((5, -6), (4, 10), n_terms)
    print("recursion:    ", recursive)
    print("closed form:  ", np.real(closed))
    print("2*2^n + 2*3^n:", 2 * 2.0 ** np.arange(n_terms) + 2 * 3.0 ** np.arange(n_terms))
    plot_sequence(recursive, title="a_n = 5a_(n-1) - 6a_(n-2): roots 2 and 3")

    # Example 2: complex roots (oscillating, growing since |root| = sqrt(5) > 1)
    print("Example 2: a_n = 4 a_(n-1) - 5 a_(n-2), a_0 = 4, a_1 = 10")
    recursive = solve_difference_equation((4, 10), (4, -5), n_terms)
    closed = general_solution((4, -5), (4, 10), n_terms)
    print("max |recursion - closed form| =", np.max(np.abs(recursive - closed)))
    plot_sequence(recursive, title="a_n = 4a_(n-1) - 5a_(n-2): complex roots 2 +/- i")

    # Example 3: Fibonacci-type recurrence
    print("Example 3: a_n = a_(n-1) + a_(n-2), a_0 = 2, a_1 = 3")
    fib = solve_difference_equation((2, 3), (1, 1), n_terms)
    print(fib)
    plot_sequence(fib, title="Fibonacci-type sequence (2, 3, 5, 8, ...)")


if __name__ == "__main__":
    main()
