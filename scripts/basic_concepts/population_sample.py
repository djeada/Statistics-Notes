import numpy as np
import matplotlib.pyplot as plt

# Define the population data (e.g., heights in inches)
population_data = np.array([68, 70, 72, 66, 74, 71, 69, 75, 73, 67, 70, 72, 68, 70, 71, 69, 72, 74, 68, 70])

# Define the sample size
sample_size = 5

# Generate a random sample from the population
sample = np.random.choice(population_data, size=sample_size, replace=False)

# Calculate sample statistics
sample_mean = np.mean(sample)
sample_std_dev = np.std(sample)
sample_variance = np.var(sample)

# Plot the population data
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.hist(population_data, bins=10, edgecolor='black', alpha=0.7)
plt.title('Population Data')
plt.xlabel('Height (inches)')
plt.ylabel('Frequency')

# Plot the random sample
plt.subplot(1, 2, 2)
plt.hist(sample, bins=5, edgecolor='black', alpha=0.7, color='green')
plt.title('Random Sample')
plt.xlabel('Height (inches)')
plt.ylabel('Frequency')

# Display population and sample statistics
plt.tight_layout()
plt.show()

print("Sample Mean:", sample_mean)
print("Sample Standard Deviation:", sample_std_dev)
print("Sample Variance:", sample_variance)
