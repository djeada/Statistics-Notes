# Generating mock data to fit the specified AR(2) model and plotting the results

# AR(2) model parameters
alpha = 3
beta1 = 0.6
beta2 = -0.2

# Generating mock time series data that roughly follows the specified AR(2) process
np.random.seed(42)
n = 100  # Number of data points

# Start with the specified past values
X = [10, 5]  # X_{t-1} = 10, X_{t-2} = 5

# Generate subsequent values using the AR(2) model equation with added random noise
for t in range(2, n):
    epsilon_t = np.random.normal()
    X_t = alpha + beta1 * X[t-1] - beta2 * X[t-2] + epsilon_t
    X.append(X_t)

time_series = pd.Series(X)

# Fit an AR(2) model to the generated data and make predictions
model = AutoReg(time_series, lags=2)
model_fit = model.fit()
predictions = model_fit.predict(start=2, end=n-1)

# Plot the Results
plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Generated Data', color='blue')
plt.plot(predictions, label='AR(2) Predictions', color='red', linestyle='dashed')
plt.title('Generated Time Series and AR(2) Model Predictions')
plt.xlabel('Time Point')
plt.ylabel('Value')
plt.legend()
plt.show()

