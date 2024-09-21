from scipy.stats import binom

# Parameters for two binomial distributions
n1, p1 = 10, 0.5  # number of trials and probability of success for the first distribution
n2, p2 = 15, 0.7  # number of trials and probability of success for the second distribution

# Generate x values (possible number of successes)
x_binom_1 = np.arange(0, n1 + 1)
x_binom_2 = np.arange(0, n2 + 1)

# Calculate the PMF and CDF for the binomial distributions
pmf_binom_1 = binom.pmf(x_binom_1, n1, p1)
pmf_binom_2 = binom.pmf(x_binom_2, n2, p2)

cdf_binom_1 = binom.cdf(x_binom_1, n1, p1)
cdf_binom_2 = binom.cdf(x_binom_2, n2, p2)

# Create two separate plots for the PMF and CDF

# Plot 1: PMF of Binomial Distributions
plt.figure(figsize=(10, 6))
plt.stem(x_binom_1, pmf_binom_1, basefmt=" ", linefmt="blue", markerfmt="bo", label=f'Binomial(n={n1}, p={p1}) PMF')
plt.stem(x_binom_2, pmf_binom_2, basefmt=" ", linefmt="red", markerfmt="ro", label=f'Binomial(n={n2}, p={p2}) PMF')
plt.title('Probability Mass Function (PMF) of Binomial Distributions')
plt.xlabel('Number of Successes (k)')
plt.ylabel('PMF')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of Binomial Distributions
plt.figure(figsize=(10, 6))
plt.step(x_binom_1, cdf_binom_1, where="mid", label=f'Binomial(n={n1}, p={p1}) CDF', color='blue')
plt.step(x_binom_2, cdf_binom_2, where="mid", label=f'Binomial(n={n2}, p={p2}) CDF', color='red')
plt.title('Cumulative Distribution Function (CDF) of Binomial Distributions')
plt.xlabel('Number of Successes (k)')
plt.ylabel('CDF')
plt.legend()
plt.grid(True)
plt.show()
