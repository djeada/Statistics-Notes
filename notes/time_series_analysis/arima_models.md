## ARMA, ARIMA and SARIMA Models

ARMA, ARIMA, and SARIMA are models commonly used to analyze and forecast time series data. ARMA (AutoRegressive Moving Average) combines two ideas: using past values to predict current ones (**autoregression**) and smoothing out noise using past forecast errors (**moving average**). ARIMA (AutoRegressive Integrated Moving Average) builds on ARMA by adding a step to handle trends in non-stationary data through differencing. SARIMA (Seasonal ARIMA) takes it a step further by accounting for repeating seasonal patterns. These models are practical and versatile for working with time series data that show trends, noise, or seasonal effects.

### Autoregressive Moving Average (ARMA) Models

ARMA models combine autoregressive (AR) and moving average (MA) components to model time series data exhibiting both autocorrelation and serial dependence.

#### Mathematical Definition of ARMA Models

An **ARMA($p, q$)** model is defined by:

$$X_t = c + \sum_{i=1}^{p} \phi_i X_{t-i} + \epsilon_t + \sum_{j=1}^{q} \theta_j \epsilon_{t-j}$$

or, equivalently, using the backshift operator $B$:

$$\phi(B) X_t = c + \theta(B) \epsilon_t$$

where:

- $\phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p$
- $\theta(B) = 1 + \theta_1 B + \theta_2 B^2 + \dots + \theta_q B^q$

#### Stationarity of AR Processes

An AR($p$) process is **stationary** if all the roots of the characteristic polynomial $\phi(B) = 0$ lie outside the unit circle in the complex plane. This condition ensures that the time series has a constant mean and variance over time.

#### Invertibility of MA Processes

An MA($q$) process is **invertible** if all the roots of $\theta(B) = 0$ lie outside the unit circle. Invertibility allows the MA process to be expressed as an infinite AR process, ensuring a unique representation and facilitating parameter estimation.

#### Infinite Order Representations

**AR(∞) Representation of MA Processes**:

An MA process can be expressed as an infinite-order AR process:

$$X_t = \sum_{k=1}^{\infty} \pi_k X_{t-k} + \epsilon_t$$

**MA(∞) Representation of AR Processes**:

An AR process can be expressed as an infinite-order MA process:

$$X_t = \sum_{k=0}^{\infty} \psi_k \epsilon_{t-k}$$

#### Example: ARMA(1,1) Process

Consider the ARMA(1,1) model:

$$X_t = \phi X_{t-1} + \epsilon_t + \theta \epsilon_{t-1}$$

Let $\phi = 0.7$, $\theta = 0.2$, and $\epsilon_t$ is white noise.

##### Simulation

To analyze this process, we simulate a large number of observations using statistical software (e.g., R or Python) to approximate its properties.

```r
set.seed(500)
data <- arima.sim(n = 1e6, list(ar = 0.7, ma = 0.2))
```

##### Converting ARMA to Infinite Order Processes

**AR(∞) Representation**:

$$(1 - \phi B) X_t = (1 + \theta B) \epsilon_t$$

$$X_t = (1 - \phi B)^{-1} (1 + \theta B) \epsilon_t$$

$$X_t = [1 + \phi B + \phi^2 B^2 + \dots] (1 + \theta B) \epsilon_t$$

Multiplying the series:

$$X_t = [1 + (\phi + \theta) B + (\phi^2 + \phi \theta) B^2 + \dots] \epsilon_t$$

**MA(∞) Representation**:

$$X_t = \frac{1 + \theta B}{1 - \phi B} \epsilon_t = [1 + \psi_1 B + \psi_2 B^2 + \dots] \epsilon_t$$

Calculating $\psi$ coefficients:

$$\psi_k = \phi^k + \theta \phi^{k-1}$$

##### Theoretical Autocorrelations

The autocorrelation function (ACF) for an ARMA(1,1) process is:

