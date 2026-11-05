"""Lesson 15 - Residual analysis and model diagnostics."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.diagnostic import het_breuschpagan

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "15-residual-analysis-and-model-diagnostics"
TITLE = "Residual analysis and model diagnostics"
MODULE = "Relationships and statistical models"
DATASET = "120 courier deliveries: distance (km) and delivery time (min); R-squared 0.89 but the model fails four diagnostics"
COOK_THR = 0.5
BANDS = [("< 6 km", 0, 6), ("6 - 12 km", 6, 12), (">= 12 km", 12, 1e9)]


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1515)
    n = 120
    d = np.clip(rng.gamma(4, 2.2, n) + 1, 1, 24).round(1)
    idx = [41, 86]
    d[idx] = [44.0, 47.5]  # two long-haul orders
    noise = rng.normal(0, 0.35 * d + 0.3)  # spread grows with distance
    jam = (rng.random(n) < 0.08) * rng.exponential(0.4 * d)  # occasional long delays
    t = 8 + 2.5 * d + noise + jam
    t[idx] = [8 + 2.5 * 44 - 20, 8 + 2.5 * 47.5 - 26]  # long-haul orders used a fast highway route
    ts = pd.date_range("2026-02-02 08:00", periods=n, freq="45min")
    return pd.DataFrame({"ordered_at": ts, "distance_km": d, "delivery_min": t.round(0)})


def wls_fit(x, y, w):
    sw = w.sum()
    sx, sy = (w * x).sum(), (w * y).sum()
    b = ((w * x * y).sum() - sx * sy / sw) / ((w * x * x).sum() - sx * sx / sw)
    return float(b), float((sy - b * sx) / sw)


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    x, y = df["distance_km"].to_numpy(), df["delivery_min"].to_numpy()
    X = sm.add_constant(x)
    ols = sm.OLS(y, X).fit()
    inf = ols.get_influence()
    a0, b0 = float(ols.params[0]), float(ols.params[1])
    s_e = float(np.sqrt(ols.scale))
    res = ols.resid
    lev = inf.hat_matrix_diag
    stud = inf.resid_studentized_internal
    cook = inf.cooks_distance[0]
    keep = (cook <= COOK_THR).astype(float)
    wls_w = 1 / x ** 2
    schemes = {"OLS, all rows": np.ones(n), "OLS, influential rows removed": keep, "WLS (w = 1/x^2), all rows": wls_w,
               "WLS, influential rows removed": wls_w * keep}
    fits = {k: wls_fit(x, y, w) for k, w in schemes.items()}
    bw, aw = fits["WLS (w = 1/x^2), all rows"]
    res_w = (y - (aw + bw * x)) / x
    sk, ku = float(stats.skew(res, bias=False)), float(stats.kurtosis(res, bias=False))
    jb = n / 6 * (sk ** 2 + ku ** 2 / 4)
    bp_lm, bp_p = het_breuschpagan(res, X)[:2]
    r2_e2 = float(np.corrcoef(res ** 2, x)[0, 1] ** 2)
    assert abs(n * r2_e2 - bp_lm) < 1e-6 * max(1, bp_lm)
    thr_lev = 4 / n
    order_c = np.argsort(cook)[::-1]

    # toy numbers quoted in theory.md
    tx, ty = np.array([1, 2, 3, 4, 10.]), np.array([2.1, 3.9, 6.2, 7.8, 10.])
    tf = sm.OLS(ty, sm.add_constant(tx)).fit()
    ti = tf.get_influence()
    assert np.allclose(tf.params, [2.824, 0.794]) and abs(ti.hat_matrix_diag[4] - 0.92) < 1e-9
    assert abs(ti.cooks_distance[0][4] - 17.058) < 5e-3 and abs(ti.resid_studentized_internal[4] + 1.722) < 5e-3
    assert np.allclose(np.polyfit(tx[:4], ty[:4], 1), [1.94, 0.15])

    b = Book(df, "Lesson 15 - Residual analysis and model diagnostics",
             "Solved workbook. Yellow cells are assumptions; everything else is a live formula.")
    last = n + 1
    DX, DY = b.rng("distance_km"), b.rng("delivery_min")
    b.section("1. The model that looks fine:  delivery_min = a + b * distance_km")
    b.row("n (orders)", f"=COUNT({DY})", n, "0")
    sl = b.row("Slope b (min per km)", f"=SLOPE({DY},{DX})", b0, "0.000")
    ic = b.row("Intercept a (min)", f"=INTERCEPT({DY},{DX})", a0, "0.000")
    b.row("R-squared", f"=RSQ({DY},{DX})", ols.rsquared, "0.000", "High - so is the model fine?")
    se = b.row("Residual standard error (min)", f"=STEYX({DY},{DX})", s_e, "0.00")

    # helper columns (all rows)
    b.add_column("fitted", lambda r: f"={ic}+{sl}*Data!B{r}", expected=ols.fittedvalues, fmt="0.00")
    b.add_column("resid", lambda r: f"=Data!C{r}-Data!D{r}", expected=res, fmt="0.00")
    b.add_column("leverage", lambda r: f"=1/{n}+(Data!B{r}-AVERAGE({DX}))^2/DEVSQ({DX})", expected=lev, fmt="0.0000")
    b.add_column("std_resid", lambda r: f"=Data!E{r}/({se}*SQRT(1-Data!F{r}))", expected=stud, fmt="0.000")
    b.add_column("cooks_d", lambda r: f"=Data!G{r}^2*Data!F{r}/((1-Data!F{r})*2)", expected=cook, fmt="0.0000")
    b.add_column("resid_sq", lambda r: f"=Data!E{r}^2", expected=res ** 2, fmt="0.00")
    RES, LEV, STD, COOK, RSQ_ = (b.rng(c) for c in ("resid", "leverage", "std_resid", "cooks_d", "resid_sq"))
    bandcols = []
    for name, lo, hi in BANDS:
        cn = f"resid {name}"
        b.add_column(cn, lambda r, lo=lo, hi=hi: f'=IF(AND(Data!B{r}>={lo},Data!B{r}<{hi}),Data!E{r},"")',
                     expected=np.where((x >= lo) & (x < hi), res, np.nan), fmt="0.00")
        bandcols.append(b.rng(cn))
    # QQ columns
    b.add_column("qq_theory", lambda r: f"=NORMSINV((ROW()-1-0.5)/{n})", expected=stats.norm.ppf((np.arange(1, n + 1) - 0.5) / n), fmt="0.000")
    b.add_column("qq_sample", lambda r: f"=SMALL({STD},ROW()-1)", expected=np.sort(stud), fmt="0.000")

    b.section("2. Constant variance?  Spread of residuals by distance band")
    rows, exp, sds = [], {}, []
    for i, ((name, lo, hi), br) in enumerate(zip(BANDS, bandcols)):
        m = (x >= lo) & (x < hi)
        rows.append([name, f"=COUNT({br})", f"=STDEV({br})"])
        exp[(i, 1)], exp[(i, 2)] = int(m.sum()), float(res[m].std(ddof=1))
        sds.append(res[m].std(ddof=1))
    t2a, t2b = b.table(["Distance band", "orders", "SD of residual (min)"], rows, fmt={2: "0.00"}, expect=exp)
    ratio = b.row("SD far / SD near", f"=C{t2b}/C{t2a}", sds[2] / sds[0], "0.00", "1 = constant variance")
    r2e = b.row("R-squared of squared residuals on distance", f"=RSQ({RSQ_},{DX})", r2_e2, "0.000")
    lm = b.row("Breusch-Pagan LM = n * R2", f"={n}*{b.local(r2e)}", float(bp_lm), "0.00")
    bpp = b.row("p-value  CHIDIST(LM, 1)", f"=CHIDIST({b.local(lm)},1)", float(bp_p), "0.0000", "Small p: the variance depends on distance")
    b.scatter_chart("Residuals vs distance", "distance_km", ["resid"], anchor="G4", x_title="distance (km)", y_title="residual (min)")

    b.section("3. Normal residuals?")
    skw = b.row("Skewness of residuals", f"=SKEW({RES})", sk, "0.00", "0 for a symmetric distribution")
    kur = b.row("Excess kurtosis", f"=KURT({RES})", ku, "0.00", "0 for a normal distribution")
    tails = b.row("Share of |standardised residual| > 2",
                  f'=(COUNTIF({STD},">2")+COUNTIF({STD},"<-2"))/{n}', float((np.abs(stud) > 2).mean()), "0.0%")
    b.row("Share expected under normality", "=2*(1-NORMSDIST(2))", float(2 * (1 - stats.norm.cdf(2))), "0.0%")
    jbc = b.row("Jarque-Bera (approximate)", f"={n}/6*({b.local(skw)}^2+{b.local(kur)}^2/4)", jb, "0.0", "Compare with chi-square(2): 5.99 at 5%")
    b.row("p-value  CHIDIST(JB, 2)", f"=CHIDIST({b.local(jbc)},2)", float(stats.chi2.sf(jb, 2)), "0.0000")
    b.scatter_chart("Normal QQ plot of standardised residuals", "qq_theory", ["qq_sample"], anchor="G24",
                    x_title="theoretical normal quantile", y_title="sample quantile")

    b.section("4. Leverage and influence")
    thr_l = b.row("Leverage threshold 2p/n (p = 2)", f"=4/{n}", thr_lev, "0.0000")
    b.row("Number of orders above the leverage threshold", f'=COUNTIF({LEV},">"&{b.local(thr_l)})', int((lev > thr_lev).sum()), "0")
    b.row("Largest leverage", f"=MAX({LEV})", float(lev.max()), "0.000")
    thr_c = b.row("Cook's D cut-off (assumption)", COOK_THR, None, "0.00", "Edit me: 4/n = 0.033 is a stricter alternative", is_input=True)
    c1 = b.row("Largest Cook's D", f"=MAX({COOK})", float(cook[order_c[0]]), "0.000")
    b.row("... distance of that order (km)", f"=INDEX({DX},MATCH({b.local(c1)},{COOK},0))", float(x[order_c[0]]), "0.0")
    b.row("... its standardised residual", f"=INDEX({STD},MATCH({b.local(c1)},{COOK},0))", float(stud[order_c[0]]), "0.00")
    c2 = b.row("Second largest Cook's D", f"=LARGE({COOK},2)", float(cook[order_c[1]]), "0.000")
    b.row("... distance of that order (km)", f"=INDEX({DX},MATCH({b.local(c2)},{COOK},0))", float(x[order_c[1]]), "0.0")
    nc = b.row("Orders with Cook's D above the cut-off", f'=COUNTIF({COOK},">"&{b.local(thr_c)})', int((cook > COOK_THR).sum()), "0")
    # keep flag and weights depend on the (editable) cut-off
    b.add_column("keep", lambda r: f"=IF(Data!{b.col('cooks_d')}{r}>{thr_c},0,1)", expected=keep, fmt="0")
    b.add_column("w_wls", lambda r: f"=1/Data!B{r}^2", expected=wls_w, fmt="0.00000")
    b.add_column("w_wls_keep", lambda r: f"=Data!{b.col('w_wls')}{r}*Data!{b.col('keep')}{r}", expected=wls_w * keep, fmt="0.00000")
    b.add_column("w_ols", lambda r: "=1", expected=np.ones(n), fmt="0")

    b.section("5. Remedies: refit without the influential orders, and weight by 1/distance^2")
    rows, exp = [], {}
    wcols = {"OLS, all rows": "w_ols", "OLS, influential rows removed": "keep", "WLS (w = 1/x^2), all rows": "w_wls",
             "WLS, influential rows removed": "w_wls_keep"}
    r0 = b.next_row + 1
    for i, (nm, wc) in enumerate(wcols.items()):
        W = b.rng(wc)
        rr = r0 + i
        rows.append([nm, f"=SUM({W})", f"=SUMPRODUCT({W},{DX})", f"=SUMPRODUCT({W},{DY})", f"=SUMPRODUCT({W},{DX},{DY})",
                     f"=SUMPRODUCT({W},{DX},{DX})", f"=(E{rr}-C{rr}*D{rr}/B{rr})/(F{rr}-C{rr}^2/B{rr})", f"=(D{rr}-G{rr}*C{rr})/B{rr}"])
        bb, aa = fits[nm]
        exp[(i, 6)], exp[(i, 7)] = bb, aa
    t5a, t5b = b.table(["Weighting scheme", "sum w", "sum w*x", "sum w*y", "sum w*x*y", "sum w*x*x", "slope (min/km)", "intercept (min)"],
                       rows, fmt={1: "0.00", 2: "0.00", 3: "0.0", 4: "0.0", 5: "0.0", 6: "0.000", 7: "0.00"}, expect=exp)
    # scaled WLS residuals
    b.add_column("resid_wls_scaled", lambda r: f"=(Data!C{r}-($H${t5a + 2}+$G${t5a + 2}*Data!B{r}))/Data!B{r}".replace("$H$", "Analysis!$H$").replace("$G$", "Analysis!$G$"),
                 expected=res_w, fmt="0.000")
    bandw = []
    for name, lo, hi in BANDS:
        cn = f"wls resid {name}"
        b.add_column(cn, lambda r, lo=lo, hi=hi: f'=IF(AND(Data!B{r}>={lo},Data!B{r}<{hi}),Data!{b.col("resid_wls_scaled")}{r},"")',
                     expected=np.where((x >= lo) & (x < hi), res_w, np.nan), fmt="0.000")
        bandw.append(b.rng(cn))
    rows, exp = [], {}
    sdw = []
    for i, ((name, lo, hi), bc) in enumerate(zip(BANDS, bandw)):
        m = (x >= lo) & (x < hi)
        rows.append([name, f"=STDEV({bc})"])
        exp[(i, 1)] = float(res_w[m].std(ddof=1))
        sdw.append(res_w[m].std(ddof=1))
    b.table(["Distance band", "SD of WLS residual / distance"], rows, fmt={1: "0.000"}, expect=exp)
    b.row("Slope: OLS vs WLS, both on all rows (min/km)", f"=G{t5a}-G{t5a + 2}", fits["OLS, all rows"][0] - fits["WLS (w = 1/x^2), all rows"][0], "0.000")

    b.answers([
        ("Slope, intercept, R-squared and residual SE of the straight-line model", f"={sl}",
         f"delivery = {a0:.1f} + {b0:.2f} x distance, R-squared {ols.rsquared:.2f}, residual SE {s_e:.1f} min. Looks like a good model."),
        ("Residual SD in the three distance bands; far / near ratio", f"={ratio}",
         f"{sds[0]:.1f} / {sds[1]:.1f} / {sds[2]:.1f} min, ratio {sds[2] / sds[0]:.1f}: the error grows with distance (a fan), so one residual SE for all orders is wrong."),
        ("Breusch-Pagan statistic and p-value", f"={lm}",
         f"LM = {bp_lm:.1f}, p = {bp_p:.1e}: reject constant variance. Standard errors and prediction intervals from the usual formulas are unreliable."),
        ("Skewness, excess kurtosis, share beyond +-2, Jarque-Bera", f"={jbc}",
         f"Skew {sk:.2f}, excess kurtosis {ku:.1f}, {(np.abs(stud) > 2).mean():.1%} of standardised residuals beyond +-2 (normal: 4.6%), JB = {jb:.0f}: "
         f"right-skewed, heavy-tailed residuals (occasional long delays); the QQ plot bends away from the diagonal."),
        ("Number of high-leverage orders and the largest leverage", f"={thr_l}",
         f"{int((lev > thr_lev).sum())} orders exceed 4/n = {thr_lev:.3f}; the largest leverage is {lev.max():.2f} (a {x[np.argmax(lev)]:.1f} km order)."),
        ("Largest and second largest Cook's D, and which orders", f"={c1}",
         f"D = {cook[order_c[0]]:.2f} ({x[order_c[0]]:.1f} km, standardised residual {stud[order_c[0]]:.1f}) and {cook[order_c[1]]:.2f} ({x[order_c[1]]:.1f} km). "
         f"Two long-haul orders far from the rest are steering the whole line; {int((cook > COOK_THR).sum())} orders exceed {COOK_THR}."),
        ("Slope with and without the influential orders", f"=Analysis!G{t5a + 1}",
         f"{fits['OLS, all rows'][0]:.2f} with them, {fits['OLS, influential rows removed'][0]:.2f} min/km without: they pull the slope down by "
         f"{fits['OLS, influential rows removed'][0] - fits['OLS, all rows'][0]:.2f}."),
        ("WLS slope and residual spread after weighting", f"=Analysis!G{t5a + 2}",
         f"WLS slope {bw:.2f}; scaled residual SDs by band {sdw[0]:.2f} / {sdw[1]:.2f} / {sdw[2]:.2f} (roughly constant, far/near {sdw[2] / sdw[0]:.1f} vs {sds[2] / sds[0]:.1f} before)."),
        ("Can the OLS model be used to promise delivery times?", "see text",
         "Not as is: the line is acceptable for typical short orders but its error band is much too narrow for long trips, and the two long-haul orders need "
         "their own explanation (route type?). Fit separately or add a route variable, then re-check the residuals."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-15-diagnostics", "15 · Residual analysis and model diagnostics",
             "A regression with R-squared 0.89 that fails the residual checks: fan-shaped spread, skewed tails, two influential orders.",
             df.rename(columns={"ordered_at": "time"}), "time")
    d.stat("Looks good, is not", {"R2": ols.rsquared, "residual SE (min)": s_e, "Breusch-Pagan LM": float(bp_lm), "skew": sk,
                                  "max Cook's D": float(cook.max()), "slope OLS": b0, "slope WLS": bw},
           "R-squared passes; heteroscedasticity (BP), skewness and influence do not.", decimals=2)
    o = np.argsort(x)
    m = keep.astype(bool)
    b_wo, a_wo = fits["OLS, influential rows removed"]
    sc = pd.DataFrame({"distance_km": x[o], "delivery_min": y[o], "OLS_all": (a0 + b0 * x)[o], "OLS_without_influential": (a_wo + b_wo * x)[o],
                       "WLS": (aw + bw * x)[o]})
    d.xy("Delivery time vs distance", sc, "distance_km", ["delivery_min", "OLS_all", "OLS_without_influential", "WLS"],
         "The two long-haul orders (right edge, below the cloud) tilt the OLS line; fits without them or with weights are steeper.",
         lines=["OLS_all", "OLS_without_influential", "WLS"])
    rs = pd.DataFrame({"distance_km": x[o], "residual_min": res[o]})
    d.xy("Residuals vs distance (fan shape)", rs, "distance_km", ["residual_min"],
         "A well-specified model gives a patternless band of constant width. Here the band widens with distance.")
    q = pd.DataFrame({"theoretical": stats.norm.ppf((np.arange(1, n + 1) - 0.5) / n), "sample": np.sort(stud)})
    q["diagonal"] = q["theoretical"]
    d.xy("Normal QQ plot of standardised residuals", q, "theoretical", ["sample", "diagonal"],
         "Points should lie on the diagonal. The right tail (long delays) and left tail (long-haul orders) leave it.", lines=["diagonal"])
    cd = pd.DataFrame({"time": df["ordered_at"], "cooks_d": cook, "cutoff": COOK_THR})
    d.timeseries("Cook's distance by order", cd, "Two orders stand out far above the cut-off; every other order is below 0.15.",
                 bars=["cooks_d"], dashed=["cutoff"], colors={"cooks_d": "#4E79A7", "cutoff": "#E15759"})
    top = order_c[:6]
    tb = pd.DataFrame({"ordered_at": df["ordered_at"].dt.strftime("%m-%d %H:%M").to_numpy()[top], "distance_km": x[top],
                       "delivery_min": y[top], "std_resid": stud[top].round(2),
                       "cooks_d": cook[top].round(3)})
    d.table("Six most influential orders", tb, "Sorted by Cook's distance. The long-haul orders combine high leverage with a large negative residual.")
    bd = pd.DataFrame({"band": [b_[0] for b_ in BANDS], "OLS_residual_SD_min": sds, "WLS_scaled_residual_SD": sdw})
    d.bars("Residual spread by distance band", bd, "OLS residual SD (min) grows with distance; after weighting by 1/distance the scaled spread is flat.")
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: residual analysis and model diagnostics

## Why this matters

$R^2$ measures how close the fitted line is to the data **on average**. It does not tell you whether the model's assumptions
hold, and the assumptions are what make coefficients, standard errors, confidence intervals and prediction intervals trustworthy.
A model can have $R^2 \approx 0.9$ while its error is several times larger for some customers than for others, while a handful of rows
control the slope, and while the "typical error" you quote is wrong for exactly the cases you care about. Residual analysis is the
routine that finds this out before the model is used.

## Residuals

For a fitted model $\hat y_i$, the residual is $e_i = y_i - \hat y_i$. OLS inference assumes, for the true errors,
(1) the mean is 0 for every $x$ (the shape is right), (2) constant variance (**homoscedasticity**), (3) independence (lesson 14),
(4) approximate normality (needed for small-sample intervals, less so for the slope in large samples).
Because residuals of rows with high leverage are artificially small, we use **standardised (internally studentised) residuals**:

$$
r_i = \frac{e_i}{s\sqrt{1-h_{ii}}},\qquad s = \sqrt{\tfrac{SSE}{n-p}} .
$$

## The four plots and tests

1. **Residuals vs fitted (or vs $x$):** a patternless horizontal band is the goal. A curve means the shape is wrong (lesson 12);
   a funnel means the variance changes with the level. **Breusch-Pagan** formalises the funnel: regress $e_i^2$ on the predictors,
   and $LM = n R^2_{e^2}$ is approximately $\chi^2$ with (number of predictors) degrees of freedom under constant variance.
2. **Normal QQ plot:** sorted standardised residuals against normal quantiles $\Phi^{-1}\!\big(\tfrac{i-0.5}{n}\big)$. Points on the diagonal mean
   normality; an S-shape means heavy tails; a bend means skew. Numerically use skewness and excess kurtosis; the
   Jarque-Bera statistic $JB = \tfrac n6\big(S^2 + \tfrac{K^2}{4}\big)$ is compared with $\chi^2_2$ (5.99 at the 5 % level). The Excel
   `SKEW`/`KURT` functions are bias-adjusted, so a spreadsheet JB is approximate.
3. **Leverage:** $h_{ii} = \tfrac1n + \tfrac{(x_i-\bar x)^2}{\sum (x_j-\bar x)^2}$ measures how far a row's $x$ is from the others (with $p$ parameters,
   $\sum h_{ii} = p$; flag $h_{ii} > 2p/n$).
4. **Influence (Cook's distance):** how much the fitted values change if row $i$ is dropped,

$$
D_i = \frac{r_i^2}{p}\cdot\frac{h_{ii}}{1-h_{ii}} .
$$

A row is influential when it has **both** leverage and a large residual. Flag $D_i > 1$ (or $> 0.5$, or $> 4/n$ if you want to be strict) and
refit without it to see how much the conclusions move.

**Worked example.** Five points: $x = 1,2,3,4,10$, $y = 2.1, 3.9, 6.2, 7.8, 10.0$. The line is $\hat y = 2.82 + 0.794x$, $R^2 = 0.81$, $s = 1.57$. The point
$x = 10$ has $h = \tfrac15 + \tfrac{36}{50} = 0.92$ and residual $-0.76$, so $r = -0.764/(1.57\sqrt{0.08}) = -1.72$ and
$D = \tfrac{1.72^2}{2}\cdot\tfrac{0.92}{0.08} = 17.1$. Without it the slope is $1.94$: one point out of five changed the slope by a factor of 2.4, although its
residual is unremarkable. Leverage, not the size of the residual alone, makes a point dangerous.

## What to do when a check fails

- **Funnel / non-constant variance:** transform $y$ (log), use **weighted least squares** with weights $w_i \propto 1/\mathrm{Var}(e_i)$ (here
  $\mathrm{SD}(e)\propto x$, so $w = 1/x^2$), or keep OLS coefficients and use robust (heteroscedasticity-consistent) standard errors.
  The slope may barely move; the *intervals* are what were wrong.
- **Curvature:** change the shape (lesson 12) or add a variable (lesson 13).
- **Skew / heavy tails:** look at what the large residuals have in common (a missing variable such as traffic or weather); consider a log
  transform, quantile regression or a bootstrap for intervals (lesson 17).
- **Influential rows:** do not delete them silently. Check for data errors; if they are real, find out why they differ (a different regime may deserve its own model)
  and report results with and without them.

## Assumptions and pitfalls

1. **Residual tests are not a verdict.** With large $n$ trivial departures are "significant"; with small $n$ real ones are missed. Look at the plot and the size
   of the effect.
2. **R-squared can reward a wrong model**, particularly when a few extreme points make the variance of $x$ large.
3. **Removing outliers until the diagnostics look good** is data dredging. State the rule in advance.
4. **Residuals of an overfitted model look better** than the true errors, because they were used to fit it; check on held-out data (lesson 24).
5. **Time-ordered data:** also plot residuals against time and check autocorrelation (Durbin-Watson, lesson 14).

## Related notes

- [Linear and nonlinear regression](../12-linear-and-nonlinear-regression/theory.md)
- [Multiple regression and confounding](../13-multiple-regression-and-confounding/theory.md)
- [Spurious correlation and autocorrelation](../14-spurious-correlation-and-autocorrelation/theory.md)
- [Outlier detection](../04-outlier-detection/theory.md)
- [Bootstrapping and confidence intervals](../17-bootstrapping-and-confidence-intervals/theory.md)
- Repo note: [Simple linear regression](../../notes/regression/simple_linear_regression.md)
"""

