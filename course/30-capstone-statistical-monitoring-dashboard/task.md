# Task: capstone - a statistical monitoring dashboard for a checkout service

## Scenario

You are the new data analyst on the platform team of an online shop. Leadership asks for **one dashboard and one rule set** that tells on-call
engineers when the checkout service is degraded, without paging them for ordinary weekend dips. You have 90 days of daily metrics, the
deploy log, and a post-mortem list of the days that were later judged "degraded". Build the analysis, choose the alert policy, and write the
decision memo the head of engineering will read.

## Data

`data.csv` - 90 days (2026-08-03 to 2026-10-31), one row per day.

| column | meaning |
|---|---|
| `date` | calendar day (the series starts on a Monday) |
| `requests` | checkout requests that day |
| `p95_latency_ms` | 95th percentile of request latency for the day, milliseconds |
| `errors` | requests that ended in a server error |
| `deploy` | 1 on days a release was deployed |
| `incident` | 1 on days the post-mortem judged the service degraded, else 0 |

Treat days 1-45 as **phase I** ("normal"); use medians and MADs there.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. *Distribution.* Mean, median and skewness of `p95_latency_ms`; skewness of its natural logarithm. Which scale should the limits use?
2. Error rate (errors / requests) pooled over the first and over the last 45 days, and the median daily error rate in each half. Compare the two ratios: which one is more trustworthy, and why?
3. *Trend.* Fit a straight line to `requests` against the day number: slope, R-squared, growth per day as a share of the mean.
4. *Seasonality.* Divide requests by the trend, take the **median** ratio for each weekday. Highest and lowest factor? How do weekends compare with a Tuesday?
5. Build the expected requests (trend x weekday factor), the log residual and its robust z-score. How many days exceed $|z| > 3$ and what are they?
6. *Latency shift.* Standardise $\ln$(latency) with the phase-I median and robust sigma, cap $z$ at 3 and run an upper CUSUM ($k = 0.5$, $h = 5$). On which day does it alarm, and how many days after the last deploy?
7. *Error rate.* Compute $p_0$ (median phase-I rate), the binomial 3-sigma upper limit per day and the number of days above it before and after the last deploy. What does the pre-deploy count say about the binomial assumption?
8. *Combined detector.* Score each day as the maximum of $|z_{req}|$, $z_{lat}$ and the error-rate z. With $T = 3$: days flagged, TP, FP, FN, precision, recall against `incident`. Which flagged day is a false alarm and why?
9. Sweep $T = 2, 3, 4, 5, 6, 8$ and tabulate flagged, TP, FP, FN, precision, recall, F1. Which T would you deploy?
10. Write the **decision memo** (see Deliverable) and name two risks the numbers do not show.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Requests per day", which three events leave the alarm band and which of them was not an incident?
- In "p95 latency vs phase-I baseline" and "CUSUM of latency", why does the point rule stay quiet while the CUSUM alarms?
- In "Error rate with binomial control limits", what changes on the deploy day, and what do the two limit lines (3 sigma and T sigma) tell you about
  the choice of limit width?

## Deliverable

A one-page decision memo with four named parts: **Policy** (the detectors and the values of T, k, h), **Evidence** (flags, false alarms, misses,
the CUSUM lag after the deploy), **Alert load** (expected pages per month, how many false) and **Risks** (at least two: e.g. short phase I, label quality,
overdispersion, holidays). Include one chart.
