"""Lesson 17 - Bootstrapping and confidence intervals."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import HEADER_FILL, HEADER_FONT, Book, Dash, md, write_csv  # noqa: E402

SLUG = "17-bootstrapping-and-confidence-intervals"
TITLE = "Bootstrapping and confidence intervals"
MODULE = "Uncertainty and statistical inference"
DATASET = "30 support tickets (resolution hours) + 400 pre-generated bootstrap resamples"
N, B = 30, 400
PROMISE_H = 8.0  # the "average resolution under 8 hours" promise


def make_data():
    rng = np.random.default_rng(1707)
    x = np.round(rng.lognormal(np.log(6.0), 0.75, N), 1)
    idx = rng.integers(1, N + 1, size=(B, N))  # 1-based ticket numbers drawn with replacement
    return x, idx


def build(out: Path) -> Book:
    x, idx = make_data()
    cols = {"ticket_id": np.r_[np.arange(1, N + 1), np.full(B - N, np.nan)],
            "resolution_hours": np.r_[x, np.full(B - N, np.nan)],
            "resample": np.arange(1, B + 1)}
    for j in range(N):
        cols[f"draw_{j + 1:02d}"] = idx[:, j]
    df = pd.DataFrame(cols)
    csv = df.copy()
    csv["ticket_id"] = csv["ticket_id"].astype("Int64")
    write_csv(out, csv)

    bm = x[idx - 1].mean(axis=1)
    bmed = np.median(x[idx - 1], axis=1)
    q = lambda a, p: float(np.percentile(a, p))
    n = N
    mean, med, sd = float(x.mean()), float(np.median(x)), float(x.std(ddof=1))
    se = sd / np.sqrt(n)
    tcrit = float(stats.t.ppf(0.975, n - 1))
    t_lo, t_hi = mean - tcrit * se, mean + tcrit * se
    b_lo, b_hi = q(bm, 2.5), q(bm, 97.5)
    m_lo, m_hi = q(bmed, 2.5), q(bmed, 97.5)
    bse = float(bm.std(ddof=1))

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 17 - Bootstrapping and confidence intervals",
             "Data = 30 tickets + pre-generated resample indexes. 'Resamples' turns each index row into a resample.")
    X = f"Data!$B$2:$B${N + 1}"

    # Resamples sheet: value cells INDEX(x, draw) + mean + median per resample
    rs = b.wb.create_sheet("Resamples", 1)
    rs.cell(row=1, column=1, value="resample")
    for j in range(N):
        rs.cell(row=1, column=2 + j, value=f"v{j + 1:02d}")
    cm, cd = 2 + N, 3 + N
    rs.cell(row=1, column=cm, value="mean")
    rs.cell(row=1, column=cd, value="median")
    for c in range(1, cd + 1):
        rs.cell(row=1, column=c).fill, rs.cell(row=1, column=c).font = HEADER_FILL, HEADER_FONT
    first_draw = int(b.col("draw_01") and 4)  # draw_01 is column D on Data
    for r in range(2, B + 2):
        rs.cell(row=r, column=1, value=f"=Data!C{r}")
        for j in range(N):
            dcol = get_column_letter(first_draw + j)
            rs.cell(row=r, column=2 + j, value=f"=INDEX({X},Data!{dcol}{r})")
        v0, v1 = get_column_letter(2), get_column_letter(1 + N)
        rs.cell(row=r, column=cm, value=f"=AVERAGE({v0}{r}:{v1}{r})").number_format = "0.000"
        rs.cell(row=r, column=cd, value=f"=MEDIAN({v0}{r}:{v1}{r})").number_format = "0.000"
        b.checks.append((f"Resamples!{get_column_letter(cm)}{r}", f"resample mean {r}", float(bm[r - 2])))
        b.checks.append((f"Resamples!{get_column_letter(cd)}{r}", f"resample median {r}", float(bmed[r - 2])))
    Lm, Ld = get_column_letter(cm), get_column_letter(cd)
    BM = f"Resamples!${Lm}$2:${Lm}${B + 1}"
    BD = f"Resamples!${Ld}$2:${Ld}${B + 1}"

    b.section("1. The sample")
    b.row("n", f"=COUNT({X})", n, "0")
    r_mean = b.row("Sample mean (h)", f"=AVERAGE({X})", mean, "0.00")
    r_med = b.row("Sample median (h)", f"=MEDIAN({X})", med, "0.00")
    r_sd = b.row("Sample SD (h)", f"=STDEV({X})", sd, "0.00")
    b.row("Skewness", f"=SKEW({X})", float(stats.skew(x, bias=False)), "0.00", "Positive = long right tail")
    b.row("Largest ticket (h)", f"=MAX({X})", float(x.max()), "0.0")

    b.section("2. Classical t interval for the mean")
    conf = b.row("Confidence level", 0.95, None, "0%", "Edit me (try 0.90, 0.99)", is_input=True)
    alpha = f"(1-{b.local(conf)})"
    r_se = b.row("Standard error s / sqrt(n)", f"={b.local(r_sd)}/SQRT(COUNT({X}))", se, "0.000")
    r_tc = b.row("t critical value (n-1 df)", f"=TINV({alpha},COUNT({X})-1)", tcrit, "0.000")
    r_tlo = b.row("t interval: lower (h)", f"={b.local(r_mean)}-{b.local(r_tc)}*{b.local(r_se)}", t_lo, "0.00")
    r_thi = b.row("t interval: upper (h)", f"={b.local(r_mean)}+{b.local(r_tc)}*{b.local(r_se)}", t_hi, "0.00")
    promise = b.row("Promise: mean resolution under (h)", PROMISE_H, None, "0.0", is_input=True)
    b.row("Does the t interval contain the promise?",
          f'=IF(AND({b.local(r_tlo)}<={b.local(promise)},{b.local(r_thi)}>={b.local(promise)}),"yes","no")', None)

    b.section("3. Bootstrap distribution of the mean (400 resamples)")
    b.row("Number of resamples", f"=COUNT({BM})", B, "0")
    r_bmean = b.row("Mean of the resample means (h)", f"=AVERAGE({BM})", float(bm.mean()), "0.000")
    b.row("Bootstrap bias (mean of means - sample mean)", f"={b.local(r_bmean)}-{b.local(r_mean)}", float(bm.mean() - mean),
          "0.000", "Close to 0 for a mean")
    r_bse = b.row("Bootstrap standard error (h)", f"=STDEV({BM})", bse, "0.000", "Compare with s/sqrt(n)")
    r_blo = b.row("Percentile interval: lower (h)", f"=PERCENTILE({BM},{alpha}/2)", b_lo, "0.00")
    r_bhi = b.row("Percentile interval: upper (h)", f"=PERCENTILE({BM},1-{alpha}/2)", b_hi, "0.00")
    r_tw = b.row("Width of t interval (h)", f"={b.local(r_thi)}-{b.local(r_tlo)}", t_hi - t_lo, "0.00")
    r_bw = b.row("Width of bootstrap interval (h)", f"={b.local(r_bhi)}-{b.local(r_blo)}", b_hi - b_lo, "0.00")
    r_asym_t = b.row("t: upper arm / lower arm", f"=({b.local(r_thi)}-{b.local(r_mean)})/({b.local(r_mean)}-{b.local(r_tlo)})",
                     (t_hi - mean) / (mean - t_lo), "0.00", "Always 1: the t interval is symmetric")
    r_asym_b = b.row("Bootstrap: upper arm / lower arm",
                     f"=({b.local(r_bhi)}-{b.local(r_mean)})/({b.local(r_mean)}-{b.local(r_blo)})",
                     (b_hi - mean) / (mean - b_lo), "0.00", "> 1: the data say the mean can be much higher than observed")

    b.section("4. Bootstrap interval for the median (no simple formula exists)")
    r_mlo = b.row("Median: lower (h)", f"=PERCENTILE({BD},{alpha}/2)", m_lo, "0.00")
    r_mhi = b.row("Median: upper (h)", f"=PERCENTILE({BD},1-{alpha}/2)", m_hi, "0.00")
    b.row("Bootstrap standard error of the median (h)", f"=STDEV({BD})", float(bmed.std(ddof=1)), "0.000")

    b.section("5. Convergence: how many resamples are enough?")
    ks = [25, 50, 100, 200, 300, 400]
    rows, exp = [], {}
    for i, k in enumerate(ks):
        rk = f"Resamples!${Lm}$2:${Lm}${k + 1}"
        rows.append([k, f"=PERCENTILE({rk},0.025)", f"=PERCENTILE({rk},0.975)", f"=C{b.next_row + 1 + i}-B{b.next_row + 1 + i}"])
        lo, hi = q(bm[:k], 2.5), q(bm[:k], 97.5)
        exp.update({(i, 1): lo, (i, 2): hi, (i, 3): hi - lo})
    c0, c1 = b.table(["Resamples used", "Lower 2.5%", "Upper 97.5%", "Width"], rows, fmt={1: "0.00", 2: "0.00", 3: "0.00"}, expect=exp)
    b.line_chart_from_table("95% interval ends vs number of resamples", 1, [2, 3], c0, c1, anchor="H4", y_title="hours")

    b.section("6. Histogram of the bootstrap means (0.5 h buckets)")
    lo_e = np.floor(bm.min() * 2) / 2
    edges = np.arange(lo_e, bm.max() + 0.5, 0.5)
    rows, exp = [], {}
    cnt, _ = np.histogram(bm, bins=np.r_[edges, edges[-1] + 0.5])
    for i, e in enumerate(edges):
        rr = b.next_row + 1 + i
        rows.append([f"{e:.1f}", e, f'=COUNTIFS({BM},">="&B{rr},{BM},"<"&B{rr}+0.5)'])
        exp[(i, 2)] = float(cnt[i])
    h0, h1 = b.table(["Bucket", "From (h)", "Resamples"], rows, fmt={1: "0.0", 2: "0"}, expect=exp)
    b.bar_chart_from_table("Bootstrap distribution of the mean", 1, [3], h0, h1, anchor="H24", x_title="mean resolution time (h)",
                           y_title="resamples")

    b.answers([
        ("Mean, median, SD, skewness, max", f"={r_mean}",
         f"Mean {mean:.2f} h, median {med:.2f} h, SD {sd:.2f} h. The mean is {mean - med:.1f} h above the median and the largest "
         f"ticket took {x.max():.1f} h: right-skewed."),
        ("Standard error and 95% t interval; does it contain 8 h?", f"={r_tlo}",
         f"SE = {se:.2f} h, t interval [{t_lo:.2f}, {t_hi:.2f}] h. It contains the {PROMISE_H:.0f} h promise, so the data cannot "
         f"show the promise is broken - nor that it is kept."),
        ("Bootstrap standard error of the mean", f"={r_bse}",
         f"{bse:.3f} h from 400 resamples vs {se:.3f} h from the formula: the two routes agree on the spread."),
        ("95% percentile bootstrap interval for the mean; compare with t", f"={r_blo}",
         f"[{b_lo:.2f}, {b_hi:.2f}] h vs t [{t_lo:.2f}, {t_hi:.2f}] h. The bootstrap interval is narrower ({b_hi - b_lo:.2f} h vs {t_hi - t_lo:.2f} h) and asymmetric: upper arm "
         f"{(b_hi - mean):.2f} h, lower arm {(mean - b_lo):.2f} h - the t interval is forced to be symmetric."),
        ("Bootstrap 95% interval for the median", f"={r_mlo}",
         f"[{m_lo:.2f}, {m_hi:.2f}] h around a median of {med:.2f} h. The 'typical' ticket is clearly resolved faster than the mean suggests."),
        ("Convergence with 50, 100, 200, 400 resamples", f"=Analysis!C{c0 + 3}",
         "Upper end with 50 / 100 / 200 / 400 resamples: " + " / ".join(f"{q(bm[:k], 97.5):.2f}" for k in (50, 100, 200, 400)) +
         " h - the ends still move by up to a whole hour between B = 50 and B = 400, so use 1000+ for a final report."),
        ("Bootstrap bias of the mean", f"={r_bmean}",
         f"Mean of resample means {bm.mean():.3f} vs sample mean {mean:.3f}: bias {bm.mean() - mean:+.3f} h, negligible for a mean."),
        ("Effect of the confidence level", f"={conf}",
         "Set the yellow cell to 0.90 or 0.99: higher confidence = wider interval (cost of certainty). "
         f"At 90%: t [{mean - stats.t.ppf(.95, n - 1) * se:.2f}, {mean + stats.t.ppf(.95, n - 1) * se:.2f}], "
         f"bootstrap [{q(bm, 5):.2f}, {q(bm, 95):.2f}]."),
        ("Interpretation of the 95% interval and limits", "text",
         "Not 'a 95% probability the true mean is inside this interval' - the true mean is fixed; the *procedure* captures it in "
         "95% of repeated samples. With n = 30 and one 38.8 h ticket the percentile interval is itself uncertain, and it assumes "
         "tickets are independent and representative."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-17-bootstrap", "17 · Bootstrapping and confidence intervals",
             "A skewed sample of 30 ticket resolution times: classical t interval vs percentile bootstrap (400 resamples).")
    d.stat("Estimates and 95% intervals (hours)", {"mean": mean, "median": med, "t lower": t_lo, "t upper": t_hi,
                                                   "bootstrap lower": b_lo, "bootstrap upper": b_hi},
           "Mean with the symmetric t interval and the percentile bootstrap interval.", unit="h", decimals=2)
    hb = np.arange(0, 44, 4)
    hc, _ = np.histogram(x, bins=np.r_[hb, 100])
    d.bars("The data: resolution time (4 h buckets)", pd.DataFrame(
        {"bucket_h": [f"{a}-{a + 4}" if a < 40 else "40+" for a in hb], "tickets": hc}),
           "30 tickets. Right-skewed: a few very slow tickets.", w=8)

    def hist(vals, lo, hi, step, label):
        e = np.arange(np.floor(vals.min() / step) * step, vals.max() + step, step)
        c, _ = np.histogram(vals, bins=np.r_[e, e[-1] + step])
        mid = e + step / 2
        inside = (mid >= lo) & (mid <= hi)
        return pd.DataFrame({label: [f"{a:.0f}-{a + step:.0f}" for a in e],
                             "inside 95% interval": np.where(inside & (c > 0), c, np.nan),
                             "outside": np.where(~inside & (c > 0), c, np.nan)})

    d.bars("Bootstrap distribution of the mean", hist(bm, b_lo, b_hi, 1.0, "mean_h"),
           "400 resample means; the middle 95% (blue) is the percentile interval. Note the long right arm.", stacking="normal", w=8)
    d.panels[-1]["options"]["showValue"] = "never"
    d.bars("Bootstrap distribution of the median", hist(bmed, m_lo, m_hi, 1.0, "median_h"),
           "Medians of the same 400 resamples; discrete because a median is one of the observed values.", stacking="normal", w=8)
    d.panels[-1]["options"]["showValue"] = "never"
    ci = pd.DataFrame({"method": ["t interval (mean)", "bootstrap (mean)", "bootstrap (median)"],
                       "lower_h": [t_lo, b_lo, m_lo], "estimate_h": [mean, mean, med], "upper_h": [t_hi, b_hi, m_hi]}).round(2)
    d.table("Interval comparison", ci, "Same data, three intervals.", w=12)
    kk = np.arange(25, B + 1, 25)
    d.xy("Interval ends vs number of resamples", pd.DataFrame(
        {"resamples": kk, "lower": [q(bm[:k], 2.5) for k in kk], "upper": [q(bm[:k], 97.5) for k in kk]}),
         "resamples", ["lower", "upper"], "The ends settle down as B grows; 400 is the minimum for a stable interval.",
         lines=["lower", "upper"], w=12)
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK.format(promise=int(PROMISE_H)))
    return b


THEORY = r"""
# Theory: bootstrapping and confidence intervals

