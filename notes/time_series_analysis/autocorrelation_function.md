## Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF)

In time series analysis, understanding the relationships between observations at different time lags is crucial for model identification and forecasting. Two essential tools for analyzing these relationships are the **Autocorrelation Function (ACF)** and the **Partial Autocorrelation Function (PACF)**.

- The **ACF** measures the correlation between observations at different time lags.
- The **PACF** isolates the direct effect of a specific lag by removing the influence of intermediate lags.

### Autocorrelation Function (ACF)

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

#### Plotting the ACF

The **Autocorrelation Function (ACF) plot**, or **Correlogram**, is a useful tool for understanding the structure of time series data. In Python, you can generate and interpret the ACF plot using libraries like `statsmodels` and `matplotlib`. The ACF plot helps identify significant correlations at different lags and reveals patterns in the data.

e ACF plot can provide answers to the following questions:

    Is the observed time series white noise / random?
    Is an observation related to an adjacent observation, an observation twice-removed, and so on?
    Can the observed time series be modeled with an MA model? If yes, what is the order?

Key Points for Interpreting the ACF Plot

1. If the ACF values decrease slowly over many lags, this suggests the presence of a **trend** in the data.
2. Repeated peaks or cyclic behavior in the ACF plot indicate **seasonal patterns** in the data, with regular intervals of high correlation.
3. A rapid drop-off or sharp cutoff after a few lags suggests the data may follow a **Moving Average (MA)** process, where the current value is explained by a few prior error terms (shocks).

#### Python Example

Below is a Python example where we generate and plot the ACF for three different types of time series: one with a trend, one with seasonal patterns, and one following a moving average process.

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# code for simulating time series with trend and seasonality
np.random.seed(42)
N = 1000

# Example 1: Time Series with a stronger trend (Random Walk)
trend_series = np.cumsum(np.random.normal(1, 1, N))  # Random walk simulating a trend with positive drift

# Example 2: Time Series with clearer seasonality (less noise)
seasonal_series = np.sin(np.linspace(0, 20 * np.pi, N))  # A sine wave to emphasize seasonality

# Moving Average Process (MA(1)) remains the same
ma_series = np.random.normal(0, 1, N)
for i in range(1, N):
    ma_series[i] += 0.5 * ma_series[i - 1]  # Moving average with lag 1

# Plotting the time series
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(trend_series, label="Time Series with Trend")
plt.title('Time Series with Trend')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(seasonal_series, label="Time Series with Seasonality")
plt.title('Time Series with Seasonality')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(ma_series, label="Moving Average (MA(1)) Process")
plt.title('Moving Average (MA(1)) Process')
plt.grid(True)

plt.tight_layout()
plt.show()

# Plotting ACF for each time series
plt.figure(figsize=(12, 8))

# ACF for the time series with trend
plt.subplot(3, 1, 1)
plot_acf(trend_series, lags=50, ax=plt.gca())
plt.title('ACF of Time Series with Trend')

# ACF for the time series with seasonality
plt.subplot(3, 1, 2)
plot_acf(seasonal_series, lags=50, ax=plt.gca())
plt.title('ACF of Time Series with Seasonality')

# ACF for the MA(1) process
plt.subplot(3, 1, 3)
plot_acf(ma_series, lags=50, ax=plt.gca())
plt.title('ACF of Moving Average (MA(1)) Process')

