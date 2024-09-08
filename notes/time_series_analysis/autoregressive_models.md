## Autoregressive Models

Autoregressive (AR) models are a type of linear model used for time series forecasting. They predict future values of the time series using a linear combination of past values. The order of an AR model, denoted as p, represents the number of past values (lags) used as predictors.

### Autoregressive Model Equation

An AR(p) model can be represented by the following equation:

$$
X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \cdots + \phi_p X_{t-p} + \epsilon_t
$$

where:

- $X_t$: The value of the time series at time t
- $c$: A constant term
- $\phi_i$: The autoregressive coefficient for the i-th lag
- $X_{t-i}$: The value of the time series at time t-i (i-th lag)
- $\epsilon_t$: The error term at time t

### Estimating AR Model Parameters

The parameters of an AR model (constant term and autoregressive coefficients) can be estimated using methods such as least squares, maximum likelihood, or Bayesian techniques.

### Model Selection

The order p of the AR model is a critical choice. Common methods for selecting the order include:

1. **Akaike Information Criterion (AIC)**: A measure that takes into account both the goodness of fit and the complexity of the model. Lower AIC values indicate better models.
2. **Bayesian Information Criterion (BIC)**: Similar to AIC, but with a stronger penalty for model complexity. Lower BIC values indicate better models.
3. **Partial autocorrelation function (PACF)**: A plot of the partial autocorrelation coefficients for different lags. The lag at which the PACF drops to zero or below a significance threshold can be used as the order of the AR model.

## Example: AR(2) Model in Time Series Forecasting

Consider an AR model of order 2, known as AR(2). This model assumes that the value at a particular time point is a linear function of the two preceding values, plus some error term. The general form of an AR(2) model is:

$$
X_t = \alpha + \beta_1X_{t-1} + \beta_2X_{t-2} + \epsilon_t
$$

where:
- $X_t$ is the value at time $t$.
- $\alpha$ is the intercept.
- $\beta_1, \beta_2$ are coefficients for the lagged values.
- $\epsilon_t$ is the error term at time $t$.

Suppose we have an AR(2) model with the following equation:

$$
X_t = 3 + 0.6X_{t-1} - 0.2X_{t-2} + \epsilon_t
$$

Given Data:

- Past value $X_{t-1} = 10$
- Past value $X_{t-2} = 5$

To predict the value of $X_t$, we use the AR(2) equation:

$$
X_t = 3 + 0.6(10) - 0.2(5) + \epsilon_t = 8 + \epsilon_t
$$

Interpretation:

- **Base Calculation**: The predicted value without considering the error term is 8. 
- **Error Term ($\epsilon_t$)**: This represents random fluctuations, noise, or unexpected events affecting the value at time $t$.
- **Prediction**: The actual predicted value of $X_t$ will be 8 plus whatever value $\epsilon_t$ takes. If $\epsilon_t$ is a random variable with mean 0, the expected value of $X_t$ is 8.

