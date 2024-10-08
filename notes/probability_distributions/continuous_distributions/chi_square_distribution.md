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

![output(5)](https://github.com/user-attachments/assets/0a071a01-8604-458d-884f-97a9e0505b04)

### Cumulative Distribution Function (CDF)

The CDF of a chi-square distribution is given by:

$$F(x) = \frac{\gamma \left(\frac{k}{2}, \frac{x}{2}\right)}{\Gamma\left(\frac{k}{2}\right)}$$

where $\gamma(\cdot)$ is the lower incomplete gamma function and $\Gamma(\cdot)$ is the gamma function.

![output(6)](https://github.com/user-attachments/assets/6b5404fb-62b8-4a56-ab21-5fc6dcc9db5f)

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

### Example: Goodness-of-Fit Test for a Fair Die

A researcher is testing the fairness of a six-sided die. The die is rolled 60 times, resulting in the following observed frequencies for each face:

| Face of the Die | Observed Frequency |
|-----------------|--------------------|
| 1               | 8                  |
| 2               | 9                  |
| 3               | 13                 |
| 4               | 7                  |
| 5               | 12                 |
| 6               | 11                 |

To determine if the die is fair, the researcher employs a chi-square goodness-of-fit test.

Given:

The expected frequency for each face (assuming the die is fair): `E = Total rolls / Number of faces = 60 / 6 = 10`

The chi-square formula:

$$ \chi^2 = \sum \frac{(O_i - E)^2}{E} $$

where $O_i$ is the observed frequency and $E$ is the expected frequency.

I. Calculate the chi-square statistic:

$$ \chi^2 = \frac{(8-10)^2}{10} + \frac{(9-10)^2}{10} + \frac{(13-10)^2}{10} + \frac{(7-10)^2}{10} + \frac{(12-10)^2}{10} + \frac{(11-10)^2}{10} = 3.6 $$

II. Determine the degrees of freedom:

Degrees of freedom for chi-square test: `Number of categories - 1 = 6 - 1 = 5`

### Applications

Chi-square distributions are widely used in hypothesis testing (such as the chi-square test for independence), goodness-of-fit tests, and confidence interval estimation for the population variance in normally distributed data.

