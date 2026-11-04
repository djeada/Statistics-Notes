"""Lesson 01 - Distribution shapes and heavy tails."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "01-distribution-shapes-and-heavy-tails"
TITLE = "Distribution shapes and heavy tails"
MODULE = "Understanding data beyond averages"
DATASET = "500 online-shop orders (basket value in EUR, delivery time in hours, channel)"
HILL_K = 25  # number of upper order statistics used by the Hill estimator


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(101)
    n = 500
    t = pd.date_range("2026-04-06 08:00:00", periods=n, freq="11min")
    channel = rng.choice(["web", "app"], size=n, p=[0.6, 0.4])
    body = rng.lognormal(np.log(42), 0.5, n)  # ordinary baskets
    is_tail = rng.random(n) < 0.06  # ~6 % bulk / business orders with a Pareto tail (alpha = 1.8)
    pareto = 150 * (1 - rng.random(n)) ** (-1 / 1.8)
    basket = np.where(is_tail, pareto, body).round(2)
    delivery = np.clip(rng.normal(48, 9, n), 14, None).round(1)  # symmetric, light-tailed contrast
    return pd.DataFrame({"order_id": np.arange(1, n + 1), "timestamp": t, "channel": channel,
                         "basket_value_eur": basket, "delivery_hours": delivery})


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    x = df["basket_value_eur"].to_numpy()
    y = df["delivery_hours"].to_numpy()
    n = len(df)
    skew = lambda v: float(stats.skew(v, bias=False))  # == Excel SKEW
    kurt = lambda v: float(stats.kurtosis(v, bias=False))  # == Excel KURT (excess)
    sd = lambda v: float(np.std(v, ddof=1))
    lx = np.log(x)
    srt = np.sort(x)[::-1]

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 01 - Distribution shapes and heavy tails",
             "Solved workbook. Yellow cells are assumptions you can change; everything else is a live formula.")
    X = b.rng("basket_value_eur")
    Y = b.rng("delivery_hours")
    cb = b.col("basket_value_eur")
    b.add_column("ln_basket", lambda r: f"=LN(Data!{cb}{r})", expected=lx)
    LX = b.rng("ln_basket")
    run_mean = pd.Series(x).expanding().mean().to_numpy()
    run_med = pd.Series(x).expanding().median().to_numpy()
    b.add_column("running_mean", lambda r: f"=AVERAGE(Data!${cb}$2:{cb}{r})", expected=run_mean, fmt="0.00")
    b.add_column("running_median", lambda r: f"=MEDIAN(Data!${cb}$2:{cb}{r})", expected=run_med, fmt="0.00")

    b.section("1. Centre and spread")
    mx_, my_ = b.row("Basket: mean (EUR)", f"=AVERAGE({X})", x.mean(), "0.00"), b.row(
        "Delivery: mean (h)", f"=AVERAGE({Y})", y.mean(), "0.00")
    mdx = b.row("Basket: median (EUR)", f"=MEDIAN({X})", float(np.median(x)), "0.00")
    mdy = b.row("Delivery: median (h)", f"=MEDIAN({Y})", float(np.median(y)), "0.00")
    sdx = b.row("Basket: standard deviation (STDEV.S)", f"=STDEV({X})", sd(x), "0.00")
    sdy = b.row("Delivery: standard deviation (STDEV.S)", f"=STDEV({Y})", sd(y), "0.00")
    rx = b.row("Basket: mean / median", f"={b.local(mx_)}/{b.local(mdx)}", x.mean() / np.median(x), "0.000")
    ry = b.row("Delivery: mean / median", f"={b.local(my_)}/{b.local(mdy)}", y.mean() / np.median(y), "0.000")

    b.section("2. Shape: skewness and excess kurtosis")
    skx = b.row("Basket: SKEW", f"=SKEW({X})", skew(x), "0.000", "adjusted Fisher-Pearson G1")
    kux = b.row("Basket: KURT (excess)", f"=KURT({X})", kurt(x), "0.000", "0 for a normal distribution")
    sky = b.row("Delivery: SKEW", f"=SKEW({Y})", skew(y), "0.000")
    kuy = b.row("Delivery: KURT (excess)", f"=KURT({Y})", kurt(y), "0.000")

    b.section("3. How much is 'within 2 SD'?  (normal data: 95.4 %)")
    inx = b.row("Basket: share within mean +/- 2 SD",
                f"=COUNTIFS({X},\">=\"&({b.local(mx_)}-2*{b.local(sdx)}),{X},\"<=\"&({b.local(mx_)}+2*{b.local(sdx)}))/COUNT({X})",
                float((np.abs(x - x.mean()) <= 2 * sd(x)).mean()), "0.0%")
    iny = b.row("Delivery: share within mean +/- 2 SD",
                f"=COUNTIFS({Y},\">=\"&({b.local(my_)}-2*{b.local(sdy)}),{Y},\"<=\"&({b.local(my_)}+2*{b.local(sdy)}))/COUNT({Y})",
                float((np.abs(y - y.mean()) <= 2 * sd(y)).mean()), "0.0%")
    n3x = b.row("Basket: orders above mean + 3 SD", f"=COUNTIF({X},\">\"&({b.local(mx_)}+3*{b.local(sdx)}))",
                int((x > x.mean() + 3 * sd(x)).sum()), "0")
    below = b.row("Basket: share of orders below the mean", f"=COUNTIF({X},\"<\"&{b.local(mx_)})/COUNT({X})",
                  float((x < x.mean()).mean()), "0.0%")

    b.section("4. Concentration: who generates the revenue?")
    n1, n10 = int(round(n * 0.01)), int(round(n * 0.10))
    top1 = b.row("Revenue share of the top 1 % of orders", f"=SUMIF({X},\">=\"&LARGE({X},{n1}))/SUM({X})",
                 float(srt[:n1].sum() / x.sum()), "0.0%", f"top {n1} orders")
    top10 = b.row("Revenue share of the top 10 % of orders", f"=SUMIF({X},\">=\"&LARGE({X},{n10}))/SUM({X})",
                  float(srt[:n10].sum() / x.sum()), "0.0%", f"top {n10} orders")
    b.row("Largest single order / median order", f"=MAX({X})/{b.local(mdx)}", float(x.max() / np.median(x)), "0.0")

    b.section("5. Log transform")
    lm = b.row("Mean of ln(basket)", f"=AVERAGE({LX})", float(lx.mean()), "0.000")
    gm = b.row("Geometric mean = EXP(mean of ln) (EUR)", f"=EXP({b.local(lm)})", float(np.exp(lx.mean())), "0.00",
               "compare with the median")
    skl = b.row("ln(basket): SKEW", f"=SKEW({LX})", skew(lx), "0.000")
    kul = b.row("ln(basket): KURT (excess)", f"=KURT({LX})", kurt(lx), "0.000")

    b.section("6. Tail index (Hill estimator)")
    k = b.row("k = number of largest orders used", HILL_K, None, "0", "Edit me (try 15, 40)", is_input=True)
    lsrt = np.sort(lx)[::-1]
    hill = b.row("Hill estimate of the tail index alpha",
                 f"=1/(SUMIF({LX},\">=\"&LARGE({LX},{b.local(k)}))/{b.local(k)}-LARGE({LX},{b.local(k)}+1))",
                 float(1 / (lsrt[:HILL_K].mean() - lsrt[HILL_K])), "0.00", "alpha < 2 means infinite variance")

    b.section("7. Does the mean settle down?  (running statistics)")
    rows, exp = [], {}
    for i, m in enumerate(range(50, 501, 50)):
        rows.append([m, f"=AVERAGE(Data!${cb}$2:${cb}${m + 1})", f"=MEDIAN(Data!${cb}$2:${cb}${m + 1})"])
        exp[(i, 1)], exp[(i, 2)] = x[:m].mean(), np.median(x[:m])
    r0, r1 = b.table(["Orders so far", "Mean (EUR)", "Median (EUR)"], rows, fmt={1: "0.00", 2: "0.00"}, expect=exp)
    ms = list(range(50, 501, 50))
    rmean = [float(np.mean(x[:m])) for m in ms]
    rmed = [float(np.median(x[:m])) for m in ms]
    ranges = {}
    ranges["mean"] = b.row("Range of the 10 running means (max - min)", f"=MAX(B{r0}:B{r1})-MIN(B{r0}:B{r1})",
                           max(rmean) - min(rmean), "0.00")
    ranges["median"] = b.row("Range of the 10 running medians (max - min)", f"=MAX(C{r0}:C{r1})-MIN(C{r0}:C{r1})",
                             max(rmed) - min(rmed), "0.00")
    b.line_chart("Running mean vs running median of the basket (EUR)", "timestamp", ["running_mean", "running_median"],
                 anchor="F4", y_title="EUR")

    b.section("8. Histogram on a log scale (bins double in width)")
    edges = [0, 10, 20, 40, 80, 160, 320, 640, 1280]
    rows, exp = [], {}
    first_row = b.next_row + 1
    for i in range(len(edges) - 1):
        lo, hi = edges[i], edges[i + 1]
        r = first_row + i
        rows.append([lo, hi, f"=COUNTIFS({X},\">=\"&A{r},{X},\"<\"&B{r})", f"=C{r}/COUNT({X})"])
        c = int(((x >= lo) & (x < hi)).sum())
        exp[(i, 2)], exp[(i, 3)] = c, c / n
    h0, h1 = b.table(["From (EUR)", "To (EUR)", "Orders", "Share"], rows, fmt={3: "0.0%"}, expect=exp)
    b.bar_chart_from_table("Orders per doubling basket-value bin", 2, [3], h0, h1, anchor="F24", x_title="upper edge, EUR",
                           y_title="orders")
    log_bins = [int(((x >= edges[i]) & (x < edges[i + 1])).sum()) for i in range(len(edges) - 1)]

    top1v, top10v = srt[:n1].sum() / x.sum(), srt[:n10].sum() / x.sum()
    b.answers([
        ("Mean, median, SD of basket and delivery; mean/median ratio", f"={rx}",
         f"Basket: mean {x.mean():.1f} vs median {np.median(x):.1f} EUR (ratio {x.mean() / np.median(x):.2f}), SD {sd(x):.1f}. "
         f"Delivery: mean {y.mean():.1f} vs median {np.median(y):.1f} h (ratio {y.mean() / np.median(y):.3f}). The mean is dragged upward only for the basket."),
        ("SKEW and KURT of both columns", f"={skx}",
         f"Basket: skew {skew(x):.2f}, excess kurtosis {kurt(x):.1f}. Delivery: skew {skew(y):.2f}, kurtosis {kurt(y):.2f}. "
         "Delivery is close to normal (both near 0); the basket is strongly right-skewed with very heavy tails."),
        ("Share within mean +/- 2 SD and count above mean + 3 SD", f"={inx}",
         f"Basket: {(np.abs(x - x.mean()) <= 2 * sd(x)).mean():.1%} within 2 SD (more than the normal 95.4 %, because the extreme orders inflate the SD) "
         f"and {int((x > x.mean() + 3 * sd(x)).sum())} orders beyond mean + 3 SD. Delivery: {(np.abs(y - y.mean()) <= 2 * sd(y)).mean():.1%}."),
        ("Revenue share of the top 1 % and top 10 % of orders; share of orders below the mean", f"={top10}",
         f"Top 1 % ({n1} orders) = {top1v:.1%} of revenue, top 10 % ({n10} orders) = {top10v:.1%}. "
         f"{(x < x.mean()).mean():.0%} of orders are below the mean, so the mean is not a 'typical' basket."),
        ("ln(basket): SKEW, KURT, geometric mean vs median", f"={gm}",
         f"After the log, skew {skew(lx):.2f} and kurtosis {kurt(lx):.2f}: much closer to symmetric, but still right-skewed, since the tail is "
         f"Pareto, not lognormal. Geometric mean {np.exp(lx.mean()):.1f} EUR is close to the median {np.median(x):.1f}."),
        ("Hill estimate of the tail index (k = 25)", f"={hill}",
         f"alpha = {1 / (lsrt[:HILL_K].mean() - lsrt[HILL_K]):.2f} (true generating value 1.8). Below 2, so the population variance is "
         "infinite: the sample SD and the 2-SD rule are not trustworthy for this variable."),
        ("Running mean vs running median at n = 50, 100, ..., 500", f"={ranges['mean']}",
         f"The 10 running means span {min(rmean):.1f} to {max(rmean):.1f} EUR (range {max(rmean) - min(rmean):.1f}); the running medians span "
         f"{min(rmed):.1f} to {max(rmed):.1f} (range {max(rmed) - min(rmed):.1f}). The median settles much faster."),
        ("Which summary for which decision?", "see text",
         "Forecasting total revenue needs the mean (it keeps the tail mass) but with a wide uncertainty; describing the typical customer needs "
         "the median or geometric mean. Limitation: 500 orders contain only ~30 tail orders, so any tail statistic (kurtosis, alpha, top share) is noisy."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-01-distribution-shapes", "01 · Distribution shapes and heavy tails",
             "Basket value vs delivery time: mean vs median, skewness, kurtosis, concentration and the log-log tail "
             "(values computed from data.csv).", df.rename(columns={"timestamp": "time"}), "time")
    d.stat("Basket value: the mean is not the typical order (EUR)",
           {"mean": x.mean(), "median": np.median(x), "SD": sd(x), "skew": skew(x), "excess kurtosis": kurt(x),
            "top 10% revenue share (%)": 100 * top10v}, "Basket value, all 500 orders.", decimals=1,
           thresholds=[(None, "blue")])
    # linear histogram (EUR 50 bins, last = 500+)
    bins = np.arange(0, 550, 50)
    cnt, _ = np.histogram(np.clip(x, 0, 549), bins=bins)
    d.bars("Basket value histogram, linear scale (50 EUR bins)", pd.DataFrame(
        {"bucket_eur": [f"{int(a)}-{int(a) + 50}" if a < 500 else "500+" for a in bins[:-1]], "orders": cnt}),
        "On a linear axis the body is squeezed into 3 bars and the tail is invisible.")
    d.bars("Basket value histogram, log scale (bins double)", pd.DataFrame(
        {"bucket_eur": [f"{edges[i]}-{edges[i + 1]}" for i in range(len(edges) - 1)], "orders": log_bins}),
        "Doubling bins: the body looks roughly lognormal and the tail runs out slowly.")
    run = pd.DataFrame({"time": df["timestamp"], "running_mean": run_mean, "running_median": run_med})
    d.timeseries("Running mean vs running median (EUR)", run,
                 "The mean keeps jumping each time a large order arrives; the median hardly moves.", unit="none")
    # log-log survival plot
    xs = np.sort(x)
    surv = 1 - np.arange(n) / n  # P(X >= x_i)
    lx10, ls10 = np.log10(xs), np.log10(surv)
    xk = np.sort(x)[::-1][HILL_K]  # threshold = (k+1)th largest
    alpha = 1 / (lsrt[:HILL_K].mean() - lsrt[HILL_K])
    fit = np.minimum(0.0, np.log10(HILL_K / n) - alpha * (lx10 - np.log10(xk)))  # Pareto line through the tail, extrapolated and capped at P = 1
    sdf = pd.DataFrame({"log10_basket": lx10, "log10_survival": ls10, "pareto_fit": fit})
    d.xy("Log-log survival plot of basket value", sdf, "log10_basket", ["log10_survival", "pareto_fit"],
         f"log10 P(X >= x) against log10 x. A straight line means a power-law tail; slope -alpha (Hill alpha = {alpha:.2f}).",
         lines=["pareto_fit"])
    dd = np.arange(10, 90, 6)
    cntd, _ = np.histogram(np.clip(y, 10, 83.9), bins=dd)
    d.bars("Delivery time histogram (6-hour bins): the symmetric contrast", pd.DataFrame(
        {"bucket_h": [f"{a}-{a + 6}" for a in dd[:-1]], "orders": cntd}), "Bell-shaped; mean and median coincide.")
    tbl = pd.DataFrame({"statistic": ["mean", "median", "SD", "SKEW", "excess KURT", "share within mean +/- 2 SD (%)"],
                        "basket_value_eur": [x.mean(), np.median(x), sd(x), skew(x), kurt(x),
                                             100 * (np.abs(x - x.mean()) <= 2 * sd(x)).mean()],
                        "delivery_hours": [y.mean(), np.median(y), sd(y), skew(y), kurt(y),
                                           100 * (np.abs(y - y.mean()) <= 2 * sd(y)).mean()]}).round(2)
    d.table("Basket vs delivery: shape statistics", tbl, "Same style of summary, very different shapes.")
    d.save(out)

    # ------------------------------------------------------------------ markdown
    vals = theory_values(x, y)
    md(out / "theory.md", fill(THEORY, vals))
    md(out / "task.md", fill(TASK, {"k": HILL_K}))
    return b


def fill(text: str, vals: dict) -> str:
    for k, v in vals.items():
        text = text.replace(f"<<{k}>>", str(v))
    return text


def theory_values(x, y) -> dict:
    ex = np.array([2, 3, 3, 4, 5, 6, 100.0])
    m, med = ex.mean(), np.median(ex)
    s = np.std(ex, ddof=1)
    return {
        "ex_mean": f"{m:.2f}", "ex_ratio": f"{m / ex[:-1].mean():.1f}", "ex_med": f"{med:.0f}", "ex_sd": f"{s:.2f}",
        "ex_skew": f"{stats.skew(ex, bias=False):.2f}", "ex_kurt": f"{stats.kurtosis(ex, bias=False):.2f}",
        "ex_skew_wo": f"{stats.skew(ex[:-1], bias=False):.2f}", "ex_mean_wo": f"{ex[:-1].mean():.2f}",
        "ex_med_wo": f"{np.median(ex[:-1]):.1f}",
        "ln_mean": f"{42 * np.exp(0.5 ** 2 / 2):.1f}", "ln_med": "42", "ln_ratio": f"{np.exp(0.5 ** 2 / 2):.3f}",
        "ln_ratio2": f"{np.exp(1.0 ** 2 / 2):.3f}",
        "p_tail": f"{(150 / 600) ** 1.8 * 100:.1f}",
        "p_tail2": f"{(150 / 1200) ** 1.8 * 100:.2f}",
        "basket_skew": f"{stats.skew(x, bias=False):.1f}", "basket_n": len(x),
    }


THEORY = r"""
# Theory: distribution shapes and heavy tails

