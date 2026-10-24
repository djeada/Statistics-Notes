# Time Series Quiz

Notes: [Time Series](../notes/time_series/time_series.md), [Stationarity](../notes/time_series/stationarity.md), [White Noise](../notes/time_series/stochastic_processes_and_white_noise.md), [Random Walk](../notes/time_series/random_walk.md), [Autocorrelation Function](../notes/time_series/autocorrelation_function.md), [Backward Shift Operator](../notes/time_series/backward_shift_operator.md), [AR Models](../notes/time_series/autoregressive_models.md), [MA Models](../notes/time_series/moving_average_models.md), [Invertibility](../notes/time_series/invertibility.md), [ARIMA Models](../notes/time_series/arima_models.md), [Seasonality and Trends](../notes/time_series/seasonality_and_trends.md), [Randomness Tests](../notes/time_series/randomness_tests.md), [Forecasting](../notes/time_series/forecasting.md), [Forecast Evaluation](../notes/time_series/forecast_evaluation.md), [Financial Models](../notes/time_series/financial_time_series_models.md), [Multivariate Time Series](../notes/time_series/multivariate_time_series.md), [State-Space Models](../notes/time_series/state_space_models.md), [Frequency-Domain Analysis](../notes/time_series/frequency_domain_analysis.md)

Check your understanding of stationarity, autocorrelation, ARIMA-type models, forecasting and forecast evaluation.

#### Q. What is a **time series**?

* [ ] A random sample of independent observations from a population
* [x] A sequence of observations of a variable indexed in time order
* [ ] A type of linear regression model with lagged predictors
* [ ] A set of measurements on many units taken at one moment

> **Explanation:** What makes data a time series is the time ordering, usually at regular intervals. Nearby observations are typically dependent, unlike an i.i.d. sample. Measurements on many units at one moment are cross-sectional data.

#### Q. Which of the following is an example of **seasonality**?

* [ ] A gradual upward trend in sales over several years
* [x] Sales peaking every December because of holiday shopping
* [ ] A one-time spike in sales caused by a special event
* [ ] Day-to-day random fluctuations in a stock price

> **Explanation:** Seasonality is a pattern that repeats with a fixed, known period, here 12 months. A long-run drift is a trend and a one-off spike is an outlier or intervention.

#### Q. What is **first differencing**, $y_t - y_{t-1}$, mainly used for?

* [ ] Removing a repeating pattern with a period of 12
* [x] Removing a trend or unit root so the mean becomes stationary
* [ ] Stabilising a variance that grows with the level of the series
* [ ] Smoothing out high-frequency noise for plotting

> **Explanation:** Differencing turns a random walk or a linear trend into a series with a stable mean. Seasonal patterns need lag-$m$ differencing, and a variance that grows with the level calls for a log or Box–Cox transform.

#### Q. In an **ARIMA(p, d, q)** model, what does **d** represent?

* [ ] The number of autoregressive terms
* [x] The number of differences needed to make the series stationary
* [ ] The number of moving-average terms
* [ ] The length of the seasonal period

> **Explanation:** The "I" (integrated) part applies $(1 - B)^d$ before an ARMA(p, q) is fitted. Most series need $d = 0$, 1 or occasionally 2.

#### Q. Which plot is most useful for choosing the **AR order p** of an ARIMA model?

* [x] Partial autocorrelation function (PACF)
* [ ] Autocorrelation function (ACF)
* [ ] Histogram of the residuals
* [ ] Seasonal decomposition plot

> **Explanation:** For an AR(p) process the theoretical PACF cuts off after lag $p$. The ACF cutting off after lag $q$ is the signature of an MA(q).

#### Q. What is the main purpose of **seasonal differencing** $y_t - y_{t-m}$ in a SARIMA model?

* [ ] To stabilise the variance of the series
* [ ] To remove a non-seasonal linear trend only
* [x] To remove a recurring seasonal pattern of period m
* [ ] To smooth random noise between seasons

> **Explanation:** Subtracting the value from the same season one cycle earlier removes a stable seasonal pattern. In the model this is the $(1 - B^m)^D$ factor.

#### Q. In a **SARIMA(p, d, q)×(P, D, Q)m** model, what does **P** control?

* [x] The number of seasonal autoregressive terms
* [ ] The order of seasonal differencing
* [ ] The number of seasonal moving-average terms
* [ ] The number of non-seasonal moving-average terms

