# Time Series Extensions Quiz

#### Q. Which statement best describes weak white noise?

* [ ] The observations must be normally distributed
* [x] Mean and variance are constant and nonzero-lag autocovariances are zero
* [ ] Every observation must be independent of all others
* [ ] The process must have zero variance

#### Q. Which validation design is appropriate for forecasting?

* [ ] Randomly shuffle observations before each split
* [x] Train on earlier observations and validate on later observations
* [ ] Normalize using the full series before splitting
* [ ] Tune the model using the final test period

#### Q. What is the main advantage of rolling-origin evaluation?

* [ ] It guarantees normally distributed forecast errors
* [x] It evaluates the forecasting procedure at multiple historical origins
* [ ] It makes non-stationary data stationary
* [ ] It eliminates the need for a test set

#### Q. Which metric can remain useful when actual observations include zeros?

* [ ] MAPE
* [x] MASE
* [ ] Percentage bias only
* [ ] Log percentage error

#### Q. In dynamic regression, what must be considered before using an exogenous predictor for future forecasts?

* [ ] Whether the predictor has a high in-sample correlation only
* [x] Whether its future value will actually be known or forecastable at the forecast origin
* [ ] Whether its mean equals zero
* [ ] Whether it has exactly one lag

#### Q. Granger causality establishes that:

* [ ] One variable has a structural causal effect on another
* [x] Past values of one variable improve prediction of another given the model's information set
* [ ] Two variables are cointegrated
* [ ] Both variables are stationary

#### Q. When two I(1) variables have a stationary linear combination, they are:

* [ ] White noise
* [ ] Seasonally adjusted
* [x] Cointegrated
* [ ] Necessarily independent

#### Q. A VECM is especially appropriate when:

* [ ] All variables are independent white noise
* [x] Integrated variables share one or more cointegrating relationships
* [ ] The target is purely seasonal
* [ ] Only one scalar variable is observed

#### Q. Kalman smoothing differs from Kalman filtering because smoothing:

* [ ] Uses no observations
* [ ] Can only estimate future states
* [x] May use observations that occur after the state being estimated
* [ ] Requires the state to be directly observed

#### Q. What can cause a spectral peak to spread into neighboring frequencies?

* [ ] Cointegration
* [x] Spectral leakage
* [ ] Granger causality
* [ ] Seasonal differencing

#### Q. If a signal is sampled below the rate needed to distinguish its frequency, the result is:

* [ ] Invertibility
* [ ] Heteroskedasticity
* [x] Aliasing
* [ ] Cointegration
