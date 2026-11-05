"""Lesson 19 - A/B testing and effect sizes."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "19-a-b-testing-and-effect-sizes"
TITLE = "A/B testing and effect sizes"
MODULE = "Uncertainty and statistical inference"
DATASET = "28-day checkout A/B test: visitors and conversions per day x variant x device (112 rows)"
DAYS = 28
ALPHA, POWER = 0.05, 0.80
PRACTICAL = 0.003  # smallest absolute lift worth shipping: +0.3 percentage points


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1928)
    dates = pd.date_range("2026-04-06", periods=DAYS, freq="D")  # starts on a Monday
    dow = np.array([1.0, 1.0, 1.0, 1.05, 1.1, 0.85, 0.8])
    rows = []
    for dt in dates:
        tot = int(1500 * dow[dt.weekday()] * rng.uniform(0.92, 1.08))
        for v in ["A", "B"]:
            n_tot = int(tot * rng.uniform(0.97, 1.03))
            n_m = int(n_tot * rng.uniform(0.57, 0.63))
            n_d = n_tot - n_m
            pm = {"A": 0.030, "B": 0.0345}[v]  # B only helps on mobile
            rows.append((dt, v, "mobile", n_m, rng.binomial(n_m, pm)))
            rows.append((dt, v, "desktop", n_d, rng.binomial(n_d, 0.050)))
    return pd.DataFrame(rows, columns=["date", "variant", "device", "visitors", "conversions"])


def two_prop(cA, nA, cB, nB):
    pA, pB = cA / nA, cB / nB
    pool = (cA + cB) / (nA + nB)
    se0 = np.sqrt(pool * (1 - pool) * (1 / nA + 1 / nB))
    z = (pB - pA) / se0
    se1 = np.sqrt(pA * (1 - pA) / nA + pB * (1 - pB) / nB)
    return pA, pB, pB - pA, z, 2 * stats.norm.sf(abs(z)), se1


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    g = df.groupby("variant")[["visitors", "conversions"]].sum()
    nA, nB = int(g.loc["A", "visitors"]), int(g.loc["B", "visitors"])
    cA, cB = int(g.loc["A", "conversions"]), int(g.loc["B", "conversions"])
    pA, pB, diff, z, pval, se1 = two_prop(cA, nA, cB, nB)
    zc = float(stats.norm.ppf(1 - ALPHA / 2))
    zb = float(stats.norm.ppf(POWER))
    lo, hi = diff - zc * se1, diff + zc * se1
    h = 2 * (np.arcsin(np.sqrt(pB)) - np.arcsin(np.sqrt(pA)))
    mde = (zc + zb) * np.sqrt(pA * (1 - pA) * (1 / nA + 1 / nB))
    n_req = float(np.ceil((zc + zb) ** 2 * (pA * (1 - pA) + (pA + PRACTICAL) * (1 - pA - PRACTICAL)) / PRACTICAL ** 2))
    per_day = nA / DAYS
    days_req = n_req / per_day
    pool = (cA + cB) / (nA + nB)
    se0 = np.sqrt(pool * (1 - pool) * (1 / nA + 1 / nB))

    # cumulative (peeking) table
    cum = []
    for k, dt in enumerate(sorted(df["date"].unique())):
        s = df[df["date"] <= dt].groupby("variant")[["visitors", "conversions"]].sum()
        r = two_prop(s.loc["A", "conversions"], s.loc["A", "visitors"], s.loc["B", "conversions"], s.loc["B", "visitors"])
        cum.append((k + 1, pd.Timestamp(dt), int(s.loc["A", "visitors"]), int(s.loc["A", "conversions"]),
                    int(s.loc["B", "visitors"]), int(s.loc["B", "conversions"]), r[3], r[2], r[1], r[0]))
    cz = np.array([c[6] for c in cum])
    flag = (np.abs(cz) > zc).astype(int)
    first = int(np.argmax(flag)) + 1
    n_flag = int(flag.sum())
    after = int(((flag[first - 1:]) == 0).sum())

    dev = {}
    for d_ in ["mobile", "desktop"]:
        s = df[df.device == d_].groupby("variant")[["visitors", "conversions"]].sum()
        dev[d_] = (int(s.loc["A", "visitors"]), int(s.loc["A", "conversions"]), int(s.loc["B", "visitors"]),
                   int(s.loc["B", "conversions"]))

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 19 - A/B testing and effect sizes",
             "Solved workbook. Yellow cells are assumptions you can change; everything else is a live formula.")
    b.add_column("conv_rate", lambda r: f"=E{r}/D{r}", expected=(df.conversions / df.visitors).to_numpy(), fmt="0.00%")
    V, C, VAR, DEV, DT = (b.rng(n) for n in ["visitors", "conversions", "variant", "device", "date"])

    b.section("1. Totals by variant (28 days, both devices)")
    rows = [["A (control)", f'=SUMIFS({V},{VAR},"A")', f'=SUMIFS({C},{VAR},"A")', f"=C{b.next_row + 1}/B{b.next_row + 1}"],
            ["B (new checkout)", f'=SUMIFS({V},{VAR},"B")', f'=SUMIFS({C},{VAR},"B")', f"=C{b.next_row + 2}/B{b.next_row + 2}"]]
    t0, t1 = b.table(["Variant", "Visitors", "Conversions", "Conversion rate"], rows, fmt={1: "#,##0", 2: "#,##0", 3: "0.000%"},
                     expect={(0, 1): nA, (0, 2): cA, (0, 3): pA, (1, 1): nB, (1, 2): cB, (1, 3): pB})
    nAc, cAc, pAc, nBc, cBc, pBc = f"$B${t0}", f"$C${t0}", f"$D${t0}", f"$B${t1}", f"$C${t1}", f"$D${t1}"

    b.section("2. Two-proportion z-test")
    alpha = b.row("Significance level alpha", ALPHA, None, "0.00", "Edit me", is_input=True)
    r_diff = b.row("Absolute difference p_B - p_A", f"={pBc}-{pAc}", diff, "0.0000%")
    r_pool = b.row("Pooled rate", f"=({cAc}+{cBc})/({nAc}+{nBc})", pool, "0.000%")
    r_se0 = b.row("Standard error under H0 (pooled)", f"=SQRT({b.local(r_pool)}*(1-{b.local(r_pool)})*(1/{nAc}+1/{nBc}))", se0, "0.00000")
    r_z = b.row("z statistic", f"={b.local(r_diff)}/{b.local(r_se0)}", z, "0.000")
    r_p = b.row("Two-sided p-value", f"=2*(1-NORMSDIST(ABS({b.local(r_z)})))", pval, "0.0000")
    b.row("Significant at alpha?", f'=IF({b.local(r_p)}<{b.local(alpha)},"yes","no")', None)

    b.section("3. Effect size and confidence interval")
    r_se1 = b.row("Unpooled standard error", f"=SQRT({pAc}*(1-{pAc})/{nAc}+{pBc}*(1-{pBc})/{nBc})", se1, "0.00000")
    r_zc = b.row("Critical value z(1-alpha/2)", f"=NORMSINV(1-{b.local(alpha)}/2)", zc, "0.000")
    r_lo = b.row("CI for the difference: lower", f"={b.local(r_diff)}-{b.local(r_zc)}*{b.local(r_se1)}", lo, "0.0000%")
    r_hi = b.row("CI for the difference: upper", f"={b.local(r_diff)}+{b.local(r_zc)}*{b.local(r_se1)}", hi, "0.0000%")
    r_rel = b.row("Relative lift (p_B - p_A) / p_A", f"={b.local(r_diff)}/{pAc}", diff / pA, "0.0%")
    r_rlo = b.row("Relative lift CI: lower (CI / p_A)", f"={b.local(r_lo)}/{pAc}", lo / pA, "0.0%")
    r_rhi = b.row("Relative lift CI: upper (CI / p_A)", f"={b.local(r_hi)}/{pAc}", hi / pA, "0.0%")
    r_h = b.row("Cohen's h", f"=2*(ASIN(SQRT({pBc}))-ASIN(SQRT({pAc})))", h, "0.0000", "|h| < 0.2 is a 'small' effect by convention")

    b.section("4. Practical importance and power")
    prac = b.row("Smallest lift worth shipping (absolute)", PRACTICAL, None, "0.00%", "Edit me: +0.3 percentage points", is_input=True)
    power = b.row("Desired power", POWER, None, "0.00", "Edit me", is_input=True)
    r_zb = b.row("z for the power", f"=NORMSINV({b.local(power)})", zb, "0.000")
    b.row("Does the CI lower bound clear the practical threshold?", f'=IF({b.local(r_lo)}>={b.local(prac)},"yes","no")', None)
    r_mde = b.row("Minimum detectable effect with this n (absolute)",
                  f"=({b.local(r_zc)}+{b.local(r_zb)})*SQRT({pAc}*(1-{pAc})*(1/{nAc}+1/{nBc}))", mde, "0.000%",
                  "Smallest true difference the test detects with the chosen power")
    r_nreq = b.row("Visitors needed per arm for the practical lift",
                   f"=ROUNDUP(({b.local(r_zc)}+{b.local(r_zb)})^2*({pAc}*(1-{pAc})+({pAc}+{b.local(prac)})*(1-{pAc}-{b.local(prac)}))/{b.local(prac)}^2,0)",
                   n_req, "#,##0")
    r_days = b.row("Days needed at the observed traffic", f"={b.local(r_nreq)}/({nAc}/{DAYS})", days_req, "0.0")

    b.section("5. Peeking: the test re-run every day on cumulative data")
    rows, exp = [], {}
    t = b.next_row + 1
    for i, c in enumerate(cum):
        rr = t + i
        rows.append([i + 1, f"=MIN({DT})+A{rr}-1",
                     f'=SUMIFS({V},{VAR},"A",{DT},"<="&B{rr})', f'=SUMIFS({C},{VAR},"A",{DT},"<="&B{rr})',
                     f'=SUMIFS({V},{VAR},"B",{DT},"<="&B{rr})', f'=SUMIFS({C},{VAR},"B",{DT},"<="&B{rr})',
                     f"=(F{rr}/E{rr}-D{rr}/C{rr})/SQRT(((D{rr}+F{rr})/(C{rr}+E{rr}))*(1-(D{rr}+F{rr})/(C{rr}+E{rr}))*(1/C{rr}+1/E{rr}))",
                     f"=IF(ABS(G{rr})>{b.local(r_zc)},1,0)", f"={b.local(r_zc)}", f"=-{b.local(r_zc)}"])
        exp.update({(i, 2): c[2], (i, 3): c[3], (i, 4): c[4], (i, 5): c[5], (i, 6): c[6], (i, 7): flag[i]})
    p0, p1 = b.table(["Day", "Date", "Visitors A", "Conv A", "Visitors B", "Conv B", "z (cumulative)", "|z| > crit", "+crit", "-crit"],
                     rows, fmt={1: "yyyy-mm-dd", 6: "0.00"}, expect=exp)
    b.line_chart_from_table("Cumulative z statistic by day", 1, [7, 9, 10], p0, p1, anchor="L4", x_title="day", y_title="z")
    FL = f"$H${p0}:$H${p1}"
    r_first = b.row("First day with |z| above the critical value", f"=MATCH(1,{FL},0)", first, "0")
    r_nflag = b.row("Number of days with |z| above the critical value", f"=SUM({FL})", n_flag, "0")
    b.row("Final-day z (the planned analysis)", f"=G{p1}", float(cz[-1]), "0.000")

    b.section("6. By device")
    rows, exp = [], {}
    t = b.next_row + 1
    for i, d_ in enumerate(["mobile", "desktop"]):
        rr = t + i
        a, ca, bb, cb = dev[d_]
        pa_, pb_, df_, zz, pp, _ = two_prop(ca, a, cb, bb)
        rows.append([d_, f'=SUMIFS({V},{VAR},"A",{DEV},A{rr})', f'=SUMIFS({C},{VAR},"A",{DEV},A{rr})',
                     f'=SUMIFS({V},{VAR},"B",{DEV},A{rr})', f'=SUMIFS({C},{VAR},"B",{DEV},A{rr})',
                     f"=C{rr}/B{rr}", f"=E{rr}/D{rr}", f"=G{rr}-F{rr}",
                     f"=H{rr}/SQRT(((C{rr}+E{rr})/(B{rr}+D{rr}))*(1-(C{rr}+E{rr})/(B{rr}+D{rr}))*(1/B{rr}+1/D{rr}))",
                     f"=2*(1-NORMSDIST(ABS(I{rr})))"])
        exp.update({(i, 1): a, (i, 2): ca, (i, 3): bb, (i, 4): cb, (i, 5): pa_, (i, 6): pb_, (i, 7): df_, (i, 8): zz, (i, 9): pp})
    d0, d1 = b.table(["Device", "Visitors A", "Conv A", "Visitors B", "Conv B", "Rate A", "Rate B", "Difference", "z", "p-value"], rows,
                     fmt={1: "#,##0", 3: "#,##0", 5: "0.00%", 6: "0.00%", 7: "0.00%", 8: "0.00", 9: "0.0000"}, expect=exp)
    pm_, pd_ = [two_prop(dev[k][1], dev[k][0], dev[k][3], dev[k][2]) for k in ("mobile", "desktop")]

    pk = f"{first}"
    b.answers([
        ("Conversion rate of A and B", f"=Analysis!{pBc}",
         f"A: {cA:,}/{nA:,} = {pA:.3%}; B: {cB:,}/{nB:,} = {pB:.3%}. Difference {diff * 100:+.3f} percentage points."),
        ("Absolute difference and relative lift", f"={r_rel}",
         f"{diff * 100:+.3f} pp absolute; relative lift {diff / pA:+.1%} (a small absolute number on a small base looks bigger in relative terms)."),
        ("Pooled z statistic and two-sided p-value", f"={r_p}",
         f"z = {z:.2f}, p = {pval:.4f}: below 0.05, so the overall difference is statistically significant."),
        ("95% CI for the difference", f"={r_lo}",
         f"[{lo * 100:.3f}, {hi * 100:.3f}] pp. The lower end is near zero: the data allow a tiny lift as well as a large one."),
        ("Cohen's h", f"={r_h}",
         f"h = {h:.3f}, far below the 0.2 'small' benchmark. With conversion rates this low, h is naturally small - judge by money, not by the label."),
        ("Is the lift practically important? (threshold +0.3 pp)", f"={r_lo}",
         f"The point estimate {diff * 100:.2f} pp is "
         f"{'above' if diff >= PRACTICAL else 'below'} the 0.3 pp threshold, but the CI lower bound ({lo * 100:.2f} pp) is below it: "
         f"statistically significant is not the same as practically proven."),
        ("MDE and the sample size needed for the practical lift", f"={r_nreq}",
         f"With {nA:,} visitors per arm the test can reliably detect {mde * 100:.2f} pp (80% power); detecting {PRACTICAL * 100:.1f} pp needs "
         f"{n_req:,.0f} per arm (about {days_req:.0f} days at this traffic)."),
        ("First day a daily 'peeker' would have declared a winner", f"={r_first}",
         f"Day {first}. |z| exceeded {zc:.2f} on {n_flag} of {DAYS} days in total and fell back below it on {after} days after the first crossing: "
         f"the final-day z ({cz[-1]:.2f}) is the only one that matches the planned sample size."),
        ("Results by device", f"=Analysis!I{d0}",
         f"Mobile: {pm_[0]:.2%} -> {pm_[1]:.2%} ({pm_[2] * 100:+.2f} pp, z = {pm_[3]:.2f}, p = {pm_[4]:.4f}); desktop: {pd_[0]:.2%} -> "
         f"{pd_[1]:.2%} ({pd_[2] * 100:+.2f} pp, p = {pd_[4]:.2f}). The effect is concentrated on mobile; the desktop traffic dilutes the overall lift."),
        ("Recommendation and limitations", "text",
         "Ship to mobile (a subgroup chosen after looking at the data, so confirm with a follow-up test) and do not claim a "
         "site-wide lift. Limitations: device was a post-hoc split, 28 days cover only four weekly cycles, "
         "and one two-sided test at alpha = 0.05 still has a 5% false-positive rate."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-19-ab-test", "19 · A/B testing and effect sizes",
             "28-day checkout experiment: two-proportion z-test, effect sizes, and what peeking at the data every day would have shown.",
             pd.DataFrame({"time": df["date"]}), "time")
    d.stat("Conversion rates and relative lift", {"rate A": pA, "rate B": pB, "relative lift": diff / pA},
           "Overall, both devices pooled.", unit="percentunit", decimals=2, w=12)
    d.stat("Test result", {"lift (percentage points)": diff * 100, "z": z, "p-value": pval},
           "Two-proportion z-test, pooled standard error, two-sided.", decimals=3, w=12)
    cdf = pd.DataFrame({"time": [c[1] for c in cum], "z": cz, "+1.96": zc, "-1.96": -zc})
    d.timeseries("Peeking: cumulative z by day", cdf,
                 "z computed on all data up to each day. Crossing +-1.96 early and falling back is what a daily peeker experiences.",
                 dashed=["+1.96", "-1.96"], colors={"+1.96": "#E15759", "-1.96": "#E15759"}, w=12)
    rdf = pd.DataFrame({"time": [c[1] for c in cum], "A": [c[9] * 100 for c in cum], "B": [c[8] * 100 for c in cum]})
    d.timeseries("Cumulative conversion rate (%)", rdf, "Both variants drift together with traffic mix; the gap is small.", unit="percent", w=12)
    bd = pd.DataFrame({"device": ["mobile", "desktop"], "A": [pm_[0] * 100, pd_[0] * 100], "B": [pm_[1] * 100, pd_[1] * 100]}).round(3)
    d.bars("Conversion rate by device (%)", bd, "The lift is concentrated in one device.", unit="percent", w=8)
    eff = np.arange(0.002, 0.0101, 0.0005)
    need = [np.ceil((zc + zb) ** 2 * (pA * (1 - pA) + (pA + e) * (1 - pA - e)) / e ** 2) / per_day for e in eff]
    d.xy("Days of traffic needed vs lift to detect", pd.DataFrame({"lift_pp": eff * 100, "days_needed": need, "days_we_ran": DAYS}),
         "lift_pp", ["days_needed", "days_we_ran"], "80% power, alpha 0.05, baseline = control rate, current traffic. "
         "Halving the detectable lift quadruples the duration.", lines=["days_needed", "days_we_ran"], w=8)
    tab = pd.DataFrame({"method": ["difference (pp)", "CI lower (pp)", "CI upper (pp)", "Cohen's h", "MDE (pp)", "needed n/arm for +0.3 pp"],
                        "value": [diff * 100, lo * 100, hi * 100, h, mde * 100, n_req]}).round(3)
    d.table("Effect sizes and power", tab, "Practical-importance numbers from the analysis.", w=8)
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: A/B testing and effect sizes

## What the test is for

A/B testing is a randomized experiment: visitors are assigned at random to the control (A) or the variant (B) and a metric is
compared. Randomization is what lets you read a difference as *caused* by the variant. The statistics have two jobs: say
whether the difference could be noise (**significance**), and say how big it is (**effect size**). Teams that report only the first
ship changes that do nothing; teams that stop the test at the first good-looking number ship false wins.

## The two-proportion z-test

With $n_A, n_B$ visitors and $c_A, c_B$ conversions, $\hat p_A = c_A/n_A$, $\hat p_B = c_B/n_B$ and the pooled rate
$\hat p = (c_A + c_B)/(n_A + n_B)$:

$$
z = \frac{\hat p_B - \hat p_A}{\sqrt{\hat p (1-\hat p)\,(1/n_A + 1/n_B)}},\qquad p = 2\,(1 - \Phi(|z|)).
$$

The pooled standard error is correct *under the null* (equal rates), so it is used for the test. A **confidence interval** for the difference
is not computed under the null and uses the unpooled standard error:

$$
(\hat p_B - \hat p_A) \pm z_{1-\alpha/2}\sqrt{\tfrac{\hat p_A(1-\hat p_A)}{n_A} + \tfrac{\hat p_B(1-\hat p_B)}{n_B}}.
$$

The normal approximation needs roughly at least 10 conversions and 10 non-conversions in each arm. For tiny counts use Fisher's exact test or a
[permutation test](../18-permutation-tests/theory.md).

## Effect sizes

- **Absolute difference** $\hat p_B - \hat p_A$ (percentage points): what the business actually earns.
- **Relative lift** $(\hat p_B - \hat p_A)/\hat p_A$: easy to read, easy to exaggerate on a small base. Its CI is obtained approximately by dividing the CI of the difference by $\hat p_A$.
- **Cohen's h** $= 2\arcsin\sqrt{\hat p_B} - 2\arcsin\sqrt{\hat p_A}$: a standardized difference for proportions, independent of the base
  rate; conventional labels are 0.2 small, 0.5 medium, 0.8 large. For conversion rates of a few percent even valuable lifts have small $h$, so judge importance in money.

## Worked example (computed)

Control: 200 conversions of 4000 ($5.0\%$); variant: 240 of 4000 ($6.0\%$). Difference $+1.0$ pp, relative lift $+20\%$.
Pooled rate $5.5\%$, $SE_0 = 0.00510$, $z = 1.962$, $p = 0.0498$ - just significant. The unpooled interval is $[0.00,\ 2.00]$ pp: the lift could be
anywhere from nothing to double the estimate. Cohen's $h = 0.044$. A "+20 % lift, significant!" headline hides all of that.

## Power, minimum detectable effect and sample size

Power is the probability to detect a true difference $\delta$. For two equal arms of size $n$ at significance $\alpha$ and power $1-\beta$:

$$
n \approx \frac{(z_{1-\alpha/2} + z_{1-\beta})^2\,\bigl[p_A(1-p_A) + p_B(1-p_B)\bigr]}{\delta^2}
\qquad\Longleftrightarrow\qquad
\text{MDE} \approx (z_{1-\alpha/2} + z_{1-\beta})\sqrt{p(1-p)\,(1/n_A + 1/n_B)}.
$$

Example: to detect $5\% \to 6\%$ at $\alpha = 0.05$, power $0.80$ you need about **8155 visitors per arm** ($z$-values 1.960 and 0.842).
Since $n \propto 1/\delta^2$, detecting half the lift costs four times the traffic. Fix the **practically important effect** before the test, and size the test for it;
then a non-significant result means "no effect as large as $\delta$", not "no effect".

## Peeking

The p-value is valid for **one** analysis at the planned sample size. If you re-run the test every day and stop at the first $p < 0.05$, you give the random
walk of the cumulative $z$ many chances to cross $\pm 1.96$. In a simulation of 20 000 A/A tests (no true difference; 28 daily
looks of 1500 visitors per arm, base rate 4 %), $27.9\%$ declared a "winner" at some look; with 10 looks $21.4\%$, with 5 looks $16.3\%$, and with a single look $4.9\%$.
Remedies: fix the sample size and the stopping date in advance; or use a sequential design (alpha-spending, always-valid p-values).

## Assumptions and pitfalls

1. **Independent randomization units.** Randomize by user, not by page view; the same user in both arms or repeated visits break the formula.
2. **Sample ratio mismatch.** If a 50/50 split delivers 51/49 on thousands of users, something is wrong with assignment; check before reading the result.
3. **Novelty and weekly cycles.** Run whole weeks; early effects often fade.
4. **Subgroups and many metrics** multiply false positives ([multiple comparisons note](../../notes/hypothesis_testing_and_confidence_intervals/multiple_comparisons.md)). A subgroup found after the fact (e.g. "it works on mobile") is a hypothesis for the next test.
5. **Significance is not importance**, and a large relative lift on a tiny base is not a large gain.
6. **Not significant is not equal.** Report the interval and the MDE.

## Connections

- Sampling variability of a proportion: [lesson 16](../16-sampling-distributions-and-the-clt/theory.md); intervals and bootstrap: [lesson 17](../17-bootstrapping-and-confidence-intervals/theory.md).
- Simpson's paradox when arms differ in device mix: [lesson 5](../05-sampling-bias-and-simpson-s-paradox/theory.md).
- Alarm thresholds and false alarms behave like peeking: [lesson 29](../29-false-alarms-and-detection-performance/theory.md).
- Repo notes: [hypothesis testing](../../notes/hypothesis_testing_and_confidence_intervals/hypothesis_testing.md),
  [type I and II errors](../../notes/hypothesis_testing_and_confidence_intervals/type_i_and_type_ii_errors.md),
  [confidence intervals](../../notes/hypothesis_testing_and_confidence_intervals/confidence_intervals.md).
"""

