"""Lesson 22 - Trend and seasonal regression forecasting (daily orders, trend + weekday + month dummies via LINEST)."""
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import Book, Dash, md, write_csv  # noqa: E402
from _orders_story import orders_series, DAYNAMES  # noqa: E402

SLUG = "22-trend-and-seasonal-regression-forecasting"
TITLE = "Trend and seasonal regression forecasting"
MODULE = "Forecasting and model evaluation"
DATASET = "420 days of shop orders (2025-01-01 .. 2026-02-24), 392 training days + 28 holdout days"

N, TR, H = 420, 392, 28
LAST = TR + 1  # last training row in Excel (header = row 1)
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def make_data() -> pd.DataFrame:
    # trend that slowly stalls (quad<0), annual cycle peaking in December, AR(1) noise, Black Friday / Cyber Monday spikes
    return orders_series("2025-01-01", N, 2201, base=150, lin=0.30, quad=-0.00025, annual=22, sd=7, ar=0.3,
                         spikes=[(331, 85), (334, 50)])


def design(df: pd.DataFrame) -> pd.DataFrame:
    d = pd.DataFrame({"t": np.arange(1, len(df) + 1)})
    dow, mon = df["date"].dt.dayofweek.to_numpy(), df["date"].dt.month.to_numpy()
    for k in range(1, 7):
        d[f"d_{DAYNAMES[k]}"] = (dow == k).astype(int)
    for m in range(2, 13):
        d[f"m_{MONTHS[m - 1]}"] = (mon == m).astype(int)
    return d


