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


### Example: Comparing Sample Means

Suppose a researcher is interested in determining whether there is a significant difference between the mean systolic blood pressure of two different diets. The researcher collects the following data from a random sample:

- Diet A: n1 = 20, mean1 = 120, standard deviation1 = 8
- Diet B: n2 = 25, mean2 = 130, standard deviation2 = 10

The researcher decides to use a two-sample t-test to determine if there is a significant difference in means.

a) What is the t-statistic for the test?
b) What is the degrees of freedom for the test?

Using the formula for the two-sample t-test:

$$t = \frac{(\text{mean1} - \text{mean2})}{\sqrt{(\text{s1}^2/\text{n1}) + (\text{s2}^2/\text{n2})}}$$

a) Calculate the t-statistic:

$$t = \frac{(120 - 130)}{\sqrt{(8^2/20) + (10^2/25)}} \approx -3.78$$

b) Estimate the degrees of freedom using the Welch-Satterthwaite equation:

$$df \approx \frac{(\text{s1}^2/\text{n1} + \text{s2}^2/\text{n2})^2}{(\text{s1}^4/(\text{n1}^2(\text{n1}-1)) + \text{s2}^4/(\text{n2}^2(\text{n2}-1)))} \approx 40.4$$


### Applications

Student's t-distributions are widely used in hypothesis testing (such as the one-sample t-test, two-sample t-test, and paired t-test), confidence interval estimation for the population mean, and in regression analysis. They are particularly useful when the sample size is small and the population standard deviation is unknown.
