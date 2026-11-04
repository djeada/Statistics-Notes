"""Lesson 16 - Sampling distributions and the central limit theorem."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl.utils import get_column_letter
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "16-sampling-distributions-and-the-clt"
TITLE = "Sampling distributions and the CLT"
MODULE = "Uncertainty and statistical inference"
DATASET = "1,000 order values (a skewed population) and 250 repeated samples of 50 orders drawn from it"
NS = [5, 20, 50]
NREP, NMAX, NPOP = 250, 50, 1000
EDGES = list(range(0, 150, 10))  # 0,10,...,140 ; last bucket is 140+
THRESH = 70.0  # dollars, for the tail-probability question
TARGET_SE = 4.0


def make_data():
    rng = np.random.default_rng(1616)
    pop = rng.lognormal(np.log(40), 0.9, NPOP).round(2)
    samples = rng.choice(pop, size=(NREP, NMAX), replace=True)
    cols = {"customer_id": np.arange(1, NPOP + 1), "order_value": pop,
            "rep": pd.Series([int(i) for i in range(1, NREP + 1)] + [None] * (NPOP - NREP), dtype=object)}
    for j in range(NMAX):
        cols[f"s{j + 1}"] = np.r_[samples[:, j], np.full(NPOP - NREP, np.nan)]
    return pd.DataFrame(cols), pop, samples


def build(out: Path) -> Book:
    df, pop, S = make_data()
    write_csv(out, df)
    mu, sg = float(pop.mean()), float(pop.std())  # population SD (divide by N)
    skw = float(stats.skew(pop, bias=False))
    means = {n: S[:, :n].mean(1) for n in NS}
    sds = {n: S[:, :n].std(1, ddof=1) for n in NS}
    cover = {n: (np.abs(means[n] - mu) < 1.96 * sds[n] / np.sqrt(n)).astype(float) for n in NS}

    # toy numbers for theory.md: population {2,4,6,12}, samples of size 2 with replacement
    import itertools
    tp = np.array([2, 4, 6, 12.])
    tm = np.array([np.mean(c) for c in itertools.product(tp, repeat=2)])
    assert tp.mean() == 6 and abs(tp.var() - 14) < 1e-12 and abs(tm.mean() - 6) < 1e-12 and abs(tm.var() - 7) < 1e-12
    assert abs(tm.std() - 2.6458) < 5e-5 and (tm == 12).sum() == 1 and tm.min() == 2 and abs(tp.std() - 3.7417) < 5e-5

    b = Book(df, "Lesson 16 - Sampling distributions and the CLT",
             "Solved workbook. Yellow cells are assumptions; everything else is a live formula.")
    R = NREP + 1
    OV = b.rng("order_value", last=NPOP + 1)
    first_c, last_c = b.col("s1"), b.col("s50")

    mean_names = {}
    for n in NS:
        nm = f"mean_n{n}"
        endL = get_column_letter(list(b._cols).index("s1") + n)
        b.add_column(nm, lambda r, endL=endL: f"=AVERAGE(Data!{first_c}{r}:{endL}{r})",
                     expected=np.r_[means[n], np.full(NPOP - NREP, np.nan)], fmt="0.00")
        mean_names[n] = nm
    b.section("1. The population (all 1,000 orders)")
    b.row("Number of orders N", f"=COUNT({OV})", NPOP, "0")
    m_ = b.row("Population mean mu ($)", f"=AVERAGE({OV})", mu, "0.00")
    s_ = b.row("Population standard deviation sigma ($, divide by N)", f"=STDEVP({OV})", sg, "0.00")
    b.row("Median ($)", f"=MEDIAN({OV})", float(np.median(pop)), "0.00")
    b.row("Skewness", f"=SKEW({OV})", skw, "0.00", "Strongly right-skewed")
    b.row("Largest order ($)", f"=MAX({OV})", float(pop.max()), "0.00")

    # SD and coverage helper columns
    for n in NS:
        endL = get_column_letter(list(b._cols).index("s1") + n)
        b.add_column(f"sd_n{n}", lambda r, endL=endL: f"=STDEV(Data!{first_c}{r}:{endL}{r})",
                     expected=np.r_[sds[n], np.full(NPOP - NREP, np.nan)], fmt="0.00")
    for n in NS:
        b.add_column(f"covers_n{n}", lambda r, n=n: (
            f"=IF(ABS(Data!{b.col(f'mean_n{n}')}{r}-{m_})<1.96*Data!{b.col(f'sd_n{n}')}{r}/SQRT({n}),1,0)"),
            expected=np.r_[cover[n], np.full(NPOP - NREP, np.nan)], fmt="0")

    b.section("2. Sampling distribution of the mean (250 samples for each size)")
    rows, exp = [], {}
    r0 = b.next_row + 1
    for i, n in enumerate(NS):
        mc = b.rng(mean_names[n], last=R)
        cc = b.rng(f"covers_n{n}", last=R)
        rr = r0 + i
        rows.append([n, f"=AVERAGE({mc})", f"=STDEV({mc})", f"={b.local(s_)}/SQRT(A{rr})", f"=C{rr}/D{rr}", f"=SKEW({mc})",
                     f"={b.local(m_)}-B{rr}", f"=AVERAGE({cc})"])
        exp[(i, 1)] = means[n].mean()
        exp[(i, 2)] = means[n].std(ddof=1)
        exp[(i, 3)] = sg / np.sqrt(n)
        exp[(i, 4)] = means[n].std(ddof=1) / (sg / np.sqrt(n))
        exp[(i, 5)] = float(stats.skew(means[n], bias=False))
        exp[(i, 6)] = mu - means[n].mean()
        exp[(i, 7)] = float(cover[n].mean())
    t2a, t2b = b.table(["Sample size n", "Mean of sample means", "SD of sample means", "Theory: sigma/sqrt(n)", "Ratio observed/theory",
                        "Skewness of sample means", "mu minus mean of means", "Share with mu inside mean +- 1.96 s/sqrt(n)"],
                       rows, fmt={1: "0.00", 2: "0.00", 3: "0.00", 4: "0.000", 5: "0.00", 6: "0.00", 7: "0.0%"}, expect=exp)

    b.section("3. Histograms: share of samples (and of the population) in each $10 bucket")
    rows, exp = [], {}
    r0 = b.next_row + 1
    for i, lo in enumerate(EDGES):
        hi = lo + 10 if lo < EDGES[-1] else 1e9
        lab = f"{lo}-{lo + 10}" if lo < EDGES[-1] else f"{lo}+"
        row = [lab, lo, hi if hi < 1e9 else 100000]
        for n in NS:
            mc = b.rng(mean_names[n], last=R)
            row.append(f'=COUNTIFS({mc},">="&$B{r0 + i},{mc},"<"&$C{r0 + i})/{NREP}')
        row.append(f'=COUNTIFS({OV},">="&$B{r0 + i},{OV},"<"&$C{r0 + i})/{NPOP}')
        rows.append(row)
        for j, n in enumerate(NS):
            exp[(i, 3 + j)] = float(((means[n] >= lo) & (means[n] < hi)).mean())
        exp[(i, 6)] = float(((pop >= lo) & (pop < hi)).mean())
    t3a, t3b = b.table(["bucket ($)", "from", "to", "n = 5", "n = 20", "n = 50", "population (single orders)"], rows,
                       fmt={3: "0.0%", 4: "0.0%", 5: "0.0%", 6: "0.0%"}, expect=exp)
    b.bar_chart_from_table("Share of samples per $10 bucket: means narrow and become symmetric as n grows", 1, [4, 5, 6, 7], t3a, t3b,
                           anchor="K4", y_title="share")

    b.section("4. Using the sampling distribution")
    thr = b.row("Threshold for the sample mean ($)", THRESH, None, "0.0", "Edit me", is_input=True)
    z = (THRESH - mu) / (sg / np.sqrt(50))
    p_norm = 1 - stats.norm.cdf(z)
    mc50 = b.rng(mean_names[50], last=R)
    pn = b.row("Normal approximation: P(mean of 50 orders > threshold)",
          f"=1-NORMSDIST(({b.local(thr)}-{b.local(m_)})/({b.local(s_)}/SQRT(50)))", float(p_norm), "0.0%")
    b.row("Observed share of the 250 samples (n = 50) above threshold", f'=COUNTIF({mc50},">"&{b.local(thr)})/{NREP}',
          float((means[50] > THRESH).mean()), "0.0%")
    mc5 = b.rng(mean_names[5], last=R)
    z5 = (THRESH - mu) / (sg / np.sqrt(5))
    b.row("Same question for n = 5: normal approximation", f"=1-NORMSDIST(({b.local(thr)}-{b.local(m_)})/({b.local(s_)}/SQRT(5)))",
          float(1 - stats.norm.cdf(z5)), "0.0%")
    b.row("Same question for n = 5: observed share", f'=COUNTIF({mc5},">"&{b.local(thr)})/{NREP}', float((means[5] > THRESH).mean()), "0.0%",
          "Skew makes the normal approximation poor at n = 5")
    tse = b.row("Target standard error of the mean ($)", TARGET_SE, None, "0.0", "Edit me", is_input=True)
    need = int(np.ceil((sg / TARGET_SE) ** 2))
    nreq = b.row("Orders needed so that sigma/sqrt(n) <= target", f"=ROUNDUP(({b.local(s_)}/{b.local(tse)})^2,0)", need, "0")
    b.row("Orders needed for half that standard error", f"=ROUNDUP(({b.local(s_)}/({b.local(tse)}/2))^2,0)",
          int(np.ceil((sg / (TARGET_SE / 2)) ** 2)), "0", "Four times as many")

    b.answers([
        ("Population mean, SD (divide by N), skewness, median", f"={m_}",
         f"mu = {mu:.2f}, sigma = {sg:.2f}, skewness {skw:.2f}, median {np.median(pop):.2f}: the mean is {mu / np.median(pop):.1f} times the median because a few "
         f"very large orders (max {pop.max():.0f}) pull it up."),
        ("Sample means for n = 5, 20, 50 (first n draws of each row): their average", f"=Analysis!B{t2a}",
         f"Averages {means[5].mean():.2f} / {means[20].mean():.2f} / {means[50].mean():.2f} vs mu = {mu:.2f}: the sample mean is unbiased."),
        ("SD of the sample means vs sigma/sqrt(n)", f"=Analysis!C{t2a + 2}",
         f"Observed {means[5].std(ddof=1):.2f} / {means[20].std(ddof=1):.2f} / {means[50].std(ddof=1):.2f} vs theory {sg / np.sqrt(5):.2f} / {sg / np.sqrt(20):.2f} / "
         f"{sg / np.sqrt(50):.2f}. Ten times the data would shrink the spread by sqrt(10) = 3.2, not 10."),
        ("Skewness of the sample means; what the histograms show", f"=Analysis!F{t2a}",
         f"Skewness {stats.skew(means[5], bias=False):.2f} (n=5), {stats.skew(means[20], bias=False):.2f} (n=20), {stats.skew(means[50], bias=False):.2f} (n=50) vs {skw:.2f} for single orders: "
         f"the distribution of the mean becomes narrower and more symmetric as n grows (CLT), but n = 5 is still visibly skewed."),
        ("Share of samples whose mean +- 1.96 s/sqrt(n) contains mu", f"=Analysis!H{t2a}",
         f"{cover[5].mean():.0%} (n=5), {cover[20].mean():.0%} (n=20), {cover[50].mean():.0%} (n=50) instead of 95%: with skewed data and small n the "
         f"simple interval is too optimistic (a typical sample misses the few very large orders and underestimates s)."),
        (f"Orders needed for SE <= {TARGET_SE:.0f}; and for half of that", f"={nreq}",
         f"{need} orders; halving the standard error needs {int(np.ceil((sg / (TARGET_SE / 2)) ** 2))}, four times as many."),
        (f"P(mean of 50 orders > {THRESH:.0f}): normal approximation vs observed", f"={pn}",
         f"Approximation {p_norm:.1%}, observed {(means[50] > THRESH).mean():.1%} of 250 samples; for n = 5 the same approximation gives {1 - stats.norm.cdf(z5):.1%} "
         f"against an observed {(means[5] > THRESH).mean():.1%}."),
        ("What does the CLT not guarantee?", "see text",
         "It is a statement about the limit: how fast the mean becomes normal depends on skewness and tails (here n = 5 is not enough and n = 20 is borderline), "
         "it needs independent draws from one population, and it says nothing about the spread of the individual orders."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-16-clt", "16 · Sampling distributions and the CLT",
             "A skewed population of orders, and what the average of n orders looks like for n = 5, 20, 50 (250 repeated samples).")
    d.stat("Population and standard errors", {"mu ($)": mu, "sigma ($)": sg, "skewness": skw, "SD of means, n=5": means[5].std(ddof=1),
                                              "SD of means, n=20": means[20].std(ddof=1), "SD of means, n=50": means[50].std(ddof=1)},
           "Observed SD of the sample means is close to sigma/sqrt(n) = 28.15 / 14.08 / 8.90.", decimals=2)
    labs = [f"{lo}-{lo + 10}" if lo < EDGES[-1] else f"{lo}+" for lo in EDGES]
    ph = pd.DataFrame({"bucket_$": labs, "share_of_orders": [float(((pop >= lo) & (pop < (lo + 10 if lo < EDGES[-1] else 1e9))).mean()) for lo in EDGES]})
    d.bars("Population: single orders", ph, "Heavily right-skewed: most orders are small, a few are very large.", unit="percentunit")
    mh = pd.DataFrame({"bucket_$": labs})
    for n in NS:
        mh[f"n={n}"] = [float(((means[n] >= lo) & (means[n] < (lo + 10 if lo < EDGES[-1] else 1e9))).mean()) for lo in EDGES]
    d.bars("Sample means: share of 250 samples per $10 bucket", mh, "Narrower and more symmetric as n grows; n = 5 keeps a long right tail.", unit="percentunit")
    rp = pd.DataFrame({"sample": np.arange(1, NREP + 1), "n=5": means[5], "n=20": means[20], "n=50": means[50], "mu": mu})
    d.xy("Sample mean of each repetition", rp, "sample", ["n=5", "n=20", "n=50", "mu"],
         "250 repetitions: the dots tighten around the line mu as n increases.", lines=["mu"])
    ns_all = np.arange(1, NMAX + 1)
    emp = [S[:, :n].mean(1).std(ddof=1) for n in ns_all]
    se = pd.DataFrame({"n": ns_all, "observed_SD_of_means": emp, "sigma_over_sqrt_n": sg / np.sqrt(ns_all)})
    d.xy("Standard error vs sample size", se, "n", ["observed_SD_of_means", "sigma_over_sqrt_n"],
         "The spread of the mean falls like 1/sqrt(n): quadrupling n halves it.", lines=["sigma_over_sqrt_n"])
    tb = pd.DataFrame({"n": NS, "mean_of_means": [means[n].mean() for n in NS], "SD_of_means": [means[n].std(ddof=1) for n in NS],
                       "sigma_over_sqrt_n": [sg / np.sqrt(n) for n in NS], "skewness_of_means": [float(stats.skew(means[n], bias=False)) for n in NS],
                       "ci_coverage": [float(cover[n].mean()) for n in NS]}).round(3)
    d.table("Summary by sample size", tb, "ci_coverage = share of samples whose mean +- 1.96 s/sqrt(n) contains the population mean (nominal 0.95).", w=24)
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK.format(thresh=f"{THRESH:.0f}", target=f"{TARGET_SE:.0f}"))
    return b


THEORY = r"""
# Theory: sampling distributions and the central limit theorem

