### Seasonal ARIMA Processes (SARIMA)

Seasonal ARIMA (SARIMA) models are widely used for time series data exhibiting both trend and seasonal behaviors.

#### Mathematical Formulation

A **SARIMA(\( p, d, q \times P, D, Q \))\(_s\)** model incorporates both non-seasonal and seasonal factors:

\[
\Phi_P(B^s) \phi_p(B) (1 - B^s)^D (1 - B)^d X_t = \Theta_Q(B^s) \theta_q(B) \epsilon_t
\]

- **Non-seasonal Components**:
  - **Autoregressive (AR) Polynomial**: \( \phi_p(B) \)
  - **Differencing Order**: \( d \)
  - **Moving Average (MA) Polynomial**: \( \theta_q(B) \)

- **Seasonal Components**:
  - **Seasonal AR Polynomial**: \( \Phi_P(B^s) \)
  - **Seasonal Differencing Order**: \( D \)
  - **Seasonal MA Polynomial**: \( \Theta_Q(B^s) \)
  - **Seasonal Period**: \( s \)

- **Backshift Operator**:
  - **Non-seasonal**: \( B X_t = X_{t-1} \)
  - **Seasonal**: \( B^s X_t = X_{t-s} \)

#### Examples of SARIMA Models

##### Example 1: SARIMA(1, 0, 0)(1, 0, 0)\(_{12}\)

**Model Equation**:

\[
(1 - \phi_1 B)(1 - \Phi_1 B^{12}) X_t = \epsilon_t
\]

- **Non-seasonal AR(1)**: \( \phi_1 B X_t \)
- **Seasonal AR(1) with period 12**: \( \Phi_1 B^{12} X_t \)
- **Interpretation**: Current value depends on the previous value and the value from 12 periods ago.

##### Example 2: SARIMA(0, 1, 1)(0, 1, 1)\(_{4}\)

**Model Equation**:

\[
(1 - B)(1 - B^4) X_t = (1 + \theta_1 B)(1 + \Theta_1 B^4) \epsilon_t
\]

- **First-order Non-seasonal Differencing**: \( (1 - B) X_t \)
- **First-order Seasonal Differencing with period 4**: \( (1 - B^4) X_t \)
- **Non-seasonal MA(1)**: \( \theta_1 B \epsilon_t \)
- **Seasonal MA(1)**: \( \Theta_1 B^4 \epsilon_t \)

##### Simplification and Expansion

**Expanding the Differencing Operators**:

- **Non-seasonal Differencing**:
  \[
  (1 - B) X_t = X_t - X_{t-1}
  \]
- **Seasonal Differencing**:
  \[
  (1 - B^s) X_t = X_t - X_{t-s}
  \]

**Combining Differencing**:

\[
(1 - B)(1 - B^s) X_t = X_t - X_{t-1} - X_{t-s} + X_{t-s-1}
\]

#### Stationarity and Invertibility Conditions

- **Stationarity**: All roots of \( \phi_p(B) \) and \( \Phi_P(B^s) \) polynomials must lie outside the unit circle.
- **Invertibility**: All roots of \( \theta_q(B) \) and \( \Theta_Q(B^s) \) polynomials must lie outside the unit circle.

#### Seasonal Differencing

- **Purpose**: Remove seasonal trends to achieve stationarity.
- **First-order Seasonal Differencing**:
  \[
  \nabla_s X_t = X_t - X_{t-s}
  \]
- **Second-order Seasonal Differencing**:
  \[
  \nabla_s^2 X_t = X_t - 2 X_{t-s} + X_{t-2s}
  \]

### Autocorrelation Function (ACF) of SARIMA Processes

The ACF of a SARIMA model displays patterns reflecting both seasonal and non-seasonal behavior.

#### Example: SARIMA(0, 0, 1)(0, 0, 1)\(_{12}\)

**Model Specification**:

\[
X_t = \epsilon_t + \theta_1 \epsilon_{t-1} + \Theta_1 \epsilon_{t-12} + \theta_1 \Theta_1 \epsilon_{t-13}
\]

- **Parameters**:
  - \( \theta_1 = 0.7 \)
  - \( \Theta_1 = 0.6 \)
- **Error Term**:
  - \( \epsilon_t \): White noise with mean zero and variance \( \sigma^2 \)

#### Calculating Autocovariances

1. **Variance (\( \gamma_0 \))**:

   \[
   \gamma_0 = \text{Var}(X_t) = \sigma^2 \left(1 + \theta_1^2 + \Theta_1^2 + \theta_1^2 \Theta_1^2\right)
   \]

2. **Covariance at Lag 1 (\( \gamma_1 \))**:

   \[
   \gamma_1 = \text{Cov}(X_t, X_{t-1}) = \sigma^2 \theta_1 \left(1 + \Theta_1^2\right)
   \]

3. **Covariance at Lag 12 (\( \gamma_{12} \))**:

   \[
   \gamma_{12} = \sigma^2 \Theta_1 \left(1 + \theta_1^2\right)
   \]

4. **Covariance at Lag 13 (\( \gamma_{13} \))**:

   \[
   \gamma_{13} = \sigma^2 \theta_1 \Theta_1 \left(1 + \theta_1 \Theta_1\right)
   \]

#### Calculating Autocorrelations

- **ACF at Lag \( k \)**:

  \[
  \rho_k = \frac{\gamma_k}{\gamma_0}
  \]

- **Interpretation**:
  - Significant spikes at lags that are multiples of the seasonal period (\( s \)) indicate seasonal correlations.
  - Non-seasonal correlations are observed at lower lags.

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
