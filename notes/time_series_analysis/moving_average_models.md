## Moving Average (MA) Models

Moving Average (MA) models are a fundamental class of univariate time series models used for forecasting and understanding temporal data. Unlike Autoregressive (AR) models, which rely on past values of the series itself, MA models utilize past forecast errors to model the current value of the series. This approach is particularly effective for capturing short-term dependencies and abrupt changes in the data.

### Overview of Moving Average Models

An MA model expresses the current value of the time series as a linear combination of past error terms and a constant mean. This method can be visualized similarly to a low-pass filter in signal processing, where high-frequency noise is smoothed out to reveal the underlying trend.

### Mathematical Definition of MA Models

A **Moving Average model of order $q$**, denoted as **MA($q$)**, is defined by the following equation:

$$Y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \theta_2 \varepsilon_{t-2} + \dots + \theta_q \varepsilon_{t-q}$$

Alternatively, using summation notation:

$$Y_t = \mu + \sum_{i=0}^{q} \theta_i \varepsilon_{t-i}$$

where:

- **$Y_t$**: The observation at time $t$.
- **$\mu$**: The mean of the time series.
- **$\varepsilon_t$**: The error term (white noise) at time $t$, assumed to be independently and identically distributed (i.i.d.) with mean zero and constant variance $\sigma^2$.
- **$\theta_i$**: The parameters of the MA model for lag $i$.
- **$q$**: The order of the MA model, indicating the number of lagged error terms included.

### Examples of MA Models

#### First-Order Moving Average Model (MA(1))

An MA(1) model incorporates the current error term and the immediately preceding error term:

$$Y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1}$$

#### Second-Order Moving Average Model (MA(2))

An MA(2) model includes the current error term and the two most recent error terms:

$$Y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \theta_2 \varepsilon_{t-2}$$

#### General MA($q$) Model

A $q$-th order MA model extends this concept by including $q$ lagged error terms:

$$Y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \theta_2 \varepsilon_{t-2} + \dots + \theta_q \varepsilon_{t-q}$$

### Properties of MA Models

Understanding the theoretical properties of MA models is crucial for effective modeling and forecasting. Below, we outline the key properties, particularly focusing on the MA(1) model as an example.

#### Theoretical Properties of MA(1) Model

For an MA(1) model defined as:

$$Y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1}$$

the following properties hold:

I. **Mean:**

$$\mathbb{E}[Y_t] = \mu$$

II. **Variance:**

$$\text{Var}(Y_t) = \sigma^2 (1 + \theta_1^2)$$

III. **Autocorrelation Function (ACF):**

The ACF measures the correlation between $Y_t$ and $Y_{t-h}$ for different lags $h$.

**Lag 1 ($h = 1$):**

 $$\rho_1 = \frac{\theta_1}{1 + \theta_1^2}$$

**Lags $h \geq 2$:**

 $$\rho_h = 0$$

- The only non-zero autocorrelation occurs at **lag 1**, determined by the parameter $\theta_1$.
- All autocorrelations beyond **lag 1** are zero. This property is a key indicator for identifying the order of an MA model.

#### Autocorrelation Function (ACF) in MA Models

The ACF of an MA($q$) model has non-zero autocorrelations up to lag $q$ and zero autocorrelations beyond that. Specifically:

- **MA(1):** Significant autocorrelation at lag 1; zero for lags $h \geq 2$.
- **MA(2):** Significant autocorrelations at lags 1 and 2; zero for lags $h \geq 3$.
- **General MA($q$)**: Significant autocorrelations up to lag $q$; zero thereafter.

This truncation property of the ACF is instrumental in determining the appropriate order $q$ for an MA model.

### Identifying the Order $q$ of an MA Model

Selecting the correct order $q$ is essential for building an effective MA model. The process involves analyzing the ACF and, in some cases, the Partial Autocorrelation Function (PACF).

#### Step-by-Step Process for Model Selection

I. **Plot the Autocorrelation Function (ACF):**

- Identify the lag beyond which the autocorrelations drop to zero.
- A sharp cutoff in the ACF after lag $q$ suggests an MA($q$) model.

II. **Estimate Models with Varying Orders:**

Fit MA models with different orders $q$ (e.g., MA(1), MA(2), MA(3), etc.).

III. **Compare Model Fits Using Information Criteria:**

**Akaike Information Criterion (AIC):**

$$\text{AIC} = -2 \ln(L) + 2k$$

**Bayesian Information Criterion (BIC):**

$$\text{BIC} = -2 \ln(L) + k \ln(n)$$

where:

- $L$: Maximized value of the likelihood function for the model.
- $k$: Number of estimated parameters.
- $n$: Number of observations.

Lower AIC or BIC values indicate a better balance between model fit and complexity.

IV. **Select the Model with the Lowest AIC/BIC:**
- Choose the MA($q$) model that minimizes the chosen information criterion.

#### Example: Selecting an MA(2) Model

Suppose the ACF plot of a time series shows significant autocorrelations at lags 1 and 2, with autocorrelations near zero for lags $h \geq 3$. This pattern suggests considering an MA(2) model.

After fitting MA models of orders 1, 2, and 3, you obtain the following information criteria:

| Model | AIC  | BIC  |
|-------|------|------|
| MA(1) | 200  | 205  |
| MA(2) | 190  | 195  |
| MA(3) | 192  | 200  |

Both AIC and BIC are minimized at **MA(2)**, indicating that an MA(2) model is the most appropriate choice for the data.

### Example: Moving Average (MA) Model

