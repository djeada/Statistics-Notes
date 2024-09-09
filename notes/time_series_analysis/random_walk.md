## Random Walk Model

The **random walk** is a fundamental and widely used time series model, often applied in finance to represent stock prices and other economic indicators. The idea behind the random walk is that the value of the process at time $t$ is the sum of its value at time $t-1$ and a random shock (or noise). Essentially, each step of the process is unpredictable and governed by randomness.

Mathematically, the random walk model is represented as:

$$
X_t = X_{t-1} + Z_t
$$

Where:

- $X_t$ is the value of the process at time $t$ (e.g., the stock price today).
- $X_{t-1}$ is the value at the previous time step (e.g., the stock price yesterday).
- $Z_t$ is a **white noise** term, typically assumed to follow a normal distribution $Z_t \sim \mathcal{N}(\mu, \sigma^2)$, with mean $\mu$ and variance $\sigma^2$.

### Evolution of a Random Walk Over Time

To better understand how a random walk evolves, we can expand the model over time. Starting at $X_0 = 0$, we have:

$$
X_1 = Z_1
$$
$$
X_2 = Z_1 + Z_2
$$
$$
X_3 = Z_1 + Z_2 + Z_3
$$
$$
X_t = \sum_{i=1}^{t} Z_i
$$

In general, the value at time $t$, $X_t$, is the cumulative sum of all past shocks $Z_1, Z_2, \dots, Z_t$. This means that the random walk retains the effects of all previous shocks, making it highly dependent on its past values.

### Mean and Variance of a Random Walk

The key properties of a random walk are its **mean** and **variance**. Since each step $Z_t$ is a random shock with its own distribution, the behavior of the entire random walk can be derived from the properties of the shocks.

#### Expected Value

The expected value $E[X_t]$ gives us the average or mean value of $X_t$ over time. Since $Z_t \sim \mathcal{N}(\mu, \sigma^2)$, the expected value of each shock $Z_t$ is $E[Z_t] = \mu$. Therefore, the expected value of $X_t$ at any time $t$ is:

$$
E[X_t] = E\left[\sum_{i=1}^{t} Z_i\right] = \sum_{i=1}^{t} E[Z_i] = \mu t
$$

This shows that the expected value of a random walk grows linearly with time $t$ if $\mu \neq 0$. When $\mu = 0$, the random walk has no trend, and its expected value remains 0.

#### Variance

The variance $\text{Var}(X_t)$ measures the spread or uncertainty of $X_t$ at time $t$. Since the variance of each shock $Z_t$ is $\sigma^2$, and the shocks are assumed to be independent, the variance of the sum of shocks is the sum of their variances:

$$
\text{Var}(X_t) = \text{Var}\left(\sum_{i=1}^{t} Z_i\right) = \sum_{i=1}^{t} \text{Var}(Z_i) = \sigma^2 t
$$

This means that the variance of a random walk increases linearly with time, implying that the uncertainty around $X_t$ grows as $t$ increases. The longer the random walk progresses, the more dispersed the values become.

### Simulation of a Random Walk in Python

Simulating a random walk in Python is straightforward. We initialize the process at some starting value (typically $X_0 = 0$) and then iteratively generate random shocks $Z_t$ to calculate each successive value $X_t$.

Below is an example of how to simulate and plot a random walk in Python using NumPy and Matplotlib:

```python
import numpy as np
import matplotlib.pyplot as plt

# Number of steps in the random walk
N = 1000

# Generate white noise (Z_t ~ N(0, 1))
Z = np.random.normal(loc=0, scale=1, size=N)

# Initialize the random walk (X_0 = 0)
X = np.cumsum(np.insert(Z, 0, 0))  # Insert X_0 = 0 and compute cumulative sum

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(X, label='Random Walk')
plt.title('Simulation of a Random Walk')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

# Plot the autocorrelation function (ACF)
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(X, lags=50)
plt.show()
```

Explanation:

- `Z` is generated as a sequence of white noise values $Z_t \sim \mathcal{N}(0, 1)$.
- `X` is the cumulative sum of the white noise sequence, representing the random walk.
- We plot the random walk and its autocorrelation function (ACF), which typically shows high autocorrelation due to the cumulative nature of the random walk.

### Removing the Trend with the Difference Operator

A random walk exhibits a **trend** because its expected value $E[X_t]$ changes with time. Specifically, if $\mu \neq 0$, the random walk will exhibit a clear upward or downward trend over time. Even if $\mu = 0$, the random walk still exhibits **non-stationarity** because its variance increases over time.

To make a random walk **stationary**, we can apply the **difference operator** $\Delta$, which removes the trend. The difference operator is defined as:

$$
\Delta X_t = X_t - X_{t-1} = Z_t
$$

Thus, differencing transforms the random walk into a purely random process (white noise) where the differenced series $\Delta X_t$ consists of independent and identically distributed (i.i.d.) random shocks $Z_t$.

In Python, differencing can be done using the `numpy.diff()` function:

```python
# Difference the random walk to remove the trend
diff_X = np.diff(X)

# Plot the differenced time series
plt.figure(figsize=(10, 6))
plt.plot(diff_X, label='Differenced Random Walk')
plt.title('Differenced Time Series (White Noise)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

# Plot the autocorrelation function (ACF) of the differenced series
plot_acf(diff_X, lags=50)
plt.show()
```

After applying the difference operator, the resulting series is stationary, and the ACF shows no significant autocorrelation, indicating that the series is now white noise.

### Correlogram of a Random Walk

The **Autocorrelation Function (ACF)** of a random walk provides important insights into its structure. Since each value in a random walk is highly dependent on its previous value (and indirectly on all past values), the autocorrelation at lower lags tends to be very high. The ACF of a random walk decays slowly, indicating **non-stationarity**. 

Specifically:

- The autocorrelation at lag 1 is typically close to 1.
- The autocorrelation decreases gradually at higher lags but remains significant.

Once we apply the difference operator, the ACF of the differenced series becomes close to zero for all lags, confirming that the differenced series is now **stationary white noise**.
