# Task: robust statistics

## Scenario

A cold room storing vaccines has two independent digital thermometers, **A** and **B**, logging every 10 minutes for two days. Quality
assurance wants one number for the room's temperature and one for its variability, to set alarm limits. The first report from sensor A
says the temperature is "about 23 C with a standard deviation of 14 C" - nobody believes this, since the compressor holds the room near
21-22 C. You must decide which statistics to trust and how much the answer depends on a few readings.

## Data

`data.csv` - 288 rows (12 Jan 2026 00:00 to 13 Jan 2026 23:50), one row per 10-minute reading.

| column | meaning |
|---|---|
| `timestamp` | time of the reading |
| `temp_a_c` | sensor A, degrees Celsius |
| `temp_b_c` | sensor B, degrees Celsius (same room) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`. `STDEV` is the sample SD; `TRIMMEAN(range, 0.1)` removes 10 % in total.

1. Compute mean and SD of both sensors. Do they agree?
2. Compute the median, the 10 % trimmed mean and the 5 % winsorised mean (clip to P5/P95, then average) of both sensors.
3. Compute IQR, IQR/1.349, MAD and 1.4826 x MAD of both sensors and compare with the SD.
4. How many readings of A are further than 10 robust SDs (1.4826 x MAD) from the median? What values do they have? What is the mean of A without them, and how far is it from B's mean?
5. Add *one* extra reading X to sensor B for X = 22, 30, 85, 500, 5000. How do the mean and the median change?
6. Overwrite the first k readings of B with 85.0 for k = 14, 29, 58, 100, 150. For each k compute mean, trimmed mean, winsorised mean and median. At what share of corrupted data does each estimator break?
7. Compute 3-sigma alarm limits for sensor A (a) as mean $\pm$ 3 SD and (b) as median $\pm$ 3 x 1.4826 MAD. Which pair would flag a reading of 35 C?
8. *Explain in three sentences* when a robust estimate would be the wrong choice and one weakness of robust estimators on clean data.

## Grafana

Import `grafana/dashboard.json` (no data-source setup is needed).

- In "Raw readings, sensor A vs sensor B", where do the mean and median of A sit relative to the bulk of the data?
- In "Three estimates of the spread", which estimates of A and B agree and which do not?
- In "Breakdown curves", read off the share of corrupted readings at which each line leaves the horizontal.

## Deliverable

A short note (6-10 lines) titled *Which numbers go on the QA report?* with three named parts: **What was wrong** (the evidence in
sensor A), **Recommended estimates** (centre and spread, with values) and **Limits** (when these estimates stop being reliable).
Include one chart.
