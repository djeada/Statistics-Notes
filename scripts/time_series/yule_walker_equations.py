import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.stattools import acf

# Set random seed for reproducibility
np.random.seed(42)

# 1. Simulate an AR Process
def simulate_ar_process(phi, n_samples=500):
    """
    Simulate an AR process of order p with given coefficients.

    Parameters:
    - phi: List or array of AR coefficients (phi_1, phi_2, ..., phi_p)
    - n_samples: Number of samples to generate

    Returns:
    - x: Simulated time series
    """
    p = len(phi)
    x = np.zeros(n_samples)
    # Assume zero mean and unit variance for epsilon
    epsilon = np.random.normal(0, 1, n_samples)
    
    for t in range(p, n_samples):
        x[t] = np.dot(phi, x[t-p:t][::-1]) + epsilon[t]
    return x

# Define AR coefficients (True parameters)
true_phi = np.array([0.75, -0.25])  # AR(2) model: X_t = 0.75 X_{t-1} -0.25 X_{t-2} + epsilon_t

# Simulate the AR process
n_samples = 500
x = simulate_ar_process(true_phi, n_samples)

# 2. Compute Autocorrelation Function (ACF)
max_lag = len(true_phi)
acf_values = acf(x, nlags=max_lag, fft=True)

# 3. Set Up Yule-Walker Equations
# The Yule-Walker equations can be written in matrix form: R * phi = r
R = np.array([acf_values[abs(i-j)] for i in range(1, max_lag+1) for j in range(1, max_lag+1)]).reshape(max_lag, max_lag)
r = acf_values[1:max_lag+1]

# 4. Solve for AR Coefficients using Yule-Walker Equations
estimated_phi = np.linalg.solve(R, r)

# 5. Visualization
fig, axs = plt.subplots(3, 2, figsize=(15, 15))

# a. Time Series Plot
axs[0, 0].plot(x, color='blue')
axs[0, 0].set_title('Simulated AR Time Series')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('Value')

# b. Autocorrelation Function
lags = np.arange(0, max_lag+1)
axs[0, 1].stem(lags, acf_values, use_line_collection=True)
axs[0, 1].set_title('Autocorrelation Function (ACF)')
axs[0, 1].set_xlabel('Lag')
axs[0, 1].set_ylabel('Autocorrelation')

# c. Autocorrelation Matrix (Toeplitz Matrix)
cax = axs[1, 0].matshow(R, cmap='viridis')
fig.colorbar(cax, ax=axs[1, 0])
axs[1, 0].set_title('Autocorrelation Matrix (R)')
axs[1, 0].set_xlabel('Phi Coefficients')
axs[1, 0].set_ylabel('Equation Rows')
axs[1, 0].set_xticks(range(max_lag))
axs[1, 0].set_yticks(range(max_lag))
axs[1, 0].set_xticklabels([f'phi_{i+1}' for i in range(max_lag)])
axs[1, 0].set_yticklabels([f'Equation {i+1}' for i in range(max_lag)])

# d. Right-Hand Side Vector (r)
axs[1, 1].stem(np.arange(1, max_lag+1), r, use_line_collection=True, linefmt='r-', markerfmt='ro')
axs[1, 1].set_title('Right-Hand Side Vector (r)')
axs[1, 1].set_xlabel('Lag')
axs[1, 1].set_ylabel('Autocorrelation')

# e. Yule-Walker System Solution
equation_text = '\n'.join([f"phi_{i+1} = {estimated_phi[i]:.4f}" for i in range(max_lag)])
axs[2, 0].text(0.1, 0.5, equation_text, fontsize=12, verticalalignment='center')
axs[2, 0].axis('off')
axs[2, 0].set_title('Estimated AR Coefficients from Yule-Walker')

# f. Comparison of True and Estimated Coefficients
index = np.arange(1, max_lag+1)
bar_width = 0.35
axs[2, 1].bar(index, true_phi, bar_width, label='True Phi')
axs[2, 1].bar(index + bar_width, estimated_phi, bar_width, label='Estimated Phi')
axs[2, 1].set_xlabel('Phi Coefficients')
axs[2, 1].set_ylabel('Coefficient Value')
axs[2, 1].set_title('Comparison of True and Estimated AR Coefficients')
axs[2, 1].set_xticks(index + bar_width / 2)
axs[2, 1].set_xticklabels([f'phi_{i}' for i in range(1, max_lag+1)])
axs[2, 1].legend()

plt.tight_layout()
plt.show()

# Optional: Print the estimated coefficients
print("True AR coefficients:", true_phi)
print("Estimated AR coefficients from Yule-Walker:", estimated_phi)
