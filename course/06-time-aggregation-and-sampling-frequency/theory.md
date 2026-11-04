# Theory: time aggregation and sampling frequency

## Why the window and the aggregate function are part of the result

Raw monitoring data is almost never read raw: a dashboard shows one point per minute, a report one per day, a capacity review one per week. Each step reduces many values
to one, and **what you keep depends on the function (sum, mean, max, weighted mean) and on the window**. Choose badly and the burst that took the checkout down for an hour
disappears into a daily average, or a nightly batch job that saturates the CPU is never seen because the gauge is read only on the hour. Two separate questions are involved:

1. **Aggregation**: given fine-grained data, how do I combine it into coarser buckets correctly?
2. **Sampling**: given that data is only observed every $\Delta$ time units, which phenomena are visible at all?

## Pick the aggregate by what the metric *is*

| metric type | example | right daily aggregate | wrong one |
|---|---|---|---|
| **counter / amount** (additive) | requests, errors, revenue | sum | mean of the per-slot values times a different number of slots |
| **rate / ratio** | error rate, conversion rate | ratio of sums $\sum \text{errors}/\sum \text{requests}$ | mean of the per-slot ratios |
| **mean per slot** | mean latency per 15 min | weighted mean $\sum n_i\bar x_i/\sum n_i$ (weights = request counts) | unweighted mean of the $\bar x_i$ |
| **gauge** (level at an instant) | CPU %, queue length, temperature | mean for cost/typical level, **max** (or high percentile) for capacity and alarms, last for state | the value at one fixed instant |
| **percentile** | P95 latency | recompute from raw values or merge histograms | mean of per-slot P95 ([percentiles do not average](../03-percentiles-and-extreme-values/theory.md)) |

For a ratio with numerator $a_i$ and denominator $b_i$ in slot $i$ the correct aggregate is $\sum a_i / \sum b_i$, a *weighted* mean of the slot ratios $a_i/b_i$ with weights $b_i$.
The unweighted mean is a different statistic that over-represents low-traffic slots. This is the same mechanism as [Simpson's paradox](../05-sampling-bias-and-simpson-s-paradox/theory.md).

### Worked example

A night slot has 50 requests and 5 errors (10.0%); a day slot has 950 requests and 10 errors (1.05%). The mean of the two slot rates is 5.53%, the pooled rate is
$15/1000=1.50%$: the naive average is 3.7 times too high. The same two slots with mean latency 90 ms (night) and 160 ms (day) give a weighted mean of 156.5 ms
(the typical request saw a loaded system) against an unweighted 125.0 ms. In the data of this lesson, the pooled error rate and the mean of the interval rates differ in
exactly this way.

## Aggregation hides short events

A bucket average dilutes an event by the ratio of event duration to bucket length. In the dataset a one-hour outage has a 30 % failure rate at the worst 15-minute slots. The worst
error rate seen at each resolution is: 15 min 31%, 1 hour 29.1%, 1 day 3.2%, 1 week 1.1%. Alert on short windows (or on max / high percentiles), and report long windows for trend.
Averaging is a low-pass filter: it keeps the slow component (trend, seasonality) and removes the fast component (bursts). Useful for planning, dangerous for detection.

Related practical points: time zones and daylight-saving changes (a "day" can have 23 or 25 hours); partial buckets at the ends of the data; missing data (`AVERAGE` over what exists
versus `SUM` that silently undercounts); and week alignment (ISO week starts Monday).

## Sampling frequency and aliasing

A gauge sampled every $\Delta$ (sampling frequency $f_s=1/\Delta$) can represent only fluctuations slower than the **Nyquist frequency** $f_s/2$. A periodic component of frequency
$f > f_s/2$ is not lost: it is **aliased** to the apparent frequency

$$
f_\text{alias} = \left| f - k f_s \right|,\quad k = \text{the integer nearest to } f/f_s.
$$

Example: a process with a 60-minute cycle ($f=1/60$ per min) read every 45 minutes ($f_s=1/45$) appears to have $|1/60-1/45|=1/180$ per minute, a **180-minute cycle that does not exist**.
If it is read exactly once per cycle ($f_s=f$) the alias frequency is 0: it shows as a constant whose level depends on the phase of the reading.

That is what the CPU gauge in the data does. An hourly batch job runs about 15 minutes after the full hour. Reading the gauge on the hour never catches it (mean CPU 27.1 %), reading it at :15 always does
(77.2 %). Both are "correct" samples and both are misleading. For a short event of duration $T$ sample at least every $T/2$, store a **max** over each window next to the mean when you
downsample, or use event counters and histograms that accumulate between scrapes (the reason Prometheus counters and histograms survive coarse scrape intervals much better than gauges).

Before aggregating or resampling, aggregate in the direction that **preserves information for the decision**: sums and counts for volume, max and percentiles for risk, ratios of sums for rates.

## Assumptions and pitfalls

1. **Averaging an average** is only valid with equal weights (equal bucket sizes and equal counts); otherwise weight by the denominator.
2. **Aggregating after the ratio** (mean of hourly error rates) answers "what is a typical hour?", not "what did a request experience?". Decide which question you are asking.
3. **A coarser window cannot be un-aggregated.** Keep raw (or fine-grained) data for as long as storage allows; downsample with several functions (sum, max, count), not just the mean.
4. **Retention policies bite:** a five-minute series that is rolled up to one hour after 30 days has lost every short incident older than a month.
5. **Aligned sampling can alias** (cron jobs, hourly scrapes); jittering the scrape time or sampling faster reveals it.
6. **Bucket boundaries matter**: a burst across 14:55-15:05 is split between two hourly buckets and looks half as bad in each.
7. **Different windows, different statistics**: do not compare a daily mean with an hourly mean without saying so.

## Related notes

- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)
- [Trend, seasonality and noise](../07-trend-seasonality-and-noise/theory.md) and [rolling statistics](../10-rolling-statistics/theory.md)
- [Seasonality and trends](../../notes/time_series/seasonality_and_trends.md) and [frequency-domain analysis](../../notes/time_series/frequency_domain_analysis.md)
- [Statistical process control](../26-statistical-process-control/theory.md)