$$\rho_k = \phi^k \left( \frac{1 + \phi \theta}{1 + 2 \phi \theta + \theta^2} \right)$$

Calculations:

$$\rho_1 = 0.7 \left( \frac{1 + 0.7 \times 0.2}{1 + 2 \times 0.7 \times 0.2 + 0.2^2} \right) \approx 0.777$$

$$\rho_2 = 0.7 \times \rho_1 \approx 0.544$$

$$\rho_3 = 0.7 \times \rho_2 \approx 0.381$$

##### Results and Interpretation

- The autocorrelations computed from the simulated data closely match the theoretical values, validating the model.
- The ARMA(1,1) model captures both the short-term dependencies (MA component) and the longer-term autocorrelation (AR component).

### Autoregressive Integrated Moving Average (ARIMA) Models

ARIMA models generalize ARMA models to include differencing, allowing them to model non-stationary time series data.

#### Mathematical Definition of ARIMA Models

An **ARIMA($p, d, q$)** model is defined by:

$$\phi(B) (1 - B)^d X_t = c + \theta(B) \epsilon_t$$

where:

- $\phi(B)$: Autoregressive polynomial.
- $\theta(B)$: Moving average polynomial.
- $d$: Order of differencing required to achieve stationarity.

#### Determining Differencing Order

- **Unit Root Tests**: Tests like the Augmented Dickey-Fuller (ADF) test assess whether differencing is needed.
- **Visual Inspection**: Time series plots reveal trends or changing variance.
- **ACF Analysis**: A slow decay in the ACF suggests non-stationarity.

#### Fitting ARIMA Models: Numerical Example

Suppose we have a time series $X_t$ exhibiting an upward trend.

##### Step 1: Differencing

First-order differencing is applied to achieve stationarity:

$$Y_t = (1 - B) X_t = X_t - X_{t-1}$$

##### Step 2: Model Identification

Analyzing the differenced series $Y_t$:

- **ACF**: Significant spikes at lag $q$ suggest an MA($q$) component.
- **PACF**: Significant spikes at lag $p$ suggest an AR($p$) component.

Assume ACF suggests MA(1) and PACF suggests AR(1).

##### Step 3: Parameter Estimation

Fit an ARIMA(1,1,1) model:

$$(1 - \phi B)(1 - B) X_t = c + (1 + \theta B) \epsilon_t$$

Estimate $\phi$, $\theta$, and $c$ using MLE.

##### Step 4: Model Diagnostics

- **Residual Analysis**: Plot residuals to check for randomness.
- **Ljung-Box Test**: Confirm absence of autocorrelation in residuals.
- **Information Criteria**: Compare AIC and BIC values for different models.

##### Step 5: Forecasting

Use the fitted model to forecast future values:

$$\hat{X}_{t+h} = c + \phi \hat{X}_{t+h-1} + \theta \hat{\epsilon}_{t+h-1}$$

### Seasonal ARIMA Processes (SARIMA)

Seasonal ARIMA (SARIMA) models are widely used for time series data exhibiting both trend and seasonal behaviors.

#### Mathematical Formulation

A **SARIMA($p, d, q \times P, D, Q$)$_s$** model incorporates both non-seasonal and seasonal factors:

$$\Phi_P(B^s) \phi_p(B) (1 - B^s)^D (1 - B)^d X_t = \Theta_Q(B^s) \theta_q(B) \epsilon_t$$

**Non-seasonal components** in time series models include several terms:  

- The **autoregressive (AR) polynomial**, represented as $\phi_p(B)$, captures the influence of past values on the current value.  
- The **differencing order**, $d$, represents the number of times the series is differenced to achieve stationarity.  
- The **moving average (MA) polynomial**, $\theta_q(B)$, models the impact of past forecast errors on the current value.  

**Seasonal components** extend these concepts to capture repeating patterns:  

