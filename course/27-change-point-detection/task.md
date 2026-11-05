# Task: change-point detection

## Scenario

The jacket temperature of a chemical reactor is read every hour. The set-point is 70 C and the control chart has
been quiet for two weeks, yet the quality lab suspects the reactor now runs slightly warmer than it did in early May. A
Shewhart chart (3-sigma limits) has not complained. You must decide whether the process mean has really moved, estimate when,
and propose an alarm rule that would have caught it quickly without crying wolf.

## Data

`data.csv` - 240 hourly readings from 2026-05-04 00:00 to 2026-05-13 23:00.

| column | meaning |
|---|---|
| `timestamp` | hour of the reading |
| `reading` | reading number 1-240 |
| `temp_c` | jacket temperature, degrees Celsius |

Treat readings 1-100 as **phase I** (the process is known to be in control).

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. From phase I compute $\mu_0$ (mean) and $\sigma_0$ (sample standard deviation); standardise all 240 readings.
2. How many readings fall beyond $\pm 3\sigma_0$ in total, and how many in phase I? What is special about the phase-I one?
3. Build the upper and lower CUSUM with $k = 0.5$ and $h = 5$. At which reading and timestamp is the first alarm, and on which side?
4. Estimate the start of the change from the CUSUM (last zero of $C^+$ before the alarm, plus one).
5. For every split point from reading 10 to 230 compute the two-mean SSE. Which split minimises it? Report both means, the shift
   in C and in units of $\sigma_0$, and the percentage reduction of SSE compared with a single mean.
6. How many readings after the best split does the CUSUM alarm?
7. Compute the first alarm for $h = 2, 3, 4, 5, 6, 8$ ($k$ fixed). Which values of $h$ raise a false alarm before the change? Compare their ARL0
   and delay. Which $h$ would you deploy?
8. Change $k$ to 0.25 and to 1.0 with $h = 5$. How does the alarm time change, and why?
9. *Limitations:* name two assumptions behind the split estimate and the CUSUM that this data might violate.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Temperature with Shewhart limits and the two-mean fit", does any single point justify an alarm? What does the stepped line add?
- In "CUSUM statistics vs decision threshold h", what happens to C+ around the phase-I spike and what happens after the change?
- In "SSE of the two-mean fit by candidate split", where is the minimum and how sharp is it?

## Deliverable

A short note (5-8 lines) with three named parts: **Finding** (has the mean moved, by how much, since when), **Alarm rule**
(your k and h with the reason) and **Risk** (expected false-alarm spacing and expected delay).
