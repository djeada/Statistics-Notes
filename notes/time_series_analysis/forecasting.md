## Forecasting with Time Series

Time series forecasting is a technique used to predict future values based on historical data. It is widely used in various fields, such as finance, economics, and meteorology. In this section, we will discuss the basics of time series forecasting.

### Components of a Time Series

A time series can be decomposed into four main components:

1. **Trend**: This represents the long-term progression of the series, signifying a persistent, general direction of the data over a long period. It can be upward, downward, or even a stable trend.

```
^
| Value 
|         __________
|       /
|     /
|   /
| /
|/___________________ Time ->
```

2. **Seasonality**: These are patterns that repeat at regular intervals, like daily, monthly, or quarterly. This component reflects the influence of seasonal factors on the time series.

```
^
| Value
|    /\  /\  /\  /\  /\  
|   /  \/  \/  \/  \/  \ 
|  /                    \
|/_______________________\___ Time ->
```

3. **Cycles**:  Unlike seasonality, cyclical patterns occur at less regular intervals. These fluctuations are often linked to economic, political, or even environmental factors and can span multiple years.

```
^
| Value
|                               ___
|                         ___--     --___
|        ___         ___-                 -
|   __--     --__-                          -__
|_/                                              \_
|__________________________________________________ Time ->
```

4. **Random (or Irregular)**: This component captures the 'noise' or random variation in the data. It represents the unpredictable, erratic factors affecting the time series after the trend, seasonality, and cyclical components have been accounted for.

```
^
| Value
|   .       .  .      .   .   . . 
|  . .    .      .  .    .      . 
|    .      . .   .  . .   .    .
| .    .  .   .     .    .   .   
|________________________________ Time ->
```

### Forecasting Methods

There are various methods for time series forecasting, each suited to specific scenarios and data characteristics. Here are some commonly used methods:

#### Naive Forecast

This method assumes that the next value in the time series will be equal to the most recent value.

If `y` is the time series and `t` is an index to time, the naive forecast for time `t+1` is simply the value at time `t`.

$$
\hat{y}_{t+1} = y_t
$$

###  Simple Exponential Smoothing (SES)

#### **1. Overview of SES**
**Simple Exponential Smoothing (SES)** is a method used for forecasting univariate time series data without a trend or seasonal component. Unlike methods that weight each past observation equally, SES assigns exponentially decreasing weights to past observations, giving more importance to recent data. The method is especially suitable for data that follows a pattern that is approximately flat with noise around a constant level.

The formula for SES is:
\[
\hat{x}_{t+1} = \alpha x_t + (1 - \alpha) \hat{x}_t
\]
where:
- \(\hat{x}_{t+1}\) is the forecast for the next time period.
- \(x_t\) is the actual observation at time \(t\).
- \(\hat{x}_t\) is the forecast for time \(t\) made at time \(t-1\).
- \(\alpha\) is the smoothing parameter, \(0 < \alpha \leq 1\), which determines the rate of smoothing. A higher \(\alpha\) gives more weight to recent observations.

#### **2. SES as a Weighted Average**
SES can be thought of as a weighted average of past observations, where the weights decrease exponentially as we move further into the past. This means that more recent observations are weighted more heavily than older ones.

For example, for any time \(t\), we can recursively substitute the previous forecasts:
\[
\hat{x}_{t+1} = \alpha x_t + (1 - \alpha)\left[\alpha x_{t-1} + (1 - \alpha)\hat{x}_{t-1}\right]
\]
Expanding this equation:
\[
\hat{x}_{t+1} = \alpha x_t + \alpha(1 - \alpha) x_{t-1} + \alpha(1 - \alpha)^2 x_{t-2} + \ldots
\]
This shows that the forecast is a weighted average of all previous observations, with the weights decreasing exponentially at the rate \(1 - \alpha\).

The sum of the weights converges to 1, ensuring the method remains stable.

#### **3. Initial Condition**
To initialize the process, we need a starting point for the forecast, \(\hat{x}_1\). One common approach is to set the initial forecast equal to the first data point:
\[
\hat{x}_1 = x_1
\]
Alternatively, we can use the average of the first few data points as the initial value.