> **Explanation:** Uppercase letters are the seasonal counterparts of p, d and q. $P$ is the order of the seasonal AR polynomial $\Phi(B^m)$, with lags at multiples of $m$.

#### Q. Which criterion balances **goodness of fit against model complexity** when comparing ARIMA models?

* [ ] $R^2$
* [ ] The maximised log-likelihood alone
* [x] AIC (Akaike information criterion)
* [ ] Durbin–Watson statistic

> **Explanation:** $AIC = -2\log L + 2k$ rewards fit and penalises the number of parameters $k$. The log-likelihood alone always favours bigger models.

#### Q. What typically happens if a random walk is **differenced twice** instead of once?

* [ ] The series keeps a unit root and remains non-stationary
* [x] A strong negative lag-1 autocorrelation appears and the variance increases
* [ ] All autocorrelation is removed and the series becomes white noise
* [ ] The AIC of any model fitted to the series always decreases

> **Explanation:** Over-differencing white noise gives $\varepsilon_t - \varepsilon_{t-1}$, an MA(1) with lag-1 autocorrelation $-0.5$ and twice the variance. It adds structure and noise rather than removing it.

#### Q. After fitting an ARIMA model, which diagnostic suggests the **residuals are still autocorrelated**?

* [ ] A Shapiro–Wilk test that rejects normality
* [x] Several significant spikes in the ACF of the residuals
* [ ] A roughly constant residual variance over time
* [ ] A Ljung–Box p-value of 0.40

> **Explanation:** Residuals from an adequate model should look like white noise. A large Ljung–Box p-value (such as 0.40) fails to reject that, while ACF spikes outside the bounds point to structure the model missed.

#### Q. A series behaves like a **random walk with drift**. Which operation makes it stationary?

* [ ] Taking logarithms of the series
* [x] Taking first differences
* [ ] Taking lag-12 seasonal differences only
* [ ] Applying a 3-point moving average

> **Explanation:** For $y_t = \delta + y_{t-1} + \varepsilon_t$, the first difference $\Delta y_t = \delta + \varepsilon_t$ is stationary. Logs and moving averages leave the unit root in place.

#### Q. How does an **LSTM** differ from a basic recurrent neural network (RNN) in time series forecasting?

* [ ] An LSTM uses moving averages of past values instead of the values themselves
* [x] An LSTM uses gated memory cells that help it learn long-range dependencies
* [ ] An LSTM requires the series to be stationary while an RNN does not
* [ ] An LSTM can only be applied to strongly seasonal data

> **Explanation:** LSTM gates control what is stored and forgotten, which improves gradient flow and eases the vanishing-gradient problem of plain RNNs. Like other models, LSTMs still need chronological evaluation.

#### Q. Which is the usual way to fill **a few missing values** in a smooth time series?

* [ ] Drop the entire series from the analysis
* [ ] Replace them with the mean of the whole series
* [x] Interpolate between neighbours, or carry the last value forward
* [ ] Replace them with randomly chosen observed values

> **Explanation:** Interpolation and forward or backward fill use nearby observations, which respects the time dependence. A global mean ignores trend and seasonality and can create artificial jumps.

#### Q. Which evaluation scheme **respects temporal ordering** when assessing a forecasting model?

* [ ] Random k-fold cross-validation
* [ ] Leave-one-out cross-validation on shuffled data
* [x] Rolling-origin (time series) cross-validation
* [ ] Bootstrapping individual observations

> **Explanation:** Rolling-origin evaluation always trains on the past and tests on the following period, as in real forecasting. Random folds leak future information into training.

#### Q. What is the key difference between **ARIMA** and **SARIMA** models?

* [ ] ARIMA includes seasonal terms and SARIMA does not
* [ ] SARIMA never requires any differencing
* [x] SARIMA adds seasonal AR, differencing and MA terms at lags that are multiples of m
* [ ] ARIMA can model only additive components

> **Explanation:** SARIMA multiplies the non-seasonal ARIMA polynomials by seasonal ones, $\Phi(B^m)$, $(1-B^m)^D$ and $\Theta(B^m)$, to capture repeating patterns of period $m$.

#### Q. A standard **classical decomposition** splits a time series into which components?

* [ ] Autoregressive, integrated and moving-average parts
* [ ] Trend, autocorrelation and residual
* [x] Trend(-cycle), seasonal and remainder (noise)
* [ ] Mean, median and mode

