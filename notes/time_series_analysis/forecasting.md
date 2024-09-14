## Forecasting with Time Series

Time series forecasting is a technique used to predict future values based on historical data. It is widely used in various fields, such as finance, economics, and meteorology. In this section, we will discuss the basics of time series forecasting.

### Components of a Time Series

A time series can be decomposed into four main components:

I. **Trend** represents the long-term progression of the series, signifying a persistent, general direction of the data over a long period. It can be upward, downward, or even a stable trend.

![output(3)](https://github.com/user-attachments/assets/e13025a4-6bef-42ed-965e-4ddb3c2145b0)

II. **Seasonality** are patterns that repeat at regular intervals, like daily, monthly, or quarterly. This component reflects the influence of seasonal factors on the time series.

![output(4)](https://github.com/user-attachments/assets/13340698-294d-41a9-ab0f-95e7e1b9bb82)

III. Unlike seasonality, **cyclical** patterns occur at less regular intervals. These fluctuations are often linked to economic, political, or even environmental factors and can span multiple years.

![output(7)](https://github.com/user-attachments/assets/92f432e5-92af-42fa-bf1e-4bf8c39bd8fc)

IV. **Random (or Irregular)** component captures the 'noise' or random variation in the data. It represents the unpredictable, erratic factors affecting the time series after the trend, seasonality, and cyclical components have been accounted for.

![output(6)](https://github.com/user-attachments/assets/a96bd328-82b5-4e39-9cba-f008dbaf57dc)

### Forecasting Methods

There are various methods for time series forecasting, each suited to specific scenarios and data characteristics. Here are some commonly used methods:

#### Naive Forecast

This method assumes that the next value in the time series will be equal to the most recent value.

If `y` is the time series and `t` is an index to time, the naive forecast for time `t+1` is simply the value at time `t`.

$$
\hat{y}_{t+1} = y_t
$$

####  Simple Exponential Smoothing (SES)

**Simple Exponential Smoothing (SES)** is a method used for forecasting univariate time series data without a trend or seasonal component. Unlike methods that weight each past observation equally, SES assigns exponentially decreasing weights to past observations, giving more importance to recent data. The method is especially suitable for data that follows a pattern that is approximately flat with noise around a constant level.

The formula for SES is:

$$
\hat{x}_{t+1} = \alpha x_t + (1 - \alpha) \hat{x}_t
$$

where:

- $\hat{x}_{t+1}$ is the forecast for the next time period.
- $x_t$ is the actual observation at time $t$.
- $\hat{x}_t$ is the forecast for time $t$ made at time $t-1$.
- $\alpha$ is the smoothing parameter, $0 < \alpha \leq 1$, which determines the rate of smoothing. A higher $\alpha$ gives more weight to recent observations.

SES can be thought of as a weighted average of past observations, where the weights decrease exponentially as we move further into the past. This means that more recent observations are weighted more heavily than older ones.

For example, for any time $t$, we can recursively substitute the previous forecasts:

$$
\hat{x}_{t+1} = \alpha x_t + (1 - \alpha)\left[\alpha x_{t-1} + (1 - \alpha)\hat{x}_{t-1}\right]
$$

Expanding this equation:

$$
\hat{x}_{t+1} = \alpha x_t + \alpha(1 - \alpha) x_{t-1} + \alpha(1 - \alpha)^2 x_{t-2} + \ldots
$$

This shows that the forecast is a weighted average of all previous observations, with the weights decreasing exponentially at the rate $1 - \alpha$.

The sum of the weights converges to 1, ensuring the method remains stable.

##### Initial Condition

To initialize the process, we need a starting point for the forecast, $\hat{x}_1$. One common approach is to set the initial forecast equal to the first data point:

$$
\hat{x}_1 = x_1
$$

Alternatively, we can use the average of the first few data points as the initial value.

##### Forecast Error

The forecast error at any time $t$ is the difference between the actual observation and the forecast made at time $t-1$:

$$
e_t = x_t - \hat{x}_t
$$

The aim of SES is to minimize the sum of squared errors over time. We can use this to find the optimal value of $\alpha$.

##### Sum of Squared Errors (SSE)

The **Sum of Squared Errors (SSE)** is a measure of the total error in the model, which we aim to minimize when choosing the best smoothing parameter $\alpha$. The SSE is defined as:

$$
SSE(\alpha) = \sum_{t=1}^{n} (x_t - \hat{x}_t)^2
$$

For different values of $\alpha$, we compute the SSE and select the $\alpha$ that minimizes this sum.

##### Choosing the Optimal Smoothing Parameter

The choice of $\alpha$ determines how much weight we give to recent observations versus older ones:

- **If $\alpha$ is close to 1**, most of the weight is placed on the most recent observation, making the method highly reactive to new data and suitable for rapidly changing time series.
- **If $\alpha$ is close to 0**, the forecast gives more weight to older observations, making the method less sensitive to recent fluctuations.

In practice, $\alpha$ is usually chosen by minimizing the SSE using a grid search or another optimization technique.

##### Recursive Form of SES

SES is often expressed in a **recursive form**, which is computationally efficient:

$$
\hat{x}_{t+1} = \alpha x_t + (1 - \alpha) \hat{x}_t
$$

This recursive equation updates the forecast at time $t+1$ based on the observed value at time $t$ and the forecast made for time $t$. It requires minimal computational resources and is easy to implement programmatically.

#### Holt’s Linear Trend Method (Double Exponential Smoothing)

- **Holt’s Linear Trend Model** extends SES to handle data with a linear trend. It introduces a second smoothing equation to account for the trend in the time series.
- The method smooths both the level and the trend of the series.

Holt's model has two equations: one for the level and one for the trend.

**Level equation**:

$$
\ell_t = \alpha x_t + (1 - \alpha)(\ell_{t-1} + b_{t-1})
$$

where:

- $\ell_t$ is the level (smoothed value) at time $t$,
- $b_t$ is the trend (slope) at time $t$,
- $\alpha$ is the smoothing parameter for the level.

**Trend equation**:

$$
b_t = \beta (\ell_t - \ell_{t-1}) + (1 - \beta) b_{t-1}
$$

where:

- $\beta$ is the smoothing parameter for the trend.

**Forecast equation**:

$$
\hat{x}_{t+h} = \ell_t + h b_t
$$

where:

- $\hat{x}_{t+h}$ is the forecast $h$ periods ahead,
- $h$ is the forecast horizon.

- The initial level ($\ell_1$) is typically set as the first observation $x_1$.
- The initial trend ($b_1$) can be estimated as the difference between the first two observations:

$$
b_1 = x_2 - x_1
$$

- Holt’s method **captures trends** effectively and is ideal for time series with a constant linear trend.
- There are **two smoothing parameters** in Holt’s method: $\alpha$ for controlling level smoothing and $\beta$ for controlling trend smoothing.
- In **sales forecasting**, companies use Holt’s method to predict sales data that follows a linear growth or decline over time.
- For **revenue prediction**, Holt’s method is useful for forecasting revenue in businesses experiencing steady growth.

#### Holt-Winters Seasonal Method (Triple Exponential Smoothing)

- The **Holt-Winters method** extends Holt’s Linear Trend Model by introducing a third equation to model the seasonal component in the time series, making it suitable for data with seasonality.
- With the **Holt-Winters method**, you can handle time series data that exhibits both trend and seasonality, making it a powerful tool for more complex forecasting scenarios.
- An **additive model** is used when the seasonal variation in the time series remains roughly constant over time.
- A **multiplicative model** is appropriate when the seasonal variation increases or decreases proportionally with the level of the series.

##### **Additive Model**:

**Level equation**:

$$
\ell_t = \alpha \frac{x_t}{s_{t-L}} + (1 - \alpha)(\ell_{t-1} + b_{t-1})
$$

where:

- $\ell_t$ is the smoothed level at time $t$,
- $b_t$ is the trend at time $t$,
- $s_t$ is the seasonal component,
- $L$ is the length of the seasonal cycle (e.g., 12 months or 4 quarters).

**Trend equation**:

$$
b_t = \beta (\ell_t - \ell_{t-1}) + (1 - \beta) b_{t-1}
$$

**Seasonality equation**:

$$
s_t = \gamma \frac{x_t}{\ell_t} + (1 - \gamma) s_{t-L}
$$

where:

- $\gamma$ is the smoothing parameter for the seasonal component.

**Forecast equation**:

$$
\hat{x}_{t+h} = (\ell_t + h b_t) s_{t+h-L(k+1)}
$$

where:

- $h$ is the forecast horizon, $L$ is the seasonal period.

##### **Multiplicative Model**:

**Level equation**:

$$
\ell_t = \alpha (x_t - s_{t-L}) + (1 - \alpha)(\ell_{t-1} + b_{t-1})
$$

**Trend equation**:

$$
b_t = \beta (\ell_t - \ell_{t-1}) + (1 - \beta) b_{t-1}
$$

**Seasonality equation**:

$$
s_t = \gamma (x_t - \ell_t) + (1 - \gamma) s_{t-L}
$$

**Forecast equation**:

$$
\hat{x}_{t+h} = (\ell_t + h b_t) \times s_{t+h-L(k+1)}
$$

- The **level** of a time series can initially be set as the average of the first season's observations, denoted as $\ell_1$.
- For the **trend**, the initial value $b_1$ can be estimated by averaging the first differences in the data.
- To calculate **seasonality**, the initial seasonal components $s_1$ to $s_L$ are estimated by averaging observations within each season and subtracting the overall mean.
- The choice between **additive vs. multiplicative** models depends on the data; additive is used when seasonal amplitude is constant, while multiplicative handles cases where seasonal variation changes with the level.
- There are **three smoothing parameters**: $\alpha$ for the level, $\beta$ for the trend, and $\gamma$ for the seasonality.
- In **retail forecasting**, demand is predicted for products with seasonal sales patterns, such as those seen during holiday sales or back-to-school periods.
- **Energy consumption forecasting** focuses on predicting energy usage patterns with seasonal fluctuations, such as the demand for electricity or gas.
  
### Machine Learning for Time Series Forecasting

Machine learning (ML) has become increasingly popular for time series forecasting, especially as data grows more complex and requires non-linear methods. Traditional statistical approaches like ARIMA work well for simpler datasets, but machine learning can handle complex patterns, high-dimensionality, and non-linear relationships better. In this overview, we'll cover key machine learning models used for time series forecasting, with detailed explanations of each approach.

#### Key Challenges in Time Series Forecasting

Machine learning algorithms for time series forecasting face several challenges:

- The **temporal dependency** in time series data indicates that current values depend on past values, so the data cannot be treated as independent observations.
- **Stationarity** is often assumed in many models, meaning the statistical properties of the time series, like mean and variance, remain constant over time.
- Time series frequently exhibit **seasonality and trends**, with recurring seasonal patterns or trends that need to be effectively modeled.

To address these challenges, various machine learning models and techniques can be employed.

#### 1. Supervised Learning Approach for Time Series

In a **supervised learning framework** for time series forecasting, we aim to transform the time series problem into a regression task where:

- **Input features** (X) are the lagged values (past observations),
- **Target variable** (Y) is the future value we want to predict.

For example, to predict the value at time $t$, the features might be the values at times $t-1, t-2, \ldots, t-n$.

##### **Data Preparation (Feature Engineering for Time Series)**

1. The **lag features** are essential in time series analysis and include past values of the time series. Example: To predict the value of $y_t$, we can use past values like $y_{t-1}, y_{t-2}, \ldots$ as input features.
2. **Windowed features** summarize past values over a specific window, such as calculating the mean, variance, or sum over the last 7 days.
3. **Time-based features** include details like month, year, weekday, and hour, helping capture seasonality or periodic trends.
4. Using **rolling/aggregated statistics**, such as moving averages or rolling sums, provides useful features by aggregating data over time windows.

#### 2. Machine Learning Models for Time Series Forecasting

- Models like **decision trees** split data based on conditions, creating a tree-like structure where each split aims to minimize error for the target variable, such as predicting the future value of a time series.
- A **random forest** is an ensemble method that combines multiple decision trees, each trained on different data subsets, and averages their results to improve robustness and reduce overfitting.
- In the approach of **time series as a supervised learning problem**, lagged values (past observations) are used as features to predict the next value, with the model learning the relationships between past lags and the future outcome.
- One of the **advantages** of this method is that it handles non-linear relationships, is robust to outliers, and can model interactions between lagged variables.
- However, its **disadvantages** include not directly modeling temporal dependencies and lacking the ability to handle autoregressive forecasting natively.

Example:

```python
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Assuming 'data' is a Pandas DataFrame with time series values in the column 'value'
# Create lag features
data['lag1'] = data['value'].shift(1)
data['lag2'] = data['value'].shift(2)
data.dropna(inplace=True)

# Train-test split
train_size = int(len(data) * 0.8)
train, test = data.iloc[:train_size], data.iloc[train_size:]

# Train Random Forest Regressor
X_train, y_train = train[['lag1', 'lag2']], train['value']
X_test, y_test = test[['lag1', 'lag2']], test['value']

rf_model = RandomForestRegressor(n_estimators=100)
rf_model.fit(X_train, y_train)

# Predict future values
predictions = rf_model.predict(X_test)
```

##### 2.2 Gradient Boosting Machines (GBM, XGBoost, LightGBM, CatBoost)

- **Gradient Boosting** builds an ensemble of trees sequentially, where each tree attempts to correct the errors of the previous trees. This process allows it to model complex, non-linear relationships effectively.
- **XGBoost**, **LightGBM**, and **CatBoost** are advanced implementations of gradient boosting, each optimized for speed and performance.
- Like Random Forests, lagged values and windowed features are used to predict future values. However, Gradient Boosting models tend to perform better than Random Forests on many time series tasks because they can better model complex relationships between features.
- Handles missing data.
- Models non-linearities and interactions between features.
- Offers state-of-the-art performance on many time series datasets.
- Requires careful tuning to avoid overfitting.
- Computationally expensive compared to simpler models.

Example Using XGBoost:

```python
import xgboost as xgb
import numpy as np

# Train XGBoost Regressor
xgb_model = xgb.XGBRegressor(n_estimators=100, max_depth=3, learning_rate=0.1)
xgb_model.fit(X_train, y_train)

# Predict future values
predictions = xgb_model.predict(X_test)
```

##### 2.3 Support Vector Machines (SVM)

- **Support Vector Machines (SVMs)** are typically used for classification but can also be adapted for regression (SVR - Support Vector Regression). SVM works by finding the best boundary (or hyperplane) between data points to minimize the prediction error.
- For time series forecasting, lagged values are used as input features to predict future values. The SVR algorithm learns the relationship between lagged values and future outcomes using a kernel trick to model non-linear relationships.
- Effective in high-dimensional spaces.
- Can model non-linear relationships via kernel functions (e.g., RBF kernel).
- Computationally expensive for large datasets.
- Sensitive to feature scaling and requires careful tuning of kernel parameters.

Example:

```python
from sklearn.svm import SVR

# Train Support Vector Regressor
svr_model = SVR(kernel='rbf', C=100, gamma=0.1)
svr_model.fit(X_train, y_train)

# Predict future values
predictions = svr_model.predict(X_test)
```

##### 2.4 Artificial Neural Networks (ANN)

- **Artificial Neural Networks (ANNs)** are a type of machine learning algorithm inspired by the human brain. They consist of layers of interconnected "neurons" that can learn complex patterns in data.
- For time series, ANNs are used to predict future values based on past values.
- The input to an ANN for time series forecasting is typically a set of lagged values. The ANN learns to map these inputs to the future target values using backpropagation and gradient descent.
- Highly flexible and can model complex, non-linear relationships.
- Can be combined with other models for hybrid approaches.
- Requires a lot of data to train effectively.
- Prone to overfitting if not properly regularized.
- Requires significant computational resources.

Example:

```python
from sklearn.neural_network import MLPRegressor

# Train a Multi-Layer Perceptron Regressor (ANN)
mlp_model = MLPRegressor(hidden_layer_sizes=(100,), activation='relu', solver='adam', max_iter=1000)
mlp_model.fit(X_train, y_train)

# Predict future values
predictions = mlp_model.predict(X_test)
```

#### 3. Advanced Neural Network Models for Time Series

- **Recurrent Neural Networks (RNNs)** are designed specifically for sequential data like time series. Unlike traditional neural networks, RNNs maintain a "memory" of previous inputs, making them suitable for tasks where temporal order is important.
- RNNs process the time series sequentially, passing information from one step to the next. This allows the model to learn dependencies between different time steps.
- Handles long-term dependencies in time series.
- Suitable for complex sequences with temporal dependencies.
- Prone to vanishing gradient problems, which makes it hard to learn long-term dependencies.
  
Example:
 
```python
import tensorflow as tf

# Define a simple RNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.SimpleRNN(50, activation='relu', input_shape=(n_timesteps, n_features)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32)
```

##### 3.2 Long Short-Term Memory (LSTM)

- **Long Short-Term Memory (LSTM)** networks are a type of RNN designed to overcome the limitations of standard RNNs, particularly the problem of vanishing gradients. LSTMs can capture long-term dependencies in time series data, making them highly effective for time series forecasting.
- LSTM networks maintain a memory cell that can learn which information to keep or discard over long periods of time. This allows LSTMs to model long-range dependencies in sequential data.
- Effective for long-term dependencies.
- Can model non-linear relationships and capture complex temporal patterns.
- Computationally expensive and requires large datasets.
- Requires careful tuning of hyperparameters.

Example Using LSTM:

```python
import tensorflow as tf

# Reshape the data for LSTM (samples, timesteps, features)
X_train_reshaped = X_train.values.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test_reshaped = X_test.values.reshape((X_test.shape[0], X_test.shape[1], 1))

# Define LSTM model
model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(50, activation='relu', input_shape=(X_train_reshaped.shape[1], X_train_reshaped.shape[2])),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train_reshaped, y_train, epochs=100, batch_size=32)

# Predict future values
predictions = model.predict(X_test_reshaped)
```

##### 3.3 Gated Recurrent Units (GRU)

- **Gated Recurrent Units (GRUs)** are similar to LSTMs but with a simplified structure. GRUs are often faster to train than LSTMs and perform comparably in many time series tasks.
- Less computationally expensive than LSTMs.
- Suitable for both short-term and long-term dependencies.

Example Using GRU:

```python
import tensorflow as tf

# Define a GRU model
model = tf.keras.models.Sequential([
    tf.keras.layers.GRU(50, activation='relu', input_shape=(n_timesteps, n_features)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32)
```

#### 4. Hybrid Models

In practice, many machine learning models for time series forecasting combine traditional statistical models with machine learning models. For instance:

- The combination of **ARIMA + Neural Network** involves using ARIMA to handle the linear components while a neural network models the non-linear residuals.
- By using **XGBoost + LSTM**, gradient boosting models like XGBoost can capture short-term patterns, while LSTM networks handle long-term dependencies.

### Comparison of Various Models

The table below compares several time series forecasting algorithms, highlighting their descriptions, advantages, disadvantages, and whether they can be applied locally or globally:

| Algorithm Name | Description | Pros | Cons | Local vs Global |
|----------------|-------------|------|------|-----------------|
| **ARIMA (AutoRegressive Integrated Moving Average)** | A statistical model used for analyzing and forecasting time series data by using the dependencies between an observation and a number of lagged observations. | - Flexible and capable of handling a wide range of time series patterns. <br> - Suitable for univariate time series data. | - Complex to understand and implement. <br> - Requires the data to be stationary. <br> - Sensitive to the chosen parameters. <br> - AutoARIMA can alleviate some implementation challenges but still requires expertise. | Local only. Cannot be used globally. |
| **Prophet** | Developed by Facebook, this algorithm is tailored for forecasting time series data with daily observations that include strong seasonal effects and the presence of outliers. | - Easy to use with intuitive parameter settings. <br> - Automatically handles missing data and outliers well. <br> - Provides a simple and interpretable result. | - Less effective for non-daily data or data without strong seasonality. <br> - Requires domain knowledge to fine-tune accurately. <br> - Has faced criticism after issues with high-profile predictions (e.g., Zillow collapse). | Local only. Cannot be used globally. |
| **LSTM (Long Short-Term Memory)** | A type of recurrent neural network (RNN) that is well-suited for learning from sequences and time series data, capable of capturing long-term dependencies. | - Excellent at capturing long-term dependencies and patterns in time series data. <br> - Can handle large and complex datasets. | - Requires substantial amounts of data for training. <br> - Computationally intensive and can be slow to train. <br> - Complex architecture that requires careful tuning of hyperparameters. | Can be used locally or globally. |
| **Holt-Winters Method** | A time series forecasting method that accounts for level, trend, and seasonality by applying exponential smoothing. | - Good for data with trend and seasonal patterns. <br> - Straightforward and relatively easy to implement. | - May not perform well on non-seasonal data. <br> - Sensitive to parameter choices and initial settings. | Local only. Cannot be used globally. |
| **SARIMA (Seasonal ARIMA)** | An extension of ARIMA that includes seasonal components, enabling it to handle seasonal effects in the data. | - Capable of handling both trend and seasonality in the data. <br> - Flexible model structure that can be tailored to specific time series characteristics. | - Complex to configure and requires a thorough understanding of time series analysis. <br> - Data must be stationary, requiring transformations. <br> - AutoARIMA can assist but still demands expertise. | Local only. Cannot be used globally. |
| **Exponential Smoothing** | A forecasting technique that applies weighted averages to past observations, with the weights decaying exponentially over time. | - Simple to implement and use. <br> - Effective for data without clear trend or seasonal patterns. | - May not be accurate for more complex data involving trends and seasonality. <br> - Struggles with data exhibiting sudden changes or volatility. | Local only. Cannot be used globally. |
| **Random Forest** | An ensemble learning method using multiple decision trees to improve predictive performance and robustness. | - Handles a wide variety of data types and is robust to outliers. <br> - Can detect complex interactions and dependencies in the data. | - Computationally intensive, especially for large datasets. <br> - Can overfit if not properly tuned. <br> - Does not extrapolate beyond the range of training data. | Can be used locally or globally. |
| **XGBoost** | A highly efficient and scalable implementation of gradient boosting, particularly effective for structured data and competitions. | - High performance with excellent predictive power. <br> - Handles a wide range of data types well, including complex seasonality. <br> - Offers extensive tuning options and regularization techniques to improve accuracy. | - Can be complex to tune and requires careful parameter selection to avoid overfitting. <br> - Computationally demanding. <br> - Cannot predict values outside the range of training data (above max or below min). | Can be used locally or globally. |

### Model Evaluation
When evaluating the accuracy and performance of time series forecasting models like **Simple Exponential Smoothing (SES)**, **Holt-Winters**, **ARIMA**, and others, there are several widely used metrics that help assess how well the model predictions match the actual data. Here are the key evaluation metrics commonly employed:

| **Metric**                           | **Definition**                                                                                                                                                                         | **Formula**                                                                                          | **Interpretation**                                                                                                                                                                                            |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Mean Absolute Error (MAE)**         | Measures the average of the absolute differences between predicted and actual values.                                                                                               | $MAE = \frac{1}{n} \sum_{t=1}^{n} |y_t - \hat{y}_t| $                                                                      | MAE gives a clear, easy-to-interpret sense of the error magnitude but doesn’t penalize large errors as much as other metrics like MSE.                                                                         |
| **Mean Squared Error (MSE)**          | The average of the squared differences between predicted and actual values.                                                                                                          | $MSE = \frac{1}{n} \sum_{t=1}^{n} (y_t - \hat{y}_t)^2$                                           | MSE penalizes larger errors more than MAE, making it useful when large errors are particularly undesirable. However, it is sensitive to outliers.                                                             |
| **Root Mean Squared Error (RMSE)**    | The square root of the mean squared error, often used to bring the error metric back to the original scale of the data.                                                              | $RMSE = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (y_t - \hat{y}_t)^2}$                                  | RMSE is more sensitive to outliers than MAE and is commonly used because it provides an error measure in the same units as the original data.                                                                  |
| **Mean Absolute Percentage Error (MAPE)**| Measures the percentage error by calculating the ratio of the absolute forecast error to the actual value.                                                                          | $MAPE = \frac{1}{n} \sum_{t=1}^{n} \left| \frac{y_t - \hat{y}_t}{y_t} \right| \times 100$        | MAPE provides a percentage-based error, making it easier to interpret across different datasets. However, it can be problematic when actual values are close to zero.                                          |
| **Symmetric Mean Absolute Percentage Error (sMAPE)**| A variation of MAPE that accounts for the symmetry in the error measurement, avoiding the issue of dividing by small actual values.                                                  | $sMAPE = \frac{1}{n} \sum_{t=1}^{n} \frac{|y_t - \hat{y}_t|}{(|y_t| + |\hat{y}_t|)/2} \times 100$ | sMAPE addresses the shortcomings of MAPE by taking both actual and predicted values into account and is widely used in time series forecasting.                                                                |
| **Akaike Information Criterion (AIC)**| Used for model selection, the AIC balances the goodness-of-fit of the model with its complexity. Lower AIC values indicate better models, but it penalizes models with more parameters.| $AIC = 2k - 2\ln(L)$                                                                            | AIC is useful for comparing different models, especially in determining the trade-off between model fit and simplicity.                                                                                         |
| **Bayesian Information Criterion (BIC)**| Similar to AIC but includes a stronger penalty for models with more parameters, making it more suitable when the number of data points is small.                                      | $BIC = k \ln(n) - 2\ln(L)$                                                                      | BIC penalizes model complexity, often yielding more conservative models than AIC, and is useful when the dataset is small.                                                                                      |
| **Ljung-Box Q-test**                  | A statistical test that checks whether the residuals from a time series forecasting model exhibit any remaining autocorrelation. If the residuals are white noise, the model is adequate.| N/A                                                                                                  | If the test indicates significant autocorrelation in the residuals, the model may not fully capture the time series' structure.                                                                                 |
