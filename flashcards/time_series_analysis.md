# Quizzes on Time Series Analysis

This series of quizzes covers essential topics in time series analysis, including:

- **Time Series Components**: Test your understanding of trends, seasonality, and noise in time series data.
- **Stationarity**: Learn about stationary and non-stationary series, and how to use tests like the Augmented Dickey-Fuller (ADF) test.
- **Autocorrelation and Partial Autocorrelation**: Explore how past values influence future values, and how to use ACF and PACF plots.
- **Moving Averages**: Assess your knowledge of simple, weighted, and exponential moving averages, and how they smooth time series data.
- **ARIMA Models**: Understand autoregressive, integrated, and moving average components in ARIMA models and how to fit them to time series data.
- **Seasonal Decomposition**: Learn about seasonal decomposition of time series, using techniques like STL to break down series into trend, seasonality, and residuals.
- **Forecasting**: Test your ability to forecast future values using various models, including exponential smoothing, ARIMA, and seasonal ARIMA (SARIMA).
- **Evaluation Metrics**: Assess your understanding of how to evaluate the accuracy of time series models using metrics like Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE).

## Time Series Components

<details>
<summary>What are the main components of a time series?</summary>

A time series is commonly decomposed into three components:

1. **Trend (or trend-cycle)**: the long-term movement of the level (upward, downward or flat), sometimes including slower non-periodic cycles.
2. **Seasonality**: patterns that repeat with a fixed, known period, such as every 12 months or every 7 days.
3. **Remainder (noise)**: irregular fluctuations not explained by the trend or seasonality.

They can combine additively ($y_t = T_t + S_t + R_t$) or multiplicatively ($y_t = T_t \times S_t \times R_t$).

</details>

<details>
<summary>What is an example of seasonality in time series data?</summary>

Retail sales that peak every December because of holiday shopping are a classic example. The pattern repeats every 12 months, so the seasonal period is $m = 12$ for monthly data. Other examples are higher electricity demand every summer afternoon and weekly cycles in website traffic.

</details>

<details>
<summary>How can a trend affect a time series?</summary>

A **trend** is a persistent long-term change in the level of the series. It can be upward, downward, or absent (a flat level). Because a trend makes the mean change over time, the series is non-stationary. The trend usually has to be removed, by differencing or detrending, or modelled explicitly before fitting a stationary model such as ARMA.

</details>

## Stationarity

<details>
<summary>What is a stationary time series?</summary>

A (weakly) **stationary** time series has a constant mean, a constant variance, and an autocovariance $\text{Cov}(X_t, X_{t+h})$ that depends only on the lag $h$, not on time $t$. Series with trends, seasonality or unit roots are not stationary. ARMA models assume stationarity, while ARIMA handles some non-stationarity by differencing first.

</details>

<details>
<summary>How do you test for stationarity?</summary>

- The **augmented Dickey–Fuller (ADF) test** has the null hypothesis of a unit root (non-stationarity). A p-value below $\alpha$ (e.g. 0.05) rejects it, which is evidence of stationarity.
- The **KPSS test** reverses the roles: its null hypothesis is stationarity.

Using both tests together, along with time plots and the ACF, gives a more reliable picture than either test alone.

</details>

<details>
<summary>How do you make a time series stationary?</summary>

Common ways to make a time series stationary are:

1. **Differencing**: replace $y_t$ with $y_t - y_{t-1}$ to remove a stochastic trend or unit root.
2. **Detrending**: subtract a fitted deterministic trend.
3. **Log or Box–Cox transformation**: stabilise a variance that grows with the level of the series.
4. **Seasonal differencing**: replace $y_t$ with $y_t - y_{t-m}$ to remove a stable seasonal pattern of period $m$.

</details>

## Autocorrelation and Partial Autocorrelation

<details>
<summary>What is autocorrelation?</summary>

**Autocorrelation** is the correlation between a time series and a lagged copy of itself:

$$\rho(h) = \frac{\gamma(h)}{\gamma(0)}$$

where $\gamma(h)$ is the autocovariance at lag $h$. Positive autocorrelation means high values tend to follow high values. Negative autocorrelation means high values tend to follow low values, and vice versa.

</details>

<details>
<summary>What is a partial autocorrelation function (PACF)?</summary>

The **partial autocorrelation** at lag $k$ is the correlation between $X_t$ and $X_{t-k}$ after removing the linear effect of the intermediate values $X_{t-1}, \dots, X_{t-k+1}$. For an AR(p) process the PACF cuts off after lag $p$, so it helps choose the number of autoregressive terms.

</details>

<details>
<summary>What are ACF and PACF plots used for?</summary>

**ACF plots** show the sample autocorrelation at each lag, and **PACF plots** show the partial autocorrelation at each lag, usually with approximate significance bounds $\pm 1.96/\sqrt{n}$. They help identify ARMA orders:

- **AR(p)**: the ACF tails off and the PACF cuts off after lag $p$.
- **MA(q)**: the ACF cuts off after lag $q$ and the PACF tails off.
- **ARMA**: both tail off.

They are also used to check that residuals look like white noise.

</details>

## Moving Averages

<details>
<summary>What is a simple moving average?</summary>

A **simple moving average (SMA)** is the unweighted mean of the most recent $n$ observations. Sliding it along the series smooths short-term fluctuations, which makes trends easier to see:

$$\text{SMA}_t = \frac{1}{n} \sum_{i=t-n+1}^{t} X_i$$

where $n$ is the window size. This smoothing tool is different from an MA(q) model, which is built from past innovations.

</details>

<details>
<summary>What is an exponential moving average (EMA)?</summary>

An **exponential moving average** weights recent observations more heavily than older ones, so it reacts faster to changes than an SMA. It is computed recursively with a smoothing factor $0 < \alpha \le 1$:

$$\text{EMA}_t = \alpha X_t + (1 - \alpha)\,\text{EMA}_{t-1}$$

The weight on $X_{t-j}$ is $\alpha(1 - \alpha)^j$, so it decays exponentially with age.

</details>

<details>
<summary>How are moving averages used in time series forecasting?</summary>

**Moving averages** are used mainly to smooth noise so the trend and seasonality are easier to see. They are also used to estimate the trend in classical decomposition, for example with a centred 12-month moving average. As a simple forecast, the latest moving average can be used as the next value, which works only for series without a strong trend or seasonality.

</details>

## ARIMA Models

<details>
<summary>What does ARIMA stand for?</summary>

**ARIMA** stands for **AutoRegressive Integrated Moving Average**:

1. **AR (autoregressive)**: the current value depends linearly on past values.
2. **I (integrated)**: the series is differenced to make it stationary.
3. **MA (moving average)**: the current value depends on past forecast errors (innovations).

Plain ARIMA is used for non-seasonal series. SARIMA adds seasonal terms.

</details>

<details>
<summary>What are the parameters of an ARIMA model?</summary>

An ARIMA(p, d, q) model has three orders:

1. **p**: the number of autoregressive (AR) terms.
2. **d**: the number of differences needed to make the series stationary.
3. **q**: the number of moving-average (MA) terms.

In backshift notation the model is $\phi(B)(1 - B)^d X_t = c + \theta(B)\varepsilon_t$.

</details>

<details>
<summary>What is the difference between ARIMA and SARIMA?</summary>

**SARIMA (seasonal ARIMA)** extends ARIMA with seasonal autoregressive, seasonal differencing and seasonal moving-average terms of orders (P, D, Q). These act at multiples of the seasonal period $m$. The model is written ARIMA(p, d, q)(P, D, Q)$_m$, for example ARIMA(1,1,1)(1,1,1)$_{12}$ for monthly data with yearly seasonality.

</details>

## Seasonal Decomposition

<details>
<summary>What is seasonal decomposition of time series?</summary>

**Seasonal decomposition** splits a series into **trend**, **seasonal** and **remainder** components. Classical decomposition estimates the trend with a centred moving average and averages the detrended values by season. **STL** (Seasonal-Trend decomposition using Loess) uses local regression, which lets the seasonal pattern change slowly over time and is more robust to outliers.

</details>

<details>
<summary>Why is it important to decompose a time series?</summary>

Decomposition shows the structure of a series: how strong the trend and seasonality are, and what the remainder looks like. It supports seasonal adjustment (removing $S_t$ to compare periods), helps choose a forecasting model, and makes unusual observations easier to spot in the remainder.

</details>

## Forecasting

<details>
<summary>What is time series forecasting?</summary>

**Time series forecasting** predicts future values from past observations of the series and, optionally, related variables. Common methods include simple benchmarks (naive, seasonal naive, drift), exponential smoothing, ARIMA and SARIMA, regression with ARMA errors, and machine-learning models. Good forecasts include prediction intervals, not just point forecasts.

</details>

<details>
<summary>What is exponential smoothing?</summary>

**Exponential smoothing** forecasts with weighted averages of past observations, with weights that decrease exponentially with age. The main forms are:

1. **Simple exponential smoothing (SES)**: for series with no trend or seasonality.
2. **Holt's linear trend method**: adds a trend component.
3. **Holt–Winters method**: adds both trend and seasonal components, in additive or multiplicative form.

</details>

<details>
<summary>When should you use ARIMA vs exponential smoothing for forecasting?</summary>

- **Exponential smoothing (ETS)** describes the level, trend and seasonality explicitly, so it suits series where these components are clear.
- **ARIMA** describes the autocorrelation structure after differencing, so it suits series with rich short-term dependence and can include covariates through regression with ARMA errors.

Linear exponential smoothing models are special cases of ARIMA. In practice, compare candidates on out-of-sample forecast accuracy.

</details>

## Evaluation Metrics

<details>
<summary>What is Mean Absolute Error (MAE)?</summary>

**Mean absolute error** is the average absolute difference between actual and forecast values:

$$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} | y_i - \hat{y}_i |$$

where $y_i$ are the actual values and $\hat{y}_i$ the forecasts. It is in the units of the data, ignores the direction of errors, and weights all errors equally.

</details>

<details>
<summary>What is Root Mean Squared Error (RMSE)?</summary>

**Root mean squared error** is the square root of the average squared forecast error:

$$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

Squaring gives large errors more weight, so RMSE is more sensitive to occasional big misses and outliers than MAE. RMSE is always at least as large as MAE.

</details>

<details>
<summary>What is Mean Absolute Percentage Error (MAPE)?</summary>

**Mean absolute percentage error** expresses forecast errors as percentages of the actual values:

$$\text{MAPE} = \frac{100}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right|$$

Because it is scale-free, it can compare accuracy across series. However, it is undefined when an actual value is zero and unstable near zero, and it is asymmetric. Scaled measures such as MASE avoid these problems.

</details>

<details>
<summary>How do you choose the best model for time series forecasting?</summary>

Choose using several criteria:

1. **Out-of-sample accuracy**: compare MAE, RMSE or MASE on a hold-out period or with rolling-origin evaluation, never with random shuffling.
2. **Residual diagnostics**: the residuals should resemble white noise, for example by passing a Ljung–Box test.
3. **Parsimony**: among models that perform similarly, prefer simpler ones, for example by lower AIC or BIC.
4. **Domain knowledge**: make sure the model captures known features such as seasonality and structural breaks.

Always compare against simple benchmarks such as the naive or seasonal naive forecast.

</details>
