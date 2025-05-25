#### Q. What is a **time series**?

* [ ] A sequence of random variables
* [x] A set of data points recorded at regular intervals over time
* [ ] A type of linear regression model
* [ ] A random sample drawn from a population

#### Q. Which of the following is an example of **seasonality** in time series data?

* [ ] A gradual upward trend in sales over several years
* [x] Sales peaking every December due to holiday shopping
* [ ] A one-time spike in data due to a special event
* [ ] Random fluctuations in stock prices

#### Q. What is the purpose of **differencing** a time series?

* [ ] To remove seasonality
* [x] To make the time series stationary
* [ ] To forecast future values
* [ ] To smooth the time series

#### Q. In an **ARIMA(p, d, q)** model, what does the **d** parameter represent?

* [ ] The number of autoregressive terms
* [x] The number of differences needed to make the series stationary
* [ ] The number of moving-average terms
* [ ] The seasonal period

#### Q. Which plot would you examine to decide the AR order **p** when fitting an ARIMA model?

* [x] Partial Autocorrelation Function (PACF)
* [ ] Autocorrelation Function (ACF)
* [ ] Histogram of residuals
* [ ] Time-series decomposition plot

#### Q. What is the main purpose of **seasonal differencing** in a SARIMA model?

* [ ] To stabilize variance
* [ ] To remove the overall trend
* [x] To remove recurring seasonal patterns of period m
* [ ] To smooth random noise

#### Q. In a **SARIMA(p, d, q)×(P, D, Q)m** model, what does **P** control?

* [x] The number of seasonal autoregressive terms
* [ ] The seasonal differencing order
* [ ] The seasonal moving-average order
* [ ] The non-seasonal moving-average order

#### Q. What information criterion balances model fit against complexity when selecting ARIMA orders?

* [ ] R²
* [ ] Log-likelihood
* [x] AIC (Akaike Information Criterion)
* [ ] Durbin–Watson statistic

#### Q. Over-differencing an ARIMA model typically leads to:

* [ ] Underestimated parameter standard errors
* [x] Introduction of spurious MA terms and inflated variance
* [ ] Persistent autocorrelation in residuals
* [ ] Lower AIC values

#### Q. After fitting an ARIMA or SARIMA model, which diagnostic indicates residuals are still autocorrelated?

* [ ] Shapiro–Wilk test on residuals
* [x] Significant spikes in the ACF of residuals
* [ ] Constant variance in residuals over time
* [ ] Ljung–Box p-value > 0.05
#### Q. Which method is commonly used to **remove trend** in time series data?

* [ ] Exponential smoothing
* [x] Differencing
* [ ] Cross-validation
* [ ] Seasonal decomposition 

#### Q. How does **LSTM** differ from a traditional **RNN** in time series forecasting?

* [ ] LSTM models use moving averages instead of past values
* [x] LSTM can capture long-term dependencies by mitigating the vanishing gradient problem
* [ ] LSTM requires data to be stationary while RNN does not
* [ ] LSTM only works for seasonal data 

#### Q. Which technique is commonly used to **impute missing values** in a time series?

* [ ] Dropping the entire series
* [ ] Mean substitution across the full dataset
* [x] Interpolation or forward/backward fill
* [ ] Ignoring them during modeling 

#### Q. Which method provides a **robust evaluation** of time series models by respecting temporal ordering?

* [ ] Random k-fold cross-validation
* [ ] Leave-one-out cross-validation
* [x] Time Series Cross-Validation (e.g., TimeSeriesSplit)
* [ ] Bootstrapping 

#### Q. What is the key **difference** between an **ARIMA** and a **SARIMA** model?

* [ ] ARIMA includes seasonal terms; SARIMA does not
* [ ] SARIMA does not require differencing
* [x] SARIMA adds explicit seasonal AR, differencing, and MA components
* [ ] ARIMA can only model additive components 

#### Q. A standard **time series decomposition** splits data into which three components?

