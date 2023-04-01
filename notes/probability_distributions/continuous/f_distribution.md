## F-Distribution (Continuous)

The F-distribution, also known as the Fisher-Snedecor distribution, is a continuous probability distribution that arises in hypothesis testing when comparing the variances of two normally distributed populations. The F-distribution is denoted as $X \sim F(d_1, d_2)$, where $d_1$ and $d_2$ are the degrees of freedom for the numerator and denominator, respectively.

### Probability Density Function (PDF)

The PDF of an F-distribution is given by:

$$f(x) = \frac{\sqrt{\frac{(d_1x)^{d_1} \cdot d_2^{d_2}}{(d_1x + d_2)^{d_1 + d_2}}}}{xB(d_1/2, d_2/2)}$$

where $B(\cdot)$ is the beta function.

### Cumulative Distribution Function (CDF)

The CDF of an F-distribution can be expressed in terms of the regularized incomplete beta function, $I_x(a, b)$:

$$F(x) = I_{\frac{d_1x}{d_1x + d_2}}\left(\frac{d_1}{2}, \frac{d_2}{2}\right)$$

### Expected Value and Variance

The expected value (mean) of an F-distribution is given by:

$$E[X] = \frac{d_2}{d_2 - 2}, \text{ for } d_2 > 2$$

The variance of an F-distribution is given by:

$$\text{Var}(X) = \begin{cases}
  \frac{2d_2^2(d_1 + d_2 - 2)}{d_1(d_2 - 2)^2(d_2 - 4)}, & \text{if}\ d_2 > 4 \\
  \text{undefined}, & \text{if}\ d_2 \le 4
\end{cases}
$$

### Applications

F-distributions are primarily used in hypothesis testing, such as the F-test for testing the equality of the variances of two normally distributed populations, and in the analysis of variance (ANOVA) for comparing the means of multiple groups. They are also used in regression analysis to test the overall significance of a model and in constructing confidence intervals for the ratio of two population variances.
