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

- **Probability Distribution**: A mathematical description of the likelihood of different outcomes in an experiment or process.
- **Types**:
  - **Discrete Probability Distributions**: Used for discrete variables (e.g., counting outcomes like the number of heads in coin flips).
  - **Continuous Probability Distributions**: Used for continuous variables (e.g., measurements like height or weight).

### Calculating Probabilities

- For a discrete variable (e.g., X), the probability of a specific outcome is found directly from the PMF.
- For a continuous variable, probabilities of specific outcomes are zero; instead, probabilities of ranges are considered using the PDF.

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
2. $P(3 \text{ or } 4) = P(3) + P(4) ≈ 0.1157 + 0.0964 ≈ 0.2121$
3. $P(X < 5) = P(1) + P(2) + P(3) + P(4) ≈ 0.1667 + 0.1389 + 0.1157 + 0.0964 ≈ 0.5177$
4. $P(X \leq 3) = P(1) + P(2) + P(3) ≈ 0.1667 + 0.1389 + 0.1157 ≈ 0.4213$
5. $P(X > 3) = 1 - P(X \leq 3) ≈ 1 - 0.4213 ≈ 0.5787$
6. $P(X \geq 3) = P(3) + P(4) + P(5) + P(6) + ... ≈ 0.1157 + 0.0964 + 0.0803 + 0.0669 + ...$

### Example: Number of Pets Owned by Individuals

Consider the following probability distribution for the number of pets $P$ owned by individuals.

| $P$ | $P(P)$ |
|---------|------------|
| 0       | 0.28       |
| 1       | 0.35       |
| 2       | 0.22       |
| 3       | 0.10       |
| 4       | 0.04       |
| 5       | 0.01       |