* [ ] Autoregression, Integration, Moving Average
* [ ] Trend, Autocorrelation, Residual
* [x] Trend, Seasonality, Residual (Noise)
* [ ] Mean, Median, Mode

#### Q. Which metric measures the **average absolute percentage error** in forecasts?

* [ ] MAE (Mean Absolute Error)
* [ ] MSE (Mean Squared Error)
* [ ] RMSE (Root Mean Squared Error)
* [x] MAPE (Mean Absolute Percentage Error) 

#### Q. What is the primary **purpose of time series cross-validation**?

* [ ] To remove seasonality from data
* [ ] To impute missing values
* [x] To assess model performance on unseen future data segments
* [ ] To test for stationarity

#### Q. What does the **“m”** in SARIMA(p, d, q)×(P, D, Q)m denote?

* [ ] The order of non-seasonal MA terms
* [ ] The total number of parameters
* [x] The seasonal period (e.g., 12 for monthly data)
* [ ] The number of differences applied

#### Q. In forecasting with ARIMA, the **prediction intervals** widen over longer horizons because:

* [ ] The model’s parameters change over time
* [x] Forecast uncertainty accumulates with each step ahead
* [ ] Seasonality increases at longer lags
* [ ] Residuals become more autocorrelated

#### Q. Which method automates ARIMA order selection by testing stationarity and minimizing AIC?

* [ ] Ljung–Box test
* [ ] Box–Cox transformation
* [x] auto.arima()
* [ ] KPSS test


#### Q. Which of the following is a characteristic of a **stationary time series**?

* [ ] The mean and variance change over time
* [x] It has a constant mean and variance over time
* [ ] It exhibits strong seasonality
* [ ] It shows an increasing trend over time

#### Q. What does the **autocorrelation function (ACF)** measure in a time series?

* [x] The correlation between a time series and a lagged version of itself
* [ ] The trend in the time series data
* [ ] The strength of the relationship between two different time series
* [ ] The forecast accuracy of a time series model

#### Q. In the context of time series, what is a **lag**?

* [ ] A delay in the data collection process
* [ ] The difference between actual and predicted values
* [x] A previous observation from the same time series
* [ ] A type of error in the time series model

#### Q. What is a **moving average** in time series analysis?

* [x] The average value of the most recent observations
* [ ] The long-term average of the entire time series
* [ ] The average of the forecasted values
* [ ] A method to calculate seasonality

#### Q. What is the main difference between an **AR (Autoregressive)** model and an **MA (Moving Average)** model in time series?

* [x] AR models use past values of the time series, while MA models use past forecast errors
* [ ] AR models are used for stationary time series, while MA models are used for non-stationary time series
* [ ] AR models predict future values, while MA models smooth the data
* [ ] AR models are used for seasonality, while MA models are used for trend

#### Q. What does the **partial autocorrelation function (PACF)** measure in time series?

* [ ] The total correlation between a time series and its lagged values
* [x] The correlation between a time series and a lag after removing the influence of intermediate lags
* [ ] The residuals of a time series model
* [ ] The difference between the actual and forecasted values

#### Q. Which time series model includes **both autoregressive and moving average components**?

* [x] ARMA model
* [ ] AR model
* [ ] MA model
* [ ] SARIMA model

#### Q. Which of the following is a **stationarity test** commonly used in time series analysis?

* [ ] ACF test
* [x] Augmented Dickey-Fuller (ADF) test
* [ ] Durbin-Watson test
* [ ] Z-test

#### Q. In a **SARIMA model**, what does the "S" stand for?

* [x] Seasonal
* [ ] Simple
* [ ] Stationary
* [ ] Smoothing

#### Q. What is the main purpose of **forecasting** in time series analysis?

* [ ] To determine if the time series is stationary
* [x] To predict future values based on past observations
* [ ] To calculate the correlation between two variables
* [ ] To remove seasonality from the data

#### Q. Which of the following is a method used to handle **seasonality** in time series forecasting?

* [ ] Differencing
* [ ] Exponential smoothing
* [x] Seasonal decomposition
* [ ] Box-Cox transformation

