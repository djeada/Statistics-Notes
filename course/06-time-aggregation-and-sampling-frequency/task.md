# Task: time aggregation and sampling frequency

## Scenario

You maintain the metrics for a web shop. The management report is built from **daily** numbers and the capacity plan from **hourly CPU readings**. Two
sentences from last week's review make you suspicious: "the error rate is a steady 1 %, so nothing happened on any day" and "the servers never exceed 50 % CPU at the top
of the hour, so we can cut the instance count." You have the full 15-minute metrics for 14 days and must check what the coarser views hide, and which aggregation is correct for each metric.

## Data

`data.csv` - 1,344 rows, one per 15-minute slot, 2 Feb 2026 00:00 (Monday) to 15 Feb 2026 23:45.

| column | meaning |
|---|---|
| `timestamp` | start of the 15-minute slot |
| `requests` | requests served in the slot |
| `errors` | requests that returned an error in the slot |
| `mean_latency_ms` | mean response time in the slot (ms) |
| `cpu_pct` | CPU utilisation read at the start of the slot (%) - a gauge |

## Questions

Work in a spreadsheet (import `data.csv`; you will need `SUM`, `AVERAGE`, `MAX`, `SUMPRODUCT`, `COUNTIF` and blocks of 4 rows = 1 hour, 96 rows = 1 day), then compare with `solution.xlsx`.

1. Compute total requests and errors. Compute the error rate (a) as total errors / total requests and (b) as the average of the 1,344 interval error rates. Why do they differ?
2. Compute the mean latency (a) as the plain average of the 1,344 slot means and (b) weighted by `requests`. Which one describes the average request?
3. Aggregate to days: requests, errors, pooled error rate and the average of the interval rates. Which day is worst and how many times the median daily rate is it?
4. Aggregate to weeks. Compare each week's pooled error rate with the average of its seven daily rates.
5. Find the worst error rate at 15-minute, hourly, daily and weekly resolution. What does coarser aggregation do to the worst value, and what would an alert on daily data have shown?
6. Compute mean and peak CPU (a) from all 15-minute samples and (b) from only the sample at the top of each hour. How many samples reach 80 % in each case? How many hours have a MAX of at least 80 %?
7. Compute the mean CPU separately for the readings at minute 0, 15, 30 and 45 of the hour. What does the pattern tell you about the sampling interval of the CPU gauge?
8. *Explain in three sentences* which aggregate (sum, mean, weighted mean, ratio of sums, max) you would use for requests, error rate, latency and CPU in a capacity report, and one limitation of 14 days of data.

## Grafana

Import `grafana/dashboard.json` (no data-source setup is needed).

- In "Error rate: hourly vs daily aggregation", find the burst. When does it occur and how large is it on the hourly versus the daily line?
- In "CPU: what each way of reducing the data shows", which reduction would have triggered a 80 % alert and which never would?
- In "Mean CPU by the minute of the hour that is sampled", which minute is special and why?

## Deliverable

A short note (6-10 lines) titled *What the daily report and the hourly snapshot do not show* with three named parts: **Corrections** (the right error rate and latency, with numbers),
**Hidden events** (the incident and the CPU pattern, with the resolution at which each becomes visible) and **Recommendation** (aggregation and sampling rules for the report and the alerts).
Include one chart.