## Why this matters

Every number computed from a sample (a mean, a median, a conversion rate, a regression slope) would have come out slightly
different if you had drawn another sample. Statistical inference is the discipline of describing *how much* it would differ.
The failure it prevents is reading a single sample statistic as if it were the truth: deciding that a campaign "lifted" order value by
$3 when a different sample of the same size would show $-4, or promising precision that your sample size cannot deliver.

## The sampling distribution

The **sampling distribution** of a statistic is its distribution over all possible samples of a given size $n$ from the population.
It is a theoretical object, but we can approximate it by simulation, which is what the dataset in this lesson does: 250 repeated
samples of size 50 are stored, and the means of the first 5, 20 and 50 draws of each row are compared.

For the sample mean $\bar X$ of $n$ independent draws from a population with mean $\mu$ and standard deviation $\sigma$:

$$
E[\bar X] = \mu,\qquad \operatorname{Var}(\bar X) = \frac{\sigma^2}{n},\qquad \operatorname{SE}(\bar X) = \frac{\sigma}{\sqrt n}.
$$

The first says $\bar X$ is **unbiased**. The second is the reason a larger sample is more precise, and also why precision is expensive:
to halve the standard error you need four times the data.

**Worked example (exact).** Population $\{2,4,6,12\}$: $\mu = 6$, $\sigma^2 = (16+4+0+36)/4 = 14$. List all 16 equally likely samples of size 2
(with replacement). The means range from 2 (one sample) to 12 (one sample); their average is exactly $6$, and their variance is exactly $7 = 14/2$,
so $\operatorname{SE} = \sqrt 7 = 2.65$. The means are less spread out than the single values: standard deviation $2.65$ against $\sigma = 3.74$.

