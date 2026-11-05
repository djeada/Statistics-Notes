"""Lesson 05 - Sampling bias and Simpson's paradox."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "05-sampling-bias-and-simpson-s-paradox"
TITLE = "Sampling bias and Simpson's paradox"
MODULE = "Understanding data beyond averages"
DATASET = "2,800 checkout sessions of a non-randomised A/B test (device, variant, converted, exit-survey score)"

# (device, variant): (sessions, conversions)  -- planted so that A wins in both devices and B wins when pooled
CELLS = {("desktop", "A"): (320, 109), ("desktop", "B"): (1080, 292),
         ("mobile", "A"): (1080, 108), ("mobile", "B"): (320, 19)}
DAYS = 14


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(505)
    parts = []
    for (dev, var), (n, k) in CELLS.items():
        conv = np.zeros(n, dtype=int)
        conv[rng.choice(n, k, replace=False)] = 1
        parts.append(pd.DataFrame({"device": dev, "variant": var, "converted": conv,
                                   "day": rng.integers(0, DAYS, n)}))
    df = pd.concat(parts, ignore_index=True)
    df = df.sample(frac=1, random_state=5).sort_values("day", kind="stable").reset_index(drop=True)
    df["date"] = pd.Timestamp("2026-03-02") + pd.to_timedelta(df["day"], unit="D")
    mean = np.where(df["variant"] == "A", 4.4, 4.1)
    answers = (df["converted"] == 1) & (rng.random(len(df)) < 0.55)  # only buyers see the exit survey, and 55 % answer
    score = np.clip(np.round(rng.normal(mean, 0.8)), 1, 5)
    df["csat"] = np.where(answers, score, np.nan)
    df.insert(0, "session_id", np.arange(1, len(df) + 1))
    return df[["session_id", "date", "device", "variant", "converted", "csat"]]


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    conv = df["converted"].to_numpy()
    dev, var = df["device"].to_numpy(), df["variant"].to_numpy()
    cs = df["csat"]

    b = Book(df, "Lesson 05 - Sampling bias and Simpson's paradox",
             "Solved workbook. Yellow cells are assumptions you can change; everything else is a live formula.")
    loc = b.local
    D, V, C, S, T = b.rng("device"), b.rng("variant"), b.rng("converted"), b.rng("csat"), b.rng("date")

    def cell(d, v):
        m = (dev == d) & (var == v)
        return int(m.sum()), int(conv[m].sum())

    # ------------------------------------------------ 1 pooled
    b.section("1. Pooled comparison (everything lumped together)")
    pooled = {}
    for v in "AB":
        m = var == v
        ns = b.row(f"Variant {v}: sessions", f"=COUNTIF({V},\"{v}\")", int(m.sum()), "0")
        nc = b.row(f"Variant {v}: conversions", f"=SUMIF({V},\"{v}\",{C})", int(conv[m].sum()), "0")
        r = b.row(f"Variant {v}: conversion rate", f"={loc(nc)}/{loc(ns)}", float(conv[m].mean()), "0.00%")
        pooled[v] = dict(n=ns, c=nc, r=r, nv=int(m.sum()), cv=int(conv[m].sum()), rv=float(conv[m].mean()))
    b.row("Pooled difference B - A (percentage points)", f"=({loc(pooled['B']['r'])}-{loc(pooled['A']['r'])})*100",
          100 * (pooled['B']['rv'] - pooled['A']['rv']), "0.00")

    # ------------------------------------------------ 2 segments
    b.section("2. Segment by segment (device x variant)")
    rows, exp = [], {}
    r0 = b.next_row + 1
    seg = {}
    for i, ((d, v), (nn, kk)) in enumerate(CELLS.items()):
        r = r0 + i
        rows.append([d, v, f"=COUNTIFS({D},A{r},{V},B{r})", f"=COUNTIFS({D},A{r},{V},B{r},{C},1)", f"=D{r}/C{r}"])
        exp.update({(i, 2): nn, (i, 3): kk, (i, 4): kk / nn})
        seg[(d, v)] = (r, nn, kk)
    b.table(["device", "variant", "sessions", "conversions", "rate"], rows, fmt={4: "0.00%"}, expect=exp)

    b.section("3. Is each difference larger than chance?  Two-proportion z-test (pooled variance)")
    rows, exp = [], {}
    r0 = b.next_row + 1
    ztab = {}
    scopes = [("desktop", seg[("desktop", "A")], seg[("desktop", "B")]), ("mobile", seg[("mobile", "A")], seg[("mobile", "B")]),
              ("pooled", None, None)]
    for i, (name, a_, b_) in enumerate(scopes):
        r = r0 + i
        if name == "pooled":
            na, ka = pooled["A"]["nv"], pooled["A"]["cv"]
            nb, kb = pooled["B"]["nv"], pooled["B"]["cv"]
            NA, KA, NB, KB = loc(pooled["A"]["n"]), loc(pooled["A"]["c"]), loc(pooled["B"]["n"]), loc(pooled["B"]["c"])
        else:
            na, ka, nb, kb = a_[1], a_[2], b_[1], b_[2]
            NA, KA, NB, KB = f"C{a_[0]}", f"D{a_[0]}", f"C{b_[0]}", f"D{b_[0]}"
        z, p = proportions_ztest([ka, kb], [na, nb])
        rows.append([name, f"={KA}/{NA}", f"={KB}/{NB}", f"=(B{r}-C{r})*100",
                     f"=(B{r}-C{r})/SQRT(({KA}+{KB})/({NA}+{NB})*(1-({KA}+{KB})/({NA}+{NB}))*(1/{NA}+1/{NB}))",
                     f"=2*(1-NORMSDIST(ABS(E{r})))"])
        exp.update({(i, 1): ka / na, (i, 2): kb / nb, (i, 3): 100 * (ka / na - kb / nb), (i, 4): z, (i, 5): p})
        ztab[name] = (ka / na, kb / nb, z, p)
    z0, z1 = b.table(["scope", "rate A", "rate B", "A - B (pp)", "z", "p (two-sided)"], rows,
                     fmt={1: "0.00%", 2: "0.00%", 3: "0.00", 4: "0.00", 5: "0.0000"}, expect=exp)
    ztab_rows = (z0, z1)

    # ------------------------------------------------ 4 mix
    b.section("4. Who saw which variant? (traffic mix)")
    mix = {}
    for v in "AB":
        m = var == v
        mix[v] = b.row(f"Share of variant {v} sessions on desktop", f"=COUNTIFS({V},\"{v}\",{D},\"desktop\")/COUNTIF({V},\"{v}\")",
                       float((dev[m] == "desktop").mean()), "0.0%")
    ov = b.row("Share of all sessions on desktop", f"=COUNTIF({D},\"desktop\")/COUNTA({D})", float((dev == "desktop").mean()), "0.0%")
    wd = float((dev == "desktop").mean())

    # ------------------------------------------------ 5 decomposition and standardisation
    b.section("5. Reconcile and standardise")
    rate = {k: v[2] / v[1] for k, v in seg.items()}
    for v in "AB":
        sh = float((dev[var == v] == "desktop").mean())
        rd_c, rm_c = f"E{seg[('desktop', v)][0]}", f"E{seg[('mobile', v)][0]}"
        b.row(f"Variant {v}: mix x rate = share_desktop*rate_desktop + share_mobile*rate_mobile",
              f"={loc(mix[v])}*{rd_c}+(1-{loc(mix[v])})*{rm_c}", sh * rate[("desktop", v)] + (1 - sh) * rate[("mobile", v)], "0.00%",
              "equals the pooled rate")
    adj = {}
    for v in "AB":
        rd_c, rm_c = f"E{seg[('desktop', v)][0]}", f"E{seg[('mobile', v)][0]}"
        adj[v] = b.row(f"Variant {v}: standardised rate (overall mix of {wd:.0%} desktop)",
                       f"={loc(ov)}*{rd_c}+(1-{loc(ov)})*{rm_c}", wd * rate[("desktop", v)] + (1 - wd) * rate[("mobile", v)], "0.00%")
    adjv = {v: wd * rate[("desktop", v)] + (1 - wd) * rate[("mobile", v)] for v in "AB"}
    b.row("Standardised difference A - B (percentage points)", f"=({loc(adj['A'])}-{loc(adj['B'])})*100",
          100 * (adjv["A"] - adjv["B"]), "0.00")
    for v in "AB":
        rd_c, rm_c = f"E{seg[('desktop', v)][0]}", f"E{seg[('mobile', v)][0]}"
        b.row(f"Variant {v}: unweighted mean of the two segment rates (a common mistake)", f"=AVERAGE({rd_c},{rm_c})",
              (rate[("desktop", v)] + rate[("mobile", v)]) / 2, "0.00%", "ignores segment sizes")

    # ------------------------------------------------ 6 daily
    b.section("6. Does it hold every day?")
    rows, exp = [], {}
    r0 = b.next_row + 1
    daily = []
    for i in range(DAYS):
        day = pd.Timestamp("2026-03-02") + pd.Timedelta(days=i)
        r = r0 + i
        m = (df["date"] == day).to_numpy()
        ra = conv[m & (var == "A")].mean()
        rb = conv[m & (var == "B")].mean()
        sb = (dev[m & (var == "B")] == "desktop").mean()
        rows.append([day.to_pydatetime(), f"=COUNTIFS({T},A{r},{V},\"A\",{C},1)/COUNTIFS({T},A{r},{V},\"A\")",
                     f"=COUNTIFS({T},A{r},{V},\"B\",{C},1)/COUNTIFS({T},A{r},{V},\"B\")",
                     f"=COUNTIFS({T},A{r},{V},\"B\",{D},\"desktop\")/COUNTIFS({T},A{r},{V},\"B\")"])
        exp.update({(i, 1): ra, (i, 2): rb, (i, 3): sb})
        daily.append((day, ra, rb, sb))
    d0, d1 = b.table(["date", "pooled rate A", "pooled rate B", "desktop share of B"], rows,
                     fmt={0: "yyyy-mm-dd", 1: "0.0%", 2: "0.0%", 3: "0.0%"}, expect=exp)
    b.line_chart_from_table("Daily pooled conversion rate and the desktop share of variant B", 1, [2, 3, 4], d0, d1, anchor="H4",
                            y_title="share")
    days_b = sum(1 for _, ra, rb, _ in daily if rb > ra)
    days_cell = b.row("Days on which B beats A in the pooled rate", f"=SUMPRODUCT(--(C{d0}:C{d1}>B{d0}:B{d1}))",
                      days_b, "0", f"of {DAYS} days")

    # ------------------------------------------------ 7 selection bias
    b.section("7. Who answers the exit survey? (selection bias)")
    resp = cs.notna().to_numpy()
    nresp = b.row("Survey responses", f"=COUNT({S})", int(resp.sum()), "0")
    rr = b.row("Responses as a share of ALL sessions", f"={loc(nresp)}/COUNTA({D})", float(resp.mean()), "0.0%")
    b.row("Responses as a share of converting sessions", f"={loc(nresp)}/SUM({C})", float(resp.sum() / conv.sum()), "0.0%")
    b.row("Responses from non-converting sessions", f"=COUNTIFS({S},\">0\",{C},0)", int((resp & (conv == 0)).sum()), "0")
    csa = b.row("Mean score, variant A respondents", f"=AVERAGEIF({V},\"A\",{S})", float(cs[var == "A"].mean()), "0.00")
    csb = b.row("Mean score, variant B respondents", f"=AVERAGEIF({V},\"B\",{S})", float(cs[var == "B"].mean()), "0.00")
    b.row("Number of respondents in A / in B", f"=COUNTIFS({V},\"A\",{S},\">0\")", int((resp & (var == "A")).sum()), "0",
          f"B: {int((resp & (var == 'B')).sum())}")

    # ---------------------------------------------------------------- answers
    pa, pb = pooled["A"]["rv"], pooled["B"]["rv"]
    sig = {k: v[3] for k, v in ztab.items()}
    b.answers([
        ("Pooled sessions, conversions and rate for A and B; which wins?", f"={pooled['B']['r']}",
         f"A: {pooled['A']['cv']}/{pooled['A']['nv']} = {pa:.1%}; B: {pooled['B']['cv']}/{pooled['B']['nv']} = {pb:.1%}. Pooled, B wins by {100 * (pb - pa):.1f} points."),
        ("Conversion rate per device and variant; who wins within each device?", f"=Analysis!E{seg[('desktop', 'A')][0]}",
         f"Desktop: A {rate[('desktop', 'A')]:.1%} vs B {rate[('desktop', 'B')]:.1%}. Mobile: A {rate[('mobile', 'A')]:.1%} vs B {rate[('mobile', 'B')]:.1%}. "
         "A wins in both devices, yet B wins pooled: Simpson's paradox."),
        ("Share of desktop sessions in A and in B", f"={mix['B']}",
         f"A: {float((dev[var == 'A'] == 'desktop').mean()):.1%} desktop; B: {float((dev[var == 'B'] == 'desktop').mean()):.1%}. Desktop converts about 3x better than mobile, "
         "and B was shown mostly to desktop users - the allocation was not random."),
        ("Reconcile the pooled rates from the segment rates; unweighted mean of segment rates", f"={ov}",
         "Pooled rate = sum of (share of sessions in segment x segment rate); the shares differ between variants, so the pooled rates are not comparable. "
         f"The unweighted segment means (A {(rate[('desktop', 'A')] + rate[('mobile', 'A')]) / 2:.1%}, B {(rate[('desktop', 'B')] + rate[('mobile', 'B')]) / 2:.1%}) "
         "ignore sizes and are equally wrong as a summary."),
        ("Standardise both variants to the same traffic mix", f"={adj['A']}",
         f"With the overall mix ({wd:.0%} desktop) A converts {adjv['A']:.1%} and B {adjv['B']:.1%}: A is {100 * (adjv['A'] - adjv['B']):.1f} points better, the opposite of the pooled picture."),
        ("Two-proportion z-tests per device and pooled", f"=Analysis!F{ztab_rows[0] + 2}",
         f"Desktop z = {ztab['desktop'][2]:.2f} (p = {sig['desktop']:.3f}), mobile z = {ztab['mobile'][2]:.2f} (p = {sig['mobile']:.3f}); pooled z = {ztab['pooled'][2]:.2f} "
         f"(p = {sig['pooled']:.1e}) in favour of B. The pooled 'significance' is real arithmetic but answers the wrong question."),
        ("Days on which B beats A pooled", f"={days_cell}",
         f"B beats A pooled on {days_b} of {DAYS} days, with B's desktop share steady around {np.mean([x[3] for x in daily]):.0%}: the confounding is structural, not a one-day fluke."),
        ("Survey responses, response rates, mean score by variant", f"={nresp}",
         f"{int(resp.sum())} responses = {resp.mean():.1%} of all sessions, all from converting sessions (0 from non-converters). Mean score A {cs[var == 'A'].mean():.2f}, B {cs[var == 'B'].mean():.2f}. "
         "These describe satisfied buyers, not visitors: survivorship / selection bias."),
        ("Interpretation: what was wrong with the experiment and what would you do?", "see text",
         "Variants were allocated by a campaign that sent B mostly to desktop users, so 'variant' is confounded with 'device'. Randomise within device (or at least "
         "balance and check the traffic mix first), and report segment rates and a standardised estimate. Limitation: standardising adjusts only for the variable you "
         "stratified on; other unobserved differences between who got A and B remain."),
    ])

    # ---------------------------------------------------------------- grafana
    d = Dash("stats-05-simpsons-paradox", "05 · Sampling bias and Simpson's paradox",
             "B wins the pooled comparison and loses in every device: a mix effect from non-random allocation "
             "(values computed from data.csv).", df.rename(columns={"date": "time"}), "time")
    d.stat("Conversion rate (%)", {"pooled A": 100 * pa, "pooled B": 100 * pb, "desktop A": 100 * rate[("desktop", "A")],
                                    "desktop B": 100 * rate[("desktop", "B")], "mobile A": 100 * rate[("mobile", "A")],
                                    "mobile B": 100 * rate[("mobile", "B")]},
           "B looks better pooled, but A is better in each segment.", decimals=1, unit="percent")
    rt = pd.DataFrame({"scope": ["pooled", "desktop", "mobile", "standardised"],
                       "A": [100 * pa, 100 * rate[("desktop", "A")], 100 * rate[("mobile", "A")], 100 * adjv["A"]],
                       "B": [100 * pb, 100 * rate[("desktop", "B")], 100 * rate[("mobile", "B")], 100 * adjv["B"]]}).round(2)
    d.bars("Conversion rate: pooled vs segments vs standardised (%)", rt,
           "The ranking flips between the pooled bar group and every other group.", unit="percent")
    mx = pd.DataFrame({"variant": ["A", "B"],
                       "desktop": [cell("desktop", v)[0] for v in "AB"], "mobile": [cell("mobile", v)[0] for v in "AB"]})
    d.bars("Who saw which variant? (sessions by device)", mx,
           "B was mostly shown to desktop users, A to mobile users.", stacking="percent", unit="short")
    dd = pd.DataFrame(daily, columns=["time", "pooled rate A (%)", "pooled rate B (%)", "desktop share of B (%)"])
    for c in dd.columns[1:]:
        dd[c] = (100 * dd[c]).round(2)
    d.timeseries("Daily pooled rate and the desktop share of B (%)", dd,
                 "B wins every day, and its desktop share stays high every day: the mix effect is structural.",
                 unit="percent", colors={"pooled rate A (%)": "#4E79A7", "pooled rate B (%)": "#F28E2B", "desktop share of B (%)": "#9C755F"},
                 dashed=["desktop share of B (%)"])
    tb = pd.DataFrame([[f"{k[0]} / {k[1]}", v[1], v[2], round(100 * v[2] / v[1], 2)] for k, v in seg.items()],
                      columns=["device / variant", "sessions", "conversions", "rate %"])
    d.table("The 2 x 2 counts behind the paradox", tb, "Segment sizes differ strongly between the variants.")
    sv = pd.DataFrame({"group": ["converting sessions", "non-converting sessions"],
                       "survey responses": [int((resp & (conv == 1)).sum()), int((resp & (conv == 0)).sum())],
                       "no response": [int((~resp & (conv == 1)).sum()), int((~resp & (conv == 0)).sum())]})
    d.bars("Selection bias: who answers the exit survey?", sv,
           "Only converting sessions are asked, so satisfaction scores describe buyers, not visitors.", stacking="none")
    d.save(out)

    md(out / "theory.md", fill(THEORY, theory_values()))
    md(out / "task.md", TASK)
    return b


def fill(text: str, vals: dict) -> str:
    for k, v in vals.items():
        text = text.replace(f"<<{k}>>", str(v))
    return text


def theory_values() -> dict:
    t = {"da": (34, 100), "db": (270, 1000), "ma": (100, 1000), "mb": (6, 100)}
    pa = (t["da"][0] + t["ma"][0]) / (t["da"][1] + t["ma"][1])
    pb = (t["db"][0] + t["mb"][0]) / (t["db"][1] + t["mb"][1])
    return {
        "t_da": f"{t['da'][0] / t['da'][1]:.0%}", "t_db": f"{t['db'][0] / t['db'][1]:.0%}",
        "t_ma": f"{t['ma'][0] / t['ma'][1]:.0%}", "t_mb": f"{t['mb'][0] / t['mb'][1]:.0%}",
        "t_pa": f"{pa:.1%}", "t_pb": f"{pb:.1%}", "t_pa_n": f"{t['da'][0] + t['ma'][0]}/{t['da'][1] + t['ma'][1]}",
        "t_pb_n": f"{t['db'][0] + t['mb'][0]}/{t['db'][1] + t['mb'][1]}",
        "t_wa": f"{t['da'][1] / 1100:.0%}", "t_wb": f"{t['db'][1] / 1100:.0%}",
        "t_adj_a": f"{0.5 * 0.34 + 0.5 * 0.10:.1%}", "t_adj_b": f"{0.5 * 0.27 + 0.5 * 0.06:.1%}",
        "p_cells": " ".join(f"{k}" for k in CELLS),
    }


THEORY = r"""
# Theory: sampling bias and Simpson's paradox

