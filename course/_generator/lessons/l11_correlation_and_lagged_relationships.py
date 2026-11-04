"""Lesson 11 - Correlation and lagged relationships (Pearson vs Spearman, cross-correlation, lead/lag, confounding)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "11-correlation-and-lagged-relationships"
TITLE = "Correlation and lagged relationships"
MODULE = "Relationships and statistical models"
DATASET = "150 days of ad spend, new sign-ups (reacting to spend 3 days earlier) and newsletter opens (sharing only the weekday pattern)"
N = 150
LAG = 3  # true delay between spend and sign-ups
BOT = 100  # a bot-sign-up day (outlier), hidden in the task
MAXLAG = 10


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1115)
    pre = LAG
    u = np.zeros(N + pre)
    for i in range(1, N + pre):
        u[i] = 0.8 * u[i - 1] + rng.normal(0, 0.6)  # campaign intensity: persistent, so spend is autocorrelated
    spend_all = (2400 + 700 * u).round(-1)
    t = np.arange(N)
    wk = np.array([14, 12, 6, 2, -4, -16, -14], dtype=float)
    wk -= wk.mean()
    signups = 60 + 0.022 * (spend_all[:N] - 2400) + wk[t % 7] + rng.normal(0, 9, N)  # spend_all[:N] = spend LAG days earlier
    signups[BOT] += 140
    ow = np.array([90, 70, 30, 0, -20, -90, -80], dtype=float)
    ow -= ow.mean()
    opens = 900 + ow[t % 7] + rng.normal(0, 60, N)
    return pd.DataFrame({"date": pd.date_range("2026-01-05", periods=N, freq="D"), "ad_spend_usd": spend_all[pre:].astype(int),
                         "signups": signups.round(0).astype(int), "newsletter_opens": opens.round(0).astype(int)})


def fill(text: str, **kw) -> str:
    for k, v in kw.items():
        text = text.replace(f"@{k}@", str(v))
    return text


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    sp, sg, op = (df[c].to_numpy(float) for c in ["ad_spend_usd", "signups", "newsletter_opens"])
    cc = lambda a, b, k: float(np.corrcoef(a[:n - k], b[k:])[0, 1])
    ccf = [cc(sp, sg, k) for k in range(MAXLAG + 1)]  # spend leads signups by k
    rev = [cc(sg, sp, k) for k in range(MAXLAG + 1)]  # signups lead spend by k
    best = int(np.argmax(ccf))
    assert best == LAG
    r_best = ccf[best]
    xs, ys = sp[:n - best], sg[best:]
    rho = float(stats.spearmanr(xs, ys)[0])
    slope, icpt = np.polyfit(xs, ys, 1)
    wd = df["date"].dt.weekday.to_numpy()
    adj = lambda v: v - pd.Series(v).groupby(wd).transform("mean").to_numpy()
    r_open = float(np.corrcoef(op, sg)[0, 1])
    r_open_adj = float(np.corrcoef(adj(op), adj(sg))[0, 1])
    r_sp_open = float(np.corrcoef(sp, op)[0, 1])
    band = 2 / np.sqrt(n)
    big = int(np.argmax(sg))

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 11 - Correlation and lagged relationships",
             "Pearson and Spearman correlation, cross-correlation by lag, and a confounder (weekday).")
    S, G, O = b.rng("ad_spend_usd"), b.rng("signups"), b.rng("newsletter_opens")
    first = lambda name: f"Data!${b.col(name)}$2"
    last = n + 1

    b.section("1. Correlation on the same day (lag 0)")
    r0 = b.row("Pearson: ad spend vs sign-ups", f"=CORREL({S},{G})", ccf[0], "0.000")
    r_o = b.row("Pearson: newsletter opens vs sign-ups", f"=CORREL({O},{G})", r_open, "0.000")
    b.row("Pearson: ad spend vs newsletter opens", f"=CORREL({S},{O})", r_sp_open, "0.000")
    b.row("Rough noise band for |r| (2 / sqrt(n))", f"=2/SQRT(COUNT({G}))", band, "0.000", "valid only if the series have no memory")

    b.section("2. Cross-correlation: does spend today relate to sign-ups k days later?")
    c0 = b.next_row + 1
    rows, exp = [], {}
    for k in range(MAXLAG + 1):
        r = c0 + k
        rows.append([k,
                     f"=CORREL(OFFSET({first('ad_spend_usd')},0,0,{n}-A{r},1),OFFSET({first('signups')},A{r},0,{n}-A{r},1))",
                     f"=CORREL(OFFSET({first('signups')},0,0,{n}-A{r},1),OFFSET({first('ad_spend_usd')},A{r},0,{n}-A{r},1))",
                     f"=2/SQRT({n}-A{r})"])
        exp.update({(k, 1): ccf[k], (k, 2): rev[k], (k, 3): 2 / np.sqrt(n - k)})
    c0_, c1_ = b.table(["Lag k (days)", "r(spend_t, signups_t+k)", "r(signups_t, spend_t+k)", "noise band"], rows,
                       fmt={1: "0.000", 2: "0.000", 3: "0.000"}, expect=exp)
    assert c0_ == c0
    lag = b.row("Lag with the highest correlation (spend leads sign-ups)", f"=INDEX(A{c0}:A{c1_},MATCH(MAX(B{c0}:B{c1_}),B{c0}:B{c1_},0))",
                best, "0", "days")
    peak = b.row("Correlation at that lag", f"=MAX(B{c0}:B{c1_})", r_best, "0.000")
    rv = b.row("Highest correlation in the reverse direction (k >= 1)", f"=MAX(C{c0 + 1}:C{c1_})", max(rev[1:]), "0.000",
               "sign-ups today do not predict later spend")
    b.line_chart_from_table("Cross-correlation by lag", 1, [2, 3], c0, c1_, anchor="H4", x_title="lag (days)", y_title="r")

    L = b.local(lag)
    lagabs = lag  # absolute reference to the chosen lag, used by Data formulas
    b.add_column("weekday", lambda r: f"=WEEKDAY(A{r},2)", expected=wd + 1, fmt="0")
    # E weekday
    lagged = pd.Series(sp).shift(best).to_numpy()
    pair = np.where(np.arange(n) >= best, sg, np.nan)
    rx = np.full(n, np.nan)
    ry = np.full(n, np.nan)
    rx[best:] = stats.rankdata(lagged[best:])
    ry[best:] = stats.rankdata(pair[best:])
    cols = [("spend_lagged", lambda r: f'=IF(ROW()-2<{lagabs},"",OFFSET(B{r},-{lagabs},0))', lagged, "#,##0"),
            ("signups_pair", lambda r: f'=IF(ROW()-2<{lagabs},"",C{r})', pair, "0")]
    for nm, fn, ex, fm in cols:
        b.add_column(nm, fn, expected=ex, fmt=fm)
        j = list(b._cols).index(nm) + 1
        for r in range(2, n + 2):
            if b.data.cell(row=r, column=j).value is None:
                b.data.cell(row=r, column=j, value=fn(r)).number_format = fm
    # F spend_lagged, G signups_pair
    rkf = lambda col: (lambda r: f'=IF(ISNUMBER({col}{r}),COUNTIF(${col}$2:${col}${last},"<"&{col}{r})+(COUNTIF(${col}$2:${col}${last},{col}{r})+1)/2,"")')
    for nm, col, ex in [("rank_spend_lagged", "F", rx), ("rank_signups_pair", "G", ry)]:
        fn = rkf(col)
        b.add_column(nm, fn, expected=ex, fmt="0.0")
        j = list(b._cols).index(nm) + 1
        for r in range(2, n + 2):
            if b.data.cell(row=r, column=j).value is None:
                b.data.cell(row=r, column=j, value=fn(r)).number_format = "0.0"
    # H rank_spend_lagged, I rank_signups_pair
    b.add_column("signups_adj", lambda r: f"=C{r}-AVERAGEIF({b.rng('weekday')},E{r},{G})", expected=adj(sg), fmt="0.0")
    b.add_column("opens_adj", lambda r: f"=D{r}-AVERAGEIF({b.rng('weekday')},E{r},{O})", expected=adj(op), fmt="0.0")
    # J signups_adj, K opens_adj
    reg = lambda col: f"OFFSET(Data!${col}$2,{L},0,{n}-{L},1)"

    b.section("3. Pearson vs Spearman at the best lag")
    pe = b.row("Pearson at that lag", f"=CORREL({reg('F')},{reg('G')})", r_best, "0.000")
    sr = b.row("Spearman at that lag (Pearson of the ranks)", f"=CORREL({reg('H')},{reg('I')})", rho, "0.000")
    b.row("Spearman minus Pearson", f"={b.local(sr)}-{b.local(pe)}", rho - r_best, "0.000", "positive: an outlier is weighing down Pearson")
    b.row("Largest number of sign-ups in one day", f"=MAX({G})", float(sg.max()), "0")
    b.row("Date of the largest number", f"=INDEX(Data!$A$2:$A${last},MATCH(MAX({G}),{G},0))", None, "yyyy-mm-dd")
    b.row("Mean sign-ups per day", f"=AVERAGE({G})", float(sg.mean()), "0.0")

    b.section("4. Size of the lagged effect")
    sl = b.row("Slope: extra sign-ups per extra USD of spend 3 days earlier", f"=SLOPE({reg('G')},{reg('F')})", slope, "0.00000")
    per1000 = b.row("Extra sign-ups per extra 1,000 USD", f"=1000*{b.local(sl)}", 1000 * slope, "0.00")
    b.row("Intercept", f"=INTERCEPT({reg('G')},{reg('F')})", icpt, "0.0")

    b.section("5. A confounder: the weekday")
    adjr = b.row("Pearson: newsletter opens vs sign-ups after removing weekday means", f"=CORREL({b.rng('opens_adj')},{b.rng('signups_adj')})",
                 r_open_adj, "0.000")
    b.row("Raw Pearson: opens vs sign-ups (from section 1)", f"={b.local(r_o)}", r_open, "0.000")

    b.scatter_chart("Sign-ups vs ad spend 3 days earlier", "spend_lagged", ["signups_pair"], anchor="H22",
                    x_title="ad spend, k days earlier (USD)", y_title="sign-ups", first=2 + best)

    b.answers([
        ("Pearson correlation of ad spend and sign-ups on the same day", f"={r0}",
         f"r = {ccf[0]:.3f}: moderate and positive, but the real link is delayed, so the same-day value understates it. "
         f"Noise band about +/-{band:.2f}."),
        ("Cross-correlation for lags 0 to 10: which lag is highest?", f"={lag}",
         f"Lag {best} days (r = {r_best:.2f}); neighbours at lag {best - 1} ({ccf[best - 1]:.2f}) and lag {best + 1} ({ccf[best + 1]:.2f}) "
         f"are also high because spend is autocorrelated, so the whole hump is evidence for one delay, not for three."),
        ("Highest correlation in the reverse direction (sign-ups leading spend)", f"={rv}",
         f"At most {max(rev[1:]):.2f} for k>=1 versus {r_best:.2f} forward: the asymmetry says spend comes first (the reverse "
         f"values at small lags still carry the autocorrelation of spend)."),
        ("Pearson vs Spearman at the best lag; the date of the largest sign-up day", f"={sr}",
         f"Pearson {r_best:.3f}, Spearman {rho:.3f}. The largest day ({int(sg[big])} sign-ups on {df['date'][big]:%Y-%m-%d}, against a mean of "
         f"{sg.mean():.0f}) pulls Pearson down; Spearman uses ranks only."),
        ("Extra sign-ups per extra 1,000 USD of spend three days earlier", f"={per1000}",
         f"{1000 * slope:.1f} sign-ups per 1,000 USD (slope {slope:.4f}); this is a description of co-movement, interpreted as an effect "
         f"only if nothing else changed along with spend."),
        ("Newsletter opens vs sign-ups: raw correlation and after removing weekday means", f"={adjr}",
         f"Raw r = {r_open:.2f}, after removing the weekday average of both columns r = {r_open_adj:.2f}. Both series fall on weekends; "
         f"the weekday is a common driver, so opens did not cause sign-ups."),
        ("Why are lags 2 and 4 also high?", "see note",
         "Ad spend is autocorrelated (campaigns last several days), so spend on neighbouring days is almost the same series shifted by one. "
         "A cross-correlation hump of width 3-5 is normal; the peak, not each lag, carries the information."),
        ("Interpretation: what does the lead-lag result prove?", "see note",
         "That spend precedes sign-ups with a delay of about three days and that the relation is monotone and strong. It does not prove "
         "causation: a campaign calendar, seasonality or a third variable could move both. Evidence would need an experiment (holdout "
         "regions or randomised spend) or a convincing adjustment."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-11-correlation-lag", "11 · Correlation and lagged relationships",
             "Spend leads sign-ups by three days: lag profile, Pearson vs Spearman and a weekday confounder.",
             df.rename(columns={"date": "time"}), "time")
    d.stat("Correlation summary", {"r same day": ccf[0], "best lag (days)": best, "r at best lag": r_best, "Spearman at best lag": rho,
                                   "opens vs sign-ups (raw)": r_open, "opens vs sign-ups (weekday-adjusted)": r_open_adj},
           "Spend vs sign-ups, and the newsletter opens that only share the weekday pattern.", decimals=2)
    zs = lambda v: (v - v.mean()) / v.std()
    sps = pd.Series(zs(sp)).shift(best).to_numpy()
    ts = pd.DataFrame({"time": df["date"], "sign-ups (z)": zs(sg), "ad spend (z)": zs(sp), f"ad spend shifted {best} days (z)": sps})
    d.timeseries("Standardised sign-ups and ad spend", ts, "Shifting spend forward by three days makes its peaks line up with the sign-up peaks. "
                 "Standardised = (value - mean) / SD, so both fit one axis.", dashed=["ad spend (z)"], w=24, h=9,
                 colors={"sign-ups (z)": "#4E79A7", "ad spend (z)": "#B8C0CC", f"ad spend shifted {best} days (z)": "#F28E2B"})
    cd = pd.DataFrame({"lag (days)": [f"lag {k}" for k in range(MAXLAG + 1)], "spend leads sign-ups": np.round(ccf, 3),
                       "sign-ups lead spend": np.round(rev, 3)})
    d.bars("Cross-correlation by lag", cd, f"Noise band is about +/-{band:.2f}. A single peak at a positive lag in one direction only.", w=12)
    fit = icpt + slope * xs
    x3 = pd.DataFrame({"ad spend 3 days earlier (USD)": xs, "sign-ups": ys, "linear fit": fit})
    d.xy("Sign-ups vs spend three days earlier", x3, "ad spend 3 days earlier (USD)", ["sign-ups", "linear fit"],
         "The single high point is the bot day; it pulls the line up and Pearson down.", lines=["linear fit"], w=12)
    x0 = pd.DataFrame({"ad spend same day (USD)": sp, "sign-ups": sg})
    d.xy("Sign-ups vs spend on the same day", x0, "ad spend same day (USD)", ["sign-ups"], "Same data, wrong alignment: a loose cloud.", w=12)
    xo = pd.DataFrame({"newsletter opens": op, "sign-ups": sg})
    d.xy("Newsletter opens vs sign-ups (a confounded pair)", xo, "newsletter opens", ["sign-ups"],
         "Positive correlation with no causal link: both are higher on weekdays. The weekday-adjusted correlation is near zero.", w=12)
    d.save(out)

    # ------------------------------------------------------------------ markdown
    tx, ty = np.array([1, 2, 3, 4, 5.0]), np.array([2, 4, 5, 7, 40.0])
    ex = dict(tp=f"{np.corrcoef(tx, ty)[0, 1]:.3f}", ts=f"{stats.spearmanr(tx, ty)[0]:.3f}", r0=f"{ccf[0]:.2f}", rb=f"{r_best:.2f}",
              band=f"{band:.2f}", b=best, ro=f"{r_open:.2f}", roa=f"{r_open_adj:.2f}", rho=f"{rho:.2f}", sl=f"{1000 * slope:.1f}",
              r2=f"{ccf[2]:.2f}", r4=f"{ccf[4]:.2f}", rrev=f"{max(rev[1:]):.2f}", rp=f"{r_best:.2f}")
    md(out / "theory.md", fill(THEORY, **ex))
    md(out / "task.md", fill(TASK, first=df["date"].iloc[0].strftime("%Y-%m-%d"), last=df["date"].iloc[-1].strftime("%Y-%m-%d")))
    return b


THEORY = r"""
# Theory: correlation and lagged relationships