## Standard error versus standard deviation

The **standard deviation** $\sigma$ (or its estimate $s$) describes how much *individual observations* vary. The **standard error** describes how much
the *estimate* varies from sample to sample. A population can be wildly variable and still be estimated precisely, given enough data.
In practice $\sigma$ is unknown and estimated by $s$ from the one sample you have: $\widehat{\operatorname{SE}} = s/\sqrt n$. Use
`STDEV` (divides by $n-1$) for $s$, and `STDEVP` only when you really hold the entire population, as in the first section of the workbook.

## The central limit theorem

If the draws are independent with finite variance, then for large $n$

$$
\frac{\bar X - \mu}{\sigma/\sqrt n} \;\approx\; N(0,1),
$$

**whatever the shape of the population**. This is what justifies normal-based intervals and tests for means. The theorem is a limit statement; how large $n$
must be depends on how far the population is from normal. A useful measure is skewness: the skewness of $\bar X$ is the population skewness divided by $\sqrt n$,
so a very skewed population needs a much larger $n$ than a symmetric one (the folklore "$n \ge 30$" is a rule of thumb, not a law). With very
heavy tails (for example income, file sizes or insurance claims) the convergence can be so slow that the mean of a few hundred observations is still dominated by the
largest values; then use medians, transformations or the bootstrap (lesson 17).

