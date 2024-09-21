# Parameters for two geometric distributions
p1 = 0.3  # probability of success for the first distribution
p2 = 0.5  # probability of success for the second distribution

# Generate x values (number of trials until first success)
x_geom_1 = np.arange(1, 20)
x_geom_2 = np.arange(1, 20)

# Calculate the PMF and CDF for the geometric distributions
pmf_geom_1 = nbinom.pmf(x_geom_1 - 1, 1, p1)
pmf_geom_2 = nbinom.pmf(x_geom_2 - 1, 1, p2)

cdf_geom_1 = nbinom.cdf(x_geom_1 - 1, 1, p1)
cdf_geom_2 = nbinom.cdf(x_geom_2 - 1, 1, p2)

# Create two separate plots for the PMF and CDF

# Plot 1: PMF of Geometric Distributions
plt.figure(figsize=(10, 6))
plt.stem(x_geom_1, pmf_geom_1, basefmt=" ", linefmt="blue", markerfmt="bo", label=f'Geometric(p={p1}) PMF')
plt.stem(x_geom_2, pmf_geom_2, basefmt=" ", linefmt="red", markerfmt="ro", label=f'Geometric(p={p2}) PMF')
plt.title('Probability Mass Function (PMF) of Geometric Distributions')
plt.xlabel('Number of Trials (k)')
plt.ylabel('PMF')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of Geometric Distributions
plt.figure(figsize=(10, 6))
plt.step(x_geom_1, cdf_geom_1, where="mid", label=f'Geometric(p={p1}) CDF', color='blue')
plt.step(x_geom_2, cdf_geom_2, where="mid", label=f'Geometric(p={p2}) CDF', color='red')
plt.title('Cumulative Distribution Function (CDF) of Geometric Distributions')
plt.xlabel('Number of Trials (k)')
plt.ylabel('CDF')
plt.legend()
plt.grid(True)
plt.show()