plt.tight_layout()
plt.show()
```

Time Series Data:

![output(1)](https://github.com/user-attachments/assets/9358ee1c-9b09-4df8-8434-1835868b38f3)

Acf plots:

![output(2)](https://github.com/user-attachments/assets/ce26bcd4-bbcc-4334-a8cc-b1c52d54b548)

Interpreting the ACF Plot:

- **Slow Decay** in the first plot indicates that the time series has a **trend** and is non-stationary.
- **Regular Peaks** in the second plot highlight **seasonal patterns** in the data, repeating at consistent intervals.
- **Sharp Cutoff** in the third plot suggests that the data is generated from an **MA(1)** process, where values depend only on recent observations.

### Partial Autocorrelation Function (PACF)

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

The **Partial Autocorrelation Function (PACF) plot** is a valuable tool for understanding the relationship between a time series and its lagged values after accounting for the influence of intervening lags. Unlike the ACF, which shows the correlation between the series and its lagged values, the PACF removes the effect of any intermediate lags.

The PACF is particularly useful for identifying the order of an **Autoregressive (AR) process**. If you suspect your time series follows an AR model, the PACF plot can help you determine the number of lag terms to include in your model.

he PACF plot can provide answers to the following questions:

    Can the observed time series be modeled with an AR model? If yes, what is the order?

Key Points for Interpreting the PACF Plot:

1. Significant spikes at early lags indicate that those specific lags are important for modeling the time series. For an **AR(p)** process, you will see significant spikes up to lag \( p \), and the PACF will then cut off.
2. A sharp drop after lag \( p \) suggests that the time series follows an **AR(p)** process, meaning that only \( p \) past observations are needed to model the series.
3. If the PACF plot exhibits a gradual decay, this indicates the presence of a **Moving Average (MA) process**, since partial correlations decrease slowly over many lags.

#### Python Example

In this example, we will simulate different time series data (AR, MA, and ARMA processes) and plot their PACF to see how they behave.

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.graphics.tsaplots import plot_pacf

# Example 1: Simulating an AR(2) process
np.random.seed(42)
ar2 = np.array([1, -0.75, 0.25])  # AR(2) coefficients (X_t = 0.75*X_t-1 - 0.25*X_t-2 + noise)
ma0 = np.array([1])  # No MA component
AR_process = ArmaProcess(ar2, ma0)
ar_series = AR_process.generate_sample(nsample=1000)

# Example 2: Simulating a Moving Average (MA) process
ma1 = np.array([1, 0.5])  # MA(1) coefficients
MA_process = ArmaProcess([1], ma1)
ma_series = MA_process.generate_sample(nsample=1000)

# Example 3: Simulating an ARMA(1,1) process
ar1 = np.array([1, 0.5])  # AR(1) coefficients
ma1 = np.array([1, -0.5])  # MA(1) coefficients
ARMA_process = ArmaProcess(ar1, ma1)
arma_series = ARMA_process.generate_sample(nsample=1000)

# Plotting the time series
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(ar_series, label="AR(2) Process")
plt.title('AR(2) Process')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(ma_series, label="MA(1) Process")
plt.title('MA(1) Process')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(arma_series, label="ARMA(1,1) Process")
plt.title('ARMA(1,1) Process')
plt.grid(True)

plt.tight_layout()
plt.show()

# Plotting PACF for each time series
plt.figure(figsize=(12, 8))

# PACF for the AR(2) process
plt.subplot(3, 1, 1)
plot_pacf(ar_series, lags=30, ax=plt.gca())
plt.title('PACF of AR(2) Process')

# PACF for the MA(1) process
plt.subplot(3, 1, 2)
plot_pacf(ma_series, lags=30, ax=plt.gca())
plt.title('PACF of MA(1) Process')

# PACF for the ARMA(1,1) process
plt.subplot(3, 1, 3)
plot_pacf(arma_series, lags=30, ax=plt.gca())
plt.title('PACF of ARMA(1,1) Process')

plt.tight_layout()
plt.show()
```

Time Series Data:

