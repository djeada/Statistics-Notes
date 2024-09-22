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
<summary>What are the main components of a time series?</summary><br>
A time series can be decomposed into three main components:
1. **Trend**: The long-term direction of the series (upward, downward, or flat).
2. **Seasonality**: Regular, repeating patterns that occur over specific intervals (e.g., quarterly sales increases).
3. **Residual (Noise)**: Random fluctuations that are not explained by trend or seasonality.
</details>

<details>
<summary>What is an example of seasonality in time series data?</summary><br>
An example of seasonality would be retail sales that peak every December due to holiday shopping. This repeating annual pattern in sales data is a typical seasonal component.
</details>

<details>
<summary>How can a trend affect a time series?</summary><br>
A **trend** represents the long-term movement in the data over time. It can be upward (increasing values), downward (decreasing values), or stationary (no consistent change). For example, a rising trend in stock prices over several years indicates an overall upward movement despite short-term fluctuations.
</details>

---

## Stationarity

<details>
<summary>What is a stationary time series?</summary><br>
A **stationary time series** is one where the statistical properties (mean, variance, and autocorrelation) are constant over time. A stationary series does not exhibit trends or seasonality and is essential for many time series models, including ARIMA.
</details>

<details>
<summary>How do you test for stationarity?</summary><br>
The **Augmented Dickey-Fuller (ADF) test** is commonly used to test for stationarity. If the p-value of the test is less than a chosen significance level (e.g., 0.05), the null hypothesis (that the series is non-stationary) can be rejected, indicating that the series is stationary.
</details>

<details>
<summary>How do you make a time series stationary?</summary><br>
To make a time series stationary, you can:
1. **Differencing**: Subtracting each observation from the previous one to remove trends.
2. **De-trending**: Removing the trend component.
3. **Log transformation**: Reducing variance by applying a logarithmic transformation to the data.
4. **Seasonal differencing**: Subtracting observations from the corresponding value in the previous season to remove seasonality.
</details>

---

## Autocorrelation and Partial Autocorrelation

<details>
<summary>What is autocorrelation?</summary><br>
**Autocorrelation** is the correlation of a time series with a lagged version of itself. It measures how current values of the series relate to past values. Positive autocorrelation indicates that high values tend to follow high values, and negative autocorrelation indicates that high values follow low values.
</details>

<details>
<summary>What is a partial autocorrelation function (PACF)?</summary><br>
The **partial autocorrelation function (PACF)** measures the correlation between the current time series value and its lagged values, controlling for the values of the time series at shorter lags. PACF helps identify the number of autoregressive (AR) terms needed in an ARIMA model.
</details>

<details>
<summary>What are ACF and PACF plots used for?</summary><br>
**ACF (Autocorrelation Function) plots** show how the correlation between time series values decreases as the lag increases, while **PACF plots** show the partial correlation at each lag, adjusting for earlier lags. These plots are used to identify the appropriate parameters for ARIMA models.
</details>

---

## Moving Averages

<details>
<summary>What is a simple moving average?</summary><br>
A **simple moving average (SMA)** is the unweighted mean of a fixed number of past observations. It smooths out fluctuations in a time series by averaging over a sliding window of previous values, making it easier to identify trends.
The formula is:
\[ \text{SMA}_t = \frac{1}{n} \sum_{i=t-n+1}^{t} X_i \]
where \(n\) is the window size.
</details>

<details>
<summary>What is an exponential moving average (EMA)?</summary><br>
An **exponential moving average (EMA)** gives more weight to recent observations compared to older ones, making it more responsive to changes in the time series. The EMA is calculated recursively, using a smoothing factor that controls how much weight is given to recent data points.
</details>

<details>
<summary>How are moving averages used in time series forecasting?</summary><br>
**Moving averages** smooth out short-term fluctuations in time series data, making it easier to identify underlying trends and seasonality. In forecasting, they are often used to estimate future values by extrapolating current trends or to remove noise from the data.
</details>

---

## ARIMA Models

<details>
<summary>What does ARIMA stand for?</summary><br>
**ARIMA** stands for **AutoRegressive Integrated Moving Average**:
1. **AR (AutoRegressive)**: Uses past values (lags) to predict future values.
2. **I (Integrated)**: Involves differencing the data to make it stationary.
3. **MA (Moving Average)**: Uses past forecast errors to improve predictions.
ARIMA models are commonly used for time series forecasting when the data shows no strong seasonal component.
</details>

