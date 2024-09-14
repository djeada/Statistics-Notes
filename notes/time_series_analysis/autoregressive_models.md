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

---

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

## Autoregressive Moving Average (ARMA) Models

ARMA models combine autoregressive (AR) and moving average (MA) components to model time series data exhibiting both autocorrelation and serial dependence.

### Mathematical Definition of ARMA Models

An **ARMA(\( p, q \))** model is defined by:

\[
X_t = c + \sum_{i=1}^{p} \phi_i X_{t-i} + \epsilon_t + \sum_{j=1}^{q} \theta_j \epsilon_{t-j}
\]

or, equivalently, using the backshift operator \( B \):

\[
\phi(B) X_t = c + \theta(B) \epsilon_t
\]

where:

- \( \phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p \)
- \( \theta(B) = 1 + \theta_1 B + \theta_2 B^2 + \dots + \theta_q B^q \)

### Key Concepts

#### Stationarity of AR Processes

An AR(\( p \)) process is **stationary** if all the roots of the characteristic polynomial \( \phi(B) = 0 \) lie outside the unit circle in the complex plane. This condition ensures that the time series has a constant mean and variance over time.

#### Invertibility of MA Processes

An MA(\( q \)) process is **invertible** if all the roots of \( \theta(B) = 0 \) lie outside the unit circle. Invertibility allows the MA process to be expressed as an infinite AR process, ensuring a unique representation and facilitating parameter estimation.

#### Infinite Order Representations

- **AR(∞) Representation of MA Processes**:

  An MA process can be expressed as an infinite-order AR process:

  \[
  X_t = \sum_{k=1}^{\infty} \pi_k X_{t-k} + \epsilon_t
  \]

- **MA(∞) Representation of AR Processes**:

  An AR process can be expressed as an infinite-order MA process:

  \[
  X_t = \sum_{k=0}^{\infty} \psi_k \epsilon_{t-k}
  \]

### Example: ARMA(1,1) Process

Consider the ARMA(1,1) model:

\[
X_t = \phi X_{t-1} + \epsilon_t + \theta \epsilon_{t-1}
\]

Let \( \phi = 0.7 \), \( \theta = 0.2 \), and \( \epsilon_t \) is white noise.

#### Simulation

To analyze this process, we simulate a large number of observations using statistical software (e.g., R or Python) to approximate its properties.

```r
set.seed(500)
data <- arima.sim(n = 1e6, list(ar = 0.7, ma = 0.2))
```

#### Converting ARMA to Infinite Order Processes

- **AR(∞) Representation**:

  \[
  \begin{align*}
  (1 - \phi B) X_t &= (1 + \theta B) \epsilon_t \\
  X_t &= (1 - \phi B)^{-1} (1 + \theta B) \epsilon_t \\
  X_t &= [1 + \phi B + \phi^2 B^2 + \dots] (1 + \theta B) \epsilon_t \\
  \end{align*}
  \]

  Multiplying the series:

  \[
  X_t = [1 + (\phi + \theta) B + (\phi^2 + \phi \theta) B^2 + \dots] \epsilon_t
  \]

- **MA(∞) Representation**:

  \[
  X_t = \frac{1 + \theta B}{1 - \phi B} \epsilon_t = [1 + \psi_1 B + \psi_2 B^2 + \dots] \epsilon_t
  \]

  Calculating \( \psi \) coefficients:

  \[
  \psi_k = \phi^k + \theta \phi^{k-1}
  \]

#### Theoretical Autocorrelations

The autocorrelation function (ACF) for an ARMA(1,1) process is:

\[
\rho_k = \phi^k \left( \frac{1 + \phi \theta}{1 + 2 \phi \theta + \theta^2} \right)
\]

Calculations:

\[
\begin{align*}
\rho_1 &= 0.7 \left( \frac{1 + 0.7 \times 0.2}{1 + 2 \times 0.7 \times 0.2 + 0.2^2} \right) \approx 0.777 \\
\rho_2 &= 0.7 \times \rho_1 \approx 0.544 \\
\rho_3 &= 0.7 \times \rho_2 \approx 0.381 \\
\end{align*}
\]

#### Results and Interpretation

- **Empirical ACF**: The autocorrelations computed from the simulated data closely match the theoretical values, validating the model.
- **Model Behavior**: The ARMA(1,1) model captures both the short-term dependencies (MA component) and the longer-term autocorrelation (AR component).

---

## Autoregressive Integrated Moving Average (ARIMA) Models

ARIMA models generalize ARMA models to include differencing, allowing them to model non-stationary time series data.

### Mathematical Definition of ARIMA Models

An **ARIMA(\( p, d, q \))** model is defined by:

\[
\phi(B) (1 - B)^d X_t = c + \theta(B) \epsilon_t
\]

where:

- \( \phi(B) \): Autoregressive polynomial.
- \( \theta(B) \): Moving average polynomial.
- \( d \): Order of differencing required to achieve stationarity.

### Determining Differencing Order

- **Unit Root Tests**: Tests like the Augmented Dickey-Fuller (ADF) test assess whether differencing is needed.
- **Visual Inspection**: Time series plots reveal trends or changing variance.
- **ACF Analysis**: A slow decay in the ACF suggests non-stationarity.

### Fitting ARIMA Models: Numerical Example

Suppose we have a time series \( X_t \) exhibiting an upward trend.

#### Step 1: Differencing

First-order differencing is applied to achieve stationarity:

\[
Y_t = (1 - B) X_t = X_t - X_{t-1}
\]

#### Step 2: Model Identification

Analyzing the differenced series \( Y_t \):

- **ACF**: Significant spikes at lag \( q \) suggest an MA(\( q \)) component.
- **PACF**: Significant spikes at lag \( p \) suggest an AR(\( p \)) component.

Assume ACF suggests MA(1) and PACF suggests AR(1).

#### Step 3: Parameter Estimation

Fit an ARIMA(1,1,1) model:

\[
(1 - \phi B)(1 - B) X_t = c + (1 + \theta B) \epsilon_t
\]

Estimate \( \phi \), \( \theta \), and \( c \) using MLE.

#### Step 4: Model Diagnostics

- **Residual Analysis**: Plot residuals to check for randomness.
- **Ljung-Box Test**: Confirm absence of autocorrelation in residuals.
- **Information Criteria**: Compare AIC and BIC values for different models.

#### Step 5: Forecasting

Use the fitted model to forecast future values:

\[
\hat{X}_{t+h} = c + \phi \hat{X}_{t+h-1} + \theta \hat{\epsilon}_{t+h-1}
\]

## Limitations of AR and ARIMA Models

- **Linearity Assumption**: AR and ARIMA models assume linear relationships, which may not capture nonlinear dynamics.
- **Stationarity Requirement**: Accurate modeling requires stationarity; real-world data often violate this assumption.
- **Parameter Estimation Sensitivity**: Estimates can be sensitive to outliers and model specification.
- **Model Selection Complexity**: Choosing appropriate \( p \), \( d \), and \( q \) values is non-trivial and may require expert judgment.
- **Overfitting Risk**: Overly complex models may fit the noise rather than the underlying process, reducing predictive performance.
