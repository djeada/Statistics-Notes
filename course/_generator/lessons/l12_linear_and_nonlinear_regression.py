"""Lesson 12 - Linear and nonlinear regression."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "12-linear-and-nonlinear-regression"
TITLE = "Linear and nonlinear regression"
MODULE = "Relationships and statistical models"
DATASET = "120 weekly observations of advertising spend (k$) and sales (units); spend grows over time"
N_TRAIN = 96  # first 96 weeks fit the model, last 24 weeks are the holdout
PLANNED = 80.0  # planned spend (k$) for the extrapolation question


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1212)
    n = 120
    spend = np.clip(np.linspace(6, 58, n) + rng.normal(0, 4, n), 3, None).round(1)
    sales = (250 + 420 * np.log(spend) + rng.normal(0, 90, n)).round(0)
    week = pd.date_range("2024-01-01", periods=n, freq="7D")
    return pd.DataFrame({"week": week, "ad_spend_k": spend, "sales_units": sales})


def ols(x, y):
    r = sm.OLS(y, sm.add_constant(x)).fit()
    return float(r.params[1]), float(r.params[0]), float(r.rsquared), float(np.sqrt(r.scale))


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    x, y = df["ad_spend_k"].to_numpy(), df["sales_units"].to_numpy()
    lx = np.log(x)
    n = len(df)
    s1, i1, r1, se1 = ols(x, y)
    s2, i2, r2, se2 = ols(lx, y)
    res1, res2 = y - (i1 + s1 * x), y - (i2 + s2 * lx)

    # toy numbers quoted in theory.md
    tx, ty = np.array([1, 2, 3, 4, 5.]), np.array([3, 5, 4, 7, 9.])
    assert np.allclose(np.polyfit(tx, ty, 1), [1.4, 1.4]) and abs(ols(tx, ty)[2] - 0.8448) < 5e-5
    ux, uy = np.array([1, 2, 4, 8, 16.]), np.array([10, 16, 22, 28, 34.])
    assert np.allclose(np.polyfit(ux, uy, 1), [1.4516, 13.0], atol=1e-3) and abs(ols(ux, uy)[2] - 0.8710) < 5e-4

    b = Book(df, "Lesson 12 - Linear and nonlinear regression",
             "Solved workbook. Yellow cells are assumptions; everything else is a live formula.")
    X, Y = b.rng("ad_spend_k"), b.rng("sales_units")
    last = n + 1
    ntr = N_TRAIN + 1  # last Excel row of the training block
    b.add_column("ln_spend", lambda r: f"=LN(Data!B{r})", expected=lx, fmt="0.0000")
    LX = b.rng("ln_spend")

    b.section("1. Straight line  sales = a + b * spend")
    cnt = b.row("n (weeks)", f"=COUNT({Y})", n, "0")
    sl1 = b.row("Slope b (units per k$)", f"=SLOPE({Y},{X})", s1, "0.000")
    ic1 = b.row("Intercept a (units)", f"=INTERCEPT({Y},{X})", i1, "0.0")
    rs1 = b.row("R-squared", f"=RSQ({Y},{X})", r1, "0.0000")
    st1 = b.row("Residual standard error (units)", f"=STEYX({Y},{X})", se1, "0.0", "STEYX: sqrt(SSE/(n-2))")
    nxt = b.row("Planned spend (k$)", PLANNED, None, "0.0", "Edit me", is_input=True)
    p40 = b.row("Line: predicted sales at 40 k$", f"={b.local(ic1)}+{b.local(sl1)}*40", i1 + s1 * 40, "0.0")
    p80 = b.row("Line: predicted sales at planned spend", f"={b.local(ic1)}+{b.local(sl1)}*{b.local(nxt)}",
                i1 + s1 * PLANNED, "0.0")
    b.add_column("fit_line", lambda r: f"={ic1}+{sl1}*Data!B{r}", expected=i1 + s1 * x, fmt="0.0")
    b.add_column("resid_line", lambda r: f"=Data!C{r}-Data!{b.col('fit_line')}{r}", expected=res1, fmt="0.0")

    b.section("2. Transform and refit  sales = c + d * ln(spend)")
    sl2 = b.row("Slope d (units per unit of ln spend)", f"=SLOPE({Y},{LX})", s2, "0.00")
    ic2 = b.row("Intercept c (units)", f"=INTERCEPT({Y},{LX})", i2, "0.0")
    rs2 = b.row("R-squared", f"=RSQ({Y},{LX})", r2, "0.0000")
    st2 = b.row("Residual standard error (units)", f"=STEYX({Y},{LX})", se2, "0.0")
    q80 = b.row("Log model: predicted sales at planned spend", f"={b.local(ic2)}+{b.local(sl2)}*LN({b.local(nxt)})",
                i2 + s2 * np.log(PLANNED), "0.0")
    b.row("Line minus log model at planned spend (units)", f"={b.local(p80)}-{b.local(q80)}",
          (i1 + s1 * PLANNED) - (i2 + s2 * np.log(PLANNED)), "0.0", "How far the line over-promises")
    b.add_column("fit_log", lambda r: f"={ic2}+{sl2}*Data!{b.col('ln_spend')}{r}", expected=i2 + s2 * lx, fmt="0.0")
    b.add_column("resid_log", lambda r: f"=Data!C{r}-Data!{b.col('fit_log')}{r}", expected=res2, fmt="0.0")

    b.section("3. Where does each model miss?  Mean residual by spend third")
    q33, q67 = np.percentile(x, [100 / 3, 200 / 3])
    c33 = b.row("Lower third boundary (k$)", f"=PERCENTILE({X},1/3)", q33, "0.00")
    c67 = b.row("Upper third boundary (k$)", f"=PERCENTILE({X},2/3)", q67, "0.00")
    RL, RG = b.rng("resid_line"), b.rng("resid_log")
    lo, hi = x < q33, x >= q67
    mid = ~lo & ~hi
    rows = [["low spend", f'=AVERAGEIFS({RL},{X},"<"&{b.local(c33)})', f'=AVERAGEIFS({RG},{X},"<"&{b.local(c33)})'],
            ["middle", f'=AVERAGEIFS({RL},{X},">="&{b.local(c33)},{X},"<"&{b.local(c67)})',
             f'=AVERAGEIFS({RG},{X},">="&{b.local(c33)},{X},"<"&{b.local(c67)})'],
            ["high spend", f'=AVERAGEIFS({RL},{X},">="&{b.local(c67)})', f'=AVERAGEIFS({RG},{X},">="&{b.local(c67)})']]
    exp = {}
    for i, m in enumerate([lo, mid, hi]):
        exp[(i, 1)], exp[(i, 2)] = res1[m].mean(), res2[m].mean()
    t3, _ = b.table(["Spend range", "Mean residual: line", "Mean residual: log"], rows, fmt={1: "0.0", 2: "0.0"}, expect=exp)

    b.section(f"4. Holdout test: fit on the first {N_TRAIN} weeks, score the last {n - N_TRAIN}")
    Xt, Yt, Lt = (f"Data!$B$2:$B${ntr}", f"Data!$C$2:$C${ntr}", f"Data!${b.col('ln_spend')}$2:${b.col('ln_spend')}${ntr}")
    Xh, Yh, Lh = (f"Data!$B${ntr + 1}:$B${last}", f"Data!$C${ntr + 1}:$C${last}",
                  f"Data!${b.col('ln_spend')}${ntr + 1}:${b.col('ln_spend')}${last}")
    ts1, ti1, _, _ = ols(x[:N_TRAIN], y[:N_TRAIN])
    ts2, ti2, _, _ = ols(lx[:N_TRAIN], y[:N_TRAIN])
    tsl = b.row("Line, training slope", f"=SLOPE({Yt},{Xt})", ts1, "0.000")
    til = b.row("Line, training intercept", f"=INTERCEPT({Yt},{Xt})", ti1, "0.0")
    tsg = b.row("Log model, training slope", f"=SLOPE({Yt},{Lt})", ts2, "0.00")
    tig = b.row("Log model, training intercept", f"=INTERCEPT({Yt},{Lt})", ti2, "0.0")
    nh = n - N_TRAIN
    e1 = y[N_TRAIN:] - (ti1 + ts1 * x[N_TRAIN:])
    e2 = y[N_TRAIN:] - (ti2 + ts2 * lx[N_TRAIN:])
    rm1 = b.row("Holdout RMSE: line (units)",
                f"=SQRT(SUMPRODUCT(({Yh}-({b.local(til)}+{b.local(tsl)}*{Xh}))^2)/{nh})", float(np.sqrt((e1 ** 2).mean())), "0.0")
    rm2 = b.row("Holdout RMSE: log model (units)",
                f"=SQRT(SUMPRODUCT(({Yh}-({b.local(tig)}+{b.local(tsg)}*{Lh}))^2)/{nh})", float(np.sqrt((e2 ** 2).mean())), "0.0")
    b.row("Holdout mean error: line (units)", f"=SUMPRODUCT({Yh}-({b.local(til)}+{b.local(tsl)}*{Xh}))/{nh}",
          float(e1.mean()), "0.0", "Negative = the line over-predicts")

    b.section("5. What does one more k$ buy?  Marginal sales per k$")
    marg = {}
    for sp in (10, 30, 50):
        marg[sp] = b.row(f"Log model at {sp} k$ (units per k$) = d / spend", f"={b.local(sl2)}/{sp}", s2 / sp, "0.00")
    b.row("Line (units per k$), same everywhere", f"={b.local(sl1)}", s1, "0.00")

    b.scatter_chart("Sales vs ad spend: line and log fit", "ad_spend_k", ["sales_units", "fit_line", "fit_log"],
                    anchor="F4", x_title="Ad spend (k$)", y_title="Sales (units)", lines=["fit_line", "fit_log"])

    b.answers([
        ("Slope of the straight-line fit (units per k$)", f"={sl1}",
         f"Slope {s1:.2f}, intercept {i1:.0f}, R-squared {r1:.3f}: each extra k$ is associated with {s1:.1f} extra units."),
        ("Predicted sales at 40 k$ from the line", f"={p40}",
         f"{i1 + s1 * 40:.0f} units. R-squared {r1:.2f} looks respectable, which is exactly why you must still look at residuals."),
        ("Mean residual of the line in the low / middle / high spend third", f"=Analysis!B{t3}",
         f"{res1[lo].mean():+.0f} / {res1[mid].mean():+.0f} / {res1[hi].mean():+.0f} units: negative, positive, negative is an "
         f"arch, the signature of a concave relationship that a straight line cannot follow."),
        ("Slope and R-squared of the ln(spend) model", f"={sl2}",
         f"d = {s2:.1f} units per unit of ln(spend), R-squared {r2:.3f} (line: {r1:.3f}). Doubling spend adds d*ln 2 = {s2 * np.log(2):.0f} units at any level."),
        ("Residual standard error: line vs log model", f"={st2}",
         f"{se1:.0f} vs {se2:.0f} units: the log model's typical miss is {1 - se2 / se1:.0%} smaller."),
        ("Holdout RMSE of line and of log model", f"={rm2}",
         f"Line {np.sqrt((e1 ** 2).mean()):.0f} vs log {np.sqrt((e2 ** 2).mean()):.0f} units on the 24 highest-spend weeks; the line over-predicts by "
         f"{-e1.mean():.0f} units on average because it never saturates."),
        (f"Predicted sales at {PLANNED:.0f} k$: line vs log model", f"={q80}",
         f"Log model {i2 + s2 * np.log(PLANNED):.0f}, line {i1 + s1 * PLANNED:.0f} units. {PLANNED:.0f} k$ is above every observed spend (max {x.max():.0f}), so both are extrapolations."),
        ("Marginal units per extra k$ at 10 and at 50 k$ (log model)", f"={marg[10]}",
         f"{s2 / 10:.1f} at 10 k$ vs {s2 / 50:.1f} at 50 k$; the line says {s1:.1f} everywhere, so it is wrong at both ends in opposite directions."),
        ("Limitation of the fitted curve", "see text",
         "The log curve fits the observed range and the story (diminishing returns) but keeps growing without bound, spend and time are "
         "entangled here (spend rose steadily), and association is not proof that ads cause sales."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-12-regression", "12 · Linear and nonlinear regression",
             "Line vs ln(spend) fit: scatter, residuals, holdout error and marginal return.",
             df.iloc[N_TRAIN:].rename(columns={"week": "time"}), "time")
    d.stat("Fit quality", {"R2 line": r1, "R2 log": r2, "resid SE line": se1, "resid SE log": se2,
                           "holdout RMSE line": float(np.sqrt((e1 ** 2).mean())),
                           "holdout RMSE log": float(np.sqrt((e2 ** 2).mean()))},
           "R-squared and typical errors (units) for the two models.", decimals=2)
    o = np.argsort(x)
    sc = pd.DataFrame({"ad_spend_k": x[o], "sales": y[o], "line_fit": (i1 + s1 * x)[o], "log_fit": (i2 + s2 * lx)[o]})
    d.xy("Sales vs ad spend with both fits", sc, "ad_spend_k", ["sales", "line_fit", "log_fit"],
         "Dots: weekly sales. The straight line sits above the dots at both ends and below them in the middle; the log curve follows the cloud.",
         lines=["line_fit", "log_fit"])
    rs = pd.DataFrame({"ad_spend_k": x[o], "resid_line": res1[o], "resid_log": res2[o]})
    d.xy("Residuals vs ad spend", rs, "ad_spend_k", ["resid_line", "resid_log"],
         "Line residuals form an arch (curvature); log-model residuals are a patternless band around 0.")
    h = df.iloc[N_TRAIN:]
    ho = pd.DataFrame({"time": h["week"].to_numpy(), "actual": y[N_TRAIN:], "line_pred": ti1 + ts1 * x[N_TRAIN:],
                       "log_pred": ti2 + ts2 * lx[N_TRAIN:]})
    d.timeseries("Holdout weeks: actual vs predictions", ho,
                 "Models fitted on the first 96 weeks only. The line drifts above the data as spend rises.",
                 points=["actual"], dashed=["line_pred", "log_pred"], colors={"actual": "#4E79A7", "line_pred": "#E15759", "log_pred": "#59A14F"})
    mg = pd.DataFrame({"ad_spend_k": [f"{s} k$" for s in (10, 20, 30, 40, 50)], "line": [s1] * 5,
                       "log_model": [s2 / s for s in (10, 20, 30, 40, 50)]})
    d.bars("Marginal sales per extra k$", mg, "The log model: returns shrink as spend rises. The line assumes a constant return.")
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK.format(planned=f"{PLANNED:.0f}", ntr=N_TRAIN, nh=n - N_TRAIN))
    return b


THEORY = r"""
# Theory: linear and nonlinear regression

