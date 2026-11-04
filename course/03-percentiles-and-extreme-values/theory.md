# Theory: percentiles and extreme values

## Why the mean is the wrong summary for latency

Response times, file sizes, incomes and queue lengths are **right-skewed**: most values are small and a few are very
large. The arithmetic mean is pulled towards those few large values, but it also *averages them away* when most users
are fast. Two systems with the same mean can deliver completely different experiences, so what matters is the **shape of
the distribution**, especially its tail.

## Definition

The **p-th percentile** $Q_p$ is a value such that a fraction $p/100$ of the observations are at or below it.
Equivalently, $Q_p = F^{-1}(p/100)$ where $F$ is the empirical distribution function.

- $P50$ is the **median**: half of the requests are faster.
- $P95$ is the value that 95 % of requests do not exceed; 1 in 20 requests is slower.
- $P99$, $P99.9$ describe the **tail**: what your unluckiest users see.

Do not confuse the two directions: $P95 = 230\,\text{ms}$ does **not** mean "95 % of requests exceed the SLO"; it means
5 % of requests take longer than 230 ms.

## Computing a sample percentile

Sort the $n$ observations $x_{(1)} \le \dots \le x_{(n)}$. The common "linear interpolation" definition (used by
Excel/Sheets `PERCENTILE`, `numpy.percentile`) places $x_{(k)}$ at position $(k-1)/(n-1)$ and interpolates:

$$
h = (n-1)\,p + 1,\qquad
Q_p = x_{(\lfloor h \rfloor)} + (h - \lfloor h \rfloor)\,\bigl(x_{(\lfloor h \rfloor + 1)} - x_{(\lfloor h \rfloor)}\bigr).
$$

Worked example with $n = 5$ values $\{12, 15, 20, 40, 200\}$ and $p = 0.9$: $h = 4 \cdot 0.9 + 1 = 4.6$, so
$Q_{0.9} = x_{(4)} + 0.6\,(x_{(5)} - x_{(4)}) = 40 + 0.6 \cdot 160 = 136$. Other textbooks use slightly different
interpolation rules, so small samples can give slightly different answers in different tools.

## Exceedance and SLOs

A **service-level objective** is a statement about a percentile or a proportion, for example "P95 latency below 250 ms"
or equivalently "at most 5 % of requests slower than 250 ms". The **exceedance share** for a threshold $c$ is

$$
\hat{\pi}(c) = \frac{\#\{x_i > c\}}{n}.
$$

Percentile and exceedance are two views of the same curve: $P95 \le c \iff \hat\pi(c) \le 5\%$.

## The tail needs enough data

An extreme percentile is determined by very few points. With $n = 600$ requests, $P99$ is decided by the 6 slowest
requests, and $P99.9$ by less than one. The standard error of a sample percentile grows quickly in the tail and with
heavy-tailed data, so:

- do not report $P99.9$ from a few hundred samples;
- compare tail percentiles over windows long enough to contain many tail events;
- use the bootstrap (lesson 17) to attach a confidence interval to a percentile.

## Percentiles do not average

You **cannot** compute the P95 of a day by averaging the P95 of each hour (or each server). Percentiles are not linear:
the P95 of a union depends on the whole distributions, not on their P95s. Either keep raw values, or store histograms and
merge the histograms.

This is also why Prometheus `histogram_quantile` is an *estimate*: it interpolates linearly inside a bucket, so its
accuracy is limited by the bucket boundaries. Pick buckets around your SLO threshold.

## Assumptions and pitfalls

1. **Pooling hides segments.** A healthy endpoint can mask a broken one in the pooled percentile; always slice by
   endpoint, region, customer tier.
2. **Aggregation window matters.** A one-minute P99 and a one-day P99 answer different questions.
3. **Coordinated omission.** If you only measure requests that completed, timeouts vanish from your percentiles.
4. **Mean versus percentile of means.** Averaging first and taking percentiles later (or the reverse) are different
   statistics.

## Related notes

- [Distribution shape and skewness](../01-distribution-shapes-and-heavy-tails/theory.md)
- [Robust statistics](../02-robust-statistics/theory.md)
- [Bootstrapping confidence intervals](../17-bootstrapping-and-confidence-intervals/theory.md)
