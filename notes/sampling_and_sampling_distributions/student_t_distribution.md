# Student's t-Distribution (Continuous)

Student's t-distribution is a continuous probability distribution that arises when a normally distributed quantity is standardized using an estimated standard deviation rather than a known population standard deviation. Formally, if $Z\sim N(0,1)$ and $V\sim\chi^2(\nu)$ are independent, then $T=Z/\sqrt{V/\nu}\sim t(\nu)$. It has heavier tails than the normal distribution and approaches the normal distribution as its degrees of freedom increase. The t-distribution is denoted as $X \sim t(\nu)$, where $\nu$ is the number of degrees of freedom.

## Why estimating a standard deviation creates heavier tails

For independent $N(\mu,\sigma^2)$ observations, the mean and sample variance are independent, and

```math
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1),
\qquad V=\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1).
```

Substituting these into the defining ratio yields $(\bar X-\mu)/(S/\sqrt n)\sim t(n-1)$. Occasionally $S$ underestimates $\sigma$, making the ratio unusually large in magnitude. This extra denominator uncertainty explains the heavier tails. With more degrees of freedom, $V/\nu$ concentrates near one and the t distribution approaches the standard normal.

The exact result requires the normal-sample construction and independence in the ratio. Dividing an arbitrary statistic by any estimated standard error does not automatically produce an exact t distribution.

## Probability Density Function (PDF)

The PDF of a t-distribution is given by:

$$f(x) = \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\nu \pi} \, \Gamma\left(\frac{\nu}{2}\right)} \left(1 + \frac{x^2}{\nu}\right)^{-\frac{\nu + 1}{2}}$$

where $\Gamma(\cdot)$ is the gamma function.

![Figure for Probability Density Function (PDF)](https://github.com/user-attachments/assets/80382e02-30b2-4477-af09-e87d360a02e6)

## Cumulative Distribution Function (CDF)

The CDF of a t-distribution can be expressed in terms of the regularized incomplete beta function $I_x(a,b)$. For $t\ne0$,

$$
F(t)=1-\tfrac12 I_{\frac{\nu}{t^2+\nu}}\!\left(\tfrac{\nu}{2},\tfrac12\right)\quad (t>0),
$$

and $F(-t)=1-F(t)$ by symmetry.

At $t=0$, symmetry gives $F(0)=1/2$. Negative quantiles are obtained by reflecting positive quantiles. The density's symmetry does not guarantee existence of a mean: when $\nu\leq1$, the positive and negative tail integrals fail to be absolutely integrable, so cancellation cannot define an ordinary expectation.

![Figure for Cumulative Distribution Function (CDF)](https://github.com/user-attachments/assets/f4cca998-c7fe-43e2-874b-854264a76725)

## Expected Value and Variance

The expected value (mean) of a t-distribution is equal to 0 for $\nu > 1$:

$$E[X] = 0$$

The variance of a t-distribution is given by:

$$\text{Var}(X) = \begin{cases}
  \frac{\nu}{\nu - 2}, & \text{if}\ \nu > 2 \\
  \infty, & \text{if}\ 1 < \nu \le 2 \\
  \text{undefined}, & \text{if}\ \nu \le 1
\end{cases}
$$

## Moments

The moment generating function of a t-distribution does not exist in a neighborhood of zero because of its heavy tails. Moments that do exist can be computed from the density.

* **First Moment (Mean):**

$$E[X] = 0, \text{ for } \nu > 1$$

* **Second Raw Moment:**

$$E[X^2] = \frac{\nu}{\nu - 2}, \text{ for } \nu > 2$$

Because the mean is zero, the second raw moment equals the variance whenever $\nu > 2$.

## Example: Analyzing the Effect of Diet on Blood Pressure

A researcher investigates whether two diets lead to different average systolic blood pressure. The following data is collected from a random sample:

- Diet A: Sample size (n1) = 20, Mean (mean1) = 120, Standard Deviation (s1) = 8
- Diet B: Sample size (n2) = 25, Mean (mean2) = 130, Standard Deviation (s2) = 10

To compare the means, a two-sample t-test is employed.

I. Calculation of the T-statistic:

The t-statistic is calculated using the formula for Welch's two-sample t-test:

$$ t = \frac{(\text{mean1} - \text{mean2})}{\sqrt{(\text{s1}^2/\text{n1}) + (\text{s2}^2/\text{n2})}} $$

For the given data:

$$ t = \frac{(120 - 130)}{\sqrt{(8^2/20) + (10^2/25)}} \approx -3.73 $$

This value measures the mean difference in units of its estimated standard error. Using the Welch approximation with about 43 degrees of freedom gives a two-sided p-value about $0.0006$. Under the independent-sample model, these data provide strong evidence of a difference in the population group means.

II. Estimation of Degrees of Freedom:

The degrees of freedom can be estimated using the Welch-Satterthwaite equation:

$$ df \approx \frac{((\text{s1}^2/\text{n1}) + (\text{s2}^2/\text{n2}))^2}{(\text{s1}^4/(\text{n1}^2(\text{n1}-1)) + \text{s2}^4/(\text{n2}^2(\text{n2}-1)))} \approx 43.0 $$

These degrees of freedom are used to determine the reference t-distribution for the hypothesis test.

Here the estimated standard error is $\sqrt{64/20+100/25}=\sqrt{7.2}\approx2.683$, so the estimated difference is $-10$ mmHg, about $3.727$ standard errors below zero. Welch's degrees of freedom are approximately $43.00$, giving a two-sided p-value near $0.00056$. A corresponding 95% confidence interval for the mean difference is approximately $-10\pm2.017(2.683)$, or $(-15.41,-4.59)$ mmHg.

Welch's reference distribution is an approximation even for two independent normal samples with unequal variances; the exact one-sample construction above should not be transferred to it without qualification. Interpretation also requires independent sampling within and between groups. The difference is evidence of an association with diet group; attributing it to a causal diet effect additionally requires an appropriate assignment design or assumptions.

## Applications

Student's t-distributions are widely used in hypothesis testing (such as the one-sample t-test, two-sample t-test, and paired t-test), confidence interval estimation for population means, and regression analysis when standard errors are estimated from data.