#### **4. Forecast Error**
The forecast error at any time \(t\) is the difference between the actual observation and the forecast made at time \(t-1\):
\[
e_t = x_t - \hat{x}_t
\]
The aim of SES is to minimize the sum of squared errors over time. We can use this to find the optimal value of \(\alpha\).

#### **5. Sum of Squared Errors (SSE)**
The **Sum of Squared Errors (SSE)** is a measure of the total error in the model, which we aim to minimize when choosing the best smoothing parameter \(\alpha\). The SSE is defined as:
\[
SSE(\alpha) = \sum_{t=1}^{n} (x_t - \hat{x}_t)^2
\]
For different values of \(\alpha\), we compute the SSE and select the \(\alpha\) that minimizes this sum.

### **Choosing the Optimal Smoothing Parameter (\(\alpha\))**

The choice of \(\alpha\) determines how much weight we give to recent observations versus older ones:
- **If \(\alpha\) is close to 1**: We place most of the weight on the most recent observation. This approach is highly reactive to new data and can work well if the time series changes rapidly.
- **If \(\alpha\) is close to 0**: The forecast places more weight on older observations, and the method becomes less sensitive to recent fluctuations.

In practice, \(\alpha\) is usually chosen by minimizing the SSE using a grid search or another optimization technique.

### **6. Recursive Form of SES**
SES is often expressed in a **recursive form**, which is computationally efficient:
\[
\hat{x}_{t+1} = \alpha x_t + (1 - \alpha) \hat{x}_t
\]
This recursive equation updates the forecast at time \(t+1\) based on the observed value at time \(t\) and the forecast made for time \(t\). It requires minimal computational resources and is easy to implement programmatically.

### **7. Generalization to Exponential Smoothing**
Simple Exponential Smoothing (SES) can be generalized to handle time series with trends and seasonality:
- **Holt’s Linear Trend Method**: Extends SES to include a trend component.
- **Holt-Winters Seasonal Method**: Extends SES to include both trend and seasonality.

Both of these methods use exponential smoothing for different components (level, trend, and seasonality) and are widely used in more complex time series forecasting.


### **Detailed Overview of Exponential Smoothing Methods**

Exponential Smoothing Methods are widely used for time series forecasting due to their simplicity and effectiveness. These methods assume that more recent observations are more relevant for forecasting than older ones, and they assign exponentially decreasing weights to past observations. There are several variations of exponential smoothing methods depending on the presence of trends and seasonality in the data.


### **2. Holt’s Linear Trend Method (Double Exponential Smoothing)**

#### **Overview**:
- **Holt’s Linear Trend Model** extends SES to handle data with a linear trend. It introduces a second smoothing equation to account for the trend in the time series.
- The method smooths both the level and the trend of the series.

#### **Formulas**:
Holt's model has two equations: one for the level and one for the trend.

- **Level equation**:
\[
\ell_t = \alpha x_t + (1 - \alpha)(\ell_{t-1} + b_{t-1})
\]
  - \(\ell_t\) is the level (smoothed value) at time \(t\),
  - \(b_t\) is the trend (slope) at time \(t\),
  - \(\alpha\) is the smoothing parameter for the level.

- **Trend equation**:
\[
b_t = \beta (\ell_t - \ell_{t-1}) + (1 - \beta) b_{t-1}
\]
  - \(\beta\) is the smoothing parameter for the trend.

- **Forecast equation**:
\[
\hat{x}_{t+h} = \ell_t + h b_t
\]
  - \(\hat{x}_{t+h}\) is the forecast \(h\) periods ahead,
  - \(h\) is the forecast horizon.

#### **Initial Conditions**:
- The initial level (\(\ell_1\)) is typically set as the first observation \(x_1\).
- The initial trend (\(b_1\)) can be estimated as the difference between the first two observations:
  \[
  b_1 = x_2 - x_1
  \]

