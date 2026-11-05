# Theory: robust statistics

## Why a few points can ruin an average

Sensors glitch, logs contain sentinel values (`-1`, `9999`, `85.0`), a data-entry slip adds a zero. If your estimate changes a lot
when a handful of observations change, it is not safe to run unattended: a dashboard, a control chart or a forecasting pipeline fed with it
will fail silently. **Robust statistics** are estimators whose value stays close to the "right" answer when a small share of the data is
arbitrarily wrong or comes from a different process. The price is a little less precision on perfectly clean, normal data.

## How we measure robustness

Two ideas capture most of what you need.

- **Breakdown point**: the smallest fraction of observations that can be replaced by arbitrary values to make the estimator
  arbitrarily bad. The sample mean and the standard deviation have breakdown point 0 (one bad value is enough), the median and the MAD have 50 %
  (the maximum possible), the IQR 25 %, a trimmed mean with $\alpha$ trimmed from each tail has $\alpha$.
- **Influence**: how much one extra observation at value $x$ moves the estimate. For the mean it is $(x-\bar x)/(n+1)$ - unbounded in $x$.
  For the median it is bounded: once $x$ is beyond the centre, it only changes which of the middle order statistics is selected.

## The estimators

**Centre.**

- *Median*: the middle order statistic (average of the two middle ones for even $n$).
- *Trimmed mean*: sort, drop the lowest and highest $\alpha n$ values, average the rest. Excel/Sheets `TRIMMEAN(range, p)` takes $p$ as the **total**
  proportion removed (both tails) and removes $\lfloor np/2\rfloor$ from each end.
- *Winsorised mean*: instead of dropping the extremes, clip them to the $\alpha$ and $1-\alpha$ percentiles, then average. It keeps the sample size
  (and the weight of the tail observations, but capped).

**Scale.**

- *IQR* $= Q_3 - Q_1$. For normal data $\text{IQR}\approx1.349\,\sigma$, so $\text{IQR}/1.349$ estimates $\sigma$.
- *MAD* $=\operatorname{median}_i\,|x_i-\operatorname{median}(x)|$. For normal data $\text{MAD}\approx0.6745\,\sigma$, so
  $\hat\sigma = 1.4826\cdot\text{MAD}$ (since $1.4826 = 1/\Phi^{-1}(0.75)$).

The factors 1.349 and 1.4826 make the estimators agree with $\sigma$ *for normal data*; for skewed data the scaled MAD or IQR is a robust measure of
spread, not an estimate of the SD.

## Worked example

Nine readings of a room temperature: $21.4,\ 21.6,\ 21.5,\ 21.7,\ 85.0,\ 21.3,\ 21.5,\ 21.6,\ 21.4$ (the 85.0 is a sensor reset code).

- mean $=28.56$, SD $=21.17$ - both useless.
- median $=21.5$. Absolute deviations from it, sorted: 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 63.5; their median is MAD $=0.1$, so $1.4826\cdot\text{MAD}=0.15$.
- Without the 85.0 the mean is 21.50 and the SD 0.13; the median-based answers were already close to these.
- A 25 % trimmed mean drops the two smallest and two largest values: 21.53.
- Winsorising at P10/P90 (bounds 21.38 and 34.36 with linear-interpolation percentiles, as `PERCENTILE` computes) gives a mean of 22.94.

One bad value out of nine moved the mean by 7.1 C and multiplied the SD by about 162; the median moved by 0.00 C.

## Choosing an estimator

| situation | centre | scale |
|---|---|---|
| clean, symmetric, light tails | mean | SD |
| a few suspected gross errors | median or 5-10 % trimmed mean | 1.4826 MAD or IQR/1.349 |
| heavy tails that are real (not errors) | median plus the mean (they answer different questions) | MAD, quantile ranges |
| need to use all points but cap influence | winsorised mean | winsorised SD |

For normal data the median has asymptotic efficiency $2/\pi\approx 64\,\%$ relative to the mean (its sampling variance is 1.57 times larger); a 10 % trimmed mean
loses only a few percent. That is the insurance premium for robustness.

## Assumptions and pitfalls

1. **Robust is not "ignore the data".** A median does not tell you that 3 % of your readings are `85.0`. Always count and look at the points
   that robust and classical estimates disagree about (see [outlier detection](../04-outlier-detection/theory.md)).
2. **Breakdown is a limit.** If a third of the readings are corrupted a 10 % trimmed mean fails; if more than half are, nothing can save the median.
3. **Genuine heavy tails are not contamination.** Robust centres of a [heavy-tailed](../01-distribution-shapes-and-heavy-tails/theory.md) variable estimate the typical
   value, not the total; the mean is still the right target for totals.
4. **Ties break the MAD.** If more than half of the values are identical (counts, rounded data) then MAD $=0$ and any observation
   is "infinitely" far; use IQR or add a small floor.
5. **Different tools, different conventions.** `TRIMMEAN` takes a total proportion; `PERCENTILE` interpolates linearly; `STDEV` is the sample SD ($n-1$).
6. **Robust standard errors are a different topic.** The median's sampling error is not $s/\sqrt n$; use the bootstrap ([lesson 17](../17-bootstrapping-and-confidence-intervals/theory.md)).

## Related notes

- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)
- [Outlier detection](../04-outlier-detection/theory.md)
- [Descriptive statistics](../../notes/foundations/descriptive_statistics.md)
