## Autoregressive (AR) Models in Time Series Analysis

Autoregressive (AR) models are fundamental tools in time series analysis, used to describe and forecast time-dependent data. An AR model predicts future values based on a linear combination of past observations. The order of an AR model, denoted as \( p \), indicates how many lagged past values are used.

### Mathematical Definition of AR Models

An **Autoregressive model of order \( p \)**, denoted as AR(\( p \)), is defined by the equation:

\[
X_t = c + \sum_{i=1}^{p} \phi_i X_{t-i} + \epsilon_t
\]

where:

- \( X_t \): The value of the time series at time \( t \).
- \( c \): A constant term (intercept).
- \( \phi_i \): Autoregressive coefficients for lag \( i \).
- \( X_{t-i} \): The value of the time series at lag \( i \).
- \( \epsilon_t \): White noise error term at time \( t \), assumed to be independently and identically distributed with mean zero and constant variance \( \sigma^2 \).

### Properties of AR Models

- **Stationarity**: An AR model is stationary if the roots of its characteristic equation lie outside the unit circle in the complex plane. For an AR(1) model, stationarity requires \(|\phi_1| < 1\).
- **Autocorrelation Function (ACF)**: The ACF of an AR model declines exponentially or in a damped sinusoidal pattern.
- **Partial Autocorrelation Function (PACF)**: The PACF of an AR(\( p \)) model cuts off after lag \( p \).

### Estimation of Parameters

Parameters \( c \) and \( \phi_i \) can be estimated using methods such as:

- **Least Squares Estimation**: Minimizes the sum of squared residuals.
- **Yule-Walker Equations**: Utilizes autocorrelations to solve for parameters.
- **Maximum Likelihood Estimation (MLE)**: Based on the likelihood function of the observed data.

### Model Selection

Selecting the appropriate order \( p \) is crucial. Common criteria include:

- **Akaike Information Criterion (AIC)**:

  \[
  \text{AIC} = -2 \ln(L) + 2k
  \]

- **Bayesian Information Criterion (BIC)**:

  \[
  \text{BIC} = -2 \ln(L) + k \ln(n)
  \]

where:

- \( L \): The maximized value of the likelihood function.
- \( k \): The number of estimated parameters.
- \( n \): The number of observations.

Lower values of AIC or BIC indicate a better model, balancing goodness of fit and model complexity.

## Example: AR(2) Model in Time Series Forecasting

Consider an AR model of order 2, denoted as AR(2). This model assumes that the value at a particular time point is a linear function of the two preceding values, plus some error term.

### AR(2) Model Equation

The AR(2) model is given by:

\[
X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \epsilon_t
\]

Suppose we have:

- \( c = 3 \)
- \( \phi_1 = 0.6 \)
- \( \phi_2 = -0.2 \)
- Past observations: \( X_{t-1} = 10 \), \( X_{t-2} = 5 \)

#### Calculation

Plugging the values into the AR(2) equation:

\[
\begin{align*}
X_t &= 3 + 0.6 \times 10 - 0.2 \times 5 + \epsilon_t \\
&= 3 + 6 - 1 + \epsilon_t \\
&= 8 + \epsilon_t
\end{align*}
\]

#### Interpretation

- **Deterministic Part**: The expected value of \( X_t \) given past observations is 8.
- **Stochastic Part**: \( \epsilon_t \) represents random fluctuations (white noise).
- **Prediction**: The forecasted value of \( X_t \) is 8, with variability introduced by \( \epsilon_t \).

### Visualization

![ar2_model](https://github.com/djeada/Statistics-Notes/assets/37275728/9cc88c5a-174a-4503-a9cb-a20c43e26ab7)

- The blue line represents the original mock data generated to simulate a time series following an AR(2) process.
- The red dashed line shows the predictions made by the fitted AR(2) model.

This visualization illustrates how the AR(2) model captures the underlying pattern of the time series. The model uses the two most recent values to make predictions, adjusting to the trends and fluctuations in the data. 

## Limitations of AR Models

- **Linearity Assumption**: AR and ARIMA models assume linear relationships, which may not capture nonlinear dynamics.
- **Stationarity Requirement**: Accurate modeling requires stationarity; real-world data often violate this assumption.
- **Parameter Estimation Sensitivity**: Estimates can be sensitive to outliers and model specification.
- **Model Selection Complexity**: Choosing appropriate \( p \), \( d \), and \( q \) values is non-trivial and may require expert judgment.
- **Overfitting Risk**: Overly complex models may fit the noise rather than the underlying process, reducing predictive performance.