Related: the **law of large numbers** says $\bar X \to \mu$ as $n$ grows (the centre), whereas the CLT describes the *shape and size of the fluctuation* around it.

## Using it

- **Probability statements about a mean.** For a hypothetical $\sigma = 40$ and $n = 25$: $\operatorname{SE} = 8$; if $\mu = 100$ then
  $P(\bar X > 110) \approx 1 - \Phi\!\left(\tfrac{110-100}{8}\right) = 1 - \Phi(1.25) = 0.106$.
- **Planning sample size.** To reach $\operatorname{SE} \le \varepsilon$ you need $n \ge (\sigma/\varepsilon)^2$. With $\sigma=40$ and $\varepsilon = 4$: $n \ge 100$.
- **Interval for a mean.** $\bar x \pm t_{n-1,\,0.975}\, s/\sqrt n$ covers $\mu$ in about 95 % of repeated samples *if* the sampling distribution is close to
  normal. With skewed data and small $n$ the real coverage is lower, because $s$ is itself noisy and correlated with $\bar x$.

## Assumptions and pitfalls

1. **Independence.** $\sigma/\sqrt n$ is wrong for autocorrelated data (lesson 14): consecutive minutes of traffic are not independent draws, and the effective $n$ is smaller.
2. **Sampling bias.** A biased sample has a perfectly nice sampling distribution centred on the wrong value (lesson 05); more data does not fix it.
3. **Finite populations.** If you sample without replacement more than ~5 % of the population, multiply the variance by $(N-n)/(N-1)$. The simulation here samples with replacement.
4. **Confusing the histogram of the data with the sampling distribution.** The first stays skewed however large $n$ is; the second changes with $n$.
5. **The mean is not always the right statistic.** The CLT helps for sums and means; medians and extreme percentiles have different sampling distributions (lesson 03).
6. **Do not use $n \ge 30$ blindly**: check the shape with a histogram of repeated samples or a bootstrap.