## Why this matters

A fitted line always exists, and its R-squared is often high enough to look convincing. The failure this lesson prevents is
trusting a straight line in a world that bends: you then misjudge the effect at the ends of the range, and a budget
decision based on the slope (or on a forecast beyond the data) is wrong in a predictable direction. The skill is to fit
a simple model, ask what it gets wrong, and change the *shape* of the model when the evidence says so.

## Simple linear regression

Given pairs $(x_i, y_i)$, ordinary least squares (OLS) chooses $a$ and $b$ to minimise the sum of squared residuals
$e_i = y_i - a - b x_i$:

$$
b = \frac{\sum (x_i - \bar x)(y_i - \bar y)}{\sum (x_i - \bar x)^2} = r\,\frac{s_y}{s_x},\qquad a = \bar y - b\,\bar x .
$$

The slope is the **average change in $y$ per unit of $x$ across the sample**; the line passes through $(\bar x, \bar y)$.
Spreadsheet functions: `SLOPE(y, x)`, `INTERCEPT(y, x)`, `RSQ(y, x)`, `STEYX(y, x)` and `FORECAST(x0, y, x)`.

**Worked example.** $x = 1,2,3,4,5$ and $y = 3,5,4,7,9$. Then $\bar x = 3$, $\bar y = 5.6$,
$\sum (x-\bar x)(y-\bar y) = 14$, $\sum (x-\bar x)^2 = 10$, so $b = 1.4$ and $a = 5.6 - 1.4\cdot 3 = 1.4$. The residuals are
$0.2, 0.8, -1.6, 0, 0.6$ with $SSE = 3.6$; $SST = \sum (y-\bar y)^2 = 23.2$.