## Why the shape matters before any statistic

Every summary statistic is a compromise, and which compromise is sensible depends on the **shape** of the distribution.
For a symmetric, thin-tailed variable the mean, median and mode agree and the standard deviation (SD) describes spread well.
For basket values, session lengths, incomes, file sizes or incident costs they do not agree, and quoting "mean +/- SD" can
be actively misleading. Looking at the shape first prevents two classic failures: reporting an "average customer" who does
not exist, and trusting a $\pm 2$ SD rule that only works for bell curves.

## Describing shape with moments

For a sample $x_1,\dots,x_n$ with mean $\bar x$ and standard deviation $s$ (denominator $n-1$, `STDEV.S`), the
**skewness** measures asymmetry and the **excess kurtosis** measures tail weight relative to a normal distribution:

$$
g_1 = \frac{1}{n}\sum_{i=1}^n \left(\frac{x_i-\bar x}{s}\right)^3,\qquad
g_2 = \frac{1}{n}\sum_{i=1}^n \left(\frac{x_i-\bar x}{s}\right)^4 - 3 .
$$

Spreadsheets apply small-sample corrections: Excel/Sheets `SKEW` returns the adjusted $G_1 = g_1\sqrt{n(n-1)}/(n-2)$ and
`KURT` returns the adjusted *excess* kurtosis $G_2$. They are exactly `scipy.stats.skew(x, bias=False)` and
`scipy.stats.kurtosis(x, bias=False)`; this course uses the spreadsheet versions. A normal distribution has skewness 0 and
excess kurtosis 0. Positive skew means a long right tail; positive excess kurtosis means more probability far from the centre
(and, perhaps counter-intuitively, usually also more mass near the centre) than a normal with the same SD.