## Why a correct average can still point to the wrong decision

A comparison of two rates can be arithmetically right and still mislead, for two different reasons. **Selection bias** means the units you observe are not
a fair sample of the units you want to talk about (only buyers answer the exit survey; only surviving companies appear in the database). **Confounding**
means the groups you compare differ in something else that also affects the outcome - and, in the extreme, **Simpson's paradox** shows the pooled rate favouring
one group while every subgroup favours the other. Both failures come from comparing numbers without asking who is in each group and how they got there.

## Rates are weighted averages

Let a population split into segments $k=1,\dots,K$ (device, hospital, age band). If segment $k$ contains a fraction $w_k$ of the sessions and has conversion rate $p_k$,
then by the law of total probability

$$
p = \sum_{k=1}^{K} w_k\,p_k, \qquad w_k = \frac{n_k}{n}.
$$

The pooled rate is the segment rates **weighted by the traffic mix**. Two variants have comparable pooled rates only if they have the same mix $w_k$. If variant B has more
of the high-converting segment in its mix, its pooled rate is higher even when B is worse inside every segment.

## Simpson's paradox, with numbers

Toy example (conversions / sessions):

| | desktop | mobile | pooled |
|---|---|---|---|
| A | 34/100 = <<t_da>> | 100/1000 = <<t_ma>> | <<t_pa_n>> = <<t_pa>> |
| B | 270/1000 = <<t_db>> | 6/100 = <<t_mb>> | <<t_pb_n>> = <<t_pb>> |