## R-squared and the residual standard error

$$
R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{3.6}{23.2} = 0.845,\qquad s_e = \sqrt{\frac{SSE}{n-2}} = \sqrt{\frac{3.6}{3}} = 1.10 .
$$

$R^2$ is the share of the variance of $y$ explained by the line; with one predictor it equals $r^2$. $s_e$ is the typical
miss **in the units of $y$**, which is usually the more useful number. R-squared compares models only when they have the
same $y$ (for instance, you cannot compare the $R^2$ of a model for $y$ with that of a model for $\ln y$).

## When a line is wrong

Many business relationships **saturate**: the first dollar of advertising, the first server, the first hour of training
buys a lot, and later ones buy less. A straight line forces the same return everywhere. Warning signs:

- the scatter plot visibly bends;
- residuals plotted against $x$ are not a patternless band but a U or an arch (lesson 15 develops this);
- the model fits the middle of the data but misses both ends, or predicts impossible values outside the range.

## Fixing it with a transformation

A model can be **nonlinear in $x$ and still linear in its parameters**, so OLS still applies after transforming the variable:

$$
y = c + d\,\ln x \qquad (\text{logarithmic}),\qquad
\ln y = c + d\,\ln x \qquad (\text{power law / elasticity}),\qquad
y = c + d\,x + g\,x^2 \qquad (\text{quadratic}).
$$

