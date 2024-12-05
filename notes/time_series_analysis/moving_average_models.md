## Moving Average Models

Moving Average (MA) models are part of time series analysis in statistics, used for forecasting and understanding past data. They are crucial for analyzing data points by creating a series of averages of different subsets of the full data set.

### Moving Average Model (MA)

A Moving Average model, MA($q$), uses past forecast errors in a regression-like model. It involves a linear combination of error terms of the lagged forecast. The model is:

$$
y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \theta_2 \varepsilon_{t-2} + \dots + \theta_q \varepsilon_{t-q}
$$

- $y_t$ is the observation at time `t`.
- $\mu$ is the mean of the series.
- $\varepsilon_t$ is the error at time `t`.
- $\theta_i$ are the parameters of the model.

MA models are best for modeling time series with short-term, abrupt changes.

### Simple Moving Average (SMA)

The Simple Moving Average (SMA) is the unweighted mean of the previous `k` data points. It's used to smooth out data series and identify trends over time. The formula for SMA is:

$$
SMA_t = \frac{1}{k} \sum_{i=0}^{k-1} y_{t-i}
$$

- $y_t$ is the observation at time `t`.
- $k$ is the number of periods in the SMA calculation.
- $\text{SMA}_t$ is the SMA value at time `t`.

SMA helps in reducing the noise in the data to see the underlying trend more clearly.

### Exponential Moving Average (EMA)

The Exponential Moving Average (EMA) places a greater weight on more recent data points, making it more responsive to new information. The formula for EMA is:

$$
EMA_{t} = (1 - \alpha) y_t + \alpha \cdot {EMA}_{t-1}
$$

- $y_t$ is the observation at time `t`.
- $\alpha$ is the smoothing factor, a constant between 0 and 1.
- $\text{EMA}_t$ is the EMA value at time `t`.

A higher $\alpha$ places more weight on recent observations, helping in tracking the latest changes more closely.

### Example: Stock Price Analysis

When analyzing stock prices, technical indicators like the Simple Moving Average (SMA) and the Exponential Moving Average (EMA) are frequently employed. These methods help to smooth out price data over a specified period and can be crucial in identifying trends.

#### SMA Analysis
The Simple Moving Average (SMA) is a calculation that takes the arithmetic mean of a given set of prices over a specific number of days in the past; for instance, over the previous 20 days.

$SMA = (P1 + P2 + ... + P20) / 20$$

Here, $P1$, $P2$, ..., $P20$ represent the stock prices for each of the 20 days.

The 20-day SMA helps smooth out short-term fluctuations in stock prices, providing a clearer view of the overall price trend.

#### EMA Analysis
The Exponential Moving Average (EMA) gives more weight to more recent prices. This sensitivity to newer prices makes the EMA more responsive to price changes. Unlike the SMA, the EMA applies a weighting factor to each day's price depending on its recency.

$$EMA = Price(T) * k + EMA(Y) * (1 - k)$$

Where:

- $T$ = Today
- $Y$ = Yesterday
- $k = 2 / (N + 1)$
- $N$ = The number of days in the EMA (e.g., 20 days)
  
The EMA is valuable for capturing more recent trends and is often used for shorter time frames.

#### Trend Identification

- **Crossing**: When the EMA crosses the SMA, it may indicate a shift in trend. An upward crossing can signal a bullish trend, while a downward crossing might signal a bearish trend.
- **Divergence**: If the EMA diverges significantly from the SMA, it suggests increased market momentum in the direction of the EMA.
- Investors often use these indicators in conjunction to get a more nuanced understanding of the market sentiment.
- It's important to remember that SMA and EMA are based on past prices and are not predictive of future prices but rather indicative of trends.

![stock_price_analysis](https://github.com/djeada/Statistics-Notes/assets/37275728/69a7a991-b80c-406b-b0c9-129953f80e3f)

- The blue line represents the mock stock prices, exhibiting a more dynamic and volatile behavior, similar to real-world stock market trends.
- The orange line is the 20-day Simple Moving Average (SMA). It smooths out the fluctuations in the stock prices, providing a clearer view of the long-term trend.
- The green line shows the 20-day Exponential Moving Average (EMA), which reacts more quickly to recent price changes, thus capturing short-term movements more effectively.
