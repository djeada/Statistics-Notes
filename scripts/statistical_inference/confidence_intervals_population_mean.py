from scipy.stats import sem, t

# Function to calculate confidence interval
def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_err = sem(data)
    margin = std_err * t.ppf((1 + confidence) / 2., n - 1)
    return mean - margin, mean, mean + margin

# Parameters for data generation
sample_size = 100
true_mean = 50
std_dev = 5

# Generate sample data
np.random.seed(0)
data = np.random.normal(true_mean, std_dev, sample_size)

# Calculate confidence interval
lower_bound, sample_mean, upper_bound = confidence_interval(data)

# Plotting
plt.figure(figsize=(10, 4))
plt.hist(data, bins=15, alpha=0.7, label='Sample Data')
plt.axvline(sample_mean, color='red', linestyle='dashed', linewidth=2, label='Sample Mean')
plt.axvline(lower_bound, color='green', linestyle='dashed', linewidth=2, label='Lower Bound of CI')
plt.axvline(upper_bound, color='blue', linestyle='dashed', linewidth=2, label='Upper Bound of CI')
plt.title(f"Confidence Interval for Mean (95%)")
plt.legend()
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
