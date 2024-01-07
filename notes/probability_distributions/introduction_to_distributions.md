## Introduction to Distributions

A distribution is a function that describes the probability of a random variable. It helps to understand the underlying patterns and characteristics of a dataset. Distributions are widely used in statistics, data analysis, and machine learning for tasks such as hypothesis testing, confidence intervals, and predictive modeling.

## Random Variables

Random variables assign numerical values to outcomes of random processes in probability and statistics. Random variables can be **discrete** (taking specific values) or **continuous** (taking any value within a range).

### Examples

1. **Drawing a Card from a Deck**: 
   - **Suit of the Card (Discrete)**: Assigns a category based on the suit (e.g., hearts, spades).
   - **Rank of the Card (Discrete)**: Numerical value or face (e.g., 2, 10, King).
   - **Color of the Card (Discrete)**: Red or Black.

2. **Weather Forecast**:
   - **Temperature (Continuous)**: The forecasted temperature in degrees.
   - **Chance of Precipitation (Continuous)**: Probability of rain or snow, expressed in percentage.
   - **Wind Speed (Continuous)**: Speed of the wind in kilometers or miles per hour.

### Probability Calculations

- **Discrete Example (Card Drawing)**: If X represents the suit of a card, $P(X = Hearts)$ is the probability of drawing a heart.
- **Continuous Example (Temperature)**: If Y represents temperature, $P(Y > 20°C)$ is the chance that the temperature is above 20 degrees Celsius.
- **General Probability Notations**: Calculate probabilities like $P(X < x), P(X ≤ x), P(X > x), P(X ≥ x)$, where 'x' is a specific value.

## Probability Distributions

- **Probability Density Function (PDF) - Continuous Variables**: 
  - Definition: For continuous random variables, the PDF gives the probability density at a specific point $x$. 
  - Notation: $f_X(x)$.
  - Usage: Used to calculate the probability of the variable falling within a certain range.
  - Key Point: The area under the curve between two points gives the probability of the variable falling within that range.

- **Probability Mass Function (PMF) - Discrete Variables**: 
  - Definition: For discrete random variables, the PMF gives the probability that the variable takes a specific value $x$.
  - Notation: $p_X(x) = P(X = x)$.
  - Usage: Used to directly find the probability of specific outcomes.
  - Example: In a dice roll, the PMF gives the probability of rolling any specific number (1 through 6).

- **Cumulative Distribution Function (CDF) - Both Continuous and Discrete Variables**: 
  - Definition: The CDF gives the probability that a random variable is less than or equal to a specific value $x$.
  - Notation: $F_X(x) = P(X \leq x)$.
  - Usage: Used to calculate the probability of the variable falling within a range below a certain threshold.
  - Key Point: The CDF is non-decreasing and approaches 1 as $x$ approaches infinity.

### Example: Probability Distribution of a Discrete Random Variable

Consider a discrete random variable $X$ with the following probability distribution:

| Value of $X$ | Probability $p_X(x)$ |
|------------------|--------------------------|
| 1                | 0.05                     |
| 2                | 0.10                     |
| 3                | 0.15                     |
| 4                | 0.20                     |
| 5                | 0.15                     |
| 6                | 0.10                     |
| 7                | 0.08                     |
| 8                | 0.07                     |
| 9                | 0.05                     |
| 10               | 0.05                     |


Interpreting the Table:
- **Higher Probability Values**: The value 4 has the highest probability (0.20), suggesting that it is the most likely outcome.
- **Comparing Probabilities**: The probability of getting a 4 is higher than getting a 10, as indicated by their respective probabilities (0.20 vs. 0.05).
- **Sum of Probabilities**: The sum of all these probabilities equals 1, confirming that the table represents a complete probability distribution.

This table can be visualized using a bar graph, with the height of each bar representing the likelihood of each outcome.

