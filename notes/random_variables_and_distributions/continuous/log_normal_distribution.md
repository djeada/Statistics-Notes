## Log-Normal Distribution (Continuous)

A continuous random variable X follows a log-normal distribution if its natural logarithm is normally distributed. The log-normal distribution is useful in modeling continuous random variables that are constrained to be positive. It is denoted as $X \sim \text{LogNormal}(\mu, \sigma^2)$, where $\mu$ and $\sigma^2$ are the mean and variance of the variable's natural logarithm.

### Probability Density Function (PDF)

The PDF of a log-normal distribution is given by:

$$f(x; \mu, \sigma) = \frac{1}{x \sigma \sqrt{2 \pi}} \exp\left( -\frac{(\ln x - \mu)^2}{2 \sigma^2} \right)$$

for $x > 0$, $\mu \in \mathbb{R}$, and $\sigma > 0$.

![output(13)](https://github.com/user-attachments/assets/49eff855-655b-4c5c-8593-354f1b1cabe0)

### Cumulative Distribution Function (CDF)

The CDF of a log-normal distribution, $F(x; \mu, \sigma)$, is the normal cumulative distribution function of $\ln(x)$:

$$F(x; \mu, \sigma) = \frac{1}{2} + \frac{1}{2} \text{erf}\left( \frac{\ln(x) - \mu}{\sigma \sqrt{2}} \right)$$

![output(14)](https://github.com/user-attachments/assets/7ffd1673-cc6c-44dc-a7b3-724abe673ff5)

### Expected Value and Variance

The expected value (mean) of a log-normal distribution is:

$$E[X] = \exp\left( \mu + \frac{\sigma^2}{2} \right)$$

The variance of a log-normal distribution is:

$$\text{Var}(X) = \left[ \exp(\sigma^2) - 1 \right] \exp(2\mu + \sigma^2)$$

### Example: Stock Prices

Suppose the logarithm of the daily closing prices of a stock is normally distributed with $\mu = 0$ and $\sigma = 0.1$. 

I. What is the expected price of the stock?

Expected price of the stock:

$$E[X] = \exp\left( 0 + \frac{0.1^2}{2} \right) \approx 1.005$$

II. What is the variance of the stock price?

Variance of the stock price:

$$\text{Var}(X) = \left[ \exp(0.1^2) - 1 \right] \exp(2 \times 0 + 0.1^2) \approx 0.0101$$

### Applications

The log-normal distribution is widely used in finance for modeling stock prices, in environmental science for modeling concentrations of pollutants, and in survival analysis. It is also applied in economics for income distribution and in reliability engineering for representing lifetimes of systems.