#### **Characteristics**:
- **Captures trends**: Holt’s method is ideal for time series with a constant linear trend.
- **Two smoothing parameters**: \(\alpha\) controls the level smoothing, and \(\beta\) controls the trend smoothing.

#### **Use Cases**:
- **Sales forecasting**: Companies use Holt’s method to forecast sales data that shows a linear growth or decline over time.
- **Revenue prediction**: Holt’s method can predict revenue for businesses experiencing steady growth.

---

### **3. Holt-Winters Seasonal Method (Triple Exponential Smoothing)**

#### **Overview**:
- **Holt-Winters method** extends Holt’s Linear Trend Model to account for seasonality. It introduces a third equation to model the seasonal component in the time series.
- The Holt-Winters method can handle data with both trend and seasonality, making it a powerful tool for more complex forecasting scenarios.

There are two versions of the Holt-Winters method:
  - **Additive Model**: For time series where the seasonal variation is roughly constant over time.
  - **Multiplicative Model**: For time series where the seasonal variation increases or decreases proportionally with the level of the series.

#### **Formulas**:

##### **Additive Model**:
1. **Level equation**:
   \[
   \ell_t = \alpha \frac{x_t}{s_{t-L}} + (1 - \alpha)(\ell_{t-1} + b_{t-1})
   \]
   - \(\ell_t\) is the smoothed level at time \(t\),
   - \(b_t\) is the trend at time \(t\),
   - \(s_t\) is the seasonal component,
   - \(L\) is the length of the seasonal cycle (e.g., 12 months or 4 quarters).

2. **Trend equation**:
   \[
   b_t = \beta (\ell_t - \ell_{t-1}) + (1 - \beta) b_{t-1}
   \]

3. **Seasonality equation**:
   \[
   s_t = \gamma \frac{x_t}{\ell_t} + (1 - \gamma) s_{t-L}
   \]
   - \(\gamma\) is the smoothing parameter for the seasonal component.

4. **Forecast equation**:
   \[
   \hat{x}_{t+h} = (\ell_t + h b_t) s_{t+h-L(k+1)}
   \]
   - \(h\) is the forecast horizon, \(L\) is the seasonal period.

##### **Multiplicative Model**:
1. **Level equation**:
   \[
   \ell_t = \alpha (x_t - s_{t-L}) + (1 - \alpha)(\ell_{t-1} + b_{t-1})
   \]

2. **Trend equation**:
   \[
   b_t = \beta (\ell_t - \ell_{t-1}) + (1 - \beta) b_{t-1}
   \]

3. **Seasonality equation**:
   \[
   s_t = \gamma (x_t - \ell_t) + (1 - \gamma) s_{t-L}
   \]

4. **Forecast equation**:
   \[
   \hat{x}_{t+h} = (\ell_t + h b_t) \times s_{t+h-L(k+1)}
   \]

#### **Initial Conditions**:
- **Level**: The initial level \(\ell_1\) can be set as the average of the first season's observations.
- **Trend**: The initial trend \(b_1\) can be estimated by averaging the first differences.
- **Seasonality**: The initial seasonal components \(s_1\) to \(s_L\) can be estimated by averaging the observations in each season and subtracting the overall mean.

#### **Characteristics**:
- **Additive vs. Multiplicative**: Additive is for data with constant seasonal amplitude, while multiplicative is for data where seasonal variation changes with the level.
- **Three smoothing parameters**: \(\alpha\) for the level, \(\beta\) for the trend, and \(\gamma\) for the seasonality.

#### **Use Cases**:
- **Retail forecasting**: Predicting demand for products with seasonal sales patterns, such as holiday sales or back-to-school items.
- **Energy consumption forecasting**: Forecasting energy usage with seasonal patterns, such as electricity or gas demand.

  
### **Machine Learning for Time Series Forecasting**

Machine learning (ML) has become increasingly popular for time series forecasting, especially as data grows more complex and requires non-linear methods. Traditional statistical approaches like ARIMA work well for simpler datasets, but machine learning can handle complex patterns, high-dimensionality, and non-linear relationships better. In this overview, we'll cover key machine learning models used for time series forecasting, with detailed explanations of each approach.

