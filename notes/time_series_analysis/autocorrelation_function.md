## Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF)

In time series analysis, understanding the relationships between observations at different time lags is crucial for model identification and forecasting. Two essential tools for analyzing these relationships are the **Autocorrelation Function (ACF)** and the **Partial Autocorrelation Function (PACF)**.

- The **ACF** measures the correlation between observations at different time lags.
- The **PACF** isolates the direct effect of a specific lag by removing the influence of intermediate lags.

### Autocorrelation Function (ACF)

#### Definition of the ACF

The **Autocorrelation Function (ACF)** measures the correlation between a time series and its lagged values. It helps detect patterns such as trends and seasonality. The autocorrelation at lag $k$, denoted $\rho_k$, is defined as:

$$
\rho_k = \frac{\gamma_k}{\gamma_0}
$$

Where:

- $\gamma_k$ is the autocovariance at lag $k$.
- $\gamma_0$ is the variance of the time series (autocovariance at lag 0).

#### Autocovariance Function

The **autocovariance** at lag $k$ is the covariance between observations separated by $k$ time periods. It is given by:

$$
\gamma_k = \text{Cov}(X_t, X_{t+k}) = \mathbb{E}[(X_t - \mu)(X_{t+k} - \mu)]
$$

Where:

- $\mu$ is the mean of the time series.
- $\mathbb{E}$ denotes the expectation operator.

#### Autocorrelation Coefficient

The **autocorrelation coefficient** at lag $k$ normalizes the autocovariance $\gamma_k$ by dividing it by the variance $\gamma_0$. It is a dimensionless quantity that ranges between -1 and 1, making it easier to interpret:

$$
\rho_k = \frac{\gamma_k}{\gamma_0} = \frac{\mathbb{E}[(X_t - \mu)(X_{t+k} - \mu)]}{\mathbb{E}[(X_t - \mu)^2]}
$$

#### Sample Autocorrelation Function

In practice, the ACF is estimated from the data using sample autocorrelations. The **sample autocorrelation coefficient** $r_k$ at lag $k$ is calculated as:

$$
r_k = \frac{\sum_{t=1}^{N-k} (x_t - \bar{x})(x_{t+k} - \bar{x})}{\sum_{t=1}^{N} (x_t - \bar{x})^2}
$$

Where:

- $\bar{x}$ is the sample mean of the series.
- $N$ is the number of observations.
- $x_t$ is the observed value at time $t$.

#### Plotting the ACF: Correlogram

The **ACF plot** (or **Correlogram**) is a graphical tool used to visualize the autocorrelation coefficients for different lags. This helps to identify significant correlations at specific lags. The plot shows $r_k$ for different values of $k$, starting at $r_0 = 1$ because the autocorrelation at lag 0 is always 1 (since the series is perfectly correlated with itself).

#### Interpreting the ACF Plot

- **Slow decay** in the ACF indicates a trend in the data.
- **Seasonal patterns** can be identified by repeated peaks at regular intervals in the ACF.
- A **sharp cutoff** after a few lags suggests a **Moving Average (MA) process**.

---

### Partial Autocorrelation Function (PACF)

#### Definition of the PACF

The **Partial Autocorrelation Function (PACF)** measures the correlation between the time series and its lagged values, after removing the linear effects of the intermediate lags. It helps isolate the direct impact of each lag.

The PACF at lag $k$, denoted by $\phi_{kk}$, represents the correlation between $X_t$ and $X_{t+k}$, after accounting for the effect of $X_{t+1}, X_{t+2}, \dots, X_{t+k-1}$.

#### Yule-Walker Equations

The **Yule-Walker equations** for an autoregressive (AR) process provide a recursive way to compute the PACF for different lags. For an AR(p) process:

$$
\gamma_k = \sum_{j=1}^{p} \phi_{pj} \gamma_{k-j}
$$

Where $\phi_{pj}$ are the partial autocorrelation coefficients, and $\gamma_k$ is the autocovariance at lag $k$.

