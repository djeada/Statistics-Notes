# Theory: distribution shapes and heavy tails

## Why the shape matters before any statistic

Every summary statistic is a compromise, and which compromise is sensible depends on the **shape** of the distribution.
For a symmetric, thin-tailed variable the mean, median and mode agree and the standard deviation (SD) describes spread well.
For basket values, session lengths, incomes, file sizes or incident costs they do not agree, and quoting "mean +/- SD" can
be actively misleading. Looking at the shape first prevents two classic failures: reporting an "average customer" who does
not exist, and trusting a $\pm 2$ SD rule that only works for bell curves.

## Describing shape with moments

For a sample $x_1,\dots,x_n$ with mean $\bar x$ and standard deviation $s$ (denominator $n-1$, `STDEV.S`), the
**skewness** measures asymmetry and the **excess kurtosis** measures tail weight relative to a normal distribution:

$$
g_1 = \frac{1}{n}\sum_{i=1}^n \left(\frac{x_i-\bar x}{s}\right)^3,\qquad
g_2 = \frac{1}{n}\sum_{i=1}^n \left(\frac{x_i-\bar x}{s}\right)^4 - 3 .
$$

Spreadsheets apply small-sample corrections: Excel/Sheets `SKEW` returns the adjusted $G_1 = g_1\sqrt{n(n-1)}/(n-2)$ and
`KURT` returns the adjusted *excess* kurtosis $G_2$. They are exactly `scipy.stats.skew(x, bias=False)` and
`scipy.stats.kurtosis(x, bias=False)`; this course uses the spreadsheet versions. A normal distribution has skewness 0 and
excess kurtosis 0. Positive skew means a long right tail; positive excess kurtosis means more probability far from the centre
(and, perhaps counter-intuitively, usually also more mass near the centre) than a normal with the same SD.

Because the third and fourth powers weigh large deviations enormously, **one point can dominate both numbers**.

### Worked example

Take $\{2,3,3,4,5,6,100\}$. The mean is 17.57, the median 4, $s = 36.37$, `SKEW` = 2.64,
`KURT` = 6.97. Remove the 100 and the same statistics are mean 3.83, median 3.5, `SKEW` = 0.42.
One observation out of seven multiplied the mean by 4.6, but moved the median only from 3.5 to 4.

## Mean, median and the ordering of the three

For a right-skewed variable the usual ordering is mode < median < mean. The mean/median ratio is a quick skew diagnostic: close
to 1 for symmetric data, well above 1 for right-skewed positive data.

## Lognormal and power-law tails

Two families produce most real right-skewed data.

**Lognormal.** If $\ln X \sim N(\mu,\sigma^2)$ then $X$ has median $e^{\mu}$ and mean $e^{\mu+\sigma^2/2}$, so
mean/median $= e^{\sigma^2/2}$. With $\mu=\ln 42$ and $\sigma=0.5$ the median is 42 and the mean 47.6
(ratio 1.133); with $\sigma=1$ the ratio is already 1.649. All moments exist, and a log transform makes the data normal.
The geometric mean $\exp(\bar{\ln x})$ estimates the median $e^{\mu}$.

**Power law (Pareto).** The survival function is $P(X>x) = (x_m/x)^{\alpha}$ for $x\ge x_m$. On a log-log plot of
$P(X>x)$ against $x$ this is a straight line with slope $-\alpha$. The **tail index** $\alpha$ controls which moments exist:
$E[X^k]$ is finite only for $k<\alpha$. For $\alpha\le 2$ the variance is infinite; for $\alpha\le 1$ even the mean is.
With $x_m=150$ and $\alpha=1.8$, $P(X>600) = 8.2\,\%$ and $P(X>1200) = 2.37\,\%$: each doubling of the threshold
removes only a factor $2^{1.8}\approx 3.5$ of the probability, where a normal tail would fall away vastly faster.

The **Hill estimator** uses the $k$ largest observations $x_{(1)}\ge\dots\ge x_{(n)}$:

$$
\hat\alpha = \left[\frac{1}{k}\sum_{i=1}^{k}\ln x_{(i)} - \ln x_{(k+1)}\right]^{-1}.
$$

It is only meaningful for the tail (choose $k$ so that the log-log plot is straight above $x_{(k+1)}$), and it is noisy for small $k$
and biased for large $k$.

## What heavy tails do to familiar tools

- **The mean converges slowly** or not at all. Even when the mean exists, a handful of tail orders decide the total; the running
  mean keeps jumping, the running median settles quickly (lesson [2](../02-robust-statistics/theory.md)).
- **Rules based on $\bar x \pm k s$ break.** The SD is inflated by the very points you want to detect, so more data fall within
  $\pm 2$ SD than the 95.4 % of a normal (see [outlier detection](../04-outlier-detection/theory.md)).
- **Concentration:** in a heavy-tailed population a few percent of units produce a large share of the total. Report the share
  of the top 1 % and 10 %, not only an average.
- **Log transform:** analysing $\ln x$ often restores symmetry (lognormal) and linearises multiplicative effects, but a Pareto
  tail stays right-skewed after the log, and the back-transformed mean of logs is the geometric mean, not the arithmetic mean.

## Assumptions and pitfalls

1. **Skewness and kurtosis from small samples are unstable.** With about 5 % of the observations in the tail, a sample of
   a few hundred contains only a few dozen tail points; treat $g_2$ and $\hat\alpha$ as rough indications.
2. **Kurtosis is not "peakedness".** It measures the contribution of extreme deviations; compare shapes with a histogram.
3. **A single threshold hides the shape.** A linear histogram of heavy-tailed data shows one tall bar and an empty axis;
   use a log scale or a log-log survival plot.
4. **Mixtures look like heavy tails.** The basket data here are a mixture (ordinary orders plus a few business orders).
   Segment first; the heavy tail may come from one identifiable group.
5. **Do not delete the tail to "fix" the shape.** The tail orders are real revenue; decide per question whether the mean
   (totals) or a robust centre (typical case) is the right summary.

## Related notes

- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)
- [Robust statistics](../02-robust-statistics/theory.md)
- [Descriptive statistics](../../notes/foundations/descriptive_statistics.md) and
  [statistical moments](../../notes/random_variables_and_distributions/statistical_moments.md)
- [Bootstrapping confidence intervals](../17-bootstrapping-and-confidence-intervals/theory.md)