- The **seasonal AR polynomial**, $\Phi_P(B^s)$, accounts for autoregressive effects at seasonal lags.  
- The **seasonal differencing order**, $D$, specifies the number of seasonal differences needed to remove seasonal trends.  
- The **seasonal MA polynomial**, $\Theta_Q(B^s)$, models the impact of seasonal forecast errors.  
- The **seasonal period**, $s$, defines the length of the seasonal cycle (e.g., 12 for monthly data).  

The **backshift operator** is used to reference previous values in the series:

- For **non-seasonal lags**, $BX_t = X_{t-1}$, indicating a one-period shift backward.  
- For **seasonal lags**, $B^sX_t = X_{t-s}$, referencing values from the same season in prior cycles.  
  
#### Examples of SARIMA Models

##### Example 1: SARIMA(1, 0, 0)(1, 0, 0)$_{12}$

**Model Equation**:

$$(1 - \phi_1 B)(1 - \Phi_1 B^{12}) X_t = \epsilon_t$$

- **Non-seasonal AR(1)**: $\phi_1 B X_t$
- **Seasonal AR(1) with period 12**: $\Phi_1 B^{12} X_t$
- **Interpretation**: Current value depends on the previous value and the value from 12 periods ago.
##### Example 2: SARIMA(0, 1, 1)(0, 1, 1)$_{4}$

**Model Equation**:

$$(1 - B)(1 - B^4) X_t = (1 + \theta_1 B)(1 + \Theta_1 B^4) \epsilon_t$$

- **First-order Non-seasonal Differencing**: $(1 - B) X_t$
- **First-order Seasonal Differencing with period 4**: $(1 - B^4) X_t$
- **Non-seasonal MA(1)**: $\theta_1 B \epsilon_t$
- **Seasonal MA(1)**: $\Theta_1 B^4 \epsilon_t$

##### Simplification and Expansion

**Non-seasonal Differencing**:

$$(1 - B) X_t = X_t - X_{t-1}$$

**Seasonal Differencing**:

$$(1 - B^s) X_t = X_t - X_{t-s}$$

**Combining Differencing**:

$$(1 - B)(1 - B^s) X_t = X_t - X_{t-1} - X_{t-s} + X_{t-s-1}$$

#### Stationarity and Invertibility Conditions

- **Stationarity**: All roots of $\phi_p(B)$ and $\Phi_P(B^s)$ polynomials must lie outside the unit circle.
- **Invertibility**: All roots of $\theta_q(B)$ and $\Theta_Q(B^s)$ polynomials must lie outside the unit circle.

#### Seasonal Differencing

- Removes seasonal trends to achieve stationarity.

**First-order Seasonal Differencing**:

$$\nabla_s X_t = X_t - X_{t-s}$$

**Second-order Seasonal Differencing**:
 
$$\nabla_s^2 X_t = X_t - 2 X_{t-s} + X_{t-2s}$$

#### Autocorrelation Function (ACF) of SARIMA Processes

The ACF of a SARIMA model displays patterns reflecting both seasonal and non-seasonal behavior.

##### Example: SARIMA(0, 0, 1)(0, 0, 1)$_{12}$

**Model Specification**:

$$X_t = \epsilon_t + \theta_1 \epsilon_{t-1} + \Theta_1 \epsilon_{t-12} + \theta_1 \Theta_1 \epsilon_{t-13}$$

**Parameters**:

- $\theta_1 = 0.7$
- $\Theta_1 = 0.6$

**Error Term**:

$\epsilon_t$: White noise with mean zero and variance $\sigma^2$

##### Calculating Autocovariances

I. **Variance ($\gamma_0$)**:

$$\gamma_0 = \text{Var}(X_t) = \sigma^2 \left(1 + \theta_1^2 + \Theta_1^2 + \theta_1^2 \Theta_1^2\right)$$

II. **Covariance at Lag 1 ($\gamma_1$)**:

$$\gamma_1 = \text{Cov}(X_t, X_{t-1}) = \sigma^2 \theta_1 \left(1 + \Theta_1^2\right)$$

III. **Covariance at Lag 12 ($\gamma_{12}$)**:

$$\gamma_{12} = \sigma^2 \Theta_1 \left(1 + \theta_1^2\right)$$

IV. **Covariance at Lag 13 ($\gamma_{13}$)**:

$$\gamma_{13} = \sigma^2 \theta_1 \Theta_1 \left(1 + \theta_1 \Theta_1\right)$$

##### Calculating Autocorrelations

**ACF at Lag $k$**:

$$\rho_k = \frac{\gamma_k}{\gamma_0}$$

- Significant spikes at lags that are multiples of the seasonal period ($s$) indicate seasonal correlations.
- Non-seasonal correlations are observed at lower lags.

#### Example: Monthly Airline Passenger Data

Consider a time series consisting of monthly airline passenger data. This particular time series is characterized by two distinct features: an upward trend indicating an increase in the number of passengers over time, and a seasonal pattern that repeats every 12 months, typically linked to factors such as holiday travel or seasonal tourism.

Steps to Model and Forecast the Time Series:

I. Decompose the Time Series into Trend, Seasonal, and Residual Components:

- Time series decomposition methods such as classical decomposition and STL decomposition can be applied to analyze the structure of a time series.  
- The decomposition process breaks down the original time series into three distinct components to enhance interpretability.  
- The **trend component** reveals the long-term direction of the data, indicating whether it is increasing, decreasing, or remaining stable over time.  
- The **seasonal component** highlights periodic patterns in the data, occurring at consistent intervals such as months, quarters, or years.  
- The **residual component** accounts for random fluctuations or noise that are not explained by the trend or seasonal patterns.

II. Detrend the Time Series Using Differencing or Transformation:

- Methods such as logarithmic transformation and differencing are useful for stabilizing the mean and variance of a time series.  
- **Differencing** involves subtracting the current value from the previous value, which helps remove trends and make the series stationary. Seasonal differencing adjusts for periodic patterns by subtracting the value from the same period in the previous cycle.  
- **Transformations** like logarithmic, square root, or Box-Cox are applied to stabilize variance and reduce heteroscedasticity in the time series. These techniques make it easier to model and analyze the data effectively.
  
III. Fit an Appropriate Model that Accounts for Both Trend and Seasonality:

- Models such as Seasonal ARIMA (SARIMA) and Exponential Smoothing State Space Model (ETS) are effective for forecasting time series data with seasonal patterns.  
- **SARIMA** extends the ARIMA model by incorporating seasonal terms, making it suitable for data with repeating seasonal behavior. It is defined by the parameters (p, d, q) for the non-seasonal part and (P, D, Q)s for the seasonal part, where "s" represents the seasonal frequency.  
- **ETS** combines error, trend, and seasonal components, making it useful for handling time series with stable seasonal patterns. It adapts to variations in the data and is flexible in modeling additive or multiplicative effects.

IV. Forecast Future Values Using the Fitted Model:

- Use the model to forecast future values.
- This step involves generating predictions based on the model's understanding of the trend and seasonal patterns in the historical data.
- Ensure to provide confidence intervals for these predictions to understand the potential variability in the forecasts.

![seasonality_forecast](https://github.com/djeada/Statistics-Notes/assets/37275728/218ec3bc-81a7-492e-a69b-3bf3d97ba8de)

- The **original data** is presented in blue, and the trend component is shown in orange, allowing for a clear visualization of long-term trends over time.  
- The **seasonal component** is depicted in green, illustrating the recurring patterns that occur periodically within the data.  
- The **differenced series** is represented in purple, demonstrating how differencing can transform the data to remove trends and achieve stationarity.  
- The **forecast versus actual values** plot combines the original series in blue and the forecasted values in red. Confidence intervals are shaded in black to indicate the forecast's uncertainty.  
