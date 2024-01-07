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

### Example: Equipment Failure Rate

An engineer is studying the failure rate of a critical component in a machine. The time until failure of the component follows an exponential distribution with a mean time to failure of 5 years.

a) What is the probability that a component fails within the first year?
b) What is the probability that a component lasts more than 10 years?

Using the PDF of an exponential distribution:

$$f(x; \lambda) = \lambda e^{-\lambda x}$$

where $\lambda = \frac{1}{\text{mean time to failure}} = \frac{1}{5}$ years.

a) Probability of failing within the first year:

$$P(X < 1) = 1 - e^{-\frac{1}{5}} \approx 0.1813$$

b) Probability of lasting more than 10 years:

$$P(X > 10) = e^{-\frac{10}{5}} = e^{-2} \approx 0.1353$$

### Applications

Exponential distributions are used in various fields such as reliability theory, queuing theory, and survival analysis. They model waiting times, lifetimes of electronic components, and the time between consecutive events in a Poisson process.
