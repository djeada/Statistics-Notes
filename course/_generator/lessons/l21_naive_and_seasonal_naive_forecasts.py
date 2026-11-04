"""Lesson 21 - Naive and seasonal naive forecasts (benchmarks, holdout, MAE/RMSE/MAPE/MASE)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "21-naive-and-seasonal-naive-forecasts"
TITLE = "Naive and seasonal naive forecasts"
MODULE = "Forecasting and model evaluation"
DATASET = "140 days of bakery sales (loaves per day): 112 days of history + 28-day holdout"
T, H = 112, 28  # training days, holdout days
M = 7  # season length (week)
R_T = T + 1  # Excel row of the last training day
R_1, R_N = T + 2, T + H + 1  # first / last holdout rows


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(2101)
    n = T + H
    t = np.arange(1, n + 1)
    dates = pd.date_range("2026-01-05", periods=n, freq="D")  # a Monday
    mult = np.array([0.80, 0.85, 0.90, 1.00, 1.25, 1.60, 1.30])  # Mon..Sun
    y = (120 + 0.35 * t) * mult[dates.day_of_week] * rng.normal(1, 0.05, n)
    y[107] *= 0.35  # a public holiday on the Wednesday of the last training week (day 108)
    return pd.DataFrame({"date": dates, "loaves_sold": np.round(y).astype(int)})


def metrics(a, f, scale):
    e = a - f
    mae = float(np.abs(e).mean())
    return mae, float(np.sqrt((e ** 2).mean())), float((np.abs(e) / a).mean()), mae / scale, float(e.mean())


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    y = df["loaves_sold"].to_numpy(float)
    tr, te = y[:T], y[T:]
    h = np.arange(1, H + 1)
    dow = df["date"].dt.day_of_week.to_numpy() + 1  # 1 = Monday
    fc = {"mean": np.full(H, tr.mean()), "naive": np.full(H, tr[-1]),
          "snaive": y[T + h - 1 - M * np.ceil(h / M).astype(int)],
          "drift": tr[-1] + h * (tr[-1] - tr[0]) / (T - 1),
          "naive1": y[T - 1:-1], "snaive1": y[T - M:-M]}
    scale = float(np.abs(tr[M:] - tr[:-M]).mean())  # in-sample one-season-ahead seasonal naive error
    pad = lambda v: np.r_[np.full(T, np.nan), v]

    b = Book(df, "Lesson 21 - Naive and seasonal naive forecasts",
             f"Training = first {T} days, holdout = last {H} days. Benchmarks are computed only for the holdout rows.")
    A = f"Data!$B${R_1}:$B${R_N}"
    b.add_column("weekday", lambda r: f"=WEEKDAY(A{r},2)", expected=dow, fmt="0")
    srcs = {}
    srcs["fc_mean"] = b.add_column("fc_mean", lambda r: f"=AVERAGE(Data!$B$2:$B${R_T})", expected=pad(fc["mean"]), fmt="0.0", first_row=R_1)
    srcs["fc_naive"] = b.add_column("fc_naive", lambda r: f"=Data!$B${R_T}", expected=pad(fc["naive"]), fmt="0.0", first_row=R_1)
    srcs["fc_snaive"] = b.add_column("fc_snaive", lambda r: f"=INDEX(Data!$B$1:$B${R_N},{r}-{M}*ROUNDUP(({r}-{R_T})/{M},0))",
                                     expected=pad(fc["snaive"]), fmt="0.0", first_row=R_1)
    srcs["fc_drift"] = b.add_column("fc_drift", lambda r: f"=Data!$B${R_T}+({r}-{R_T})*(Data!$B${R_T}-Data!$B$2)/{T - 1}",
                                    expected=pad(fc["drift"]), fmt="0.0", first_row=R_1)
    srcs["fc_naive_1step"] = b.add_column("fc_naive_1step", lambda r: f"=Data!B{r - 1}", expected=pad(fc["naive1"]), fmt="0.0", first_row=R_1)
    srcs["fc_snaive_1step"] = b.add_column("fc_snaive_1step", lambda r: f"=Data!B{r - M}", expected=pad(fc["snaive1"]), fmt="0.0", first_row=R_1)
    b.add_column("abs_err_snaive", lambda r: f"=ABS(B{r}-{srcs['fc_snaive']}{r})", expected=pad(np.abs(te - fc["snaive"])), fmt="0.0",
                 first_row=R_1)
    ERR = f"Data!${b.col('abs_err_snaive')}${R_1}:${b.col('abs_err_snaive')}${R_N}"
    WD = f"Data!${b.col('weekday')}$2:${b.col('weekday')}${R_N}"
    WDH = f"Data!${b.col('weekday')}${R_1}:${b.col('weekday')}${R_N}"

    b.section("1. Training history and holdout")
    b.row("Training days", f"=COUNT(Data!$B$2:$B${R_T})", T, "0")
    b.row("Holdout days", f"=COUNT({A})", H, "0")
    r_trm = b.row("Mean daily sales, training", f"=AVERAGE(Data!$B$2:$B${R_T})", float(tr.mean()), "0.0")
    r_tem = b.row("Mean daily sales, holdout", f"=AVERAGE({A})", float(te.mean()), "0.0")
    b.row("Growth: holdout mean / training mean - 1", f"={b.local(r_tem)}/{b.local(r_trm)}-1", float(te.mean() / tr.mean() - 1), "0.0%")
    r_scale = b.row("In-sample scale for MASE: mean |y(t) - y(t-7)|, training",
                    f"=SUMPRODUCT(ABS(Data!$B$9:$B${R_T}-Data!$B$2:$B${R_T - M}))/COUNT(Data!$B$9:$B${R_T})", scale, "0.00",
                    "The error a one-week-ago forecast would have made in the past")

    b.section("2. Weekday profile and where the seasonal naive forecast fails")
    names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    rows, exp = [], {}
    t0 = b.next_row + 1
    for k in range(7):
        rr = t0 + k
        rows.append([k + 1, names[k], f'=AVERAGEIFS(Data!$B$2:$B${R_N},{WD},A{rr},Data!$A$2:$A${R_N},"<="&Data!$A${R_T})',
                     f'=AVERAGEIFS(Data!$B$2:$B${R_N},{WD},A{rr},Data!$A$2:$A${R_N},">"&Data!$A${R_T})', f"=AVERAGEIFS({ERR},{WDH},A{rr})"])
        exp.update({(k, 2): tr[dow[:T] == k + 1].mean(), (k, 3): te[dow[T:] == k + 1].mean(),
                    (k, 4): np.abs(te - fc["snaive"])[dow[T:] == k + 1].mean()})
    w0, w1 = b.table(["Weekday #", "Day", "Mean sales, training", "Mean sales, holdout", "Seasonal naive MAE (holdout)"], rows,
                     fmt={2: "0.0", 3: "0.0", 4: "0.0"}, expect=exp)
    r_worst = b.row("Weekday with the largest seasonal naive error (1 = Mon)", f"=INDEX($A${w0}:$A${w1},MATCH(MAX($E${w0}:$E${w1}),$E${w0}:$E${w1},0))",
                    float(np.argmax([np.abs(te - fc["snaive"])[dow[T:] == k + 1].mean() for k in range(7)]) + 1), "0")
    mask = dow[T:] != 3
    r_exw = b.row("Seasonal naive MAE excluding that weekday",
                  f"=SUMPRODUCT(({WDH}<>{b.local(r_worst)})*Data!${b.col('abs_err_snaive')}${R_1}:${b.col('abs_err_snaive')}${R_N})/SUMPRODUCT(--({WDH}<>{b.local(r_worst)}))",
                  float(np.abs(te - fc['snaive'])[mask].mean()), "0.00")

    b.section("3. Accuracy on the 28-day holdout")
    methods = [("Mean (training average)", "mean", "fc_mean"), ("Naive (last value, 28 days flat)", "naive", "fc_naive"),
               ("Seasonal naive (same weekday, last week)", "snaive", "fc_snaive"), ("Drift (line from first to last)", "drift", "fc_drift"),
               ("Naive, 1 step ahead (yesterday)", "naive1", "fc_naive_1step"), ("Seasonal naive, 1 step ahead (7 days ago)", "snaive1", "fc_snaive_1step")]
    rows, exp = [], {}
    t0 = b.next_row + 1
    for i, (lab, k, col) in enumerate(methods):
        F = f"Data!${b.col(col)}${R_1}:${b.col(col)}${R_N}"
        rr = t0 + i
        rows.append([lab, f"=SUMPRODUCT(ABS({A}-{F}))/COUNT({A})", f"=SQRT(SUMXMY2({A},{F})/COUNT({A}))",
                     f"=SUMPRODUCT(ABS({A}-{F})/{A})/COUNT({A})", f"=B{rr}/{b.local(r_scale)}", f"=AVERAGE({A})-AVERAGE({F})"])
        m = metrics(te, fc[k], scale)
        exp.update({(i, 1): m[0], (i, 2): m[1], (i, 3): m[2], (i, 4): m[3], (i, 5): m[4]})
    a0, a1 = b.table(["Method", "MAE", "RMSE", "MAPE", "MASE", "Mean error (actual - forecast)"], rows,
                     fmt={1: "0.0", 2: "0.0", 3: "0.0%", 4: "0.00", 5: "0.0"}, expect=exp)
    b.bar_chart_from_table("MAE and RMSE by method (holdout)", 1, [2, 3], a0, a1, anchor="H4", y_title="loaves")
    b.line_chart("Sales and benchmark forecasts", "date", ["loaves_sold", "fc_snaive", "fc_naive", "fc_mean"], anchor="H24", y_title="loaves")
    mt = {k: metrics(te, fc[k], scale) for k in fc}
    r_skill = b.row("Skill of seasonal naive vs naive: 1 - MAE_snaive / MAE_naive", f"=1-B{a0 + 2}/B{a0 + 1}", 1 - mt["snaive"][0] / mt["naive"][0], "0.0%")
    r_skill2 = b.row("Skill of seasonal naive vs mean forecast", f"=1-B{a0 + 2}/B{a0}", 1 - mt["snaive"][0] / mt["mean"][0], "0.0%")
    r_skill3 = b.row("Skill of 1-step seasonal naive vs 1-step naive", f"=1-B{a0 + 5}/B{a0 + 4}", 1 - mt["snaive1"][0] / mt["naive1"][0], "0.0%")

    sn, nv, mn, dr, nv1, sn1 = (mt[k] for k in ("snaive", "naive", "mean", "drift", "naive1", "snaive1"))
    b.answers([
        ("Mean daily sales in training and holdout, and the weekday profile", f"={r_tem}",
         f"Training mean {tr.mean():.1f} loaves, holdout mean {te.mean():.1f} ({te.mean() / tr.mean() - 1:+.0%}): the level is rising. "
         f"Saturday is the peak ({tr[dow[:T] == 6].mean():.0f}) and Monday the low ({tr[dow[:T] == 1].mean():.0f}) in training."),
        ("Mean forecast: MAE, RMSE, MAPE", f"=Analysis!B{a0}",
         f"MAE {mn[0]:.1f}, RMSE {mn[1]:.1f}, MAPE {mn[2]:.1%}. It ignores both the weekly pattern and the growth (mean error {mn[4]:+.0f})."),
        ("Naive forecast: MAE, RMSE, MAPE", f"=Analysis!B{a0 + 1}",
         f"MAE {nv[0]:.1f}, RMSE {nv[1]:.1f}, MAPE {nv[2]:.1%}. The last training day is a Sunday (a high day), so all 28 forecasts are too high "
         f"(mean error {nv[4]:+.0f})."),
        ("Seasonal naive forecast: MAE, RMSE, MAPE", f"=Analysis!B{a0 + 2}",
         f"MAE {sn[0]:.1f}, RMSE {sn[1]:.1f}, MAPE {sn[2]:.1%}: the best of the four multi-step benchmarks. It captures the weekly pattern but not the growth "
         f"(mean error {sn[4]:+.0f}). Drift is worst (MAE {dr[0]:.1f}): it extrapolates a straight line through a seasonal series."),
        ("Skill of seasonal naive versus naive and mean", f"={r_skill}",
         f"Seasonal naive cuts the MAE by {1 - sn[0] / nv[0]:.0%} against naive and {1 - sn[0] / mn[0]:.0%} against the mean forecast. "
         f"Any model you build must beat {sn[0]:.1f} MAE, else it adds complexity for nothing."),
        ("MASE of each method", f"=Analysis!E{a0 + 2}",
         f"MASE of seasonal naive = {sn[3]:.2f}: its 28-day-ahead error is {sn[3]:.1f}x the typical one-week-ahead error in the history ({scale:.1f}). "
         f"MASE below 1 would beat the in-sample seasonal naive; naive scores {nv[3]:.1f}."),
        ("One-step-ahead versions", f"=Analysis!B{a0 + 5}",
         f"Forecasting each day from yesterday gives MAE {nv1[0]:.1f}; from the same weekday last week {sn1[0]:.1f} "
         f"({1 - sn1[0] / nv1[0]:.0%} better). Shorter horizons help, since the forecast origin keeps moving, but the weekly pattern still matters more than recency."),
        ("Weekday where seasonal naive fails, and MAE without it", f"={r_worst}",
         f"Wednesday (weekday 3): MAE {np.abs(te - fc['snaive'])[dow[T:] == 3].mean():.0f} vs {np.abs(te - fc['snaive'])[mask].mean():.1f} for the other days. "
         f"Day 108 (a Wednesday, only {y[107]:.0f} loaves) was a holiday; seasonal naive copies it into all four holdout Wednesdays."),
        ("Bias of each method", f"=Analysis!F{a0 + 2}",
         f"Mean errors (actual - forecast): mean {mn[4]:+.0f}, naive {nv[4]:+.0f}, seasonal naive {sn[4]:+.0f}, drift {dr[4]:+.0f}. "
         f"The mean forecast is too low (it averages the past), naive and drift are too high."),
        ("Recommendation and limitations", "text",
         "Use seasonal naive as the benchmark, but clean the holiday in the base week (or take the median of the last 3-4 same weekdays) and add the growth; "
         "the next lessons build models that must beat this table. Limitations: one 28-day holdout is a single test (lesson 24 repeats it), and MAPE, "
         "RMSE and MAE rank the methods the same way here but need not elsewhere."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-21-naive-forecasts", "21 · Naive and seasonal naive forecasts",
             "Benchmark forecasts for 28 days of bakery sales: mean, naive, seasonal naive and drift, and how each performs on the holdout.",
             df.rename(columns={"date": "time"}), "time")
    d.stat("Holdout MAE (loaves per day)", {"seasonal naive": sn[0], "mean": mn[0], "naive": nv[0], "drift": dr[0]},
           "Mean absolute error on the 28-day holdout. Lower is better; any real model must beat the best of these.", decimals=1,
           thresholds=[(None, "green"), (30, "orange"), (45, "red")])
    ts = pd.DataFrame({"time": df["date"], "actual": y, "seasonal naive": pad(fc["snaive"]), "naive": pad(fc["naive"]),
                       "mean": pad(fc["mean"]), "drift": pad(fc["drift"])})
    d.timeseries("Sales and benchmark forecasts", ts, "History, then four 28-day-ahead forecasts from the last training day.",
                 dashed=["seasonal naive", "naive", "mean", "drift"],
                 colors={"actual": "#4E79A7", "seasonal naive": "#59A14F", "naive": "#E15759", "mean": "#F28E2B", "drift": "#B07AA1"}, w=24, h=10)
    ee = pd.DataFrame({"day": df["date"][T:].dt.strftime("%a %d").to_numpy(), "seasonal naive error": te - fc["snaive"],
                       "naive error": te - fc["naive"]})
    d.bars("Holdout errors (actual - forecast, loaves)", ee, "Seasonal naive errors are small except the four Wednesdays that copy the holiday; "
           "naive errors are mostly negative (forecast too high) and follow the weekly cycle.", w=24, h=8)
    d.panels[-1]["options"]["showValue"] = "never"
    mdf = pd.DataFrame({"method": ["mean", "naive", "snaive", "drift", "naive-1", "snaive-1"],
                        "MAE": [mn[0], nv[0], sn[0], dr[0], nv1[0], sn1[0]], "RMSE": [mn[1], nv[1], sn[1], dr[1], nv1[1], sn1[1]]}).round(1)
    d.bars("MAE and RMSE by method (holdout)", mdf, "RMSE exceeds MAE where a few days are far off.", w=8)
    wk = pd.DataFrame({"day": names, "training mean": [tr[dow[:T] == k + 1].mean() for k in range(7)],
                       "holdout mean": [te[dow[T:] == k + 1].mean() for k in range(7)]}).round(1)
    d.bars("Weekday profile (loaves)", wk, "Strong weekly seasonality; holdout is higher on every weekday (growth).", w=8)
    short = ["mean", "naive", "snaive", "drift", "naive-1", "snaive-1"]
    tab = pd.DataFrame({"method": short, "MAE": [mt[m[1]][0] for m in methods], "MASE": [mt[m[1]][3] for m in methods]}).round(2)
    d.table("Accuracy table", tab, "All methods on the same 28 holdout days. snaive = seasonal naive; -1 = one step ahead. (RMSE/MAPE are in the workbook.)", w=8)
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: naive and seasonal naive forecasts

## Why benchmarks come first

A forecast error of "24 loaves" means nothing until you know what a trivial method would have achieved. Forecasting projects fail quietly when a clever model is
*worse than copying last week* and nobody checked. A **benchmark** is a method so simple that it costs nothing and needs no estimation; a model earns its
complexity only by beating it on data it has not seen. The four classical benchmarks, for history $y_1,\dots,y_T$ and horizon $h = 1,2,\dots$:

| method | forecast $\hat y_{T+h}$ | when it is hard to beat |
|---|---|---|
| **mean** | $\frac1T\sum_{t=1}^T y_t$ | stationary noise around a constant level |
| **naive** | $y_T$ | random-walk-like series (prices, levels that drift) |
| **seasonal naive** | $y_{T+h-m(k+1)},\ k=\lfloor (h-1)/m\rfloor$ | strong, stable seasonality (period $m$: 7 for daily data with a weekly cycle) |
| **drift** | $y_T + h\,\dfrac{y_T - y_1}{T-1}$ | steady trend without seasonality |

The seasonal naive rule says: "tomorrow looks like the same weekday in the last observed week". For horizons up to $m$ it uses the previous season; for $h = m+1,\dots,2m$ it
reuses the **same last observed** season again - it never uses forecasts as inputs.

## The holdout

Evaluate on data the method did not see: split the series at time $T$ into **training** ($1..T$) and **holdout/test** ($T+1..T+H$), choose methods using only the training
part, and compute errors on the holdout. Never shuffle a time series before splitting and never tune on the holdout (that is leakage: the number then measures nothing).
A single holdout is one experiment; [lesson 24](../24-backtesting-and-forecast-accuracy/theory.md) repeats it over several origins.

## Accuracy measures

With errors $e_t = y_t - \hat y_t$ on the $H$ holdout points:

$$
\text{MAE} = \frac1H\sum |e_t|,\qquad
\text{RMSE} = \sqrt{\frac1H\sum e_t^2},\qquad
\text{MAPE} = \frac1H\sum \frac{|e_t|}{|y_t|},\qquad
\text{MASE} = \frac{\text{MAE}}{\frac1{T-m}\sum_{t=m+1}^T |y_t - y_{t-m}|}.
$$

- MAE is in the units of the data and treats all errors alike; RMSE punishes large errors and is always $\ge$ MAE; the gap shows how concentrated the errors are.
- MAPE is unit-free but explodes when actual values are near zero, and penalizes over-forecasts less than under-forecasts relative to the same absolute error.
- MASE scales by the in-sample error of the (seasonal) naive method: below 1 means better than that benchmark did in the past; comparable across series.
- The **mean error** $\frac1H\sum e_t$ measures bias: a method with large mean error is systematically high or low.
- **Skill** relative to a benchmark: $1 - \text{MAE}_{model}/\text{MAE}_{benchmark}$.

## Worked example (computed)

Period $m = 3$. History $y_1..y_6 = 10, 14, 6, 12, 16, 8$; the next three actual values are $13, 18, 9$.

| method | forecasts | MAE | RMSE | MAPE |
|---|---|---|---|---|
| mean | 11, 11, 11 | 3.67 | 4.36 | 25.5 % |
| naive | 8, 8, 8 | 5.33 | 6.48 | 35.0 % |
| seasonal naive | 12, 16, 8 | 1.33 | 1.41 | 10.0 % |

The in-sample seasonal naive error is $(|12-10| + |16-14| + |8-6|)/3 = 2$, so the MASE of the seasonal naive forecast is $1.33/2 = 0.67$ and that of naive $5.33/2 = 2.67$.
Naive is worst because the last value (8) is the low point of the cycle; the mean ignores the cycle.

## Assumptions and when it fails

1. **Seasonal naive copies the base season, noise included.** One holiday, outage or promotion in the last season is repeated at every horizon - robustify by using the median or average of several past seasons, or by cleaning
   the anomaly first ([lesson 4](../04-outlier-detection/theory.md)).
2. **It cannot extrapolate a trend** (growing series are forecast too low); drift or a trend model is needed ([lesson 22](../22-trend-and-seasonal-regression-forecasting/theory.md)).
3. **Naive after a seasonal peak** inherits the peak: the last value of a weekly series is a poor level estimate.
4. **Choose $m$ from the data** ([lesson 7](../07-trend-seasonality-and-noise/theory.md)); a wrong period makes seasonal naive worse than the mean.

## Pitfalls in evaluation

1. Comparing models on different holdouts or horizons.
2. Reporting only RMSE or only MAPE; show at least MAE and RMSE and check bias.
3. Using a holdout that covers only a quiet period; include at least one full season, preferably several.
4. Letting the holdout influence the choice of model (leakage), then calling the result "out-of-sample".
5. Declaring success when the model beats the *mean* but not seasonal naive.

## Connections

- Seasonality and noise: [lesson 7](../07-trend-seasonality-and-noise/theory.md); smoothing methods that generalize these benchmarks: [lesson 8](../08-moving-averages-and-exponential-smoothing/theory.md) and [lesson 23](../23-exponential-smoothing-models/theory.md).
- Regression forecasts with trend and seasonal terms: [lesson 22](../22-trend-and-seasonal-regression-forecasting/theory.md); proper evaluation by rolling origin: [lesson 24](../24-backtesting-and-forecast-accuracy/theory.md); intervals: [lesson 25](../25-prediction-intervals-and-forecast-uncertainty/theory.md).
- Repo notes: [forecasting](../../notes/time_series/forecasting.md), [forecast evaluation](../../notes/time_series/forecast_evaluation.md),
  [seasonality and trends](../../notes/time_series/seasonality_and_trends.md), [metrics](../../notes/resampling_and_model_assessment/metrics.md).
"""

