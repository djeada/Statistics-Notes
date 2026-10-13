# Simple Linear Regression: Exercises

Review the note [Simple Linear Regression](../../notes/regression/simple_linear_regression.md) first. Problems 1-5 and 8 use the same data set:

| $i$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $x_i$ | 1 | 2 | 3 | 4 | 5 |
| $y_i$ | 2 | 4 | 5 | 4 | 5 |

## Problems

1. Compute $\bar{x}$, $\bar{y}$, $S_{xx}$, $S_{xy}$, and the least-squares estimates $\hat\beta_0$ and $\hat\beta_1$.
2. Compute the fitted values and residuals. Verify that the residuals sum to zero and are orthogonal to $x$ ($\sum x_i e_i = 0$). Then compute SST, SSR, SSE, and $R^2$.
3. Compute the residual standard error $s$, $\mathrm{SE}(\hat\beta_1)$, the $t$ statistic for $H_0:\beta_1=0$, and a 95 % confidence interval for $\beta_1$. Use $t_{0.975,3}=3.182$. Is the slope significant at the 5 % level?
4. Predict $y$ at $x_0=6$ and give a 95 % prediction interval. Then give a 95 % confidence interval for the *mean* response at $x_0=3$. Comment on the extrapolation at $x_0=6$.
5. Show that $R^2 = r_{xy}^2$ and $\hat\beta_1 = r_{xy}\, s_y/s_x$ for this data. Also compute the slope of the regression of $x$ on $y$ and verify that the product of the two slopes equals $R^2$.
6. (Conceptual) Suppose $x$ is rescaled to $x^* = 2x$. What happens to $\hat\beta_0$, $\hat\beta_1$, $\mathrm{SE}(\hat\beta_1)$, $t$, and $R^2$? Verify with the data above.
7. (Conceptual) State the LINE assumptions. Which of them are required for the least-squares estimates to be unbiased, and which are required only for the exact $t$-based inference of problem 3? What happens to $\hat\beta_1$ if $x$ is measured with error?
8. Add a sixth observation $(x_6,y_6)=(10,5)$ to the data. Recompute $\hat\beta_1$, $\hat\beta_0$, and $R^2$. Compute the leverage $h_{66}=1/n + (x_6-\bar{x})^2/S_{xx}$ and explain what has happened.
9. (Conceptual) Explain why a very high $R^2$ does not prove that the model is correct, and describe two residual plots you would examine.

## Solutions

**Problem 1.** $\bar{x}=15/5=3$, $\bar{y}=20/5=4$.

| $x_i$ | $y_i$ | $x_i-\bar x$ | $y_i-\bar y$ | product | $(x_i-\bar x)^2$ |
|---|---|---|---|---|---|
| 1 | 2 | -2 | -2 | 4 | 4 |
| 2 | 4 | -1 | 0 | 0 | 1 |
| 3 | 5 | 0 | 1 | 0 | 0 |
| 4 | 4 | 1 | 0 | 0 | 1 |
| 5 | 5 | 2 | 1 | 2 | 4 |

$S_{xy}=4+0+0+0+2=6$ and $S_{xx}=4+1+0+1+4=10$. Hence $\hat\beta_1=6/10=0.6$ and $\hat\beta_0=4-0.6(3)=2.2$. The fitted line is $\hat y=2.2+0.6x$.

**Problem 2.** Fitted values: $2.8,\ 3.4,\ 4.0,\ 4.6,\ 5.2$. Residuals $e_i=y_i-\hat y_i$: $-0.8,\ 0.6,\ 1.0,\ -0.6,\ -0.2$.

- $\sum e_i=-0.8+0.6+1.0-0.6-0.2=0$.
- $\sum x_ie_i=-0.8+1.2+3.0-2.4-1.0=0$.
- $\mathrm{SSE}=0.64+0.36+1.00+0.36+0.04=2.4$.
- $\mathrm{SST}=(-2)^2+0+1+0+1=6$.
- $\mathrm{SSR}=\mathrm{SST}-\mathrm{SSE}=3.6$ (check: $\hat\beta_1^2S_{xx}=0.36\cdot10=3.6$).
- $R^2=3.6/6=0.60$.

**Problem 3.** $s^2=\mathrm{SSE}/(n-2)=2.4/3=0.8$, so $s=\sqrt{0.8}\approx0.894$.
$\mathrm{SE}(\hat\beta_1)=s/\sqrt{S_{xx}}=0.894/\sqrt{10}\approx0.283$.
$t=0.6/0.283\approx2.12$ on $3$ degrees of freedom.
CI: $0.6\pm3.182(0.283)=0.6\pm0.900=(-0.30,\ 1.50)$.
Since $|t|=2.12<3.182$ (equivalently, the CI contains 0), the slope is not significant at the 5 % level (exact two-sided $p\approx0.124$).