## What a correlation tells you, and what it does not

Two business series that rise and fall together invite a causal story: "ad spend drives sign-ups". A correlation coefficient
is the first quantitative test of such a story, but it answers a narrow question - *how closely do two variables follow a
straight line (or a monotone curve) together?* - and it is easily fooled by outliers, by timing (the effect arrives later) and by
a third variable that moves both. This lesson separates those cases.

## Pearson correlation

For paired observations $(x_i, y_i)$, $i=1..n$:

$$
r = \frac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum_i (x_i-\bar x)^2}\,\sqrt{\sum_i (y_i-\bar y)^2}}
= \frac{\operatorname{Cov}(x,y)}{s_x s_y}, \qquad -1 \le r \le 1 .
$$

It is the covariance rescaled by both standard deviations, hence unit-free. $r^2$ is the share of the variance of $y$ explained by
the best straight line on $x$ ([lesson 12](../12-linear-and-nonlinear-regression/theory.md)). $r = 0$ does not mean "no relationship": a perfect
parabola can give $r=0$. Spreadsheet function: `CORREL`.

## Spearman rank correlation

Replace each value by its rank (ties get the average rank) and compute Pearson on the ranks. Spearman measures how well the
relationship is a **monotone** curve and ignores how far an extreme value lies from the others.

