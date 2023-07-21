## Forecasting with Time Series

Time series forecasting is a technique used to predict future values based on historical data. It is widely used in various fields, such as finance, economics, and meteorology. In this section, we will discuss the basics of time series forecasting.

### Components of a Time Series

A time series can be decomposed into four main components:

1. **Trend**: The long-term movement in the data, usually upward or downward.

```
^
| Value 
|         _________
|       /
|     /
|   /
| /
|/____________ Time ->
```

2. **Seasonality**: Regular fluctuations in the data that occur within fixed periods (e.g., daily, monthly, yearly).

```
^
| Value 
|   _   _   _   _   _
|  / \ / \ / \ / \ / \
| /   X   X   X   X   X
|/_________________ Time ->

```

3. **Cycles**: Irregular fluctuations that occur over longer periods and are not seasonal.

```
^
| Value 
|     _     ___    _   ___
|   /   \_/     \_/ \_/   \
|  /_____________________ Time ->

```

4. **Random (or Irregular)**: The unexplained variation in the data after accounting for the other components.

```
^
| Value 
|
|           . 
|     .                 . 
|                   .
| .     .
|               .
|   .       .       .   
|
|______________________Time ->
```

### Forecasting Methods

### Forecasting Methods

There are various methods for time series forecasting, each suited to specific scenarios and data characteristics. Here are some commonly used methods:

1. **Naive Forecast**: This method assumes that the next value in the time series will be equal to the most recent value.

    If `y` is the time series and `t` is an index to time, the naive forecast for time `t+1` is simply the value at time `t`.

    $$
    \hat{y}_{t+1} = y_t
    $$

2. **Simple Moving Average**: This method calculates the average of the most recent `n` observations and uses it as the forecast for the next value.

    The forecast for time `t+1` is the average of the `p` most recent values.

    $$
    \hat{y}_{t+1} = \frac{1}{p} \sum_{i=0}^{p-1} y_{t-i}
    $$

3. **Exponential Smoothing**: This method applies a weighting scheme to the most recent observations, with higher weights given to more recent values.

    The forecast for time `t+1` is a weighted average between the current value and the previous forecast, where `α` is the smoothing factor (0 < `α` < 1).

    $$
    \hat{y}_{t+1} = αy_t + (1 - α)\hat{y}_t
    $$

4. **Autoregressive (AR) Models**: These models treat the next value in the series as a linear combination of the previous values.

    The value at time `t+1` is modeled as a linear combination of the `p` previous values plus a stochastic error term `ε`.

    $$
    y_{t+1} = c + φ_1y_t + φ_2y_{t-1} + ... + φ_py_{t-p+1} + ε_{t+1}
    $$

5. **Moving Average (MA) Models**: These models treat the next value in the series as a linear combination of previous error terms.

    The value at time `t+1` is modeled as a linear combination of the previous `q` error terms plus a stochastic error term `ε`.

    $$
    y_{t+1} = μ + ε_{t+1} + θ_1ε_t + θ_2ε_{t-1} + ... + θ_qε_{t-q+1}
    $$

6. **Autoregressive Integrated Moving Average (ARIMA) Models**: These models combine AR and MA models and also account for differencing to make the time series stationary.

    The `d`th difference of the time series `y` is modeled as an ARMA(p, q) process.

    $$
    Δ^d y_{t+1} = c + φ_1Δ^d y_t + φ_2Δ^d y_{t-1} + ... + φ_pΔ^d y_{t-p+1} + ε_{t+1} + θ_1ε_t + θ_2ε_{t-1} + ... + θ_qε_{t-q+1}
    $$

    where `Δ^d y` denotes the `d`th difference of `y`.

7. **Seasonal Decomposition of Time Series (STL) and Seasonal ARIMA (SARIMA)**: These methods account for seasonality in time series data. SARIMA is an extension of ARIMA that includes a seasonal component.

    $$
    Δ^D Y_{t+s} = c + φ_1Δ^D Y_{t+s-1} + ... + φ_PΔ^D Y_{t+s-P} + ε_{t+1} + θ_1ε_t + ... + θ_Qε_{t-Q+1}
    $$

    where `Δ^D Y` denotes the seasonal difference (usually, `D=1` and `s` is the period of the seasonality).

### Model Evaluation

To evaluate the accuracy of a time series forecasting model, common metrics include:

1. **Mean Absolute Error (MAE)**: The average of the absolute differences between the predicted and actual values.
2. **Mean Squared Error (MSE)**: The average of the squared differences between the predicted and actual values.
3. **Root Mean Squared Error (RMSE)**: The square root of the MSE.
4. **Mean Absolute Percentage Error (MAPE)**: The average of the absolute percentage differences between the predicted and actual values.

It is crucial to select an appropriate model and evaluate its performance using historical data before making forecasts. This process, known as model validation, helps ensure that the chosen model is accurate and reliable.