To illustrate the concepts of Moving Average (MA) models, consider the following example of an MA(1) model.

#### Defining the MA(1) Model

Suppose we have an MA(1) model defined as:

$$Y_t = \mu + w_t + \theta_1 w_{t-1}$$

Where:

- **$Y_t$**: The observation at time $t$.
- **$\mu$**: The mean of the series.
- **$w_t$**: The error term at time $t$, assumed to be independently and identically distributed (i.i.d.) with a normal distribution, $w_t \sim N(0, \sigma^2)$.
- **$\theta_1$**: The parameter of the MA(1) model.
- 
**Given Parameters:**
  
- $\mu = 10$
- $\theta_1 = 0.5$
- $w_t \sim N(0, 1)$ (i.e., $\sigma^2 = 1$)

Thus, the MA(1) model becomes:

$$Y_t = 10 + w_t + 0.5w_{t-1}$$

#### Theoretical Autocorrelation Function (ACF) of MA(1)

The Autocorrelation Function (ACF) for an MA($q$) model has non-zero autocorrelations up to lag $q$ and zero autocorrelations beyond that. Specifically, for an MA(1) model:

I. **Lag 1 ($h = 1$):**

$$\rho_1 = \frac{\theta_1}{1 + \theta_1^2} = \frac{0.5}{1 + (0.5)^2} = \frac{0.5}{1.25} = 0.4$$

II. **Lags $h \geq 2$:**

$$\rho_h = 0 \quad \text{for} \quad h \geq 2$$

Visual Representation:

![MA(1) Model ACF Plot](https://github.com/user-attachments/assets/5ec986c9-db7f-4ab7-b02b-81211009ceca)

- At **Lag 1** the ACF is significantly positive at 0.4.
- At **Lags $h \geq 2$** he ACF values are approximately zero, as expected for an MA(1) process.

**Note:** In practice, sample ACF plots may not perfectly align with theoretical expectations due to randomness and finite sample sizes. However, the characteristic pattern—significant autocorrelation at lag 1 and near-zero autocorrelations at higher lags—serves as a strong indicator for identifying the order of an MA model.

### Simple Moving Average (SMA)

The Simple Moving Average (SMA) is the unweighted mean of the previous `k` data points. It's used to smooth out data series and identify trends over time. The formula for SMA is:

$$
SMA_t = \frac{1}{k} \sum_{i=0}^{k-1} y_{t-i}
$$

- $y_t$ is the observation at time `t`.
- $k$ is the number of periods in the SMA calculation.
- $\text{SMA}_t$ is the SMA value at time `t`.

SMA helps in reducing the noise in the data to see the underlying trend more clearly.

### Exponential Moving Average (EMA)

The Exponential Moving Average (EMA) places a greater weight on more recent data points, making it more responsive to new information. The formula for EMA is:

$$
EMA_{t} = (1 - \alpha) y_t + \alpha \cdot {EMA}_{t-1}
$$

- $y_t$ is the observation at time `t`.
- $\alpha$ is the smoothing factor, a constant between 0 and 1.
- $\text{EMA}_t$ is the EMA value at time `t`.

A higher $\alpha$ places more weight on recent observations, helping in tracking the latest changes more closely.

### Example: Stock Price Analysis

When analyzing stock prices, technical indicators like the Simple Moving Average (SMA) and the Exponential Moving Average (EMA) are frequently employed. These methods help to smooth out price data over a specified period and can be crucial in identifying trends.

#### SMA Analysis
The Simple Moving Average (SMA) is a calculation that takes the arithmetic mean of a given set of prices over a specific number of days in the past; for instance, over the previous 20 days.

$SMA = (P1 + P2 + ... + P20) / 20$$

Here, $P1$, $P2$, ..., $P20$ represent the stock prices for each of the 20 days.

The 20-day SMA helps smooth out short-term fluctuations in stock prices, providing a clearer view of the overall price trend.

#### EMA Analysis
The Exponential Moving Average (EMA) gives more weight to more recent prices. This sensitivity to newer prices makes the EMA more responsive to price changes. Unlike the SMA, the EMA applies a weighting factor to each day's price depending on its recency.

$$EMA = Price(T) * k + EMA(Y) * (1 - k)$$

Where:

- $T$ = Today
- $Y$ = Yesterday
- $k = 2 / (N + 1)$
- $N$ = The number of days in the EMA (e.g., 20 days)
  
The EMA is valuable for capturing more recent trends and is often used for shorter time frames.

#### Trend Identification

- **Crossing**: When the EMA crosses the SMA, it may indicate a shift in trend. An upward crossing can signal a bullish trend, while a downward crossing might signal a bearish trend.
- **Divergence**: If the EMA diverges significantly from the SMA, it suggests increased market momentum in the direction of the EMA.
- Investors often use these indicators in conjunction to get a more nuanced understanding of the market sentiment.
- It's important to remember that SMA and EMA are based on past prices and are not predictive of future prices but rather indicative of trends.

![stock_price_analysis](https://github.com/djeada/Statistics-Notes/assets/37275728/69a7a991-b80c-406b-b0c9-129953f80e3f)

- The blue line represents the mock stock prices, exhibiting a more dynamic and volatile behavior, similar to real-world stock market trends.
- The orange line is the 20-day Simple Moving Average (SMA). It smooths out the fluctuations in the stock prices, providing a clearer view of the long-term trend.
- The green line shows the 20-day Exponential Moving Average (EMA), which reacts more quickly to recent price changes, thus capturing short-term movements more effectively.
