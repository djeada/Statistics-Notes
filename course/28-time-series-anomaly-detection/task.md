# Task: time-series anomaly detection

## Scenario

A refrigeration compressor housing has a temperature probe whose **daily mean** is logged. The plant runs Monday to Friday and idles
at the weekend. The current alert rule ("one global robust z-score, alarm above 3.5") pages the on-call technician every
weekend, so the team wants to switch it off. Before they do, you must build a detector that respects the weekly cycle,
test it against the maintenance log, and say which kinds of events it can and cannot catch.

## Data

`data.csv` - 154 daily means (22 weeks, Monday 2026-01-05 to Sunday 2026-06-07).

| column | meaning |
|---|---|
| `date` | calendar day |
| `weekday` | Mon ... Sun |
| `temp_c` | daily mean housing temperature, degrees Celsius |
| `event` | maintenance log label: `none`, `spike` (brief fault, one day) or `shift` (a persistent change, every day from the first labelled day on) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the mean temperature for each weekday over the first 6 weeks (days 1-42). How large is the spread between the highest and the
   lowest weekday?
2. *Naive detector.* Take the median and $1.4826\times\mathrm{MAD}$ of days 1-42, standardise all 154 days and flag $|z|>3.5$.
   How many days are flagged, and how many of them are Saturdays or Sundays?
3. For 2026-03-09 compute the seasonal baseline (median of the previous four same weekdays), the residual, the robust scale (
   $1.4826\times$ the median absolute residual of the previous up-to-28 residuals) and the z-score.
4. Score every day from day 43 on. With $T=3.5$: how many days are flagged, how many of the labelled spikes are caught and how many
   flags fall on ordinary days (`none`)?
5. Which labelled spike is not detected, and why?
6. For the `shift` period: how many days are flagged, on which day does the flagging stop, and why does it stop although the
   process is still wrong?
7. Repeat the count of flags by group for $T=2.5, 3, 3.5, 4, 5, 6$. Which $T$ would you use, and what do you give up at each end?
8. *Limitations:* name two situations in which this seasonal detector fails (data or process), and one thing you would add to it.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Daily temperature, seasonal baseline and alarm band", where are the orange dots and which labelled events do they match?
- Compare "Naive z-score" with "Robust residual z-score": what pattern does the first show that the second removes?
- In "Days flagged by the seasonal detector", which `event` values appear, and what does that say about the false-alarm rate?

## Deliverable

A short note (5-8 lines) with three named parts: **Recommendation** (replace the old rule or not, with the T you chose),
**Evidence** (flags, catches, false alarms, weekend flags before and after) and **Blind spots** (what it will not catch, e.g. a persistent shift).
