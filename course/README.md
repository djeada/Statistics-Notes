# Applied Statistics Course - 30 lessons with data, theory, tasks, solved workbooks and Grafana

Thirty hands-on lessons (plus a five-lesson spreadsheet primer) that move from "what does this data actually look like?" to "can I defend a monitoring
decision?". Every lesson is a folder with the same five files:

| file | what it is |
|---|---|
| `theory.md` | the concept: definitions, a worked numeric example, assumptions, pitfalls |
| `task.md` | a scenario with a decision to make, numbered questions and a deliverable (no answers) |
| `data.csv` | the dataset for this lesson (synthetic, deterministic, with a planted phenomenon to discover) |
| `solution.xlsx` | the solved workbook: `Data`, `Analysis` (live formulas + a chart) and `Answers` (one row per task question) |
| `grafana/dashboard.json` | a dashboard that renders the lesson's data and solved analysis, self-contained |

## How to work through a lesson

1. Read `theory.md`.
2. Open `task.md`, import `data.csv` into a spreadsheet (Excel, Google Sheets or LibreOffice) and answer the questions
   with your own formulas.
3. Compare with `solution.xlsx`: the `Answers` sheet gives the number and the interpretation for each question; `Analysis`
   shows the formula behind it. Yellow cells are assumptions you can change.
4. Start Grafana (`cd grafana && docker compose up`, see [grafana/README.md](grafana/README.md)), open the lesson's
   dashboard and answer its Grafana questions.
5. Write the short deliverable from `task.md`.

## Lessons

