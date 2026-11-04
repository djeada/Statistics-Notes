"""Lesson 18 - Permutation tests (exact enumeration, 5 vs 5 = 252 labelings)."""
import itertools
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl.utils import get_column_letter
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import HEADER_FILL, HEADER_FONT, Book, Dash, md, write_csv  # noqa: E402

SLUG = "18-permutation-tests"
TITLE = "Permutation tests"
MODULE = "Uncertainty and statistical inference"
DATASET = "10 usability-test participants (5 old flow, 5 new flow), time to finish onboarding in minutes"
N, K = 10, 5


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1824)
    old = np.round(rng.lognormal(np.log(12), 0.25, K), 1)
    new = np.round(rng.lognormal(np.log(9.5), 0.25, K), 1)
    flow = np.array(["new"] * K + ["old"] * K)
    mins = np.r_[new, old]
    order = np.random.default_rng(99).permutation(N)
    return pd.DataFrame({"participant_id": np.arange(1, N + 1), "flow": flow[order], "task_minutes": mins[order]})


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    x = df["task_minutes"].to_numpy()
    isnew = (df["flow"] == "new").to_numpy()
    combs = list(itertools.combinations(range(N), K))  # every way to pick which 5 people get "new"
    M = np.zeros((len(combs), N), dtype=int)
    for i, c in enumerate(combs):
        M[i, list(c)] = 1
    R = lambda v: np.round(v, 9)
    mdiff = R(np.array([x[m == 1].mean() - x[m == 0].mean() for m in M]))
    meddiff = R(np.array([np.median(x[m == 1]) - np.median(x[m == 0]) for m in M]))
    obs = float(R(x[isnew].mean() - x[~isnew].mean()))
    obs_med = float(R(np.median(x[isnew]) - np.median(x[~isnew])))
    p2 = float((np.abs(mdiff) >= abs(obs) - 1e-9).mean())
    p1 = float((mdiff <= obs + 1e-9).mean())
    p2m = float((np.abs(meddiff) >= abs(obs_med) - 1e-9).mean())
    tt = stats.ttest_ind(x[isnew], x[~isnew], equal_var=True)
    sp = float(np.sqrt((x[isnew].var(ddof=1) + x[~isnew].var(ddof=1)) / 2))
    nperm = len(combs)

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 18 - Permutation tests",
             "Exact test: the 'Permutations' sheet lists all 252 ways to give 5 of the 10 people the 'new' label.")
    b.add_column("new_minutes", lambda r: f'=IF(Data!B{r}="new",Data!C{r},"")', expected=np.where(isnew, x, np.nan), fmt="0.0")
    b.add_column("old_minutes", lambda r: f'=IF(Data!B{r}="old",Data!C{r},"")', expected=np.where(~isnew, x, np.nan), fmt="0.0")
    NEW, OLD = b.rng("new_minutes"), b.rng("old_minutes")

    ps = b.wb.create_sheet("Permutations", 1)
    # layout: A id | B..K label (1 = 'new') | M..V new-group values | X..AG old-group values | AH mean diff | AI median diff
    ps["A1"], ps["A2"] = "perm", "x (minutes) ->"
    for j in range(N):
        c = ps.cell(row=1, column=2 + j, value=f"p{j + 1}")
        ps.cell(row=2, column=2 + j, value=f"=Data!C{j + 2}")
        ps.cell(row=1, column=13 + j, value=f"new{j + 1}")
        ps.cell(row=1, column=24 + j, value=f"old{j + 1}")
    ps.cell(row=1, column=34, value="mean diff (new-old)")
    ps.cell(row=1, column=35, value="median diff (new-old)")
    for c in range(1, 36):
        ps.cell(row=1, column=c).fill, ps.cell(row=1, column=c).font = HEADER_FILL, HEADER_FONT
    for i, m in enumerate(M):
        r = 3 + i
        ps.cell(row=r, column=1, value=i + 1)
        for j in range(N):
            L = get_column_letter(2 + j)
            ps.cell(row=r, column=2 + j, value=int(m[j]))
            ps.cell(row=r, column=13 + j, value=f'=IF({L}{r}=1,{L}$2,"")')
            ps.cell(row=r, column=24 + j, value=f'=IF({L}{r}=0,{L}$2,"")')
        ps.cell(row=r, column=34, value=f"=ROUND(AVERAGE(M{r}:V{r})-AVERAGE(X{r}:AG{r}),9)").number_format = "0.000"
        ps.cell(row=r, column=35, value=f"=ROUND(MEDIAN(M{r}:V{r})-MEDIAN(X{r}:AG{r}),9)").number_format = "0.000"
        b.checks.append((f"Permutations!AH{r}", f"mean diff perm {i + 1}", float(mdiff[i])))
        b.checks.append((f"Permutations!AI{r}", f"median diff perm {i + 1}", float(meddiff[i])))
    last = 2 + nperm
    PM = f"Permutations!$AH$3:$AH${last}"
    PD = f"Permutations!$AI$3:$AI${last}"

    b.section("1. The two groups")
    rows = [["new flow", f"=COUNT({NEW})", f"=AVERAGE({NEW})", f"=MEDIAN({NEW})", f"=STDEV({NEW})"],
            ["old flow", f"=COUNT({OLD})", f"=AVERAGE({OLD})", f"=MEDIAN({OLD})", f"=STDEV({OLD})"]]
    exp = {}
    for i, g in enumerate([x[isnew], x[~isnew]]):
        exp.update({(i, 1): len(g), (i, 2): g.mean(), (i, 3): float(np.median(g)), (i, 4): g.std(ddof=1)})
    g0, g1 = b.table(["Group", "n", "Mean", "Median", "SD"], rows, fmt={2: "0.00", 3: "0.00", 4: "0.00"}, expect=exp)

    b.section("2. Observed test statistics (new minus old)")
    r_obs = b.row("Observed mean difference (min)", f"=ROUND(AVERAGE({NEW})-AVERAGE({OLD}),9)", obs, "0.000")
    r_objm = b.row("Observed median difference (min)", f"=ROUND(MEDIAN({NEW})-MEDIAN({OLD}),9)", obs_med, "0.000")

    b.section("3. Exact permutation distribution (all 252 labelings)")
    r_np = b.row("Number of labelings = C(10,5)", "=COMBIN(10,5)", nperm, "0")
    b.row("Count of labelings in the permutation sheet", f"=COUNT({PM})", nperm, "0")
    r_ext = b.row("Labelings with |diff| >= |observed|",
                  f'=COUNTIF({PM},">="&ABS({b.local(r_obs)})-0.000001)+COUNTIF({PM},"<="&-ABS({b.local(r_obs)})+0.000001)',
                  float((np.abs(mdiff) >= abs(obs) - 1e-9).sum()), "0")
    r_p2 = b.row("Two-sided permutation p-value (mean)", f"={b.local(r_ext)}/{b.local(r_np)}", p2, "0.0000")
    r_p1 = b.row("One-sided p-value (new is faster)", f'=COUNTIF({PM},"<="&{b.local(r_obs)}+0.000001)/{b.local(r_np)}', p1, "0.0000")
    r_ext_m = b.row("Labelings with |median diff| >= |observed|",
                    f'=COUNTIF({PD},">="&ABS({b.local(r_objm)})-0.000001)+COUNTIF({PD},"<="&-ABS({b.local(r_objm)})+0.000001)',
                    float((np.abs(meddiff) >= abs(obs_med) - 1e-9).sum()), "0")
    r_p2m = b.row("Two-sided permutation p-value (median)", f"={b.local(r_ext_m)}/{b.local(r_np)}", p2m, "0.0000")
    r_min = b.row("Smallest possible two-sided p-value", f"=2/{b.local(r_np)}", 2 / nperm, "0.0000",
                  "Only the observed split and its mirror image")

    b.section("4. The same comparison with a t-test (equal variances, 8 df)")
    r_sp = b.row("Pooled SD (min)", f"=SQRT((VAR({NEW})+VAR({OLD}))/2)", sp, "0.000")
    r_t = b.row("t statistic", f"={b.local(r_obs)}/({b.local(r_sp)}*SQRT(1/COUNT({NEW})+1/COUNT({OLD})))", float(tt.statistic), "0.000")
    r_tp = b.row("Two-sided p-value (t, df = 8)", f"=TDIST(ABS({b.local(r_t)}),COUNT({NEW})+COUNT({OLD})-2,2)", float(tt.pvalue), "0.0000")
    r_d = b.row("Cohen's d (effect size)", f"={b.local(r_obs)}/{b.local(r_sp)}", obs / sp, "0.00", "Difference in pooled-SD units")
    alpha = b.row("Significance level", 0.05, None, "0.00", "Edit me", is_input=True)
    b.row("Permutation test significant (mean)?", f'=IF({b.local(r_p2)}<{b.local(alpha)},"yes","no")', None)
    b.row("t-test significant?", f'=IF({b.local(r_tp)}<{b.local(alpha)},"yes","no")', None)

    b.section("5. Permutation distribution of the mean difference (1-minute buckets)")
    edges = np.arange(-9, 9, 1)
    cnt, _ = np.histogram(mdiff, bins=np.r_[edges, 9])
    rows, exp = [], {}
    for i, e in enumerate(edges):
        rr = b.next_row + 1 + i
        rows.append([f"{e}", e, f'=COUNTIFS({PM},">="&B{rr},{PM},"<"&B{rr}+1)'])
        exp[(i, 2)] = float(cnt[i])
    h0, h1 = b.table(["Bucket", "From", "Labelings"], rows, fmt={1: "0", 2: "0"}, expect=exp)
    b.bar_chart_from_table("All 252 labelings: mean difference (min)", 1, [3], h0, h1, anchor="H4",
                           x_title="difference of means, new - old (min); bucket start", y_title="labelings")

    b.answers([
        ("Group means, medians and the observed differences", f"={r_obs}",
         f"New flow mean {x[isnew].mean():.2f} min, old {x[~isnew].mean():.2f} min: difference {obs:.2f} min "
         f"(medians {np.median(x[isnew]):.1f} vs {np.median(x[~isnew]):.1f}, difference {obs_med:.1f})."),
        ("How many labelings are there?", f"={r_np}",
         f"C(10,5) = {nperm}. If the flow did not matter, each of them was equally likely to be the one we observed."),
        ("Labelings at least as extreme as the observed |difference|", f"={r_ext}",
         f"{int((np.abs(mdiff) >= abs(obs) - 1e-9).sum())} of {nperm}: the observed split and its mirror image plus the others that "
         f"differ by {abs(obs):.2f} min or more in either direction."),
        ("Two-sided permutation p-value (mean)", f"={r_p2}",
         f"p = {p2:.4f} ({int(round(p2 * nperm))}/{nperm}). Just above 0.05: if the two flows were equivalent, a difference this large would "
         f"arise by labeling alone about {p2:.1%} of the time. One-sided p = {p1:.4f}."),
        ("t-test p-value and comparison", f"={r_tp}",
         f"Pooled t = {tt.statistic:.2f}, p = {tt.pvalue:.4f}: just *below* 0.05, so the verdicts differ. The t-test relies on a normal "
         f"approximation that is shaky with 5 points per group; the permutation p-value needs no distribution assumption."),
        ("Permutation p-value for the difference in medians", f"={r_p2m}",
         f"p = {p2m:.4f} ({int(round(p2m * nperm))}/{nperm}): clearly not significant. Any statistic can be tested, but the median of 5 numbers "
         f"is a very blunt instrument."),
        ("Smallest p-value this design can ever give", f"={r_min}",
         f"{2 / nperm:.4f}: with 252 labelings p-values come in steps of 1/126 and cannot be smaller than 2/252. "
         f"(With 3 vs 3 people the minimum is 0.10.)"),
        ("Effect size", f"={r_d}",
         f"Cohen's d = {obs / sp:.2f}: a large effect (about {abs(obs) / x.mean():.0%} of the average task time) that the sample is too small "
         f"to pin down."),
        ("Verdict and limitations", "text",
         "Borderline evidence the new flow is faster. With n = 5 per group a single unusual participant can flip the conclusion; "
         "the test also assumes the flow was assigned at random (otherwise exchangeability fails) and says nothing about "
         "participants who were not in the study."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-18-permutation", "18 · Permutation tests",
             "Exact permutation test for 5 vs 5 participants: all 252 relabelings, p-value as a proportion, and the t-test for comparison.")
    d.stat("Result", {"observed diff (min)": obs, "perm p (mean)": p2, "perm p (median)": p2m, "t-test p": float(tt.pvalue)}, "Mean difference new - old and two-sided p-values (252 labelings).", decimals=3,
           thresholds=[(None, "blue")])
    rng = np.random.default_rng(5)
    xs = np.where(isnew, 1.0, 2.0) + rng.uniform(-0.12, 0.12, N)
    dots = pd.DataFrame({"group_pos": xs, "new": np.where(isnew, x, np.nan), "old": np.where(~isnew, x, np.nan)})
    d.xy("Task time by flow (1 = new, 2 = old)", dots, "group_pos", ["new", "old"],
         "Each dot is a participant (horizontal position is jitter).", w=8)

    def hist(v, ob, label, step=1.0):
        e = np.arange(np.floor(v.min() / step) * step, v.max() + step, step)
        ext = np.abs(v) >= abs(ob) - 1e-9
        c_ext, _ = np.histogram(v[ext], bins=np.r_[e, e[-1] + step])
        c_less, _ = np.histogram(v[~ext], bins=np.r_[e, e[-1] + step])
        return pd.DataFrame({label: [f"{a:.0f}" for a in e], "at least as extreme as observed": np.where(c_ext > 0, c_ext, np.nan),
                             "less extreme": np.where(c_less > 0, c_less, np.nan)})

    def recolor(panel):
        panel["options"]["showValue"] = "never"
        panel["fieldConfig"]["overrides"] = [
            {"matcher": {"id": "byName", "options": n}, "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": c}}]}
            for n, c in (("at least as extreme as observed", "#E15759"), ("less extreme", "#9AA5B1"))]

    d.bars("Permutation distribution: mean difference", hist(mdiff, obs, "diff_min"),
           "Mean difference (new - old, minutes; bucket start) for each of the 252 labelings. Red = at least as extreme as what we observed; "
           "their share is the p-value.", stacking="normal", w=8)
    recolor(d.panels[-1])
    d.bars("Permutation distribution: median difference", hist(meddiff, obs_med, "diff_min", 1.0),
           "Same for the difference in medians - coarser, because a median of 5 values takes few distinct values.",
           stacking="normal", w=8)
    recolor(d.panels[-1])
    d.bars("p-values by method", pd.DataFrame({"method": ["perm. (mean)", "perm. (median)", "t-test"],
                                               "p-value": [p2, p2m, float(tt.pvalue)]}),
           "Two-sided p-values. Compare each bar with 0.05.", w=8)
    summ = pd.DataFrame({"group": ["new flow", "old flow"], "n": [K, K],
                         "mean_min": [x[isnew].mean(), x[~isnew].mean()],
                         "median_min": [np.median(x[isnew]), np.median(x[~isnew])],
                         "sd_min": [x[isnew].std(ddof=1), x[~isnew].std(ddof=1)]}).round(2)
    d.table("Group summary", summ, "The inputs of the test.", w=16)
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: permutation tests