> **Explanation:** Decomposition writes $y_t = T_t + S_t + R_t$ (additive) or $y_t = T_t \times S_t \times R_t$ (multiplicative). Methods such as STL estimate the components with local smoothing.

#### Q. Which metric measures the **average absolute percentage error** of forecasts?

* [ ] MAE (mean absolute error)
* [ ] MSE (mean squared error)
* [ ] RMSE (root mean squared error)
* [x] MAPE (mean absolute percentage error)

> **Explanation:** $MAPE = \frac{100}{n}\sum |e_t / y_t|$ expresses errors relative to the actual values, so it is scale-free. MAE and RMSE are in the units of the data.

#### Q. When is **MAPE** a poor choice of forecast accuracy measure?

* [ ] When the series is measured in different units from another series
* [x] When some actual values are zero or very close to zero
* [ ] When forecasts are compared across several horizons
* [ ] When the errors are symmetric around zero

> **Explanation:** MAPE divides by $y_t$, so it is undefined at zero and explodes near zero. Scaled measures such as MASE avoid this.

#### Q. What does **m** denote in SARIMA(p, d, q)×(P, D, Q)m?

* [ ] The order of the non-seasonal MA terms
* [ ] The total number of model parameters
* [x] The seasonal period, such as 12 for monthly data
* [ ] The number of differences applied

> **Explanation:** $m$ is the number of observations per seasonal cycle, such as 12 for monthly data with yearly seasonality or 4 for quarterly data. The seasonal terms act at lags $m, 2m, \dots$

#### Q. Why do ARIMA **prediction intervals** widen as the forecast horizon grows?

* [ ] The model's parameters change over time
* [x] Uncertainty from future shocks accumulates with each step ahead
* [ ] Seasonality becomes stronger at longer lags
* [ ] The residuals become more autocorrelated over time

> **Explanation:** Each future step adds an unknown innovation. For a random walk the $h$-step forecast error variance is $h\sigma^2$, so the interval width grows like $\sqrt{h}$.

#### Q. What is the **null hypothesis** of the augmented Dickey–Fuller (ADF) test?

* [ ] The series is stationary
* [x] The series has a unit root, so it is non-stationary
* [ ] The residuals are normally distributed
* [ ] The autocorrelations at all lags are zero

> **Explanation:** The ADF test checks $H_0: \gamma = 0$ in $\Delta X_t = \alpha + \gamma X_{t-1} + \dots$, which means a unit root. A small p-value is evidence for stationarity.

#### Q. Which property defines a **weakly stationary** time series?

* [ ] Its mean and variance change over time
* [x] Constant mean and variance, and autocovariances that depend only on the lag
* [ ] A strong seasonal component with a fixed period
* [ ] An increasing deterministic trend

> **Explanation:** Weak stationarity requires $E[X_t] = \mu$, $\text{Var}(X_t) = \sigma^2$ and $\text{Cov}(X_t, X_{t+h}) = \gamma(h)$ for all $t$. Trends and seasonality violate it.

#### Q. What does the **autocorrelation function (ACF)** measure?

* [x] The correlation between a series and lagged copies of itself
* [ ] The long-run trend in the series
* [ ] The correlation between two different time series
* [ ] The forecast accuracy of a fitted model

> **Explanation:** $\rho(h) = \gamma(h)/\gamma(0)$ is the correlation between $X_t$ and $X_{t+h}$. The correlation between two different series at various lags is the cross-correlation function.

#### Q. In time series analysis, what is a **lag**?

* [ ] A delay in collecting the data
* [ ] The difference between actual and predicted values
* [x] An earlier value of the same series, such as $y_{t-k}$
* [ ] A type of error in the fitted model

> **Explanation:** Lag $k$ refers to the value $k$ periods back, so $B^k y_t = y_{t-k}$. ACFs and AR models are built on lagged values.

#### Q. What is a **simple moving average** used as a smoothing tool?

* [x] The unweighted average of the most recent k observations
* [ ] The long-run average of the entire series
* [ ] The average of a model's forecasted values
* [ ] A weighted sum of past forecast errors

> **Explanation:** $SMA_t = \frac{1}{k}\sum_{i=0}^{k-1} y_{t-i}$ smooths short-term noise. It is different from an MA(q) model, which is a weighted sum of past innovations.

#### Q. What is the main difference between an **AR** model and an **MA** model?

