# Variance Example

Consider a random variable that takes on the value 0 half of the time and 100 the other half of the time.

## Calculating the Expected Value (Mean)

The expected value $E(X)$ of a random variable $X$ is the probability-weighted average of all possible values. 

For our random variable:

$$E(X) = P(X=0) \cdot 0 + P(X=100) \cdot 100$$
$$E(X) = \left(\frac{1}{2}\right) \cdot 0 + \left(\frac{1}{2}\right) \cdot 100$$
$$E(X) = 0 + 50$$
$$E(X) = 50$$

So, the expected value is 50.

## Calculating the Variance

Variance $\text{Var}(X)$ measures the spread of a set of numbers. It is calculated as the average of the squared differences from the Mean.

$$\text{Var}(X) = E[(X - E(X))^2]$$

Applying this to our random variable:

$$\text{Var}(X) = \left(\frac{1}{2}\right)(0 - 50)^2 + \left(\frac{1}{2}\right)(100 - 50)^2$$
$$\text{Var}(X) = \left(\frac{1}{2}\right)(-50)^2 + \left(\frac{1}{2}\right)(50)^2$$
$$\text{Var}(X) = \left(\frac{1}{2}\right)(2500) + \left(\frac{1}{2}\right)(2500)$$
$$\text{Var}(X) = 1250 + 1250$$
$$\text{Var}(X) = 2500$$

Thus, the variance is 2500.

## Calculating the Standard Deviation

The standard deviation is the square root of the variance, providing a measure of the spread of the distribution in the same units as the original data.

$$\text{SD}(X) = \sqrt{\text{Var}(X)}$$

For our random variable:

$$\text{SD}(X) = \sqrt{2500}$$
$$\text{SD}(X) = 50$$

Therefore, the standard deviation is 50.