![Screenshot from 2024-09-09 20-32-19](https://github.com/user-attachments/assets/50ddf1a6-fcae-49fa-92e0-ea0f133f0265)

Pacf plots:

![Screenshot from 2024-09-09 20-35-34](https://github.com/user-attachments/assets/59a1ff40-5b4f-4351-bfaf-63b0e6950947)

Interpreting the PACF Plot:

- In the AR(2) process, the PACF will show significant spikes at lags 1 and 2, followed by a sharp drop. This sharp cutoff indicates an autoregressive model of order 2.
- In the MA(1) process, the PACF will display a gradual decay, characteristic of a moving average process, where the partial correlations decrease slowly over time.
- For the ARMA(1,1) process, the PACF plot may show significant spikes at early lags, reflecting the autoregressive part, followed by a slower decay, reflecting the moving average component.

### Comparing ACF and PACF

- The **ACF** measures the correlation between the time series and its lagged values, capturing both direct and indirect effects (i.e., effects from intermediate lags).
- The **PACF** removes the influence of the intermediate lags, isolating the direct effect of each lag on the time series.

In practice:

- The **ACF** of an AR(p) process decays gradually, but the **PACF** cuts off after lag $p$.
- The **ACF** of an MA(q) process cuts off after lag $q$, while the **PACF** decays gradually.

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

The following is using mock data for time series with **short-term dependencies**, specifically one that could be modeled as an **AR(1) process**. Common data types that show this behavior include **financial data** (such as stock prices or returns), **economic indicators**, or **meteorological data** (like temperature series).

![c20f0056-8024-4e6d-a91b-3202c158da64](https://github.com/djeada/Statistics-Notes/assets/37275728/1154a4f5-6105-452a-a5fa-30399f43094b)

#### Left Plot: Autocorrelation Function (ACF)

- The ACF plot starts at 1 for lag 0, which is expected because the series is perfectly correlated with itself at lag 0.
- The ACF **decays gradually** but remains positive for a number of lags (up to lag ~20), which is typical of an **autoregressive (AR)** process, specifically an **AR(1)** or **AR(2)** model. In an AR process, past values have a direct influence on future values, leading to a slow decay in autocorrelation.
- The shaded area represents the **confidence intervals**. If any spikes go outside these bounds, it indicates significant autocorrelation at those lags. In this case, we see that most lags within the confidence bounds are not statistically significant, but the gradual decay suggests a trend.

#### Right Plot: Partial Autocorrelation Function (PACF)

- The PACF plot shows a **sharp cutoff** after lag 1. This is characteristic of an **AR(1) process**, where only the first lag has a significant direct effect on the current value, and the influence of higher-order lags is negligible once the first lag's effect is accounted for.
- The significant spike at lag 1 suggests that this time series can be modeled as an **autoregressive process of order 1 (AR(1))**.

### Auto-Regressive (AR) and Moving Average (MA) Models with ACF and PACF

In time series analysis, **Auto-Regressive (AR)** and **Moving Average (MA)** models are widely used for modeling and forecasting. Identifying the correct order of these models relies on interpreting the **Autocorrelation Function (ACF)** and the **Partial Autocorrelation Function (PACF)**.

#### **Auto-Regressive (AR) Model**
The AR model assumes that the current value of a time series (\(y_t\)) is a linear combination of its past values:

\[
\hat{y_t} = \alpha_1 y_{t-1} + \alpha_2 y_{t-2} + \dots + \alpha_p y_{t-p}
\]

- **Key Assumption:** The present value depends on its own prior values (\(y_{t-1}, y_{t-2}, \dots, y_{t-p}\)).
- **ACF and PACF Interpretation:**
  - **PACF:** Helps determine the order (\(p\)) of the AR model. The PACF will show significant spikes up to lag \(p\), after which it drops off.
  - **ACF:** May decay gradually, showing a tail-off pattern, which is less helpful for directly identifying \(p\).


#### **Moving Average (MA) Model**
The MA model assumes that the current value (\(y_t\)) is influenced by past error terms (\(\epsilon_t\)):

\[
\hat{y_t} = \epsilon_t + \beta_1 \epsilon_{t-1} + \beta_2 \epsilon_{t-2} + \dots + \beta_q \epsilon_{t-q}
\]

- **Key Assumption:** The present value is driven by current and past random shocks (\(\epsilon_t, \epsilon_{t-1}, \dots, \epsilon_{t-q}\)).
- **ACF and PACF Interpretation:**
  - **ACF:** Helps determine the order (\(q\)) of the MA model. The ACF will show significant spikes up to lag \(q\), after which it drops off.
  - **PACF:** Typically decreases gradually and does not provide a clear cutoff for \(q\).

