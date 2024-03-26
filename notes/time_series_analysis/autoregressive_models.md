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

### Limitations

- **Assumption of Linearity**: AR models assume a linear relationship between past and current values, which may not hold in all scenarios.
- **Stationarity Requirement**: For an AR model to be valid, the time series should be stationary (constant mean and variance over time).
- **Error Term**: The unpredictability of the error term means that while we can make educated forecasts, there's always an element of uncertainty.
  
