# Theory: linear and nonlinear regression

## Why this matters

A fitted line always exists, and its R-squared is often high enough to look convincing. The failure this lesson prevents is
trusting a straight line in a world that bends: you then misjudge the effect at the ends of the range, and a budget
decision based on the slope (or on a forecast beyond the data) is wrong in a predictable direction. The skill is to fit
a simple model, ask what it gets wrong, and change the *shape* of the model when the evidence says so.

## Simple linear regression

Given pairs $(x_i, y_i)$, ordinary least squares (OLS) chooses $a$ and $b$ to minimise the sum of squared residuals
$e_i = y_i - a - b x_i$:

$$
b = \frac{\sum (x_i - \bar x)(y_i - \bar y)}{\sum (x_i - \bar x)^2} = r\,\frac{s_y}{s_x},\qquad a = \bar y - b\,\bar x .
$$

The slope is the **average change in $y$ per unit of $x$ across the sample**; the line passes through $(\bar x, \bar y)$.
Spreadsheet functions: `SLOPE(y, x)`, `INTERCEPT(y, x)`, `RSQ(y, x)`, `STEYX(y, x)` and `FORECAST(x0, y, x)`.

**Worked example.** $x = 1,2,3,4,5$ and $y = 3,5,4,7,9$. Then $\bar x = 3$, $\bar y = 5.6$,
$\sum (x-\bar x)(y-\bar y) = 14$, $\sum (x-\bar x)^2 = 10$, so $b = 1.4$ and $a = 5.6 - 1.4\cdot 3 = 1.4$. The residuals are
$0.2, 0.8, -1.6, 0, 0.6$ with $SSE = 3.6$; $SST = \sum (y-\bar y)^2 = 23.2$.

## R-squared and the residual standard error

$$
R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{3.6}{23.2} = 0.845,\qquad s_e = \sqrt{\frac{SSE}{n-2}} = \sqrt{\frac{3.6}{3}} = 1.10 .
$$

$R^2$ is the share of the variance of $y$ explained by the line; with one predictor it equals $r^2$. $s_e$ is the typical
miss **in the units of $y$**, which is usually the more useful number. R-squared compares models only when they have the
same $y$ (for instance, you cannot compare the $R^2$ of a model for $y$ with that of a model for $\ln y$).

## When a line is wrong

Many business relationships **saturate**: the first dollar of advertising, the first server, the first hour of training
buys a lot, and later ones buy less. A straight line forces the same return everywhere. Warning signs:

- the scatter plot visibly bends;
- residuals plotted against $x$ are not a patternless band but a U or an arch (lesson 15 develops this);
- the model fits the middle of the data but misses both ends, or predicts impossible values outside the range.

## Fixing it with a transformation

A model can be **nonlinear in $x$ and still linear in its parameters**, so OLS still applies after transforming the variable:

$$
y = c + d\,\ln x \qquad (\text{logarithmic}),\qquad
\ln y = c + d\,\ln x \qquad (\text{power law / elasticity}),\qquad
y = c + d\,x + g\,x^2 \qquad (\text{quadratic}).
$$

Create the transformed column (`=LN(x)`) and use the same `SLOPE` / `INTERCEPT`. For the log model the marginal effect is
$dy/dx = d/x$: it falls as $x$ grows, and doubling $x$ always adds $d\ln 2$ to $y$.

**Worked example.** $x = 1,2,4,8,16$ and $y = 10,16,22,28,34$ (every doubling adds 6). The straight line gives
$y = 13 + 1.45x$ with $R^2 = 0.871$, which looks fine, yet the residuals (actual minus fitted) run $-4.5, +0.1, +3.2, +3.4, -2.2$ (an arch) and
the line predicts $59.5$ at $x = 32$. Regressing on $\ln x$ recovers $y = 10 + 8.66\ln x$ with $R^2 = 1$, which predicts $40$.

## Comparing the fits honestly

1. **Residual plot and residual standard error** on the data used for fitting.
2. **Holdout error**: fit on the earlier part, compute $RMSE=\sqrt{\tfrac1m\sum (y_i-\hat y_i)^2}$ on the later part. A flexible
   model can always lower in-sample error; only the holdout (lesson 24) tells you if it generalises.
3. **Plausibility**: does the shape make sense (diminishing returns, no negative sales)?

## Assumptions and pitfalls

1. **Extrapolation.** Neither model is validated outside the observed range. A log curve is still increasing forever;
   real saturation has a ceiling, and the right answer at twice the observed spend is "we do not know".
2. **Over-fitting by flexibility.** A degree-8 polynomial gets a higher $R^2$ and worse forecasts. Prefer the simplest curve
   that matches the mechanism.
3. **R-squared is not a verdict.** A high $R^2$ can coexist with a systematically wrong shape.
4. **Transforming $y$ changes the question.** Back-transforming a fit of $\ln y$ predicts a median, not a mean, and
   changes how errors are weighted.
5. **Association is not causation.** Here spend rises over time, so anything else that grows with time (seasonality, brand
   awareness) is entangled with spend; lesson 13 deals with that.

## Related notes

- [Correlation and lagged relationships](../11-correlation-and-lagged-relationships/theory.md)
- [Multiple regression and confounding](../13-multiple-regression-and-confounding/theory.md)
- [Residual analysis and model diagnostics](../15-residual-analysis-and-model-diagnostics/theory.md)
- [Backtesting and forecast accuracy](../24-backtesting-and-forecast-accuracy/theory.md)
- Repo note: [Simple linear regression](../../notes/regression/simple_linear_regression.md)