![be5cfcd9-6dcb-48ab-80a4-c10313a0ace0](https://github.com/djeada/Statistics-Notes/assets/37275728/f32e53be-7840-4574-b3e2-2e62782f3ec1)

### Example: Roll a Six-Sided Die Until a 6 Appears

Roll a fair six-sided die repeatedly until the die shows a 6.

| Number of Rolls | Probability         |
|-----------------|---------------------|
| 1               | 1/6 ≈ 0.1667       |
| 2               | (5/6) * (1/6) ≈ 0.1389 |
| 3               | (5/6)^2 * (1/6) ≈ 0.1157 |
| 4               | (5/6)^3 * (1/6) ≈ 0.0964 |
| 5               | (5/6)^4 * (1/6) ≈ 0.0803 |
| 6               | (5/6)^5 * (1/6) ≈ 0.0669 |

![bcc766bb-54d8-4005-8a06-e4de2f8b571d](https://github.com/djeada/Statistics-Notes/assets/37275728/e2211233-f9ec-4ed0-b6d6-8696d465aa64)

Find the probability that the first 6 appears:
1. On the third roll.
2. On the third or fourth roll.
3. In less than five rolls.
4. In no more than three rolls.
5. After three rolls.
6. In at least three rolls.

Now let's do calculations:

1. $P(3) = (5/6)^2 * (1/6) ≈ 0.1157$
2. $P(3 or 4) = P(3) + P(4) ≈ 0.1157 + 0.0964 ≈ 0.2121$
3. $P(X < 5) = P(1) + P(2) + P(3) + P(4) ≈ 0.1667 + 0.1389 + 0.1157 + 0.0964 ≈ 0.5177$
4. $P(X ≤ 3) = P(1) + P(2) + P(3) ≈ 0.1667 + 0.1389 + 0.1157 ≈ 0.4213$
5. $P(X > 3) = 1 - P(X ≤ 3) ≈ 1 - 0.4213 ≈ 0.5787$
6. $P(X ≥ 3) = P(3) + P(4) + P(5) + P(6) + ... ≈ 0.1157 + 0.0964 + 0.0803 + 0.0669 + ...$

## Moments and Moment Generating Functions

Moments are statistical measures that describe various aspects of a distribution, such as central tendency, dispersion, and shape. The $n$th moment of a random variable $X$ about a constant $c$ is defined as the expected value of $(X - c)^n$:

$E[(X - c)^n]$

The moment-generating function (MGF) of a random variable $X$ is a function that, when differentiated $n$ times and evaluated at $t=0$, gives the $n$th moment about the origin:

$M_X(t) = E[e^{tX}]$

The mean (first moment) and variance (second moment) can be derived from the MGF:

* **Mean (first moment):** $E[X] = \mu = M_X^{(1)}(0)$
* **Variance (second moment):** $Var(X) = \sigma^2 = E[X^2] - (E[X])^2 = M_X^{(2)}(0) - (M_X^{(1)}(0))^2$

## Types of Distributions

1. **Uniform distribution:** All values have equal probability of occurring.
2. **Normal distribution (Gaussian distribution):** A continuous distribution where data is symmetrically distributed around the mean.
3. **Exponential distribution:** A continuous distribution where data decreases exponentially as the value increases.
4. **Poisson distribution:** A discrete distribution for counting the number of events in a fixed interval of time or space.

## Measures of Central Tendency

Measures of central tendency describe the center of a distribution:

* **Mean (average):** The sum of all data points divided by the number of data points: $\mu = \frac{\sum_{i=1}^{n} x_i}{n}$
* **Median:** The middle value when data is ordered from smallest to largest.
* **Mode:** The value(s) that occurs most frequently in the data.

## Measures of Dispersion

Measures of dispersion describe the spread of a distribution:

* **Range:** The difference between the maximum and minimum values.
* **Variance:** The average of the squared differences from the mean: $\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}$
* **Standard deviation:** The square root of the variance: $\sigma = \sqrt{\sigma^2}$

## Measures of Shape

Measures of shape describe the skewness and kurtosis of a distribution:

* **Skewness:** A measure of the asymmetry of the distribution.
* **Kurtosis:** A measure of the "tailedness" of the distribution.

## Sampling and Sampling Distributions

When working with statistics, we usually base our calculations on a sample and not the full population of data. Taking multiple samples and combining the resulting means forms a sampling distribution. The larger the sample size, the closer the data will be to a perfect normal distribution, and the less variance around the mean there will be.

## The Central Limit Theorem

The Central Limit Theorem states that with a large enough sample size, the distribution of values for a random variable starts to form an approximately normal curve. This applies to any distribution of sample data if the size of the sample is large enough.

## Mean and Standard Error of a Sampling Distribution

* **Mean**: The mean of a sampling distribution is the mean of all the sample means.
* **Standard Error (SE)**: The standard deviation of a sampling distribution. For a distribution of proportion means, SE is calculated as: $\text{SE} = \sqrt{\frac{p(1-p)}{n}}$. For a distribution of sample means, the standard error is: $\text{SE} = \frac{\sigma}{\sqrt{n}}$.
