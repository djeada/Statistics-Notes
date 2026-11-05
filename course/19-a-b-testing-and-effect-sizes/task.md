# Task: did the new checkout page win?

## Scenario

An online shop ran a 4-week experiment (Mon 6 Apr - Sun 3 May 2026) of a redesigned checkout page (**B**) against the current
one (**A**). Visitors were split at random. Product wants to ship B site-wide if it lifts conversion by **at least 0.3 percentage points**;
shipping costs engineering time, so a wrong "yes" is expensive. An enthusiastic colleague who checked the dashboard every morning says
"B was significantly better after the second week - we should have shipped then". Evaluate the experiment properly.

## Data

`data.csv` - 112 rows: one per day x variant x device.

| column | meaning |
|---|---|
| `date` | day of the experiment |
| `variant` | `A` (control) or `B` (new checkout) |
| `device` | `mobile` or `desktop` |
| `visitors` | visitors assigned to that variant on that day and device |
| `conversions` | of those, how many completed a purchase |

## Questions

1. Compute visitors, conversions and conversion rate for A and B over all 28 days.
2. Compute the absolute difference (percentage points) and the relative lift.
3. Run the two-proportion z-test (pooled standard error): z and two-sided p-value. Is it significant at 5 %?
4. Compute the 95 % confidence interval for the difference (unpooled standard error). What does it tell you that the p-value does not?
5. Compute Cohen's h. What does the convention call this effect, and is the label useful here?
6. Is the lift practically important (threshold +0.3 pp)? Compare the point estimate *and* the interval with the threshold.
7. What is the minimum detectable effect of this test (80 % power)? How many visitors per arm, and how many days, would be needed to detect +0.3 pp?
8. Re-run the z-test on cumulative data for each day. On which day would a daily peeker first have called a winner, and how many days is |z| above 1.96?
9. Split the analysis by device. Where is the difference?
10. *Interpretation:* give a recommendation in three sentences, including why stopping at the first significant day is invalid and one limitation of the device split.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Peeking: cumulative z by day", when does the line cross the dashed critical values, and what happens afterwards?
- In "Conversion rate by device", for which device do the bars differ?
- In "Days of traffic needed vs lift to detect", where does the "days we ran" line cross the curve, and what lift does that correspond to?

## Deliverable

A decision memo (6-10 lines) with named parts: **Result** (rates, lift, p-value, CI), **Practical importance** (against the 0.3 pp threshold),
**Process** (why the peeking colleague is wrong), **Decision** and **Next step**. Include the cumulative-z chart.
