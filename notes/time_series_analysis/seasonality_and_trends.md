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


###  Seasonal ARIMA Processes (SARIMA)

Seasonal ARIMA (SARIMA) models extend the ARIMA framework to account for seasonality in time series data. They are particularly useful when the data exhibits regular, repeating patterns over a specific period.

#### Seasonal ARIMA Models

1. **Seasonal ARMA Processes**
   - For a time series with a seasonal period \( s \), the Seasonal ARMA model is denoted as **ARMA(P, Q)_s**:
     \[
     \Phi_P(B_s) X_t = \Theta_Q(B_s) Z_t
     \]
     where:
     - \(\Phi_P(B_s)\) is the seasonal autoregressive polynomial:
       \[
       \Phi_P(B_s) = 1 - \Phi_1 B_s - \Phi_2 B_s^2 - \ldots - \Phi_P B_s^P
       \]
     - \(\Theta_Q(B_s)\) is the seasonal moving average polynomial:
       \[
       \Theta_Q(B_s) = 1 + \Theta_1 B_s + \Theta_2 B_s^2 + \ldots + \Theta_Q B_s^Q
       \]
     - \( B_s \) denotes the backshift operator with a seasonal period of \( s \).

2. **Seasonal ARIMA Models (SARIMA)**
   - A SARIMA(p, d, q, P, D, Q)_s model combines non-seasonal and seasonal components:
     \[
     \Phi_P(B_s) \phi_p(B) (1 - B_s)^D (1 - B)^d X_t = \Theta_Q(B_s) \theta_q(B) Z_t
     \]
     where:
     - \(\phi_p(B)\) and \(\theta_q(B)\) are the non-seasonal autoregressive and moving average polynomials.
     - \(\Phi_P(B_s)\) and \(\Theta_Q(B_s)\) are the seasonal autoregressive and moving average polynomials.
     - \(D\) is the seasonal differencing order.
     - \(p\), \(d\), and \(q\) are the non-seasonal autoregressive, differencing, and moving average orders.
     - \(P\), \(D\), and \(Q\) are the seasonal autoregressive, differencing, and moving average orders.

#### Examples

1. **Seasonal ARMA(1, 0)_12**
   - This model accounts for a yearly seasonal effect (e.g., monthly data with an annual pattern):
     \[
     (1 - \Phi_1 B^{12}) X_t = Z_t
     \]
     - Here, \(X_t\) depends on \(X_{t-12}\), indicating a seasonal autoregressive term.

2. **Seasonal ARMA(1, 1)_12**
   - This model includes both seasonal autoregressive and moving average terms:
     \[
     (1 - \Phi_1 B^{12}) X_t = (1 + \Theta_1 B^{12}) Z_t
     \]
     - Here, \(X_t\) depends on \(X_{t-12}\) and includes a seasonal moving average term.

3. **SARIMA(1, 0, 0, 1, 0, 1)_12**
   - This model combines non-seasonal and seasonal components:
     \[
     (1 - \phi_1 B) (1 - \Phi_1 B^{12}) X_t = (1 + \Theta_1 B^{12}) Z_t
     \]
     - Simplified, it can be written as:
       \[
       (1 - \phi_1 B - \Phi_1 B^{12} + \phi_1 \Phi_1 B^{13}) X_t = Z_t + \Theta_1 Z_{t-12}
       \]
     - This example includes non-seasonal AR term and seasonal AR and MA terms.

4. **SARIMA(0, 1, 1, 0, 0, 1)_4**
   - This model accounts for quarterly seasonality:
     \[
     (1 - B) X_t = (1 + \Theta_1 B^4) Z_t
     \]
     - Simplified, it is:
       \[
       X_t - X_{t-1} = (1 + \Theta_1 B^4) Z_t
       \]
       - Expanding, it results in:
         \[
         X_t = X_{t-1} + Z_t + \Theta_1 Z_{t-4}
         \]

#### Key Concepts

1. **Stationarity and Invertibility**:
   - For a SARIMA model to be stationary and invertible, the complex roots of the seasonal and non-seasonal polynomials need to lie outside the unit circle.

