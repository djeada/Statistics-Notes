"""Lesson 13 - Multiple regression and confounding."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import GRAFANA_DS, PALETTE, Book, Dash, md, write_csv  # noqa: E402

SLUG = "13-multiple-regression-and-confounding"
TITLE = "Multiple regression and confounding"
MODULE = "Relationships and statistical models"
DATASET = "156 weeks of sales with ad spend, price, promo and holiday flags and an irrelevant temperature column"


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1313)
    n = 156
    hol = (rng.random(n) < 0.2).astype(int)
    promo = (rng.random(n) < 0.25).astype(int)
    ad = (30 + 18 * hol + 4 * promo + rng.normal(0, 6, n)).clip(5).round(1)
    price = (24 + 4 * hol - 2.5 * promo + rng.normal(0, 1.2, n)).round(2)
    temp = rng.normal(15, 6, n).round(1)
    sales = (1300 + 5 * ad - 40 * price + 500 * hol + 180 * promo + rng.normal(0, 60, n)).round(0)
    week = pd.date_range("2023-01-02", periods=n, freq="7D")
    return pd.DataFrame({"week": week, "ad_spend_k": ad, "unit_price": price, "promo": promo, "holiday": hol,
                         "temp_c": temp, "sales_units": sales})


def xy_multi(d, title, df, pairs, description="", lines=()):
    """Scatter with a separate x column per series (so groups of different size need no blank cells)."""
    overrides, series = [], []
    for i, (xc, yc) in enumerate(pairs):
        kind = "lines" if yc in lines else "points"
        overrides.append({"matcher": {"id": "byName", "options": yc}, "properties": [
            {"id": "color", "value": {"mode": "fixed", "fixedColor": PALETTE[i % len(PALETTE)]}},
            {"id": "custom.show", "value": kind}, {"id": "custom.pointSize.fixed", "value": 6}]})
        series.append({"x": xc, "y": yc, "color": {"fixed": PALETTE[i % len(PALETTE)]}})
    d._add({"type": "xychart", "title": title, "description": description, "datasource": GRAFANA_DS,
            "targets": d._target(df, None),
            "fieldConfig": {"defaults": {"custom": {"show": "points", "pointSize": {"fixed": 6}, "lineWidth": 2}},
                            "overrides": overrides},
            "options": {"mapping": "manual", "series": series, "legend": {"displayMode": "list", "placement": "bottom"}}}, 12, 9)


def pad_to(a, n):
    """Pad with the last value so every column of a CSV frame has the same length (duplicates are invisible)."""
    a = np.asarray(a, dtype=float)
    return np.concatenate([a, np.repeat(a[-1], n - len(a))])


def fit(df, cols):
    return sm.OLS(df["sales_units"].to_numpy(), sm.add_constant(df[cols].to_numpy(dtype=float))).fit()


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    y = df["sales_units"].to_numpy()
    ad, pr, pm, ho = (df[c].to_numpy() for c in ("ad_spend_k", "unit_price", "promo", "holiday"))

    # toy numbers for theory.md
    tz, tx, ty = np.array([0, 0, 0, 1, 1, 1.]), np.array([1, 2, 3, 3, 4, 5.]), np.array([2, 3, 5, 10, 10, 12.])
    tf = sm.OLS(ty, sm.add_constant(np.c_[tx, tz])).fit()
    assert np.allclose(tf.params, [5 / 6, 1.25, 29 / 6]) and abs(np.polyfit(tx, ty, 1)[0] - 2.7) < 1e-9
    assert abs(np.polyfit(tx, tz, 1)[0] - 0.3) < 1e-9 and abs(tf.rsquared_adj - 0.9795) < 5e-5

    m0 = np.polyfit(ad, y, 1)
    p0 = np.polyfit(pr, y, 1)
    m1 = fit(df, ["ad_spend_k", "unit_price", "promo"])
    m2 = fit(df, ["ad_spend_k", "unit_price", "promo", "holiday"])
    m3 = fit(df, ["ad_spend_k", "unit_price", "promo", "holiday", "temp_c"])
    r0 = float(np.corrcoef(ad, y)[0, 1] ** 2)
    aux = {"unit_price": np.polyfit(ad, pr, 1)[0], "promo": np.polyfit(ad, pm, 1)[0], "holiday": np.polyfit(ad, ho, 1)[0]}
    # exact identity: simple slope = full ad coefficient + sum_j b_j * (slope of x_j on ad)
    recon = m2.params[1] + m2.params[2] * aux["unit_price"] + m2.params[3] * aux["promo"] + m2.params[4] * aux["holiday"]
    assert abs(recon - m0[0]) < 1e-8
    vif_r2 = sm.OLS(ad, sm.add_constant(df[["unit_price", "promo", "holiday"]].to_numpy(dtype=float))).fit().rsquared

    b = Book(df, "Lesson 13 - Multiple regression and confounding",
             "Solved workbook. Yellow cells are assumptions; everything else is a live formula.")
    last = n + 1
    Y = b.rng("sales_units")
    AD, PR, PM, HO, TP = (b.rng(c) for c in ("ad_spend_k", "unit_price", "promo", "holiday", "temp_c"))
    X3 = f"Data!$B$2:$D${last}"   # ad, price, promo
    X4 = f"Data!$B$2:$E${last}"   # + holiday
    X5 = f"Data!$B$2:$F${last}"   # + temp
    XA = f"Data!$C$2:$E${last}"   # price, promo, holiday (for the VIF)
    L = lambda xr, r, c: f"INDEX(LINEST({Y},{xr},TRUE,TRUE),{r},{c})"  # noqa: E731

    b.section("1. Simple regressions (one predictor at a time)")
    b.row("n (weeks)", f"=COUNT({Y})", n, "0")
    s_ad = b.row("Slope of sales on ad spend (units per k$)", f"=SLOPE({Y},{AD})", m0[0], "0.00")
    b.row("R-squared, sales on ad spend", f"=RSQ({Y},{AD})", r0, "0.000")
    s_pr = b.row("Slope of sales on unit price (units per $)", f"=SLOPE({Y},{PR})", p0[0], "0.00", "Sign check: does it make sense?")

    b.section("2. Multiple regression without holiday:  ad + price + promo   (LINEST order is reversed)")
    c_ad1 = b.row("Ad spend coefficient", f"={L(X3, 1, 3)}", m1.params[1], "0.00")
    c_pr1 = b.row("Unit price coefficient", f"={L(X3, 1, 2)}", m1.params[2], "0.00")
    c_pm1 = b.row("Promo coefficient", f"={L(X3, 1, 1)}", m1.params[3], "0.0")
    b.row("Intercept", f"={L(X3, 1, 4)}", m1.params[0], "0.0")
    b.row("R-squared", f"={L(X3, 3, 1)}", m1.rsquared, "0.000")

    b.section("3. Full model:  ad + price + promo + holiday")
    c_ad = b.row("Ad spend coefficient", f"={L(X4, 1, 4)}", m2.params[1], "0.00")
    c_pr = b.row("Unit price coefficient", f"={L(X4, 1, 3)}", m2.params[2], "0.00")
    c_pm = b.row("Promo coefficient", f"={L(X4, 1, 2)}", m2.params[3], "0.0")
    c_ho = b.row("Holiday coefficient", f"={L(X4, 1, 1)}", m2.params[4], "0.0")
    c_ic = b.row("Intercept", f"={L(X4, 1, 5)}", m2.params[0], "0.0")
    se_ad = b.row("Standard error of the ad coefficient", f"={L(X4, 2, 4)}", m2.bse[1], "0.000")
    t_ad = b.row("t-statistic of the ad coefficient", f"={b.local(c_ad)}/{b.local(se_ad)}", m2.tvalues[1], "0.0")
    r2 = b.row("R-squared", f"={L(X4, 3, 1)}", m2.rsquared, "0.0000")
    dfr = b.row("Residual degrees of freedom (n - k - 1)", f"={L(X4, 4, 2)}", m2.df_resid, "0")
    kk = b.row("Number of predictors k", 4, None, "0", "Edit when you change the model", is_input=True)
    adj = b.row("Adjusted R-squared", f"=1-(1-{b.local(r2)})*({n}-1)/({n}-{b.local(kk)}-1)", m2.rsquared_adj, "0.0000",
                "1 - (1-R2)(n-1)/(n-k-1)")
    b.row("Residual standard error (units)", f"={L(X4, 3, 2)}", float(np.sqrt(m2.scale)), "0.0")
    ci_lo = b.row("95% CI of the ad coefficient: low", f"={b.local(c_ad)}-TINV(0.05,{b.local(dfr)})*{b.local(se_ad)}",
                  m2.conf_int()[1][0], "0.00")
    ci_hi = b.row("95% CI of the ad coefficient: high", f"={b.local(c_ad)}+TINV(0.05,{b.local(dfr)})*{b.local(se_ad)}",
                  m2.conf_int()[1][1], "0.00")

    b.section("4. Omitted-variable bias:  simple slope = ad coefficient + sum of (coefficient x slope of that variable on ad)")
    rows = [["unit_price", f"={b.local(c_pr)}", f"=SLOPE({PR},{AD})", "=B{r}*C{r}"],
            ["promo", f"={b.local(c_pm)}", f"=SLOPE({PM},{AD})", "=B{r}*C{r}"],
            ["holiday", f"={b.local(c_ho)}", f"=SLOPE({HO},{AD})", "=B{r}*C{r}"]]
    r0_ = b.next_row + 1
    rows = [[a, bb, c, d.format(r=r0_ + i)] for i, (a, bb, c, d) in enumerate(rows)]
    contrib = {"unit_price": m2.params[2] * aux["unit_price"], "promo": m2.params[3] * aux["promo"],
               "holiday": m2.params[4] * aux["holiday"]}
    exp = {}
    for i, k in enumerate(["unit_price", "promo", "holiday"]):
        exp[(i, 1)] = m2.params[2 + i]
        exp[(i, 2)] = aux[k]
        exp[(i, 3)] = contrib[k]
    t4a, t4b = b.table(["Omitted-from-simple variable", "Coefficient in full model", "Slope of variable on ad spend",
                        "Bias contribution (units per k$)"], rows, fmt={1: "0.00", 2: "0.0000", 3: "0.00"}, expect=exp)
    rec = b.row("Ad coefficient + all contributions", f"={b.local(c_ad)}+SUM(D{t4a}:D{t4b})", recon, "0.0000")
    b.row("Simple slope (section 1)", f"={b.local(s_ad)}", m0[0], "0.0000", "Identical: the bias is fully explained")
    b.row("Total bias of the simple slope (units per k$)", f"={b.local(s_ad)}-{b.local(c_ad)}", m0[0] - m2.params[1], "0.00")

    b.section("5. A useless predictor:  add temp_c")
    r2t = b.row("R-squared with temp_c", f"={L(X5, 3, 1)}", m3.rsquared, "0.0000")
    kt = b.row("Number of predictors k", 5, None, "0", is_input=True)
    adjt = b.row("Adjusted R-squared with temp_c", f"=1-(1-{b.local(r2t)})*({n}-1)/({n}-{b.local(kt)}-1)", m3.rsquared_adj, "0.0000")
    b.row("t-statistic of temp_c", f"={L(X5, 1, 1)}/{L(X5, 2, 1)}", m3.tvalues[5], "0.00", "|t| < 2: indistinguishable from 0")
    b.row("Change in R-squared", f"={b.local(r2t)}-{b.local(r2)}", m3.rsquared - m2.rsquared, "0.0000")
    b.row("Change in adjusted R-squared", f"={b.local(adjt)}-{b.local(adj)}", m3.rsquared_adj - m2.rsquared_adj, "0.0000")

    b.section("6. Collinearity of ad spend with the other predictors")
    vr2 = b.row("R-squared of ad spend regressed on price, promo, holiday", f"=INDEX(LINEST({AD},{XA},TRUE,TRUE),3,1)", vif_r2, "0.000")
    vif = b.row("VIF of ad spend = 1/(1-R2)", f"=1/(1-{b.local(vr2)})", 1 / (1 - vif_r2), "0.00", "Rule of thumb: >5 means estimates are unstable")
    b.row("Correlation ad spend vs holiday", f"=CORREL({AD},{HO})", float(np.corrcoef(ad, ho)[0, 1]), "0.00")
    b.row("Correlation unit price vs holiday", f"=CORREL({PR},{HO})", float(np.corrcoef(pr, ho)[0, 1]), "0.00")

    b.section("7. Using the model")
    a_in = b.row("Scenario: ad spend (k$)", 30, None, "0.0", "Edit me", is_input=True)
    p_in = b.row("Scenario: unit price ($)", 24, None, "0.00", "Edit me", is_input=True)
    pm_in = b.row("Scenario: promo (0/1)", 0, None, "0", "Edit me", is_input=True)
    ho_in = b.row("Scenario: holiday (0/1)", 0, None, "0", "Edit me", is_input=True)
    pred = m2.params @ np.array([1, 30, 24, 0, 0])
    b.row("Predicted sales for the scenario (units)",
          f"={b.local(c_ic)}+{b.local(c_ad)}*{b.local(a_in)}+{b.local(c_pr)}*{b.local(p_in)}+{b.local(c_pm)}*{b.local(pm_in)}+{b.local(c_ho)}*{b.local(ho_in)}",
          pred, "0.0")
    gain = b.row("Extra units from +10 k$ ad spend (full model)", f"=10*{b.local(c_ad)}", 10 * m2.params[1], "0.0")
    naive = b.row("Extra units a naive simple regression would promise", f"=10*{b.local(s_ad)}", 10 * m0[0], "0.0")
    b.row("Overstatement factor", f"={b.local(naive)}/{b.local(gain)}", m0[0] / m2.params[1], "0.00")

    b.add_column("fitted_simple", lambda r: f"={s_ad}*Data!B{r}+INTERCEPT({Y},{AD})".replace("Analysis!", "Analysis!"),
                 expected=np.polyval(m0, ad), fmt="0.0")
    b.add_column("fitted_full", lambda r: f"={c_ic}+{c_ad}*Data!B{r}+{c_pr}*Data!C{r}+{c_pm}*Data!D{r}+{c_ho}*Data!E{r}",
                 expected=m2.fittedvalues, fmt="0.0")
    # table for the chart
    sec_row = b.next_row
    b.section("8. Ad coefficient by model (chart)")
    t8a, t8b = b.table(["Model", "Ad spend coefficient"],
                       [["simple", f"={b.local(s_ad)}"], ["+ price + promo", f"={b.local(c_ad1)}"], ["+ holiday", f"={b.local(c_ad)}"]],
                       fmt={1: "0.00"}, expect={(0, 1): m0[0], (1, 1): m1.params[1], (2, 1): m2.params[1]})
    b.bar_chart_from_table("Estimated effect of ad spend by model (units per k$)", 1, [2], t8a, t8b, anchor="F4", y_title="units per k$")

    b.answers([
        ("Simple slope of sales on ad spend, and R-squared", f"={s_ad}",
         f"{m0[0]:.1f} units per k$ with R-squared {r0:.2f}: spend looks hugely productive."),
        ("Simple slope of sales on unit price", f"={s_pr}",
         f"{p0[0]:+.1f} units per $: higher prices apparently go with higher sales, which is not plausible economics - something else moves with price."),
        ("Coefficients of ad + price + promo (LINEST)", f"={c_ad1}",
         f"ad {m1.params[1]:.1f}, price {m1.params[2]:+.1f}, promo {m1.params[3]:+.0f}. The ad coefficient barely drops and price is still positive: an important variable is still missing."),
        ("Full model coefficients, R-squared, adjusted R-squared, t of ad", f"={c_ad}",
         f"ad {m2.params[1]:.2f} (t = {m2.tvalues[1]:.1f}), price {m2.params[2]:.1f}, promo {m2.params[3]:+.0f}, holiday {m2.params[4]:+.0f}; "
         f"R2 {m2.rsquared:.3f}, adjusted {m2.rsquared_adj:.3f}. Price turns negative once holiday is controlled."),
        ("Decompose the bias of the simple ad slope", f"={rec}",
         f"Holiday contributes {contrib['holiday']:.1f} of the {m0[0] - m2.params[1]:.1f} units per k$ of bias: holiday weeks have both higher spend "
         f"(slope of holiday on ad = {aux['holiday']:.3f}) and much higher sales."),
        ("Does temp_c help?", f"={adjt}",
         f"R2 moves by {m3.rsquared - m2.rsquared:+.4f} but adjusted R2 by {m3.rsquared_adj - m2.rsquared_adj:+.4f} and t = {m3.tvalues[5]:.2f}: drop it."),
        ("VIF of ad spend", f"={vif}",
         f"{1 / (1 - vif_r2):.1f}: ad spend is strongly (not perfectly) tied to holiday and price, so its coefficient has a wide interval "
         f"({m2.conf_int()[1][0]:.1f} to {m2.conf_int()[1][1]:.1f})."),
        ("Extra units from +10 k$ (full vs naive)", f"={gain}",
         f"Full model: {10 * m2.params[1]:.0f} units; the simple regression would promise {10 * m0[0]:.0f}, {m0[0] / m2.params[1]:.1f} times too much."),
        ("Limitations", "see text",
         "Observational data: any other variable that moves with spend (competitor activity, stock-outs, seasonality beyond the holiday flag) "
         "would bias the coefficient again. Adding controls reduces confounding only for what is measured."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-13-multiple-regression", "13 · Multiple regression and confounding",
             "The same ad-spend slope under four specifications: the confounder (holiday) inflates the simple estimate.",
             df.iloc[-52:].rename(columns={"week": "time"}), "time")
    d.stat("Ad spend effect (units per k$) and fit", {"simple slope": m0[0], "+price+promo": m1.params[1], "full model": m2.params[1],
                                                      "R2 simple": r0, "R2 full": m2.rsquared, "adj R2 full": m2.rsquared_adj},
           "The simple slope is about three times the full-model coefficient.", decimals=2)
    cm = pd.DataFrame({"model": ["simple", "+ price + promo", "+ holiday (full)"],
                       "ad_spend": [m0[0], m1.params[1], m2.params[1]],
                       "unit_price": [p0[0], m1.params[2], m2.params[2]]})
    d.bars("Coefficients by model", cm, "Ad-spend coefficient shrinks and the price coefficient flips sign once holiday is controlled.")
    o = np.argsort(ad)
    nm, hm = ho == 0, ho == 1
    xs = np.linspace(ad.min(), ad.max(), 40)
    nn = n
    sc = pd.DataFrame({"ad_normal": pad_to(ad[nm], nn), "sales_normal": pad_to(y[nm], nn),
                       "ad_holiday": pad_to(ad[hm], nn), "sales_holiday": pad_to(y[hm], nn),
                       "ad_line": pad_to(xs, nn), "simple_fit": pad_to(np.polyval(m0, xs), nn)})
    xy_multi(d, "Sales vs ad spend, holiday weeks separated", sc,
             [("ad_normal", "sales_normal"), ("ad_holiday", "sales_holiday"), ("ad_line", "simple_fit")],
             "Two clouds: holiday weeks sit higher AND further right. The simple line runs through both and is much steeper than the slope inside either cloud.",
             lines=["simple_fit"])
    last52 = slice(n - 52, n)
    fit_df = pd.DataFrame({"time": df["week"].iloc[last52], "sales": y[last52], "simple_model": np.polyval(m0, ad)[last52],
                           "full_model": m2.fittedvalues[last52]})
    d.timeseries("Weekly sales and fitted values (last 52 weeks)", fit_df,
                 "The full model tracks the holiday spikes; the simple model (driven by ad spend alone) misses level and timing.",
                 points=["sales"], colors={"sales": "#4E79A7", "simple_model": "#E15759", "full_model": "#59A14F"})
    tb = pd.DataFrame({"term": ["intercept", "ad_spend_k", "unit_price", "promo", "holiday"], "estimate": m2.params.round(3),
                       "std_error": m2.bse.round(3), "t": m2.tvalues.round(2)})
    d.table("Full model coefficients", tb, "OLS on all 156 weeks.")
    cmp_ = pd.DataFrame({"model": ["simple (ad)", "ad+price+promo", "+ holiday", "+ holiday + temp_c"], "k": [1, 3, 4, 5],
                         "R2": [r0, m1.rsquared, m2.rsquared, m3.rsquared],
                         "adjusted_R2": [1 - (1 - r0) * (n - 1) / (n - 2), m1.rsquared_adj, m2.rsquared_adj, m3.rsquared_adj]}).round(4)
    d.table("Model comparison", cmp_, "temp_c is pure noise: R2 creeps up by 0.0001, adjusted R2 goes down.")
    bias = pd.DataFrame({"term": ["unit_price", "promo", "holiday"], "contribution_to_bias": [contrib["unit_price"], contrib["promo"], contrib["holiday"]]})
    d.bars("Where the bias in the simple slope comes from", bias, "coefficient x slope of that variable on ad spend; the contributions add up to simple slope minus full coefficient.")
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: multiple regression and confounding

## Why this matters

A simple regression of sales on advertising answers "how do sales differ between weeks with more and less advertising?",
not "what happens to sales if I raise advertising?". If advertising is higher in the weeks that would have been strong anyway
(holidays, promotions, product launches), the simple slope credits advertising with the effect of those weeks. A budget set
from it will be too generous. Multiple regression separates the contributions of several variables, **if** the relevant ones are
in the model.

## The model

$$
y_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_k x_{ik} + \varepsilon_i .
$$

OLS minimises the sum of squared residuals; in matrix form $\hat\beta = (X^\top X)^{-1} X^\top y$. Each
$\hat\beta_j$ is the estimated change in $y$ for a one-unit change in $x_j$ **holding the other predictors fixed**, that is,
comparing weeks that are alike in all the other included variables. Spreadsheet tool: `LINEST(y, X, TRUE, TRUE)`; take single
cells with `INDEX(LINEST(...), row, col)`. Row 1 holds the coefficients, **in reverse order of the columns of `X`** and the
intercept last; row 2 the standard errors; row 3 holds $R^2$ and $s_e$; row 4 the $F$ statistic and the residual degrees of
freedom $n-k-1$. `X` must be a block of adjacent columns.

## Confounding and omitted-variable bias

A **confounder** $z$ influences both the predictor $x$ and the outcome $y$. If you regress $y$ on $x$ alone, the slope absorbs
part of $z$'s effect. There is an exact identity for OLS:

$$
\hat b_{\text{simple}} = \hat\beta_x + \hat\beta_z\,\hat\delta,
$$

where $\hat\beta_x,\hat\beta_z$ come from the regression of $y$ on both $x$ and $z$, and $\hat\delta$ is the slope of the
regression of $z$ on $x$. With several omitted variables, add one term $\hat\beta_j\hat\delta_j$ for each. The bias is large
when the omitted variable matters a lot for $y$ ($\beta_z$ large) **and** is strongly tied to $x$ ($\delta$ large).

**Worked example.** Six weeks: $z$ (holiday) $=0,0,0,1,1,1$, $x$ (ad spend) $=1,2,3,3,4,5$, $y=2,3,5,10,10,12$. The simple regression
gives slope $2.7$. The regression on both gives $\hat y = 0.83 + 1.25\,x + 4.83\,z$ ($R^2=0.988$, adjusted $0.979$). The slope of $z$
on $x$ is $\hat\delta = 0.3$, and $1.25 + 4.83\cdot 0.3 = 2.7$ exactly. More than half of the simple slope was the
holiday, not the advertising.

Signs can flip, not only grow: if prices are raised in peak weeks and demand is high in peak weeks, the simple price slope can
be positive even though the price effect holding the season fixed is negative (Simpson-style reversal, see
[lesson 05](../05-sampling-bias-and-simpson-s-paradox/theory.md)).

## Judging a model: R-squared, adjusted R-squared, standard errors

$R^2$ never decreases when you add a variable, even a random one, because OLS can always fit a little noise. **Adjusted**
$R^2$ charges for each parameter:

$$
R^2_{\text{adj}} = 1 - (1-R^2)\,\frac{n-1}{n-k-1}.
$$

For the six-week example: $1-(1-0.9877)\cdot 5/3 = 0.979$. Use it (or a holdout error) to compare models with a different number of
predictors. The standard error of a coefficient gives the interval $\hat\beta_j \pm t_{n-k-1,\,0.975}\,\mathrm{SE}_j$ and the
$t$-statistic $\hat\beta_j/\mathrm{SE}_j$; $|t|<2$ means "not distinguishable from 0".

## Collinearity

When predictors are strongly correlated the coefficients are individually imprecise although the model as a whole predicts well.
The **variance inflation factor** of $x_j$ is $\mathrm{VIF}_j = 1/(1-R_j^2)$ where $R_j^2$ comes from regressing $x_j$ on the other
predictors. VIF > 5 (or 10) is a warning: standard errors are inflated by $\sqrt{\mathrm{VIF}}$. Collinearity is the price of
having controlled for a variable that moves with the one you care about; it is not a reason to omit it, since omission gives a
precise but biased answer.

## Assumptions and pitfalls

1. **Controlling is only as good as your list of controls.** Unmeasured confounders still bias the coefficient; a regression is
   not an experiment (lesson 19 covers A/B tests).
2. **Do not control for consequences of $x$.** A variable *caused by* advertising (for instance, website visits) belongs on the path
   from $x$ to $y$; adjusting for it removes part of the real effect.
3. **Linearity and additivity.** The model assumes constant effects; check residuals (lesson 15) and consider transformations
   (lesson 12) or interactions.
4. **Dummy variables** (0/1) shift the intercept: the promo coefficient is the average difference between promo and non-promo weeks
   at equal ad spend and price.
5. **Too many predictors for too few rows** leads to overfitting; keep $n$ well above $k$ and check on a holdout set.

## Related notes

- [Linear and nonlinear regression](../12-linear-and-nonlinear-regression/theory.md)
- [Correlation and lagged relationships](../11-correlation-and-lagged-relationships/theory.md)
- [Residual analysis and model diagnostics](../15-residual-analysis-and-model-diagnostics/theory.md)
- [A/B testing and effect sizes](../19-a-b-testing-and-effect-sizes/theory.md)
- Repo note: [Multiple regression](../../notes/regression/multiple_regression.md)
"""

