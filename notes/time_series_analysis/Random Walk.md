## Random Walk Model

#### **2. The Random Walk Model**

The **random walk** is a fundamental time series model, often used to represent stock prices or similar processes. The key idea is that the value at time \( t \), denoted \( X_t \), is the sum of the previous value \( X_{t-1} \) and a random shock or **white noise** \( Z_t \). Mathematically, the model is:

\[
X_t = X_{t-1} + Z_t
\]

Where:
- \( X_t \) is the value at time \( t \) (e.g., the price of a stock today).
- \( X_{t-1} \) is the value at the previous time step (e.g., the stock price yesterday).
- \( Z_t \) is white noise, meaning \( Z_t \sim \mathcal{N}(\mu, \sigma^2) \), a normally distributed random variable with mean \( \mu \) and variance \( \sigma^2 \).

For a random walk starting at \( X_0 = 0 \), we can expand the model over time as:

\[
X_1 = Z_1
\]
\[
X_2 = Z_1 + Z_2
\]
\[
X_3 = Z_1 + Z_2 + Z_3
\]
\[
X_t = \sum_{i=1}^{t} Z_i
\]

#### **3. Mean and Variance of a Random Walk**

Given that \( Z_t \sim \mathcal{N}(\mu, \sigma^2) \), the expected value and variance of \( X_t \) at time \( t \) can be derived as:

- **Expected Value**:
  \[
  E[X_t] = E\left[\sum_{i=1}^{t} Z_i\right] = \sum_{i=1}^{t} E[Z_i] = \mu t
  \]
  Thus, the expected value of the random walk grows linearly with time if \( \mu \neq 0 \).

- **Variance**:
  \[
  \text{Var}(X_t) = \text{Var}\left(\sum_{i=1}^{t} Z_i\right) = \sum_{i=1}^{t} \text{Var}(Z_i) = \sigma^2 t
  \]
  The variance increases linearly with time, implying that the uncertainty around \( X_t \) grows as \( t \) increases.

#### **4. Simulation of a Random Walk**

To simulate a random walk in R (or any other statistical software), we can initialize the process and iteratively generate the random shocks \( Z_t \). The steps are:

1. **Initialize** \( X_1 = 0 \).
2. For each time step \( t \geq 2 \), generate \( Z_t \sim \mathcal{N}(0, 1) \) and compute \( X_t = X_{t-1} + Z_t \).
3. Continue this process for \( t = 2, 3, \dots, 1000 \).

In R, this can be implemented as:

```R
N <- 1000
Z <- rnorm(N, mean = 0, sd = 1)
X <- cumsum(c(0, Z))  # Cumulative sum to generate the random walk
plot(X, type = 'l')   # Plot the random walk
acf(X)                # Plot the autocorrelation function
```

#### **5. Removing the Trend with the Difference Operator**

A random walk exhibits a **trend** because the expected value \( E[X_t] \) changes with time. To remove this trend, we can apply the **difference operator**. The difference operator \( \Delta \) is defined as:

\[
\Delta X_t = X_t - X_{t-1} = Z_t
\]

Thus, differencing transforms the random walk into a **purely random process** (white noise), where the differenced series \( \Delta X_t \) consists of independent and identically distributed (i.i.d.) random shocks \( Z_t \).

In R, the differencing can be done using the `diff()` function:

```R
diff_X <- diff(X)
plot(diff_X, type = 'l')   # Plot the differenced time series
acf(diff_X)                # Plot the ACF of the differenced series
```

This operation removes the trend and converts the random walk into a stationary series with no autocorrelation, as shown by the autocorrelation function (ACF) plot.


#### **6. Correlogram of a Random Walk**

The **Autocorrelation Function (ACF)** of a random walk typically shows high autocorrelation at lower lags because the value at any time \( t \) is highly dependent on the previous values due to the cumulative nature of the process. The ACF decays slowly, indicating that the series is **non-stationary**.

After applying the difference operator, the ACF of the differenced series becomes much closer to zero for all lags, confirming that the differenced series is a **stationary white noise** process.