## Related notes

- [Distribution shapes and heavy tails](../01-distribution-shapes-and-heavy-tails/theory.md)
- [Sampling bias and Simpson's paradox](../05-sampling-bias-and-simpson-s-paradox/theory.md)
- [Bootstrapping and confidence intervals](../17-bootstrapping-and-confidence-intervals/theory.md)
- [A/B testing and effect sizes](../19-a-b-testing-and-effect-sizes/theory.md)
- Repo notes: [Central limit theorem](../../notes/sampling_and_sampling_distributions/central_limit_theorem.md),
  [Standard error and LLN](../../notes/sampling_and_sampling_distributions/standard_error_and_lln.md)
"""

TASK = r"""
# Task: sampling distributions and the central limit theorem

## Scenario

An online shop wants to monitor its average order value by auditing a **random sample of n orders** each week. Management proposes
n = 5 ("it is only an average") and the analytics team proposes n = 50. Order values are known to be very uneven: most customers
buy small baskets and a few place large orders. To settle the question you have a full table of last year's 1,000 orders and 250 simulated
audits, each a random sample of 50 orders drawn (with replacement) from that table.

## Data

`data.csv` - 1,000 rows. Columns:

| column | meaning |
|---|---|
| `customer_id` | order number 1-1000 |
| `order_value` | order value in dollars - the **entire population** (all 1,000 orders) |
| `rep` | audit number 1-250 (filled in rows 1-250 only) |
| `s1` ... `s50` | the 50 order values drawn in audit `rep` (rows 1-250 only). Use `s1:s5` for samples of size 5, `s1:s20` for size 20, `s1:s50` for size 50. |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the population mean, standard deviation (`STDEVP`), skewness and median of `order_value`. Why is the mean larger than the median?
2. For every audit (row) compute the mean of the first 5, the first 20 and all 50 draws (`AVERAGE` over `s1:s5`, `s1:s20`, `s1:s50`). Compare the average of
   the 250 means with the population mean for each n.
3. Compute the standard deviation of the 250 sample means for each n and compare it with $\sigma/\sqrt n$. How much does the spread shrink when n goes from 5 to 50?
4. Compute the skewness of the 250 sample means for each n and count how many fall in each $10 bucket (`COUNTIFS`). Describe how the shape changes.
5. For each audit and each n compute $s$ (`STDEV`) and check whether $\bar x \pm 1.96\,s/\sqrt n$ contains the population mean. What share of audits do?
6. How many orders per audit are needed for a standard error of {target} dollars? How many for half of it?
7. Using the normal approximation, what is the probability that the average of a 50-order audit exceeds {thresh} dollars? Compare with the share of the 250 audits that do. Repeat for n = 5.
8. *In two sentences:* which audit size would you recommend, and what does the central limit theorem *not* promise here?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Population: single orders" and "Sample means", which distribution is skewed and which one becomes bell-shaped as n grows?
- In "Sample mean of each repetition", how does the scatter of the dots around the line for n = 5 compare with n = 50?
- In "Standard error vs sample size", at what sample size does the spread of the mean reach half of its value at n = 10?

## Deliverable

A short note (5-8 lines) to the management: recommended audit size, the expected size of the typical error for that size, the
share of audits with a misleading "alarm" at your chosen threshold, and one limitation. Include one chart.
"""
