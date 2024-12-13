## Time Series Analysis

Time series data consists of sequential observations collected over a period of time. This kind of data is prevalent in a range of fields such as finance, economics, climatology, and more. Time series analysis involves the exploration of this data to identify inherent structures such as patterns or trends, forecasting future points in the series, and providing insights for strategic decision-making.

**Definition:** An ordered sequence of values representing a variable, recorded at equally spaced time intervals.

### The need for Time Series Models

You are probably aware of regression models, where models predict one quantity based on the relationship with another quantity. They typically involve using independent variables to predict dependent variables. For example, when predicting electricity consumption for a particular month, we would take into consideration temperature, number of residents, and so on. These factors might seem sufficient for all cases of prediction, making the creation of an entirely new domain of models just for time series seem unnecessary, doesn’t it? However, the issue arises when past values influence the current value. This is where time series models come into play. For instance, predicting this month's electricity consumption based on last month's consumption can be achieved using an AR(1) model.

**Non-Time Series Approach:**

- Often involves **interpolation**, predicting within the range of existing data points based on relationships between independent and dependent variables.
- Predict electricity consumption based on **external factors** like temperature.
- Lower temperatures generally lead to increased consumption up to a certain plateau.
- **Prediction errors** remain relatively consistent across different prediction points.
- **Confidence intervals** (prediction intervals) are similar across various predictions.

**Time Series Approach:** 

- Primarily involves **extrapolation**, forecasting future values beyond the range of available data, which inherently carries more uncertainty.
- Time series data have inherent **temporal structures** where current values are dependent on past values. Capturing these dependencies requires models that can account for autocorrelation and temporal dynamics, which traditional regression models are not designed to handle.
- In time series forecasting, **prediction errors** can accumulate over time, leading to increasing uncertainty the further into the future the forecast extends. Specialized time series models incorporate mechanisms to manage and quantify this growing uncertainty, unlike standard regression models where errors are typically more stable.
- Time series often have trends, seasonality, and other **dynamic patterns** that need to be explicitly modeled. Specialized approaches like **ARIMA**, **Exponential Smoothing**, and **state-space models** are tailored to identify and forecast these patterns effectively.
- Time series models provide **prediction intervals** that expand over time, reflecting the increasing uncertainty of forecasts. Standard regression models usually offer fixed confidence intervals that do not account for the temporal horizon of predictions.
- Time series analysis uses unique methodologies and models (e.g., **ARIMA**, **GARCH**, **LSTM networks**) that are specifically designed to handle the sequential and dependent nature of the data, which are not accommodated by conventional regression techniques.

Below is a plot that visualizes the historical data and predictions of electricity consumption over time. 