Example: $x = (1,2,3,4,5)$, $y = (2,4,5,7,40)$. Pearson is @tp@ - the single large value dominates - while Spearman is
@ts@, because $y$ increases whenever $x$ does. If your data have outliers or a skewed scale, report both; a gap between them
is itself a finding.

## Lagged relationships and the cross-correlation function

When one series acts on another with a delay, the same-day correlation is the wrong alignment. The **cross-correlation at lag $k$**
pairs $x_t$ with $y_{t+k}$:

$$
r_k = \operatorname{corr}(x_t,\ y_{t+k}),\qquad t = 1, \dots, n-k .
$$

- If $r_k$ peaks at $k>0$, $x$ **leads** $y$ by $k$ periods; a peak at $k<0$ means $y$ leads $x$. Compute both directions: a
  peak on one side only is the signature of a lead.
- Each lag uses $n-k$ pairs, so large lags rest on fewer data.
- The usual "noise band" $\pm 2/\sqrt{n}$ holds only if the series have no memory. For autocorrelated series (most business
  data), raw cross-correlations are inflated and have wide humps; the standard remedy is to remove each series' own
  dynamics first (prewhitening, [lesson 14](../14-spurious-correlation-and-autocorrelation/theory.md)).

### Worked example (from `data.csv`)

