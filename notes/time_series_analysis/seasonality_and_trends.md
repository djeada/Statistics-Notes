## Seasonality and Trends in Time Series Analysis

Seasonality and trends are fundamental components in time series data that significantly impact analysis and forecasting. Understanding and correctly modeling these elements are crucial for accurate predictions and effective time series modeling.

### Seasonality

**Seasonality** refers to periodic fluctuations that repeat at regular intervals over time. These patterns are often driven by seasonal factors such as weather, holidays, or economic cycles.

#### Characteristics of Seasonality

- **Periodicity**: Seasonality occurs at fixed, known intervals (e.g., daily, weekly, monthly, yearly).
- **Additive or Multiplicative**: Seasonal effects can be additive (constant magnitude) or multiplicative (varying magnitude proportional to the level of the series).

#### Examples of Seasonal Patterns

- **Daily**: Electricity consumption peaking during specific hours.
- **Weekly**: Increased retail sales on weekends.
- **Monthly/Quarterly**: Higher ice cream sales during summer months.
- **Annual**: Tax filings increasing every April.

#### Decomposing Seasonality

To analyze and remove seasonality, a time series can be decomposed into three main components:

1. **Trend Component (\( T_t \))**: The long-term progression of the series.
2. **Seasonal Component (\( S_t \))**: The repeating short-term cycle.
3. **Residual Component (\( R_t \))**: The irregular or random fluctuations.

Mathematically, for an additive model:

\[
X_t = T_t + S_t + R_t
\]

For a multiplicative model:

\[
X_t = T_t \times S_t \times R_t
\]

##### Decomposition Methods

1. **Moving Average Method**:

   - **Purpose**: Estimate the trend component by smoothing the series.
   - **Procedure**:
     - Apply a centered moving average of order equal to the seasonal period to \( X_t \).
     - Subtract the estimated trend \( T_t \) from \( X_t \) to obtain the seasonal component \( S_t \).

2. **Seasonal Decomposition of Time Series by Loess (STL)**:

   - **Purpose**: Decompose the series into trend, seasonal, and residual components using local regression (loess).
   - **Advantages**:
     - Handles both additive and multiplicative seasonality.
     - Robust to outliers.
     - Flexible in handling complex seasonal patterns.

### Trends

**Trend** refers to the long-term movement or direction in the time series data. Trends can be:

- **Upward**: General increase over time.
- **Downward**: General decrease over time.
- **Stationary**: No significant long-term movement.

#### Identifying Trends

- **Visual Inspection**: Plotting the time series to observe overall direction.
- **Statistical Tests**: Applying tests like the Mann-Kendall trend test.
- **Autocorrelation Function (ACF)**: Slow decay in ACF suggests non-stationarity due to trend.

#### Detrending Methods

1. **Differencing**:

   - **First-order Differencing**:
     \[
     Y_t = X_t - X_{t-1}
     \]
   - **Second-order Differencing**:
     \[
     Y_t = (X_t - X_{t-1}) - (X_{t-1} - X_{t-2}) = X_t - 2X_{t-1} + X_{t-2}
     \]
   - **Purpose**: Remove trends by analyzing changes between consecutive observations.

2. **Transformation**:

   - **Logarithmic Transformation**:
     \[
     Y_t = \log(X_t)
     \]
   - **Purpose**: Stabilize variance and linearize exponential trends.

3. **Regression Modeling**:

   - **Linear Trend Model**:
     \[
     X_t = \beta_0 + \beta_1 t + \epsilon_t
     \]
   - **Nonlinear Trend Model**:
     \[
     X_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \epsilon_t
     \]
   - **Purpose**: Fit a trend line to the data and analyze residuals.

#### Visualization of Trends

- **Time Series Plot**: Shows the overall direction of the data over time.
- **Detrended Series Plot**: Displays the series after removing the trend, highlighting other components like seasonality or noise.

### Modeling Seasonality and Trends

Effectively modeling seasonality and trends is essential for accurate forecasting. Several models explicitly account for these components.

#### 1. Seasonal ARIMA (SARIMA)

An extension of ARIMA models that includes seasonal terms to handle seasonality.

- **SARIMA Model Specification**:

  \[
  \Phi_P(B^s) \phi_p(B) (1 - B^s)^D (1 - B)^d X_t = \Theta_Q(B^s) \theta_q(B) \epsilon_t
  \]

  - \( \phi_p(B) \): Non-seasonal AR polynomial of order \( p \).
  - \( \theta_q(B) \): Non-seasonal MA polynomial of order \( q \).
  - \( \Phi_P(B^s) \): Seasonal AR polynomial of order \( P \).
  - \( \Theta_Q(B^s) \): Seasonal MA polynomial of order \( Q \).
  - \( D \): Seasonal differencing order.
  - \( d \): Non-seasonal differencing order.
  - \( s \): Seasonal period (e.g., 12 for monthly data with yearly seasonality).

#### 2. Exponential Smoothing State Space Models (ETS)

A class of models using weighted averages of past observations, suitable for data with trends and seasonality.

- **Components**:
  - **Level**: The baseline value of the series.
  - **Trend**: The direction and rate of change.
  - **Seasonality**: The repeating patterns.
- **Types**:
  - **Additive Model**: Suitable when seasonal variations are roughly constant over time.
  - **Multiplicative Model**: Suitable when seasonal variations change proportionally with the level of the series.

#### 3. Seasonal Decomposition of Time Series (STL) Forecasting

A two-step approach:

1. **Decomposition**: Split the series into trend, seasonal, and residual components.
2. **Forecasting**: Model and forecast each component separately, then recombine.

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
- The **plot description** shows the seasonal fluctuations in the data, which repeat annually.
- The **interpretation** of this seasonal component highlights the repeating yearly pattern, demonstrating the synthetic seasonal effect added to the data, and shows how the values fluctuate within each year.

**Trend Component**:
- The **plot description** represents the long-term progression of the data over the entire period.
- The **interpretation** of the trend component reveals a clear upward trajectory, indicating a consistent increase in the data over time, which aligns with the linear trend added to the synthetic data.

**Residual Component**:
- The **plot description** displays the residuals, showing the remaining variations in the data after removing the trend and seasonal components.
- The **interpretation** of the residual component reflects random noise. Ideally, it shows no discernible pattern, suggesting that the trend and seasonality have been effectively removed, with residuals randomly distributed around zero, confirming that the decomposition has captured the main patterns in the data.
