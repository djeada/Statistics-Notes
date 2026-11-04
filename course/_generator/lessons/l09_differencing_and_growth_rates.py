"""Lesson 09 - Differencing and growth rates (monthly revenue, exponential growth + seasonality)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "09-differencing-and-growth-rates"
TITLE = "Differencing and growth rates"
MODULE = "Understanding time series"
DATASET = "72 months of subscription revenue (USD), compounding growth with a yearly pattern and one outage month"
N = 72
DIP = 41  # outage month (index)
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(909)
    t = np.arange(N)
    seas = np.array([-0.05, -0.035, -0.01, 0.0, 0.01, 0.0, -0.02, -0.03, 0.0, 0.015, 0.04, 0.06])
    seas -= seas.mean()
    walk = np.cumsum(rng.normal(0, 0.014, N))  # persistent level shocks (what makes the series a random walk plus drift)
    logx = np.log(82000) + 0.0165 * t + walk + seas[t % 12] + rng.normal(0, 0.010, N)
    logx[DIP] += np.log(0.80)  # outage: a fifth of revenue lost for one month, then back
    return pd.DataFrame({"month": pd.date_range("2020-01-01", periods=N, freq="MS"), "revenue_usd": np.exp(logx).round(0).astype(int)})


def fill(text: str, **kw) -> str:
    for k, v in kw.items():
        text = text.replace(f"@{k}@", str(v))
    return text


def acf1(a):
    a = np.asarray(a, dtype=float)
    a = a[~np.isnan(a)]
    return float(np.corrcoef(a[1:], a[:-1])[0, 1])


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    x = df["revenue_usd"].astype(float)
    d1 = x.diff()
    pct = x.pct_change()
    lr = np.log(x).diff()
    sd12 = x.diff(12)
    yoy = x / x.shift(12) - 1
    lyoy = np.log(x).diff(12)
    mon = df["month"].dt.month
    H = 36  # first half = first 36 months
    cagr = float((x.iloc[-1] / x.iloc[0]) ** (12 / (n - 1)) - 1)
    ann_mean_lr = float(np.exp(12 * lr.mean()) - 1)
    ann_mean_pct = float((1 + pct.mean()) ** 12 - 1)
    dip_i = int(pct.idxmin())

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 09 - Differencing and growth rates",
             "Changes instead of levels: first difference, percent change, log return, seasonal difference, CAGR.")
    R = b.rng("revenue_usd")
    b.add_column("diff_1", lambda r: f"=B{r}-B{r - 1}", expected=d1, fmt="#,##0")
    b.add_column("pct_change", lambda r: f"=B{r}/B{r - 1}-1", expected=pct, fmt="0.00%")
    b.add_column("log_return", lambda r: f"=LN(B{r}/B{r - 1})", expected=lr, fmt="0.0000")
    b.add_column("seasonal_diff_12", lambda r: f"=B{r}-B{r - 12}", expected=sd12, fmt="#,##0")
    b.add_column("yoy_pct", lambda r: f"=B{r}/B{r - 12}-1", expected=yoy, fmt="0.0%")
    b.add_column("log_yoy", lambda r: f"=LN(B{r})-LN(B{r - 12})", expected=lyoy, fmt="0.0000")
    b.add_column("month_no", lambda r: f"=MONTH(A{r})", expected=mon, fmt="0")
    D1, PC, LR, SD, YY, LY, MN = (b.rng(c) for c in ["diff_1", "pct_change", "log_return", "seasonal_diff_12", "yoy_pct",
                                                      "log_yoy", "month_no"])
    MON = f"Data!$A$2:$A${n + 1}"
    last = n + 1

    b.section("1. First differences and growth rates")
    m_d = b.row("Mean monthly change (USD)", f"=AVERAGE({D1})", d1.mean(), "#,##0")
    b.row("SD of monthly change (USD)", f"=STDEV({D1})", d1.std(), "#,##0")
    m_p = b.row("Mean monthly percent change", f"=AVERAGE({PC})", pct.mean(), "0.000%")
    b.row("SD of monthly percent change", f"=STDEV({PC})", pct.std(), "0.000%")
    m_l = b.row("Mean monthly log return", f"=AVERAGE({LR})", lr.mean(), "0.00000")
    b.row("SD of monthly log return", f"=STDEV({LR})", lr.std(), "0.00000")

    b.section("2. The outage month")
    worst = b.row("Worst monthly percent change", f"=MIN({PC})", pct.min(), "0.0%")
    b.row("Month of the worst change", f"=INDEX({MON},MATCH(MIN({PC}),{PC},0))", None, "yyyy-mm")
    b.row("Log return in the worst month", f"=LN(1+{b.local(worst)})", lr.iloc[dip_i], "0.0000", "ln(1 + simple return)")
    b.row("Percent change the month after", f"=INDEX({PC},MATCH(MIN({PC}),{PC},0)+1)", pct.iloc[dip_i + 1], "0.0%")
    b.row("Product of the two: (1 + r1)(1 + r2) - 1", f"=(1+{b.local(worst)})*(1+INDEX({PC},MATCH(MIN({PC}),{PC},0)+1))-1",
          (1 + pct.iloc[dip_i]) * (1 + pct.iloc[dip_i + 1]) - 1, "0.0%", "after a -25% month a +25% month does not restore the level")

    b.section("3. Growth over the whole period")
    c1 = b.row("CAGR from first to last month (annual)", f"=(Data!B{last}/Data!B2)^(12/({n}-1))-1", cagr, "0.00%")
    b.row("Annual growth from the mean log return", f"=EXP(12*{b.local(m_l)})-1", ann_mean_lr, "0.00%", "identical to CAGR")
    b.row("Compounding the mean percent change: (1 + mean r)^12 - 1", f"=(1+{b.local(m_p)})^12-1", ann_mean_pct, "0.00%", "overstates: arithmetic mean > geometric mean")
    b.row("Sum of log returns = ln(last / first)", f"=SUM({LR})", float(np.log(x.iloc[-1] / x.iloc[0])), "0.0000")
    b.row("ln(last / first)", f"=LN(Data!B{last}/Data!B2)", float(np.log(x.iloc[-1] / x.iloc[0])), "0.0000")

    b.section("4. Year-over-year (seasonal difference of lag 12)")
    b.row("12-month change in USD, last month", f"=Data!F{last}", sd12.iloc[-1], "#,##0")
    yl = b.row("Year-over-year growth, last month", f"=Data!G{last}", yoy.iloc[-1], "0.0%")
    b.row("Average year-over-year growth, last 12 months", f"=AVERAGE(Data!G{last - 11}:G{last})", yoy.iloc[-12:].mean(), "0.0%")
    b.row("Months with a positive 12-month change", f'=COUNTIF({SD},">0")/COUNT({SD})', float((sd12.dropna() > 0).mean()), "0%")

    b.section("5. Is the series stable over time? First 36 months vs last 36 months (median and IQR: robust to the outage month)")
    series = [("revenue level (USD)", "revenue_usd", x), ("first difference (USD)", "diff_1", d1),
              ("percent change", "pct_change", pct), ("log return", "log_return", lr),
              ("12-month log growth", "log_yoy", lyoy)]
    rows, exp = [], {}
    for i, (lab, col, s) in enumerate(series):
        L = b.col(col)
        a = f"Data!${L}$2:${L}${H + 1}"
        z = f"Data!${L}${H + 2}:${L}${n + 1}"
        s1, s2 = s.iloc[:H].dropna(), s.iloc[H:].dropna()
        rows.append([lab, f"=MEDIAN({a})", f"=MEDIAN({z})", f"=QUARTILE({a},3)-QUARTILE({a},1)",
                     f"=QUARTILE({z},3)-QUARTILE({z},1)", f"=E{b.next_row + 1 + i}/D{b.next_row + 1 + i}"])
        exp.update({(i, 1): s1.median(), (i, 2): s2.median(), (i, 3): iqr(s1), (i, 4): iqr(s2), (i, 5): iqr(s2) / iqr(s1)})
    h0, h1 = b.table(["Series", "Median, first 36", "Median, last 36", "IQR, first 36", "IQR, last 36", "IQR ratio last/first"], rows,
                     fmt={1: "0.0000", 2: "0.0000", 3: "0.0000", 4: "0.0000", 5: "0.00"}, expect=exp)
    # level / first difference have values in the 1e3-1e5 range: format them as integers (display only)
    for r in (h0, h0 + 1):
        for c in range(2, 6):
            b.an.cell(row=r, column=c).number_format = "#,##0"

    b.section("6. Dependence left after each transformation (lag-1 and lag-12 autocorrelation)")
    xr = lambda col, a, z: f"Data!${b.col(col)}${a}:${b.col(col)}${z}"
    ac_level = b.row("lag-1 autocorrelation, revenue level", f"=CORREL({xr('revenue_usd', 3, last)},{xr('revenue_usd', 2, last - 1)})",
                     acf1(x), "0.000")
    ac_lr = b.row("lag-1 autocorrelation, log return", f"=CORREL({xr('log_return', 4, last)},{xr('log_return', 3, last - 1)})",
                  acf1(lr), "0.000")
    ac_lr12 = b.row("lag-12 autocorrelation, log return",
                    f"=CORREL({xr('log_return', 15, last)},{xr('log_return', 3, last - 12)})",
                    float(np.corrcoef(lr.iloc[13:], lr.iloc[1:-12])[0, 1]), "0.000", "the yearly pattern is still there")
    ac_ly = b.row("lag-1 autocorrelation, 12-month log growth", f"=CORREL({xr('log_yoy', 15, last)},{xr('log_yoy', 14, last - 1)})",
                  acf1(lyoy), "0.000", "overlapping 12-month windows share 11 months")

    b.section("7. Seasonality in the growth rate: average log return by calendar month")
    rows, exp = [], {}
    avg_m = lr.groupby(mon).mean()
    r0 = b.next_row
    for k in range(12):
        rows.append([MONTHS[k], f"=AVERAGEIF({MN},{k + 1},{LR})"])
        exp[(k, 1)] = avg_m[k + 1]
    m0, m1 = b.table(["Calendar month", "Average log return"], rows, fmt={1: "0.0000"}, expect=exp)
    b.bar_chart_from_table("Average monthly log return by calendar month", 1, [2], m0, m1, anchor="J4", y_title="log return")
    b.line_chart("Revenue (USD)", "month", ["revenue_usd"], anchor="J22", y_title="USD")

    best_m, worst_m = int(avg_m.idxmax()), int(avg_m.idxmin())
    b.answers([
        ("Mean and SD of the first difference; why is the USD change hard to compare over time?", f"={m_d}",
         f"Mean {d1.mean():,.0f} USD/month, SD {d1.std():,.0f}. The spread (IQR) of the USD change is {series_ratio(d1, H):.2f}x larger in the second half "
         f"because the business is bigger, not because it is riskier."),
        ("Mean percent change, worst month and the rebound that follows", f"={worst}",
         f"Mean {pct.mean():.2%}/month. Worst month {df['month'][dip_i]:%Y-%m}: {pct.iloc[dip_i]:.1%}; next month {pct.iloc[dip_i + 1]:+.1%} - "
         f"a {abs(pct.iloc[dip_i]):.0%} drop needs a {abs(pct.iloc[dip_i]) / (1 - abs(pct.iloc[dip_i])):.0%} rise to recover."),
        ("Mean and SD of log returns; log return in the worst month", f"={m_l}",
         f"Mean {lr.mean():.4f}, SD {lr.std():.4f}; worst month {lr.iloc[dip_i]:.3f} vs simple {pct.iloc[dip_i]:.3f}: logs are symmetric "
         f"(a +x then -x log return returns to the start), simple returns are not."),
        ("CAGR three ways", f"={c1}",
         f"CAGR {cagr:.2%} per year; exp(12 x mean log return) - 1 gives the same {ann_mean_lr:.2%}; compounding the mean percent change, (1 + mean r)^12 - 1, gives "
         f"{ann_mean_pct:.2%}, which overstates it (the arithmetic mean of growth rates exceeds the geometric mean)."),
        ("Year-over-year growth, last month and last-12-month average", f"={yl}",
         f"Last month {yoy.iloc[-1]:.1%} above the same month a year ago; average over the last 12 months {yoy.iloc[-12:].mean():.1%}. "
         "Seasonal differencing compares like with like, so no seasonal adjustment is needed."),
        ("Which transformation gives a stable median and spread across the two halves?", f"=Analysis!F{h0 + 3}",
         f"IQR ratios (last/first 36 months): level {series_ratio(x, H):.2f}, first difference {series_ratio(d1, H):.2f}, percent change "
         f"{series_ratio(pct, H):.2f}, log return {series_ratio(lr, H):.2f}. Percent changes and log returns stay close to 1; the level and "
         "the USD difference do not."),
        ("Best and worst calendar month for growth", f"=Analysis!B{m0 + best_m - 1}",
         f"{MONTHS[best_m - 1]} grows fastest ({avg_m[best_m]:+.3f}), {MONTHS[worst_m - 1]} slowest ({avg_m[worst_m]:+.3f}): a yearly seasonal pattern."),
        ("Autocorrelation of level, log return, lag 12 of log return, 12-month growth", f"={ac_level}",
         f"Level {acf1(x):.3f}, log return {acf1(lr):.3f}, log return at lag 12 {float(np.corrcoef(lr.iloc[13:], lr.iloc[1:-12])[0, 1]):.3f}, "
         f"12-month growth {acf1(lyoy):.3f}. Differencing removes the trend memory; seasonality and the overlap of 12-month windows leave some."),
        ("Interpretation: when is differencing wrong or risky?", "see note",
         "Differencing a series that is already stationary adds noise (over-differencing) and a negative lag-1 correlation; differencing "
         "discards the level, so you cannot answer level questions (how much revenue?) from changes alone; percent changes break near zero "
         "or for negative values."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-09-differencing-growth", "09 · Differencing and growth rates",
             "Levels grow, growth rates are stable: first difference, log return and year-over-year growth of monthly revenue.",
             df.rename(columns={"month": "time"}), "time")
    d.stat("Growth summary", {"CAGR (%)": cagr * 100, "mean monthly log return (%)": lr.mean() * 100,
                              "YoY growth, last month (%)": yoy.iloc[-1] * 100, "worst month (%)": pct.min() * 100,
                              "lag-1 autocorr. level": acf1(x), "lag-1 autocorr. log return": acf1(lr)},
           "CAGR = (last/first)^(12/(n-1)) - 1; the percent entries are in %.", decimals=2)
    d.timeseries("Revenue (USD): the level", pd.DataFrame({"time": df["month"], "revenue_usd": x}),
                 "Trending, growing swings: neither mean nor variance is constant.", unit="currencyUSD", colors={"revenue_usd": "#4E79A7"}, w=12)
    d.timeseries("Monthly change in USD (first difference)", pd.DataFrame({"time": df["month"], "diff_1": d1}),
                 "Removes the trend but the swings grow with the business.", unit="currencyUSD", bars=["diff_1"],
                 colors={"diff_1": "#F28E2B"}, w=12)
    g = pd.DataFrame({"time": df["month"], "monthly log return": lr * 100, "12-month log growth": lyoy * 100})
    d.timeseries("Monthly log return vs 12-month growth (%)", g, "Monthly returns keep the yearly pattern and the outage; the 12-month "
                 "growth has no yearly pattern (the outage shows up twice: when it happens and 12 months later).", unit="percent", colors={"monthly log return": "#E15759", "12-month log growth": "#59A14F"}, w=12)
    d.bars("Average monthly log return by calendar month (%)", pd.DataFrame({"month": MONTHS, "avg log return (%)": (avg_m.to_numpy() * 100).round(2)}),
           "Seasonality of growth: strong year-end, weak January.", w=12)
    tb = pd.DataFrame({"series": [s[0] for s in series],
                       "IQR first 36": [round(iqr(s[2].iloc[:H].dropna()), 4) for s in series],
                       "IQR last 36": [round(iqr(s[2].iloc[H:].dropna()), 4) for s in series],
                       "ratio": [round(series_ratio(s[2], H), 2) for s in series]})
    d.table("Stability check: spread (IQR) in the first vs last 36 months", tb, "A ratio near 1 means the spread does not depend on the level.", w=24, h=8)
    d.save(out)

    # ------------------------------------------------------------------ markdown
    ex = dict(cagr=f"{cagr:.2%}", cagr_m=f"{(x.iloc[-1] / x.iloc[0]):.3f}", first=f"{int(x.iloc[0]):,}", lastv=f"{int(x.iloc[-1]):,}",
              yrs=f"{(n - 1) / 12:.2f}", mlr=f"{lr.mean():.5f}", ann=f"{ann_mean_lr:.2%}", ap=f"{ann_mean_pct:.2%}",
              dipm=f"{df['month'][dip_i]:%B %Y}", dp=f"{pct.iloc[dip_i]:.1%}", dl=f"{lr.iloc[dip_i]:.3f}",
              up=f"{abs(pct.iloc[dip_i]) / (1 - abs(pct.iloc[dip_i])):.1%}", rl=f"{series_ratio(x, H):.2f}", rd=f"{series_ratio(d1, H):.2f}",
              rp=f"{series_ratio(pct, H):.2f}", rlr=f"{series_ratio(lr, H):.2f}", a1=f"{acf1(x):.3f}", a2=f"{acf1(lr):.3f}")
    md(out / "theory.md", fill(THEORY, **ex))
    md(out / "task.md", fill(TASK, claim=f"{round(float(d1.mean()), -2):,.0f}", first=df["month"].iloc[0].strftime("%Y-%m"), last=df["month"].iloc[-1].strftime("%Y-%m")))
    return b


def iqr(s):
    return float(np.percentile(s, 75) - np.percentile(s, 25))


def series_ratio(s, H):
    """IQR ratio last 36 / first 36 months (robust spread, so the single outage month does not decide the answer)."""
    return iqr(s.iloc[H:].dropna()) / iqr(s.iloc[:H].dropna())


THEORY = r"""
# Theory: differencing and growth rates