Create the transformed column (`=LN(x)`) and use the same `SLOPE` / `INTERCEPT`. For the log model the marginal effect is
$dy/dx = d/x$: it falls as $x$ grows, and doubling $x$ always adds $d\ln 2$ to $y$.

**Worked example.** $x = 1,2,4,8,16$ and $y = 10,16,22,28,34$ (every doubling adds 6). The straight line gives
$y = 13 + 1.45x$ with $R^2 = 0.871$, which looks fine, yet the residuals (actual minus fitted) run $-4.5, +0.1, +3.2, +3.4, -2.2$ (an arch) and
the line predicts $59.5$ at $x = 32$. Regressing on $\ln x$ recovers $y = 10 + 8.66\ln x$ with $R^2 = 1$, which predicts $40$.

## Comparing the fits honestly

1. **Residual plot and residual standard error** on the data used for fitting.
2. **Holdout error**: fit on the earlier part, compute $RMSE=\sqrt{\tfrac1m\sum (y_i-\hat y_i)^2}$ on the later part. A flexible
   model can always lower in-sample error; only the holdout (lesson 24) tells you if it generalises.
3. **Plausibility**: does the shape make sense (diminishing returns, no negative sales)?

## Assumptions and pitfalls

1. **Extrapolation.** Neither model is validated outside the observed range. A log curve is still increasing forever;
   real saturation has a ceiling, and the right answer at twice the observed spend is "we do not know".
