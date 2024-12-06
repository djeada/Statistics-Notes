## Seasonality and Trends

**Seasonality** and **trends** are fundamental components in time series data that significantly impact analysis and forecasting. Understanding and correctly modeling these elements are useful for accurate predictions and effective time series modeling.

- Identifying **seasonality** is useful for adjusting forecasting models to account for predictable fluctuations.
- A time series can display **cyclical** patterns, which are longer-term fluctuations occurring over variable periods, often influenced by economic or environmental factors.
- Distinguishing between **cyclical** and seasonal patterns is necessary, as cycles lack fixed periodicity and are harder to model.
- **Randomness** represents unpredictable variations in a time series caused by noise, anomalies, or irregular external factors.
- **Trends** show long-term upward or downward movements in a time series, often reflecting broader changes such as technological advances or societal shifts.

### Seasonality

**Seasonality** refers to periodic fluctuations that repeat at regular intervals over time. These patterns are often driven by seasonal factors such as weather, holidays, or economic cycles.

#### Characteristics of Seasonality

- **Periodicity** means that seasonal patterns repeat at regular, fixed intervals, such as every day, week, month, or year. For example, daily energy usage often peaks in the evening, and retail sales rise every December.
- **Additive seasonality** occurs when the seasonal effect stays the same regardless of the data’s overall level. For instance, an ice cream shop might see an additional 100 sales every summer weekend, no matter how high or low the regular sales are.
- **Multiplicative seasonality** happens when the seasonal effect depends on the data’s level. For example, if a store’s summer sales are 20% higher than its regular sales, the increase will be larger when the baseline sales are higher.
- **Consistency** is a hallmark of seasonality. Seasonal patterns remain predictable over time, such as heating bills consistently peaking during winter months.
- **Influence of external factors** can affect seasonality. Events like holidays, weather, or school terms often create repeating patterns in data.

#### Examples of Seasonal Patterns

- Daily patterns, such as **electricity consumption**, often peak during specific times of day, like morning and evening hours.
- Weekly trends are seen in **retail sales**, which typically increase on weekends due to higher consumer activity.
- Monthly or quarterly patterns include **ice cream sales**, which tend to rise during the summer months in response to warmer weather.
- Annual cycles are observed in **tax filings**, which spike every April in many countries due to tax deadlines.

