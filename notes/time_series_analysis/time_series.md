## Time Series Analysis

Time series data consists of sequential observations collected over a period of time. This kind of data is prevalent in a range of fields such as finance, economics, climatology, and more. Time series analysis involves the exploration of this data to identify inherent structures such as patterns or trends, forecasting future points in the series, and providing insights for strategic decision-making.

### Components of a Time Series

A time series is a series of data points indexed in chronological order, typically at regular time intervals. It can be decomposed into four primary components:

1. **Trend**: The underlying direction of the series over a lengthier period. It can be increasing (upward), decreasing (downward), or horizontal (stationary). Analyzing the trend component allows us to understand the long-term changes in the data.

2. **Seasonality**: The cyclical patterns that repeat over known, fixed periods of time within the data set. For instance, retail sales may increase during the holiday season each year. This seasonality helps forecast short-term variations.

3. **Cyclicity**: These are fluctuations in the data that aren't tied to a fixed seasonal period. Instead, these patterns occur at less predictable intervals, often influenced by macroeconomic factors.

4. **Irregularity** (or **Noise**): These are random, unpredictable, or residual fluctuations in the series that cannot be attributed to the trend or the cyclical variation. These could arise due to unexpected external factors such as political events, natural disasters, or sudden changes in market conditions.

### Time Series Analysis Techniques

Timeseries analysis methods can be broadly classified into two main categories: time-domain methods and frequency-domain methods.

#### Time-Domain Methods

These methods analyze the temporal sequences of data points directly. The focus here is on identifying patterns such as trends, seasonality, noise, and fluctuations within the time series data. 

Key Techniques Include:
- **Autocorrelation Analysis**: This helps measure the correlation between time-lagged observations within the same time series. Autocorrelation functions can help identify patterns and potential predictability based on past observations.

- **Cross-Correlation Analysis**: This technique measures the relationship between two time series at different lags, showing how one time series may influence another.
  
Some of the methods used for time-domain analysis include:
- **Stochastic Processes**
- **Random Vectors**
- **Deterministic Signals**
- **Time Delay Analysis**
- **Nonlinear Systems**

After decomposing the time series into its components, statistical techniques can be employed to model and forecast future points in the series. Some widely used techniques include:

- **Moving averages (MA)**: A method that calculates the average of a certain number of terms before and after each data point to create a series of averages. It helps to smooth out noise and highlight underlying trends.

- **Exponential smoothing (ES)**: Similar to moving averages but assigns a decaying weight to past observations. It is more receptive to recent changes in trends or seasonal effects.

- **Autoregressive integrated moving average (ARIMA)**: This method combines autoregression, differencing, and moving averages in one model. ARIMA models are efficient for non-stationary series and can represent series with a trend or seasonal components.

#### Frequency-Domain Methods

These methods focus on transforming the time series data into the frequency domain to detect and study cyclic behaviors and periodicities. This is typically done through mathematical transforms that help decompose the time series into constituent frequencies.

Key Techniques Include:
- **Spectral Analysis**: Utilizes Fourier Series for periodic signals, Fourier Transform for aperiodic signals, and Laplace Transform for signal decomposition.
- **Wavelet Analysis**: Focuses on discrete and continuous wavelet transforms for studying time-frequency localized phenomena.

These techniques enable you to study the frequency composition of the data, highlighting dominant cycles that might not be apparent in the time domain.

#### Parametric vs. Non-Parametric Methods

- **Parametric Methods**: These methods, such as autoregressive models and moving average models, rely on strong assumptions about the data (e.g., stationarity of the process) and estimate a finite number of parameters. They assume a specific model for the data-generating process.
  
- **Non-Parametric Methods**: These methods, including covariance or spectral analysis, make fewer assumptions and allow for more flexibility in modeling the data without a predetermined structure.

#### Types of Timeseries

The classification also distinguishes between:
- **Linear Univariate**: Single variable, linear processes
- **Linear Multivariate**: Multiple variables, linear processes
- **Nonlinear Univariate**: Single variable, nonlinear processes
- **Nonlinear Multivariate**: Multiple variables, nonlinear processes

These methods apply to discrete and continuous data, covering both simple and complex time series analysis, offering a comprehensive toolkit for researchers and practitioners to analyze temporal data.

### Applications of Time Series Analysis

Time series analysis finds widespread applications across various industries, including:

- **Financial forecasting**: In stock market analysis, the historical data of stock prices or indices are analyzed to forecast future prices.

- **Weather forecasting**: Predicting meteorological patterns based on historical weather data can aid in preparing for severe weather conditions.

- **Sales forecasting**: Businesses use time series analysis to anticipate product sales, which in turn helps with inventory and supply chain management.

## Example

Let's consider a simplified example of time series data and apply some basic analysis techniques to it. Imagine we have the following monthly sales data for a retail store:

| Month | Sales |
| ----- | ----- |
| 1     |  100 |
| 2     |  120 |
| 3     |  110 |
| 4     |  130 |
| 5     |  140 |
| 6     |  150 |
| 7     |  160 |
| 8     |  180 |
| 9     |  170 |
| 10    |  190 |
| 11    |  200 |
| 12    |  210 |

### Plotting the Time Series Data

First, we can visualize the data using an ASCII plot:

```
Sales
210 |                                   x
200 |                                x
190 |                             x
180 |                         x
170 |                      x 
160 |                   x 
150 |                x
140 |             x
130 |          x
120 |       x
110 |    x
100 | x
    -------------------------------------
      1  2  3  4  5  6  7  8  9  10 11 12
                   Month
```

From the plot, we can see an increasing trend in the sales data.

### Applying Moving Average

Next, let's apply a moving average with a window size of 3 to smooth out short-term fluctuations:

| Month | Sales | Moving Average (Window=3) |
| ----- | ----- | ------------------------- |
| 1     |  100  |         |
| 2     |  120  |         |
| 3     |  110  |     120 |
| 4     |  130  |     110 |
| 5     |  140  |     127 |
| 6     |  150  |     140 |
| 7     |  160  |     150 |
| 8     |  180  |     163 |
| 9     |  170  |     180 |
| 10    |  190  |     170 |
| 11    |  200  |     187 |
| 12    |  210  |     200 |

The moving average shows an increasing trend in sales, similar to the original time series plot.

Here's the plot with the analysis using Simple Exponential Smoothing (SES) on the given sales data:

![sales_prediction](https://github.com/djeada/Statistics-Notes/assets/37275728/85db196f-ac46-438a-8011-a6a3f952bdb8)

- The blue line represents the actual sales data for each month.
- The purple dashed line shows the predictions from the optimized SES model.