Ad spend and sign-ups on the same day: $r = @r0@$. Shifting spend forward by @b@ days gives $r_{@b@} = @rb@$ (Spearman @rho@).
The neighbouring lags are also high ($r_2 = @r2@$, $r_4 = @r4@$) because campaigns last several days, so spend on adjacent
days is nearly the same series; the lead is read from the *peak*. In the other direction (sign-ups leading spend) the highest
value for $k\ge1$ is @rrev@. The regression slope at that lag is about @sl@ extra sign-ups per extra 1,000 USD of spend three
days earlier, with a caveat in the next section.

## Correlation is not causation

A lead is *necessary* for causation (effects do not precede causes) but not *sufficient*:

1. **Common driver (confounder).** Newsletter opens and sign-ups have $r = @ro@$ in the data, but both are lower on weekends. After
   subtracting each weekday's average from both columns the correlation is @roa@. Neither causes the other.
2. **Common trend or seasonality.** Two trending series are strongly correlated whatever their relation
   ([lesson 14](../14-spurious-correlation-and-autocorrelation/theory.md)). Remove trend and season, or difference
   ([lesson 09](../09-differencing-and-growth-rates/theory.md)), before correlating.
3. **Reverse or feedback causality.** Budgets are often set after a good week; check the other direction and the timing.
4. **Selection and coincidence.** Scanning many lags or many variables will find some $|r|$ above the noise band.