TASK = r"""
# Task: did the new checkout page win?

## Scenario

An online shop ran a 4-week experiment (Mon 6 Apr - Sun 3 May 2026) of a redesigned checkout page (**B**) against the current
one (**A**). Visitors were split at random. Product wants to ship B site-wide if it lifts conversion by **at least 0.3 percentage points**;
shipping costs engineering time, so a wrong "yes" is expensive. An enthusiastic colleague who checked the dashboard every morning says
"B was significantly better after the second week - we should have shipped then". Evaluate the experiment properly.

## Data

`data.csv` - 112 rows: one per day x variant x device.

| column | meaning |
|---|---|
| `date` | day of the experiment |
| `variant` | `A` (control) or `B` (new checkout) |
| `device` | `mobile` or `desktop` |
| `visitors` | visitors assigned to that variant on that day and device |
| `conversions` | of those, how many completed a purchase |

## Questions

1. Compute visitors, conversions and conversion rate for A and B over all 28 days.
2. Compute the absolute difference (percentage points) and the relative lift.
3. Run the two-proportion z-test (pooled standard error): z and two-sided p-value. Is it significant at 5 %?
4. Compute the 95 % confidence interval for the difference (unpooled standard error). What does it tell you that the p-value does not?
5. Compute Cohen's h. What does the convention call this effect, and is the label useful here?
6. Is the lift practically important (threshold +0.3 pp)? Compare the point estimate *and* the interval with the threshold.
7. What is the minimum detectable effect of this test (80 % power)? How many visitors per arm, and how many days, would be needed to detect +0.3 pp?
8. Re-run the z-test on cumulative data for each day. On which day would a daily peeker first have called a winner, and how many days is |z| above 1.96?
9. Split the analysis by device. Where is the difference?
10. *Interpretation:* give a recommendation in three sentences, including why stopping at the first significant day is invalid and one limitation of the device split.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Peeking: cumulative z by day", when does the line cross the dashed critical values, and what happens afterwards?
- In "Conversion rate by device", for which device do the bars differ?
- In "Days of traffic needed vs lift to detect", where does the "days we ran" line cross the curve, and what lift does that correspond to?

## Deliverable

A decision memo (6-10 lines) with named parts: **Result** (rates, lift, p-value, CI), **Practical importance** (against the 0.3 pp threshold),
**Process** (why the peeking colleague is wrong), **Decision** and **Next step**. Include the cumulative-z chart.
"""