### **Key Challenges in Time Series Forecasting**
Machine learning algorithms for time series forecasting face several challenges:
- **Temporal dependency**: Time series data is dependent on past values, meaning time series cannot be treated as independent observations.
- **Stationarity**: Many models assume the time series is stationary, meaning its statistical properties (mean, variance) do not change over time.
- **Seasonality and trends**: Time series data often has recurring seasonal patterns or trends that need to be modeled effectively.

To address these challenges, various machine learning models and techniques can be employed.

### **1. Supervised Learning Approach for Time Series**

In a **supervised learning framework** for time series forecasting, we aim to transform the time series problem into a regression task where:
- **Input features** (X) are the lagged values (past observations),
- **Target variable** (Y) is the future value we want to predict.

For example, to predict the value at time \( t \), the features might be the values at times \( t-1, t-2, \ldots, t-n \).

#### **Data Preparation (Feature Engineering for Time Series)**
1. **Lag Features**: These are the core features in time series, which include past values of the time series.
   - Example: If we want to predict the value of \( y_t \), we can use \( y_{t-1}, y_{t-2}, \ldots \) as input features.
2. **Windowed Features**: Summarize past values over a certain window (e.g., mean, variance, sum over the last 7 days).
3. **Time-Based Features**: Include date/time features like month, year, weekday, hour, etc. These features help capture seasonality or periodic trends.
4. **Rolling/Aggregated Statistics**: Moving averages, rolling sums, and other aggregated statistics over windows of time are often useful features.

### **2. Machine Learning Models for Time Series Forecasting**

#### **2.1 Decision Trees and Random Forests**

##### **Overview**:
- **Decision Trees**: These models create a tree-like structure where data is split based on conditions. Each split tries to minimize the error for the target variable (e.g., the future value of a time series).
- **Random Forests**: A Random Forest is an ensemble of decision trees, where multiple trees are trained on different subsets of the data, and their results are averaged to improve robustness and reduce overfitting.

##### **How It Works**:
- **Time Series as a Supervised Learning Problem**: Lagged values (past observations) are used as features to predict the next value. The model learns relationships between the past lags and the future value.
- **Advantages**: Handles non-linear relationships, is robust to outliers, and can model interactions between lagged variables.
- **Disadvantages**: Does not directly model temporal dependencies and cannot handle autoregressive forecasting natively.

##### **Example**:
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

#### **2.2 Gradient Boosting Machines (GBM, XGBoost, LightGBM, CatBoost)**

##### **Overview**:
- **Gradient Boosting** builds an ensemble of trees sequentially, where each tree attempts to correct the errors of the previous trees. This process allows it to model complex, non-linear relationships effectively.
- **XGBoost**, **LightGBM**, and **CatBoost** are advanced implementations of gradient boosting, each optimized for speed and performance.

##### **How It Works**:
- Like Random Forests, lagged values and windowed features are used to predict future values. However, Gradient Boosting models tend to perform better than Random Forests on many time series tasks because they can better model complex relationships between features.

##### **Advantages**:
- Handles missing data.
- Models non-linearities and interactions between features.
- Offers state-of-the-art performance on many time series datasets.

##### **Disadvantages**:
- Requires careful tuning to avoid overfitting.
- Computationally expensive compared to simpler models.

##### **Example Using XGBoost**:
```python
import xgboost as xgb
import numpy as np

# Train XGBoost Regressor
xgb_model = xgb.XGBRegressor(n_estimators=100, max_depth=3, learning_rate=0.1)
xgb_model.fit(X_train, y_train)

# Predict future values
predictions = xgb_model.predict(X_test)
```

#### **2.3 Support Vector Machines (SVM)**

##### **Overview**:
- **Support Vector Machines (SVMs)** are typically used for classification but can also be adapted for regression (SVR - Support Vector Regression). SVM works by finding the best boundary (or hyperplane) between data points to minimize the prediction error.