TASK = r"""
# Task: multiple regression and confounding

## Scenario

A retail chain wants to know whether to increase its weekly advertising budget. A first regression of sales on ad spend gives a
striking slope, and the finance team has already used it to forecast the return on an extra 10 k$ per week. You are asked to
review that estimate before the budget is signed. You also have weekly price, a promotion flag and a holiday flag.

## Data

`data.csv` - 156 weeks (2023-01-02 onwards), one row per week.

| column | meaning |
|---|---|
| `week` | Monday of the week |
| `ad_spend_k` | advertising spend, thousand dollars |
| `unit_price` | average selling price, dollars |
| `promo` | 1 if a price promotion ran that week, else 0 |
| `holiday` | 1 if the week contains a public holiday / peak-season event, else 0 |
| `temp_c` | mean outdoor temperature, degrees Celsius |
| `sales_units` | units sold |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`. Use `LINEST` inside `INDEX` for multiple regression.

1. Regress `sales_units` on `ad_spend_k` alone (`SLOPE`, `RSQ`). Report the slope and R-squared.
2. Regress `sales_units` on `unit_price` alone. What sign do you get, and does it make business sense?
3. Fit `sales_units ~ ad_spend_k + unit_price + promo`. Report the three coefficients. What changed relative to questions 1-2?
4. Add `holiday` as a fourth predictor. Report all coefficients, R-squared, adjusted R-squared and the t-statistic of the ad
   coefficient.
5. Explain the change in the ad coefficient quantitatively: regress each other predictor on `ad_spend_k` (`SLOPE`) and show that
   `ad coefficient + sum(coefficient x slope)` reproduces the simple slope from question 1.
6. Add `temp_c` as a fifth predictor. What happens to R-squared and adjusted R-squared? Keep it or drop it?
7. Compute the VIF of `ad_spend_k` against the other three predictors. What does it imply for the precision of its coefficient
   (give the 95% interval from question 4)?
8. Using the full model, how many extra units does +10 k$ per week buy in an otherwise normal week? How many would the
   simple regression have promised?
9. *In two or three sentences:* what would have to be true for the full-model coefficient to still be biased?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Sales vs ad spend, holiday weeks separated", what do the two clouds look like, and how does the slope inside each compare with the simple line?
- In "Coefficients by model", what happens to the unit price bar across the three specifications?
- In "Where the bias in the simple slope comes from", which variable dominates?

## Deliverable

A short note (6-8 lines) to the finance team: the corrected return on +10 k$, why the earlier estimate was too high, the
uncertainty of the corrected number, and one residual risk. Include one chart.
"""
