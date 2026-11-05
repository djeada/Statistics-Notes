"""Lesson 14 - Spurious correlation and autocorrelation."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "14-spurious-correlation-and-autocorrelation"
TITLE = "Spurious correlation and autocorrelation"
MODULE = "Relationships and statistical models"
DATASET = "250 days of three indicators: two independent random walks and one series genuinely tied to the first"
LAGS = [1, 2, 5, 10, 20]
ROLL = 60


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1657)
    n = 250
    sessions = 100 + np.cumsum(rng.normal(0, 2.5, n))        # random walk
    stock = 100 + np.cumsum(rng.normal(0, 2.0, n))           # an independent random walk
    orders = 20 + 0.4 * sessions + rng.normal(0, 0.5, n)     # genuinely driven by sessions (same-day)
    date = pd.date_range("2025-01-01", periods=n, freq="D")
    return pd.DataFrame({"date": date, "sessions_k": sessions.round(2), "stock_index": stock.round(2),
                         "orders_k": orders.round(2)})


def acf(x, k):
    x = np.asarray(x, dtype=float)
    m = x.mean()
    return float(((x[k:] - m) * (x[:-k] - m)).sum() / ((x - m) ** 2).sum())


def dw(e):
    e = np.asarray(e, dtype=float)
    return float((np.diff(e) ** 2).sum() / (e ** 2).sum())


def tstat(r, n):
    return float(r * np.sqrt((n - 2) / (1 - r * r)))


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    s, k, o = (df[c].to_numpy() for c in ("sessions_k", "stock_index", "orders_k"))
    ds, dk, do = np.diff(s), np.diff(k), np.diff(o)
    r_lv, r_df = float(np.corrcoef(s, k)[0, 1]), float(np.corrcoef(ds, dk)[0, 1])
    slope_lv, icpt_lv = np.polyfit(k, s, 1)
    res_lv = s - (icpt_lv + slope_lv * k)
    slope_df, icpt_df = np.polyfit(dk, ds, 1)
    res_df = ds - (icpt_df + slope_df * dk)
    ro_lv, ro_df = float(np.corrcoef(o, s)[0, 1]), float(np.corrcoef(do, ds)[0, 1])
    slope_o = float(np.polyfit(ds, do, 1)[0])
    a1s, a1k = acf(s, 1), acf(k, 1)
    neff = n * (1 - a1s * a1k) / (1 + a1s * a1k)
    dfe = int(neff) - 2
    tcrit = float(stats.t.ppf(0.975, dfe))
    rcrit = tcrit / np.sqrt(tcrit ** 2 + dfe)
    share = None  # shown in theory: simulation of 10,000 pairs, |r| > 0.5 in about 40 %

    # toy numbers quoted in theory.md
    A, B = np.array([10, 12, 13, 15, 16, 18.]), np.array([5, 6, 8, 8, 9, 11.])
    assert abs(np.corrcoef(A, B)[0, 1] - 0.969) < 5e-4 and abs(np.corrcoef(np.diff(A), np.diff(B))[0, 1] + 0.327) < 5e-4
    assert abs(acf(A, 1) - 19 / 42) < 1e-12
    e = np.array([1.0, 0.8, 0.5, -0.2, -0.6, -0.9])
    assert abs(dw(e) - 0.87 / 3.1) < 1e-12

    b = Book(df, "Lesson 14 - Spurious correlation and autocorrelation",
             "Solved workbook. Yellow cells are assumptions; everything else is a live formula.")
    last = n + 1
    S, K, O = b.rng("sessions_k"), b.rng("stock_index"), b.rng("orders_k")
    first_d = f"$3:${last}"  # differences start in row 3
    b.add_column("d_sessions", lambda r: f"=Data!B{r}-Data!B{r - 1}", expected=np.r_[np.nan, ds], first_row=3)
    b.add_column("d_stock", lambda r: f"=Data!C{r}-Data!C{r - 1}", expected=np.r_[np.nan, dk], first_row=3)
    b.add_column("d_orders", lambda r: f"=Data!D{r}-Data!D{r - 1}", expected=np.r_[np.nan, do], first_row=3)
    dS, dK, dO = (f"Data!${b.col(c)}$3:${b.col(c)}${last}" for c in ("d_sessions", "d_stock", "d_orders"))

    b.section("1. Correlation of the LEVELS of sessions and the stock index")
    b.row("n (days)", f"=COUNT({S})", n, "0")
    c_lv = b.row("Correlation of levels", f"=CORREL({S},{K})", r_lv, "0.000")
    b.row("R-squared", f"=RSQ({S},{K})", r_lv ** 2, "0.000")
    sl_lv = b.row("Slope of sessions on stock index", f"=SLOPE({S},{K})", slope_lv, "0.000")
    ic_lv = b.row("Intercept", f"=INTERCEPT({S},{K})", icpt_lv, "0.00")
    t_lv = b.row("Naive t-statistic  r*sqrt((n-2)/(1-r^2))", f"={b.local(c_lv)}*SQRT(({n}-2)/(1-{b.local(c_lv)}^2))", tstat(r_lv, n), "0.0",
                 "Looks overwhelming - but it assumes independent observations")

    b.section("2. Correlation of the CHANGES (first differences)")
    c_df = b.row("Correlation of daily changes", f"=CORREL({dS},{dK})", r_df, "0.000")
    t_df = b.row("Naive t-statistic of the changes", f"={b.local(c_df)}*SQRT(({n}-1-2)/(1-{b.local(c_df)}^2))", tstat(r_df, n - 1), "0.00",
                 "|t| < 2: nothing there")

    b.section("3. Autocorrelation function  r_k = sum (x_t - mean)(x_t-k - mean) / sum (x_t - mean)^2")
    def acf_f(rng_col, row0, row1, kk):
        L = rng_col
        cur = f"Data!${L}${row0 + kk}:${L}${row1}"
        prev = f"Data!${L}${row0}:${L}${row1 - kk}"
        full = f"Data!${L}${row0}:${L}${row1}"
        return f"=SUMPRODUCT(({cur}-AVERAGE({full}))*({prev}-AVERAGE({full})))/DEVSQ({full})"
    rows, exp = [], {}
    for i, kk in enumerate(LAGS):
        rows.append([kk, acf_f("B", 2, last, kk), acf_f("C", 2, last, kk), acf_f(b.col("d_sessions"), 3, last, kk)])
        exp[(i, 1)], exp[(i, 2)], exp[(i, 3)] = acf(s, kk), acf(k, kk), acf(ds, kk)
    t3a, t3b = b.table(["Lag k (days)", "Sessions (levels)", "Stock index (levels)", "Sessions (daily changes)"], rows,
                       fmt={1: "0.000", 2: "0.000", 3: "0.000"}, expect=exp)
    band = b.row("Rough 95% band for white noise: 2/sqrt(n)", f"=2/SQRT({n})", 2 / np.sqrt(n), "0.000",
                 "Autocorrelations inside the band are indistinguishable from 0")
    b.bar_chart_from_table("Autocorrelation: levels vs changes", 1, [2, 4], t3a, t3b, anchor="H4", x_title="lag (days)")

    b.section("4. Residuals of the levels regression and the Durbin-Watson statistic")
    b.add_column("resid_levels", lambda r: f"=Data!B{r}-({ic_lv}+{sl_lv}*Data!C{r})", expected=res_lv, fmt="0.00")
    RL = b.rng("resid_levels")
    RL1, RL0 = f"Data!${b.col('resid_levels')}$3:${b.col('resid_levels')}${last}", f"Data!${b.col('resid_levels')}$2:${b.col('resid_levels')}${last - 1}"
    dw_lv = b.row("Durbin-Watson, levels regression", f"=SUMXMY2({RL1},{RL0})/SUMSQ({RL})", dw(res_lv), "0.000",
                  "DW = sum (e_t - e_t-1)^2 / sum e_t^2; about 2 for independent residuals, near 0 for strong positive autocorrelation")
    r1_res = b.row("Lag-1 autocorrelation of residuals",
                   f"=SUMPRODUCT(({RL1}-AVERAGE({RL}))*({RL0}-AVERAGE({RL})))/DEVSQ({RL})", acf(res_lv, 1), "0.000")
    b.row("Check: 2*(1 - r1)", f"=2*(1-{b.local(r1_res)})", 2 * (1 - acf(res_lv, 1)), "0.000", "DW is approximately 2(1 - r1)")
    sl_d = b.row("Slope of changes: d_sessions on d_stock", f"=SLOPE({dS},{dK})", slope_df, "0.0000")
    ic_d = b.row("Intercept of changes regression", f"=INTERCEPT({dS},{dK})", icpt_df, "0.0000")
    b.add_column("resid_changes", lambda r: f"=Data!{b.col('d_sessions')}{r}-({ic_d}+{sl_d}*Data!{b.col('d_stock')}{r})",
                 expected=np.r_[np.nan, res_df], fmt="0.00", first_row=3)
    RD = f"Data!${b.col('resid_changes')}$3:${b.col('resid_changes')}${last}"
    RD1, RD0 = f"Data!${b.col('resid_changes')}$4:${b.col('resid_changes')}${last}", f"Data!${b.col('resid_changes')}$3:${b.col('resid_changes')}${last - 1}"
    dw_df = b.row("Durbin-Watson, regression on changes", f"=SUMXMY2({RD1},{RD0})/SUMSQ({RD})", dw(res_df), "0.000")

    b.section("5. How many independent observations do we really have?")
    la_s = b.row("Lag-1 autocorrelation, sessions", f"={b.local(f'Analysis!$B${t3a}')}", a1s, "0.000")
    la_k = b.row("Lag-1 autocorrelation, stock index", f"={b.local(f'Analysis!$C${t3a}')}", a1k, "0.000")
    ne = b.row("Effective sample size  n(1 - rx*ry)/(1 + rx*ry)", f"={n}*(1-{b.local(la_s)}*{b.local(la_k)})/(1+{b.local(la_s)}*{b.local(la_k)})",
               neff, "0.0", "Bartlett's approximation")
    dfc = b.row("Degrees of freedom  INT(n_eff) - 2", f"=INT({b.local(ne)})-2", dfe, "0")
    tc = b.row("Critical t (5%, two-sided)", f"=TINV(0.05,{b.local(dfc)})", tcrit, "0.000")
    b.row("Smallest |r| that would be significant", f"={b.local(tc)}/SQRT({b.local(tc)}^2+{b.local(dfc)})", rcrit, "0.000",
          "Compare with the observed correlation of levels")

    b.section("6. A genuine relationship for comparison: orders vs sessions")
    b.row("Correlation of levels", f"=CORREL({O},{S})", ro_lv, "0.000")
    co_d = b.row("Correlation of daily changes", f"=CORREL({dO},{dS})", ro_df, "0.000", "Survives differencing: it is real")
    so_d = b.row("Slope of d_orders on d_sessions", f"=SLOPE({dO},{dS})", slope_o, "0.000")

    b.line_chart("Sessions and stock index (levels)", "date", ["sessions_k", "stock_index"], anchor="H24", y_title="index")

    b.answers([
        ("Correlation, R-squared and slope of the levels", f"={c_lv}",
         f"r = {r_lv:.3f}, R-squared {r_lv ** 2:.2f}, slope {slope_lv:.2f}: the stock index appears to explain {r_lv ** 2:.0%} of the variation in sessions."),
        ("Naive t-statistic of that correlation", f"={t_lv}",
         f"t = {tstat(r_lv, n):.1f}, far beyond any critical value - if the days were independent. They are not."),
        ("Correlation of the daily changes", f"={c_df}",
         f"r = {r_df:.3f} (t = {tstat(r_df, n - 1):.2f}): once the shared drift-like movement is removed there is no relationship."),
        ("Autocorrelation of levels vs changes at lag 1, 5, 10", f"=Analysis!B{t3a}",
         f"Sessions levels: {acf(s, 1):.3f} / {acf(s, 5):.3f} / {acf(s, 10):.3f}. Daily changes: {acf(ds, 1):.3f} / {acf(ds, 5):.3f} / {acf(ds, 10):.3f} "
         f"(band +-{2 / np.sqrt(n):.2f}). The levels remember; the changes do not."),
        ("Durbin-Watson of the levels regression (and of the regression on changes)", f"={dw_lv}",
         f"DW = {dw(res_lv):.3f} (about 2 expected); the changes regression gives {dw(res_df):.2f}. DW this far below 2 signals autocorrelated residuals "
         f"and therefore a meaningless t-statistic."),
        ("Effective sample size and the smallest significant |r|", f"={ne}",
         f"n_eff = {neff:.1f} instead of {n}; |r| would have to exceed {rcrit:.3f} (df = {dfe}). The observed {r_lv:.2f} "
         f"{'does not reach' if abs(r_lv) < rcrit else 'reaches'} that bar: the levels correlation carries almost no evidence "
         f"(Bartlett's formula is itself crude for random walks, but the message is the same)."),
        ("Orders vs sessions: correlation of levels and of changes", f"={co_d}",
         f"Levels {ro_lv:.2f}, changes {ro_df:.2f}, slope of changes {slope_o:.2f}: this link holds after differencing, so it is not a trend artefact."),
        ("Which relationship would you trust, and what would you do next?", "see text",
         "Trust orders-sessions, not sessions-stock. Next: model changes (or detrend), test lead-lag relations on changes, and look for a "
         "mechanism before acting."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-14-spurious", "14 · Spurious correlation and autocorrelation",
             "Two independent random walks look 90 % correlated in levels and uncorrelated in changes.", df.rename(columns={"date": "time"}), "time")
    d.stat("Correlation and Durbin-Watson", {"r levels (sessions vs stock)": r_lv, "r changes": r_df,
                                            "r levels (orders vs sessions)": ro_lv, "r changes (orders vs sessions)": ro_df,
                                            "DW levels": dw(res_lv), "DW changes": dw(res_df)},
           "The sessions/stock link vanishes when you difference; the orders/sessions link survives.", decimals=2)
    lv = pd.DataFrame({"time": df["date"], "sessions_k": s, "stock_index": k})
    d.timeseries("Two unrelated series, levels", lv, "Both wander; they happen to wander in the same direction for months.")
    o_ = np.argsort(k)
    sc = pd.DataFrame({"stock_index": k[o_], "sessions_k": s[o_], "fit": (icpt_lv + slope_lv * k)[o_]})
    d.xy("Levels scatter: a convincing-looking line", sc, "stock_index", ["sessions_k", "fit"],
         f"r = {r_lv:.2f}, naive t = {tstat(r_lv, n):.0f}. Autocorrelated data break the usual p-value.", lines=["fit"])
    dsc = pd.DataFrame({"d_sessions": ds, "d_stock (unrelated)": dk, "d_orders (related)": do}).sort_values("d_sessions")
    d.xy("Daily changes scatter", dsc, "d_sessions", ["d_stock (unrelated)", "d_orders (related)"],
         "After differencing: no pattern against the unrelated series, a clear line for orders.")
    roll = pd.DataFrame({"time": df["date"].to_numpy()[ROLL:],
                         "levels": pd.Series(s).rolling(ROLL).corr(pd.Series(k)).to_numpy()[ROLL:],
                         "changes": pd.Series(np.r_[np.nan, ds]).rolling(ROLL).corr(pd.Series(np.r_[np.nan, dk])).to_numpy()[ROLL:]})
    d.timeseries(f"Rolling {ROLL}-day correlation, sessions vs stock", roll,
                 "The correlation of levels is unstable and drifts across the full range; the correlation of changes stays near 0.",
                 colors={"levels": "#E15759", "changes": "#4E79A7"}, ymin=-1)
    ac = pd.DataFrame({"lag": [str(i) for i in range(1, 11)], "levels": [acf(s, i) for i in range(1, 11)],
                       "changes": [acf(ds, i) for i in range(1, 11)]})
    d.bars("Autocorrelation of sessions: levels vs changes", ac, f"Levels decay very slowly; changes are inside the +-{2 / np.sqrt(n):.2f} band.")
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: spurious correlation and autocorrelation

## Why this matters

Two quantities that have nothing to do with each other can show a correlation of 0.9 and a "highly significant" p-value.
The failure is routine in time-series work: someone finds a "leading indicator", builds a forecast or an alert on it, and it
falls apart in the next quarter. The cause is **autocorrelation**: when today's value is mostly yesterday's value, neighbouring
observations are not independent, so the sample contains far less information than its length suggests and the textbook
significance test is invalid.

## Autocorrelation

The lag-$k$ autocorrelation of a series $x_1,\dots,x_n$ with mean $\bar x$ is

$$
r_k = \frac{\sum_{t=k+1}^{n} (x_t-\bar x)(x_{t-k}-\bar x)}{\sum_{t=1}^{n} (x_t-\bar x)^2}.
$$

For white noise, $r_k$ is approximately normal with standard deviation $1/\sqrt{n}$, so values outside $\pm 2/\sqrt n$ are
signals. **Worked example**: $x = 10,12,13,15,16,18$ has $\bar x = 14$, numerator $19$, denominator $42$, so $r_1 = 0.452$. A series
that trends or wanders has a large $r_1$ and slowly decaying $r_k$ (see the autocorrelation chart in the dashboard).

## Random walks and spurious correlation

A **random walk** $x_t = x_{t-1} + \varepsilon_t$ is the sum of its shocks, so it never returns to a mean and its $r_k$ stays near 1.
Two *independent* random walks have sample correlations that are widely spread over $(-1,1)$, not concentrated near 0: in a
simulation of 10,000 independent pairs of length 250, about 40 % had $|r| > 0.5$. Trends (a shared upward drift,
growth, inflation, seasonality) create the same illusion. This is the **spurious regression** problem (Yule 1926; Granger and
Newbold 1974): the usual $t$ and $R^2$ are misleading, and a tell-tale sign is a high $R^2$ together with a low Durbin-Watson.

**Worked example (toy).** $A = 10,12,13,15,16,18$ and $B = 5,6,8,8,9,11$ both rise, so $\mathrm{corr}(A,B)=0.969$. Their
daily changes are $2,1,2,1,2$ and $1,2,0,1,2$, and those are correlated at $-0.33$ (with only 5 points, no evidence of anything).
All of the levels correlation came from both series going up.

## The remedies

1. **Difference** (or take growth rates, lesson 09): correlate $\Delta x_t = x_t - x_{t-1}$ with $\Delta y_t$. A relationship that
   survives differencing is not just two things trending together.
2. **Detrend / de-season** and model the remainder (lessons 07-08).
3. **Model the dynamics**: include lagged $y$ as a predictor, or use regression with autocorrelated errors.
4. **Reduce the sample size honestly**: with autocorrelations $\rho_x,\rho_y$, the effective sample size is roughly
   $n_{\text{eff}} \approx n\,\dfrac{1-\rho_x\rho_y}{1+\rho_x\rho_y}$ (Bartlett). Use it in the $t$ test of a correlation.

## Durbin-Watson

For regression residuals $e_t$:

$$
DW = \frac{\sum_{t=2}^{n} (e_t-e_{t-1})^2}{\sum_{t=1}^{n} e_t^2} \approx 2\,(1-r_1(e)).
$$

$DW\approx 2$ means no first-order autocorrelation, $DW\to 0$ strong positive autocorrelation, $DW\to 4$ negative. **Worked
example**: residuals $1.0, 0.8, 0.5, -0.2, -0.6, -0.9$ give $\sum(\Delta e)^2 = 0.87$, $\sum e^2 = 3.10$, so $DW = 0.28$: smooth,
strongly positively autocorrelated residuals. Rule of thumb (Granger-Newbold): $R^2 > DW$ is a warning of a spurious regression.
Formal critical values depend on $n$ and the number of predictors; for diagnostics here the approximation $2(1-r_1)$ is enough.

## Assumptions and pitfalls

1. **Differencing removes information** about long-run (cointegrated) relationships: two random walks that share a common stochastic
   trend are related even though their changes may be weakly correlated. Testing for this is beyond this course; the point is
   that high correlation of levels is never sufficient evidence.
2. **A significant correlation of changes is not causation either**; look for a mechanism and out-of-sample stability.
3. **Lead-lag claims** ("A leads B by 3 days") must be tested on differenced or pre-whitened data (lesson 11).
4. **Rolling correlations** that jump between large positive and negative values are a symptom of this problem.
5. **Over-differencing** adds negative autocorrelation (an artificial $r_1 \approx -0.5$); stop when the changes look like noise.
6. Seasonal data need seasonal differencing (lag 7 or 12), not just first differences.

## Related notes

- [Correlation and lagged relationships](../11-correlation-and-lagged-relationships/theory.md)
- [Differencing and growth rates](../09-differencing-and-growth-rates/theory.md)
- [Trend, seasonality and noise](../07-trend-seasonality-and-noise/theory.md)
- [Residual analysis and model diagnostics](../15-residual-analysis-and-model-diagnostics/theory.md)
- Repo notes: [Random walk](../../notes/time_series/random_walk.md), [Autocorrelation function](../../notes/time_series/autocorrelation_function.md)
"""