## The problem: one sample, no repeat experiments

You measured 30 tickets and the mean is 9.4 hours. How far could the *true* mean be from that? Classical statistics answers
with a formula built on assumptions (normal data, or a sample large enough for the CLT, see
[sampling distributions](../16-sampling-distributions-and-the-clt/theory.md)). The **bootstrap** answers with a
computer: treat the sample as a stand-in for the population, redraw samples from it, and watch how much the statistic
moves. It works for statistics that have no convenient formula (median, percentile, ratio, trimmed mean).

## The percentile bootstrap

Given data $x_1,\dots,x_n$ and a statistic $\hat\theta = T(x_1,\dots,x_n)$:

1. Draw $n$ values **with replacement** from the data: a *resample* $x^*_1,\dots,x^*_n$ (some points appear twice, some not at all).
2. Compute $\hat\theta^* = T(x^*_1,\dots,x^*_n)$.
3. Repeat $B$ times to get $\hat\theta^*_1,\dots,\hat\theta^*_B$.

The distribution of $\hat\theta^*$ approximates the sampling distribution of $\hat\theta$. Then:

- **bootstrap standard error**: $\widehat{SE}_{boot} = \text{sd}(\hat\theta^*_1,\dots,\hat\theta^*_B)$;
- **percentile interval** with confidence $1-\alpha$: $[\,q_{\alpha/2},\ q_{1-\alpha/2}\,]$, the empirical quantiles of the $\hat\theta^*$ values.

