import numpy as np
import matplotlib.pyplot as plt

# Function to plot a sequence
def plot_sequence(sequence_fn, n_terms=100, title="Sequence Example"):
    n = np.arange(1, n_terms + 1)
    sequence_values = sequence_fn(n)
    
    plt.figure(figsize=(8, 5))
    plt.plot(n, sequence_values, marker="o", linestyle="-")
    plt.title(title)
    plt.xlabel("n (term index)")
    plt.ylabel("a_n (sequence value)")
    plt.grid(True)
    plt.show()

# Function to plot partial sums
def plot_partial_sums(sequence_fn, n_terms=100, title="Partial Sums"):
    n = np.arange(1, n_terms + 1)
    sequence_values = sequence_fn(n)
    partial_sums = np.cumsum(sequence_values)
    
    plt.figure(figsize=(8, 5))
    plt.plot(n, partial_sums, marker="o", linestyle="-")
    plt.title(title)
    plt.xlabel("n (number of terms)")
    plt.ylabel("S_n (partial sum)")
    plt.grid(True)
    plt.show()

# Function to demonstrate series convergence for geometric series
def demonstrate_series_convergence(r, n_terms=50):
    n = np.arange(1, n_terms + 1)
    partial_sums = np.cumsum((r ** (n - 1)))
    
    plt.figure(figsize=(8, 5))
    plt.plot(n, partial_sums, marker="o", linestyle="-")
    plt.axhline(y=1/(1 - r), color="r", linestyle="--", label="Limit (1/(1-r))")
    plt.title(f"Convergence of Geometric Series (r={r})")
    plt.xlabel("n (number of terms)")
    plt.ylabel("Partial Sum")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
def main():
    print("Demonstrating sequences and series...")
    
    # Example: Convergent sequence
    print("Plotting a convergent sequence: a_n = n / (n + 2)")
    plot_sequence(lambda n: n / (n + 2), title="Convergent Sequence: a_n = n / (n + 2)")
    
    # Example: Divergent sequence
    print("Plotting a divergent sequence: a_n = 4^n")
    plot_sequence(lambda n: 4 ** n, n_terms=10, title="Divergent Sequence: a_n = 4^n")
    
    # Example: Partial sums of a geometric series
    print("Plotting partial sums of a geometric series: r=1/3")
    plot_partial_sums(lambda n: (1 / 3) ** (n - 1), title="Partial Sums: Geometric Series")
    
    # Example: Convergence of geometric series
    print("Demonstrating convergence of geometric series: r=1/3")
    demonstrate_series_convergence(r=1/3)
    
    # Example: Divergent harmonic series
    print("Plotting partial sums of the harmonic series (divergent).")
    plot_partial_sums(lambda n: 1 / n, title="Partial Sums: Harmonic Series (Divergent)")
    
    # Example: Alternating series
    print("Plotting partial sums of an alternating harmonic series (convergent).")
    plot_partial_sums(lambda n: (-1) ** (n + 1) / n, title="Partial Sums: Alternating Harmonic Series")

if __name__ == "__main__":
    main()
