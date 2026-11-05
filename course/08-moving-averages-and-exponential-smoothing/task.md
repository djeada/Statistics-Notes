# Task: moving averages and exponential smoothing

## Scenario

You lead customer support analytics. Product shipped a pricing-page release on **2026-04-27** and asked you to set up an
alert that fires when daily ticket volume rises above **215 tickets** *on a smoothed basis*: the raw daily number is too
noisy to alert on. You must choose a smoother and show the trade-off to the on-call manager: how quickly does each
option fire after a real change, and how often does it fire when nothing happened?

## Data

`data.csv` - 140 consecutive days from 2026-02-02 (a Monday) to 2026-06-21; one row = one day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `tickets` | new support tickets opened that day (count) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute a **trailing 7-day SMA**. What is its value on the last day, how many rows are empty, and how old (on average,
   in days) is the data inside the window?
2. Compute a **centred 7-day MA** as well. On which rows is it defined, and how does its timing compare with the trailing
   SMA around the release date?
3. Compute **EWMA** with alpha = 0.3 (fast) and alpha = 0.1 (slow), starting from the first observation. What are the last
   values, and which alpha has the same average age as a 7-day SMA?
4. For each series (raw, SMA 7, SMA 21, centred MA 7, EWMA fast, EWMA slow) compute the **standard deviation over days 22 to the
   release** (before the release). How much noise does each one remove? Which smoother removes more than its alpha/window
   suggests, and why?
5. Create alert flags (smoothed value > 215). For each series count the alerts **before** the release and find how many days after
   it the first alert occurs.
6. Compute a one-step forecast RMSE (forecast for day t+1 = EWMA at day t) for alpha = 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9.
   Which alpha is best?
7. Change the window input to 21. What happens to noise and delay?
8. *Interpretation:* which smoother would you deploy for the alert, and why can the centred MA not be used?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Tickets per day and three smoothers", where do the curves cross the threshold relative to each other? Which one is last?
- In "Weights on past observations", why does the EWMA 0.1 bar series reach so far back, and what does that mean for its delay?
- In "Noise left vs days to alert", is there any series that is both quick and smooth?

## Deliverable

A note (6-8 lines) for the on-call manager with named parts: **Recommendation** (smoother and parameter), **Evidence** (delay
and false alerts of at least three options), **Trade-off** (what you give up) and **Caveat** (one limitation, e.g. a single
release, weekday pattern, start-up).
