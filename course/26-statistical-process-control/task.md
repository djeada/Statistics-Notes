# Task: statistical process control

## Scenario

A cell-culture lab runs an incubator whose chamber temperature must stay near **37.0 C**. A sensor logs one reading every
5 minutes. The first 100 readings were taken right after a service visit and are believed to represent normal operation. The
lab manager wants a **control chart** that raises an alarm when the chamber stops behaving normally, and asks whether
control limits drawn from the first 100 readings are good enough. Your job: build the limits, decide which signals are real, and find out when
the process really changed.

## Data

`data.csv` - 400 readings, 2026-02-10 08:00 to 2026-02-11 17:15, one row per 5-minute reading.

| column | meaning |
|---|---|
| `timestamp` | time of the reading |
| `temp_c` | chamber temperature in degrees Celsius |

Number the readings 1..400. Two candidate baselines: **A = readings 1-100** (the lab's choice) and **B = readings 1-60**. Put the
baseline limits, the monitoring start (100) and the search start (200) in input cells.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. For baselines A and B compute the mean, the sample SD, the average moving range MR-bar (mean of |x[t] - x[t-1]| inside the baseline) and sigma = MR-bar / 1.128.
2. Build 3-sigma limits (mean +/- 3 sigma) for the four combinations: A or B, sigma from the sample SD or from MR-bar.
3. For each of the four limit sets, count the readings after reading 100 that lie outside the limits.
4. For each limit set, find the first reading after reading 200 that is outside the limits (0 if none).
5. Using baseline B (MR-based sigma), compute z = (x - mean) / sigma and Western Electric rules 1-4. Count flags per rule and find the first flag after reading 200 for each rule.
6. How many flags does chart B raise among readings 61-100? What do they have in common? What does it say about baseline A?
7. Group readings in subgroups of 5. Build an X-bar / R chart with limits from the first 12 subgroups (A2 = 0.577, D4 = 2.114). How many subgroup means leave the limits after the baseline, and at which subgroup does X-bar first signal after reading 200?
8. For normal in-control data, what is P(|z| > 3), the average run length between rule-1 false alarms, and how many false alarms do you expect among 400 readings?
9. *Explain in 3-4 sentences* whether the problem you found is a sudden shift or something else, what you would do on the first alarm, and which assumption of the chart you worry about most.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Individuals chart", which red dots are isolated and which form a pattern? Compare the orange line with the red limit.
- In "X-bar chart", which red dots belong to the baseline excursion and when does the drift first push the means out? Compare with the individuals chart.
- In "First signal after reading 200", rank the detectors. Which one never or almost never fires?

## Deliverable

A short note (6-8 lines) for the lab manager: *is the incubator in control, when did it stop being so, and which chart would you
install?* Include the individuals chart with limits and one table comparing the detectors. State one risk of acting on every alarm.