A beats B on desktop (<<t_da>> vs <<t_db>>) and on mobile (<<t_ma>> vs <<t_mb>>), but B beats A pooled (<<t_pb>> vs <<t_pa>>). The reason is the mix: A has only <<t_wa>> desktop sessions,
B has <<t_wb>>. Standardising both to a 50/50 mix gives A $0.5\cdot0.34+0.5\cdot0.10=<<t_adj_a>>$ and B $0.5\cdot0.27+0.5\cdot0.06=<<t_adj_b>>$: A is clearly better.
Note that *no arithmetic is wrong*; the paradox is that the pooled number answers a question nobody asked ("which variant did better on whatever traffic it happened to get?").

The reversal needs two ingredients: the segment variable must **change the outcome rate** a lot (desktop converts much better), and it must be **unevenly distributed across the
groups** (B got mostly desktop). If assignment is random, the mix is the same in expectation and the pooled and stratified answers agree.

## Which table is right? It depends on the causal story

- If the segment *causes the assignment* and affects the outcome (a marketing campaign sends desktop users to B): the segment is a **confounder**; compare within segments or standardise.
- If the segment is *caused by the treatment* (B's new page makes more people use the desktop site): the segment is a **mediator**; conditioning on it would remove part of the effect you want to measure,
  and the pooled number may be right.

Statistics alone cannot tell you which; you need to know how the data were generated. This is why a randomised experiment is preferable: randomisation breaks the link between
assignment and everything else (see [A/B testing](../19-a-b-testing-and-effect-sizes/theory.md)); for observational data see [confounding in regression](../13-multiple-regression-and-confounding/theory.md).

## Standardisation and tests

**Direct standardisation** reports $\sum_k w_k^{*}\,p_{k}$ with one common reference mix $w^*$ for all groups. A within-segment comparison of proportions uses the two-proportion $z$-test

$$
z=\frac{\hat p_A-\hat p_B}{\sqrt{\hat p\,(1-\hat p)\,(1/n_A+1/n_B)}},\qquad \hat p=\frac{x_A+x_B}{n_A+n_B},
$$

with a two-sided p-value $2\,(1-\Phi(|z|))$ (Excel `NORMSDIST`). Mantel-Haenszel and logistic regression with the segment as a covariate generalise this to many segments and continuous confounders.
A small $p$ in the pooled table does not rescue a biased comparison: bias is not reduced by sample size.

## Selection and survivorship bias

- **Survivorship bias**: you only see units that "made it". Classic case: armour was added where returning bombers had bullet holes, but the planes that were hit elsewhere never returned.
  In this lesson's data the exit-survey score exists only for sessions that converted: its mean says nothing about visitors who left.
- **Self-selection and non-response**: respondents to an opt-in survey differ from non-respondents (happy or furious users answer).
- **Selection on the outcome**: studying "successful startups" or "customers who stayed" to find what drives success guarantees spurious findings.
- **Sample-ratio mismatch**: if an experiment designed for 50/50 traffic shows 78/22 in some segment, assignment is broken; check the split before the result.

## Checklist before trusting a comparison

1. Who is in each group and how did they get there (random, campaign, opt-in, survival)?
2. **Table 1 / balance check**: compare the mix of key segments across groups (here: the desktop share of A and B).
3. Compute the comparison within segments and standardised; do they agree with the pooled one?
4. Is any variable used to define the sample affected by the outcome?
5. Report denominators ($x/n$), not only rates.

## Assumptions and pitfalls

1. **Stratifying on the wrong variable can create bias** (conditioning on a mediator or a collider).
2. **Too many strata** give tiny cells and noisy rates; standardisation weights then need care.
3. **Averaging rates**: never average segment rates without weights; never average a ratio of sums as a sum of ratios.
4. **Adjustment covers only what you observed**: unobserved confounders remain.
5. **Subgroup hunting**: after slicing many ways, some reversal will appear by chance ([multiple comparisons](../../notes/hypothesis_testing_and_confidence_intervals/multiple_comparisons.md)).

## Related notes

- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)
- [Total probability](../../notes/probability/total_probability.md) and [conditional probability](../../notes/probability/conditional_probability.md)
- [Spurious correlation](../14-spurious-correlation-and-autocorrelation/theory.md)
- [Analysis of categorical data](../../notes/hypothesis_testing_and_confidence_intervals/analysis_of_categorical_data.md)
"""

TASK = r"""
# Task: sampling bias and Simpson's paradox