Causal claims need an experiment, a natural experiment or a model that controls the other drivers
([lesson 13](../13-multiple-regression-and-confounding/theory.md); [A/B tests](../19-a-b-testing-and-effect-sizes/theory.md)).

## Assumptions and pitfalls

- **Linearity (Pearson).** Always plot first; a curve, a cluster or two groups can give any $r$. Spearman needs monotonicity.
- **Outliers.** One bot day lowers Pearson in `data.csv`; see the gap to Spearman.
- **Restricted range** (only high-spend days) shrinks $r$; a mix of groups can create or reverse it
  ([lesson 05](../05-sampling-bias-and-simpson-s-paradox/theory.md)).
- **Significance is not strength.** With 150 days, $|r| > @band@$ is "significant", yet $r = 0.2$ explains 4 % of the variance.
- **Aggregation level matters.** Daily and weekly correlations differ ([lesson 06](../06-time-aggregation-and-sampling-frequency/theory.md)).
- **Lead time can vary.** A fixed lag model misses a delay that changes by season or campaign.

## Where this leads

Regression quantifies a relationship ([lesson 12](../12-linear-and-nonlinear-regression/theory.md)); multiple regression
controls a confounder ([lesson 13](../13-multiple-regression-and-confounding/theory.md)); dynamic regression uses the lagged
predictor for forecasting. Background: [correlation](../../notes/joint_distributions_and_covariance/correlation.md),
[covariance](../../notes/joint_distributions_and_covariance/covariance.md),
[autocorrelation function](../../notes/time_series/autocorrelation_function.md),
[dynamic regression](../../notes/time_series/dynamic_regression.md).
"""

TASK = r"""
# Task: correlation and lagged relationships

