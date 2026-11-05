"""Lesson 24 - Backtesting and forecast accuracy (rolling-origin evaluation, MAE/RMSE/MAPE/sMAPE/MASE, leakage)."""
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import INPUT_FILL, Book, Dash, md, write_csv  # noqa: E402
from _orders_story import orders_series  # noqa: E402

SLUG = "24-backtesting-and-forecast-accuracy"
TITLE = "Backtesting and forecast accuracy"
MODULE = "Forecasting and model evaluation"
DATASET = "336 days of shop orders (2025-01-06 .. 2025-12-07), 36 weekly forecast origins x 7-day horizon"

N, T0 = 336, 84            # first origin = 84 days of history
ORIGINS = list(range(T0, N - 6, 7))  # 84, 91, ..., 329
NORIG = len(ORIGINS)       # 36
R0, R1 = T0 + 2, N + 1     # Excel rows of the evaluated days (t = 85 .. 336)
LAST4 = R1 - 27            # first Excel row of the last 28 days
METHODS = ["Naive", "Seasonal naive", "Weekday mean (4 wk)", "Weekday mean (all history)"]
KEYS = ["naive", "snaive", "mean4", "meanall"]
WINDOWS = [1, 2, 4, 6, 8, 12]


def make_data() -> pd.DataFrame:
    # three promotions / dips of two weeks each on top of a slow trend and a random-walk level; calm last two months
    promos = [(100, 45), (170, -40), (250, 60)]
    sp = [(i + k, s) for i, s in promos for k in range(14)]
    return orders_series("2025-01-06", N, 2405, base=150, lin=0.18, ar=0.25, sd=6.5, rw_sd=1.5, weekday_scale=1.5, spikes=sp)


def fill(text, **kw):
    for k, v in kw.items():
        text = text.replace(f"@@{k}@@", str(v))
    assert "@@" not in text
    return text


def forecasts(y):
    """Reference implementation: dict of arrays (length N, NaN where not evaluated) for origin T and horizon h = t - T."""
    out = {k: np.full(N, np.nan) for k in KEYS + ["leaky"]}
    origin = np.full(N, np.nan)
    hh = np.full(N, np.nan)
    for T in ORIGINS:
        for h in range(1, 8):
            i = T + h - 1                  # 0-based index of the target day
            origin[i], hh[i] = T, h
            out["naive"][i] = y[T - 1]
            out["snaive"][i] = y[i - 7]
            out["mean4"][i] = np.mean([y[i - 7 * k] for k in range(1, 5)])
            out["meanall"][i] = np.mean([y[j] for j in range(i % 7, T, 7)])   # all earlier same-weekday days up to the origin
    # LEAKY: realised mean of the target week + weekday profile estimated on ALL evaluated days (test period included)
    wm = np.full(N, np.nan)
    for T in ORIGINS:
        wm[T:T + 7] = np.mean(y[T:T + 7])
    dev = y - wm
    for i in range(N):
        if not np.isnan(origin[i]):
            out["leaky"][i] = wm[i] + np.nanmean(dev[(np.arange(N) % 7 == i % 7) & ~np.isnan(dev)])
    return out, origin, hh


