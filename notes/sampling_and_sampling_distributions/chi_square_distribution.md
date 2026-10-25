# Chi-Square Distribution

A chi-square distribution is a continuous probability distribution of the sum of the squares of k independent standard normal random variables. The chi-square distribution is denoted as $X \sim \chi^2(k)$, where k is the number of degrees of freedom.

If $Z_1,\ldots,Z_k$ are independent standard normal variables, then $Q=\sum_{j=1}^kZ_j^2$ has a chi-square distribution with $k$ degrees of freedom. Squaring makes every contribution nonnegative. Since $E[Z_j^2]=1$ and $\operatorname{Var}(Z_j^2)=2$, independence gives $E[Q]=k$ and $\operatorname{Var}(Q)=2k$.

The density formula extends to every positive real degrees-of-freedom value, even though the literal finite sum construction uses integer $k$. In gamma shape/rate notation, $\chi^2(k)$ is Gamma$(k/2,1/2)$. This connection explains the gamma functions in the density and the MGF.

## Probability Density Function (PDF)

The PDF of a chi-square distribution is given by:

$$f(x) =
\begin{cases}
  \frac{1}{2^{k/2} \Gamma \left(\frac{k}{2}\right)} x^{\frac{k}{2} - 1} e^{-\frac{x}{2}}, & \text{if}\ x > 0 \\
  0, & \text{if}\ x < 0
\end{cases}
$$

where $\Gamma(\cdot)$ is the gamma function.

![Figure for Probability Density Function (PDF)](https://github.com/user-attachments/assets/0a071a01-8604-458d-884f-97a9e0505b04)

## Cumulative Distribution Function (CDF)

The CDF of a chi-square distribution is given by:

$$F(x) = \frac{\gamma \left(\frac{k}{2}, \frac{x}{2}\right)}{\Gamma\left(\frac{k}{2}\right)}$$

where $\gamma(\cdot)$ is the lower incomplete gamma function and $\Gamma(\cdot)$ is the gamma function.

The displayed CDF applies for $x\geq0$; for $x<0$, it is zero. The density formula is interpreted on $x>0$, with its boundary value at zero taken by a limit when necessary. For $k<2$ the density diverges there, but probabilities remain finite because a density's value at one point is not a point mass.

![Figure for Cumulative Distribution Function (CDF)](https://github.com/user-attachments/assets/6b5404fb-62b8-4a56-ab21-5fc6dcc9db5f)

## Expected Value and Variance

The expected value (mean) of a chi-square distribution is equal to the number of degrees of freedom:

$$E[X] = k$$

The variance of a chi-square distribution is given by:

$$\text{Var}(X) = 2k$$

In normal sampling, if $X_1,\ldots,X_n$ are i.i.d. $N(\mu,\sigma^2)$ and $S^2$ is the sample variance, then $(n-1)S^2/\sigma^2\sim\chi^2(n-1)$. This is the link to confidence intervals for a variance.

Estimating the mean imposes the constraint $\sum_i(X_i-\bar X)=0$, leaving $n-1$ independent normal directions in the residual vector. Their squared standardized lengths produce the chi-square statistic. If $q_p$ denotes the $p$ quantile of $\chi^2(n-1)$, inversion gives the variance interval

```math
\left[\frac{(n-1)S^2}{q_{1-\alpha/2}},
\frac{(n-1)S^2}{q_{\alpha/2}}\right].
```

The larger quantile is in the lower endpoint's denominator. Reversing those denominators would reverse the interval bounds. Exact coverage here depends on normal observations.

## Moment Generating Functions and Moments

The moment generating function (MGF) of a chi-square distribution, defined for $t<1/2$, is:

$$M_X(t) = E[e^{tX}] = (1-2t)^{-\frac{k}{2}}$$

To find the n-th moment, we take the n-th derivative of the MGF with respect to t and then evaluate it at t=0:

$$E[X^n] = \frac{d^n M_X(t)}{dt^n}\Bigg|_{t=0}$$

* **First Moment (Mean):**

$$E[X] = k$$

* **Second Moment ($\text{Var}(X) + (E[X])^2 = 2k + k^2$):**

$$E[X^2] = k^2 + 2k$$

## Example: Goodness-of-Fit Test for a Fair Die

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

$$ \chi^2 = \frac{(8-10)^2}{10} + \frac{(9-10)^2}{10} + \frac{(13-10)^2}{10} + \frac{(7-10)^2}{10} + \frac{(12-10)^2}{10} + \frac{(11-10)^2}{10} = \frac{4+1+9+9+4+1}{10} = 2.8 $$

II. Determine the degrees of freedom:

Degrees of freedom for chi-square test: `Number of categories - 1 = 6 - 1 = 5`

III. Decide:

The 5% critical value of $\chi^2(5)$ is $11.07$ and the p-value is $P(\chi^2(5)\ge 2.8)\approx 0.73$. Since $2.8<11.07$, there is no evidence that the die is unfair.

Each term compares a squared count discrepancy with its null expected count, so departures in either direction increase the statistic. The six count deviations sum to zero, leaving five degrees of freedom because the six null face probabilities were specified rather than estimated. Unlike the normal-sample variance statistic, this goodness-of-fit statistic has a chi-square reference distribution only asymptotically. With expected counts of ten and independent rolls, the approximation is reasonable. Failing to reject does not prove exact fairness; it means these 60 rolls do not provide strong evidence against the specified model.

## Applications

Chi-square distributions are widely used in hypothesis testing (such as the chi-square test for independence), goodness-of-fit tests, and confidence interval estimation for the population variance in normally distributed data.
