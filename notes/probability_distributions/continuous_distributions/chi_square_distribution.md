## Chi-Square Distribution (Continuous)

A chi-square distribution is a continuous probability distribution of the sum of the squares of k independent standard normal random variables. The chi-square distribution is denoted as $X \sim \chi^2(k)$, where k is the number of degrees of freedom.

### Probability Density Function (PDF)

The PDF of a chi-square distribution is given by:

$$f(x) =
\begin{cases}
  \frac{1}{2^{k/2} \Gamma \left(\frac{k}{2}\right)} x^{\frac{k}{2} - 1} e^{-\frac{x}{2}}, & \text{if}\ x \ge 0 \\
  0, & \text{if}\ x < 0
\end{cases}
$$

where $\Gamma(\cdot)$ is the gamma function.

### Cumulative Distribution Function (CDF)

The CDF of a chi-square distribution is given by:

$$F(x) = \frac{\gamma \left(\frac{k}{2}, \frac{x}{2}\right)}{\Gamma\left(\frac{k}{2}\right)}$$

where $\gamma(\cdot)$ is the lower incomplete gamma function and $\Gamma(\cdot)$ is the gamma function.

### Expected Value and Variance

The expected value (mean) of a chi-square distribution is equal to the number of degrees of freedom:

$$E[X] = k$$

The variance of a chi-square distribution is given by:

$$\text{Var}(X) = 2k$$

### Moment Generating Functions and Moments

The moment generating function (MGF) of a chi-square distribution is:

$$M_X(t) = E[e^{tX}] = (1-2t)^{-\frac{k}{2}}$$

To find the n-th moment, we take the n-th derivative of the MGF with respect to t and then evaluate it at t=0:

$$E[X^n] = \frac{d^n M_X(t)}{dt^n}\Bigg|_{t=0}$$

* **First Moment (Mean):**

$$E[X] = k$$

* **Second Moment (Variance + Mean^2):**

$$E[X^2] = k^2 + 2k$$

### Example: Goodness-of-Fit Test

A researcher wants to test whether a die is fair. She rolls the die 60 times, and the observed frequencies for each face are as follows:

- 1: 8 times
- 2: 9 times
- 3: 13 times
- 4: 7 times
- 5: 12 times
- 6: 11 times

The researcher uses a chi-square goodness-of-fit test to determine if the die is fair.

a) What is the chi-square statistic for the test?
b) What is the degrees of freedom for the test?

The expected frequency for each face if the die is fair: E = Total rolls / Number of faces = 60 / 6 = 10

Using the chi-square formula:

$$\chi^2 = \sum \frac{(O_i - E)^2}{E}$$

a) Calculate the chi-square statistic:

$$\chi^2 = \frac{(8-10)^2}{10} + \frac{(9-10)^2}{10} + \frac{(13-10)^2}{10} + \frac{(7-10)^2}{10} + \frac{(12-10)^2}{10} + \frac{(11-10)^2}{10} \approx 3.6$$

b) Degrees of freedom: Number of categories (6) - 1 = 5


### Applications

Chi-square distributions are widely used in hypothesis testing (such as the chi-square test for independence), goodness-of-fit tests, and confidence interval estimation for the population variance in normally distributed data.