Because the third and fourth powers weigh large deviations enormously, **one point can dominate both numbers**.

### Worked example

Take $\{2,3,3,4,5,6,100\}$. The mean is <<ex_mean>>, the median <<ex_med>>, $s = <<ex_sd>>$, `SKEW` = <<ex_skew>>,
`KURT` = <<ex_kurt>>. Remove the 100 and the same statistics are mean <<ex_mean_wo>>, median <<ex_med_wo>>, `SKEW` = <<ex_skew_wo>>.
One observation out of seven multiplied the mean by <<ex_ratio>>, but moved the median only from <<ex_med_wo>> to <<ex_med>>.

## Mean, median and the ordering of the three

For a right-skewed variable the usual ordering is mode < median < mean. The mean/median ratio is a quick skew diagnostic: close
to 1 for symmetric data, well above 1 for right-skewed positive data.

## Lognormal and power-law tails

Two families produce most real right-skewed data.

**Lognormal.** If $\ln X \sim N(\mu,\sigma^2)$ then $X$ has median $e^{\mu}$ and mean $e^{\mu+\sigma^2/2}$, so
mean/median $= e^{\sigma^2/2}$. With $\mu=\ln 42$ and $\sigma=0.5$ the median is <<ln_med>> and the mean <<ln_mean>>
(ratio <<ln_ratio>>); with $\sigma=1$ the ratio is already <<ln_ratio2>>. All moments exist, and a log transform makes the data normal.
The geometric mean $\exp(\bar{\ln x})$ estimates the median $e^{\mu}$.

