## Normal/Gaussian Distribution (Continuous)

A continuous random variable X follows a normal distribution, denoted as $X \sim \mathcal{N}(\mu,\,\sigma^{2})$. The normal distribution is characterized by its bell shape and symmetry. The majority of the values are concentrated around the mean, and there are no extreme values. It can be viewed as a generalization of the binomial distribution as $n \to \infty$.

### Probability Density Function (PDF)

The PDF of a normal distribution is given by:

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

### Cumulative Distribution Function (CDF)

The CDF of a normal distribution is given by:

$$F(x) = \frac{1}{2} \left[ 1 + \text{erf} \left( \frac{x - \mu}{\sigma \sqrt{2}} \right) \right]$$

where erf is the error function.

### Expected Value

The expected value (mean) of a normal distribution is given by:

$$E[X] = \mu$$

To derive the expected value, we integrate the product of the PDF and the variable x over the entire range:

$$E[X] = \int_{-\infty}^{\infty} x \cdot f(x) dx = \int_{-\infty}^{\infty} x \cdot \frac{1}{{\sigma \sqrt {2\pi } }}e^{{{ - \left( {x - \mu } \right)^2 } \mathord{\left/ {\vphantom {{ - \left( {x - \mu } \right)^2 } {2\sigma ^2 }}} \right. } {2\sigma ^2 }}} dx$$

Let $u = \frac{x - \mu}{\sqrt{2} \sigma}$, then $x = \mu + \sqrt{2} \sigma u$. The integral becomes:

$$E[X] = \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} (\mu + \sqrt{2} \sigma u) e^{-u^2} du$$

This integral can be split into two parts:

$$E[X] = \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} \mu e^{-u^2} du + \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} \sqrt{2} \sigma u e^{-u^2} du$$

The first integral evaluates to $\mu$, and the second integral evaluates to 0 (since it is an odd function integrated over a symmetric interval). Therefore, the expected value is $\mu$.

### Variance and Standard Deviation

The variance of a normal distribution is given by:

$$\text{Var}(X) = \sigma^2$$

The standard deviation is the square root of the variance:

$$\text{SD}(X) = \sigma$$

### Moment Generating Functions and Moments

The moment generating function (MGF) of a normal distribution is:

$$M_X(t) = E[e^{tX}] = e^{\mu t + \frac{1}{2} \sigma^2 t^2}$$

To find the n-th moment, we take the n-th derivative of the MGF with respect to t and then evaluate it at t=0:

$$E[X^n] = \frac{d^n M_X(t)}{dt^n}\Bigg|_{t=0}$$

* **First Moment (Mean):**

$$E[X] = \mu$$

* **Second Moment (Variance + Mean^2):**

$$E[X^2] = \sigma^2 + \mu^2$$

### Empirical Rule (68-95-99.7 Rule)

The empirical rule, also known as the 68-95-99.7 rule, describes the proportion of the probability mass that falls within certain intervals around the mean:

* 68% of the probability mass falls within $1\sigma$ of the mean ($\mu \pm \sigma$).
* 95% of the probability mass falls within $2\sigma$ of the mean ($\mu \pm 2\sigma$).
* 99.7% of the probability mass falls within $3\sigma$ of the mean ($\mu \pm 3\sigma$).