2. **Seasonal Differencing**:
   - **\(D = 1\)**: Seasonal differencing removes seasonal trends:
     \[
     \nabla_s X_t = X_t - X_{t-s}
     \]
   - **\(D = 2\)**: Double seasonal differencing:
     \[
     \nabla_s^2 X_t = X_t - 2 X_{t-s} + X_{t-2s}
     \]

### ACF of SARIMA Processes


#### Example: SARIMA(0,0,1,0,0,1)_12

**Model Specification:**
\[
X_t = Z_t + \Theta_1 B^{12} (1 + \theta_1 B) Z_t
\]
Expanding, we get:
\[
X_t = Z_t + \theta_1 Z_{t-1} + \Theta_1 Z_{t-12} + \theta_1 \Theta_1 Z_{t-13}
\]

Let’s consider \(\theta_1 = 0.7\) and \(\Theta_1 = 0.6\):
\[
X_t = Z_t + 0.7 Z_{t-1} + 0.6 Z_{t-12} + 0.42 Z_{t-13}
\]

**Autocovariance Function (\(\gamma(k)\)):**

1. **\(\gamma_0\) (Variance of \(X_t\)):**
   \[
   \gamma_0 = \text{Var}(X_t)
   \]
   Since \(X_t\) is composed of white noise terms \(Z_t\) with variance \(\sigma_Z^2\):
   \[
   \text{Var}(X_t) = \sigma_Z^2 + \theta_1^2 \sigma_Z^2 + \Theta_1^2 \sigma_Z^2 + \theta_1^2 \Theta_1^2 \sigma_Z^2
   \]
   Therefore:
   \[
   \gamma_0 = \sigma_Z^2 \left(1 + \theta_1^2 + \Theta_1^2 + \theta_1^2 \Theta_1^2 \right)
   \]

2. **\(\gamma_1\) (Covariance at lag 1):**
   \[
   \gamma_1 = \text{Cov}(X_t, X_{t-1})
   \]
   Since:
   \[
   X_{t-1} = Z_{t-1} + \theta_1 Z_{t-2} + \Theta_1 Z_{t-13} + \theta_1 \Theta_1 Z_{t-14}
   \]
   We get:
   \[
   \gamma_1 = \text{Cov}(Z_t + \theta_1 Z_{t-1} + \Theta_1 Z_{t-12} + \theta_1 \Theta_1 Z_{t-13}, Z_{t-1} + \theta_1 Z_{t-2} + \Theta_1 Z_{t-13} + \theta_1 \Theta_1 Z_{t-14})
   \]
   Simplifying:
   \[
   \gamma_1 = \theta_1 \sigma_Z^2 + \theta_1 \Theta_1 \sigma_Z^2
   \]
   \[
   \gamma_1 = \theta_1 \sigma_Z^2 (1 + \Theta_1)
   \]

3. **ACF at lag 1 (\(\rho(1)\)):**
   \[
   \rho(1) = \frac{\gamma_1}{\gamma_0} = \frac{\theta_1 (1 + \Theta_1)}{1 + \theta_1^2 + \Theta_1^2 + \theta_1^2 \Theta_1^2}
   \]

4. **\(\gamma_2\) (Covariance at lag 2):**
   \[
   \gamma_2 = \text{Cov}(X_t, X_{t-2})
   \]
   Since:
   \[
   X_{t-2} = Z_{t-2} + \theta_1 Z_{t-3} + \Theta_1 Z_{t-14} + \theta_1 \Theta_1 Z_{t-15}
   \]
   We get:
   \[
   \gamma_2 = \text{Cov}(Z_t + \theta_1 Z_{t-1} + \Theta_1 Z_{t-12} + \theta_1 \Theta_1 Z_{t-13}, Z_{t-2} + \theta_1 Z_{t-3} + \Theta_1 Z_{t-14} + \theta_1 \Theta_1 Z_{t-15})
   \]
   Since \(Z_t\) are independent, all cross-terms vanish and:
   \[
   \gamma_2 = 0
   \]