**Power law (Pareto).** The survival function is $P(X>x) = (x_m/x)^{\alpha}$ for $x\ge x_m$. On a log-log plot of
$P(X>x)$ against $x$ this is a straight line with slope $-\alpha$. The **tail index** $\alpha$ controls which moments exist:
$E[X^k]$ is finite only for $k<\alpha$. For $\alpha\le 2$ the variance is infinite; for $\alpha\le 1$ even the mean is.
With $x_m=150$ and $\alpha=1.8$, $P(X>600) = <<p_tail>>\,\%$ and $P(X>1200) = <<p_tail2>>\,\%$: each doubling of the threshold
removes only a factor $2^{1.8}\approx 3.5$ of the probability, where a normal tail would fall away vastly faster.

The **Hill estimator** uses the $k$ largest observations $x_{(1)}\ge\dots\ge x_{(n)}$:

$$
\hat\alpha = \left[\frac{1}{k}\sum_{i=1}^{k}\ln x_{(i)} - \ln x_{(k+1)}\right]^{-1}.
$$

It is only meaningful for the tail (choose $k$ so that the log-log plot is straight above $x_{(k+1)}$), and it is noisy for small $k$
and biased for large $k$.

## What heavy tails do to familiar tools

- **The mean converges slowly** or not at all. Even when the mean exists, a handful of tail orders decide the total; the running
  mean keeps jumping, the running median settles quickly (lesson [2](../02-robust-statistics/theory.md)).