![ar2_model](https://github.com/djeada/Statistics-Notes/assets/37275728/9cc88c5a-174a-4503-a9cb-a20c43e26ab7)

- The blue line represents the original mock data generated to simulate a time series following an AR(2) process.
- The red dashed line shows the predictions made by the fitted AR(2) model.

This visualization illustrates how the AR(2) model captures the underlying pattern of the time series. The model uses the two most recent values to make predictions, adjusting to the trends and fluctuations in the data. 

## ARMA

#### Key Concepts

1. **Invertibility of MA(q) Processes:**
   - An MA(q) process is invertible if the roots of the polynomial \( \theta(B) = \theta_0 + \theta_1B + \cdots + \theta_qB^q \) lie outside the unit circle. This ensures a unique representation in terms of the ACF and the \( \beta \) coefficients.

2. **Stationarity of AR(p) Processes:**
   - An AR(p) process is stationary if the roots of \( \phi(B) = 1 - \phi_1B - \phi_2B^2 - \cdots - \phi_pB^p \) lie outside the unit circle.

3. **ARMA Processes:**
   - An ARMA(p, q) process combines autoregressive and moving average components. Its general form is:
     \[
     \phi(B) X_t = \theta(B) Z_t
     \]
     where \( \phi(B) \) represents the AR part, \( \theta(B) \) represents the MA part, and \( Z_t \) is white noise.

4. **Infinite Order Representations:**
   - An ARMA(p, q) process can be expressed as an infinite-order MA(∞) or AR(∞) process using:
     - MA(∞): \( \psi(B) Z_t = X_t \), where \( \psi(B) = \frac{\theta(B)}{\phi(B)} \)
     - AR(∞): \( \pi(B) X_t = Z_t \), where \( \pi(B) = \frac{\phi(B)}{\theta(B)} \)

#### Example: ARMA(1,1) Process

Consider the ARMA(1,1) process:
\[ X_t = 0.7 X_{t-1} + Z_t + 0.2 Z_{t-1} \]

**Simulation:**

```r
rm(list=ls(all=TRUE))
set.seed(500)
data = arima.sim(list(order = c(1,0,1), ar = .7, ma = .2), n = 1000000)
par(mfcol = c(3,1))
plot(data, main="ARMA(1,1) Time Series: phi1=.7, theta1=.2", xlim=c(0,400))
acf(data, main="Autocorrelation of ARMA(1,1), phi1=.7, theta1=.2")
acf(data, type="partial", main="Partial Autocorrelation of ARMA(1,1), phi1=.7, theta1=.2")
```

**Mixed ARMA to Autoregressive:**

To express the ARMA(1,1) as an autoregressive process, rewrite:
\[ (1 - 0.7B) X_t = (1 + 0.2B) Z_t \]
Then:
\[ \pi(B) = \frac{\phi(B)}{\theta(B)} = \frac{1 - 0.7B}{1 + 0.2B} \]

Using a geometric series expansion:
\[ \pi(B) = (1 - 0.7B) \cdot (1 - 0.2B + 0.04B^2 - \cdots) \]
\[ \pi(B) = 1 - 0.9B + 0.18B^2 - 0.036B^3 + \cdots \]

**Mixed ARMA to Moving Average:**

To express the ARMA(1,1) as a moving average process:
\[ \psi(B) = \frac{\theta(B)}{\phi(B)} = \frac{1 + 0.2B}{1 - 0.7B} \]
Expanding this:
\[ \psi(B) = (1 + 0.2B) \cdot (1 + 0.7B + 0.49B^2 + \cdots) \]
\[ \psi(B) = 1 + 0.9B + 0.63B^2 + 0.441B^3 + \cdots \]

#### Results

For the ARMA(1,1) process with \( \phi_1 = 0.7 \) and \( \theta_1 = 0.2 \), the theoretical and simulated autocorrelations should match closely, verifying the accuracy of our models.

**Theoretical Autocorrelations:**
\[
\begin{align*}
\rho(1) &= \frac{1 + \phi \theta}{1 + \theta^2 + 2\phi \theta} = 0.777 \\
\rho(2) &= \phi \cdot \rho(1) = 0.544 \\
\rho(3) &= \phi \cdot \rho(2) = 0.381 \\
\rho(4) &= \phi \cdot \rho(3) = 0.267
\end{align*}
\]

**Empirical Autocorrelations from Simulation:**
\[
\begin{align*}
r(1) &= 0.777 \\
r(2) &= 0.544 \\
r(3) &= 0.380 \\
r(4) &= 0.266
\end{align*}
\]

These results confirm that the theoretical models align well with simulated data, showing the consistency and accuracy of the ARMA process estimations.

### ARMA Model Overview
- **ARMA (AutoRegressive Moving Average)** models combine elements of both Autoregressive (AR) and Moving Average (MA) processes.
- The general ARMA(p, q) model is expressed as:
  \[
  X_t = Z_t + \phi_1 X_{t-1} + \ldots + \phi_p X_{t-p} + \theta_1 Z_{t-1} + \ldots + \theta_q Z_{t-q}
  \]
  where \(Z_t\) represents noise.

### Example with Scientific Discoveries Data
1. **Data Visualization**:
   - The `discoveries` data set contains the number of major scientific discoveries per year.
   - **Plots**:
     - `plot(discoveries)` shows the time series plot.
     - `stripchart(discoveries)` provides a dot plot of the data.

2. **ACF and PACF Analysis**:
   - **ACF (Autocorrelation Function)** and **PACF (Partial Autocorrelation Function)** plots are used to determine potential AR and MA terms.
   - The ACF plot shows three significant spikes, suggesting the possibility of an MA component.
   - The PACF plot indicates one or two spikes, suggesting the possibility of an AR component.

3. **Model Fitting**:
   - Several ARMA models were fit to the data with different values for \(p\) and \(q\).
   - **AIC (Akaike Information Criterion)** values for different models are compared to assess model quality. Lower AIC values indicate a better model fit.

   **Calculated AIC Values**:
   - ARMA(0,0,1): AIC = 445.59
   - ARMA(0,0,2): AIC = 444.67
   - ARMA(0,0,3): AIC = 441.32
   - ARMA(1,0,0): AIC = 443.38
   - ARMA(1,0,1): AIC = 440.20
   - ARMA(1,0,2): AIC = 442.04
   - ARMA(2,0,0): AIC = 441.62
   - ARMA(2,0,1): AIC = 442.07
   - ARMA(3,0,0): AIC = 441.57
   - ARMA(3,0,1): AIC = 443.57

   The ARMA(1,0,1) model has the lowest AIC, suggesting it is a good fit based on parsimony (simplicity) and AIC.

4. **Automatic Model Selection**:
   - **`auto.arima()`**: This R function automates the ARMA model selection process.
   - When `approximation=FALSE`, `auto.arima()` suggests ARMA(2,0,0).
   - When `approximation=TRUE`, it suggests ARMA(1,0,1).
   - The choice of model may depend on whether approximation is used and which information criterion is prioritized (AIC, BIC, etc.).

   **Automatic Model Outputs**:
   - For AIC with approximation FALSE: ARMA(2,0,0)
   - For AIC with approximation TRUE: ARMA(1,0,1)
   - For BIC (with approximation FALSE): ARMA(1,0,1)
   - For AICc (with approximation FALSE): ARMA(1,0,1)

### ARIMA

#### 1. **ARMA (Autoregressive Moving Average) Processes**
- **General Form**: An ARMA(p, q) process combines autoregressive (AR) and moving average (MA) components to model stationary time series data. It is written as:
  \[
  X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + \ldots + \phi_p X_{t-p} + Z_t + \theta_1 Z_{t-1} + \theta_2 Z_{t-2} + \ldots + \theta_q Z_{t-q}
  \]
  where:
  - \(X_t\) is the time series value at time \(t\),
  - \(Z_t\) is white noise (zero mean, constant variance),
  - \(\phi_1, \ldots, \phi_p\) are AR coefficients, and
  - \(\theta_1, \ldots, \theta_q\) are MA coefficients.

- **Backshift and Difference Operators**:
  - **Backshift Operator** \( B \): \(B X_t = X_{t-1}\), so powers of \(B\) correspond to lagging time series data: \(B^k X_t = X_{t-k}\).
  - **Difference Operator** \( \nabla \): Used for differencing to address non-stationarity, defined as \( \nabla X_t = X_t - X_{t-1} = (1 - B) X_t\).

- **ARMA as a Polynomial Representation**: 
  The ARMA model can be written using backshift notation:
  \[
  \phi(B) X_t = \theta(B) Z_t
  \]
  where:
  \[
  \phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \ldots - \phi_p B^p
  \]
  and
  \[
  \theta(B) = 1 + \theta_1 B + \theta_2 B^2 + \ldots + \theta_q B^q.
  \]

- **Stationarity and Invertibility**:
  - The ARMA process is **stationary** if all the roots of the AR polynomial \(\phi(z)\) lie outside the unit circle in the complex plane. This ensures that the series does not exhibit an explosive behavior.
  - The process is **invertible** if the roots of the MA polynomial \(\theta(z)\) also lie outside the unit circle, allowing past white noise terms to be reconstructed from observed data.

#### 2. **ARIMA (Autoregressive Integrated Moving Average) Processes**
- **Definition**: An ARIMA(p, d, q) process generalizes ARMA to handle non-stationary time series by differencing \(d\) times. The general form is:
  \[
  \phi(B) \nabla^d X_t = \theta(B) Z_t
  \]
  where:
  - \(\nabla^d = (1 - B)^d\) is the differencing operator applied \(d\) times to achieve stationarity.

- **ARIMA Components**:
  - **p**: Autoregressive order (number of lag terms),
  - **d**: Degree of differencing (number of times the series is differenced to become stationary),
  - **q**: Moving average order (number of lagged error terms).

#### 3. **Determining Differencing Order**
- **Unit Root Test**: 
  A non-stationary series exhibits a unit root, detectable by:
  - Slowly decaying ACF, indicating persistence in the series.
  - **Dickey-Fuller Test**: A formal statistical test to determine whether differencing is needed.

- **Trend and Variance Considerations**:
  - If the series has a **trend**, differencing is recommended.
  - If there is **heteroscedasticity** (variance changes over time), a log transformation may stabilize the variance before differencing.

### Fitting ARIMA Models to Data: Numerical Example

#### Example 1: Simulated Time Series
Let's assume a synthetic dataset that shows a clear upward trend, requiring one level of differencing (d = 1) to achieve stationarity.

1. **Data Generation**:
   Suppose the time series follows the process:
   \[
   X_t = 0.7 X_{t-1} + Z_t + 0.5 Z_{t-1}
   \]
   where \( Z_t \sim N(0,1) \). This is an ARMA(1,1) process.

2. **Differencing**:
   After differencing once to remove the trend, the differenced series becomes:
   \[
   \nabla X_t = X_t - X_{t-1}
   \]
   We fit an ARIMA(1, 1, 1) model.

3. **Model Fitting**:
   After estimating parameters for ARIMA(1,1,1), we might arrive at:
   \[
   (1 - 0.6 B) \nabla X_t = Z_t + 0.4 Z_{t-1}
   \]
   The estimated AR and MA coefficients (\(\hat{\phi} = 0.6\) and \(\hat{\theta} = 0.4\)) suggest moderate autocorrelation and noise in the system.

#### 4. **Model Evaluation**:
- **ACF and PACF**:
  - **ACF** helps identify the order of the moving average (MA) part by observing where the ACF cuts off.
  - **PACF** helps determine the autoregressive (AR) order by examining where the PACF cuts off.
  
  In this example, the ACF decays slowly, indicating the need for differencing (d=1), and the PACF cuts off after lag 1, suggesting AR(1).

- **Model Selection Criteria**:
  - **Akaike Information Criterion (AIC)**: A lower AIC indicates a better-fitting model.
  - **Bayesian Information Criterion (BIC)**: Also used for model comparison, penalizing for model complexity.

- **Residual Diagnostics**:
  - **Ljung-Box Test**: Evaluates whether residuals from the fitted model exhibit autocorrelation. If the p-value is small, there’s evidence of autocorrelation, indicating a poorly fit model.

### Example 2: Forecasting

Once the ARIMA model is fitted, we can use it to forecast future values. For an ARIMA(1,1,1) model with estimated parameters, the forecast equation is:
\[
\hat{X}_{t+1} = 0.6 \hat{X}_t + 0.4 \hat{Z}_t
\]
where \(\hat{Z}_t\) represents the error term estimated from the residuals. The forecast combines lagged observations and past errors to predict the next value.




### Limitations

- **Assumption of Linearity**: AR models assume a linear relationship between past and current values, which may not hold in all scenarios.
- **Stationarity Requirement**: For an AR model to be valid, the time series should be stationary (constant mean and variance over time).
- **Error Term**: The unpredictability of the error term means that while we can make educated forecasts, there's always an element of uncertainty.
  
