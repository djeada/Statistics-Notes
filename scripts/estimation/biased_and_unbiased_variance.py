import numpy as np
import matplotlib.pyplot as plt

# Function to simulate a finite population of heights
def generate_population(mean: float, std: float, size: int) -> np.ndarray:
    """
    Generate a population with a normal distribution.
    
    Parameters:
        mean (float): The mean of the population.
        std (float): The standard deviation of the population.
        size (int): The size of the population.
        
    Returns:
        np.ndarray: An array representing the population data.
    """
    return np.random.normal(mean, std, size)

# Function to take a sample from the population with or without replacement
def take_sample(population: np.ndarray, sample_size: int, replace: bool = True) -> np.ndarray:
    """
    Take a random sample from the population, with or without replacement.
    
    Parameters:
        population (np.ndarray): The population array from which to sample.
        sample_size (int): The number of elements to sample.
        replace (bool): Whether to sample with or without replacement.
        
    Returns:
        np.ndarray: The sampled subset of the population.
    """
    return np.random.choice(population, size=sample_size, replace=replace)

# Function to calculate sample mean and variance
def calculate_statistics(sample: np.ndarray) -> dict:
    """
    Calculate the mean and variance of a sample.
    
    Parameters:
        sample (np.ndarray): The sample for which to calculate statistics.
        
    Returns:
        dict: A dictionary containing the mean and variance of the sample.
    """
    return {
        "mean": np.mean(sample),
        "variance": np.var(sample, ddof=1)  # Unbiased variance
    }

# Function to calculate both biased and unbiased variance for a given sample
def calculate_full_variances(sample: np.ndarray) -> dict:
    """
    Calculate both biased and unbiased variance for a given sample.
    
    Parameters:
        sample (np.ndarray): The sample to compute variance on.
        
    Returns:
        dict: A dictionary containing both biased and unbiased variance.
    """
    biased_variance = np.var(sample, ddof=0)   # Biased variance (divided by n)
    unbiased_variance = np.var(sample, ddof=1) # Unbiased variance (divided by n-1)
    return {
        "biased_variance": biased_variance,
        "unbiased_variance": unbiased_variance
    }

# Generate a finite population of heights for 500 individuals
population_size = 500
population_mean = 170  # Mean height in cm
population_std = 10     # Standard deviation in cm
finite_population_heights = generate_population(population_mean, population_std, population_size)

# Define a smaller sample size (20 individuals sampled)
sample_size = 20

# Sampling with and without replacement
sample_with_replacement_stats = calculate_statistics(take_sample(finite_population_heights, sample_size, replace=True))
sample_without_replacement_stats = calculate_statistics(take_sample(finite_population_heights, sample_size, replace=False))

# Calculate full variances (biased and unbiased) for both with and without replacement
full_variances_with_replacement = calculate_full_variances(take_sample(finite_population_heights, sample_size, replace=True))
full_variances_without_replacement = calculate_full_variances(take_sample(finite_population_heights, sample_size, replace=False))

# Organize means, biased variances, and unbiased variances for plotting
means = {
    "With Replacement": sample_with_replacement_stats['mean'],
    "Without Replacement": sample_without_replacement_stats['mean']
}

biased_variances = {
    "With Replacement": full_variances_with_replacement['biased_variance'],
    "Without Replacement": full_variances_without_replacement['biased_variance']
}

unbiased_variances = {
    "With Replacement": full_variances_with_replacement['unbiased_variance'],
    "Without Replacement": full_variances_without_replacement['unbiased_variance']
}

# Calculate the population statistics (real mean and variance)
real_population_mean = np.mean(finite_population_heights)
real_population_variance = np.var(finite_population_heights)

# Function to plot all statistics (including the real mean and variance)
def plot_full_statistics_with_population(means, biased_variances, unbiased_variances, real_mean, real_variance) -> None:
    """
    Plot comparison of sample means, biased variance, unbiased variance, and show the real mean and variance.
    
    Parameters:
        means (dict): A dictionary of sample means.
        biased_variances (dict): A dictionary of biased variances.
        unbiased_variances (dict): A dictionary of unbiased variances.
        real_mean (float): The real population mean.
        real_variance (float): The real population variance.
    """
    categories = ['With Replacement', 'Without Replacement']
    
    # Create subplots for mean, biased variance, and unbiased variance
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))
    
    # Plot sample means
    ax[0].bar(categories, [means['With Replacement'], means['Without Replacement']], color=['blue', 'green'], alpha=0.7)
    ax[0].axhline(y=real_mean, color='red', linestyle='--', label='Population Mean')
    ax[0].set_title('Sample Means of Heights')
    ax[0].set_ylabel('Mean (cm)')
    ax[0].legend()

    # Plot biased variances
    ax[1].bar(categories, [biased_variances['With Replacement'], biased_variances['Without Replacement']], color=['orange', 'purple'], alpha=0.7)
    ax[1].axhline(y=real_variance, color='red', linestyle='--', label='Population Variance')
    ax[1].set_title('Biased Sample Variances of Heights')
    ax[1].set_ylabel('Variance (cm^2)')
    ax[1].legend()
    
    # Plot unbiased variances
    ax[2].bar(categories, [unbiased_variances['With Replacement'], unbiased_variances['Without Replacement']], color=['cyan', 'magenta'], alpha=0.7)
    ax[2].axhline(y=real_variance, color='red', linestyle='--', label='Population Variance')
    ax[2].set_title('Unbiased Sample Variances of Heights')
    ax[2].set_ylabel('Variance (cm^2)')
    ax[2].legend()
    
    plt.tight_layout()
    plt.show()

# Plotting all statistics with real mean and variance
plot_full_statistics_with_population(means, biased_variances, unbiased_variances, real_population_mean, real_population_variance)