| # | Lesson | Theory | Task | Data | Solution | Grafana | Dataset |
|---:|---|---|---|---|---|---|---|
| | **Understanding data beyond averages** | | | | | | |
| 01 | Distribution shapes and heavy tails | [theory](01-distribution-shapes-and-heavy-tails/theory.md) | [task](01-distribution-shapes-and-heavy-tails/task.md) | [csv](01-distribution-shapes-and-heavy-tails/data.csv) | [xlsx](01-distribution-shapes-and-heavy-tails/solution.xlsx) | [json](01-distribution-shapes-and-heavy-tails/grafana/dashboard.json) | 500 online-shop orders (basket value in EUR, delivery time in hours, channel) |
| 02 | Robust statistics | [theory](02-robust-statistics/theory.md) | [task](02-robust-statistics/task.md) | [csv](02-robust-statistics/data.csv) | [xlsx](02-robust-statistics/solution.xlsx) | [json](02-robust-statistics/grafana/dashboard.json) | 288 temperature readings (10 min apart) from two sensors in a cold room; sensor A has driver error codes |
| 03 | Percentiles and extreme values | [theory](03-percentiles-and-extreme-values/theory.md) | [task](03-percentiles-and-extreme-values/task.md) | [csv](03-percentiles-and-extreme-values/data.csv) | [xlsx](03-percentiles-and-extreme-values/solution.xlsx) | [json](03-percentiles-and-extreme-values/grafana/dashboard.json) | 600 API requests, 5 s apart (latency in ms, endpoint, HTTP status) |
| 04 | Outlier detection | [theory](04-outlier-detection/theory.md) | [task](04-outlier-detection/task.md) | [csv](04-outlier-detection/data.csv) | [xlsx](04-outlier-detection/solution.xlsx) | [json](04-outlier-detection/grafana/dashboard.json) | 300 purchase-order lines (category, quantity, unit price, amount) with decimal slips and genuine bulk orders |
| 05 | Sampling bias and Simpson's paradox | [theory](05-sampling-bias-and-simpson-s-paradox/theory.md) | [task](05-sampling-bias-and-simpson-s-paradox/task.md) | [csv](05-sampling-bias-and-simpson-s-paradox/data.csv) | [xlsx](05-sampling-bias-and-simpson-s-paradox/solution.xlsx) | [json](05-sampling-bias-and-simpson-s-paradox/grafana/dashboard.json) | 2,800 checkout sessions of a non-randomised A/B test (device, variant, converted, exit-survey score) |
| | **Understanding time series** | | | | | | |
| 06 | Time aggregation and sampling frequency | [theory](06-time-aggregation-and-sampling-frequency/theory.md) | [task](06-time-aggregation-and-sampling-frequency/task.md) | [csv](06-time-aggregation-and-sampling-frequency/data.csv) | [xlsx](06-time-aggregation-and-sampling-frequency/solution.xlsx) | [json](06-time-aggregation-and-sampling-frequency/grafana/dashboard.json) | 14 days of 15-minute web-service metrics (requests, errors, mean latency, CPU gauge) |
| 07 | Trend, seasonality and noise | [theory](07-trend-seasonality-and-noise/theory.md) | [task](07-trend-seasonality-and-noise/task.md) | [csv](07-trend-seasonality-and-noise/data.csv) | [xlsx](07-trend-seasonality-and-noise/solution.xlsx) | [json](07-trend-seasonality-and-noise/grafana/dashboard.json) | 147 days (21 full weeks) of daily orders of an online shop |
| 08 | Moving averages and exponential smoothing | [theory](08-moving-averages-and-exponential-smoothing/theory.md) | [task](08-moving-averages-and-exponential-smoothing/task.md) | [csv](08-moving-averages-and-exponential-smoothing/data.csv) | [xlsx](08-moving-averages-and-exponential-smoothing/solution.xlsx) | [json](08-moving-averages-and-exponential-smoothing/grafana/dashboard.json) | 140 days of support tickets with a level shift after a product release |
| 09 | Differencing and growth rates | [theory](09-differencing-and-growth-rates/theory.md) | [task](09-differencing-and-growth-rates/task.md) | [csv](09-differencing-and-growth-rates/data.csv) | [xlsx](09-differencing-and-growth-rates/solution.xlsx) | [json](09-differencing-and-growth-rates/grafana/dashboard.json) | 72 months of subscription revenue (USD), compounding growth with a yearly pattern and one outage month |
| 10 | Rolling statistics | [theory](10-rolling-statistics/theory.md) | [task](10-rolling-statistics/task.md) | [csv](10-rolling-statistics/data.csv) | [xlsx](10-rolling-statistics/solution.xlsx) | [json](10-rolling-statistics/grafana/dashboard.json) | 180 days of average payment-processing time (ms) with a volatile period and three spike days |
| | **Relationships and statistical models** | | | | | | |
| 11 | Correlation and lagged relationships | [theory](11-correlation-and-lagged-relationships/theory.md) | [task](11-correlation-and-lagged-relationships/task.md) | [csv](11-correlation-and-lagged-relationships/data.csv) | [xlsx](11-correlation-and-lagged-relationships/solution.xlsx) | [json](11-correlation-and-lagged-relationships/grafana/dashboard.json) | 150 days of ad spend, new sign-ups (reacting to spend 3 days earlier) and newsletter opens (sharing only the weekday pattern) |
| 12 | Linear and nonlinear regression | [theory](12-linear-and-nonlinear-regression/theory.md) | [task](12-linear-and-nonlinear-regression/task.md) | [csv](12-linear-and-nonlinear-regression/data.csv) | [xlsx](12-linear-and-nonlinear-regression/solution.xlsx) | [json](12-linear-and-nonlinear-regression/grafana/dashboard.json) | 120 weekly observations of advertising spend (k$) and sales (units); spend grows over time |
| 13 | Multiple regression and confounding | [theory](13-multiple-regression-and-confounding/theory.md) | [task](13-multiple-regression-and-confounding/task.md) | [csv](13-multiple-regression-and-confounding/data.csv) | [xlsx](13-multiple-regression-and-confounding/solution.xlsx) | [json](13-multiple-regression-and-confounding/grafana/dashboard.json) | 156 weeks of sales with ad spend, price, promo and holiday flags and an irrelevant temperature column |
| 14 | Spurious correlation and autocorrelation | [theory](14-spurious-correlation-and-autocorrelation/theory.md) | [task](14-spurious-correlation-and-autocorrelation/task.md) | [csv](14-spurious-correlation-and-autocorrelation/data.csv) | [xlsx](14-spurious-correlation-and-autocorrelation/solution.xlsx) | [json](14-spurious-correlation-and-autocorrelation/grafana/dashboard.json) | 250 days of three indicators: two independent random walks and one series genuinely tied to the first |
| 15 | Residual analysis and model diagnostics | [theory](15-residual-analysis-and-model-diagnostics/theory.md) | [task](15-residual-analysis-and-model-diagnostics/task.md) | [csv](15-residual-analysis-and-model-diagnostics/data.csv) | [xlsx](15-residual-analysis-and-model-diagnostics/solution.xlsx) | [json](15-residual-analysis-and-model-diagnostics/grafana/dashboard.json) | 120 courier deliveries: distance (km) and delivery time (min); R-squared 0.89 but the model fails four diagnostics |
| | **Uncertainty and statistical inference** | | | | | | |
| 16 | Sampling distributions and the CLT | [theory](16-sampling-distributions-and-the-clt/theory.md) | [task](16-sampling-distributions-and-the-clt/task.md) | [csv](16-sampling-distributions-and-the-clt/data.csv) | [xlsx](16-sampling-distributions-and-the-clt/solution.xlsx) | [json](16-sampling-distributions-and-the-clt/grafana/dashboard.json) | 1,000 order values (a skewed population) and 250 repeated samples of 50 orders drawn from it |
| 17 | Bootstrapping and confidence intervals | [theory](17-bootstrapping-and-confidence-intervals/theory.md) | [task](17-bootstrapping-and-confidence-intervals/task.md) | [csv](17-bootstrapping-and-confidence-intervals/data.csv) | [xlsx](17-bootstrapping-and-confidence-intervals/solution.xlsx) | [json](17-bootstrapping-and-confidence-intervals/grafana/dashboard.json) | 30 support tickets (resolution hours) + 400 pre-generated bootstrap resamples |
| 18 | Permutation tests | [theory](18-permutation-tests/theory.md) | [task](18-permutation-tests/task.md) | [csv](18-permutation-tests/data.csv) | [xlsx](18-permutation-tests/solution.xlsx) | [json](18-permutation-tests/grafana/dashboard.json) | 10 usability-test participants (5 old flow, 5 new flow), time to finish onboarding in minutes |
| 19 | A/B testing and effect sizes | [theory](19-a-b-testing-and-effect-sizes/theory.md) | [task](19-a-b-testing-and-effect-sizes/task.md) | [csv](19-a-b-testing-and-effect-sizes/data.csv) | [xlsx](19-a-b-testing-and-effect-sizes/solution.xlsx) | [json](19-a-b-testing-and-effect-sizes/grafana/dashboard.json) | 28-day checkout A/B test: visitors and conversions per day x variant x device (112 rows) |
| 20 | Monte Carlo simulation | [theory](20-monte-carlo-simulation/theory.md) | [task](20-monte-carlo-simulation/task.md) | [csv](20-monte-carlo-simulation/data.csv) | [xlsx](20-monte-carlo-simulation/solution.xlsx) | [json](20-monte-carlo-simulation/grafana/dashboard.json) | 2000 pre-generated uniform random triples (demand, price, unit cost) for a product-launch profit model |
| | **Forecasting and model evaluation** | | | | | | |
| 21 | Naive and seasonal naive forecasts | [theory](21-naive-and-seasonal-naive-forecasts/theory.md) | [task](21-naive-and-seasonal-naive-forecasts/task.md) | [csv](21-naive-and-seasonal-naive-forecasts/data.csv) | [xlsx](21-naive-and-seasonal-naive-forecasts/solution.xlsx) | [json](21-naive-and-seasonal-naive-forecasts/grafana/dashboard.json) | 140 days of bakery sales (loaves per day): 112 days of history + 28-day holdout |
| 22 | Trend and seasonal regression forecasting | [theory](22-trend-and-seasonal-regression-forecasting/theory.md) | [task](22-trend-and-seasonal-regression-forecasting/task.md) | [csv](22-trend-and-seasonal-regression-forecasting/data.csv) | [xlsx](22-trend-and-seasonal-regression-forecasting/solution.xlsx) | [json](22-trend-and-seasonal-regression-forecasting/grafana/dashboard.json) | 420 days of shop orders (2025-01-01 .. 2026-02-24), 392 training days + 28 holdout days |
| 23 | Exponential smoothing models | [theory](23-exponential-smoothing-models/theory.md) | [task](23-exponential-smoothing-models/task.md) | [csv](23-exponential-smoothing-models/data.csv) | [xlsx](23-exponential-smoothing-models/solution.xlsx) | [json](23-exponential-smoothing-models/grafana/dashboard.json) | 168 days of shop orders (2025-03-03 .. 2025-08-17), 140 training days + 28 holdout days |
| 24 | Backtesting and forecast accuracy | [theory](24-backtesting-and-forecast-accuracy/theory.md) | [task](24-backtesting-and-forecast-accuracy/task.md) | [csv](24-backtesting-and-forecast-accuracy/data.csv) | [xlsx](24-backtesting-and-forecast-accuracy/solution.xlsx) | [json](24-backtesting-and-forecast-accuracy/grafana/dashboard.json) | 336 days of shop orders (2025-01-06 .. 2025-12-07), 36 weekly forecast origins x 7-day horizon |
| 25 | Prediction intervals and forecast uncertainty | [theory](25-prediction-intervals-and-forecast-uncertainty/theory.md) | [task](25-prediction-intervals-and-forecast-uncertainty/task.md) | [csv](25-prediction-intervals-and-forecast-uncertainty/data.csv) | [xlsx](25-prediction-intervals-and-forecast-uncertainty/solution.xlsx) | [json](25-prediction-intervals-and-forecast-uncertainty/grafana/dashboard.json) | 350 days of shop orders (2025-01-06 .. 2025-12-20); calibration on the first 224 days, coverage check on the last 126 |
| | **Statistical monitoring and decision-making** | | | | | | |
| 26 | Statistical process control | [theory](26-statistical-process-control/theory.md) | [task](26-statistical-process-control/task.md) | [csv](26-statistical-process-control/data.csv) | [xlsx](26-statistical-process-control/solution.xlsx) | [json](26-statistical-process-control/grafana/dashboard.json) | 400 incubator-chamber temperature readings, 5 minutes apart (target 37.0 C) |
| 27 | Change-point detection | [theory](27-change-point-detection/theory.md) | [task](27-change-point-detection/task.md) | [csv](27-change-point-detection/data.csv) | [xlsx](27-change-point-detection/solution.xlsx) | [json](27-change-point-detection/grafana/dashboard.json) | 240 hourly reactor-jacket temperature readings (C) with a small mean shift hidden in the noise |
| 28 | Time-series anomaly detection | [theory](28-time-series-anomaly-detection/theory.md) | [task](28-time-series-anomaly-detection/task.md) | [csv](28-time-series-anomaly-detection/data.csv) | [xlsx](28-time-series-anomaly-detection/solution.xlsx) | [json](28-time-series-anomaly-detection/grafana/dashboard.json) | 154 daily mean compressor-housing temperatures (C), strong weekday cycle, injected spikes and a level shift |
| 29 | False alarms and detection performance | [theory](29-false-alarms-and-detection-performance/theory.md) | [task](29-false-alarms-and-detection-performance/task.md) | [csv](29-false-alarms-and-detection-performance/data.csv) | [xlsx](29-false-alarms-and-detection-performance/solution.xlsx) | [json](29-false-alarms-and-detection-performance/grafana/dashboard.json) | 720 hourly furnace-zone temperature readings vs controller set-point, 8 labelled fault episodes |
| 30 | Capstone: statistical monitoring dashboard | [theory](30-capstone-statistical-monitoring-dashboard/theory.md) | [task](30-capstone-statistical-monitoring-dashboard/task.md) | [csv](30-capstone-statistical-monitoring-dashboard/data.csv) | [xlsx](30-capstone-statistical-monitoring-dashboard/solution.xlsx) | [json](30-capstone-statistical-monitoring-dashboard/grafana/dashboard.json) | 90 days of an online checkout service: daily requests, p95 latency (ms), errors, deploy and post-mortem labels |