## The question a permutation test answers

You gave 5 people a new onboarding flow and 5 people the old one, and the new group was faster on average. Was that the
flow, or just which people landed in which group? A permutation test answers directly: **if the label did not matter, how often
would shuffling the labels produce a difference at least this large?** No normal distribution and no formula for a standard error
are needed - only the data and a computer. It prevents the failure of declaring victory because of a number that random assignment alone often produces.

## The logic

- **Null hypothesis (exchangeability):** the outcome of each participant would have been the same whichever group they were in, so every
  relabeling of the data is as likely as the one observed.
- **Test statistic** $T$: any number that measures the effect, e.g. $T = \bar x_{new} - \bar x_{old}$ (or a difference of medians, a ratio, a correlation).
- **Reference distribution:** compute $T$ for every relabeling. With $n_1 + n_2 = n$ people there are $\binom{n}{n_1}$ of them.
- **p-value:** the proportion of relabelings whose statistic is at least as extreme as the observed one:

$$
p = \frac{\#\{\text{labelings with } |T^*| \ge |T_{obs}|\}}{\binom{n}{n_1}}.
$$

The observed labeling is one of the labelings, so $p \ge 1/\binom{n}{n_1}$ and it is never exactly zero.

## Worked example (3 vs 3, computed)

Group A $=\{4,5,6\}$, group B $=\{7,9,11\}$: $\bar x_A = 5$, $\bar x_B = 9$, $T_{obs} = -4$. There are
$\binom{6}{3} = 20$ ways to choose which 3 values are called "A". Their mean differences take the values
$\pm 4,\ \pm 3.33,\ \pm 2.67,\ \pm 2,\ \pm 1.33,\ \pm 0.67,\ 0$; only two labelings reach $|T| \ge 4$
(the observed one and its mirror image). So $p = 2/20 = 0.10$ two-sided, or $0.05$ one-sided. The pooled t-test on the same
data gives $t = -3.10$, $p = 0.036$ - it "finds" an effect the exact test says is impossible to establish with 6 observations:
**the smallest two-sided p-value 3 vs 3 can produce is 0.10**.

## Exact versus Monte Carlo

$\binom{10}{5} = 252$ labelings are easy to enumerate in a spreadsheet (this lesson does exactly that). $\binom{20}{10} = 184\,756$ is
already too many for a sheet, and $\binom{100}{50} \approx 10^{29}$ is impossible. Then you draw $B$ random relabelings
(thousands, in code) and use

$$
\hat p = \frac{1 + \#\{|T^*_b| \ge |T_{obs}|\}}{B + 1},
$$

where the "+1" counts the observed labeling and keeps $\hat p > 0$. The Monte Carlo error is about $\sqrt{p(1-p)/B}$. In a
spreadsheet the random labelings must be pre-generated (see [Monte Carlo simulation](../20-monte-carlo-simulation/theory.md)) so that the answer is reproducible.

## Comparison with the t-test

The two-sample t-test computes the same kind of statistic but gets its reference distribution from a theoretical formula: it assumes
normal data (or enough data for the CLT) and, in the pooled version, equal variances. With large $n$ or well-behaved data the two p-values are close.
With small, skewed samples they can disagree in either direction. The permutation test is not "more powerful"; its advantage is
that its validity rests on **random assignment**, not on a distribution. In the lesson's data the t-test just clears 0.05 while the permutation test just misses.

## Two-sided, one-sided, and other statistics

Use two-sided counts $|T^*| \ge |T_{obs}|$ unless a direction was committed to *before* seeing the data. The same recipe tests any
statistic: difference of medians, difference of proportions (A/B tests, [lesson 19](../19-a-b-testing-and-effect-sizes/theory.md)),
correlation (shuffle one column), a difference of variances. Discrete statistics produce ties and coarse p-values (a median of 5 values takes few distinct values).

## Assumptions and pitfalls

1. **Exchangeability is not automatic.** It holds when units were *randomly assigned*; with observational groups (e.g. users who chose the new flow) the test is valid
   only for "no association", not for "no causal effect".
2. **The p-value is not the probability the null is true** nor the probability of the result being "chance"; it is a tail proportion computed under the null.
3. **Tiny samples have a floor on p** (see the 3 vs 3 example); say so instead of reporting "p = 0.00".
4. **Dependent observations** (repeated measures, time series) must be permuted in blocks or within subject; shuffling individual rows breaks the dependence.
5. **A single outlier** changes means a lot; choose the statistic (mean, median, trimmed mean) before looking at the data, and report the effect size, not just $p$.
6. Do not run many statistics until one passes: each one needs its own multiplicity correction.

## Connections

- Bootstrap (resampling *with* replacement, to estimate uncertainty) in [lesson 17](../17-bootstrapping-and-confidence-intervals/theory.md); permutation (resampling *without* replacement, to test a null).
- Sampling variability of a difference of means: [lesson 16](../16-sampling-distributions-and-the-clt/theory.md).
- Repo notes: [hypothesis testing](../../notes/hypothesis_testing_and_confidence_intervals/hypothesis_testing.md),
  [null hypothesis](../../notes/hypothesis_testing_and_confidence_intervals/null_hypothesis.md),
  [resampling](../../notes/resampling_and_model_assessment/resampling.md).
"""

TASK = r"""
# Task: is the new onboarding flow really faster?

## Scenario

A product team tested a redesigned onboarding flow with 10 volunteers. Five were randomly given the **new** flow and five the
**old** one; each was timed on the same set-up task. The new flow looks faster, and a colleague's t-test says
"significant". Before the redesign is rolled out to everyone, you are asked to check the claim without trusting a normal approximation:
by asking how often **random relabeling** of the same 10 numbers beats the observed difference.

## Data

`data.csv` - 10 rows, one per participant.

| column | meaning |
|---|---|
| `participant_id` | 1-10 |
| `flow` | `new` or `old` (randomly assigned, 5 each) |
| `task_minutes` | time to finish the set-up task, minutes |

## Questions

Work in a spreadsheet; the solution uses a second sheet listing every one of the $\binom{10}{5} = 252$ ways to pick which 5
participants get the "new" label (you can generate them yourself or build a smaller 3 vs 3 version by hand first).

1. Compute count, mean, median and standard deviation of `task_minutes` for each flow, and the observed differences of means and of medians (new - old).
2. How many different labelings (which 5 of 10 are "new") are there? Why is each equally likely under the null hypothesis?
3. For every labeling compute the difference of means. How many labelings give $|\text{difference}| \ge |\text{observed}|$?
4. What is the two-sided permutation p-value? What is the one-sided p-value (new is faster)?
5. Run the t-test for the same data (pooled variances, 8 degrees of freedom): t statistic and two-sided p-value (`TDIST`). Do the two tests reach the same decision at 5 %?
6. Repeat the permutation test with the difference of **medians**. What p-value do you get, and why is it coarser?
7. What is the smallest two-sided p-value this design can give? What would it be with only 3 vs 3 participants?
8. Compute Cohen's d. Is the effect large? Is the sample large enough to be sure?
9. *Interpretation:* write two sentences for the product manager - what the p-value means here, and two reasons not to roll out on this evidence alone.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Task time by flow", how much do the two groups overlap?
- In "Permutation distribution: mean difference", where do the red bars lie and what share of all labelings do they make up?
- In "p-values by method", which bars are on which side of 0.05, and what does that say about trusting one test?

## Deliverable

A short note (5-8 lines) with named parts: **Result** (difference and both p-values), **Reasoning** (what the permutation p-value
counts), **Decision** (roll out / collect more data) and **Limitation**. Include one chart of the permutation distribution with the observed value marked.
"""