![electricity consumption over time](https://github.com/user-attachments/assets/89a67e4f-1c56-4ca8-8ff2-66ce2fb663ee)

The plot includes three components:

1. **Historical Data** shown as a solid line, this represents the actual electricity consumption data collected over a two-year period from January 2021 to December 2022.
2. **Regression Prediction** represented by a dashed blue line, this forecast is based on a linear regression model. It captures a simple trend over the historical data and projects it forward for the first three months of 2023.
3. **Time Series Prediction** shown as another dashed line, this prediction uses an Exponential Smoothing model with a seasonal component. It considers both trend and seasonality in the data to provide a more dynamic projection for the same three-month period.

### Components of a Time Series

A time series is a series of data points indexed in chronological order, typically at regular time intervals. It can be decomposed into four primary components:

- **Trend** in a time series reflects the general direction in which the values are moving over a longer time frame. This could be an upward trend indicating growth, a downward trend signaling decline, or a stationary trend showing no significant change over time.
- **Seasonality** in a time series is identified by regular, repeating patterns that occur at fixed intervals, such as daily, monthly, or yearly. Examples include increased sales during holiday seasons or higher electricity demand in summer months.
- **Cyclicity** in a time series refers to patterns that occur over irregular intervals and are influenced by external or macroeconomic factors. Unlike seasonality, cyclic patterns are not tied to a fixed calendar period and can vary in duration.
- **Irregularity** or **noise** in a time series represents random and unpredictable fluctuations that are not explained by the trend, seasonality, or cyclicity. These could be caused by unexpected events such as policy changes, economic shocks, or natural disasters.
- **Decomposition** of a time series involves breaking it down into its constituent components: trend, seasonality, cyclicity, and irregularity. This is useful for analysis and forecasting.

### Time Series Analysis Techniques

Timeseries analysis methods can be broadly classified into two main categories: time-domain methods and frequency-domain methods.

#### Time-Domain Methods

These methods analyze the temporal sequences of data points directly. The focus here is on identifying patterns such as trends, seasonality, noise, and fluctuations within the time series data. 

Important Techniques Include:

- **Autocorrelation** analysis measures the correlation between a time series and its lagged values. This helps identify repetitive patterns and predictability based on the relationships between past and current observations.
- **Cross-correlation** analysis evaluates the relationship between two different time series at varying time lags. It reveals how changes in one series may lead to or influence changes in another over time.

Some of the methods used for time-domain analysis include:

- **Stochastic Processes**
- **Random Vectors**
- **Deterministic Signals**
- **Time Delay Analysis**
- **Nonlinear Systems**

After decomposing the time series into its components, statistical techniques can be employed to model and forecast future points in the series. Some widely used techniques include:

- **Moving averages (MA)** involve calculating the average of a fixed number of consecutive data points around each observation. This method smooths out short-term fluctuations, reducing noise and emphasizing the underlying trend.
- **Exponential smoothing (ES)** assigns exponentially decreasing weights to older observations, giving more importance to recent data. This method is particularly useful for capturing trends and seasonal effects in dynamic datasets.
- **Autoregressive integrated moving average (ARIMA)** combines autoregression (using past values), differencing (removing trends to achieve stationarity), and moving averages (smoothing residuals) in one model. It is effective for modeling and forecasting non-stationary time series with trends or seasonality.

#### Frequency-Domain Methods

These methods focus on transforming the time series data into the frequency domain to detect and study cyclic behaviors and periodicities. This is typically done through mathematical transforms that help decompose the time series into constituent frequencies.

Important Techniques Include:

- **Spectral analysis** uses techniques such as Fourier Series for analyzing periodic signals, Fourier Transform for decomposing aperiodic signals into frequency components, and Laplace Transform for signal decomposition and stability analysis.
- **Wavelet analysis** applies discrete and continuous wavelet transforms to study localized phenomena in both time and frequency domains, making it particularly useful for analyzing non-stationary or transient signals.

These techniques enable you to study the frequency composition of the data, highlighting dominant cycles that might not be apparent in the time domain.

#### Parametric vs. Non-Parametric Methods

- **Parametric methods** involve models like autoregressive and moving average models, which assume a specific structure for the data-generating process. These methods estimate a finite set of parameters and typically require strong assumptions, such as stationarity of the series.
- **Non-parametric methods** include approaches like covariance or spectral analysis, which impose fewer assumptions on the data. These methods provide greater flexibility by not requiring a predetermined model structure, allowing for a more adaptable analysis of the series.

#### Types of Timeseries

The classification also distinguishes between:

- **Linear univariate** models analyze time series with a single variable and assume a linear relationship between the current and past values of the series.
- **Linear multivariate** models extend linear analysis to multiple variables, capturing the relationships and interactions between them over time.
- **Nonlinear univariate** models deal with a single variable but allow for complex, nonlinear relationships within the series, often capturing dynamics that linear models cannot.
- **Nonlinear multivariate** models analyze multiple variables, accounting for nonlinear interactions and dependencies among them, which are common in complex systems.

Below is a plot demonstrating the four concepts of time series modeling:

![types_of_models](https://github.com/user-attachments/assets/e49984c5-e6d1-46c1-b7ba-e6aea8a437df)

1. **Linear Univariate Model** shows predictions using a single variable with a linear ARIMA model.
2. **Linear Multivariate Model** shows predictions with multiple variables using a VAR model.
3. **Nonlinear Univariate Model** shows predictions using a single variable with a nonlinear MLP model.
4. **Nonlinear Multivariate Model** shows predictions with multiple variables using a nonlinear MLP model.

### Applications of Time Series Analysis

Time series analysis finds widespread applications across various industries, including:

- **Financial forecasting** involves analyzing historical stock prices, indices, or financial metrics to predict future market trends, assisting in investment and trading decisions.
- **Weather forecasting** uses historical meteorological data to predict future weather patterns, aiding in planning and mitigating the impact of severe weather events.
- **Sales forecasting** applies time series analysis to estimate future product demand, enabling businesses to optimize inventory, production, and supply chain operations.

### Example

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

#### Applying Moving Average

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