**Problem 4.** $\hat y_0=2.2+0.6(6)=5.8$.
Prediction interval: $\mathrm{SE}_{\text{pred}}=s\sqrt{1+\tfrac1n+\tfrac{(x_0-\bar x)^2}{S_{xx}}}=0.894\sqrt{1+0.2+0.9}=0.894\sqrt{2.1}\approx1.296$.
Interval: $5.8\pm3.182(1.296)=5.8\pm4.12=(1.68,\ 9.92)$.

Mean response at $x_0=3$: $\hat y=4.0$, $\mathrm{SE}=s\sqrt{\tfrac1n+0}=0.894\sqrt{0.2}=0.4$, so $4.0\pm3.182(0.4)=4.0\pm1.27=(2.73,\ 5.27)$.

$x_0=6$ lies outside the observed range $[1,5]$, so the linearity assumption is untested there; the interval is also much wider than at the centre $\bar x$ because of the $(x_0-\bar x)^2/S_{xx}$ term.

**Problem 5.** $S_{yy}=\mathrm{SST}=6$. $r_{xy}=S_{xy}/\sqrt{S_{xx}S_{yy}}=6/\sqrt{60}\approx0.7746$, so $r_{xy}^2=36/60=0.60=R^2$.
$s_x=\sqrt{10/4}\approx1.581$, $s_y=\sqrt{6/4}\approx1.225$, and $r_{xy}s_y/s_x=0.7746(1.225/1.581)=0.7746\cdot0.7746=0.6=\hat\beta_1$.
Regression of $x$ on $y$: slope $=S_{xy}/S_{yy}=6/6=1.0$. Product of slopes $=0.6\times1.0=0.6=R^2$.

**Problem 6.** With $x^*=2x$: $\bar x^*=6$, $S_{x^*x^*}=40$, $S_{x^*y}=12$, so $\hat\beta_1^*=12/40=0.3=\hat\beta_1/2$. The intercept is unchanged ($4-0.3\cdot6=2.2$). The fitted values and residuals are unchanged, hence $s$, SSE and $R^2=0.60$ are unchanged. $\mathrm{SE}(\hat\beta_1^*)=0.894/\sqrt{40}\approx0.141$, half the old SE, so $t=0.3/0.141\approx2.12$ is unchanged. Rescaling a predictor rescales the slope and its SE by the same factor, so the test is invariant.

**Problem 7.** LINE: **L**inearity of the mean, **I**ndependent errors, **N**ormal errors, **E**qual variance. Unbiasedness of $\hat\beta_0,\hat\beta_1$ needs only linearity and $E[\varepsilon_i\mid x_i]=0$. Correct standard errors (and the Gauss-Markov optimality) additionally need independence and equal variance. Normality is required only for exact small-sample $t$ and $F$ distributions (for large $n$, a CLT argument makes it largely unnecessary). Measurement error in $x$ attenuates the slope: $\hat\beta_1$ is biased toward zero by the reliability ratio $\sigma_x^2/(\sigma_x^2+\sigma_u^2)$.

**Problem 8.** New data: $n=6$, $\bar x=25/6\approx4.167$, $\bar y=25/6\approx4.167$. $\sum x^2=155$, $\sum xy=66+50=116$.
$S_{xx}=155-6(4.167)^2=50.83$, $S_{xy}=116-6(4.167)^2=11.83$.
$\hat\beta_1=11.83/50.83\approx0.233$, $\hat\beta_0=4.167-0.233(4.167)\approx3.197$.
$R^2\approx0.403$ (down from 0.60).
Leverage: $h_{66}=1/6+(10-4.167)^2/50.83=0.167+0.669\approx0.836$.
A single point far from the other $x$ values has leverage $\approx0.84$ and dragged the slope from $0.6$ to $0.23$: it is a high-leverage, influential observation. Always check leverage and Cook's distance before trusting a fit.

**Problem 9.** $R^2$ only measures the proportion of sample variance explained by the line. A curved relationship, a few influential points, or a derived or time-trending variable can all give high $R^2$ with a misspecified model (and a low $R^2$ is compatible with a correct model with large noise). Check (a) residuals vs fitted values for curvature or funnel shapes (non-linearity, heteroscedasticity) and (b) a normal Q-Q plot of the residuals (normality), plus residuals vs. order for dependence.
