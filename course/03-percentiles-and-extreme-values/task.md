# Task: percentiles and extreme values

## Scenario

You run the on-call rotation for an e-commerce API. The dashboards show an average latency of "about 115 ms" and the
team believes the service meets its objective: **P95 latency below 250 ms**. Support keeps getting complaints about slow
checkouts. Your job is to find out whether the average is hiding a problem.

## Data

`data.csv` - 600 requests, one every 5 seconds (09:00:00 - 09:49:55).

| column | meaning |
|---|---|
| `timestamp` | when the request arrived |
| `endpoint` | `search`, `checkout` or `profile` |
| `latency_ms` | server response time in milliseconds |
| `status` | HTTP status code |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the **mean** latency. Does it meet a 250 ms objective?
2. Compute **P50, P90, P95, P99** and the maximum. How many times larger is P99 than the median?
3. What share of requests is slower than 250 ms? How many requests is that?
4. Compute count, mean, P50, P95 and P99 **per endpoint**. Which endpoint violates the objective?
5. Split the data into windows of 50 consecutive requests (5 minutes each) and compute mean, P95 and P99 per window.
   In which window does the tail explode? What happens to the mean in the same window?
6. Change the threshold to 150 ms. How does the exceedance share change, and what does that say about choosing
   an SLO from the average?
7. *Explain in two sentences* why you cannot average the 12 window P95 values to obtain the P95 of the whole run.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- Find the degraded period on the "Raw request latency vs SLO" panel. Which time range is it?
- Compare "Mean vs tail per 5-minute window" with your table from question 5.
- Which endpoint's bar breaks the SLO line in "Percentiles by endpoint"?

## Deliverable

A short note (5-8 lines) answering: *Is the service meeting its SLO, for whom is it failing, and since when?*
Include one chart and state one limitation of using 600 requests to estimate P99.
