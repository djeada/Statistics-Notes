# Function to plot PMF for a single discrete variable
def plot_single_variable_pmf():
    # Using a simple discrete distribution (e.g., rolling a six-sided die)
    outcomes = np.arange(1, 7)  # Possible outcomes: 1, 2, 3, 4, 5, 6
    probabilities = np.full(6, 1/6)  # Equal probability for each outcome

    plt.figure(figsize=(8, 4))
    plt.bar(outcomes, probabilities)
    plt.title('Probability Mass Function of a Six-Sided Die')
    plt.xlabel('Outcome')
    plt.ylabel('Probability')
    plt.xticks(outcomes)
    plt.grid(axis='y')
    plt.show()

# Function to plot joint PMF for two discrete variables
def plot_joint_variable_pmf():
    # Example: Joint distribution of two six-sided dice
    outcomes = np.arange(1, 7)
    X, Y = np.meshgrid(outcomes, outcomes)
    joint_probabilities = np.full((6, 6), 1/36)  # Equal probability for each pair of outcomes

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(X.flatten(), Y.flatten(), np.zeros_like(X.flatten()), 1, 1, joint_probabilities.flatten())
    ax.set_title('Joint Probability Mass Function of Two Six-Sided Dice')
    ax.set_xlabel('Die 1 Outcome')
    ax.set_ylabel('Die 2 Outcome')
    ax.set_zlabel('Probability')
    plt.xticks(outcomes)
    plt.yticks(outcomes)
    plt.show()

# Generate and display the plots
plot_single_variable_pmf()
plot_joint_variable_pmf()

