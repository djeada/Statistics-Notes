## Forecasting with Time Series

Time series forecasting is a technique used to predict future values based on historical data. It is widely used in various fields, such as finance, economics, and meteorology. In this section, we will discuss the basics of time series forecasting.

### Components of a Time Series

A time series can be decomposed into four main components:

1. **Trend**: This represents the long-term progression of the series, signifying a persistent, general direction of the data over a long period. It can be upward, downward, or even a stable trend.

```
^
| Value 
|         __________
|       /
|     /
|   /
| /
|/___________________ Time ->
```

2. **Seasonality**: These are patterns that repeat at regular intervals, like daily, monthly, or quarterly. This component reflects the influence of seasonal factors on the time series.

```
^
| Value
|    /\  /\  /\  /\  /\  
|   /  \/  \/  \/  \/  \ 
|  /                    \
|/_______________________\___ Time ->
```

3. **Cycles**:  Unlike seasonality, cyclical patterns occur at less regular intervals. These fluctuations are often linked to economic, political, or even environmental factors and can span multiple years.

```
^
| Value
|                               ___
|                         ___--     --___
|        ___         ___-                 -
|   __--     --__-                          -__
|_/                                              \_
|__________________________________________________ Time ->
```

4. **Random (or Irregular)**: This component captures the 'noise' or random variation in the data. It represents the unpredictable, erratic factors affecting the time series after the trend, seasonality, and cyclical components have been accounted for.

```
^
| Value
|   .       .  .      .   .   . . 
|  . .    .      .  .    .      . 
|    .      . .   .  . .   .    .
| .    .  .   .     .    .   .   
|________________________________ Time ->
```

### Forecasting Methods

There are various methods for time series forecasting, each suited to specific scenarios and data characteristics. Here are some commonly used methods:

#### Naive Forecast

This method assumes that the next value in the time series will be equal to the most recent value.

If `y` is the time series and `t` is an index to time, the naive forecast for time `t+1` is simply the value at time `t`.

$$
\hat{y}_{t+1} = y_t
$$

#### Simple Moving Average

This method calculates the average of the most recent `n` observations and uses it as the forecast for the next value.

The forecast for time `t+1` is the average of the `p` most recent values.

$$
\hat{y}_{t+1} = \frac{1}{p} \sum_{i=0}^{p-1} y_{t-i}
$$

#### Exponential Smoothing

This method applies a weighting scheme to the most recent observations, with higher weights given to more recent values.

The forecast for time `t+1` is a weighted average between the current value and the previous forecast, where `α` is the smoothing factor (0 < `α` < 1).

$$
\hat{y}_{t+1} = αy_t + (1 - α)\hat{y}_t
$$

#### Autoregressive (AR) Models

These models treat the next value in the series as a linear combination of the previous values.

The value at time `t+1` is modeled as a linear combination of the `p` previous values plus a stochastic error term `ε`.

$$
y_{t+1} = c + φ_1y_t + φ_2y_{t-1} + ... + φ_py_{t-p+1} + ε_{t+1}
$$

#### Moving Average (MA) Models

These models treat the next value in the series as a linear combination of previous error terms.

The value at time `t+1` is modeled as a linear combination of the previous `q` error terms plus a stochastic error term `ε`.

$$
y_{t+1} = μ + ε_{t+1} + θ_1ε_t + θ_2ε_{t-1} + ... + θ_qε_{t-q+1}
$$

#### Autoregressive Integrated Moving Average (ARIMA) Models

These models combine AR and MA models and also account for differencing to make the time series stationary.

The `d`th difference of the time series `y` is modeled as an ARMA(p, q) process.

$$
Δ^d y_{t+1} = c + φ_1Δ^d y_t + φ_2Δ^d y_{t-1} + ... + φ_pΔ^d y_{t-p+1} + ε_{t+1} + θ_1ε_t + θ_2ε_{t-1} + ... + θ_qε_{t-q+1}
$$

where `Δ^d y` denotes the `d`th difference of `y`.

#### Seasonal Decomposition of Time Series (STL) and Seasonal ARIMA (SARIMA)

These methods account for seasonality in time series data. SARIMA is an extension of ARIMA that includes a seasonal component.

$$
Δ^D Y_{t+s} = c + φ_1Δ^D Y_{t+s-1} + ... + φ_PΔ^D Y_{t+s-P} + ε_{t+1} + θ_1ε_t + ... + θ_Qε_{t-Q+1}
$$

where `Δ^D Y` denotes the seasonal difference (usually, `D=1` and `s` is the period of the seasonality).

### Model Evaluation for Time Series Forecasting

Evaluating the accuracy and effectiveness of a time series forecasting model is crucial. Various metrics are used, each providing different insights into the model's performance. Understanding these metrics and their implications can help in choosing the right model and refining it for better accuracy.

#### Mean Absolute Error (MAE)

The average of the absolute differences between the forecasted and actual values.

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$

where $y_i$ are actual values, $\hat{y}_i$ are forecasted values, and $n$ is the number of observations.

Lower MAE values indicate better model accuracy. MAE gives a straightforward measure of error magnitude but doesn't indicate direction (over or under-forecasting).

#### Mean Squared Error (MSE)

The average of the squared differences between the forecasted and actual values.

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Lower MSE values are better. MSE penalizes larger errors more severely than smaller ones, making it useful when large errors are particularly undesirable.

#### Root Mean Squared Error (RMSE)

The square root of the MSE.

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

RMSE is more interpretable in the same units as the forecasted values. Like MSE, it gives more weight to larger errors. Lower RMSE values indicate better model performance.

#### Mean Absolute Percentage Error (MAPE)
The average of the absolute percentage differences between the forecasted and actual values.

$$
\text{MAPE} = \frac{100\%}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right|
$$

MAPE expresses accuracy as a percentage, making it easily interpretable. Lower MAPE values indicate better accuracy. However, it can be misleading when dealing with zero or near-zero actual values.

#### Acceptance Criteria for Models

- The acceptance of a model based on these metrics depends on the specific context and requirements of the forecasting task. There's no universal threshold for these metrics to declare a model acceptable or not.
- In practice, models are often compared with each other, and the one with the lowest error metrics (considering the business context and cost of errors) is chosen.
- It's also important to balance statistical accuracy with the interpretability and complexity of the model. Sometimes a slightly less accurate but simpler model is preferred for ease of use and understanding.

#### Additional Considerations

- **Overfitting**: A model that performs exceptionally well on training data but poorly on unseen data may be overfitting. It's crucial to evaluate models on a separate test dataset.
- **Baseline Comparisons**: Compare model performance against a naive baseline (like simple historical average) to gauge the added value of the model.
- **Cross-Validation**: Especially in time series, using techniques like time series cross-validation can provide a more reliable performance estimate.
- **Combination of Metrics**: Using a combination of different error metrics can provide a more holistic view of model performance.
