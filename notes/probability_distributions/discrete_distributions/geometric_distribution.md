## Geometric Distribution (Discrete)

A discrete random variable X follows a geometric distribution if it represents the number of trials needed to get the first success in a sequence of Bernoulli trials. The geometric distribution is denoted as $X \sim \text{Geometric}(p)$, where p is the probability of success on each trial.

### Probability Mass Function (PMF)

The PMF of a geometric distribution is given by:

$$P(X=k) = (1-p)^{k-1} p$$

where $k \in \{1, 2, 3, \dots\}$, representing the number of trials until the first success.

### Cumulative Distribution Function (CDF)

The CDF of a geometric distribution is given by:

$$F(k) = P(X \le k) = 1 - (1-p)^k$$

### Expected Value and Variance

The expected value (mean) of a geometric distribution is:

$$E[X] = \frac{1}{p}$$

The variance of a geometric distribution is:

$$\text{Var}(X) = \frac{1-p}{p^2}$$

### Moment Generating Function (MGF)

The moment generating function (MGF) of a geometric distribution is:

$$M_X(t) = \frac{pe^t}{1 - (1 - p)e^t}$$

### Example: Flipping a Coin

Consider flipping a fair coin (probability of heads `p = 0.5`) until the first head appears.

I. What is the probability that the first head appears on the 3rd flip?

For the first head on the 3rd flip:

$$P(X = 3) = (1-0.5)^{3-1} \times 0.5 = 0.125$$

II. What is the expected number of flips to get the first head?

Expected number of flips:

$$E[X] = \frac{1}{0.5} = 2$$

III. What is the variance in the number of flips?

Variance in the number of flips:

$$\text{Var}(X) = \frac{1-0.5}{0.5^2} = 2$$

### Applications

Geometric distributions are useful in scenarios where you are waiting for the first success in a series of independent trials, such as in quality control testing, network packet delivery analysis, and reliability testing in engineering.