![seasonal_pattern](https://github.com/user-attachments/assets/0b8772f9-2f2f-4bd8-b194-2002e99d810b)

#### Decomposing Seasonality

To analyze and remove seasonality, a time series can be decomposed into three main components:

- The **trend component ($T_t$)** captures the long-term progression of the time series, representing its overall direction.
- The **seasonal component ($S_t$)** represents the repeating short-term patterns or cycles in the data, often tied to calendar-based events.
- The **residual component ($R_t$)** accounts for the irregular or random fluctuations not explained by the trend or seasonality.

Mathematically, for an additive model:

$$X_t = T_t + S_t + R_t$$

For a multiplicative model:

$$X_t = T_t \times S_t \times R_t$$

##### Decomposition Methods

**I. Moving Average Method**

- The method estimates trends by smoothing data to reduce short-term fluctuations.
- A centered moving average is calculated using a window size matching the seasonal period.
- The trend component is obtained by averaging values within the defined window for each time point.
- The seasonal component is derived by subtracting the trend from the original data at each time point.
- Adjustments may be necessary if the series exhibits multiplicative seasonality by first log-transforming the data.

**II. Seasonal Decomposition of Time Series by Loess (STL)**

- STL is a method for decomposing time series data into trend, seasonal, and residual components.
- The technique uses local regression (loess) to estimate components over a flexible range of data points.
- It can handle additive or multiplicative seasonality depending on the problem context.
- The method is robust to outliers, reducing their impact on the estimated components.
- STL is effective for identifying and modeling complex and non-constant seasonal patterns.

**III. Additive vs. Multiplicative Decomposition**

- Additive decomposition assumes the series is composed of components added together: $X_t = T_t + S_t + R_t$.
- Multiplicative decomposition assumes components combine through multiplication: $X_t = T_t \times S_t \times R_t$.
- Choosing between models depends on the nature of the series, typically determined by visual inspection or transformations.

### Trends

**Trend** refers to the long-term movement or direction in the time series data. Trends can be:

- **Upward trend** refers to a general increase in the time series values over time, indicating growth or improvement.  
- **Downward trend** represents a general decrease in the time series values over time, indicating decline or reduction.  
- **Stationary trend** occurs when there is no significant long-term movement in the series, and it fluctuates around a constant mean.

![trends](https://github.com/user-attachments/assets/00cb585e-e378-4b99-8ff8-cbdf91e9fef8)

#### Identifying Trends

- **Visual inspection** involves plotting the time series data to observe the overall direction, such as upward, downward, or stationary trends.  
- **Statistical tests**, such as the Mann-Kendall trend test, are applied to formally detect the presence of trends in the time series.  
- **Autocorrelation function (ACF)** analysis shows a slow decay in autocorrelation, which suggests non-stationarity caused by the presence of a trend.  

#### Detrending Methods

I. **Differencing**:

Remove trends by analyzing changes between consecutive observations.

**First-order Differencing**:

$$Y_t = X_t - X_{t-1}$$

**Second-order Differencing**:

$$Y_t = (X_t - X_{t-1}) - (X_{t-1} - X_{t-2}) = X_t - 2X_{t-1} + X_{t-2}$$

II. **Transformation**:

Stabilize variance and linearize exponential trends.

**Logarithmic Transformation**:

$$Y_t = \log(X_t)$$

III. **Regression Modeling**:

Fit a trend line to the data and analyze residuals.

**Linear Trend Model**:

$$X_t = \beta_0 + \beta_1 t + \epsilon_t$$

**Nonlinear Trend Model**:

$$X_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \epsilon_t$$

#### Visualization of Trends

- **Time series plot** provides a visual representation of the overall direction of the data over time, helping to identify trends and patterns.  
- **Detrended series plot** illustrates the data after the trend component is removed, making it easier to observe other elements such as seasonality or residual noise.

### Modeling Seasonality and Trends

**Modeling seasonality and trends** is critical for accurate forecasting by explicitly separating these components for analysis.

#### Seasonal ARIMA (SARIMA)

- **SARIMA models** extend ARIMA by incorporating seasonal terms to handle periodic patterns.
- The **SARIMA model equation** is given as:  

$$\Phi_P(B^s) \phi_p(B) (1 - B^s)^D (1 - B)^d X_t = \Theta_Q(B^s) \theta_q(B) \epsilon_t$$

- $\phi_p(B)$ represents the **non-seasonal AR polynomial** of order $p$.
- $\theta_q(B)$ represents the **non-seasonal MA polynomial** of order $q$.
- $\Phi_P(B^s)$ represents the **seasonal AR polynomial** of order $P$.
- $\Theta_Q(B^s)$ represents the **seasonal MA polynomial** of order $Q$.
- $D$ is the **seasonal differencing order** to account for periodic patterns.
- $d$ is the **non-seasonal differencing order** to address overall trends.
- $s$ is the **seasonal period**, such as 12 for monthly data with yearly seasonality.

#### Exponential Smoothing State Space Models (ETS)

- **ETS models** use weighted averages to smooth time series data, accounting for trends and seasonality.
- The **level component** ($L_t$) represents the baseline value of the series.
- The **trend component** ($T_t$) captures the direction and magnitude of changes over time.
- The **seasonal component** ($S_t$) accounts for recurring patterns within the data.

**Additive ETS models** apply when seasonal variations are constant, expressed as:  

$$X_t = L_t + T_t + S_t + \epsilon_t$$

**Multiplicative ETS models** apply when seasonal variations scale with the level, expressed as:  

$$X_t = L_t \cdot T_t \cdot S_t \cdot \epsilon_t$$

#### Seasonal Decomposition of Time Series (STL) Forecasting

- **STL decomposition** splits a series into **trend ($T_t$)**, **seasonal ($S_t$)**, and **residual ($R_t$)** components.
- The **decomposition step** isolates each component to allow for independent modeling.
- **Forecasting each component separately** ensures flexibility in handling non-linear trends and complex seasonality.
- The final forecast is obtained by **recombining components** as:  

$$\hat{X}_t = \hat{T}_t + \hat{S}_t + \hat{R}_t \quad \text{(additive)} \quad \text{or} \quad \hat{X}_t = \hat{T}_t \cdot \hat{S}_t \cdot \hat{R}_t \quad \text{(multiplicative)}$$

##### Example

To illustrate STL decomposition, we'll generate a synthetic time series dataset that exhibits clear seasonal patterns, trends, and some random noise. We'll then apply STL decomposition to this data and visualize the components.

This plot shows the original synthetic time series data, combining seasonal, trend, and noise components.

![output(3)](https://github.com/djeada/Statistics-Notes/assets/37275728/b10c0196-3455-4c59-8807-a64d11ebc651)

The original data exhibits an upward trend with clear seasonal fluctuations and some random noise. This visualization helps in understanding the overall structure and patterns in the time series.

By performing STL decomposition, we can separately analyze the trend, seasonal, and residual components, providing insights into the underlying structure of the time series data. This technique is particularly useful for identifying patterns and making more accurate forecasts.

![output(4)](https://github.com/djeada/Statistics-Notes/assets/37275728/6cd784df-8e35-411c-92bd-f94b9529e191)

**Seasonal Component**:

- The plot description shows the **seasonal fluctuations** in the data, which repeat annually.
- It shows **repeating yearly pattern**, demonstrating the synthetic seasonal effect added to the data, and shows how the values fluctuate within each year.

**Trend Component**:

- The plot description represents the **long-term progression** of the data over the entire period.
- It reveals a clear **upward trajectory**, indicating a consistent increase in the data over time, which aligns with the linear trend added to the synthetic data.

**Residual Component**:

- The plot description displays the residuals, showing the **remaining variations** in the data after removing the trend and seasonal components.
- The residual component reflects **random noise**. Ideally, it shows no discernible pattern, suggesting that the trend and seasonality have been effectively removed, with residuals randomly distributed around zero, confirming that the decomposition has captured the main patterns in the data.