## Scenario

You work in growth analytics. Marketing spends on paid ads and believes "ads bring sign-ups right away"; the same-day numbers
do not show it clearly, so the budget owner wants to cut the ads. A product manager adds that the **newsletter** must be
working too, because newsletter opens and sign-ups "move together". You have 150 days of data and must decide when and whether
spend relates to sign-ups, what the newsletter relationship really is, and how much of it you can claim as cause.

## Data

`data.csv` - 150 consecutive days from @first@ (a Monday) to @last@; one row = one day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `ad_spend_usd` | paid-ad spend that day (USD) |
| `signups` | new accounts created that day (count) |
| `newsletter_opens` | number of newsletter e-mails opened that day (count) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the Pearson correlation of `ad_spend_usd` and `signups` **on the same day**. Compare with the rough noise band
   $2/\sqrt{n}$.
2. Compute the **cross-correlation** $r_k = \operatorname{corr}(\text{spend}_t, \text{signups}_{t+k})$ for $k = 0,\dots,10$. Which lag is highest?
   Why are the neighbouring lags high as well?
3. Compute the reverse direction, $\operatorname{corr}(\text{signups}_t, \text{spend}_{t+k})$, for $k = 1,\dots,10$. What does the comparison say?
4. At the best lag compute **Pearson** and **Spearman** correlation (Spearman = Pearson of the ranks; ties get average ranks). Find the day with
   the most sign-ups and say what it does to the two coefficients.
5. Fit a line of sign-ups on spend (at the best lag). How many extra sign-ups per extra 1,000 USD?
6. Compute the correlation of `newsletter_opens` and `signups`. Then subtract each weekday's average from both columns and correlate again.
   What changes, and what does it mean?
7. Explain in two sentences why the profile in question 2 has a wide hump instead of one spike.
8. *Interpretation:* what can you conclude about ads and about the newsletter, and what would you need to claim that ads *cause* sign-ups?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- On "Standardised sign-ups and ad spend", which curve do the sign-up peaks follow, and by how many days is it late?
- On "Cross-correlation by lag", why do the two bar series look different?
- Compare the three scatter plots: which alignment gives a tight cloud, and which point does not fit?

## Deliverable

A short note (6-8 lines) to the budget owner with named parts: **Timing** (the lag and how sure you are), **Strength** (correlation
and extra sign-ups per 1,000 USD), **Newsletter** (why the correlation is not an effect) and **Caveat** (what correlation cannot tell you).
"""