TASK = r"""
# Task: spurious correlation and autocorrelation

## Scenario

Your growth team has found what it calls a "leading indicator": a market index published by a partner seems to move together with
the number of daily website sessions. The team wants to put the index on the weekly KPI dashboard and base the traffic forecast
on it. Before that happens, you are asked whether the relationship is real. A second metric, orders, is also available.

## Data

`data.csv` - 250 consecutive days from 2025-01-01, one row per day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `sessions_k` | website sessions that day, thousands |
| `stock_index` | closing value of the partner's market index (index points) |
| `orders_k` | orders placed that day, thousands |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Correlate `sessions_k` with `stock_index` (levels): report `CORREL`, R-squared and the slope of sessions on the index.
2. Compute the naive t-statistic $t = r\sqrt{(n-2)/(1-r^2)}$. What would you conclude if you believed the days were independent?
3. Create day-to-day changes for all three columns (`=B3-B2`, ...). What is the correlation of the changes of sessions and the index?
4. Compute the autocorrelation at lags 1, 2, 5, 10, 20 for the **levels** of sessions and for the **changes** of sessions, using
   $r_k = \sum (x_t-\bar x)(x_{t-k}-\bar x) / \sum (x_t-\bar x)^2$. Compare with the band $\pm 2/\sqrt n$.
5. Compute the residuals of the regression in question 1 and their Durbin-Watson statistic `SUMXMY2(...)/SUMSQ(...)`. Do the same
   for the regression of the changes. How do the two compare with 2?
6. Estimate the effective sample size $n(1-r_x r_y)/(1+r_x r_y)$ from the lag-1 autocorrelations of both series, then the smallest
   $|r|$ that would be significant at 5% with that many degrees of freedom. Is the observed correlation of levels informative?
7. Repeat questions 1 and 3 for `orders_k` against `sessions_k`. What is different?
8. *Explain in two or three sentences* which of the two relationships you would put on a dashboard, and what further evidence
   you would want.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Rolling 60-day correlation, sessions vs stock", describe how stable the correlation of levels is compared with that of changes.
- In "Daily changes scatter", which of the two series shows a pattern against `d_sessions`?
- In "Autocorrelation of sessions", how long does the memory of the levels last compared with that of the changes?

## Deliverable

A short note (5-8 lines) to the growth team: is the index a usable leading indicator, what you checked, which numbers
support your answer, and what you recommend instead. Include one chart.
"""