## Why look at changes instead of levels

A revenue curve that climbs for six years looks like a story but is a poor object for statistics: its mean depends on
*when* you look, its swings grow with its size, and each value is almost determined by the previous one. Averages,
correlations and control limits computed on such a **level** series are unreliable. The remedy is to model the *change*
from one period to the next, in the form that makes the change comparable across time: a difference, a percent change or
a log return. This is also how growth is reported - "up 18 % on last year" is a seasonal percent change.

## The transformations

For a positive series $x_t$:

| name | formula | use |
|---|---|---|
| first difference | $\Delta x_t = x_t - x_{t-1}$ | absolute change; removes a *linear* trend |
| simple (percent) change | $r_t = x_t/x_{t-1} - 1$ | relative change; what people quote |
| log return | $g_t = \ln(x_t/x_{t-1}) = \ln(1+r_t)$ | relative change that **adds up** over time |
| seasonal difference | $x_t - x_{t-m}$ | change from the same period last cycle ($m=12$ for months) |
| year-over-year growth | $x_t/x_{t-12}-1$ | seasonal percent change |

**Simple vs log.** For small changes $\ln(1+r) \approx r$ ($r = 0.02$ gives $0.0198$), but for large changes they differ:
a $-25\,\%$ month has $g = \ln 0.75 = -0.288$. Log returns are **additive** over time,
$\sum_{t=1}^{n} g_t = \ln(x_n/x_0)$, and symmetric ($+x$ then $-x$ in logs returns to the start). Simple returns compound
multiplicatively: $+50\,\%$ followed by $-50\,\%$ is $1.5 \times 0.5 - 1 = -25\,\%$, not $0$. Use simple changes to
communicate, log returns to compute with.

