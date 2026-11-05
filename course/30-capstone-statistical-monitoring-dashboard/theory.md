# Theory: a statistical monitoring dashboard, end to end

## Why a capstone

Every earlier lesson answers one question: is the distribution skewed, is there a trend, is this point unusual, has the level moved, how many alerts
are false. A real monitoring system needs all of them at once, chosen so that the people who are paged trust the pages. A dashboard
that shows a latency line and a red threshold is not monitoring; monitoring is a **policy** (what to watch, what counts as abnormal, who is told)
together with **evidence** that the policy works. This lesson walks through building one for the daily metrics of a checkout service:
requests, p95 latency and error count.

## The workflow

1. **Frame the decision.** What action does an alert trigger (page, rollback, ticket)? What does a false alarm cost versus a miss
   ([lesson 29](../29-false-alarms-and-detection-performance/theory.md))? The answer fixes how aggressive the thresholds should be.
2. **Look at the distribution first** ([lesson 1](../01-distribution-shapes-and-heavy-tails/theory.md),
   [3](../03-percentiles-and-extreme-values/theory.md)). Daily p95 latency here has skewness 5.02, which drops to 3.24 after taking logs
   (what remains is a handful of genuinely extreme days): latency is multiplicative, so limits belong on the log scale where "12 % slower" is one fixed distance whatever the baseline.
3. **Remove trend and seasonality** ([lesson 7](../07-trend-seasonality-and-noise/theory.md)). Requests grow linearly and have a strong weekday factor
   (weekends at about 0.79 of the trend). Fit the trend, take the *median* ratio to trend per weekday (robust to the very anomalies we want to find), and
   score the residual $z=\ln(\text{requests}/\text{expected})/\hat\sigma$ with $\hat\sigma=1.4826\cdot\text{median}|\ln\text{residual}|$
   ([lesson 28](../28-time-series-anomaly-detection/theory.md)).
4. **Pick a detector per failure type.**
   - *Point anomalies* (outage, spike): robust z-scores, flag $|z|>T$.
   - *Sustained small shifts* (a release that is 12 % slower): CUSUM on the standardised log latency
     ([lesson 27](../27-change-point-detection/theory.md)), with a **Winsorising cap** (here 3) so that one extreme day cannot trigger it.
   - *Rates* (errors per request): a p-chart. With daily volume $n_t$ the binomial standard deviation of the observed rate is
     $\sqrt{p_0(1-p_0)/n_t}$, so the limit moves with traffic. Worked example: $p_0=0.0074$ and $n=136,206$ give
     $\sigma=0.000233$ and a 3-sigma upper limit of 0.0081 ([lesson 26](../26-statistical-process-control/theory.md)).
5. **Combine and calibrate.** Reduce the detectors to one *sigma-scale* score, here $\max(|z_{req}|,z_{lat},z_{err})$, and choose $T$ from labelled history
   with a threshold sweep (precision, recall, F1, cost). A maximum over three scores raises the false-alarm rate roughly threefold compared with one score
   at the same $T$; that is the price of watching three things.
6. **Write the decision memo**: the policy (what, which $T$, $k$, $h$), the evidence (flags, false alarms, misses, delays), the expected alert load per
   month, and the risks.

## Phase I and what it assumes

All baselines are estimated on the first 45 days with medians and MADs, because the phase-I window itself contains an outage, a marketing surge and a
holiday. A mean and standard deviation would be inflated by exactly these days; the median is not
([lesson 2](../02-robust-statistics/theory.md)). If phase I contained a regression, the detectors would be calibrated to the broken state.

## Reading the results as a decision-maker

- A **sustained** problem (the release regression) is found by the CUSUM 60 - 58 days after the deploy, even though almost no single day
  looks extreme; a pure point detector would only flag the worst of those days. That lag is the detection delay of [lesson 29](../29-false-alarms-and-detection-performance/theory.md).
- A **legitimate** change (public holiday) is flagged because the model knows nothing about it. Add a calendar of known events, or accept this
  false alarm and say so in the memo.
- **Overdispersion**: the day-to-day variation of the error rate is larger than binomial sampling alone predicts (retries, client mix),
  so binomial limits give extra pre-deploy exceedances. Either widen the limits (use $T$ rather than 3) or estimate the extra variance (Laney p').

## Assumptions and pitfalls

1. **Evaluating on the data you tuned on.** The sweep here uses all 90 days; the honest procedure is to tune on one period and report on the next.
2. **Labels are post-hoc.** Every day after the deploy is labelled an incident, but a team would not have ticketed most of them; precision depends on who labels.
3. **A linear trend fitted on all days** is slightly bent by the anomalies; refit after removing flagged days.
4. **Multiple detectors, multiple false-alarm budgets.** Count alerts per month, not per detector.
5. **Alert fatigue** is the real failure mode: a rule with 90 % recall that pages ten times a week will be muted.
6. **Averages are not monitoring.** The overall mean latency changes by little; the decision-relevant facts are the shift after the deploy and the error rate.

## Related notes

- [Percentiles](../03-percentiles-and-extreme-values/theory.md), [trend and seasonality](../07-trend-seasonality-and-noise/theory.md),
  [rolling statistics](../10-rolling-statistics/theory.md), [prediction intervals](../25-prediction-intervals-and-forecast-uncertainty/theory.md)
- [Statistical process control](../26-statistical-process-control/theory.md), [change points](../27-change-point-detection/theory.md),
  [anomaly detection](../28-time-series-anomaly-detection/theory.md), [detection performance](../29-false-alarms-and-detection-performance/theory.md)
- Repo notes: [seasonality and trends](../../notes/time_series/seasonality_and_trends.md), [descriptive statistics](../../notes/foundations/descriptive_statistics.md)
