import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define population parameters
population_mean = 100    # Mean of the population
population_std = 15      # Standard deviation of the population
sample_size = 30         # Size of each sample
B = 1000                 # Number of independent samples (iterations)

# Step 2: Monte Carlo simulation - Drawing B samples and calculating sample means
np.random.seed(42)  # Setting seed for reproducibility
sample_means = []

for _ in range(B):
    # Draw a sample from the normal distribution
    sample = np.random.normal(loc=population_mean, scale=population_std, size=sample_size)
    sample_mean = np.mean(sample)  # Calculate sample mean
    sample_means.append(sample_mean)

# Convert list of sample means to a numpy array for further calculations
sample_means = np.array(sample_means)

# Step 3: Calculate the overall mean of the sample means (theta_bar)
theta_bar = np.mean(sample_means)

# Step 4: Estimate the standard error using the Monte Carlo formula
# Formula: sqrt( sum( (sample_means - theta_bar)^2 ) / (B - 1) )
standard_error_estimate = np.sqrt(np.sum((sample_means - theta_bar)**2) / (B - 1))

# Step 5: Display the results
print(f"Estimated Standard Error (Monte Carlo): {standard_error_estimate:.4f}")

# Step 6: Plotting the distribution of sample means
plt.figure(figsize=(10, 6))

# Histogram of sample means
plt.hist(sample_means, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Add vertical lines for the sample mean and population mean
plt.axvline(theta_bar, color='red', linestyle='dashed', linewidth=2, label=f"Mean of Sample Means = {theta_bar:.4f}")
plt.axvline(population_mean, color='green', linestyle='dotted', linewidth=2, label=f"Population Mean = {population_mean}")

# Plot aesthetics
plt.title('Distribution of Sample Means (Monte Carlo Simulation)', fontsize=16)
plt.xlabel('Sample Mean', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Optimize layout and display the plot
plt.tight_layout()
plt.show()