## Compound annual growth rate

$$
\mathrm{CAGR} = \left(\frac{x_n}{x_0}\right)^{\frac{12}{n}} - 1 \quad (n \text{ months between first and last observation}),
$$

and because the log returns telescope, $\mathrm{CAGR} = \exp\bigl(12\,\bar g\bigr) - 1$ where $\bar g$ is the mean monthly log
return. The shortcut $(1+\bar r)^{12}-1$ built from the *arithmetic* mean percent change overstates compound growth (the arithmetic mean of growth
rates always exceeds the geometric mean), and the gap grows with volatility.

### Worked example (from `data.csv`)

Revenue goes from @first@ USD to @lastv@ USD over @yrs@ years (71 months), a ratio of @cagr_m@. CAGR =
$@cagr_m@^{12/71} - 1$ = @cagr@. The mean monthly log return is @mlr@, so $\exp(12 \cdot @mlr@) - 1$ = @ann@, the same
number, while $(1+\bar r)^{12}-1$ = @ap@. In the outage month (@dipm@) revenue changed by @dp@, i.e. a log return of @dl@; a rise of
@up@ is needed to get back to where it was.

## Differencing to make a series stationary

A **stationary** series has a mean, variance and dependence structure that do not drift
([notes](../../notes/time_series/stationarity.md)). Trends break it. Differencing is the cheapest repair:

