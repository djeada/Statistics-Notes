# Parameters for two Poisson distributions
lambda1 = 3  # mean number of events for the first distribution
lambda2 = 5  # mean number of events for the second distribution

# Generate x values (possible number of events)
x_poisson_1 = np.arange(0, 15)
x_poisson_2 = np.arange(0, 15)

# Calculate the PMF and CDF for the Poisson distributions
pmf_poisson_1 = nbinom.pmf(x_poisson_1, 1, np.exp(-lambda1))
pmf_poisson_2 = nbinom.pmf(x_poisson_2, 1, np.exp(-lambda2))

cdf_poisson_1 = np.cumsum(pmf_poisson_1)
cdf_poisson_2 = np.cumsum(pmf_poisson_2)

# Create two separate plots for the PMF and CDF

# Plot 1: PMF of Poisson Distributions
plt.figure(figsize=(10, 6))
plt.stem(x_poisson_1, pmf_poisson_1, basefmt=" ", linefmt="blue", markerfmt="bo", label=f'Poisson(λ={lambda1}) PMF')
plt.stem(x_poisson_2, pmf_poisson_2, basefmt=" ", linefmt="red", markerfmt="ro", label=f'Poisson(λ={lambda2}) PMF')
plt.title('Probability Mass Function (PMF) of Poisson Distributions')
plt.xlabel('Number of Events (k)')
plt.ylabel('PMF')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of Poisson Distributions
plt.figure(figsize=(10, 6))
plt.step(x_poisson_1, cdf_poisson_1, where="mid", label=f'Poisson(λ={lambda1}) CDF', color='blue')
plt.step(x_poisson_2, cdf_poisson_2, where="mid", label=f'Poisson(λ={lambda2}) CDF', color='red')
plt.title('Cumulative Distribution Function (CDF) of Poisson Distributions')
plt.xlabel('Number of Events (k)')
plt.ylabel('CDF')
plt.legend()
plt.grid(True)
plt.show()
