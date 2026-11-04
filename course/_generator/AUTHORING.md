# Authoring a lesson

Each lesson is one Python module `lessons/lNN_<snake_title>.py` that defines `SLUG`, `TITLE`, `MODULE` and
`build(out: Path) -> Book`. The reference implementation is **`lessons/l03_percentiles_and_extreme_values.py`** - read it
and `common.py` first; copy its structure.

`python build.py NN` builds lesson NN (writes `data.csv`, `theory.md`, `task.md`, `grafana/dashboard.json`,
`solution.xlsx`) and then **verifies**: the workbook is recalculated in LibreOffice and every cell registered with
`expect=` / `expected=` must equal a value computed independently in numpy/scipy/statsmodels. Any `#DIV/0!`/`#NAME?` fails.

## What a finished lesson folder contains

| file | content |
|---|---|
| `theory.md` | A real mini-chapter (see bar below). |
| `task.md` | Scenario, dataset column table, numbered questions, Grafana questions, deliverable. **No answers.** |
| `data.csv` | The dataset students work with (raw columns only; no derived columns). |
| `solution.xlsx` | `Data` (raw + helper formula columns), `Analysis` (every answer as a live formula, sections, small tables, a chart), `Answers` (one row per task question, numbered like task.md, with interpretation text). |
| `grafana/dashboard.json` | 4-6 panels built with `Dash`; data embedded; works on import. |

## Bar for theory.md (60-130 lines)
- Open with *why this matters / the failure it prevents* (1 short paragraph), then precise definitions.
- Math in `$...$` / `$$...$$` (GitHub-safe: no `\\tag`, no `\\begin{align}` with `&` problems - plain `$$ ... $$` lines).
- At least one **small worked numeric example** whose numbers you have actually computed (verify in Python).
- Assumptions, when the method fails, 3-5 concrete pitfalls, how it connects to the other lessons (relative links
  `../NN-slug/theory.md`; only link lessons that exist in the curriculum list below) and optionally to the repo notes
  (`../../notes/...md`; **verify the file exists** before linking).
- Plain, precise language. No filler, no "in this lesson you will learn". Do not just restate formulas - explain the idea.
- State correct facts only. Where tools differ (e.g. percentile definitions, STDEV.S vs STDEV.P) say which one is used.

## Bar for task.md (40-80 lines)
- `## Scenario` (a concrete story with a decision to make), `## Data` (table of columns + units + n + what a row is),
  `## Questions` (6-10 numbered; the last one is an interpretation/limitation question), `## Grafana` (3 bullets that
  send the student to specific panels and ask what they show), `## Deliverable` (a short written note with named parts).
- Questions must be answerable from `data.csv` with spreadsheet functions. Number them so `Answers` rows match 1:1.
- Hide the "planted" structure: the dataset should contain a discoverable phenomenon (shift, outlier cluster, confounder,
  seasonality...) but task.md must not state it.

## Datasets
- Generate with `np.random.default_rng(<fixed seed>)`; fully deterministic. Put the generator in the lesson module.
- Tailor the dataset to *this* lesson (right size, right structure, realistic column names and units). Do NOT reuse one
  generic table for every lesson. Typical sizes: 100-600 rows. Round values to a sensible precision.
- Realistic story + units: latency (ms), daily sales (units), sensor temperature (C), conversions, etc.
- `data.csv` is written with `write_csv(out, df)`. Dates: use a `date`/`timestamp` column (datetime64).

## Workbook rules (must work in Excel, Google Sheets and LibreOffice)
- **No** RAND/RANDBETWEEN (non-deterministic) - pre-generate random numbers as Data columns if a simulation needs them
  (e.g. bootstrap index columns, uniform draws). **No** dynamic-array/LET/LAMBDA/FILTER/XLOOKUP, **no** array-entered
  formulas (CSE). Single-cell `INDEX(LINEST(...),r,c)`, `SLOPE`, `INTERCEPT`, `RSQ`, `CORREL`, `FORECAST`, `PERCENTILE`,
  `STDEV`/`STDEV.S`, `SUMPRODUCT`, `COUNTIFS`, `AVERAGEIFS`, `OFFSET`, `INDEX/MATCH`, `NORMSINV`, `TINV`, `NORMSDIST` are fine.
- For "by group" statistics use helper columns (`=IF(group="x",value,"")`) so ordinary range functions ignore the rest.
- Every number a student is asked for must be a **formula** in `Analysis` (not pasted) and carry `expect=` (value from
  Python, computed independently - not by re-implementing the same formula string).