* [x] AR models use past values of the series; MA models use past innovations (shocks)
* [ ] AR models are for stationary series; MA models are for non-stationary series
* [ ] AR models predict future values; MA models only smooth the data
* [ ] AR models capture seasonality; MA models capture trend

> **Explanation:** AR(p): $X_t = c + \sum \phi_i X_{t-i} + \varepsilon_t$. MA(q): $X_t = \mu + \varepsilon_t + \sum \theta_j \varepsilon_{t-j}$. Both can be used for forecasting.

#### Q. What does the **partial autocorrelation function (PACF)** measure at lag k?

* [ ] The total correlation between the series and its lag-k value
* [x] The correlation between $X_t$ and $X_{t-k}$ after removing the effect of lags 1 to k−1
* [ ] The residuals of a fitted time series model
* [ ] The difference between actual and forecasted values

> **Explanation:** The PACF isolates the direct relationship at lag $k$. For an AR(p) process it is zero beyond lag $p$.

#### Q. Which model is the simplest that has **both autoregressive and moving-average** components for a stationary, non-seasonal series?

* [x] ARMA(p, q)
* [ ] AR(p)
* [ ] MA(q)
* [ ] Random walk

> **Explanation:** ARMA combines $p$ AR terms and $q$ MA terms. ARIMA adds differencing and SARIMA adds seasonal terms, so both build on ARMA.

#### Q. What is the **null hypothesis** of the KPSS test?

* [x] The series is (level or trend) stationary
* [ ] The series has a unit root
* [ ] The residuals have constant variance
* [ ] Past values of another series do not help prediction

> **Explanation:** KPSS reverses the ADF set-up, which is why the two are often used together. Rejecting KPSS while failing to reject ADF is consistent evidence of a unit root.

#### Q. What is the optimal point forecast $\hat{y}_{T+h}$ for a **random walk without drift**?

* [ ] The mean of all past observations
* [x] The last observed value $y_T$, for every horizon h
* [ ] Zero, for every horizon h
* [ ] $y_T$ plus h times the average past change

> **Explanation:** Because $y_{t} = y_{t-1} + \varepsilon_t$ with zero-mean shocks, the best forecast is the current level. This is the naive forecast. Adding $h\delta$ applies only to a random walk with drift.

#### Q. For a random walk with innovation variance $\sigma^2$, what is the **variance of the h-step-ahead forecast error**?

* [ ] $\sigma^2$, the same at every horizon
* [x] $h\sigma^2$
* [ ] $h^2\sigma^2$
* [ ] $\sigma^2 / h$

> **Explanation:** The $h$-step error is the sum of $h$ independent shocks, so its variance is $h\sigma^2$. Intervals therefore widen in proportion to $\sqrt{h}$.

#### Q. Monthly sales show a trend and a stable seasonal pattern. Which **exponential smoothing** method is designed for this?

* [ ] Simple exponential smoothing
* [ ] Holt's linear trend method
* [x] Holt–Winters (triple) exponential smoothing
* [ ] A simple moving average

> **Explanation:** Holt–Winters adds a seasonal equation to Holt's level and trend equations. Simple exponential smoothing handles neither trend nor seasonality, and Holt's method handles only trend.

#### Q. For which values of $\phi$ is the AR(1) model $X_t = \phi X_{t-1} + \varepsilon_t$ **stationary**?

* [x] $|\phi| < 1$
* [ ] $\phi > 1$
* [ ] $|\phi| = 1$
* [ ] Any value of $\phi$

> **Explanation:** With $|\phi| < 1$ shocks die out geometrically. $\phi = 1$ gives a random walk (a unit root) and $|\phi| > 1$ makes the series explode.

#### Q. What does the **p** parameter in ARIMA(p, d, q) control?

* [x] The number of lagged values included (the AR order)
* [ ] The number of differences applied
* [ ] The number of lagged forecast errors (the MA order)
* [ ] The order of seasonal differencing

> **Explanation:** $p$ is the degree of the AR polynomial $\phi(B) = 1 - \phi_1 B - \dots - \phi_p B^p$, so $p$ past values enter the model.

#### Q. A stationary AR(1) process has $\phi = 0.6$. What is its theoretical **lag-2 autocorrelation** $\rho(2)$?

* [ ] 0.6
* [x] 0.36
* [ ] 1.2
* [ ] 0

> **Explanation:** For AR(1), $\rho(h) = \phi^h$, so $\rho(2) = 0.6^2 = 0.36$. The ACF decays geometrically rather than cutting off.