- A linear trend plus noise becomes noise around a constant after one first difference.
- A **random walk** $x_t = x_{t-1} + e_t$ becomes plain white noise $e_t$.
- Exponential growth becomes stationary only after **taking logs first**, then differencing: $\Delta \ln x_t$.
- A seasonal pattern of period $m$ is removed by the seasonal difference $x_t - x_{t-m}$; trend and season together
  often need both (the seasonal difference of the first difference).

How to check: compare location and spread (median and IQR, which one outlier cannot distort) of the first and second half.
In `data.csv` the IQR in the last 36 months relative to the first 36 is
@rl@ for the level, @rd@ for the USD difference, @rp@ for the percent change and @rlr@ for the log return: only the
relative measures stay close to 1. The lag-1 autocorrelation drops from @a1@ for the level to @a2@ for the log return (negative, because every difference adds the noise of two months and the outage month enters twice).

## Assumptions and pitfalls

1. **Over-differencing.** Differencing white noise multiplies its variance by 2 and creates a lag-1 autocorrelation of
   $-0.5$. If the differenced series has a strongly negative lag-1 autocorrelation, you went too far.
2. **Information is lost.** Differences carry no level. Forecast the change and add it back
   ([lesson 22](../22-trend-and-seasonal-regression-forecasting/theory.md)).