2. **Over-fitting by flexibility.** A degree-8 polynomial gets a higher $R^2$ and worse forecasts. Prefer the simplest curve
   that matches the mechanism.
3. **R-squared is not a verdict.** A high $R^2$ can coexist with a systematically wrong shape.
4. **Transforming $y$ changes the question.** Back-transforming a fit of $\ln y$ predicts a median, not a mean, and
   changes how errors are weighted.
5. **Association is not causation.** Here spend rises over time, so anything else that grows with time (seasonality, brand
   awareness) is entangled with spend; lesson 13 deals with that.

## Related notes

- [Correlation and lagged relationships](../11-correlation-and-lagged-relationships/theory.md)
- [Multiple regression and confounding](../13-multiple-regression-and-confounding/theory.md)
- [Residual analysis and model diagnostics](../15-residual-analysis-and-model-diagnostics/theory.md)
- [Backtesting and forecast accuracy](../24-backtesting-and-forecast-accuracy/theory.md)
- Repo note: [Simple linear regression](../../notes/regression/simple_linear_regression.md)
"""

TASK = r"""
# Task: linear and nonlinear regression

## Scenario

You are the marketing analyst for an online retailer. Over the last 120 weeks the weekly advertising budget has been raised
steadily, and sales have grown with it. The head of marketing wants to approve **{planned} k$ per week** next quarter and
asks you: "What does one more thousand dollars of advertising buy us, and what will we sell at {planned} k$?" A colleague
has already fitted a straight line through the data and reports its R-squared as proof that "sales grow linearly with spend".

## Data

`data.csv` - 120 rows, one per week (2024-01-01 onwards).

| column | meaning |
|---|---|
| `week` | Monday of the week |
| `ad_spend_k` | advertising spend in that week, thousand dollars |
| `sales_units` | units sold in that week |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Fit `sales_units = a + b * ad_spend_k` with `SLOPE`, `INTERCEPT`, `RSQ`. State the slope in words and with units.
2. Use the line to predict weekly sales at 40 k$.
3. Add a residual column (actual minus fitted). Sort or group the weeks into three equal spend ranges (lowest third, middle,
   highest third) and compute the mean residual in each. What pattern do you see?
4. Add a column `ln(ad_spend_k)` and refit `sales_units` on it. Report slope, intercept and R-squared.
5. Compare the two models with `STEYX` (residual standard error). Which one has the smaller typical miss, and by how much?
6. Fit both models on the first {ntr} weeks only and compute the RMSE of each on the last {nh} weeks. Which model generalises?
7. Predict sales at {planned} k$ with each model. Is that prediction an interpolation?
8. For the log model, how many extra units does one more k$ buy at 10 k$ and at 50 k$ per week (slope divided by spend)?
   How does that compare with the line's slope?
9. *Explain in two or three sentences* what could still be wrong with the log model when it is used to approve a budget.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Sales vs ad spend with both fits", where does the straight line sit relative to the dots at low, middle and high spend?
- In "Residuals vs ad spend", which model leaves a visible pattern? What does that pattern tell you about the model's shape?
- In "Holdout weeks", what happens to the straight-line prediction as spend rises?

## Deliverable

A short note (6-8 lines) to the head of marketing with: the recommended model and why, the expected sales at {planned} k$ with
a clear statement of how reliable that number is, the return on the next k$ at low and high spend, and one chart.
"""