In a spreadsheet no `RAND` is needed: pre-generate an index table (row = resample, column = position, entry = which observation
to take), look values up with `INDEX`, and use `AVERAGE`, `MEDIAN` or `PERCENTILE` on the resulting rows. That is exactly
what the *Resamples* sheet of the solution does, and why the answers never change when you recalculate.

## The classical interval for comparison

For a mean, $\bar x \pm t_{n-1,\,1-\alpha/2}\; s/\sqrt n$ (`TINV(alpha, n-1)` in Excel and Sheets, which is two-sided).
It assumes the sample mean is approximately normal and is **always symmetric** around $\bar x$.

## Worked example ($n = 5$, computed)

Data $\{4, 6, 7, 9, 14\}$: $\bar x = 8$, $s = 3.808$, $s/\sqrt n = 1.703$, $t_{4,0.975} = 2.776$, so the t interval is
$8 \pm 4.73 = [3.27,\ 12.73]$. Three example resamples: $\{7,4,7,14,9\}$ has mean 8.2, $\{14,14,6,9,4\}$ has mean 9.4,
$\{4,6,6,7,9\}$ has mean 6.4. With $B = 2000$ resamples the bootstrap standard error is about 1.51 (the plug-in value is
$\sqrt{(n-1)/n}\,s/\sqrt n = 1.52$) and the percentile interval is about $[5.4,\ 11.0]$. Notice what happened: the
bootstrap interval is **narrower** than the t interval, and shifted up. With $n=5$ the percentile bootstrap does not pay the
price for estimating $\sigma$ that the t quantile builds in, so it tends to be too optimistic. The bootstrap is not magic for tiny samples.