def mean_w(y, W):
    f = np.full(N, np.nan)
    for T in ORIGINS:
        for h in range(1, 8):
            i = T + h - 1
            f[i] = np.mean([y[i - 7 * k] for k in range(1, W + 1)])
    return f


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    y = df["orders"].to_numpy(float)
    F, origin, hh = forecasts(y)
    ev = ~np.isnan(origin)
    AE = {k: np.abs(y - F[k]) for k in F}
    n_eval = int(ev.sum())
    scale = float(np.mean(np.abs(y[7:T0] - y[:T0 - 7])))     # in-sample seasonal-naive MAE, t = 8..84

    def stats(k):
        f, m = F[k][ev], ev
        e = y[m] - f
        return dict(mae=np.mean(np.abs(e)), rmse=math.sqrt(np.mean(e ** 2)), mape=np.mean(np.abs(e) / y[m]),
                    smape=np.mean(2 * np.abs(e) / (y[m] + f)), bias=np.mean(e), mase=np.mean(np.abs(e)) / scale)
    S = {k: stats(k) for k in KEYS}
    per = {k: np.array([np.mean(AE[k][origin == T]) for T in ORIGINS]) for k in KEYS}
    best_each = [KEYS[int(np.argmin([per[k][j] for k in KEYS]))] for j in range(NORIG)]
    wins = {k: best_each.count(k) for k in KEYS}
    last4 = {k: float(np.mean(AE[k][-28:])) for k in KEYS}
    full = {k: float(S[k]["mae"]) for k in KEYS}
    rank_full = {k: 1 + sum(full[o] < full[k] for o in KEYS) for k in KEYS}
    rank_last = {k: 1 + sum(last4[o] < last4[k] for o in KEYS) for k in KEYS}
    mae_sn_same = float(np.mean(AE["snaive"][ev]))
    mae_leaky = float(np.mean(AE["leaky"][ev]))
    assert all(S[k]["mase"] > 1 for k in KEYS) and mae_leaky < 0.7 * mae_sn_same
    assert min(KEYS, key=lambda k: last4[k]) != min(KEYS, key=lambda k: full[k])

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 24 - Backtesting and forecast accuracy",
             f"Weekly forecast origins every 7 days from t = {T0}; each origin forecasts the next 7 days using only data up to that origin.")
    b.add_column("t", lambda r: "=ROW()-1", np.arange(1, N + 1), "0")
    b.add_column("dow", lambda r: f"=WEEKDAY(Data!A{r},2)", df["date"].dt.dayofweek + 1, "0")
    tc, dc = b.col("t"), b.col("dow")
    Y = f"Data!$B$2:$B${N + 1}"
    TT, DD = f"Data!${tc}$2:${tc}${N + 1}", f"Data!${dc}$2:${dc}${N + 1}"
    b.add_column("origin", lambda r: f"={T0}+7*INT((Data!{tc}{r}-{T0 + 1})/7)", origin, "0", first_row=R0)
    oc = b.col("origin")
    b.add_column("h", lambda r: f"=Data!{tc}{r}-Data!{oc}{r}", hh, "0", first_row=R0)
    b.add_column("f_naive", lambda r: f"=INDEX({Y},Data!{oc}{r})", F["naive"], "0.0", first_row=R0)
    b.add_column("f_snaive", lambda r: f"=Data!B{r - 7}", F["snaive"], "0.0", first_row=R0)
    b.add_column("f_mean4", lambda r: f'=AVERAGEIFS({Y},{DD},Data!{dc}{r},{TT},"<="&Data!{oc}{r},{TT},">"&Data!{oc}{r}-28)',
                 F["mean4"], "0.0", first_row=R0)
    b.add_column("f_meanall", lambda r: f'=AVERAGEIFS({Y},{DD},Data!{dc}{r},{TT},"<="&Data!{oc}{r})', F["meanall"], "0.0", first_row=R0)
    wmv = np.full(N, np.nan)
    for T in ORIGINS:
        wmv[T:T + 7] = y[T:T + 7].mean()
    b.add_column("week_mean", lambda r: f"=AVERAGEIFS(Data!$B${R0}:$B${R1},Data!${oc}${R0}:${oc}${R1},Data!{oc}{r})", wmv, "0.0", first_row=R0)
    b.add_column("dev_from_week", lambda r: f"=Data!B{r}-Data!{b.col('week_mean')}{r}", y - wmv, "0.0", first_row=R0)
    wc, vc = b.col("week_mean"), b.col("dev_from_week")
    b.add_column("f_leaky", lambda r: (f"=Data!{wc}{r}+AVERAGEIFS(Data!${vc}${R0}:${vc}${R1},Data!${dc}${R0}:${dc}${R1},Data!{dc}{r})"),
                 F["leaky"], "0.0", first_row=R0)
    fnames = {"naive": "f_naive", "snaive": "f_snaive", "mean4": "f_mean4", "meanall": "f_meanall", "leaky": "f_leaky"}
    anames = {k: "ae_" + k for k in fnames}
    for k in fnames:
        b.add_column(anames[k], lambda r, k=k: f"=ABS(Data!B{r}-Data!{b.col(fnames[k])}{r})", AE[k],
                     "0.0", first_row=R0)
    rr = lambda nm, lo=R0, hi=R1: f"Data!${b.col(nm)}${lo}:${b.col(nm)}${hi}"

    b.section("1. Set-up")
    b.row("Number of forecast origins", f"=COUNT({rr('origin')})/7", NORIG, "0", "one origin per week, horizon 1-7 days")
    nf = b.row("Number of evaluated forecasts", f"=COUNT({rr('origin')})", n_eval, "0")
    b.row("History available at the first origin (days)", f"=MIN({rr('origin')})", T0, "0")
    sc = b.row("MASE scale: in-sample seasonal-naive MAE (days 8-84)",
               f"=SUMPRODUCT(ABS(Data!$B$9:$B${T0 + 1}-Data!$B$2:$B${T0 - 6}))/{T0 - 7}", scale, "0.00",
               "orders; MASE divides the MAE by this")

    b.section("2. Accuracy over all 252 forecasts (error = actual - forecast)")
    rows, exp = [], {}
    for i, (nm, k) in enumerate(zip(METHODS, KEYS)):
        A = rr("f_" + k)
        yy = f"Data!$B${R0}:$B${R1}"
        rows.append([nm, f"=AVERAGE({rr(anames[k])})", f"=SQRT(SUMXMY2({yy},{A})/COUNT({A}))",
                     f"=SUMPRODUCT(ABS({yy}-{A})/{yy})/COUNT({A})", f"=SUMPRODUCT(2*ABS({yy}-{A})/({yy}+{A}))/COUNT({A})",
                     f"=B{b.next_row + 1 + i}/{b.local(sc)}", f"=SUMPRODUCT({yy}-{A})/COUNT({A})"])
        exp.update({(i, 1): S[k]["mae"], (i, 2): S[k]["rmse"], (i, 3): S[k]["mape"], (i, 4): S[k]["smape"], (i, 5): S[k]["mase"],
                    (i, 6): S[k]["bias"]})
    m0, m1 = b.table(["Method", "MAE", "RMSE", "MAPE", "sMAPE", "MASE", "Bias"], rows,
                     fmt={1: "0.00", 2: "0.00", 3: "0.0%", 4: "0.0%", 5: "0.00", 6: "0.00"}, expect=exp)

    b.section("3. One row per forecast origin: MAE of the 7 days that followed")
    hdr_row = b.next_row
    rows, exp = [], {}
    for j, T in enumerate(ORIGINS):
        rr_ = hdr_row + 1 + j
        cells = [T, f"=INDEX(Data!$A$2:$A${N + 1},A{rr_})"]
        for c, k in enumerate(KEYS):
            cells.append(f"=AVERAGEIFS({rr(anames[k])},{rr('origin')},$A{rr_})")
            exp[(j, 2 + c)] = per[k][j]
        cells.append(f'=INDEX($C${hdr_row}:$F${hdr_row},MATCH(MIN(C{rr_}:F{rr_}),C{rr_}:F{rr_},0))')
        rows.append(cells)
    o0, o1 = b.table(["Origin t", "Last known date"] + METHODS + ["Best method"], rows,
                     fmt={1: "yyyy-mm-dd", 2: "0.0", 3: "0.0", 4: "0.0", 5: "0.0"}, expect=exp)
    b.line_chart_from_table("MAE per forecast origin: the ranking changes over time", 1, [3, 4, 5, 6], o0, o1, anchor="J4",
                            x_title="origin (days of history)", y_title="MAE (orders)")
    b.section("4. Who wins how often?")
    wrow = {}
    for nm, k in zip(METHODS, KEYS):
        wrow[k] = b.row(f"Origins where '{nm}' is best", f'=COUNTIF($G${o0}:$G${o1},"{nm}")', wins[k], "0")
    sn_col = f"$D${o0}:$D${o1}"
    mn = b.row("Seasonal naive: lowest per-origin MAE", f"=MIN({sn_col})", per["snaive"].min(), "0.0")
    mx = b.row("Seasonal naive: highest per-origin MAE", f"=MAX({sn_col})", per["snaive"].max(), "0.0")
    b.row("Seasonal naive: SD of per-origin MAE", f"=STDEV({sn_col})", per["snaive"].std(ddof=1), "0.0")
    b.row("Highest / lowest", f"={b.local(mx)}/{b.local(mn)}", per["snaive"].max() / per["snaive"].min(), "0.0")

    b.section("5. A single holdout versus the whole backtest")
    rows, exp = [], {}
    for i, (nm, k) in enumerate(zip(METHODS, KEYS)):
        base = b.next_row + 1
        rows.append([nm, f"=AVERAGE({rr(anames[k])})", f"=AVERAGE({rr(anames[k], LAST4, R1)})",
                     f"=RANK(B{base + i},$B${base}:$B${base + 3},1)", f"=RANK(C{base + i},$C${base}:$C${base + 3},1)"])
        exp.update({(i, 1): full[k], (i, 2): last4[k], (i, 3): rank_full[k], (i, 4): rank_last[k]})
    h0, h1 = b.table(["Method", "MAE, all 36 origins", "MAE, last 4 origins only (last 28 days)", "Rank (all)", "Rank (last 28 days)"], rows,
                     fmt={1: "0.00", 2: "0.00", 3: "0", 4: "0"}, expect=exp)
    b.bar_chart_from_table("MAE: whole backtest vs last 28 days only", 1, [2, 3], h0, h1, anchor="J24", y_title="MAE (orders)")

    b.section("6. Leakage: a forecast that peeks at next week")
    sm_ = b.row("Seasonal naive MAE (honest)", f"=AVERAGE({rr(anames['snaive'])})", mae_sn_same, "0.00")
    lm_ = b.row("'Calibrated' forecast MAE: target week's realised mean + weekday profile from all days",
                f"=AVERAGE({rr(anames['leaky'])})", mae_leaky, "0.00", "uses the actuals of the week being forecast")
    b.row("Leaky / honest MAE", f"={b.local(lm_)}/{b.local(sm_)}", mae_leaky / mae_sn_same, "0.00", "far below 1 = too good to be true")

    b.section("7. MAE by horizon (day within the forecast week)")
    rows, exp = [], {}
    for h in range(1, 8):
        rows.append([h] + [f"=AVERAGEIFS({rr(anames[k])},{rr('h')},$A{b.next_row + h})" for k in ("naive", "snaive", "mean4")])
        for c, k in enumerate(("naive", "snaive", "mean4")):
            exp[(h - 1, 1 + c)] = float(np.mean(AE[k][hh == h]))
    b.table(["Horizon h (days)", "Naive", "Seasonal naive", "Weekday mean (4 wk)"], rows, fmt={1: "0.0", 2: "0.0", 3: "0.0"}, expect=exp)

    b.section("8. Window length of the weekday mean (yellow = edit me; 1 week = seasonal naive, 12 = quasi-expanding)")
    rows = [[w, None] for w in WINDOWS]
    w0, w1 = b.table(["Window (weeks)", "MAE over all 252 forecasts"], rows, fmt={0: "0", 1: "0.00"})
    wmae = {}
    for j, w in enumerate(WINDOWS):
        row = w0 + j
        b.an.cell(row=row, column=1).fill = INPUT_FILL
        fw = mean_w(y, w)
        wmae[w] = float(np.nanmean(np.abs(y - fw)))
        nm = f"ae_w{j + 1}"
        b.add_column(nm, lambda r, row=row: (f'=ABS(Data!B{r}-AVERAGEIFS({Y},{DD},Data!{dc}{r},{TT},"<="&Data!{oc}{r},'
                                             f'{TT},">"&Data!{oc}{r}-7*Analysis!$A${row}))'),
                     np.abs(y - fw), "0.0", first_row=R0)
        b.an.cell(row=row, column=2, value=f"=AVERAGE({rr(nm)})").number_format = "0.00"
        b.checks.append((f"Analysis!B{row}", f"MAE window {w}", wmae[w]))
    bestW = min(wmae, key=wmae.get)

    kbest = min(KEYS, key=lambda k: full[k])
    b.answers([
        ("How many forecast origins and evaluated forecasts? How much history does the first origin have?", f"={nf}",
         f"{NORIG} weekly origins x 7 days = {n_eval} forecasts; the first origin has {T0} days of history. Each forecast only used data before its origin."),
        ("MAE and RMSE of the four methods over all forecasts", f"=Analysis!B{m0 + 1}",
         "MAE: " + ", ".join(f"{nm} {S[k]['mae']:.1f}" for nm, k in zip(METHODS, KEYS)) + ". RMSE: " +
         ", ".join(f"{S[k]['rmse']:.1f}" for k in KEYS) + f". Best overall: {METHODS[KEYS.index(kbest)]}."),
        ("MAPE, sMAPE and MASE of each method; which are better than the in-sample seasonal naive (MASE < 1)?", f"=Analysis!F{m0 + 1}",
         f"MASE (scale {scale:.1f}): " + ", ".join(f"{S[k]['mase']:.2f}" for k in KEYS) + ". MASE below 1 means the method beats the seasonal naive "
         "error measured in-sample; here every method is above 1 because the future was harder than the 12 weeks the scale was measured on. "
         "MAPE: " + ", ".join(f"{S[k]['mape']:.1%}" for k in KEYS) + "."),
        ("For how many origins is each method the best one-week forecaster?", f"={wrow['snaive']}",
         "Wins: " + ", ".join(f"{nm} {wins[k]}" for nm, k in zip(METHODS, KEYS)) +
         f" of {NORIG}. Even the best method wins only about {max(wins.values()) / NORIG:.0%} of the weeks."),
        ("Pretend you had only the last 28 days as a holdout: what ranking do you get compared with the full backtest?", f"=Analysis!C{h0 + 2}",
         "Last 28 days: " + ", ".join(f"{nm} {last4[k]:.1f}" for nm, k in zip(METHODS, KEYS)) + " vs all origins: " +
         ", ".join(f"{full[k]:.1f}" for k in KEYS) + f". On the calm final month '{METHODS[KEYS.index(min(KEYS, key=lambda k: last4[k]))]}' wins, "
         f"overall it is '{METHODS[KEYS.index(kbest)]}': a single holdout picked the wrong winner."),
        ("Spread of the per-origin MAE of the seasonal naive", f"={mx}",
         f"From {per['snaive'].min():.1f} to {per['snaive'].max():.1f} (x{per['snaive'].max() / per['snaive'].min():.1f}). One origin cannot "
         "tell you the typical accuracy; promotions and level shifts make some weeks several times harder than others."),
        ("Leakage: MAE of the 'calibrated' forecast (realised weekly mean + weekday profile fitted on all days) versus the honest seasonal naive", f"={lm_}",
         f"Leaky {mae_leaky:.1f} vs honest {mae_sn_same:.1f} (ratio {mae_leaky / mae_sn_same:.2f}). The 'model' is told the realised weekly level, "
         "so promotions and level shifts are no longer errors, and its weekday profile was fitted on the test days too; on the Sunday of the forecast neither exists."),
        ("Which window length (1-12 weeks) of the weekday mean minimises the MAE?", f"=Analysis!B{w0 + WINDOWS.index(bestW)}",
         f"Best window: {bestW} weeks (MAE {wmae[bestW]:.2f}); " + ", ".join(f"{w}w {wmae[w]:.2f}" for w in WINDOWS) +
         ". Averaging more weeks removes day-level noise but lags behind promotions and level shifts; in this year the lag costs more than the averaging gains."),
        ("Which method would you deploy and how sure are you?", "see text",
         f"{METHODS[KEYS.index(kbest)]} is best on average, but the margin to the runner-up is small compared to the week-to-week spread, and "
         "overlapping forecast errors are correlated, so the effective sample is far smaller than 252. Deploy the simple benchmark, keep backtesting "
         "as new weeks arrive, and revisit if the ranking in the most recent origins keeps differing."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-24-backtesting", "24 · Backtesting and forecast accuracy",
             "Rolling-origin evaluation of four simple forecasters on 36 weekly origins, with the single-holdout and leakage traps.",
             df.rename(columns={"date": "time"}), "time")
    d.stat("MASE over all 252 forecasts (1 = in-sample seasonal naive)", {nm: S[k]["mase"] for nm, k in zip(METHODS, KEYS)},
           "Lower is better. Scaled by the in-sample seasonal-naive MAE of the first 84 days.", decimals=2)
    ts = pd.DataFrame({"time": df["date"], "orders": y, "seasonal naive": F["snaive"], "weekday mean (4 wk)": F["mean4"]})
    d.timeseries("Orders and two backtest forecasts", ts,
                 "Each day is forecast from an origin at most 7 days earlier. The mid-April promotion, the late-June dip and the mid-September promotion are missed by both.",
                 colors={"orders": "#9AA5B1", "seasonal naive": "#4E79A7", "weekday mean (4 wk)": "#E15759"}, w=24, h=9)
    po = pd.DataFrame({"time": [df["date"].iloc[T - 1] for T in ORIGINS], **{nm: per[k] for nm, k in zip(METHODS, KEYS)}})
    d.timeseries("MAE of each weekly forecast origin", po,
                 "The best method changes from week to week. The final weeks (calm) are not representative of the rest.",
                 colors=dict(zip(METHODS, ["#B07AA1", "#4E79A7", "#E15759", "#9AA5B1"])), w=12)
    d.bars("MAE: all 36 origins vs the last 4 only", pd.DataFrame({"method": METHODS, "all origins": [full[k] for k in KEYS],
                                                                   "last 28 days only": [last4[k] for k in KEYS]}),
           "A single, recent holdout reverses the ranking of the top two methods.", w=12)
    d.bars("Window length of the weekday mean: MAE", pd.DataFrame({"window": [f"{w} wk" for w in WINDOWS], "MAE": [wmae[w] for w in WINDOWS]}),
           "1 week = seasonal naive. Longer windows are not better here: promotions make recent weeks more informative than older ones.", w=12, h=8)
    d.bars("Leakage: honest vs calibrated", pd.DataFrame({"forecast": ["seasonal naive (honest)", "calibrated to the target week (leaky)"],
                                                              "MAE": [mae_sn_same, mae_leaky]}),
           "The leaky forecast looks far better and cannot be used in production.", w=12, h=8)
    d.save(out)

    md(out / "theory.md", fill(THEORY, **EX))
    md(out / "task.md", TASK)
    return b


# worked example numbers (computed once with numpy)
_a = np.array([102, 98, 110, 95.0])
_f = np.array([100, 104, 105, 99.0])
_e = _a - _f
_sc = 6.0
EX = dict(
    MAE=f"{np.mean(np.abs(_e)):.2f}", RMSE=f"{math.sqrt(np.mean(_e ** 2)):.2f}", MAPE=f"{np.mean(np.abs(_e) / _a):.2%}".replace("%", r"\%"),
    SMAPE=f"{np.mean(2 * np.abs(_e) / (_a + _f)):.2%}".replace("%", r"\%"), MASE=f"{np.mean(np.abs(_e)) / _sc:.2f}",
    BIAS=f"{np.mean(_e):.2f}")

THEORY = r"""
# Theory: backtesting and forecast accuracy

## Why this matters

A forecast model is only as good as the evidence that it works on data it has not seen. In-sample fit measures how well you
described the past; it says nothing about how wrong you will be next week. **Backtesting** replays history as if you were
forecasting in real time, so that the accuracy you measure is the accuracy you would have had. The two ways this goes wrong
are *leakage* (the evaluation secretly uses the future) and *luck* (one lucky holdout period picks the wrong model).

## Forecast origin, horizon, error

- The **origin** $T$ is the last observation available when the forecast is made; the **horizon** $h$ says how far ahead:
  $\hat y_{T+h\mid T}$ uses only $y_1,\dots,y_T$ (and anything known in advance, such as the calendar).
- The **forecast error** is $e_{T+h} = y_{T+h} - \hat y_{T+h\mid T}$ (actual minus forecast). Positive = under-forecast.

## Rolling-origin (time-series cross-validation)

Choose a first origin $T_0$ with enough history, forecast the next $H$ days, then move the origin forward and repeat:

1. **Expanding window**: the training set at origin $T$ is $y_1..y_T$ (it grows).
2. **Sliding window**: only the last $W$ observations are used (constant size); better when the process drifts.

Never shuffle: random K-fold splits train on the future and test on the past. With $K$ origins every $s$ days and horizon
$H$ you obtain $K\cdot H$ errors, but they are **not independent**: forecasts from the same origin share the same level error,
and adjacent origins overlap in time. The effective sample size is closer to the number of origins than to $K\cdot H$.

## Accuracy measures

For $n$ errors $e_i$ with actuals $a_i$ and forecasts $f_i$:

$$
\text{MAE}=\tfrac1n\sum|e_i|,\quad
\text{RMSE}=\sqrt{\tfrac1n\sum e_i^2},\quad
\text{MAPE}=\tfrac1n\sum\frac{|e_i|}{|a_i|},\quad
\text{sMAPE}=\tfrac1n\sum\frac{2|e_i|}{|a_i|+|f_i|},
$$
$$
\text{MASE}=\frac{\text{MAE}}{\frac{1}{T_0-m}\sum_{t=m+1}^{T_0}|y_t-y_{t-m}|},\qquad
\text{bias}=\tfrac1n\sum e_i .
$$

- **MAE** is in the unit of the data and robust to rare large misses; **RMSE** punishes large errors (use it when a big miss is
  disproportionately costly, e.g. stock-outs). RMSE $\ge$ MAE always; a large gap means a few large errors.
- **MAPE** is scale-free but explodes when actuals are near zero and penalises over-forecasts more than under-forecasts;
  **sMAPE** softens that but is still unstable near zero (and is not symmetric either). Never use them on series that touch zero.
- **MASE** divides by the in-sample error of the seasonal naive method ($m=7$ here). It is unit-free, defined at zero, and
  below 1 means "better than the naive benchmark would have been on the training data".
- **Bias** tells you whether errors lean in one direction (plan for it), the others tell you how large they are.

**Worked example** with actuals $(102,98,110,95)$, forecasts $(100,104,105,99)$ and an in-sample scale of 6.0: errors
$(2,-6,5,-4)$, MAE $=@@MAE@@$, RMSE $=@@RMSE@@$, MAPE $=@@MAPE@@$, sMAPE $=@@SMAPE@@$, MASE $=@@MASE@@$, bias $=@@BIAS@@$. The
RMSE is larger than the MAE because of the $-6$ and $+5$ errors; the negative bias says the model slightly over-forecasts.

## Leakage: when the test is not a test

Leakage means information from the future influences the forecast or its tuning. Typical forms:

1. **Centred smoothers** (centred moving average, a spline fitted to the whole series) used as a "forecast", or a forecast
   *calibrated* so that it matches the realised total of the period it is supposed to predict.
2. **Fitting on everything**, then scoring the last weeks (the coefficients have already seen them). Includes seasonal factors,
   scalers and outlier thresholds computed on the whole series.
3. **Tuning on the test set**: trying many models or parameters and reporting the best holdout score; the winner's score is
   optimistic by selection. Keep a final untouched block, or nest the tuning inside the backtest.
4. **Features that are not known at the origin** (next week's promo calendar is fine, next week's weather actuals are not).

## A single holdout is one draw

The error of a forecast method in one 4-week window depends heavily on what happened in that window (a promotion, a holiday, a
quiet month). Rank methods on a single holdout and the winner may be the one that suits *that* month. A rolling-origin
evaluation gives a distribution of scores (min, max, how often each method wins), which is what you need to judge
whether a difference between two methods is larger than the week-to-week scatter.

## Assumptions and pitfalls

1. Future errors resemble backtest errors: no structural change. Check the most recent origins separately.
2. The horizon of the backtest must be the horizon of the decision (a 1-day-ahead score says little about 4 weeks ahead).
3. Report several metrics: the ranking can change between MAE and RMSE.
4. Aggregating over origins hides the worst cases; look at the largest per-origin error.
5. Comparing against a naive benchmark ([lesson 21](../21-naive-and-seasonal-naive-forecasts/theory.md)) is mandatory; a score without
   a benchmark has no meaning.

## Related notes

- [Trend and seasonal regression forecasting](../22-trend-and-seasonal-regression-forecasting/theory.md)
- [Exponential smoothing models](../23-exponential-smoothing-models/theory.md)
- [Prediction intervals and forecast uncertainty](../25-prediction-intervals-and-forecast-uncertainty/theory.md)
- [Sampling distributions](../16-sampling-distributions-and-the-clt/theory.md)
- Repo note: [forecast evaluation](../../notes/time_series/forecast_evaluation.md)
"""

TASK = r"""
# Task: backtesting and forecast accuracy

## Scenario

Hearthside's operations team must pick a method for the **weekly staffing forecast**: every Sunday evening they forecast the
next seven days of orders. Three candidate rules exist, and a colleague who tested them on "the last month" says the
4-week weekday average wins clearly. You are asked to check that claim with a proper backtest before the rule is adopted.

## Data

`data.csv` - 336 consecutive days, 2025-01-06 (Monday) to 2025-12-07, one row per day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `orders` | orders placed that day |

**Forecast rules** (all use only data up to the forecast origin T, a Sunday evening; target day t = T+h, h = 1..7):

- *Naive*: every day equals the last observed day (y at T).
- *Seasonal naive*: y at t-7.
- *Weekday mean (4 wk)*: the average of the same weekday over the 4 most recent weeks (t-7, t-14, t-21, t-28).
- *Weekday mean (all history)*: the average of the same weekday over **all** days up to T.

**Origins:** T = 84, 91, ..., 329 (36 weekly origins, 252 forecasts, first origin has 12 weeks of history).

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Add day index `t` and weekday columns. For each day t = 85..336 find its origin T = 84 + 7*INT((t-85)/7) and horizon h = t - T.
   How many origins and forecasts are there?
2. Build the four forecast columns using only data up to the origin. Compute MAE, RMSE and bias for each rule over all 252 forecasts.
3. Compute MAPE, sMAPE and MASE (scale = mean |y[t] - y[t-7]| over t = 8..84). Which rules have MASE below 1?
4. Compute the MAE of each origin (7 days) for every rule and, for each origin, the best rule. Count how often each rule wins.
5. Suppose you had evaluated only the last 28 days (the last 4 origins). Compute each rule's MAE there and rank the rules; compare with the ranking over all origins.
6. For the seasonal naive, report the lowest and highest per-origin MAE and their ratio.
7. Build a "calibrated" forecast: the mean orders of the target week (Mon-Sun, i.e. the week that follows the origin) plus the average deviation of that
   weekday from its own week mean, computed over all 252 days. Compare its MAE with the plain seasonal naive. Why can this number never be produced on a Sunday evening?
8. Compute the MAE of the weekday mean for windows of 1, 2, 4, 6, 8 and 12 weeks. Which window is best?
9. *Explain in 3-4 sentences* which rule you recommend, how confident you are, and why 252 forecasts are fewer independent observations than they look.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "MAE of each weekly forecast origin", which weeks hurt every method, and what happens in the last weeks?
- In "MAE: all 36 origins vs the last 4 only", does the ranking agree with your answers to questions 2 and 5?
- In "Leakage: honest vs calibrated", how much better does the peeking forecast look, and why?

## Deliverable

A one-page note: *which weekly rule should operations adopt?* Include the metric table, the per-origin chart, a sentence on
why the colleague's "last month" test misled, and one sentence on how you would keep monitoring the chosen rule after launch.
"""