## Spreadsheet fundamentals (5 lessons, no Grafana)

If formulas, lookups and pivot tables are not yet second nature, start here. Same layout as above (`theory.md`, `task.md`,
`data.csv`, `solution.xlsx`), without the Grafana dashboard. Reference tables for lookups come as extra CSV files in the lesson folder.

| # | Lesson | Theory | Task | Data | Solution | Dataset |
|---:|---|---|---|---|---|---|
| S1 | Basics: cell references, sorting, filtering, formatting | [theory](spreadsheet-fundamentals/01-basics-references-sorting-filtering/theory.md) | [task](spreadsheet-fundamentals/01-basics-references-sorting-filtering/task.md) | [csv](spreadsheet-fundamentals/01-basics-references-sorting-filtering/data.csv) | [xlsx](spreadsheet-fundamentals/01-basics-references-sorting-filtering/solution.xlsx) | 48 stationery-shop orders |
| S2 | Essential formulas: SUM, AVERAGE, IF, COUNTIF, SUMIF | [theory](spreadsheet-fundamentals/02-essential-formulas/theory.md) | [task](spreadsheet-fundamentals/02-essential-formulas/task.md) | [csv](spreadsheet-fundamentals/02-essential-formulas/data.csv) | [xlsx](spreadsheet-fundamentals/02-essential-formulas/solution.xlsx) | 150 team expense lines with blanks and refunds |
| S3 | Lookup functions: VLOOKUP, XLOOKUP, INDEX + MATCH | [theory](spreadsheet-fundamentals/03-lookup-functions/theory.md) | [task](spreadsheet-fundamentals/03-lookup-functions/task.md) | [csv](spreadsheet-fundamentals/03-lookup-functions/data.csv) | [xlsx](spreadsheet-fundamentals/03-lookup-functions/solution.xlsx) | 120 orders + product, customer, discount and shipping tables |
| S4 | Data analysis: pivot tables, charts, conditional formatting | [theory](spreadsheet-fundamentals/04-data-analysis/theory.md) | [task](spreadsheet-fundamentals/04-data-analysis/task.md) | [csv](spreadsheet-fundamentals/04-data-analysis/data.csv) | [xlsx](spreadsheet-fundamentals/04-data-analysis/solution.xlsx) | 400 sales transactions, Jan-Jun 2026 |
| S5 | Advanced skills: dashboards, QUERY, FILTER, data cleaning | [theory](spreadsheet-fundamentals/05-advanced-skills/theory.md) | [task](spreadsheet-fundamentals/05-advanced-skills/task.md) | [csv](spreadsheet-fundamentals/05-advanced-skills/data.csv) | [xlsx](spreadsheet-fundamentals/05-advanced-skills/solution.xlsx) | 160-row messy CRM export (spaces, case, text numbers, duplicates) |

Two limits worth knowing: the workbooks cannot contain real **pivot tables** (they are built in the application, so the solution
holds the equivalent `SUMIFS` tables you check your pivot against) and `XLOOKUP`, `FILTER`, `QUERY` are shown as text next to the
result they must produce, because the verification tool (LibreOffice 24.2) cannot evaluate them. Everything else is a live, verified formula.

## Everything is reproducible and checked

The datasets, workbooks, dashboards and markdown are generated by [`_generator/`](_generator/AUTHORING.md):

```bash
pip install -r _generator/requirements.txt          # plus LibreOffice (soffice) for verification
python _generator/build.py            # all lessons;  python _generator/build.py 3 17 s2  for selected ones (sN = spreadsheet track)
python _generator/make_readme.py      # refresh this index
```

`build.py` recalculates every workbook in LibreOffice and compares each formula result with an independent
numpy/scipy/statsmodels computation, so a workbook with a wrong formula fails the build. `check_grafana.py` runs every
dashboard query against a live Grafana and fails on empty panels.

All data are synthetic teaching data; none of it comes from real systems or people.
