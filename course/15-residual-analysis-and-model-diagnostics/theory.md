# Theory: residual analysis and model diagnostics

## Why this matters

$R^2$ measures how close the fitted line is to the data **on average**. It does not tell you whether the model's assumptions
hold, and the assumptions are what make coefficients, standard errors, confidence intervals and prediction intervals trustworthy.
A model can have $R^2 \approx 0.9$ while its error is several times larger for some customers than for others, while a handful of rows
control the slope, and while the "typical error" you quote is wrong for exactly the cases you care about. Residual analysis is the
routine that finds this out before the model is used.

## Residuals

For a fitted model $\hat y_i$, the residual is $e_i = y_i - \hat y_i$. OLS inference assumes, for the true errors,
(1) the mean is 0 for every $x$ (the shape is right), (2) constant variance (**homoscedasticity**), (3) independence (lesson 14),
(4) approximate normality (needed for small-sample intervals, less so for the slope in large samples).
Because residuals of rows with high leverage are artificially small, we use **standardised (internally studentised) residuals**:

$$
r_i = \frac{e_i}{s\sqrt{1-h_{ii}}},\qquad s = \sqrt{\tfrac{SSE}{n-p}} .
$$

## The four plots and tests

1. **Residuals vs fitted (or vs $x$):** a patternless horizontal band is the goal. A curve means the shape is wrong (lesson 12);
   a funnel means the variance changes with the level. **Breusch-Pagan** formalises the funnel: regress $e_i^2$ on the predictors,
   and $LM = n R^2_{e^2}$ is approximately $\chi^2$ with (number of predictors) degrees of freedom under constant variance.
2. **Normal QQ plot:** sorted standardised residuals against normal quantiles $\Phi^{-1}\!\big(\tfrac{i-0.5}{n}\big)$. Points on the diagonal mean
   normality; an S-shape means heavy tails; a bend means skew. Numerically use skewness and excess kurtosis; the
   Jarque-Bera statistic $JB = \tfrac n6\big(S^2 + \tfrac{K^2}{4}\big)$ is compared with $\chi^2_2$ (5.99 at the 5 % level). The Excel
   `SKEW`/`KURT` functions are bias-adjusted, so a spreadsheet JB is approximate.
3. **Leverage:** $h_{ii} = \tfrac1n + \tfrac{(x_i-\bar x)^2}{\sum (x_j-\bar x)^2}$ measures how far a row's $x$ is from the others (with $p$ parameters,
   $\sum h_{ii} = p$; flag $h_{ii} > 2p/n$).
4. **Influence (Cook's distance):** how much the fitted values change if row $i$ is dropped,

$$
D_i = \frac{r_i^2}{p}\cdot\frac{h_{ii}}{1-h_{ii}} .
$$

A row is influential when it has **both** leverage and a large residual. Flag $D_i > 1$ (or $> 0.5$, or $> 4/n$ if you want to be strict) and
refit without it to see how much the conclusions move.

**Worked example.** Five points: $x = 1,2,3,4,10$, $y = 2.1, 3.9, 6.2, 7.8, 10.0$. The line is $\hat y = 2.82 + 0.794x$, $R^2 = 0.81$, $s = 1.57$. The point
$x = 10$ has $h = \tfrac15 + \tfrac{36}{50} = 0.92$ and residual $-0.76$, so $r = -0.764/(1.57\sqrt{0.08}) = -1.72$ and
$D = \tfrac{1.72^2}{2}\cdot\tfrac{0.92}{0.08} = 17.1$. Without it the slope is $1.94$: one point out of five changed the slope by a factor of 2.4, although its
residual is unremarkable. Leverage, not the size of the residual alone, makes a point dangerous.

## What to do when a check fails

- **Funnel / non-constant variance:** transform $y$ (log), use **weighted least squares** with weights $w_i \propto 1/\mathrm{Var}(e_i)$ (here
  $\mathrm{SD}(e)\propto x$, so $w = 1/x^2$), or keep OLS coefficients and use robust (heteroscedasticity-consistent) standard errors.
  The slope may barely move; the *intervals* are what were wrong.
- **Curvature:** change the shape (lesson 12) or add a variable (lesson 13).
- **Skew / heavy tails:** look at what the large residuals have in common (a missing variable such as traffic or weather); consider a log
  transform, quantile regression or a bootstrap for intervals (lesson 17).
- **Influential rows:** do not delete them silently. Check for data errors; if they are real, find out why they differ (a different regime may deserve its own model)
  and report results with and without them.

## Assumptions and pitfalls

1. **Residual tests are not a verdict.** With large $n$ trivial departures are "significant"; with small $n$ real ones are missed. Look at the plot and the size
   of the effect.
2. **R-squared can reward a wrong model**, particularly when a few extreme points make the variance of $x$ large.
3. **Removing outliers until the diagnostics look good** is data dredging. State the rule in advance.
4. **Residuals of an overfitted model look better** than the true errors, because they were used to fit it; check on held-out data (lesson 24).
5. **Time-ordered data:** also plot residuals against time and check autocorrelation (Durbin-Watson, lesson 14).

## Related notes

- [Linear and nonlinear regression](../12-linear-and-nonlinear-regression/theory.md)
- [Multiple regression and confounding](../13-multiple-regression-and-confounding/theory.md)
- [Spurious correlation and autocorrelation](../14-spurious-correlation-and-autocorrelation/theory.md)
- [Outlier detection](../04-outlier-detection/theory.md)
- [Bootstrapping and confidence intervals](../17-bootstrapping-and-confidence-intervals/theory.md)
- Repo note: [Simple linear regression](../../notes/regression/simple_linear_regression.md)
