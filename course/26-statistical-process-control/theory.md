# Theory: statistical process control

## Why control charts

A process (a furnace, an incubator, an API) wanders around its target because of many small causes: this is **common-cause
variation**. Occasionally something specific happens (a door is left open, a sensor fails, a heater degrades): an **assignable
(special) cause**. Reacting to common-cause noise (tampering) makes the process worse; ignoring a special cause lets it run.
A **Shewhart control chart** draws the centre line and limits that ordinary noise should (almost) never cross, and so turns
"is this reading odd?" into a rule you can apply consistently. It is a hypothesis test run repeatedly: each new point tests
"the process still behaves like the baseline".

## Phase I and Phase II

- **Phase I** (baseline): take a period when the process is believed to be stable, examine it, remove points with a known
  assignable cause, and estimate the centre $\bar x$ and the spread $\hat\sigma$.
- **Phase II** (monitoring): hold those limits fixed and test every new point. Limits are **not** recomputed from the data being
  monitored, otherwise a slow drift drags the limits with it.

## Individuals (I-MR) chart

For one reading per time step, limits are $\bar x \pm 3\hat\sigma$ with $\hat\sigma$ estimated from the **average moving range**

$$
\overline{MR} = \frac{1}{m-1}\sum_{i=2}^{m}|x_i-x_{i-1}|,\qquad \hat\sigma=\frac{\overline{MR}}{d_2},\quad d_2=1.128 .
$$

Why not simply use the sample SD of the baseline? The moving range measures only *short-term* point-to-point variation, so a
shift or excursion in the baseline touches just one or two ranges, while it inflates the sample SD of the whole baseline. A
contaminated baseline then produces limits that are too wide, and the chart cannot see the problem it was built to find.
The MR chart (UCL $=3.267\,\overline{MR}$) watches the spread itself.

**Worked example.** Ten readings $(37.1, 36.8, 37.0, 37.3, 36.9, 37.2, 37.0, 36.7, 37.1, 37.4)$: mean 37.05, $\overline{MR}=0.300$,
$\hat\sigma=0.266$ (sample SD $0.217$), limits $36.25 \ldots 37.85$. Now let three readings (6-8) be $+1.0$ too high, as in an excursion:
mean 37.35, sample SD $0.474$ but $\overline{MR}=0.433$, $\hat\sigma=0.384$. The SD grows by a factor 2.2 but the MR-based sigma only by a factor 1.44. The upper limit moves from 37.85 to 38.77 (SD) or
38.50 (MR-bar). With only ten points both estimates are hit hard; with a 60-100 reading baseline and a short
excursion the moving-range estimate is much less affected. Better still, remove the excursion rather than average it in.

## X-bar and R chart

With rational subgroups of size $n$ (here $n=5$ consecutive readings) plot the subgroup mean $\bar x_j$ and range $R_j$. Limits
$\bar{\bar x} \pm A_2\bar R$ and $D_4\bar R$ (for $n=5$: $A_2=0.577$, $D_4=2.114$). Averaging cuts noise by $\sqrt n$, so the chart
detects smaller sustained shifts, at the price of reacting only once a whole subgroup is complete. Choose subgroups so that
variation *within* a subgroup is common-cause only.

## Detection rules (Western Electric)

With $z=(x-\bar x)/\hat\sigma$ the zone rules flag: **1** a point beyond $\pm3$; **2** two of three consecutive points beyond $\pm2$ on the same
side; **3** four of five beyond $\pm1$ on the same side; **4** eight in a row on one side of the centre. Rule 1 finds large, sudden
changes; rules 2-4 find smaller sustained ones, which is how a drift is caught early. The price is false alarms. For independent
normal data a rule-1 flag has probability $2(1-\Phi(3))=0.0027$ per point (an average of about 370 points between false alarms).
A simulation of 2 million in-control points gave per-point flag rates of about 0.27% (rule 1), 0.30% (rule 2), 0.53% (rule 3),
0.77% (rule 4) and 1.8% for "any rule", roughly one false alarm per 55 points. More sensitivity always costs specificity
(lesson 29).

## Assumptions

1. Observations are independent. Sensor data are often autocorrelated; positive autocorrelation shrinks the moving ranges (limits too
   narrow, too many alarms) and creates long runs on one side of the centre.
2. Roughly normal, or at least symmetric, short-term variation; for skewed data transform or use percentile-based limits.
3. A baseline that really represents the stable process, with enough points (rule of thumb: 20-25 subgroups or 50-100 individual readings).
4. Fixed limits in Phase II; recalibrate only after a documented change.

## Pitfalls

1. **Contaminated baseline** (above): wide limits, missed signals.
2. **Using the sample SD of the monitoring data** for limits: the shift inflates the SD and hides itself.
3. **Chart limits vs specification limits**: control limits say what the process *does*, specs say what the customer *wants*; they are unrelated.
4. **Acting on every flag**: a 1-in-55 false alarm rate with rules 1-4 means alarms are expected in long series.
5. **Ignoring run structure**: a drift never crosses 3 sigma for a long time, but eight points above the centre line is already unusual.
6. **Rational subgroups**: grouping readings across a shift change or two machines turns special-cause variation into "within-subgroup noise".

## Related notes

- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md) and [outlier detection](../04-outlier-detection/theory.md)
- [Robust statistics](../02-robust-statistics/theory.md): MR-bar is a robust spread estimate in the same spirit
- [Rolling statistics](../10-rolling-statistics/theory.md)
- [Change-point detection](../27-change-point-detection/theory.md), [anomaly detection](../28-time-series-anomaly-detection/theory.md), [false alarms](../29-false-alarms-and-detection-performance/theory.md)
- Repo notes: [stationarity](../../notes/time_series/stationarity.md), [randomness tests](../../notes/time_series/randomness_tests.md)
