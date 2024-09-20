## Normal/Gaussian Distribution (Continuous)

A continuous random variable X follows a normal distribution, denoted as $X \sim \mathcal{N}(\mu,\,\sigma^{2})$. The normal distribution is characterized by its bell shape and symmetry. The majority of the values are concentrated around the mean, and there are no extreme values. It can be viewed as a generalization of the binomial distribution as $n \to \infty$.

### Probability Density Function (PDF)

The PDF of a normal distribution is given by:

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

![output(15)](https://github.com/user-attachments/assets/92c0b044-9b2d-4755-b14d-8e7d9068691c)

### Cumulative Distribution Function (CDF)

The CDF of a normal distribution is given by:

$$F(x) = \frac{1}{2} \left[ 1 + \text{erf} \left( \frac{x - \mu}{\sigma \sqrt{2}} \right) \right]$$

where erf is the error function.

![output(16)](https://github.com/user-attachments/assets/7963d182-5904-4849-9c17-698b2d5982ee)

### Expected Value

The expected value (mean) of a normal distribution is given by:

$$E[X] = \mu$$

To derive the expected value, we integrate the product of the PDF and the variable x over the entire range:

$$E[X] = \int_{-\infty}^{\infty} x \cdot f(x) dx$$

$$E[x] = \int_{-\infty}^{\infty} x \cdot \frac{1}{{\sigma \sqrt {2\pi } }}e^{\frac{- (x - \mu)^2}{2\sigma^2}} dx$$

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

### Example: Standardizing Test Scores

A teacher aims to standardize her class's test scores, which follow a normal distribution. The mean score is 70, with a standard deviation of 10. Consider a student who scored 85.

I. Determining the Student's Z-score:

The z-score formula:

$$ z = \frac{(X - \mu)}{\sigma} $$

where $X$ is the score, $\mu$ is the mean, and $\sigma$ is the standard deviation. 

For the student's score:

$$ z = \frac{(85 - 70)}{10} = 1.5 $$

II. Identifying the Corresponding Percentile:

To convert a z-score to a percentile, use a standard normal distribution table or a calculator. A z-score of 1.5 typically aligns with the 93rd percentile, meaning this student's score is higher than approximately 93% of the class.

### Application

The Normal distribution, also known as the Gaussian distribution, is a fundamental distribution in statistics. It's used in a wide range of applications, including hypothesis testing, creating confidence intervals, and in fields such as social sciences, natural sciences, and engineering to represent real-valued random variables whose distributions are not known.