TASK = r"""
# Task: can we beat "same as last week"?

## Scenario

A bakery chain plans next month's baking volumes for one shop. The analyst proposes an elaborate model, but the operations manager asks a blunt question: **"does it beat
copying what we sold last week?"** You have 20 weeks of daily sales. Treat the first 16 weeks (112 days) as history and the last 4 weeks (28 days) as the
holdout. Build the benchmark forecasts, score them, and decide which baseline any new model must beat.

## Data

`data.csv` - 140 rows, one per day, 2026-01-05 (Monday) to 2026-05-24.

| column | meaning |
|---|---|
| `date` | calendar day |
| `loaves_sold` | loaves sold that day (units) |

Rows 1-112 are the training history (up to 2026-04-26); rows 113-140 are the holdout (2026-04-27 to 2026-05-24).

## Questions

1. Compute the mean daily sales in the training period and in the holdout. Compute the mean by weekday (Monday-Sunday) in the training period.
2. Forecast all 28 holdout days with the **mean** of the training data. Compute MAE, RMSE and MAPE.
3. Forecast the holdout with the **naive** method (the last training value, repeated). Compute MAE, RMSE, MAPE. Why is the result so poor?
4. Forecast the holdout with **seasonal naive** (same weekday, last observed week). Compute MAE, RMSE, MAPE. Add the **drift** forecast and compare all four.
5. Compute the skill of seasonal naive against naive and against the mean forecast: $1 - \text{MAE}_{snaive}/\text{MAE}_{other}$.
6. Compute the MASE of each method, using the in-sample mean of $|y_t - y_{t-7}|$ over the training period as the scale. What does a value above 1 mean?
7. Now forecast each holdout day **one step ahead** with naive (yesterday) and seasonal naive (7 days ago). Compare MAE with the 28-day-ahead versions.
8. Compute the seasonal naive absolute error by weekday. Which weekday is worst, and what in the training data explains it? Recompute the MAE without that weekday.
9. Compute the mean error (actual - forecast) of each method. Which are biased high and which low?
10. *Interpretation:* which benchmark should a new model have to beat, what would you change in the seasonal naive forecast, and what is one limitation of judging on a single 28-day holdout?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Sales and benchmark forecasts", which dashed line follows the weekly pattern and which ones are flat or straight lines?
- In "Holdout errors", which days stand out and what do they have in common?
- In "Weekday profile", compare the training and holdout bars: what do they say about a forecast built from last week alone?

## Deliverable

A short note (5-8 lines) with named parts: **Benchmarks** (table of MAE/RMSE/MAPE), **Winner** (and by how much), **Weak spot** (the failing weekday and why), **Next step**
(what a model must beat). Include a chart of actual sales and the forecasts over the holdout.
"""