![3331851a-bd33-48fd-9f30-6e8ef54be22e](https://github.com/djeada/Statistics-Notes/assets/37275728/9c429670-c886-40fa-8017-97ce0b756494)

Find the probability that an individual owns:
1. Less than 2 pets.
   $P(P < 2) = P(P = 0) + P(P = 1) = 0.28 + 0.35 = 0.63$
2. More than 3 pets.
   $P(P > 3) = P(P = 4) + P(P = 5) = 0.04 + 0.01 = 0.05$
3. 1 or 4 pets.
   $P(P = 1 \text{ or } P = 4) = P(P = 1) + P(P = 4) = 0.35 + 0.04 = 0.39$
4. At most 3 pets.
   $P(P \leq 3) = P(P = 0) + P(P = 1) + P(P = 2) + P(P = 3) = 0.28 + 0.35 + 0.22 + 0.10 = 0.95$
5. 2 or fewer, or more than 4 pets.
   $P(P \leq 2 \text{ or } P > 4) = P(P \leq 2) + P(P > 4) = (0.28 + 0.35 + 0.22) + 0.01 = 0.86$

## Expected Value

- **Definition of Expected Value**:
  - The expected value (often denoted as $E(X)$ or $\mu$) is a fundamental concept in probability, representing the average or mean value of a random variable over a large number of trials or observations.
  - It is calculated as a weighted average of all possible values, with weights being their respective probabilities.

- **Calculating Expected Value**:
  - For a discrete random variable: $E(X) = \sum [x_i \times P(x_i)]$, where $x_i$ are the possible values and $P(x_i)$ their probabilities.
  - For a continuous random variable, it involves integrating the product of the variable's value and its probability density function.

- **Interpretation**:
  - The expected value provides a measure of the 'center' of a probability distribution.
  - It does not necessarily correspond to the most probable value but is a long-run average if an experiment is repeated many times.

- **Usage in Decision Making**:
  - Expected value is often used in various fields such as finance, insurance, and economics for making informed decisions under uncertainty.

- **Limitations**:
  - The expected value alone might not be sufficient to understand a distribution fully, especially if the distribution is skewed or has heavy tails.

### Example: Expected Value in a Dice Roll
Consider a fair six-sided dice roll. Each side, numbered from 1 to 6, has an equal probability of appearing on a single roll. The probability for each outcome is $\frac{1}{6}$. 

Step-by-Step Calculation of Expected Value:

1. **List All Possible Outcomes and Their Probabilities**:

   | Outcome (X) | Probability $P(X)$ |
   |-------------|-------------------------|
   | 1           | 1/6                     |
   | 2           | 1/6                     |
   | 3           | 1/6                     |
   | 4           | 1/6                     |
   | 5           | 1/6                     |
   | 6           | 1/6                     |

2. **Multiply Each Outcome by Its Probability**:

   - For 1: $1 \times \frac{1}{6}$
   - For 2: $2 \times \frac{1}{6}$
   - For 3: $3 \times \frac{1}{6}$
   - For 4: $4 \times \frac{1}{6}$
   - For 5: $5 \times \frac{1}{6}$
   - For 6: $6 \times \frac{1}{6}$

3. **Sum Up the Products**:

   - $E(X) = (1 \times \frac{1}{6}) + (2 \times \frac{1}{6}) + (3 \times \frac{1}{6}) + (4 \times \frac{1}{6}) + (5 \times \frac{1}{6}) + (6 \times \frac{1}{6})$

4. **Simplify the Expression**:

   - $E(X) = \frac{1 + 2 + 3 + 4 + 5 + 6}{6} = \frac{21}{6}$

5. **Calculate the Expected Value**:

   - $E(X) = 3.5$

Interpretation:

- The expected value of $E(X) = 3.5$ suggests that over a large number of dice rolls, the average value of the outcomes will converge to 3.5.
- It's important to note that while 3.5 is not a possible outcome of a single roll, it represents the long-term average or the 'center' of the distribution of outcomes.
- This concept is a cornerstone in probability theory, providing a predictive measure of the behavior of a random variable over many trials.


## Key Concepts of  Probability Distributions

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

The cumulative distribution function (cdf) or more simply, the distribution function \( F \) of the random variable \( X \), is defined for all real numbers \( b \), \( -\infty < b < \infty \) by:

\[ F(b) = P(X \leq b) \]

A distribution function has the following properties:

1) \( F \) is a nondecreasing function

2) \( \lim_{b \to \infty} F(b) = 1 \)

3) \( \lim_{b \to -\infty} F(b) = 0 \)

4) \( F \) is right continuous. That is, for any \( b \) and any decreasing sequence \( b_n, n \geq 1 \), that converges to \( b \), 

\[ \lim_{b_n \to b^+} F(b_n) = F(b) \]


### Joint Cumulative Distributions

$$ F(a,b) = P(X \leq a, Y \leq b)$$

The distribution of X can be obtained from the joint distribution of X and Y as follows:

$$F_X = P(X < a)$$

$$= P(X < a | Y < \infty)$$

$$= P(\lim_{b \to \infty} X < a | Y < b)$$

$$= \lim_{b \to \infty} P(X < a | Y < b)$$

$$= \lim_{b \to \infty} F(a, b)$$

$$= F(a, \infty)$$



## Moments and Moment Generating Functions

Moments are statistical measures that describe various aspects of a distribution, such as central tendency, dispersion, and shape. The $n$th moment of a random variable $X$ about a constant $c$ is defined as the expected value of $(X - c)^n$:

$E[(X - c)^n]$

The moment-generating function (MGF) of a random variable $X$ is a function that, when differentiated $n$ times and evaluated at $t=0$, gives the $n$th moment about the origin:

$M_X(t) = E[e^{tX}]$

The mean (first moment) and variance (second moment) can be derived from the MGF:

* **Mean (first moment):** $E[X] = \mu = M_X^{(1)}(0)$
* **Variance (second moment):** $Var(X) = \sigma^2 = E[X^2] - (E[X])^2 = M_X^{(2)}(0) - (M_X^{(1)}(0))^2$