- Helper columns on `Data` via `b.add_column(name, fn, expected=series)` (all rows are checked).
- Put adjustable assumptions in yellow cells (`is_input=True`) and make dependent formulas reference them.
- Include at least one chart (`line_chart`, `scatter_chart`, `*_from_table`). `Answers` has one row per task question.
- Interpretation strings in `Answers` are built with f-strings from the Python-computed numbers, so they never go stale.
- Excel limits: avoid >~25k formula cells per sheet; keep resampling loops small (e.g. 200-500 resamples x n<=40).

## Grafana rules
- Use `Dash` from `common.py` (TestData `csv_content`; data embedded; time range auto-fixed to the data). First column of a
  time series frame must be `time`. Show the *solved* analysis (fitted lines, control limits, rolling stats...) - precompute
  those series in pandas. Use `points=[...]`, `dashed=[...]`, `bars=[...]`, `colors={...}` to separate raw/derived/threshold.
- Non-time data (histograms, scatter, bootstrap distributions): `bars` (category strings, **not bare numbers** - bare numbers
  get K/M-formatted) and `xy`.
- 4-6 panels: one `stat` row of key numbers, 2-4 charts, optionally a `table`. Give panels a `description`.
- `python check_grafana.py http://localhost:3055 stats-NN` runs every panel query against a live Grafana (a shared one is
  running with the course folder mounted; new/changed dashboards appear within ~10-20 s) and must print `OK`.
- Look at the result: `PLAYWRIGHT_BROWSERS_PATH=$S/pw $S/venv/bin/python screenshot.py <uid> $S/x.png` then read the PNG.
  Fix anything that looks wrong (empty panel, unreadable axis, everything one colour, wrong units).
- dashboard `uid` = `stats-NN-<short-slug>`; title = `NN · <Title>`.

## Rules for working in parallel
- Only create/modify files for **your own lessons** (`lessons/lNN_*.py` and the generated outputs in your lesson folders).
  Do **not** edit `common.py`, `build.py`, `check_grafana.py`, other lessons, or anything outside `course/`.
  If you need a helper that `common.py` lacks, define it inside your lesson module. Mention such needs in your final report.
- Use the scratchpad venv: `$S/venv/bin/python` (numpy pandas scipy statsmodels openpyxl are installed), with
  `S=/tmp/claude-1000/-home-adam-my-repos/bf183163-6f74-4da0-9104-290abf8d0d9e/scratchpad`. Run from `course/_generator`.
- Do not commit; do not touch git.
- Original (weak) material for each lesson is extracted at `$S/zip/Applied_Statistics_Course/NN-slug/` (lesson.md,
  spreadsheet.xlsx). Use it only for topic/driving-question hints; the new content must be better and the datasets different.

## Curriculum (slug = folder name; link as `../<slug>/theory.md`)
01-distribution-shapes-and-heavy-tails, 02-robust-statistics, 03-percentiles-and-extreme-values, 04-outlier-detection,
05-sampling-bias-and-simpson-s-paradox, 06-time-aggregation-and-sampling-frequency, 07-trend-seasonality-and-noise,
08-moving-averages-and-exponential-smoothing, 09-differencing-and-growth-rates, 10-rolling-statistics,
11-correlation-and-lagged-relationships, 12-linear-and-nonlinear-regression, 13-multiple-regression-and-confounding,
14-spurious-correlation-and-autocorrelation, 15-residual-analysis-and-model-diagnostics,
16-sampling-distributions-and-the-clt, 17-bootstrapping-and-confidence-intervals, 18-permutation-tests,
19-a-b-testing-and-effect-sizes, 20-monte-carlo-simulation, 21-naive-and-seasonal-naive-forecasts,
22-trend-and-seasonal-regression-forecasting, 23-exponential-smoothing-models, 24-backtesting-and-forecast-accuracy,
25-prediction-intervals-and-forecast-uncertainty, 26-statistical-process-control, 27-change-point-detection,
28-time-series-anomaly-detection, 29-false-alarms-and-detection-performance, 30-capstone-statistical-monitoring-dashboard

Modules: 1-5 Understanding data beyond averages; 6-10 Understanding time series; 11-15 Relationships and statistical
models; 16-20 Uncertainty and statistical inference; 21-25 Forecasting and model evaluation; 26-30 Statistical monitoring
and decision-making. Lessons build on each other (e.g. 27/28/29 reuse the monitoring story of 26; 30 is a capstone that
combines distribution, trend, anomaly and decision-making).
