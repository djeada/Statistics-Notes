## Exponential Distribution (Continuous)

The exponential distribution is a continuous probability distribution that models the time between events in a Poisson point process. The exponential distribution is denoted as $X \sim \text{Exp}(\lambda)$, where $\lambda$ is the rate parameter.

### Probability Density Function (PDF)

The PDF of an exponential distribution is given by:

$$f(x) =
\begin{cases}
  \lambda e^{-\lambda x}, & \text{if}\ x \ge 0 \\
  0, & \text{if}\ x < 0
\end{cases}
$$

### Cumulative Distribution Function (CDF)

The CDF of an exponential distribution is given by:

$$F(x) = 1 - e^{-\lambda x}$$

### Expected Value and Variance

The expected value (mean) of an exponential distribution is equal to the reciprocal of the rate parameter:

$$E[X] = \frac{1}{\lambda}$$

The variance of an exponential distribution is given by:

$$\text{Var}(X) = \frac{1}{\lambda^2}$$

### Moment Generating Functions and Moments

The moment generating function (MGF) of an exponential distribution is:

$$M_X(t) = E[e^{tX}] = \frac{\lambda}{\lambda - t}, \text{ for } t < \lambda$$

To find the n-th moment, we take the n-th derivative of the MGF with respect to t and then evaluate it at t=0:

$$E[X^n] = \frac{d^n M_X(t)}{dt^n}\Bigg|_{t=0}$$

* **First Moment (Mean):**

$$E[X] = \frac{1}{\lambda}$$

* **Second Moment (Variance + Mean^2):**

$$E[X^2] = \frac{2}{\lambda^2}$$

### Applications

Exponential distributions are used in various fields such as reliability theory, queuing theory, and survival analysis. They model waiting times, lifetimes of electronic components, and the time between consecutive events in a Poisson process.