## What "95 %" means

A 95 % interval is the output of a **procedure**: if you repeated the whole study many times and built an interval each
time, about 95 % of those intervals would contain the true value. For *this* interval the truth is either inside or
not; saying "there is a 95 % probability that the true mean lies in $[7.0, 12.4]$" is a Bayesian statement the frequentist
interval does not make. Width, not coverage, is what you control with $n$: halving the width needs about four times the data.

## Assumptions

- Observations are **independent** and drawn from the population you care about (a biased sample bootstraps to a biased answer).
- The sample is large and representative enough to mimic the population; the bootstrap cannot add information that
  is not in the data.
- The statistic is *smooth enough*: means, medians (with mild caveats), percentiles in the body of the distribution.

## When it fails and common pitfalls

1. **Extremes**: the bootstrap of the maximum or of P99.9 is wrong - a resample can never exceed the observed maximum
   (see [percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)).
2. **Tiny $n$ or heavy tails**: percentile intervals under-cover (see the example above); with $n < 15$ prefer exact methods.
3. **Dependent data**: resampling individual points from an autocorrelated series destroys the dependence; use block
   bootstrap.
4. **Too few resamples**: $B = 400$ fits a spreadsheet, but the interval ends are still noisy (they move by tenths of an hour); use at least 1000-10000 in code.
5. **Skew**: with right-skewed data the bootstrap interval is asymmetric (long upper arm). Forcing a symmetric interval hides
   how high the true mean could plausibly be.
