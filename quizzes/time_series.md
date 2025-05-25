#### Q. What is a **time series**?

* [ ] `A sequence of random variables`
* [x] `A set of data points recorded at regular intervals over time`
* [ ] `A type of linear regression model`
* [ ] `A random sample drawn from a population`

#### Q. Which of the following is an example of **seasonality** in time series data?

* [ ] `A gradual upward trend in sales over several years`
* [x] `Sales peaking every December due to holiday shopping`
* [ ] `A one-time spike in data due to a special event`
* [ ] `Random fluctuations in stock prices`

#### Q. What is the purpose of **differencing** a time series?

* [ ] `To remove seasonality`
* [x] `To make the time series stationary`
* [ ] `To forecast future values`
* [ ] `To smooth the time series`

#### Q. Which of the following is a characteristic of a **stationary time series**?

* [ ] `The mean and variance change over time`
* [x] `It has a constant mean and variance over time`
* [ ] `It exhibits strong seasonality`
* [ ] `It shows an increasing trend over time`

#### Q. What does the **autocorrelation function (ACF)** measure in a time series?

* [x] `The correlation between a time series and a lagged version of itself`
* [ ] `The trend in the time series data`
* [ ] `The strength of the relationship between two different time series`
* [ ] `The forecast accuracy of a time series model`

#### Q. In the context of time series, what is a **lag**?

* [ ] `A delay in the data collection process`
* [ ] `The difference between actual and predicted values`
* [x] `A previous observation from the same time series`
* [ ] `A type of error in the time series model`

#### Q. What is a **moving average** in time series analysis?

* [x] `The average value of the most recent observations`
* [ ] `The long-term average of the entire time series`
* [ ] `The average of the forecasted values`
* [ ] `A method to calculate seasonality`

#### Q. What is the main difference between an **AR (Autoregressive)** model and an **MA (Moving Average)** model in time series?

* [x] `AR models use past values of the time series, while MA models use past forecast errors`
* [ ] `AR models are used for stationary time series, while MA models are used for non-stationary time series`
* [ ] `AR models predict future values, while MA models smooth the data`
* [ ] `AR models are used for seasonality, while MA models are used for trend`

#### Q. What does the **partial autocorrelation function (PACF)** measure in time series?

* [ ] `The total correlation between a time series and its lagged values`
* [x] `The correlation between a time series and a lag after removing the influence of intermediate lags`
* [ ] `The residuals of a time series model`
* [ ] `The difference between the actual and forecasted values`

#### Q. Which time series model includes **both autoregressive and moving average components**?

* [x] `ARMA model`
* [ ] `AR model`
* [ ] `MA model`
* [ ] `SARIMA model`

#### Q. Which of the following is a **stationarity test** commonly used in time series analysis?

* [ ] `ACF test`
* [x] `Augmented Dickey-Fuller (ADF) test`
* [ ] `Durbin-Watson test`
* [ ] `Z-test`

#### Q. In a **SARIMA model**, what does the "S" stand for?

* [x] `Seasonal`
* [ ] `Simple`
* [ ] `Stationary`
* [ ] `Smoothing`

#### Q. What is the main purpose of **forecasting** in time series analysis?

* [ ] `To determine if the time series is stationary`
* [x] `To predict future values based on past observations`
* [ ] `To calculate the correlation between two variables`
* [ ] `To remove seasonality from the data`

#### Q. Which of the following is a method used to handle **seasonality** in time series forecasting?

* [ ] `Differencing`
* [ ] `Exponential smoothing`
* [x] `Seasonal decomposition`
* [ ] `Box-Cox transformation`

#### Q. In an **ARIMA(p, d, q)** model, what does the parameter **d** represent?

* [ ] `The order of the autoregressive part`
* [x] `The number of differences needed to make the series stationary`
* [ ] `The order of the moving average part`
* [ ] `The seasonal period of the series`

#### Q. What does the **p** parameter in **ARIMA(p, d, q)** control?

