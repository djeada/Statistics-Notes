## Stationarity in Time Series

Stationarity is an important idea in time series analysis. A time series is considered stationary if its statistical properties—like the mean, variance, and autocovariance—stay constant over time. This matters because methods like ARIMA and ARMA are designed to work with stationary data, so it’s a good idea to check for stationarity before using these models.

Stationarity can be classified into two types:

1. Strict stationarity implies that the **entire distribution of the process remains the same over time**.  
2. Weak stationarity, also known as second-order stationarity, requires only that the **mean, variance, and autocovariance remain time-invariant** over time.  

### Why Do We Care About Stationarity?

Imagine we are analyzing synthetic stock prices that exhibit both an upward trend and random fluctuations over time. Suppose our goal is to study the seasonal variations in these stock prices throughout the year. However, the data we have spans several years, during which the stock prices have been steadily increasing. This steady increase introduces non-stationarity, complicating our analysis of seasonal patterns.

**Addressing Non-Stationarity: Detrending the Data**

To effectively analyze the seasonal component, we first need to remove the non-stationary trend. This can be accomplished by fitting a linear model to the data using least squares regression:

$$\text{Stock Price} = b \times \text{Time} + z$$

Where:

- $b$ is the slope representing the trend over time.
- $z$ is the intercept.

By subtracting this linear trend from the original stock price data, we obtain "detrended" stock prices. This process isolates the seasonal fluctuations by eliminating the underlying upward trend.

**Visualization**