#### Q. A sample ACF has significant spikes at lags 1 and 2 and then cuts off, while the PACF tails off gradually. Which model does this suggest?

* [ ] AR(2)
* [x] MA(2)
* [ ] ARMA(2, 2)
* [ ] White noise

> **Explanation:** An MA(q) process has an ACF that cuts off after lag $q$ and a PACF that tails off. An AR(2) would show the reverse: a PACF cut-off after lag 2.

#### Q. What is the mean of the stationary AR(1) process $X_t = 2 + 0.6X_{t-1} + \varepsilon_t$?

* [ ] 2
* [ ] 3.2
* [x] 5
* [ ] 1.25

> **Explanation:** Taking expectations, $\mu = 2 + 0.6\mu$, so $\mu = c/(1-\phi) = 2/0.4 = 5$. The constant $c$ is not the mean unless $\phi = 0$.

#### Q. An AR(1) process has $\phi = 0.6$ and innovation variance $\sigma^2_\varepsilon = 1$. What is its **variance**?

* [ ] 1
* [ ] 0.64
* [x] 1.5625
* [ ] 2.5

> **Explanation:** $\text{Var}(X_t) = \sigma^2_\varepsilon/(1 - \phi^2) = 1/(1 - 0.36) = 1/0.64 = 1.5625$. The value 2.5 comes from dividing by $1 - \phi$ instead.

#### Q. When is the MA(1) model $X_t = \varepsilon_t + \theta\varepsilon_{t-1}$ **invertible**?

* [ ] For every value of $\theta$
* [x] When $|\theta| < 1$
* [ ] When $|\theta| > 1$
* [ ] When $\theta = 1$

> **Explanation:** With $|\theta| < 1$ the innovations can be recovered as a convergent weighted sum of current and past observations. Invertibility also picks a unique MA model from pairs with the same ACF.

#### Q. Using the backward shift operator, what is $(1 - B)^2 y_t$?

* [ ] $y_t - y_{t-2}$
* [x] $y_t - 2y_{t-1} + y_{t-2}$
* [ ] $y_t - 2y_{t-2}$
* [ ] $y_t + y_{t-1} + y_{t-2}$

> **Explanation:** $(1 - B)^2 = 1 - 2B + B^2$, and $B^k y_t = y_{t-k}$. This is the second difference. Note that $y_t - y_{t-2}$ is $(1 - B^2)y_t$, a lag-2 difference.

#### Q. A monthly series is modelled with SARIMA(1,1,1)×(1,1,1)12. How many **initial observations are lost** to differencing?

* [ ] 2
* [x] 13
* [ ] 12
* [ ] 24

> **Explanation:** The combined operator $(1 - B)(1 - B^{12})$ reaches back $d + Dm = 1 + 12 = 13$ periods, so the first 13 values have no differenced counterpart.

#### Q. What is the **null hypothesis** of the Ljung–Box test applied to model residuals?

* [ ] The residuals have a unit root
* [x] The residual autocorrelations up to the tested lag are jointly zero
* [ ] The residuals are normally distributed
* [ ] The residual variance is constant over time

> **Explanation:** $Q_{LB} = n(n+2)\sum_{h=1}^{m}\hat{\rho}(h)^2/(n-h)$ is compared with a $\chi^2$ distribution. A small p-value means serial correlation remains in the residuals.

#### Q. Two ARIMA models are fitted to the same data. Model A has BIC 412.3 and model B has BIC 405.8. Which is preferred by BIC?

* [ ] Model A, because its BIC is higher
* [x] Model B, because its BIC is lower
* [ ] Neither, because BIC values cannot be compared
* [ ] The model with more parameters, whatever its BIC

> **Explanation:** Lower information criteria are better. BIC penalises parameters with $k \ln n$, more heavily than AIC, so it favours parsimonious models. Comparisons are valid only on the same data and with the same differencing.

#### Q. What defines a **white noise** process?

* [x] Zero mean, constant variance and no autocorrelation at any non-zero lag
* [ ] A linear trend plus random fluctuations
* [ ] Observations that are positively correlated with their previous values
* [ ] A strong seasonal component with random amplitude

> **Explanation:** White noise has $E[\varepsilon_t] = 0$, $\text{Var}(\varepsilon_t) = \sigma^2$ and $\text{Cov}(\varepsilon_t, \varepsilon_s) = 0$ for $t \neq s$. It is the benchmark that good model residuals should resemble.

