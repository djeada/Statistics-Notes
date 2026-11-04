# Theory: multiple regression and confounding

## Why this matters

A simple regression of sales on advertising answers "how do sales differ between weeks with more and less advertising?",
not "what happens to sales if I raise advertising?". If advertising is higher in the weeks that would have been strong anyway
(holidays, promotions, product launches), the simple slope credits advertising with the effect of those weeks. A budget set
from it will be too generous. Multiple regression separates the contributions of several variables, **if** the relevant ones are
in the model.

## The model

$$
y_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_k x_{ik} + \varepsilon_i .
$$

OLS minimises the sum of squared residuals; in matrix form $\hat\beta = (X^\top X)^{-1} X^\top y$. Each
$\hat\beta_j$ is the estimated change in $y$ for a one-unit change in $x_j$ **holding the other predictors fixed**, that is,
comparing weeks that are alike in all the other included variables. Spreadsheet tool: `LINEST(y, X, TRUE, TRUE)`; take single
cells with `INDEX(LINEST(...), row, col)`. Row 1 holds the coefficients, **in reverse order of the columns of `X`** and the
intercept last; row 2 the standard errors; row 3 holds $R^2$ and $s_e$; row 4 the $F$ statistic and the residual degrees of
freedom $n-k-1$. `X` must be a block of adjacent columns.

## Confounding and omitted-variable bias

A **confounder** $z$ influences both the predictor $x$ and the outcome $y$. If you regress $y$ on $x$ alone, the slope absorbs
part of $z$'s effect. There is an exact identity for OLS:

$$
\hat b_{\text{simple}} = \hat\beta_x + \hat\beta_z\,\hat\delta,
$$

where $\hat\beta_x,\hat\beta_z$ come from the regression of $y$ on both $x$ and $z$, and $\hat\delta$ is the slope of the
regression of $z$ on $x$. With several omitted variables, add one term $\hat\beta_j\hat\delta_j$ for each. The bias is large
when the omitted variable matters a lot for $y$ ($\beta_z$ large) **and** is strongly tied to $x$ ($\delta$ large).

**Worked example.** Six weeks: $z$ (holiday) $=0,0,0,1,1,1$, $x$ (ad spend) $=1,2,3,3,4,5$, $y=2,3,5,10,10,12$. The simple regression
gives slope $2.7$. The regression on both gives $\hat y = 0.83 + 1.25\,x + 4.83\,z$ ($R^2=0.988$, adjusted $0.979$). The slope of $z$
on $x$ is $\hat\delta = 0.3$, and $1.25 + 4.83\cdot 0.3 = 2.7$ exactly. More than half of the simple slope was the
holiday, not the advertising.

Signs can flip, not only grow: if prices are raised in peak weeks and demand is high in peak weeks, the simple price slope can
be positive even though the price effect holding the season fixed is negative (Simpson-style reversal, see
[lesson 05](../05-sampling-bias-and-simpson-s-paradox/theory.md)).

## Judging a model: R-squared, adjusted R-squared, standard errors

$R^2$ never decreases when you add a variable, even a random one, because OLS can always fit a little noise. **Adjusted**
$R^2$ charges for each parameter:

$$
R^2_{\text{adj}} = 1 - (1-R^2)\,\frac{n-1}{n-k-1}.
$$

For the six-week example: $1-(1-0.9877)\cdot 5/3 = 0.979$. Use it (or a holdout error) to compare models with a different number of
predictors. The standard error of a coefficient gives the interval $\hat\beta_j \pm t_{n-k-1,\,0.975}\,\mathrm{SE}_j$ and the
$t$-statistic $\hat\beta_j/\mathrm{SE}_j$; $|t|<2$ means "not distinguishable from 0".

## Collinearity

When predictors are strongly correlated the coefficients are individually imprecise although the model as a whole predicts well.
The **variance inflation factor** of $x_j$ is $\mathrm{VIF}_j = 1/(1-R_j^2)$ where $R_j^2$ comes from regressing $x_j$ on the other
predictors. VIF > 5 (or 10) is a warning: standard errors are inflated by $\sqrt{\mathrm{VIF}}$. Collinearity is the price of
having controlled for a variable that moves with the one you care about; it is not a reason to omit it, since omission gives a
precise but biased answer.

## Assumptions and pitfalls

1. **Controlling is only as good as your list of controls.** Unmeasured confounders still bias the coefficient; a regression is
   not an experiment (lesson 19 covers A/B tests).
2. **Do not control for consequences of $x$.** A variable *caused by* advertising (for instance, website visits) belongs on the path
   from $x$ to $y$; adjusting for it removes part of the real effect.
3. **Linearity and additivity.** The model assumes constant effects; check residuals (lesson 15) and consider transformations
   (lesson 12) or interactions.
4. **Dummy variables** (0/1) shift the intercept: the promo coefficient is the average difference between promo and non-promo weeks
   at equal ad spend and price.
5. **Too many predictors for too few rows** leads to overfitting; keep $n$ well above $k$ and check on a holdout set.

## Related notes

- [Linear and nonlinear regression](../12-linear-and-nonlinear-regression/theory.md)
- [Correlation and lagged relationships](../11-correlation-and-lagged-relationships/theory.md)
- [Residual analysis and model diagnostics](../15-residual-analysis-and-model-diagnostics/theory.md)
- [A/B testing and effect sizes](../19-a-b-testing-and-effect-sizes/theory.md)
- Repo note: [Multiple regression](../../notes/regression/multiple_regression.md)
