import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Fetch historical stock data using yfinance
def fetch_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Fetch historical stock data from Yahoo Finance using the yfinance library.
    
    Parameters:
        ticker (str): Stock ticker symbol (e.g., "AAPL" for Apple).
        start (str): Start date in the format 'YYYY-MM-DD'.
        end (str): End date in the format 'YYYY-MM-DD'.
        
    Returns:
        pd.DataFrame: DataFrame containing the stock data.
    """
    stock_data = yf.download(ticker, start=start, end=end)
    stock_data['Return'] = stock_data['Adj Close'].pct_change()  # Calculate daily returns
    return stock_data.dropna()  # Remove NaN values

# Calculate confidence interval for stock returns
def calculate_confidence_interval(data: np.ndarray, confidence_level: float) -> dict:
    """
    Calculate the confidence interval for a given confidence level.
    
    Parameters:
        data (np.ndarray): Array of stock returns.
        confidence_level (float): Confidence level (e.g., 0.95 for 95% confidence).
        
    Returns:
        dict: Dictionary containing the mean, margin of error, and confidence interval.
    """
    n = len(data)
    sample_mean = np.mean(data)
    sample_std_dev = np.std(data, ddof=1)
    alpha = 1 - confidence_level
    t_critical = stats.t.ppf(1 - alpha / 2, df=n-1)
    margin_of_error = t_critical * (sample_std_dev / np.sqrt(n))
    confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
    
    return {
        "mean": sample_mean,
        "margin_of_error": margin_of_error,
        "confidence_interval": confidence_interval,
        "t_critical": t_critical
    }

# Plot confidence intervals for different confidence levels
def plot_confidence_intervals(intervals: dict, stock_name: str) -> None:
    """
    Plot the confidence intervals for various confidence levels.
    
    Parameters:
        intervals (dict): Dictionary containing the confidence intervals for different levels.
        stock_name (str): The name of the stock.
    """
    confidence_levels = list(intervals.keys())
    lower_bounds = [intervals[level]['confidence_interval'][0] for level in confidence_levels]
    upper_bounds = [intervals[level]['confidence_interval'][1] for level in confidence_levels]
    
    # Plotting the confidence intervals
    plt.figure(figsize=(10, 6))
    plt.plot(confidence_levels, lower_bounds, marker='o', label='Lower Bound', color='red')
    plt.plot(confidence_levels, upper_bounds, marker='o', label='Upper Bound', color='green')
    plt.fill_between(confidence_levels, lower_bounds, upper_bounds, color='gray', alpha=0.2)
    plt.axhline(0, color='black', linestyle='--')
    plt.title(f"Confidence Intervals for {stock_name} Stock Returns")
    plt.xlabel('Confidence Level')
    plt.ylabel('Return')
    plt.legend()
    plt.grid(True)
    plt.show()

# Step 1: Fetch stock data for demonstration (e.g., Apple stock)
# If running locally, you can uncomment the code below to fetch stock data from Yahoo Finance
# stock_ticker = "AAPL"
# stock_data = fetch_stock_data(stock_ticker, start="2022-01-01", end="2023-01-01")
# stock_returns = stock_data['Return'].values

# Simulating stock return data as a substitute for real data here
np.random.seed(42)
simulated_stock_returns = np.random.normal(loc=0.001, scale=0.02, size=252)  # Simulating 252 trading days

# Step 2: Define different confidence levels for comparison
confidence_levels = [0.90, 0.95, 0.99]

# Step 3: Calculate confidence intervals for each level
confidence_intervals_sim = {}
for level in confidence_levels:
    confidence_intervals_sim[level] = calculate_confidence_interval(simulated_stock_returns, level)

# Step 4: Plot the confidence intervals
plot_confidence_intervals(confidence_intervals_sim, "Simulated Stock Data")