6. Confusing the **standard deviation of the data** (spread of individuals) with the **standard error** (uncertainty of the estimate).

## Connections

- The bootstrap distribution is an empirical [sampling distribution](../16-sampling-distributions-and-the-clt/theory.md).
- [Permutation tests](../18-permutation-tests/theory.md) resample *without* replacement to test a hypothesis; the
  bootstrap resamples *with* replacement to estimate uncertainty.
- [Robust statistics](../02-robust-statistics/theory.md) provides the medians and trimmed means whose uncertainty only the bootstrap can quantify easily.
- Repo notes: [resampling](../../notes/resampling_and_model_assessment/resampling.md),
  [confidence intervals](../../notes/hypothesis_testing_and_confidence_intervals/confidence_intervals.md).
"""

TASK = r"""
# Task: how long does a ticket take to resolve?

## Scenario

A support team advertises that its **average ticket resolution time is under {promise} hours**. Management has a sample of 30
resolved tickets and asks: *can we keep making this promise?* The times are clearly not bell-shaped, so you decide to
compare the textbook interval with a bootstrap interval. Random draws were generated in advance so every analyst gets the
same resamples.

## Data

`data.csv` - two blocks in one table:

| column | meaning |
|---|---|
| `ticket_id` | 1-30 (rows 1-30 only; blank below) |
| `resolution_hours` | time from opening to resolution, hours (rows 1-30 only) |
| `resample` | resample number 1-400 |
| `draw_01` ... `draw_30` | for resample `r`, the 30 ticket numbers drawn **with replacement** (so `draw_05 = 17` means "the 5th value of resample `r` is ticket 17") |