- **Rules based on $\bar x \pm k s$ break.** The SD is inflated by the very points you want to detect, so more data fall within
  $\pm 2$ SD than the 95.4 % of a normal (see [outlier detection](../04-outlier-detection/theory.md)).
- **Concentration:** in a heavy-tailed population a few percent of units produce a large share of the total. Report the share
  of the top 1 % and 10 %, not only an average.
- **Log transform:** analysing $\ln x$ often restores symmetry (lognormal) and linearises multiplicative effects, but a Pareto
  tail stays right-skewed after the log, and the back-transformed mean of logs is the geometric mean, not the arithmetic mean.

## Assumptions and pitfalls

1. **Skewness and kurtosis from small samples are unstable.** With about 5 % of the observations in the tail, a sample of
   a few hundred contains only a few dozen tail points; treat $g_2$ and $\hat\alpha$ as rough indications.
2. **Kurtosis is not "peakedness".** It measures the contribution of extreme deviations; compare shapes with a histogram.
3. **A single threshold hides the shape.** A linear histogram of heavy-tailed data shows one tall bar and an empty axis;
   use a log scale or a log-log survival plot.
4. **Mixtures look like heavy tails.** The basket data here are a mixture (ordinary orders plus a few business orders).
   Segment first; the heavy tail may come from one identifiable group.
