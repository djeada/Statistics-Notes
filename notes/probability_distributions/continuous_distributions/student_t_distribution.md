## Student's t-Distribution (Continuous)

The Student's t-distribution, or simply t-distribution, is a continuous probability distribution that arises when estimating the mean of a normally distributed population in situations where the sample size is small and the population standard deviation is unknown. The t-distribution is denoted as $X \sim t(\nu)$, where $\nu$ is the number of degrees of freedom.

### Probability Density Function (PDF)

The PDF of a t-distribution is given by:

$$f(x) = \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\nu \pi} \, \Gamma\left(\frac{\nu}{2}\right)} \left(1 + \frac{x^2}{\nu}\right)^{-\frac{\nu + 1}{2}}$$

where $\Gamma(\cdot)$ is the gamma function.

### Cumulative Distribution Function (CDF)

The CDF of a t-distribution can be expressed in terms of the regularized incomplete beta function, $I_x(a, b)$:

$$F(x) = 1 - \frac{1}{2} I_{\frac{x^2}{x^2 + \nu}}\left(\frac{1}{2}, \frac{\nu}{2}\right)$$

### Expected Value and Variance

The expected value (mean) of a t-distribution is equal to 0 for $\nu > 1$:

$$E[X] = 0$$

The variance of a t-distribution is given by:

$$\text{Var}(X) = \begin{cases}
  \frac{\nu}{\nu - 2}, & \text{if}\ \nu > 2 \\
  \infty, & \text{if}\ 1 < \nu \le 2 \\
  \text{undefined}, & \text{if}\ \nu \le 1
\end{cases}
$$

### Moment Generating Functions and Moments

The moment generating function (MGF) of a t-distribution does not exist due to the heavy tails of the distribution. However, we can compute the moments directly from the PDF.

* **First Moment (Mean):**

$$E[X] = 0, \text{ for } \nu > 1$$

* **Second Moment (Variance + Mean^2):**

$$E[X^2] = \nu, \text{ for } \nu > 2$$

### Applications

Student's t-distributions are widely used in hypothesis testing (such as the one-sample t-test, two-sample t-test, and paired t-test), confidence interval estimation for the population mean, and in regression analysis. They are particularly useful when the sample size is small and the population standard deviation is unknown.