## Scenario

An e-commerce team tested a redesigned checkout (**variant B**) against the current one (**variant A**) for two weeks. The product owner
presents the headline: "B converts at 22 % versus 15 % for A - ship B!" The analyst who set up the test remembers that the two variants were switched on
through different marketing campaigns. Before the decision, you must check whether the comparison is fair, say which variant is actually better, and warn
about what the customer-satisfaction survey does and does not tell you.

## Data

`data.csv` - 2,800 checkout sessions, one row per session.

| column | meaning |
|---|---|
| `session_id` | running number |
| `date` | day of the session (2 March - 15 March 2026) |
| `device` | `desktop` or `mobile` |
| `variant` | `A` (current checkout) or `B` (redesign) |
| `converted` | 1 if the session ended in a purchase, else 0 |
| `csat` | exit-survey score 1-5, empty if the visitor did not answer |

## Questions

Work in a spreadsheet (import `data.csv`; `COUNTIFS`, `SUMIF` and `AVERAGEIF` are enough), then compare with `solution.xlsx`.

1. Compute sessions, conversions and conversion rate for A and B pooled over all sessions. Which variant wins?
2. Compute the same by device (a 2 x 2 table of device x variant). Who wins within desktop and within mobile?
3. What share of variant A's sessions and of variant B's sessions is on desktop?
4. Write each variant's pooled rate as share_desktop x rate_desktop + share_mobile x rate_mobile and verify it. What do you get if you average the two segment rates without weights?
5. Standardise both variants to the overall traffic mix (desktop share of all sessions) and compare the standardised rates.
6. Run a two-proportion z-test (A versus B) within desktop, within mobile and pooled. Report z and the two-sided p-value for each.
7. Build a day-by-day table of the pooled conversion rate of A and B and the desktop share of B. On how many of the 14 days does B beat A pooled?
8. Count the `csat` responses. What share of all sessions answered, how many answers come from non-converting sessions, and what are the mean scores for A and B? What population do those scores describe?
9. *Explain in three sentences* what went wrong in the experiment design, which number you would report to the product owner and one limitation of your fix.

## Grafana

Import `grafana/dashboard.json` (no data-source setup is needed).

- In "Conversion rate: pooled vs segments vs standardised", which bars flip the ranking compared with the pooled group?
- In "Who saw which variant?", how different are the two bars, and how does that explain the paradox?
- In "Daily pooled rate...", is the pooled advantage of B a one-off or present every day?

## Deliverable

A short note (6-10 lines) titled *Should we ship B?* with three named parts: **Headline versus segments** (pooled and per-device rates), **Why they disagree**
(the mix, with numbers) and **Recommendation** (which comparison to trust, what to run next, what the survey cannot show). Include one chart.
"""