* [x] `The number of lagged observations included (AR order)`
* [ ] `The number of differences`
* [ ] `The order of the moving average part`
* [ ] `The seasonal difference order`

#### Q. In a **SARIMA(p, d, q)×(P, D, Q)m** model, what does **m** specify?

* [ ] `The order of the moving average non-seasonal component`
* [ ] `The total number of parameters`
* [x] `The seasonal period (e.g., 12 for monthly data)`
* [ ] `The number of seasonal differences`

#### Q. Which diagnostic plot is most commonly used to check the residuals of an ARIMA model for remaining autocorrelation?

* [ ] `Histogram of residuals`
* [ ] `Time plot of original series`
* [x] `Autocorrelation Function (ACF) of residuals`
* [ ] `Scatter plot of residuals vs. time`

#### Q. What is the purpose of **seasonal differencing** (D) in a SARIMA model?

* [ ] `To remove trend in the data`
* [x] `To remove seasonal patterns of period m`
* [ ] `To stabilize the variance`
* [ ] `To improve model parsimony`

#### Q. When selecting ARIMA orders via **AIC** or **BIC**, what are you trying to balance?

* [ ] `Only the fit of the model to the data`
* [ ] `Only the number of parameters`
* [x] `Goodness of fit against model complexity`
* [ ] `The seasonal versus non-seasonal components`

#### Q. In **auto.arima()** algorithms, what is the role of the **KPSS test**?

* [ ] `To estimate moving average order q`
* [ ] `To detect outliers in the series`
* [x] `To test for stationarity and determine d`
* [ ] `To choose between AR and MA components`

#### Q. What does **overdifferencing** in an ARIMA model typically cause?

* [ ] `Underestimated standard errors`
* [ ] `Poor forecast accuracy only at long horizons`
* [x] `Introduction of moving average terms and increased variance`
* [ ] `Removal of all autocorrelation`

#### Q. For a SARIMA(1,1,1)×(1,1,1)12 model, how many total difference operations are applied before fitting?

* [ ] `1`
* [ ] `2`
* [x] `2 (one non-seasonal and one seasonal difference)`
* [ ] `3`

#### Q. Which criterion indicates better model parsimony when comparing two ARIMA models?

* [ ] `Higher AIC`
* [ ] `Higher log-likelihood`
* [x] `Lower BIC`
* [ ] `Lower number of parameters`


#### Q. What does the **white noise** assumption imply in time series analysis?

* [x] `The time series contains random fluctuations with no discernible pattern`
* [ ] `The time series follows a linear trend`
* [ ] `The residuals in the time series model are correlated`
* [ ] `The time series has a strong seasonal component`

#### Q. What is the purpose of **exponential smoothing** in time series analysis?

* [x] `To reduce the effect of random fluctuations in the data`
* [ ] `To model trends and seasonality`
* [ ] `To apply autoregressive models to the data`
* [ ] `To calculate residual errors in the time series`

#### Q. Which of the following is **not** a component of a time series?

* [ ] `Trend`
* [ ] `Seasonality`
* [ ] `Random noise`
* [x] `Multicollinearity`

#### Q. In time series forecasting, what does **overfitting** refer to?

* [ ] `Using too few data points to make predictions`
* [x] `A model that fits the training data well but performs poorly on new data`
* [ ] `A model that ignores seasonality in the data`
* [ ] `Smoothing the data too much, losing important information`

#### Q. In a **seasonal decomposition of time series**, what are the typical components?

* [x] `Trend, seasonality, and residual`
* [ ] `Mean, median, and mode`
* [ ] `Autoregression, moving average, and lag`
* [ ] `Stationary, non-stationary, and trend`

#### Q. What does the **Box-Jenkins methodology** primarily focus on in time series analysis?

* [x] `Identifying and estimating ARIMA models`
* [ ] `Decomposing time series into seasonal components`
* [ ] `Smoothing the time series using moving averages`
* [ ] `Conducting hypothesis testing on time series data`