##### **How It Works**:
- For time series forecasting, lagged values are used as input features to predict future values. The SVR algorithm learns the relationship between lagged values and future outcomes using a kernel trick to model non-linear relationships.

##### **Advantages**:
- Effective in high-dimensional spaces.
- Can model non-linear relationships via kernel functions (e.g., RBF kernel).

##### **Disadvantages**:
- Computationally expensive for large datasets.
- Sensitive to feature scaling and requires careful tuning of kernel parameters.

##### **Example**:
```python
from sklearn.svm import SVR

# Train Support Vector Regressor
svr_model = SVR(kernel='rbf', C=100, gamma=0.1)
svr_model.fit(X_train, y_train)

# Predict future values
predictions = svr_model.predict(X_test)
```

#### **2.4 Artificial Neural Networks (ANN)**

##### **Overview**:
- **Artificial Neural Networks (ANNs)** are a type of machine learning algorithm inspired by the human brain. They consist of layers of interconnected "neurons" that can learn complex patterns in data.
- For time series, ANNs are used to predict future values based on past values.

##### **How It Works**:
- The input to an ANN for time series forecasting is typically a set of lagged values. The ANN learns to map these inputs to the future target values using backpropagation and gradient descent.

##### **Advantages**:
- Highly flexible and can model complex, non-linear relationships.
- Can be combined with other models for hybrid approaches.

##### **Disadvantages**:
- Requires a lot of data to train effectively.
- Prone to overfitting if not properly regularized.
- Requires significant computational resources.

##### **Example**:
```python
from sklearn.neural_network import MLPRegressor

# Train a Multi-Layer Perceptron Regressor (ANN)
mlp_model = MLPRegressor(hidden_layer_sizes=(100,), activation='relu', solver='adam', max_iter=1000)
mlp_model.fit(X_train, y_train)

# Predict future values
predictions = mlp_model.predict(X_test)
```

### **3. Advanced Neural Network Models for Time Series**

#### **3.1 Recurrent Neural Networks (RNNs)**
##### **Overview**:
- **Recurrent Neural Networks (RNNs)** are designed specifically for sequential data like time series. Unlike traditional neural networks, RNNs maintain a "memory" of previous inputs, making them suitable for tasks where temporal order is important.
  
##### **How It Works**:
- RNNs process the time series sequentially, passing information from one step to the next. This allows the model to learn dependencies between different time steps.

##### **Advantages**:
- Handles long-term dependencies in time series.
- Suitable for complex sequences with temporal dependencies.

##### **Disadvantages**:
- Prone to vanishing gradient problems, which makes it hard to learn long-term dependencies.
  
##### **Example**:
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

#### **3.2 Long Short-Term Memory (LSTM)**

##### **Overview**:
- **Long Short-Term Memory (LSTM)** networks are a type of RNN designed to overcome the limitations of standard RNNs, particularly the problem of vanishing gradients. LST

Ms can capture long-term dependencies in time series data, making them highly effective for time series forecasting.

##### **How It Works**:
- LSTM networks maintain a memory cell that can learn which information to keep or discard over long periods of time. This allows LSTMs to model long-range dependencies in sequential data.

##### **Advantages**:
- Effective for long-term dependencies.
- Can model non-linear relationships and capture complex temporal patterns.

##### **Disadvantages**:
- Computationally expensive and requires large datasets.
- Requires careful tuning of hyperparameters.

##### **Example Using LSTM**:
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

#### **3.3 Gated Recurrent Units (GRU)**
##### **Overview**:
- **Gated Recurrent Units (GRUs)** are similar to LSTMs but with a simplified structure. GRUs are often faster to train than LSTMs and perform comparably in many time series tasks.

##### **Advantages**:
- Less computationally expensive than LSTMs.
- Suitable for both short-term and long-term dependencies.

##### **Example Using GRU**:
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

### **4. Hybrid Models**

In practice, many machine learning models for time series forecasting combine traditional statistical models with machine learning models. For instance:
- **ARIMA + Neural Network**: Using ARIMA to model linear components and a neural network to model non-linear residuals.
- **XGBoost + LSTM**: Combining gradient boosting models like XGBoost with LSTM networks to capture both short-term and long-term dependencies.

