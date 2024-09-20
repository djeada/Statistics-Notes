## F-Distribution (Continuous)

The F-distribution, also known as the Fisher-Snedecor distribution, is a continuous probability distribution that arises in hypothesis testing when comparing the variances of two normally distributed populations. The F-distribution is denoted as $X \sim F(d_1, d_2)$, where $d_1$ and $d_2$ are the degrees of freedom for the numerator and denominator, respectively.

### Probability Density Function (PDF)

The PDF of an F-distribution is given by:

$$f(x) = \frac{\sqrt{\frac{(d_1x)^{d_1} \cdot d_2^{d_2}}{(d_1x + d_2)^{d_1 + d_2}}}}{xB(d_1/2, d_2/2)}$$

where $B(\cdot)$ is the beta function.

![output(9)](https://github.com/user-attachments/assets/6ff16820-c60b-4693-97c4-1061f45a3405)

### Cumulative Distribution Function (CDF)

The CDF of an F-distribution can be expressed in terms of the regularized incomplete beta function, $I_x(a, b)$:

$$F(x) = I_{\frac{d_1x}{d_1x + d_2}}\left(\frac{d_1}{2}, \frac{d_2}{2}\right)$$

![output(10)](https://github.com/user-attachments/assets/88dc09c2-c964-4d41-9b4c-362914982f5a)

### Expected Value and Variance

The expected value (mean) of an F-distribution is given by:

$$E[X] = \frac{d_2}{d_2 - 2}, \text{ for } d_2 > 2$$

The variance of an F-distribution is given by:

$$\text{Var}(X) = \begin{cases}
  \frac{2d_2^2(d_1 + d_2 - 2)}{d_1(d_2 - 2)^2(d_2 - 4)}, & \text{if}\ d_2 > 4 \\
  \text{undefined}, & \text{if}\ d_2 \le 4
\end{cases}
$$

### Example: Variability in Agricultural Yields

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

### Applications

F-distributions are primarily used in hypothesis testing, such as the F-test for testing the equality of the variances of two normally distributed populations, and in the analysis of variance (ANOVA) for comparing the means of multiple groups. They are also used in regression analysis to test the overall significance of a model and in constructing confidence intervals for the ratio of two population variances.