#### Recursive Calculation of PACF

The PACF at lag $k$ can be recursively calculated as:

I. $\phi_{11} = \rho_1$

II. For $k \geq 2$:

$$
\phi_{kk} = \frac{\rho_k - \sum_{j=1}^{k-1} \phi_{k-1,j} \rho_{k-j}}{1 - \sum_{j=1}^{k-1} \phi_{k-1,j} \rho_j}
$$

III. The intermediate coefficients $\phi_{kj}$ (for $j < k$) are updated using:

$$
\phi_{kj} = \phi_{k-1,j} - \phi_{kk} \phi_{k-1,k-j}
$$

#### Plotting the PACF

The PACF plot shows the partial autocorrelation at various lags. The interpretation of the PACF plot is particularly useful for identifying the **order of an AR process**.

#### Interpreting the PACF Plot

- **Significant spikes** at early lags indicate that those lags contribute to the model. For example, in an **AR(p) process**, the PACF typically shows significant spikes up to lag $p$, and then cuts off.
- **Sharp cutoff after lag $p$** suggests an autoregressive process of order $p$.
- **Gradual decay** in the PACF suggests a **Moving Average (MA) process**.

---

### Comparing ACF and PACF

- The **ACF** measures the correlation between the time series and its lagged values, capturing both direct and indirect effects (i.e., effects from intermediate lags).
- The **PACF** removes the influence of the intermediate lags, isolating the direct effect of each lag on the time series.

In practice:
- The **ACF** of an AR(p) process decays gradually, but the **PACF** cuts off after lag $p$.
- The **ACF** of an MA(q) process cuts off after lag $q$, while the **PACF** decays gradually.

---

### Example: ACF and PACF for AR(1) Process

Consider the autoregressive process of order 1, denoted AR(1):

$$
X_t = \phi X_{t-1} + \epsilon_t
$$

Where $\epsilon_t$ is white noise.

#### ACF for AR(1)

The autocorrelation function for an AR(1) process is:

$$
\rho_k = \phi^k
$$

This implies that the autocorrelation decays exponentially with increasing lag $k$, showing a **gradual decay** in the ACF plot.

#### PACF for AR(1)

The partial autocorrelation function for an AR(1) process shows a **significant spike at lag 1**, followed by zeros at higher lags. This is because, for an AR(1) process, only the first lag has a direct effect, while higher lags are indirectly related to the series.

### Visualization of ACF and PACF

The following is using mock data for time series with **short-term dependencies**, specifically one that could be modeled as an **AR(1) process**.  Common data types that show this behavior include **financial data** (such as stock prices or returns), **economic indicators**, or **meteorological data** (like temperature series).

![c20f0056-8024-4e6d-a91b-3202c158da64](https://github.com/djeada/Statistics-Notes/assets/37275728/1154a4f5-6105-452a-a5fa-30399f43094b)

#### Left Plot: Autocorrelation Function (ACF)

- The ACF plot starts at 1 for lag 0, which is expected because the series is perfectly correlated with itself at lag 0.
- The ACF **decays gradually** but remains positive for a number of lags (up to lag ~20), which is typical of an **autoregressive (AR)** process, specifically an **AR(1)** or **AR(2)** model. In an AR process, past values have a direct influence on future values, leading to a slow decay in autocorrelation.
- The shaded area represents the **confidence intervals**. If any spikes go outside these bounds, it indicates significant autocorrelation at those lags. In this case, we see that most lags within the confidence bounds are not statistically significant, but the gradual decay suggests a trend.

#### Right Plot: Partial Autocorrelation Function (PACF)

- The PACF plot shows a **sharp cutoff** after lag 1. This is characteristic of an **AR(1) process**, where only the first lag has a significant direct effect on the current value, and the influence of higher-order lags is negligible once the first lag's effect is accounted for.
- The significant spike at lag 1 suggests that this time series can be modeled as an **autoregressive process of order 1 (AR(1))**.