5. **ACF at lag 2 (\(\rho(2)\)):**
   \[
   \rho(2) = \frac{\gamma_2}{\gamma_0} = 0
   \]

6. **General Pattern:**
   - For lags that are not multiples of the seasonal period \(s\), \(\gamma_k = 0\) due to independence of the \(Z_t\).
   - For lags that are multiples of \(s\), \(\gamma_k\) can be non-zero.

7. **Example: \(\gamma_{11}\) (Covariance at lag 11):**
   \[
   \gamma_{11} = \text{Cov}(X_t, X_{t-11})
   \]
   We get:
   \[
   \gamma_{11} = \theta_1 \Theta_1 \sigma_Z^2
   \]
   \[
   \rho(11) = \frac{\gamma_{11}}{\gamma_0} = \frac{\theta_1 \Theta_1}{1 + \theta_1^2 + \Theta_1^2 + \theta_1^2 \Theta_1^2}
   \]


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

- **Time Series with Trend (Blue and Orange)**: The original data (in blue) is plotted alongside the trend component (in orange).
- **Seasonal Component (Green)**: This plot displays the extracted seasonal component, clearly illustrating the repeating yearly pattern.
- **Differenced Series (Purple)**: After applying differencing, this plot shows the modified time series, which helps in achieving stationarity.
- **Forecast vs. Actual (Blue and Red)**: The original series (in blue) and the forecast (in red) are displayed. The shaded area in black represents the confidence intervals, providing an estimate of the forecast's uncertainty.

## Seasonal Decomposition 

Seasonal decomposition of time series is a technique that deconstructs a time series into its constituent components: trend, seasonal, and residual. The Seasonal-Trend decomposition procedure based on LOESS (STL) is a robust method for this decomposition. This method is particularly useful for analyzing time series data with complex seasonal and trend patterns.

### Example

To illustrate STL decomposition, we'll generate a synthetic time series dataset that exhibits clear seasonal patterns, trends, and some random noise. We'll then apply STL decomposition to this data and visualize the components.

This plot shows the original synthetic time series data, combining seasonal, trend, and noise components.

![output(3)](https://github.com/djeada/Statistics-Notes/assets/37275728/b10c0196-3455-4c59-8807-a64d11ebc651)

The original data exhibits an upward trend with clear seasonal fluctuations and some random noise. This visualization helps in understanding the overall structure and patterns in the time series.

By performing STL decomposition, we can separately analyze the trend, seasonal, and residual components, providing insights into the underlying structure of the time series data. This technique is particularly useful for identifying patterns and making more accurate forecasts.

![output(4)](https://github.com/djeada/Statistics-Notes/assets/37275728/6cd784df-8e35-411c-92bd-f94b9529e191)

**Seasonal Component**:
- **Plot Description**: This plot shows the seasonal fluctuations in the data, which repeat annually.
- **Interpretation**: The seasonal component captures the repeating yearly pattern, demonstrating the synthetic seasonal effect added to the data. It shows how the data values fluctuate within each year.

**Trend Component**:
- **Plot Description**: This plot represents the long-term progression of the data over the entire period.
- **Interpretation**: The trend component shows a clear upward trajectory, indicating a consistent increase in the data over time. This is consistent with the linear trend added to the synthetic data.

**Residual Component**:
- **Plot Description**: This plot displays the residuals, which are the remaining variations in the data after removing the trend and seasonal components.
- **Interpretation**: The residual component reflects random noise. It should ideally display no discernible pattern, indicating that the trend and seasonality have been effectively removed from the data. The residuals appear to be randomly distributed around zero, confirming that the decomposition has captured the main patterns in the data.


#### Additional Considerations

- **Diagnostic Checks:** Perform residual analysis to check the adequacy of the model.
- **Model Selection:** Use criteria like AIC (Akaike Information Criterion) or BIC (Bayesian Information Criterion) to select the best model.
- **Cross-Validation:** Apply techniques like time series cross-validation to assess the model's predictive performance.
