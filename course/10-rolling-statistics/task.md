# Task: rolling statistics

## Scenario

You run reliability for a payments platform. The dashboard shows the daily average **payment-processing time** with one
fixed alert line (mean + 3 SD of everything so far). On-call engineers say it "cries wolf" during some weeks and stays
silent when a single day clearly looked wrong. You are asked to replace it with a rolling view and to explain, with data,
which window length and which rule you would use.

## Data

`data.csv` - 180 consecutive days from 2026-02-02 to 2026-07-31; one row = one day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `payment_ms` | average payment-processing time of that day (milliseconds) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. With a window of 14 days (including the current day), compute the rolling **mean, SD, minimum, maximum and 90th percentile**.
   Report the values on the last day.
2. How many days at the start have no rolling value, and on which date does the first one appear?
3. On which date is the rolling SD largest, and what is the ratio of its largest to its smallest value? Does the rolling mean change by
   a comparable factor?
4. Repeat the rolling SD for windows of 7 and 28 days. Compare the ratio largest/smallest and the dates of the maximum.
5. Compute the **global z-score** $(x-\bar x)/s$ and two **rolling z-scores** against the *previous* 14 and 28 days. How many days have
   $|z|>3$ in each case, and which days are they?
6. List the three days with the largest previous-14-day z-score and their z-scores under the other two rules. What happens to
   a spike of the same size inside and outside the volatile weeks?
7. Compute a z-score where the day is *inside* its own 14-day window. What is the largest value it can ever reach, and what does the
   first spike score?
8. *Interpretation:* which window and rule would you deploy, what do the first 13 days and the start of the volatile period tell you
   about the weak points of a rolling alert, and what does a flag actually mean?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- On "Payment time with rolling 3-SD band", how does the width of the band change over the period and why?
- Compare the flags there with the global flags in "The same data judged by one global rule". Which days differ?
- On "Rolling standard deviation by window length", which line reacts first when the spread jumps, and which is the smoothest?

## Deliverable

A short note (6-8 lines) for the on-call team with named parts: **Rule** (window, statistic, threshold), **Evidence** (flag
counts and example days for the old and the new rule), **Weak points** (edge effects, regime changes) and **Next step** (one
thing you would try, for example a median/MAD version).
