## Seasonality and Trends

Seasonality and trends are common components of time series data that can impact the analysis and forecasting. Understanding these components is essential for selecting the appropriate model and improving forecast accuracy.

### Seasonality

Seasonality refers to periodic patterns that repeat at regular intervals in a time series. Examples of seasonal patterns include daily temperature fluctuations, weekly sales patterns, or annual fluctuations in stock prices. Seasonal patterns can be either additive or multiplicative.

#### Decomposing Seasonality

To analyze and remove seasonality, a time series can be decomposed into its components: trend, seasonal, and residual (also known as irregular or noise). Common decomposition methods include:

1. Moving average: A centered moving average can be used to estimate the trend component, and the seasonal component can be obtained by subtracting the trend from the original time series.
2. Seasonal decomposition of time series (STL): A more advanced technique that decomposes a time series into its seasonal, trend, and residual components using loess smoothing.

### Trends

Trends represent the long-term direction of a time series. A trend can be upward, downward, or stationary. Identifying and accounting for trends can improve the accuracy of time series forecasts.

#### Detrending Methods

1. Differencing: Subtracting the time series values at different lags, such as first-order differencing, where each observation is replaced by the difference between consecutive observations.
2. Transformation: Applying a transformation to the time series, such as taking the logarithm, to stabilize the trend.
3. Regression: Fitting a linear or nonlinear regression model to the time series and using the residuals as the detrended series.

### Modeling Seasonality and Trends

Some time series models explicitly account for seasonality and trends:

1. Seasonal ARIMA: An extension of the ARIMA model that includes seasonal differencing and seasonal autoregressive and moving average terms.
2. Exponential smoothing state space model (ETS): A general class of forecasting models that can handle additive and multiplicative seasonality, as well as additive and multiplicative trends.
3. Seasonal decomposition of time series (STL) forecasting: A two-step approach where the time series is first decomposed into its components, and then each component is forecasted separately.

### Example: Monthly Airline Passenger Data

Consider a time series consisting of monthly airline passenger data. This particular time series is characterized by two distinct features: an upward trend indicating an increase in the number of passengers over time, and a seasonal pattern that repeats every 12 months, typically linked to factors such as holiday travel or seasonal tourism.

### Steps to Model and Forecast the Time Series

I. Decompose the Time Series into Trend, Seasonal, and Residual Components:

- Use time series decomposition methods like `classical decomposition` or `STL decomposition`.
- This process separates the original time series into three components:
- **Trend Component:** Shows the long-term progression of the series (increasing or decreasing).
- **Seasonal Component:** Reflects the regular pattern that occurs at fixed intervals (e.g., monthly, quarterly).
- **Residual Component:** Captures the irregularities or 'noise' that cannot be attributed to the trend or seasonal components.

II. Detrend the Time Series Using Differencing or Transformation:

- Apply methods like `logarithmic transformation` or `differencing` to stabilize the mean of the time series.
- **Differencing:** Subtract the current value from the previous value. This can be adjusted for seasonality (e.g., subtracting the value from the same month in the previous year).
- **Transformation:** Use techniques like log, square root, or Box-Cox transformation to stabilize variance and make the series more stationary.

III. Fit an Appropriate Model that Accounts for Both Trend and Seasonality:

- Use models like `Seasonal ARIMA (SARIMA)` or `Exponential Smoothing State Space Model (ETS)`:
- **SARIMA:** An extension of ARIMA that includes seasonal terms. It is defined by parameters (p, d, q) for the non-seasonal part and (P, D, Q)s for the seasonal part.
- **ETS:** A model that combines error, trend, and seasonal components. It is particularly useful when the data exhibit a consistent seasonal pattern.

IV. Forecast Future Values Using the Fitted Model:

- Use the model to forecast future values.
- This step involves generating predictions based on the model's understanding of the trend and seasonal patterns in the historical data.
- Ensure to provide confidence intervals for these predictions to understand the potential variability in the forecasts.

![seasonality_forecast](https://github.com/djeada/Statistics-Notes/assets/37275728/218ec3bc-81a7-492e-a69b-3bf3d97ba8de)

#### Additional Considerations

- **Diagnostic Checks:** Perform residual analysis to check the adequacy of the model.
- **Model Selection:** Use criteria like AIC (Akaike Information Criterion) or BIC (Bayesian Information Criterion) to select the best model.
- **Cross-Validation:** Apply techniques like time series cross-validation to assess the model's predictive performance.
