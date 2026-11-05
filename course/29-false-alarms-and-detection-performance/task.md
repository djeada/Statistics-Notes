# Task: false alarms and detection performance

## Scenario

A furnace-zone temperature is logged every hour and compared with the controller's set-point (70 C by day, 66 C at night). An
alarm raises a ticket for a technician. Operations kept a log of confirmed fault periods during June and now ask three things:
how good is a "3-sigma" alert rule, what happens if you move the threshold, and whether the rule would still be useful in a month
when faults are much rarer. A missed fault reading costs about 10 times as much as a false alarm.

## Data

`data.csv` - 720 hourly readings (2026-06-01 00:00 to 2026-06-30 23:00).

| column | meaning |
|---|---|
| `timestamp` | hour of the reading |
| `temp_c` | measured zone temperature, degrees Celsius |
| `setpoint_c` | controller set-point for that hour, degrees Celsius |
| `is_fault` | 1 if the hour belongs to a confirmed fault period in the operations log, else 0 |

Define the **score** as $|temp - setpoint|$ divided by $\hat\sigma = 1.4826\times\mathrm{median}|temp - setpoint|$ (robust, so the faults do not inflate it);
the alarm rule is score $\ge T$.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute $\hat\sigma$ and the share of readings labelled as faults.
2. With $T=3$ build the confusion matrix (TP, FP, FN, TN).
3. Compute precision, recall, false-positive rate and F1. Why is precision so much lower than the FPR suggests?
4. The fault readings form consecutive episodes. How many episodes are detected (at least one alarm), and what is the mean detection delay
   (faulty hours before the first alarm)?
5. How many false alarms are there in the month and what is the average spacing between them (ARL0, in hours)?
6. Build a table over thresholds $0, 0.5, 0.75, \dots, 6$ and $99$. Which threshold maximises F1? Which is the largest threshold that still gives recall $\ge 80\%$, and what is the FPR there?
7. Estimate the area under the ROC curve with the trapezoid rule over your table.
8. Add a cost column ($10\times FN + 1\times FP$). Which threshold is cheapest, and by how much does it beat $T=3$?
9. Suppose next month only 0.5 % of readings are faulty but the detector's recall and FPR at $T=3$ stay the same. What is the precision?
10. *Limitations:* give two reasons why these metrics may be too optimistic or misleading for deciding on the production threshold.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Anomaly score over the month", which red dots (false alarms) cluster, and what do they have in common?
- Read the knee of the "ROC curve": what recall do you get at about 1 % FPR?
- In "Alarms by threshold", at which threshold do the false alarms start to drop below the true alarms?

## Deliverable

A short note (5-8 lines) with three named parts: **Threshold** (your choice and why: cost, recall target or false-alarm budget),
**Expected behaviour** (precision, recall, false alarms per month, typical delay) and **Caveats** (prevalence, labels, optimistic tuning).