5. **Do not delete the tail to "fix" the shape.** The tail orders are real revenue; decide per question whether the mean
   (totals) or a robust centre (typical case) is the right summary.

## Related notes

- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)
- [Robust statistics](../02-robust-statistics/theory.md)
- [Descriptive statistics](../../notes/foundations/descriptive_statistics.md) and
  [statistical moments](../../notes/random_variables_and_distributions/statistical_moments.md)
- [Bootstrapping confidence intervals](../17-bootstrapping-and-confidence-intervals/theory.md)
"""

TASK = r"""
# Task: distribution shapes and heavy tails

## Scenario

You analyse an online shop that is preparing a revenue forecast and a delivery-time promise. The finance lead quotes
"the average order is about 60 EUR with a standard deviation of 83", and the logistics lead says "delivery takes 48 hours,
give or take 9". You are asked whether the same style of summary is appropriate for both numbers, and which figure you
would put in a plan for (a) total revenue and (b) the typical customer.

## Data

`data.csv` - 500 consecutive orders, one every 11 minutes.

| column | meaning |
|---|---|
| `order_id` | running number |
| `timestamp` | when the order was placed |
| `channel` | `web` or `app` |
| `basket_value_eur` | order value in EUR |
| `delivery_hours` | hours from order to delivery |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`. Use `STDEV.S`, `SKEW` and `KURT` (excess).

1. Compute mean, median and standard deviation of `basket_value_eur` and `delivery_hours`, and the mean/median ratio of each.
2. Compute `SKEW` and `KURT` for both columns. Which column looks normal and which does not?
3. What share of observations lies within mean $\pm$ 2 SD in each column? How many baskets exceed mean + 3 SD? Compare with the 95.4 % expected for a normal distribution.
4. What share of total revenue comes from the top 1 % and the top 10 % of orders? What share of orders is below the mean basket?
5. Add a column $\ln(\text{basket})$. Compute its `SKEW` and `KURT`, the geometric mean $e^{\overline{\ln x}}$ and compare with the median.
6. Estimate the tail index $\alpha$ of the basket value with the Hill estimator using the {k} largest orders. What does a value below 2 imply for the standard deviation?
7. Compute the mean and median of the first 50, 100, ..., 500 orders. Which of the two settles down faster?
8. Build a histogram with doubling bins (0-10, 10-20, 20-40, ..., 640-1280). *Explain in three sentences* which summary you would use for the revenue forecast and which for the "typical customer", and one limitation of the 500-order sample for tail statistics.

## Grafana

Import `grafana/dashboard.json` (no data-source setup is needed).

- Compare the two histograms of basket value. What does the linear scale hide that the log scale shows?
- In "Running mean vs running median", find the jumps of the mean. What kind of order causes each jump, and why does the median ignore them?
- In the log-log survival plot, over which range of basket values is the curve a straight line, and what is its slope?

## Deliverable

A short note (6-10 lines) titled *What is a typical order, and what drives total revenue?* with three named parts: **Shape**
(skewness, kurtosis, mean vs median), **Tail** (concentration and tail index) and **Recommendation** (which summary for
which decision). Include one chart and state one limitation.
"""
