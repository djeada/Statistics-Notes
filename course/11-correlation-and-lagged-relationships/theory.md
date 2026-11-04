# Theory: correlation and lagged relationships

## What a correlation tells you, and what it does not

Two business series that rise and fall together invite a causal story: "ad spend drives sign-ups". A correlation coefficient
is the first quantitative test of such a story, but it answers a narrow question - *how closely do two variables follow a
straight line (or a monotone curve) together?* - and it is easily fooled by outliers, by timing (the effect arrives later) and by
a third variable that moves both. This lesson separates those cases.

## Pearson correlation

For paired observations $(x_i, y_i)$, $i=1..n$:

$$
r = \frac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum_i (x_i-\bar x)^2}\,\sqrt{\sum_i (y_i-\bar y)^2}}
= \frac{\operatorname{Cov}(x,y)}{s_x s_y}, \qquad -1 \le r \le 1 .
$$

It is the covariance rescaled by both standard deviations, hence unit-free. $r^2$ is the share of the variance of $y$ explained by
the best straight line on $x$ ([lesson 12](../12-linear-and-nonlinear-regression/theory.md)). $r = 0$ does not mean "no relationship": a perfect
parabola can give $r=0$. Spreadsheet function: `CORREL`.

## Spearman rank correlation

Replace each value by its rank (ties get the average rank) and compute Pearson on the ranks. Spearman measures how well the
relationship is a **monotone** curve and ignores how far an extreme value lies from the others.

Example: $x = (1,2,3,4,5)$, $y = (2,4,5,7,40)$. Pearson is 0.782 - the single large value dominates - while Spearman is
1.000, because $y$ increases whenever $x$ does. If your data have outliers or a skewed scale, report both; a gap between them
is itself a finding.

## Lagged relationships and the cross-correlation function

When one series acts on another with a delay, the same-day correlation is the wrong alignment. The **cross-correlation at lag $k$**
pairs $x_t$ with $y_{t+k}$:

$$
r_k = \operatorname{corr}(x_t,\ y_{t+k}),\qquad t = 1, \dots, n-k .
$$

- If $r_k$ peaks at $k>0$, $x$ **leads** $y$ by $k$ periods; a peak at $k<0$ means $y$ leads $x$. Compute both directions: a
  peak on one side only is the signature of a lead.
- Each lag uses $n-k$ pairs, so large lags rest on fewer data.
- The usual "noise band" $\pm 2/\sqrt{n}$ holds only if the series have no memory. For autocorrelated series (most business
  data), raw cross-correlations are inflated and have wide humps; the standard remedy is to remove each series' own
  dynamics first (prewhitening, [lesson 14](../14-spurious-correlation-and-autocorrelation/theory.md)).

### Worked example (from `data.csv`)

Ad spend and sign-ups on the same day: $r = 0.31$. Shifting spend forward by 3 days gives $r_{3} = 0.75$ (Spearman 0.81).
The neighbouring lags are also high ($r_2 = 0.61$, $r_4 = 0.66$) because campaigns last several days, so spend on adjacent
days is nearly the same series; the lead is read from the *peak*. In the other direction (sign-ups leading spend) the highest
value for $k\ge1$ is 0.19. The regression slope at that lag is about 24.1 extra sign-ups per extra 1,000 USD of spend three
days earlier, with a caveat in the next section.

## Correlation is not causation

A lead is *necessary* for causation (effects do not precede causes) but not *sufficient*:

1. **Common driver (confounder).** Newsletter opens and sign-ups have $r = 0.34$ in the data, but both are lower on weekends. After
   subtracting each weekday's average from both columns the correlation is -0.02. Neither causes the other.
2. **Common trend or seasonality.** Two trending series are strongly correlated whatever their relation
   ([lesson 14](../14-spurious-correlation-and-autocorrelation/theory.md)). Remove trend and season, or difference
   ([lesson 09](../09-differencing-and-growth-rates/theory.md)), before correlating.
3. **Reverse or feedback causality.** Budgets are often set after a good week; check the other direction and the timing.
4. **Selection and coincidence.** Scanning many lags or many variables will find some $|r|$ above the noise band.

Causal claims need an experiment, a natural experiment or a model that controls the other drivers
([lesson 13](../13-multiple-regression-and-confounding/theory.md); [A/B tests](../19-a-b-testing-and-effect-sizes/theory.md)).

## Assumptions and pitfalls

- **Linearity (Pearson).** Always plot first; a curve, a cluster or two groups can give any $r$. Spearman needs monotonicity.
- **Outliers.** One bot day lowers Pearson in `data.csv`; see the gap to Spearman.
- **Restricted range** (only high-spend days) shrinks $r$; a mix of groups can create or reverse it
  ([lesson 05](../05-sampling-bias-and-simpson-s-paradox/theory.md)).
- **Significance is not strength.** With 150 days, $|r| > 0.16$ is "significant", yet $r = 0.2$ explains 4 % of the variance.
- **Aggregation level matters.** Daily and weekly correlations differ ([lesson 06](../06-time-aggregation-and-sampling-frequency/theory.md)).
- **Lead time can vary.** A fixed lag model misses a delay that changes by season or campaign.

## Where this leads

Regression quantifies a relationship ([lesson 12](../12-linear-and-nonlinear-regression/theory.md)); multiple regression
controls a confounder ([lesson 13](../13-multiple-regression-and-confounding/theory.md)); dynamic regression uses the lagged
predictor for forecasting. Background: [correlation](../../notes/joint_distributions_and_covariance/correlation.md),
[covariance](../../notes/joint_distributions_and_covariance/covariance.md),
[autocorrelation function](../../notes/time_series/autocorrelation_function.md),
[dynamic regression](../../notes/time_series/dynamic_regression.md).