3. **Percent change near zero or with negative values** explodes or is meaningless; use the difference instead.
4. **Seasonality survives first differencing** (see the autocorrelation at lag 12 in the workbook); use the seasonal difference
   or [decompose first](../07-trend-seasonality-and-noise/theory.md).
5. **Noise is amplified.** A difference of two noisy values has twice the noise variance; smoothing first
   ([lesson 08](../08-moving-averages-and-exponential-smoothing/theory.md)) or using longer spans reduces it.
6. **Overlapping windows.** 12-month growth computed every month shares 11 months with its neighbour, so it is strongly
   autocorrelated by construction; do not treat the points as independent.
7. **Single outliers appear twice**: a one-month dip creates a big negative change and a big positive change next month.

## Where this leads

Rolling windows of these changes are in [lesson 10](../10-rolling-statistics/theory.md); autocorrelation of a differenced
series and spurious correlation between trending series in [lesson 14](../14-spurious-correlation-and-autocorrelation/theory.md);
ARIMA formalises the "I" (integrated) as differencing ([notes](../../notes/time_series/arima_models.md),
[random walks](../../notes/time_series/random_walk.md)).
"""

TASK = r"""
# Task: differencing and growth rates

## Scenario

You are the finance analyst of a subscription software company. The CFO's board slide says "revenue grows about
@claim@ USD more every month" and the growth plan assumes it will continue. An operations manager objects: the company
is much bigger than it was, the 'steady' monthly change cannot have stayed the same, and one month "looks like an
accident". You have monthly revenue for six years and have to compute growth correctly and decide which view of the data
is safe to use for further statistics.

