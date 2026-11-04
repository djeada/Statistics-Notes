# Theory: outlier detection

## Why "find the outliers" is a decision, not a calculation

An outlier is an observation that looks inconsistent with the rest *under some model of the data*. Every detection rule encodes such a model
(a bell curve, a quartile range, a robust spread), and every rule can be wrong in two ways: **false alarms** (unusual but legitimate points)
and **misses** (errors that the rule's own yardstick hides). Outlier detection prevents two failures at once: silently averaging garbage into a
KPI, and silently deleting the most informative observations (the viral order, the real incident). The statistics only nominate candidates; the
decision to correct, keep or delete needs context.

## Three standard rules

Let $\bar x$ and $s$ be the mean and sample SD, $\tilde x$ the median, $\text{MAD}=\operatorname{median}|x_i-\tilde x|$, and $Q_1,Q_3$ the quartiles with
$\text{IQR}=Q_3-Q_1$ (linear-interpolation quartiles, as `QUARTILE` computes).

1. **z-score:** flag $|z_i|>c$ with $z_i=(x_i-\bar x)/s$ and $c=3$. For *normal* data a fraction $2\cdot0.00135 = 0.27\,\%$ of points exceed 3 by chance,
   so about 0.8 false alarms are expected among 300 clean points.
2. **Tukey fences:** flag $x_i<Q_1-k\,\text{IQR}$ or $x_i>Q_3+k\,\text{IQR}$, with $k=1.5$ ("outside") or $k=3$ ("far out"). Quartiles are robust and no normality
   is assumed, but the fences are symmetric around the box, so they over-flag in skewed data.
3. **Modified z-score (Iglewicz-Hoaglin):** $M_i = 0.6745\,(x_i-\tilde x)/\text{MAD}$, flag $|M_i|>3.5$. It is the z-score with median and MAD replacing
   mean and SD (lesson [robust statistics](../02-robust-statistics/theory.md)); the constant 0.6745 makes MAD comparable to $\sigma$ for normal data.

## Worked example: one outlier

Ten values $10,11,11,12,12,13,13,14,15,90$. Mean $20.1$, SD $24.61$, so $z(90)=2.84$ - **below 3, not flagged**, although 90 is plainly wrong.
This is not bad luck: in a sample of size $n$ no observation can have $|z|>(n-1)/\sqrt n$, which is 2.85 for $n=10$, so a 3-SD rule cannot flag anything in a sample of ten.
The robust rules have no such limit: median 12.5, MAD 1.5, $M(90)=34.8$; quartiles 11.25 and 13.75 give IQR 2.50 and an upper fence of 17.50, so 90 is far outside.

## Masking

Now append three more, similar errors: $\dots,15,90,95,100,105$. The mean jumps to 38.5 and the SD to 41.1, so $z(90)=1.25$ and the 3-SD limit is 162:
**nothing is flagged**, although 4 of 13 values are wild (here the cap $(n-1)/\sqrt n$ is 3.33, but the real cause is the inflated SD). The outliers inflated the mean and SD they were being measured with: this is *masking*. The median (13.0) and MAD (2.0)
barely move, so $M(90)=26.0$ still flags all four. Masking is why a z-score is acceptable as a quick check on a clean variable with at most one or two suspects,
but not as a general-purpose detector. The opposite problem, *swamping* (a good point flagged because bad points shifted the centre), arises with the same mechanism.

## Skewed data and transformation

For right-skewed amounts (prices, durations) any symmetric rule on the raw scale flags legitimate high values and never flags low ones. Apply the rule to
$\ln x$ (or another normalising transform), then interpret the flags on the original scale. The log turns "10 times the typical value" into a fixed distance
on the axis regardless of the level.

## From flags to decisions

A flagged point belongs to one of four cases, and the rule cannot tell which:

| cause | example | action |
|---|---|---|
| recording / unit error | price typed 100x too large | correct if the true value is recoverable, otherwise mark missing |
| different population | wholesale order inside a retail data set | keep, analyse separately (segment) |
| genuine extreme of the same process | rare large but legitimate order | keep; use robust summaries or a heavy-tail model |
| signal | the first sign of a fault or an incident | investigate; this is what you are monitoring for |

Good practice: ask *why*, using other columns (here: unit price against the category median); document every rule and threshold; report results with and without
the points; never delete silently. Deleting everything the rule flags changes the estimand: here it would understate total spend by the value of the legitimate large orders.

## Assumptions and pitfalls

1. **Thresholds are conventions.** 3 SD, 1.5 IQR and 3.5 are defaults, not laws; the expected number of false alarms grows with $n$ (0.27 % of 10 000 points is 27 points).
2. **Multiple testing.** Scanning many series or many windows with a 3 sigma rule will produce false alarms every day; see [false alarms and detection performance](../29-false-alarms-and-detection-performance/theory.md).
3. **Univariate rules miss contextual outliers.** An amount can be unremarkable overall yet impossible for its category or time of day; condition on context or build a
   residual first ([residual analysis](../15-residual-analysis-and-model-diagnostics/theory.md)).
4. **Time series.** In a series with trend or seasonality a point is unusual relative to its expected value, not to the global mean ([time-series anomaly detection](../28-time-series-anomaly-detection/theory.md)).
5. **Swamping the tails.** If the data are genuinely [heavy-tailed](../01-distribution-shapes-and-heavy-tails/theory.md), a large share of "outliers" are ordinary.
6. **A MAD of 0** (many repeated values) makes the modified z undefined; use the IQR or a floor.

## Related notes

- [Robust statistics](../02-robust-statistics/theory.md)
- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)
- [Normal curve and z-score](../../notes/random_variables_and_distributions/normal_curve_and_z_score.md)
