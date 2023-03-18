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

### Example: AR(2) Model

Suppose we have an AR(2) model with the following equation:

$$
X_t = 3 + 0.6X_{t-1} - 0.2X_{t-2} + \epsilon_t
$$

If we have the past values $X_{t-1} = 10$ and $X_{t-2} = 5$, we can predict the value of $X_t$ as follows:

$$
X_t = 3 + 0.6(10) - 0.2(5) + \epsilon_t = 8 + \epsilon_t
$$

### Estimating AR Model Parameters

The parameters of an AR model (constant term and autoregressive coefficients) can be estimated using methods such as least squares, maximum likelihood, or Bayesian techniques.

### Model Selection

The order p of the AR model is a critical choice. Common methods for selecting the order include:
1. Akaike Information Criterion (AIC): A measure that takes into account both the goodness of fit and the complexity of the model. Lower AIC values indicate better models.
2. Bayesian Information Criterion (BIC): Similar to AIC, but with a stronger penalty for model complexity. Lower BIC values indicate better models.
3. Partial autocorrelation function (PACF): A plot of the partial autocorrelation coefficients for different lags. The lag at which the PACF drops to zero or below a significance threshold can be used as the order of the AR model.

### Limitations

1. AR models assume a linear relationship between past and future values, which may not hold for all time series data.
2. AR models may not be appropriate for time series with strong seasonal or cyclical patterns.