### Comparison

# Machine Learning Models

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

### Model Evaluation for Time Series Forecasting

When evaluating the accuracy and performance of time series forecasting models like **Simple Exponential Smoothing (SES)**, **Holt-Winters**, **ARIMA**, and others, there are several widely used metrics that help assess how well the model predictions match the actual data. Here are the key evaluation metrics commonly employed:

### **1. Mean Absolute Error (MAE)**
- **Definition**: Measures the average of the absolute differences between predicted and actual values.
- **Formula**: 
  \[
  MAE = \frac{1}{n} \sum_{t=1}^{n} |y_t - \hat{y}_t|
  \]
- **Interpretation**: MAE gives a clear, easy-to-interpret sense of the error magnitude but doesn’t penalize large errors as much as other metrics like MSE.

### **2. Mean Squared Error (MSE)**
- **Definition**: The average of the squared differences between predicted and actual values.
- **Formula**: 
  \[
  MSE = \frac{1}{n} \sum_{t=1}^{n} (y_t - \hat{y}_t)^2
  \]
- **Interpretation**: MSE penalizes larger errors more than MAE, making it useful when large errors are particularly undesirable. However, it is sensitive to outliers.

### **3. Root Mean Squared Error (RMSE)**
- **Definition**: The square root of the mean squared error, often used to bring the error metric back to the original scale of the data.
- **Formula**: 
  \[
  RMSE = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (y_t - \hat{y}_t)^2}
  \]
- **Interpretation**: RMSE is more sensitive to outliers than MAE and is commonly used because it provides an error measure in the same units as the original data.

### **4. Mean Absolute Percentage Error (MAPE)**
- **Definition**: Measures the percentage error by calculating the ratio of the absolute forecast error to the actual value.
- **Formula**: 
  \[
  MAPE = \frac{1}{n} \sum_{t=1}^{n} \left| \frac{y_t - \hat{y}_t}{y_t} \right| \times 100
  \]
- **Interpretation**: MAPE is useful because it provides a percentage-based error, making it easier to interpret across different datasets. However, it can be problematic when actual values are close to zero.

### **5. Symmetric Mean Absolute Percentage Error (sMAPE)**
- **Definition**: A variation of MAPE that accounts for the symmetry in the error measurement, avoiding the issue of dividing by small actual values.
- **Formula**: 
  \[
  sMAPE = \frac{1}{n} \sum_{t=1}^{n} \frac{|y_t - \hat{y}_t|}{(|y_t| + |\hat{y}_t|)/2} \times 100
  \]
- **Interpretation**: This metric addresses the shortcomings of MAPE by taking both actual and predicted values into account, and it is widely used in time series forecasting.

### **6. Akaike Information Criterion (AIC)**
- **Definition**: Used for model selection, the AIC balances the goodness-of-fit of the model with its complexity. Lower AIC values indicate better models, but it penalizes models with more parameters.
- **Formula**: 
  \[
  AIC = 2k - 2\ln(L)
  \]
  where \(k\) is the number of parameters and \(L\) is the likelihood of the model.
- **Interpretation**: AIC is useful for comparing different models (such as ARIMA vs. Holt-Winters), especially in determining the trade-off between model fit and simplicity.

### **7. Bayesian Information Criterion (BIC)**
- **Definition**: Similar to AIC but includes a stronger penalty for models with more parameters, making it more suitable when the number of data points is small.
- **Formula**: 
  \[
  BIC = k \ln(n) - 2\ln(L)
  \]
  where \(n\) is the number of observations.
- **Interpretation**: BIC is another model selection criterion that penalizes model complexity, often yielding more conservative models than AIC.

### **8. Ljung-Box Q-test**
- **Definition**: This statistical test checks whether the residuals from a time series forecasting model exhibit any remaining autocorrelation. If the residuals are white noise, the model is considered adequate.
- **Interpretation**: If the test indicates significant autocorrelation in the residuals, the model may not fully capture the time series' structure.
