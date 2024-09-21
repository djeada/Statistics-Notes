import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

# Parameters for two negative binomial distributions
r1, p1 = 5, 0.5  # number of successes and probability of success for the first distribution
r2, p2 = 3, 0.7  # number of successes and probability of success for the second distribution

# Generate x values (number of trials required for r successes)
x_negbinom_1 = np.arange(r1, r1 + 30)  # we'll consider a range of possible trials
x_negbinom_2 = np.arange(r2, r2 + 30)

# Calculate the PMF and CDF for the negative binomial distributions
pmf_negbinom_1 = nbinom.pmf(x_negbinom_1 - r1, r1, p1)
pmf_negbinom_2 = nbinom.pmf(x_negbinom_2 - r2, r2, p2)

cdf_negbinom_1 = nbinom.cdf(x_negbinom_1 - r1, r1, p1)
cdf_negbinom_2 = nbinom.cdf(x_negbinom_2 - r2, r2, p2)

# Create two separate plots for the PMF and CDF

# Plot 1: PMF of Negative Binomial Distributions
plt.figure(figsize=(10, 6))
plt.stem(x_negbinom_1, pmf_negbinom_1, basefmt=" ", linefmt="blue", markerfmt="bo", label=f'NegBinomial(r={r1}, p={p1}) PMF')
plt.stem(x_negbinom_2, pmf_negbinom_2, basefmt=" ", linefmt="red", markerfmt="ro", label=f'NegBinomial(r={r2}, p={p2}) PMF')
plt.title('Probability Mass Function (PMF) of Negative Binomial Distributions')
plt.xlabel('Number of Trials (k)')
plt.ylabel('PMF')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: CDF of Negative Binomial Distributions
plt.figure(figsize=(10, 6))
plt.step(x_negbinom_1, cdf_negbinom_1, where="mid", label=f'NegBinomial(r={r1}, p={p1}) CDF', color='blue')
plt.step(x_negbinom_2, cdf_negbinom_2, where="mid", label=f'NegBinomial(r={r2}, p={p2}) CDF', color='red')
plt.title('Cumulative Distribution Function (CDF) of Negative Binomial Distributions')
plt.xlabel('Number of Trials (k)')
plt.ylabel('CDF')
plt.legend()
plt.grid(True)
plt.show()
