## Stationarity

1. **Intuition for (Weak) Stationary Time Series:**
   - A stationary time series is a data sequence where the statistical properties remain consistent over time. Specifically:
     - **No systematic change in mean** (i.e., no trend over time).
     - **No systematic change in variance** (i.e., constant variation across time).
     - **No periodic fluctuations** (i.e., no repeating cycles or seasonality).
   - The properties (such as mean, variance, and autocorrelation) of one section of the data are similar to those of other sections of the data.
     - This implies that the data behaves similarly at any point in time.

2. **Dealing with Non-Stationary Time Series:**
   - In practice, many time series data sets are non-stationary, meaning they may exhibit trends, changing variance, or seasonality.
   - To analyze non-stationary time series, we often apply **transformations** to make the series stationary, which is essential for many statistical modeling techniques (e.g., ARIMA models).
     - Common transformations include **differencing**, **logarithmic transformations**, or **detrending** to remove trends or stabilize variance.

### Weak Stationarity
- A **weakly stationary** (or second-order stationary) time series is a more relaxed definition of stationarity, focusing primarily on the first two moments of the distribution (mean and variance):
  - The **mean** of the series is constant over time.
  - The **variance** is constant over time (no systematic change in variance).
  - The **covariance** between values at different times depends only on the time difference (lag) between them and not the actual time itself.