## Data

`data.csv` - 72 monthly observations from @first@ to @last@; one row = one calendar month.

| column | meaning |
|---|---|
| `month` | first day of the month |
| `revenue_usd` | recognised subscription revenue in the month (USD) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the **first difference** (USD change from the previous month). What are its mean and SD? Is the SD the same in
   the first and the second half of the data?
2. Compute the **percent change**. What are its mean and SD, which month is the worst, and what happens in the month after it?
3. Compute the **log return** $\ln(x_t/x_{t-1})$. Mean and SD? Compare the log return and the percent change in the worst month and say which
   one is symmetric.
4. Compute the **CAGR** from the first to the last month, in three ways: from the ratio, from the mean log return, and as
   compounding the mean percent change, $(1+\bar r)^{12}-1$. Which one is biased and why?
5. Compute the **seasonal difference** (lag 12) and the **year-over-year growth**. What was the growth in the last month and the
   average over the last 12 months?
6. Compare median and IQR for the first 36 and the last 36 months, for the level, the first difference, the percent change, the log
   return and the 12-month log growth. Which series are stable over time?
7. Average the log return by calendar month. Which months grow fastest and slowest?
8. Compute the lag-1 autocorrelation of the level, of the log return and of the 12-month log growth, and the lag-12
   autocorrelation of the log return. What dependence is left after each transformation?
9. *Interpretation:* is the board's statement "revenue grows @claim@ USD every month" supported? Give one risk of using
   percent changes and one risk of differencing.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- Compare "Revenue (USD): the level" with "Monthly change in USD": what is still not constant after one difference?
- On "Monthly log return vs 12-month growth", what does each line remove and what does it keep?
- Which calendar months stand out in the bar chart, and is that visible in the level chart?

## Deliverable

A short memo (6-8 lines) to the CFO with named parts: **Growth rate** (CAGR and latest year-over-year, with the formula
you used), **Why not USD per month** (evidence from the two halves), **The unusual month** (date, size, effect on the level)
and **Caveat** (one limitation).
"""
