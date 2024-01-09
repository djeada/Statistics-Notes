# Function to plot CDF for a single variable
def plot_single_variable_cdf():
    # Using a normal distribution as an example
    x = np.linspace(-5, 5, 1000)
    cdf = norm.cdf(x, 0, 1)  # Normal distribution with mean=0 and std=1

    plt.figure(figsize=(8, 4))
    plt.plot(x, cdf)
    plt.title('Cumulative Distribution Function of a Normal Distribution')
    plt.xlabel('x')
    plt.ylabel('CDF')
    plt.grid(True)
    plt.show()

# Function to plot CDF for a discrete variable (e.g., rolling a six-sided die)
def plot_discrete_variable_cdf():
    # Outcomes and probabilities for a six-sided die
    outcomes = np.arange(1, 8)  # 1 to 7 (7 is not inclusive in plotting)
    probabilities = np.cumsum(np.full(6, 1/6))  # Cumulative sum of probabilities

    plt.figure(figsize=(8, 4))
    plt.step(outcomes, np.append([0], probabilities), where='post')
    plt.title('Cumulative Distribution Function of a Six-Sided Die')
    plt.xlabel('Outcome')
    plt.ylabel('CDF')
    plt.xticks(outcomes - 0.5)
    plt.yticks(np.linspace(0, 1, 7))
    plt.grid(True)
    plt.show()

# Generate and display the plots
plot_single_variable_cdf()
plot_discrete_variable_cdf()

