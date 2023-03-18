## Poisson Distribution (Discrete)

A discrete random variable X follows a Poisson distribution if the events occur independently and at a constant average rate. The Poisson distribution is denoted as $X \sim \text{Poisson}(\lambda)$, where $\lambda$ is the average rate (or mean) of events occurring in a given interval.

### Probability Mass Function (PMF)

The PMF of a Poisson distribution is given by:

$$P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}$$

where $k \in \{0, 1, 2, \dots\}$.

### Cumulative Distribution Function (CDF)

The CDF of a Poisson distribution is given by:

$$F(k) = P(X \le k) = \sum_{i=0}^{k} \frac{e^{-\lambda} \lambda^i}{i!}$$

### Expected Value and Variance

The expected value (mean) and variance of a Poisson distribution are both equal to the average rate parameter $\lambda$:

$$E[X] = \text{Var}(X) = \lambda$$

### Moment Generating Functions and Moments

The moment generating function (MGF) of a Poisson distribution is:

$$M_X(t) = E[e^{tX}] = e^{\lambda(e^t - 1)}$$

To find the n-th moment, we take the n-th derivative of the MGF with respect to t and then evaluate it at t=0:

$$E[X^n] = \frac{d^n M_X(t)}{dt^n}\Bigg|_{t=0}$$

* **First Moment (Mean):**

$$E[X] = \lambda$$

* **Second Moment (Variance + Mean^2):**

$$E[X^2] = \lambda^2 + \lambda$$

### Poisson Approximation to the Binomial Distribution

If the number of trials in a binomial distribution is large (n) and the probability of success (p) is small, then the binomial distribution can be approximated by a Poisson distribution with parameter $\lambda = np$:

$$\text{Binomial}(n, p) \approx \text{Poisson}(np)$$
