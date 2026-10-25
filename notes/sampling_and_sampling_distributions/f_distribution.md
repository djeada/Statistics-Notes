# F Distribution

The F-distribution, also known as the Fisher-Snedecor distribution, is a continuous probability distribution of the ratio $F=(U/d_1)/(V/d_2)$ of two independent chi-square variables $U\sim\chi^2(d_1)$ and $V\sim\chi^2(d_2)$, each divided by its degrees of freedom. It arises in hypothesis testing when comparing the variances of two normally distributed populations. The F-distribution is denoted as $X \sim F(d_1, d_2)$, where $d_1$ and $d_2$ are the degrees of freedom for the numerator and denominator, respectively.

Both scaled chi-square variables have expectation one, so their ratio compares two variance estimates expressed on a common null scale. A denominator that happens to be small produces a large ratio; this explains the distribution's positive skew and its unbounded upper tail. The order of the degrees of freedom matters: if $F\sim F(d_1,d_2)$, then $1/F\sim F(d_2,d_1)$.

## Probability Density Function (PDF)

The PDF of an F-distribution is given by:

$$f(x) = \frac{\sqrt{\frac{(d_1x)^{d_1} \cdot d_2^{d_2}}{(d_1x + d_2)^{d_1 + d_2}}}}{xB(d_1/2, d_2/2)}$$

where $B(\cdot)$ is the beta function.

The density is defined for $x>0$ and is zero for $x<0$, with $d_1,d_2>0$. An equivalent form makes its dependence on $x$ easier to evaluate:

```math
f(x)=\frac{(d_1/d_2)^{d_1/2}}{B(d_1/2,d_2/2)}
x^{d_1/2-1}\left(1+\frac{d_1x}{d_2}\right)^{-(d_1+d_2)/2}.
```

It follows from the change of variables $Q=d_1F/(d_1F+d_2)$, for which $Q$ has a Beta$(d_1/2,d_2/2)$ distribution. The same transformation gives the CDF below.

![Figure for Probability Density Function (PDF)](https://github.com/user-attachments/assets/6ff16820-c60b-4693-97c4-1061f45a3405)

## Cumulative Distribution Function (CDF)

The CDF of an F-distribution can be expressed in terms of the regularized incomplete beta function, $I_x(a, b)$:

$$F(x) = I_{\frac{d_1x}{d_1x + d_2}}\left(\frac{d_1}{2}, \frac{d_2}{2}\right)$$

![Figure for Cumulative Distribution Function (CDF)](https://github.com/user-attachments/assets/88dc09c2-c964-4d41-9b4c-362914982f5a)

## Expected Value and Variance

The expected value (mean) of an F-distribution is given by:

$$E[X] = \frac{d_2}{d_2 - 2}, \text{ for } d_2 > 2$$

The variance of an F-distribution is given by:

$$\text{Var}(X) = \begin{cases}
  \frac{2d_2^2(d_1 + d_2 - 2)}{d_1(d_2 - 2)^2(d_2 - 4)}, & \text{if}\ d_2 > 4 \\
  \infty, & \text{if}\ 2 < d_2 \le 4 \\
  \text{undefined}, & \text{if}\ d_2 \le 2
\end{cases}
$$

The CDF formula applies for $x\geq0$ and is zero below zero. Although the numerator degrees of freedom affect the shape, existence of the mean and variance is controlled by the denominator tail: $E[F]$ is finite only for $d_2>2$, and $E[F^2]$ only for $d_2>4$. The mean therefore need not equal one even though both scaled chi-square components have mean one; expectation does not pass through a ratio.

## Example: Variability in Agricultural Yields

An agronomist is assessing the variability in yield between two wheat varieties. Random samples yield the following data:

- Wheat Type 1: Sample size (n1) = 15, Variance (variance1) = 20
- Wheat Type 2: Sample size (n2) = 12, Variance (variance2) = 30

To compare the variances, the agronomist employs an F-test.

Given:

- F-test formula: $F = \frac{\text{variance1}}{\text{variance2}}$

I. Compute the F-statistic:

The F-statistic is calculated as the ratio of the two sample variances.

$$ F = \frac{20}{30} = \frac{2}{3} \approx 0.67 $$

II. Determine the degrees of freedom (df) for the test:

The degrees of freedom for each sample are calculated as the sample size minus one.

- Degrees of freedom for Wheat Type 1 (df1): $n1 - 1 = 15 - 1 = 14$
- Degrees of freedom for Wheat Type 2 (df2): $n2 - 1 = 12 - 1 = 11$

III. Interpret:

Under $H_0:\sigma_1^2=\sigma_2^2$, $F\sim F(14,11)$. Here $P(F\le 2/3)\approx 0.235$, so the two-sided p-value is $2\times0.235\approx 0.47$. The 95% acceptance region is $[0.32, 3.36]$, which contains $0.67$, so there is no evidence that the variances differ.

This exact reference requires two independent samples from normal populations. Under the null, each sample variance divided by the common population variance is a scaled chi-square variable, and independence of the samples gives the required independent ratio. For the equal-tail two-sided test, compute $2\min\{P(F\leq f),P(F\geq f)\}$, capped at one. One should not use twice the upper tail automatically when the observed ratio is below one.

The result fails to reject equality; it does not establish equal variances or a small difference. The classical variance-ratio test can be sensitive to non-normality. A scientifically meaningful variance comparison should therefore inspect the data distribution and distinguish this exact model from more robust procedures such as a Levene-type comparison.

## Applications

F-distributions are primarily used in hypothesis testing, such as the F-test for testing the equality of the variances of two normally distributed populations, and in the analysis of variance (ANOVA) for comparing the means of multiple groups. They are also used in regression analysis to test the overall significance of a model and in constructing confidence intervals for the ratio of two population variances.