![Synthetic Stock Prices Analysis](https://github.com/user-attachments/assets/db1f2c1c-f1ce-4aa8-b3e0-34d821a4a001)

- Top panel displays the synthetic stock prices over time with a fitted linear trend (red dashed line) using least squares regression. This trend captures the overall upward movement in stock prices.
- Bottom panel shows the detrended stock prices (residuals), highlighting the seasonal variations after removing the linear trend. These residuals are more suitable for analyzing periodic patterns without the confounding effect of the trend.

### Intuition for Stationary Time Series

A **stationary time series** behaves similarly over time, meaning:

- The mean of the series shows **no trend** and does not systematically change over time.
- The variability around the mean has a **constant variance**, remaining stable throughout.
- There are **no periodic fluctuations** such as seasonality or cyclic behavior, unless explicitly modeled.

This means that the statistical properties of one segment of the series are similar to those of any other segment, allowing us to predict future behavior based on past data.

### Strict Stationarity

A process is said to be **strictly stationary** if the joint distribution of any subset of observations $X_{t_1}, X_{t_2}, \dots, X_{t_k}$ is the same as the distribution of $X_{t_1 + \tau}, X_{t_2 + \tau}, \dots, X_{t_k + \tau}$ for all $\tau$. 

In simple terms, the process looks the same no matter how we shift it in time. Strict stationarity implies that:

- The distribution of $X_t$ does not change over time.
- All moments of the distribution (mean, variance, higher moments) are constant over time.

### Weak (Second-Order) Stationarity

Weak stationarity, also known as **second-order stationarity**, requires only that the **first two moments** (mean and variance) and the **autocovariance** depend solely on the lag between observations, not on time itself.

A time series $\{X_t\}$ is weakly stationary if:

1. The **mean** of the series is constant: $E[X_t] = \mu$ for all $t$.
2. The **variance** is constant: $\text{Var}(X_t) = \sigma^2$ for all $t$.
3. The **autocovariance** between $X_t$ and $X_{t+k}$ depends only on the lag $k$, not on $t$:

$$
\text{Cov}(X_t, X_{t+k}) = \gamma(k)
$$

Weak stationarity is often sufficient for most time series models, as it focuses on ensuring that the mean and variance remain stable over time, making the process easier to model and analyze.

### Properties of Stationary Processes

#### Mean, Variance, and Autocovariance Functions

To analyze a stationary process, we focus on three key functions:

- The **mean function** $\mu(t) = E[X_t]$ represents the expected value of the process at time $t$, and for a stationary process, this should remain constant.
- The **variance function** $\sigma^2(t) = \text{Var}(X_t)$ gives the variance at time $t$, which must also be constant for stationarity.
- The **autocovariance function** $\gamma(k) = \text{Cov}(X_t, X_{t+k})$ measures how the process correlates with itself at different time lags $k$, and for a stationary process, it depends only on the lag $k$, not on time $t$.

#### Autocorrelation and Bounds

For a weakly stationary process, the **autocorrelation function** $\rho(k)$, which measures the correlation between two points in the series separated by lag $k$, is bounded by -1 and 1:

$$
-1 \leq \rho(k) \leq 1
$$

This bound can be derived from basic linear algebra principles that apply to correlations between random variables.

### Examples of Stationary Processes

#### **White Noise**

White noise is the simplest example of a stationary process. It is defined as a sequence of uncorrelated, identically distributed random variables:

$$
X_t \sim \mathcal{N}(0, \sigma^2)
$$

Properties of white noise:

- The **mean** is constant: $E[X_t] = 0$.
- The **variance** is constant: $\text{Var}(X_t) = \sigma^2$.
- The **autocovariance** function is:
  
$$
\gamma(k) = 
\begin{cases}
\sigma^2 & \text{if } k = 0 \\
0 & \text{if } k \neq 0
\end{cases}
$$

- The **autocorrelation** function is:

$$
\rho(k) = 
\begin{cases}
1 & \text{if } k = 0 \\
0 & \text{if } k \neq 0
\end{cases}
$$

Below is a plot of synthetically generated white noise:

![white_noise](https://github.com/user-attachments/assets/a24cc561-f34a-431e-bac0-2f9cd5e62a49)

Thus, white noise is a stationary process because its mean and variance are constant, and its autocovariance depends only on the lag.

#### Moving Average (MA) Process

A **moving average (MA) process** of order $q$, denoted as MA(q), is another example of a weakly stationary process. It is defined as:

$$
X_t = \beta_0 Z_t + \beta_1 Z_{t-1} + \dots + \beta_q Z_{t-q}
$$

where $Z_t \sim \mathcal{N}(0, \sigma_Z^2)$ are independent white noise terms.

For an MA(q) process:

- The **mean** is zero: $E[X_t] = 0$.
- The **variance** is constant:

$$
\text{Var}(X_t) = \sigma_Z^2 \sum_{i=0}^{q} \beta_i^2
$$

- The **autocovariance** function $\gamma(k)$ depends on the lag $k$:

$$
\gamma(k) = 
\begin{cases}
\sigma_Z^2 \sum_{i=0}^{q-k} \beta_i \beta_{i+k} & \text{if } k \leq q \\
0 & \text{if } k > q
\end{cases}
$$
  
The autocorrelation function $\rho(k)$ is obtained by normalizing the autocovariance by the variance:

$$
\rho(k) = \frac{\gamma(k)}{\gamma(0)}
$$

Below is a plot of the Moving Average (MA) process of order $q=2$:

![moving_average](https://github.com/user-attachments/assets/28e1d7fa-243b-4841-afba-afd2188ac400)

The MA(q) process is weakly stationary because its mean and variance are constant, and the autocovariance depends only on the lag.

### Non-Stationary Processes

#### Random Walk

A **random walk** is an example of a non-stationary process. A random walk can be written as:

$$
X_t = X_{t-1} + Z_t
$$

where $Z_t$ is white noise.

For a random walk:

The **mean** grows over time:

$$
E[X_t] = t \cdot \mu
$$

The **variance** increases with time:

$$
\text{Var}(X_t) = t \cdot \sigma^2
$$

Since the variance and mean depend on time, the random walk is **not stationary**. However, applying a **difference operator** can transform a random walk into a stationary series.

#### Differencing to Remove Non-Stationarity

To handle non-stationary processes like random walks, we can apply the **difference operator** $\Delta$, which removes trends and transforms the process into a stationary one.

The difference operator is defined as:

$$
\Delta X_t = X_t - X_{t-1} = Z_t
$$

By differencing the series, we convert a random walk into white noise, which is stationary. This technique is essential for models like ARIMA that require the data to be stationary before modeling.

### Dealing with Non-Stationary Time Series

In real-world applications, many time series are non-stationary. To apply statistical models that require stationarity, we often use **transformations** such as:

- Applying **differencing** helps remove trends and makes the series stationary.  
- Using **logarithmic transformations** can stabilize the variance in the series.  
- The process of **detrending** removes long-term trends, allowing a focus on short-term fluctuations.

#### Example of Differencing in Python

We can use Python to difference a non-stationary series like a random walk:

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulate a random walk
np.random.seed(42)
N = 1000
Z = np.random.normal(0, 1, N)
X = np.cumsum(Z)  #

 Random walk as cumulative sum of white noise

# Apply differencing to make it stationary
diff_X = np.diff(X)

# Plot the original random walk and the differenced series
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(X, label='Random Walk')
plt.title('Random Walk (Non-Stationary)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(diff_X, label='Differenced Series')
plt.title('Differenced Series (Stationary)')
plt.grid(True)

plt.tight_layout()
plt.show()
```

I. Simulating a Random Walk:

- A random walk is generated by taking the cumulative sum of normally distributed random numbers. This produces a series where each value depends on the previous one plus some random noise.
- The random walk is non-stationary because it lacks a constant mean and variance over time—it drifts unpredictably.

II. Differencing:

- Differencing transforms the non-stationary series into a stationary one by subtracting the previous observation from the current one. This removes any trend or long-term structure in the data.
- In Python, this is done using `np.diff()`, which takes the difference between consecutive elements of the series.

The result plot would look like the following:

![differenced_random_walk](https://github.com/user-attachments/assets/2cebba56-7d3b-470c-9511-56d617be7159)

In this plot, the upper section shows the random walk (non-stationary), while the lower section shows the differenced series (stationary). Differencing removes the trend from the original series, making it easier to model and predict future values.