<details>
<summary>What are the parameters of an ARIMA model?</summary><br>
An ARIMA model is defined by three parameters:
1. **p**: The number of autoregressive (AR) terms.
2. **d**: The number of differences needed to make the series stationary.
3. **q**: The number of moving average (MA) terms.
The notation ARIMA(p, d, q) specifies how many terms are included for each component.
</details>

<details>
<summary>What is the difference between ARIMA and SARIMA?</summary><br>
**SARIMA (Seasonal ARIMA)** extends ARIMA by incorporating seasonality into the model. SARIMA includes additional parameters for seasonal autoregressive, seasonal differencing, and seasonal moving average components, denoted by (P, D, Q, m), where \(m\) is the length of the seasonal cycle. The full SARIMA model is expressed as ARIMA(p, d, q)(P, D, Q)_m.
</details>

---

## Seasonal Decomposition

<details>
<summary>What is seasonal decomposition of time series?</summary><br>
**Seasonal decomposition** breaks down a time series into its main components: **trend**, **seasonality**, and **residuals** (random fluctuations). Methods like **STL (Seasonal-Trend Decomposition using Loess)** are commonly used to separate these components, making it easier to understand and model the series.
</details>

<details>
<summary>Why is it important to decompose a time series?</summary><br>
Decomposing a time series allows you to better understand its structure by separating the trend, seasonal, and noise components. This is useful for improving forecasts and identifying underlying patterns, especially when the series has complex seasonal effects.
</details>

---

## Forecasting

<details>
<summary>What is time series forecasting?</summary><br>
**Time series forecasting** involves predicting future values based on historical time series data. Techniques like **ARIMA**, **SARIMA**, **Exponential Smoothing**, and **Prophet** are commonly used to generate forecasts by modeling the trend, seasonality, and noise in the data.
</details>

<details>
<summary>What is exponential smoothing?</summary><br>
**Exponential smoothing** is a time series forecasting method that assigns exponentially decreasing weights to past observations. The most common forms are:
1. **Simple Exponential Smoothing (SES)**: For series with no trend or seasonality.
2. **Holt’s Linear Trend Model**: For series with a trend but no seasonality.
3. **Holt-Winters Exponential Smoothing**: For series with both trend and seasonality.
</details>

<details>
<summary>When should you use ARIMA vs Exponential Smoothing for forecasting?</summary><br>
- **ARIMA** is preferred for non-seasonal data that requires differencing

 to achieve stationarity and for data with autocorrelated residuals.
- **Exponential Smoothing** (especially Holt-Winters) is more suited to data with a clear trend and seasonal components that are not autocorrelated.
The choice depends on the characteristics of the time series and the goal of the forecasting.
</details>

---

## Evaluation Metrics

<details>
<summary>What is Mean Absolute Error (MAE)?</summary><br>
**Mean Absolute Error (MAE)** is the average of the absolute differences between forecasted and actual values. It gives a linear measure of the magnitude of the errors, without considering their direction. The formula is:
\[ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} | y_i - \hat{y}_i | \]
where \(y_i\) are the actual values and \(\hat{y}_i\) are the forecasted values.
</details>

<details>
<summary>What is Root Mean Squared Error (RMSE)?</summary><br>
**Root Mean Squared Error (RMSE)** is the square root of the average squared differences between forecasted and actual values. RMSE gives more weight to larger errors, making it sensitive to outliers. The formula is:
\[ \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2} \]
</details>

<details>
<summary>What is Mean Absolute Percentage Error (MAPE)?</summary><br>
**Mean Absolute Percentage Error (MAPE)** expresses the accuracy of a forecast as a percentage, by taking the absolute difference between actual and forecasted values relative to the actual values. The formula is:
\[ \text{MAPE} = \frac{100}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \]
MAPE is useful when comparing forecasting errors across different time series.
</details>

<details>
<summary>How do you choose the best model for time series forecasting?</summary><br>
The best model for time series forecasting is chosen based on several criteria, including:
1. **Low forecasting error**: Measured using metrics like MAE, RMSE, or MAPE.
2. **Fit to the data**: Evaluating how well the model captures the trend, seasonality, and residual components.
3. **Simplicity**: A simpler model with good performance may be preferred over a more complex model.
4. **Domain knowledge**: Understanding the context and characteristics of the data helps in choosing the right model (e.g., seasonal patterns).
</details>
