## Negative Binomial Distribution (Discrete)

A discrete random variable X follows a negative binomial distribution if it represents the number of trials required to achieve a specified number of successes in a sequence of independent Bernoulli trials. The negative binomial distribution is often denoted as $X \sim \text{NegBinomial}(r, p)$, where r is the number of successes required and p is the probability of success on each trial.

### Probability Mass Function (PMF)

The PMF of a negative binomial distribution is given by:

$$P(X=k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}$$

where $k \in \{r, r+1, r+2, \dots\}$ and $\binom{k-1}{r-1}$ is the binomial coefficient.

### Cumulative Distribution Function (CDF)

The CDF of a negative binomial distribution is not as straightforward to express in a closed form but is the sum of its PMF values:

$$F(k) = P(X \le k) = \sum_{i=r}^{k} \binom{i-1}{r-1} p^r (1-p)^{i-r}$$

### Expected Value and Variance

The expected value (mean) of a negative binomial distribution is:

$$E[X] = \frac{r}{p}$$

The variance of a negative binomial distribution is:

$$\text{Var}(X) = \frac{r(1-p)}{p^2}$$

### Moment Generating Function (MGF)

The moment generating function (MGF) of a negative binomial distribution is:

$$M_X(t) = \left(\frac{pe^t}{1 - (1 - p)e^t}\right)^r$$

### Example: Quality Control Testing

In quality control testing, an inspector examines products until finding a certain number of defective items. Suppose the probability of a product being defective is 0.1, and the inspector continues testing until 5 defective products are found.

Given:

- Probability of defective product `p = 0.1`
- Number of defects required `r = 5`

I. What is the probability that exactly 20 products need to be tested?

For exactly 20 products tested:

$$P(X = 20) = \binom{19}{4} (0.1)^5 (0.9)^{15} ≈ 0.031$$

II. What is the expected number of products to be tested?

Expected number of products tested:

$$E[X] = \frac{5}{0.1} = 50$$

III. What is the variance in the number of products tested?

Variance in the number of products tested:

$$\text{Var}(X) = \frac{5 \times (1-0.1)}{0.1^2} = 450$$

### Applications

Negative binomial distributions are commonly used in scenarios where the number of trials until a specified number of failures occurs is of interest, such as in reliability testing, epidemiology, and ecological studies.
