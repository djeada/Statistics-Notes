import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate Mock Stock Price Data
np.random.seed(42)
dates = pd.date_range(start="2020-01-01", end="2021-01-01", freq='D')

prices = 100  # Starting price
volatility = 1.5  # Stock price volatility (percentage change)
mock_stock_prices = [prices]

# Simulate stock prices with a random percentage change each day
for _ in range(1, len(dates)):
    change_percent = np.random.normal(0, volatility)  # Random daily percentage change
    prices *= (1 + change_percent / 100)  # Apply the percentage change
    mock_stock_prices.append(prices)

# Create a pandas Series for the stock data
stock_data = pd.Series(mock_stock_prices, index=dates)

# Step 2: Calculate 20-day SMA and EMA
sma_window = 20  # 20-day window for moving averages

# Simple Moving Average (SMA) with a 20-day window
stock_data_sma = stock_data.rolling(window=sma_window).mean()

# Exponential Moving Average (EMA) with a 20-day span
stock_data_ema = stock_data.ewm(span=sma_window, adjust=False).mean()

# Step 3: Plot the Results
plt.figure(figsize=(12, 6))
plt.plot(stock_data, label='Stock Price', color='blue')
plt.plot(stock_data_sma, label=f'{sma_window}-Day SMA', color='orange')
plt.plot(stock_data_ema, label=f'{sma_window}-Day EMA', color='green')
plt.title('Stock Price Analysis with SMA and EMA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