TASK = r"""
# Task: residual analysis and model diagnostics

## Scenario

A food-delivery platform wants to show customers a promised delivery time computed from a regression of delivery time on distance, plus a
safety margin of "two residual standard errors". An analyst reports that the fitted line has an R-squared of about 0.9 and
proposes to ship it. You are the reviewer: before approval you must find out whether the model's assumptions hold and what the safety
margin really covers.

## Data

`data.csv` - 120 deliveries in time order (one every 45 minutes, starting 2026-02-02 08:00).

| column | meaning |
|---|---|
| `ordered_at` | when the order was placed |
| `distance_km` | restaurant-to-customer distance, kilometres |
| `delivery_min` | time from order to delivery, minutes |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Fit `delivery_min = a + b * distance_km` (`SLOPE`, `INTERCEPT`, `RSQ`, `STEYX`). Report all four numbers.
2. Add fitted values and residuals. Compute the standard deviation of the residuals in three distance bands (< 6 km, 6-12 km, >= 12 km).
   What is the ratio far/near?
3. Run the Breusch-Pagan check: regress squared residuals on distance, compute $LM = n R^2$ and the p-value with `CHIDIST(LM,1)`.
4. Compute skewness, excess kurtosis, the share of standardised residuals beyond +-2, and the (approximate) Jarque-Bera statistic.
   Build a normal QQ plot (sorted standardised residuals vs `NORMSINV((i-0.5)/n)`).
5. Compute leverage $h_i = 1/n + (x_i-\bar x)^2/\sum(x_j-\bar x)^2$ and standardised residuals $e_i/(s\sqrt{1-h_i})$. How many orders have $h_i > 4/n$?
6. Compute Cook's distance $D_i = r_i^2 h_i / (2(1-h_i))$. Which orders have the largest values, and what do they look like?
7. Refit the line without the orders with $D_i > 0.5$ (weighted sums via `SUMPRODUCT`). How much does the slope change?
8. Refit with weights $w_i = 1/x_i^2$ (weighted least squares). Compute the SD of (residual / distance) in the three bands. What do you see?
9. *In two or three sentences:* is the "two residual standard errors" margin appropriate for all orders? What would you change before launch?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Residuals vs distance", what shape do the residuals form, and what does that mean for the safety margin on long trips?
- In "Normal QQ plot", which tail departs from the diagonal, and which orders could be responsible?
- In "Cook's distance by order", how many orders exceed the cut-off, and where do they sit in "Delivery time vs distance"?

## Deliverable

A short review note (6-8 lines): verdict (ship / fix first), the three diagnostics that failed with their numbers, the effect on the slope
of the influential orders, and the change you propose. Include one chart.
"""
