## Binomial Distribution (Discrete)

A discrete random variable X follows a binomial distribution if it represents the number of successes in a fixed number of Bernoulli trials with the same probability of success. The binomial distribution is denoted as $X \sim \text{Binomial}(n, p)$, where n is the number of trials and p is the probability of success.

### Probability Mass Function (PMF)

The PMF of a binomial distribution is given by:

$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

where $k \in \{0, 1, 2, \dots, n\}$ and $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ is the binomial coefficient.

### Cumulative Distribution Function (CDF)

The CDF of a binomial distribution is given by:

$$F(k) = P(X \le k) = \sum_{i=0}^{k} \binom{n}{i} p^i (1-p)^{n-i}$$

### Expected Value and Variance

The expected value (mean) of a binomial distribution is the product of the number of trials and the probability of success:

$$E[X] = np$$

The variance of a binomial distribution is the product of the number of trials, the probability of success, and the probability of failure:

$$\text{Var}(X) = np(1-p)$$

### Moment Generating Functions and Moments

The moment generating function (MGF) of a binomial distribution is:

$$M_X(t) = E[e^{tX}] = (pe^t + 1 - p)^n$$

To find the n-th moment, we take the n-th derivative of the MGF with respect to t and then evaluate it at t=0:

$$E[X^n] = \frac{d^n M_X(t)}{dt^n}\Bigg|_{t=0}$$

* **First Moment (Mean):**

$$E[X] = np$$

* **Second Moment (Variance + Mean^2):**

$$E[X^2] = np(1-p) + n^2 p^2$$

### Example: Company Email Security

A company's IT department reports that 90% of their employees follow proper email security protocols. If 10 employees are randomly chosen for an audit.

Given:

- Probability of success (following protocol) `p = 0.9`
- Number of trials (employees chosen) `n = 10`

I. What is the probability exactly 7 of them follow the security protocols?

For exactly 7 employees:

$$P(X = 7) = \binom{10}{7} (0.9)^7 (0.1)^{10-7} = 0.0574$$

II. What is the probability at least 8 of them follow the security protocols?

For at least 8 employees:

$$P(X \geq 8) = \sum_{k=8}^{10} \binom{10}{k} (0.9)^k (0.1)^{10-k} = 0.9298$$

III. What is the probability fewer than 5 employees follow the protocols?

For fewer than 5 employees:

$$P(X < 5) = \sum_{k=0}^{4} \binom{10}{k} (0.9)^k (0.1)^{10-k} = 0.0001$$

### Applications

Binomial distributions are used in a variety of applications, such as quality control, risk analysis, and survey sampling, where the probability of success and the number of trials are known or can be estimated.