def fill(text: str, **kw) -> str:
    for k, v in kw.items():
        text = text.replace(f"@@{k}@@", str(v))
    assert "@@" not in text, "unfilled token"
    return text


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    y = df["orders"].to_numpy(float)
    X = design(df)
    Xw = X[["t"] + [c for c in X.columns if c.startswith("d_")]]
    Xt = X[["t"]]
    names_full = list(X.columns)

    def ols(Xm):
        m = sm.OLS(y[:TR], sm.add_constant(Xm.iloc[:TR].astype(float))).fit()
        return m, np.asarray(m.predict(sm.add_constant(Xm.astype(float), has_constant="add")))

    m_t, f_t = ols(Xt)
    m_w, f_w = ols(Xw)
    m_f, f_f = ols(X)
    h = np.arange(1, H + 1)
    f_sn = np.full(N, np.nan)
    f_sn[TR:] = [y[TR + k - 1 - 7 * math.ceil(k / 7)] for k in h]
    a = y[TR:]

    def metrics(f):
        e = a - f[TR:]
        return dict(rmse=float(np.sqrt(np.mean(e ** 2))), mae=float(np.mean(np.abs(e))), bias=float(np.mean(e)),
                    mape=float(np.mean(np.abs(e) / a)))
    M = {"Seasonal naive (lag 7)": metrics(f_sn), "Trend only": metrics(f_t),
         "Trend + weekday": metrics(f_w), "Trend + weekday + month": metrics(f_f)}
    res = y[:TR] - f_f[:TR]
    ac1 = float(np.corrcoef(res[1:], res[:-1])[0, 1])
    bf = int(np.argmax(res))

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 22 - Trend and seasonal regression forecasting",
             f"Training rows 2-{LAST}, holdout rows {LAST + 1}-{N + 1}. Coefficients come from LINEST on the training rows only.")
    b.add_column("dow", lambda r: f"=WEEKDAY(Data!A{r},2)", df["date"].dt.dayofweek + 1, "0")
    b.add_column("month", lambda r: f"=MONTH(Data!A{r})", df["date"].dt.month, "0")
    b.add_column("t", lambda r: f"=ROW()-1", X["t"], "0")
    for k in range(1, 7):
        nm = f"d_{DAYNAMES[k]}"
        b.add_column(nm, lambda r, k=k: f"=IF(Data!{b.col('dow')}{r}={k + 1},1,0)", X[nm], "0")
    for m in range(2, 13):
        nm = f"m_{MONTHS[m - 1]}"
        b.add_column(nm, lambda r, m=m: f"=IF(Data!{b.col('month')}{r}={m},1,0)", X[nm], "0")

    Y = f"Data!$B$2:$B${LAST}"
    xr = lambda cols: f"Data!${b.col(cols[0])}$2:${b.col(cols[-1])}${LAST}"
    X_full, X_wd = xr(names_full), xr(list(Xw.columns))
    mf_, mw_ = len(names_full), Xw.shape[1]
    LF = f"LINEST({Y},{X_full},TRUE,TRUE)"
    LW = f"LINEST({Y},{X_wd},TRUE,TRUE)"
    tt = f"Data!${b.col('t')}$2:${b.col('t')}${LAST}"

    b.section("1. Sample split")
    b.row("Training days", f"=COUNT({Y})", TR, "0", "first 392 days: 2025-01-01 .. 2026-01-27")
    b.row("Holdout days", f"=COUNT(Data!$B${LAST + 1}:$B${N + 1})", H, "0", "never used to fit anything")

    b.section("2. Trend only: orders = a + b*t")
    slope = b.row("Slope b (orders per day, per day)", f"=SLOPE({Y},{tt})", m_t.params["t"], "0.0000")
    icpt = b.row("Intercept a", f"=INTERCEPT({Y},{tt})", m_t.params["const"], "0.00")
    b.row("R-squared", f"=RSQ({Y},{tt})", m_t.rsquared, "0.000", "share of training variance explained by the trend alone")

    b.section("3. Full model: trend + weekday dummies (Monday = base) + month dummies (January = base)")
    rows, exp = [], {}
    terms = ["Intercept (Mon, Jan, t=0)"] + names_full
    pars_f = m_f.params.to_numpy()
    se_f = m_f.bse.to_numpy()
    pars_w = m_w.params.to_numpy()
    for i, term in enumerate(terms):
        col = mf_ + 1 if i == 0 else mf_ + 1 - i
        row = [term, f"=INDEX({LF},1,{col})", f"=INDEX({LF},2,{col})"]
        exp[(i, 1)], exp[(i, 2)] = pars_f[i], se_f[i]
        if i <= mw_:
            cw = mw_ + 1 if i == 0 else mw_ + 1 - i
            row.append(f"=INDEX({LW},1,{cw})")
            exp[(i, 3)] = pars_w[i]
        else:
            row.append("")
        rows.append(row)
    c0, c1 = b.table(["Term", "Full model coef", "Std. error", "Trend+weekday model coef"], rows,
                     fmt={1: "0.000", 2: "0.000", 3: "0.000"}, expect=exp)
    coef = lambda i, colL="B": f"Analysis!${colL}${c0 + i}"
    r2_f = b.row("R-squared, full model (training)", f"=INDEX({LF},3,1)", m_f.rsquared, "0.000")
    r2_w = b.row("R-squared, trend + weekday (training)", f"=INDEX({LW},3,1)", m_w.rsquared, "0.000")
    sey = b.row("Residual standard error, full model", f"=INDEX({LF},3,2)", math.sqrt(m_f.scale), "0.00", "orders/day, n-k-1 denominator")

    # fitted / forecast columns (training rows = fitted values, holdout rows = forecasts)
    def lin_fn(prefix_cols, colL):
        def fn(r):
            s = f"={coef(0, colL)}"
            for i, c in enumerate(prefix_cols, start=1):
                s += f"+{coef(i, colL)}*Data!{b.col(c)}{r}"
            return s
        return fn
    b.add_column("fit_trend", lambda r: f"={icpt}+{slope}*Data!{b.col('t')}{r}", f_t, "0.0")
    b.add_column("fit_weekday", lin_fn(list(Xw.columns), "D"), f_w, "0.0")
    b.add_column("fit_full", lin_fn(names_full, "B"), f_f, "0.0")
    b.add_column("seasonal_naive", lambda r: f"=Data!B{r - 7 * math.ceil((r - LAST) / 7)}", f_sn, "0", first_row=LAST + 1)
    resid_exp = np.concatenate([res, np.full(N - TR, np.nan)])
    b.add_column("resid_full", lambda r: f"=Data!B{r}-Data!{b.col('fit_full')}{r}", resid_exp, "0.0")

    hr = lambda nm: f"Data!${b.col(nm)}${LAST + 1}:${b.col(nm)}${N + 1}"
    A = hr("orders")
    b.section("4. Holdout accuracy (28 days; error = actual - forecast)")
    rows, exp = [], {}
    for i, (name, col) in enumerate([("Seasonal naive (lag 7)", "seasonal_naive"), ("Trend only", "fit_trend"),
                                     ("Trend + weekday", "fit_weekday"), ("Trend + weekday + month", "fit_full")]):
        F = hr(col)
        ins = ""
        if col != "seasonal_naive":
            ins = f"=SQRT(SUMXMY2({Y},Data!${b.col(col)}$2:${b.col(col)}${LAST})/COUNT({Y}))"
            exp[(i, 1)] = float(np.sqrt(np.mean((y[:TR] - {"fit_trend": f_t, "fit_weekday": f_w, "fit_full": f_f}[col][:TR]) ** 2)))
        mm = M[name]
        rows.append([name, ins, f"=SQRT(SUMXMY2({A},{F})/COUNT({A}))", f"=SUMPRODUCT(ABS({A}-{F}))/COUNT({A})",
                     f"=SUMPRODUCT({A}-{F})/COUNT({A})", f"=SUMPRODUCT(ABS({A}-{F})/{A})/COUNT({A})"])
        exp.update({(i, 2): mm["rmse"], (i, 3): mm["mae"], (i, 4): mm["bias"], (i, 5): mm["mape"]})
    a0, a1 = b.table(["Model", "In-sample RMSE", "Holdout RMSE", "Holdout MAE", "Bias (mean error)", "MAPE"], rows,
                     fmt={1: "0.00", 2: "0.00", 3: "0.00", 4: "0.00", 5: "0.0%"}, expect=exp)

    b.section("5. Holdout weeks: totals the warehouse cares about")
    rows, exp = [], {}
    for k in range(4):
        r0, r1 = LAST + 1 + 7 * k, LAST + 7 + 7 * k
        sl = slice(7 * k, 7 * k + 7)
        act, ff, sn_ = a[sl].sum(), f_f[TR:][sl].sum(), f_sn[TR:][sl].sum()
        rows.append([k + 1, f"=SUM(Data!B{r0}:B{r1})", f"=SUM(Data!{b.col('fit_full')}{r0}:{b.col('fit_full')}{r1})",
                     f"=SUM(Data!{b.col('seasonal_naive')}{r0}:{b.col('seasonal_naive')}{r1})"])
        exp.update({(k, 1): act, (k, 2): ff, (k, 3): sn_})
    w0, w1 = b.table(["Holdout week", "Actual orders", "Full model forecast", "Seasonal naive forecast"], rows,
                     fmt={1: "0", 2: "0", 3: "0"}, expect=exp)
    wk_err = [(a[7 * k:7 * k + 7].sum() - f_f[TR:][7 * k:7 * k + 7].sum()) / a[7 * k:7 * k + 7].sum() for k in range(4)]
    bias_pct = b.row("Full model: 4-week total error (actual - forecast) / actual",
                     f"=(SUM(B{w0}:B{w1})-SUM(C{w0}:C{w1}))/SUM(B{w0}:B{w1})", float(sum(a) - f_f[TR:].sum()) / float(sum(a)),
                     "0.0%", "negative = the model over-forecasts")

    b.section("6. Training residuals of the full model")
    R = f"Data!${b.col('resid_full')}$2:${b.col('resid_full')}${LAST}"
    ac = b.row("Lag-1 autocorrelation of residuals",
               f"=CORREL(Data!{b.col('resid_full')}3:{b.col('resid_full')}{LAST},Data!{b.col('resid_full')}2:{b.col('resid_full')}{LAST - 1})",
               ac1, "0.000", "0 would mean the dummies removed all day-to-day persistence")
    mxres = b.row("Largest positive residual (orders)", f"=MAX({R})", res.max(), "0.0")
    mxdate = b.row("... on date", f'=TEXT(INDEX(Data!$A$2:$A${LAST},MATCH(MAX({R}),{R},0)),"yyyy-mm-dd")', None)
    b.row("Residual SD / mean order level", f"=STDEV({R})/AVERAGE({Y})", float(res.std(ddof=1) / y[:TR].mean()), "0.0%")

    b.line_chart("Orders, fitted values (training) and forecast (holdout)", "date", ["orders", "fit_full", "seasonal_naive"],
                 anchor="H4", y_title="orders per day")

    best = min(M, key=lambda k: M[k]["rmse"])
    wd_eff = pars_f[2:8]
    mo_eff = pars_f[8:]
    b.answers([
        ("Training days / holdout days; trend slope and R-squared of orders on t", f"={slope}",
         f"{TR} training and {H} holdout days. Slope = {m_t.params['t']:.3f} orders/day per day, R2 = {m_t.rsquared:.2f}: "
         "the trend alone explains most of the variance of a growing series, and it is the cheapest baseline."),
        ("Weekday effects (trend + weekday model): Saturday vs Monday, and R-squared", f"={coef(6, 'D')}",
         f"Saturday is {abs(pars_w[6]):.1f} orders below Monday (all else equal); R2 rises only from {m_t.rsquared:.2f} to {m_w.rsquared:.2f}. "
         "The weekly ripple is small next to the annual swing, which the month dummies in question 3 capture."),
        ("Full model: R-squared, residual standard error, lowest and highest month vs January", f"={r2_f}",
         f"R2 = {m_f.rsquared:.2f}, residual SE = {math.sqrt(m_f.scale):.1f} orders. Lowest month: {MONTHS[1 + int(np.argmin(mo_eff))]} "
         f"({mo_eff.min():.1f} vs Jan), highest: {MONTHS[1 + int(np.argmax(mo_eff))]} ({mo_eff.max():+.1f}). Month dummies are step "
         "functions that approximate a smooth annual cycle, and Jan/Feb rest on only one or two observed years."),
        ("Holdout RMSE, MAE and bias of the three regression models", f"=Analysis!C{a0 + 3}",
         "RMSE: trend only {:.1f}, + weekday {:.1f}, + month {:.1f}. Every model has negative bias ({:.1f} for the full model): "
         "it over-forecasts, because the training trend is steeper than the recent growth.".format(
             M["Trend only"]["rmse"], M["Trend + weekday"]["rmse"], M["Trend + weekday + month"]["rmse"],
             M["Trend + weekday + month"]["bias"])),
        ("Holdout RMSE, MAE and bias of the seasonal naive forecast (repeat the last training week)", f"=Analysis!C{a0}",
         f"RMSE {M['Seasonal naive (lag 7)']['rmse']:.1f}, MAE {M['Seasonal naive (lag 7)']['mae']:.1f}, bias {M['Seasonal naive (lag 7)']['bias']:.1f}. "
         f"Best RMSE on this holdout: {best}. The gap to the full model ({M['Trend + weekday + month']['rmse']:.1f}) is small relative to the "
         "noise in only 28 days, so this holdout alone cannot rank them (lesson 24)."),
        ("In-sample vs holdout RMSE of the full model", f"=Analysis!B{a0 + 3}",
         f"In-sample {np.sqrt(np.mean(res ** 2)):.1f} vs holdout {M['Trend + weekday + month']['rmse']:.1f}. The training fit is an "
         "optimistic estimate of forecast error: the model was tuned to those rows, and the future also has a different trend."),
        ("Weekly totals in the holdout: error of the full model per week", f"={bias_pct}",
         "Weekly error (actual - forecast)/actual: " + ", ".join(f"{e:.1%}" for e in wk_err) +
         ". Errors accumulate in the same direction, which is exactly what a staffing plan would suffer from."),
        ("Lag-1 autocorrelation of the training residuals and the largest residual date", f"={ac}",
         f"Autocorrelation {ac1:.2f}: the dummies leave day-to-day persistence in the errors (a sign for AR terms / lessons 14, 15). "
         f"Largest residual {res.max():.0f} orders on {df['date'].iloc[bf]:%Y-%m-%d} (Black Friday), which no weekday or month dummy can explain."),
        ("Name two limitations of this regression forecast", "see text",
         "(1) A straight trend is extrapolated forever; if growth stalls the bias grows with the horizon. (2) Dummies assume the "
         "weekday and month pattern is identical in every year and does not scale with the level; holidays like Black Friday need "
         "their own regressors. Also: with one year of history each month effect is estimated from a single year."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-22-regression-forecast", "22 · Trend and seasonal regression forecasting",
             "Linear trend + weekday + month dummies fitted on 392 training days, forecasting 28 holdout days, versus seasonal naive.",
             df.rename(columns={"date": "time"}), "time")
    d.stat("Holdout RMSE (orders/day)", {k: v["rmse"] for k, v in M.items()},
           "28 holdout days. Lower is better. The extra terms help, but not by much against seasonal naive.", unit="short", decimals=1)
    ts = pd.DataFrame({"time": df["date"], "orders": y, "fitted (training)": np.where(np.arange(N) < TR, f_f, np.nan),
                       "trend only": f_t,
                       "forecast (holdout)": np.where(np.arange(N) >= TR - 1, f_f, np.nan)})
    ts.loc[TR - 1, "forecast (holdout)"] = np.nan
    d.timeseries("Orders, regression fit and holdout forecast", ts,
                 "Annual cycle (peak around Black Friday / December), weekly ripple, and growth that flattens near the end.",
                 dashed=["forecast (holdout)", "trend only"], colors={"orders": "#9AA5B1", "fitted (training)": "#59A14F",
                                                         "trend only": "#F28E2B", "forecast (holdout)": "#E15759"}, w=24, h=9)
    hd = pd.DataFrame({"day": h, "actual": a, "full model": f_f[TR:], "trend only": f_t[TR:], "seasonal naive": f_sn[TR:]})
    d.xy("Holdout zoom (days 1-28 after the training end)", hd, "day", ["actual", "full model", "trend only", "seasonal naive"],
         "Both regression lines sit above the actual orders for most of the 28 days: bias from extrapolating the trend.",
         lines=["full model", "trend only", "seasonal naive"])
    d.bars("Weekday effect vs Monday (orders/day)", pd.DataFrame({"weekday": DAYNAMES, "effect": [0.0] + list(wd_eff)}),
           "Coefficients of the weekday dummies in the full model; Monday is the base level.", w=6)
    d.bars("Month effect vs January (orders/day)", pd.DataFrame({"month": MONTHS, "effect": [0.0] + list(mo_eff)}),
           "Coefficients of the month dummies; December and November are high, May and June low.", w=6)
    rs = pd.DataFrame({"time": df["date"].iloc[:TR], "residual": res})
    rs["|res| > 2.5 SD"] = np.where(np.abs(res) > 2.5 * res.std(ddof=1), res, np.nan)
    d.timeseries("Training residuals of the full model", rs,
                 "What the model cannot explain. The two big spikes are Black Friday and Cyber Monday.",
                 points=["|res| > 2.5 SD"], colors={"residual": "#9AA5B1", "|res| > 2.5 SD": "#E15759"}, w=24, h=7)
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


# worked example (computed with numpy/statsmodels OLS: 10 days, t = 1..10 starting Monday, weekend dummy)
THEORY = r"""
# Theory: trend and seasonal regression forecasting

## Why regression, and what it prevents

A moving average or a naive forecast ([lesson 21](../21-naive-and-seasonal-naive-forecasts/theory.md)) reuses past values
and cannot say *how much* of the pattern is growth, *how much* is Saturday, and *how much* is December. A regression on
**time** and **calendar dummies** separates them into coefficients you can read, test and extrapolate. The danger it creates
is the opposite one: a model that fits history well (high $R^2$) and then forecasts badly because it extrapolates a trend
that has changed. This lesson shows how to build the model correctly and how to judge it on data it has not seen.

## The model

For observation $t = 1,\dots,n$ with weekday $w(t) \in \{\text{Mon},\dots,\text{Sun}\}$ and month $m(t)$:

$$
y_t = \beta_0 + \beta_1 t + \sum_{j=2}^{7} \gamma_j\,\mathbb{1}[w(t)=j] + \sum_{k=2}^{12} \delta_k\,\mathbb{1}[m(t)=k] + \varepsilon_t .
$$

- $\beta_1$ is the **trend**: expected change in orders per day, per day.
- $\gamma_j$ is the weekday $j$ level **relative to Monday** (the omitted *base* category); $\delta_k$ is month $k$ relative to
  January. One category must be omitted: with all 7 weekday dummies plus the intercept the columns add up to the constant
  column and the least-squares problem has no unique solution (the *dummy-variable trap*).
- The effects are **additive**: Saturday is always the same number of orders below Monday. If seasonality grows with the level
  (a multiplicative pattern) regress $\log y_t$ instead.

Coefficients minimise $\sum_t (y_t - \hat y_t)^2$ over the **training** rows only. In a spreadsheet:
`=INDEX(LINEST(y, X, TRUE, TRUE), 1, c)` where `X` is a block of contiguous columns. **LINEST returns the coefficients in
reverse order** (last predictor first, intercept last), so predictor $j$ of $m$ sits in column $m+1-j$.

## Forecasting

The $h$-step forecast just evaluates the fitted equation at future values of the *known* regressors:
$\hat y_{n+h} = \hat\beta_0 + \hat\beta_1 (n+h) + \hat\gamma_{w(n+h)} + \hat\delta_{m(n+h)}$. Calendar regressors are known in
advance, so no recursion or forecasting of inputs is needed. That is the main practical advantage over methods that need
future values of drivers (lesson 13).

## Worked example (10 days, 2 weekend days)

Orders $y = (112,118,121,119,126,104,101,129,135,136)$ for $t=1..10$, day 1 is a Monday; $W_t=1$ on Saturday/Sunday ($t=6,7$).

- Trend only, $y = a + bt$: $a = 110.13$, $b = 1.812$, $R^2 = 0.21$. The weekend dip hides the trend.
- Trend + weekend dummy: $\hat y_t = 111.80 + 2.419\,t - 25.02\,W_t$, $R^2 = 0.967$, residual SE $= 2.46$.
- Forecasts: $t=11$ (Thursday): $111.80 + 2.419\cdot 11 = 138.41$; $t=13$ (Saturday): $111.80 + 2.419\cdot 13 - 25.02 = 118.22$.

Adding one dummy raised $R^2$ from 0.21 to 0.97 and also *corrected the trend* from 1.81 to 2.42 orders/day: a seasonal pattern
left out of the model biases the trend estimate whenever the sample does not contain whole cycles.

## In-sample fit is not forecast accuracy

Split chronologically: fit on the first part, evaluate on the last 28 days. $R^2$ and the residual standard error describe
the *training* rows; the **holdout RMSE** $\sqrt{\tfrac1H\sum (y_{n+h}-\hat y_{n+h})^2}$ describes forecasting. Always compare
against the cheapest competitor. Here that is the seasonal naive forecast $\hat y_{n+h} = y_{n+h-7\lceil h/7\rceil}$: more
terms in the regression are only worth their complexity if they beat it **out of sample**. Report the **bias** (mean error) as
well as RMSE: a trend model that over-forecasts every day has a systematic, fixable problem; one with the same RMSE and no
bias has a noise problem.

## Assumptions

1. The relationship between time and the mean is the one you wrote down (linear trend, fixed calendar effects).
2. Errors have zero mean and roughly constant variance. With daily data they are usually **autocorrelated**, so the
   standard errors LINEST reports are too small; point forecasts stay fine but intervals need care (lesson 25).
3. The structure of the future resembles the past: that is an assumption about the world, not something the fit can test.

## Pitfalls

1. **Extrapolating a trend that stalls.** A linear term has no memory of recent growth; its error grows with the horizon.
   Shorten the fitting window, add curvature, or use smoothing that adapts ([lesson 23](../23-exponential-smoothing-models/theory.md)).
2. **Dummy trap / wrong base.** Omit exactly one category per factor; interpret coefficients relative to it.
3. **Month dummies from one year.** Each month effect is then a single observation of that month and cannot be separated
   from that year's events; two or more years are the minimum, or use a smooth Fourier term.
4. **Holidays and one-off events.** Black Friday does not belong to "November"; give it its own indicator or remove it from
   the fit, otherwise it distorts the neighbouring coefficients.
5. **Judging by $R^2$.** Adding regressors never lowers training $R^2$; it can raise holdout error.
6. **Leakage.** Fitting the dummies on all data and then "forecasting" the last weeks is not a forecast.

## Related notes

- [Trend, seasonality and noise](../07-trend-seasonality-and-noise/theory.md)
- [Linear regression](../12-linear-and-nonlinear-regression/theory.md) and [multiple regression](../13-multiple-regression-and-confounding/theory.md)
- [Residual diagnostics](../15-residual-analysis-and-model-diagnostics/theory.md)
- [Backtesting and forecast accuracy](../24-backtesting-and-forecast-accuracy/theory.md) and [prediction intervals](../25-prediction-intervals-and-forecast-uncertainty/theory.md)
- Repo notes: [seasonality and trends](../../notes/time_series/seasonality_and_trends.md), [forecast evaluation](../../notes/time_series/forecast_evaluation.md)
"""

TASK = r"""
# Task: trend and seasonal regression forecasting

## Scenario

You plan staffing and stock for **Hearthside**, an online candle shop. Next month's packing capacity is booked four weeks in
advance, so the operations lead wants a **daily orders forecast for the next 28 days**. A teammate proposes the "obvious" fix
for a growing, weekly-patterned series: regress orders on time plus weekday and month dummies. You must decide whether that
beats the simple rule "next four weeks look like last week" (the seasonal naive forecast from lesson 21).

## Data

`data.csv` - 420 consecutive days, 2025-01-01 to 2026-02-24, one row per day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `orders` | number of orders placed that day |

Use the **first 392 days (to 2026-01-27) as the training set** and the **last 28 days as the holdout**. Nothing from the
holdout may enter a fitted coefficient.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Add a day index `t` and fit `orders = a + b*t` on the training days (`SLOPE`, `INTERCEPT`, `RSQ`). How many orders per day is
   the series growing by, and how much variance does the trend explain?
2. Add six weekday dummies (Monday = base) and fit trend + weekday with `LINEST`. What is the Saturday effect relative to Monday and
   what is the new $R^2$?
3. Add eleven month dummies (January = base) and fit the full model. Report $R^2$, the residual standard error, and the lowest and
   highest month relative to January.
4. Forecast the 28 holdout days with each of the three regression models. Report holdout RMSE, MAE and bias (actual - forecast)
   for each.
5. Build the seasonal naive forecast for the holdout (repeat the last training week four times) and compute the same three numbers.
   Which method wins on RMSE?
6. Compare the in-sample RMSE and the holdout RMSE of the full model. What does the gap mean?
7. Sum actual and forecast orders for each of the four holdout weeks. In which direction, and by how much, does the full model err?
8. Compute the lag-1 autocorrelation of the full model's training residuals and find the date of the largest residual.
9. *Explain in 3-4 sentences* two limitations of using this regression to plan the next four weeks.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Orders, regression fit and holdout forecast", where does the red forecast leave the actual orders, and in which direction?
- Compare "Weekday effect vs Monday" and "Month effect vs January" with your coefficients from questions 2 and 3.
- In "Training residuals", what are the points flagged in red, and why can the dummies not absorb them?

## Deliverable

A short note (6-8 lines) with a recommendation: *which forecast would you give operations for the next four weeks, and
how wrong do you expect it to be?* Include the holdout RMSE table, one chart of forecast vs actual, and one statement
about what you would change before trusting the model for a longer horizon.
"""