#### Q. In an **ARIMA(p, d, q)** model, what does the parameter **d** represent?

* [ ] The order of the autoregressive part
* [x] The number of differences needed to make the series stationary
* [ ] The order of the moving average part
* [ ] The seasonal period of the series

#### Q. What does the **p** parameter in **ARIMA(p, d, q)** control?

* [x] The number of lagged observations included (AR order)
* [ ] The number of differences
* [ ] The order of the moving average part
* [ ] The seasonal difference order

#### Q. In a **SARIMA(p, d, q)×(P, D, Q)m** model, what does **m** specify?

* [ ] The order of the moving average non-seasonal component
* [ ] The total number of parameters
* [x] The seasonal period (e.g., 12 for monthly data)
* [ ] The number of seasonal differences

#### Q. Which diagnostic plot is most commonly used to check the residuals of an ARIMA model for remaining autocorrelation?

* [ ] Histogram of residuals
* [ ] Time plot of original series
* [x] Autocorrelation Function (ACF) of residuals
* [ ] Scatter plot of residuals vs. time

#### Q. What is the purpose of **seasonal differencing** (D) in a SARIMA model?

* [ ] To remove trend in the data
* [x] To remove seasonal patterns of period m
* [ ] To stabilize the variance
* [ ] To improve model parsimony

#### Q. When selecting ARIMA orders via **AIC** or **BIC**, what are you trying to balance?

* [ ] Only the fit of the model to the data
* [ ] Only the number of parameters
* [x] Goodness of fit against model complexity
* [ ] The seasonal versus non-seasonal components

#### Q. In **auto.arima()** algorithms, what is the role of the **KPSS test**?

* [ ] To estimate moving average order q
* [ ] To detect outliers in the series
* [x] To test for stationarity and determine d
* [ ] To choose between AR and MA components

#### Q. What does **overdifferencing** in an ARIMA model typically cause?

* [ ] Underestimated standard errors
* [ ] Poor forecast accuracy only at long horizons
* [x] Introduction of moving average terms and increased variance
* [ ] Removal of all autocorrelation

#### Q. For a SARIMA(1,1,1)×(1,1,1)12 model, how many total difference operations are applied before fitting?

* [ ] 1
* [ ] 2
* [x] 2 (one non-seasonal and one seasonal difference)
* [ ] 3

#### Q. Which criterion indicates better model parsimony when comparing two ARIMA models?

* [ ] Higher AIC
* [ ] Higher log-likelihood
* [x] Lower BIC
* [ ] Lower number of parameters


#### Q. What does the **white noise** assumption imply in time series analysis?

* [x] The time series contains random fluctuations with no discernible pattern
* [ ] The time series follows a linear trend
* [ ] The residuals in the time series model are correlated
* [ ] The time series has a strong seasonal component

#### Q. What is the purpose of **exponential smoothing** in time series analysis?

* [x] To reduce the effect of random fluctuations in the data
* [ ] To model trends and seasonality
* [ ] To apply autoregressive models to the data
* [ ] To calculate residual errors in the time series

#### Q. Which of the following is **not** a component of a time series?

* [ ] Trend
* [ ] Seasonality
* [ ] Random noise
* [x] Multicollinearity

#### Q. In time series forecasting, what does **overfitting** refer to?

* [ ] Using too few data points to make predictions
* [x] A model that fits the training data well but performs poorly on new data
* [ ] A model that ignores seasonality in the data
* [ ] Smoothing the data too much, losing important information

#### Q. In a **seasonal decomposition of time series**, what are the typical components?

* [x] Trend, seasonality, and residual
* [ ] Mean, median, and mode
* [ ] Autoregression, moving average, and lag
* [ ] Stationary, non-stationary, and trend

#### Q. What does the **Box-Jenkins methodology** primarily focus on in time series analysis?

* [x] Identifying and estimating ARIMA models
* [ ] Decomposing time series into seasonal components
* [ ] Smoothing the time series using moving averages
* [ ] Conducting hypothesis testing on time series data
