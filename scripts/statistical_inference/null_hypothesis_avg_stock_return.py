import yfinance as yf
import numpy as np
import scipy.stats as stats

# Fetch historical stock data using yfinance
def fetch_stock_data(ticker: str, start: str, end: str) -> np.ndarray:
    """
    Fetch historical stock data from Yahoo Finance using the yfinance library.
    
    Parameters:
        ticker (str): Stock ticker symbol (e.g., "MSFT" for Microsoft).
        start (str): Start date in the format 'YYYY-MM-DD'.
        end (str): End date in the format 'YYYY-MM-DD'.
        
    Returns:
        np.ndarray: Array of daily stock returns.
    """
    stock_data = yf.download(ticker, start=start, end=end)
    stock_data['Return'] = stock_data['Adj Close'].pct_change()  # Calculate daily returns
    return stock_data['Return'].dropna().values  # Return daily returns and drop NaN values

# Hypothesis Testing Function
def hypothesis_test(data: np.ndarray, alpha: float = 0.05) -> dict:
    """
    Perform a two-tailed t-test to determine if the average daily return is 0.
    
    Parameters:
        data (np.ndarray): Array of daily stock returns.
        alpha (float): Significance level for the test (default 0.05).
        
    Returns:
        dict: Dictionary containing the test statistic, p-value, and decision.
    """
    n = len(data)  # Number of observations (daily returns)
    
    # Step 1: Calculate the sample mean and standard deviation
    sample_mean = np.mean(data)
    sample_std_dev = np.std(data, ddof=1)  # Use ddof=1 to calculate sample standard deviation
    
    # Step 2: Define the null hypothesis (H0) and alternative hypothesis (Ha)
    # H0: The average daily return is 0 (mu = 0)
    # Ha: The average daily return is not 0 (mu != 0)
    hypothesized_mean = 0  # This is the mean under the null hypothesis (mu = 0)
    
    # Step 3: Calculate the t-statistic
    # The t-statistic is the number of standard errors the sample mean is away from the hypothesized mean (0)
    t_statistic = (sample_mean - hypothesized_mean) / (sample_std_dev / np.sqrt(n))
    
    # Step 4: Calculate the two-tailed p-value
    # The p-value tells us the probability of observing a result as extreme as the one we have if the null hypothesis is true
    p_value = 2 * (1 - stats.t.cdf(np.abs(t_statistic), df=n-1))  # Two-tailed test
    
    # Step 5: Decision rule
    # If the p-value is less than alpha, we reject the null hypothesis, otherwise we fail to reject it
    reject_null = p_value < alpha
    
    # Return all key statistics and the final decision
    return {
        "Sample Mean": sample_mean,
        "Sample Standard Deviation": sample_std_dev,
        "T-Statistic": t_statistic,
        "P-Value": p_value,
        "Reject Null Hypothesis": reject_null  # True = Reject H0, False = Fail to Reject H0
    }

# Fetch stock data for Microsoft (if running locally)
# msft_returns = fetch_stock_data("MSFT", start="2020-01-01", end="2023-01-01")

# Simulating stock return data for demonstration purposes (as a substitute for real data)
# This simulates daily returns for Microsoft over 1 year (252 trading days)
np.random.seed(42)  # Seed for reproducibility
simulated_msft_returns = np.random.normal(loc=0.0005, scale=0.015, size=252)  # Mean = 0.05%, Std = 1.5%

# Perform the hypothesis test on the simulated data
alpha = 0.05  # Significance level (5%)
hypothesis_test_result = hypothesis_test(simulated_msft_returns, alpha)

# Display the result of the hypothesis test
print("Hypothesis Test Result:")
for key, value in hypothesis_test_result.items():
    print(f"{key}: {value}")

# Final Decision Interpretation:
# If 'Reject Null Hypothesis' is True, we reject H0 and conclude that the average daily return is not 0.
# If 'Reject Null Hypothesis' is False, we fail to reject H0 and conclude that we don't have enough evidence to say the average daily return is not 0.
if hypothesis_test_result['Reject Null Hypothesis']:
    print("\nConclusion: We reject the null hypothesis. The average daily return is likely not 0.")
else:
    print("\nConclusion: We fail to reject the null hypothesis. We don't have enough evidence to say the average daily return is not 0.")
