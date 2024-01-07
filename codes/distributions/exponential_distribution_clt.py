import numpy as np
import matplotlib.pyplot as plt

# Number of samples and sample size
n_samples = 1000
sample_size = 50

# Generate random data from a non-normal distribution (e.g., exponential distribution)
population_data = np.random.exponential(scale=1.0, size=10000)

# Calculate sample means
sample_means = [np.mean(np.random.choice(population_data, sample_size, replace=True)) for _ in range(n_samples)]

# Plotting the histogram of sample means
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.axvline(np.mean(population_data), color='red', linestyle='dashed', linewidth=2)
plt.title('Distribution of Sample Means (Central Limit Theorem)')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.show()

# Output the mean of the population and the mean of the sample means for comparison
population_mean = np.mean(population_data)
mean_of_sample_means = np.mean(sample_means)
standard_error = np.std(population_data) / np.sqrt(sample_size)

population_mean, mean_of_sample_means, standard_error