n = 30 tickets; 400 resamples of size 30. A resample value is `=INDEX(resolution_hours range, draw cell)`.

## Questions

1. Compute the mean, median, standard deviation, skewness and largest value of `resolution_hours`.
2. Compute the standard error of the mean and the **95 % t interval** (`TINV`). Does it contain the {promise} h promise?
3. Build the 400 resamples (30 `INDEX` lookups each) and compute the mean of every resample. What is the **bootstrap standard error**
   (standard deviation of the 400 means)? Compare with $s/\sqrt n$.
4. Compute the **95 % percentile bootstrap interval** for the mean. Compare its width and its shape (distance from the sample mean to each end) with the t interval.
5. Compute the bootstrap interval for the **median**. Why can't you get this one from a simple formula?
6. Recompute the interval using only the first 50, 100, 200 and 400 resamples. How stable are the ends?
7. What is the bootstrap **bias** (mean of the resample means minus the sample mean)?
8. Change the confidence level to 90 % and 99 %. What happens to both intervals?
9. *Interpretation:* in two or three sentences, state what the 95 % interval means (and what it does not), and name one reason to
   distrust the interval with this sample.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "The data" panel, describe the shape. What does it imply for a symmetric interval?
- In the two bootstrap-distribution panels, which values form the central 95 % (blue bars)? Compare the arms of the mean's distribution around its centre.
- In "Interval comparison", which interval would you show to management, and why?

## Deliverable

A short note (5-8 lines) with named parts: **Estimate** (mean and median), **Uncertainty** (the two intervals), **Decision** (can
the promise be kept? say "cannot tell" if that is the answer) and **Limitation**. Include one chart of the bootstrap distribution.
"""
