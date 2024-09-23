import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Step 1: Generate synthetic data
np.random.seed(42)
n = 100  # Sample size
X = np.random.uniform(0, 10, size=n)  # Independent variable (random uniform distribution)
true_a = 3  # True intercept
true_b = 2  # True slope
noise = np.random.normal(0, 1, size=n)  # Random noise for the dependent variable
Y = true_a + true_b * X + noise  # Dependent variable with noise

# Step 2: Fit the original linear regression model
# Add intercept term to X
X_with_const = sm.add_constant(X)

# Fit the OLS model
model = sm.OLS(Y, X_with_const).fit()

# Extract estimated parameters (intercept and slope)
a_hat, b_hat = model.params
residuals = model.resid  # Residuals from the original model

# Step 3: Residual resampling bootstrap for slope estimation
B = 1000  # Number of bootstrap samples
bootstrap_b = []  # List to store bootstrap slope estimates

# Resample residuals and refit the model B times
for _ in range(B):
    # Resample residuals with replacement
    resampled_residuals = np.random.choice(residuals, size=n, replace=True)
    
    # Generate new responses using the resampled residuals
    Y_star = a_hat + b_hat * X + resampled_residuals
    
    # Refit the OLS model to the new responses
    model_star = sm.OLS(Y_star, X_with_const).fit()
    
    # Store the new slope estimate
    bootstrap_b.append(model_star.params[1])

# Convert list of bootstrap slope estimates to a numpy array
bootstrap_b = np.array(bootstrap_b)

# Step 4: Estimate the standard error of the original slope estimate (b_hat)
standard_error_b = np.std(bootstrap_b)

# Step 5: Plot the distribution of the bootstrap slope estimates
plt.figure(figsize=(10, 6))

# Plot histogram of the bootstrap slope estimates
plt.hist(bootstrap_b, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Plot vertical line for the original slope estimate
plt.axvline(b_hat, color='red', linestyle='dashed', linewidth=2, label=f"Original Slope = {b_hat:.4f}")

# Plot aesthetics
plt.title('Bootstrap Distribution of Slope Estimates', fontsize=16)
plt.xlabel('Slope Estimate', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Optimize layout and display the plot
plt.tight_layout()
plt.show()

# Output results
print(f"Original Slope Estimate: {b_hat:.4f}")
print(f"Bootstrap Standard Error of Slope: {standard_error_b:.4f}")