#### Q. How does **simple exponential smoothing** form its forecast?

* [x] As a weighted average of past observations with exponentially decreasing weights
* [ ] As an equally weighted average of all past observations
* [ ] By fitting a straight-line trend to the whole series
* [ ] By regressing the series on its own lag-1 value

> **Explanation:** $\hat{y}_{t+1} = \alpha y_t + (1 - \alpha)\hat{y}_t$, so the weight on $y_{t-j}$ is $\alpha(1 - \alpha)^j$. A larger $\alpha$ reacts faster to recent changes.

#### Q. In time series forecasting, what does **overfitting** mean?

* [ ] Using too few observations to fit the model
* [x] A model fits the training period closely but forecasts new periods poorly
* [ ] A model that ignores the seasonality in the data
* [ ] Smoothing the data so much that real patterns are lost

> **Explanation:** An overfit model captures noise specific to the training sample, such as too many ARMA terms. Its in-sample errors look small while its out-of-sample errors are large.

#### Q. Actual values are 10, 12 and 8, and the forecasts are 11, 10 and 8. What are the **MAE** and **RMSE**?

* [x] MAE 1.0, RMSE about 1.29
* [ ] MAE 1.0, RMSE 1.0
* [ ] MAE 1.5, RMSE about 1.67
* [ ] MAE 0.33, RMSE about 1.29

> **Explanation:** The errors are −1, 2 and 0. MAE $= (1 + 2 + 0)/3 = 1.0$ and RMSE $= \sqrt{(1 + 4 + 0)/3} = \sqrt{5/3} \approx 1.29$. RMSE ≥ MAE, because squaring weights the larger error more.

#### Q. What does the **Box–Jenkins methodology** focus on?

* [x] An iterative cycle of identifying, estimating and checking ARIMA models
* [ ] Decomposing a series into seasonal components only
* [ ] Smoothing a series with moving averages
* [ ] Running hypothesis tests on the means of time series

> **Explanation:** Box–Jenkins uses ACF and PACF to identify a model, then estimates it and checks its residuals. If the diagnostics fail, the cycle repeats before the model is used for forecasting.

#### Q. Daily stock returns show little autocorrelation, but large moves tend to be followed by large moves. Which model family targets this **volatility clustering**?

* [ ] Seasonal ARIMA models
* [x] ARCH and GARCH models
* [ ] Holt's linear trend method
* [ ] Simple moving averages

> **Explanation:** GARCH models let the conditional variance depend on past squared shocks and past variances, so volatility persists. The ACF of squared returns, not raw returns, reveals the effect.

#### Q. In a VAR model, what does it mean that **x Granger-causes y**?

* [ ] Changes in x are proven to cause changes in y
* [x] Past values of x improve predictions of y beyond y's own past
* [ ] x and y are perfectly correlated at lag 0
* [ ] y has a unit root while x is stationary

> **Explanation:** Granger causality is about predictive information: it tests whether the lagged-x coefficients in y's equation are jointly zero. It does not establish true causation.

#### Q. A periodogram of a monthly series has its largest peak at frequency **1/12 ≈ 0.083** cycles per month. What does this indicate?

* [ ] A cycle that repeats 12 times per month
* [x] A cycle with a period of about 12 months
* [ ] A linear trend with slope 0.083
* [ ] Autocorrelation of 0.083 at lag 12

> **Explanation:** Period is the reciprocal of frequency, so $1/(1/12) = 12$ months, an annual pattern. The notes stress converting a peak's frequency back to a period before interpreting it.

#### Q. What does the **Kalman filter** do in a linear Gaussian state-space model?

* [ ] It removes seasonality by differencing at lag m
* [x] It recursively updates the estimate of an unobserved state as each observation arrives
* [ ] It selects ARIMA orders by minimising AIC
* [ ] It tests whether the series has a unit root

> **Explanation:** At each step the filter predicts the state, compares the prediction with the new observation, and corrects it using the Kalman gain. The gain weighs the prediction's uncertainty against the observation's.

#### Q. A series' fluctuations grow in proportion to its level. Which transformation is commonly applied **before** fitting an ARIMA model?

* [ ] Seasonal differencing at lag 12
* [x] A log or Box–Cox transformation
* [ ] Adding a constant to every observation
* [ ] Removing every second observation

> **Explanation:** Logs turn multiplicative variation into additive variation, which stabilises the variance. Differencing deals with the mean, not with a variance that grows with the level.
