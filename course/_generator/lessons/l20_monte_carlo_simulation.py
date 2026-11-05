"""Lesson 20 - Monte Carlo simulation (profit / risk model with pre-generated uniform draws)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "20-monte-carlo-simulation"
TITLE = "Monte Carlo simulation"
MODULE = "Uncertainty and statistical inference"
DATASET = "2000 pre-generated uniform random triples (demand, price, unit cost) for a product-launch profit model"
N = 2000
# model assumptions (the yellow cells)
MU_D, SD_D, CAP = 10000, 2500, 11000
P_LO, P_HI = 24.0, 30.0
MU_C, SD_C = 15.0, 1.5
FIXED = 90000
TARGET = 50000


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(2002)
    u = np.clip(np.round(rng.random((N, 3)), 6), 1e-6, 1 - 1e-6)
    return pd.DataFrame({"trial": np.arange(1, N + 1), "u_demand": u[:, 0], "u_price": u[:, 1], "u_cost": u[:, 2]})


def simulate(df: pd.DataFrame):
    d = np.maximum(0, MU_D + SD_D * stats.norm.ppf(df.u_demand.to_numpy()))
    sold = np.minimum(d, CAP)
    price = P_LO + (P_HI - P_LO) * df.u_price.to_numpy()
    cost = MU_C + SD_C * stats.norm.ppf(df.u_cost.to_numpy())
    return d, sold, price, cost, sold * (price - cost) - FIXED


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    dem, sold, price, cost, prof = simulate(df)
    var5 = float(np.percentile(prof, 5))
    cvar5 = float(prof[prof <= var5].mean())
    ploss = float((prof < 0).mean())
    base = min(MU_D, CAP) * ((P_LO + P_HI) / 2 - MU_C) - FIXED
    se_mean = float(prof.std(ddof=1) / np.sqrt(N))

    b = Book(df, "Lesson 20 - Monte Carlo simulation",
             "Data holds the uniform draws (no RAND: the answers are reproducible). Yellow cells are model assumptions you can change.")

    b.section("1. Model assumptions (edit to run what-ifs)")
    a_mu = b.row("Demand: mean (units)", MU_D, None, "#,##0", "Normal distribution", is_input=True)
    a_sd = b.row("Demand: standard deviation (units)", SD_D, None, "#,##0", is_input=True)
    a_cap = b.row("Production capacity (units)", CAP, None, "#,##0", "Units sold = MIN(demand, capacity)", is_input=True)
    a_plo = b.row("Selling price: minimum ($)", P_LO, None, "0.00", "Uniform distribution", is_input=True)
    a_phi = b.row("Selling price: maximum ($)", P_HI, None, "0.00", is_input=True)
    a_cmu = b.row("Unit cost: mean ($)", MU_C, None, "0.00", "Normal distribution", is_input=True)
    a_csd = b.row("Unit cost: standard deviation ($)", SD_C, None, "0.00", is_input=True)
    a_fix = b.row("Fixed launch cost ($)", FIXED, None, "#,##0", is_input=True)
    a_tgt = b.row("Profit target ($)", TARGET, None, "#,##0", is_input=True)

    ud, up, uc = (b.ref(n, 2).replace("Data!", "Data!") for n in ("u_demand", "u_price", "u_cost"))
    b.add_column("demand_units", lambda r: f"=MAX(0,{a_mu}+{a_sd}*NORMSINV(Data!B{r}))", expected=dem, fmt="#,##0")
    b.add_column("units_sold", lambda r: f"=MIN(Data!E{r},{a_cap})", expected=sold, fmt="#,##0")
    b.add_column("price", lambda r: f"={a_plo}+({a_phi}-{a_plo})*Data!C{r}", expected=price, fmt="0.00")
    b.add_column("unit_cost", lambda r: f"={a_cmu}+{a_csd}*NORMSINV(Data!D{r})", expected=cost, fmt="0.00")
    b.add_column("profit", lambda r: f"=Data!F{r}*(Data!G{r}-Data!H{r})-{a_fix}", expected=prof, fmt="#,##0")
    PR = b.rng("profit")
    DEM = b.rng("demand_units")

    b.section("2. The deterministic 'base case' (every input at its average)")
    r_base = b.row("Base-case profit ($)", f"=MIN({b.local(a_mu)},{b.local(a_cap)})*(({b.local(a_plo)}+{b.local(a_phi)})/2-{b.local(a_cmu)})-{b.local(a_fix)}",
                   base, "#,##0", "Looks comfortably positive")

    b.section(f"3. Monte Carlo results ({N:,} trials)")
    b.row("Number of trials", f"=COUNT({PR})", N, "#,##0")
    r_mean = b.row("Expected profit = average of simulated profits ($)", f"=AVERAGE({PR})", float(prof.mean()), "#,##0")
    r_gap = b.row("Expected profit minus base case ($)", f"={b.local(r_mean)}-{b.local(r_base)}", float(prof.mean()) - base, "#,##0",
                  "The 'flaw of averages': the cap makes the model non-linear")
    r_sd = b.row("Standard deviation of profit ($)", f"=STDEV({PR})", float(prof.std(ddof=1)), "#,##0")
    r_se = b.row("Monte Carlo standard error of the mean ($)", f"={b.local(r_sd)}/SQRT(COUNT({PR}))", se_mean, "#,##0")
    r_ci_lo = b.row("95% interval for the expected profit: lower ($)", f"={b.local(r_mean)}-1.96*{b.local(r_se)}", float(prof.mean()) - 1.96 * se_mean, "#,##0")
    r_ci_hi = b.row("95% interval for the expected profit: upper ($)", f"={b.local(r_mean)}+1.96*{b.local(r_se)}", float(prof.mean()) + 1.96 * se_mean, "#,##0")
    r_pl = b.row("Probability of a loss P(profit < 0)", f'=COUNTIF({PR},"<0")/COUNT({PR})', ploss, "0.0%")
    r_se_pl = b.row("Monte Carlo standard error of P(loss)", f"=SQRT({b.local(r_pl)}*(1-{b.local(r_pl)})/COUNT({PR}))",
                    float(np.sqrt(ploss * (1 - ploss) / N)), "0.00%")
    r_pt = b.row("Probability of reaching the profit target", f'=COUNTIF({PR},">="&{b.local(a_tgt)})/COUNT({PR})',
                 float((prof >= TARGET).mean()), "0.0%")
    r_var = b.row("5th percentile of profit = VaR level ($)", f"=PERCENTILE({PR},0.05)", var5, "#,##0", "95% of trials do better than this")
    r_cvar = b.row("Expected profit in the worst 5% of trials ($)", f'=AVERAGEIF({PR},"<="&{b.local(r_var)})', cvar5, "#,##0",
                   "Expected shortfall: how bad it is when it is bad")
    b.row("Worst simulated outcome ($)", f"=MIN({PR})", float(prof.min()), "#,##0")
    b.row("Best simulated outcome ($)", f"=MAX({PR})", float(prof.max()), "#,##0")
    b.row("Share of trials where demand exceeds capacity", f'=COUNTIF({DEM},">"&{b.local(a_cap)})/COUNT({DEM})',
          float((dem > CAP).mean()), "0.0%")
    r_nreq = b.row("Trials needed to know P(loss) within +-1 pp (95%)", f"=ROUNDUP(1.96^2*{b.local(r_pl)}*(1-{b.local(r_pl)})/0.01^2,0)",
                   float(np.ceil(1.96 ** 2 * ploss * (1 - ploss) / 0.01 ** 2)), "#,##0")

    b.section("4. Convergence: results using only the first N trials")
    ks = list(range(100, N + 1, 100))
    rows, exp = [], {}
    t = b.next_row + 1
    for i, k in enumerate(ks):
        rk = f"Data!$I$2:$I${k + 1}"
        rows.append([k, f"=AVERAGE({rk})", f'=COUNTIF({rk},"<0")/COUNT({rk})', f"=PERCENTILE({rk},0.05)",
                     f"=STDEV({rk})/SQRT(COUNT({rk}))"])
        x = prof[:k]
        exp.update({(i, 1): x.mean(), (i, 2): (x < 0).mean(), (i, 3): np.percentile(x, 5), (i, 4): x.std(ddof=1) / np.sqrt(k)})
    c0, c1 = b.table(["Trials N", "Mean profit", "P(loss)", "5th percentile", "SE of mean"], rows,
                     fmt={1: "#,##0", 2: "0.0%", 3: "#,##0", 4: "#,##0"}, expect=exp)
    b.line_chart_from_table("Running mean profit vs number of trials", 1, [2], c0, c1, anchor="H4", x_title="trials", y_title="$")
    b.line_chart_from_table("Running P(loss) vs number of trials", 1, [3], c0, c1, anchor="H24", x_title="trials", y_title="probability")

    b.section("5. Two independent batches of 1000 trials: the noise in a Monte Carlo answer")
    H1, H2 = "Data!$I$2:$I$1001", f"Data!$I$1002:$I${N + 1}"
    rows = [["Trials 1-1000", f"=AVERAGE({H1})", f'=COUNTIF({H1},"<0")/COUNT({H1})', f"=PERCENTILE({H1},0.05)"],
            ["Trials 1001-2000", f"=AVERAGE({H2})", f'=COUNTIF({H2},"<0")/COUNT({H2})', f"=PERCENTILE({H2},0.05)"]]
    exp = {}
    for i, x in enumerate([prof[:1000], prof[1000:]]):
        exp.update({(i, 1): x.mean(), (i, 2): (x < 0).mean(), (i, 3): np.percentile(x, 5)})
    bt0, _ = b.table(["Batch", "Mean profit", "P(loss)", "5th percentile"], rows, fmt={1: "#,##0", 2: "0.0%", 3: "#,##0"}, expect=exp)

    b.section("6. Histogram of simulated profit ($20,000 buckets)")
    lo_e = np.floor(prof.min() / 20000) * 20000
    edges = np.arange(lo_e, prof.max() + 20000, 20000)
    cnt, _ = np.histogram(prof, bins=np.r_[edges, edges[-1] + 20000])
    rows, exp = [], {}
    t = b.next_row + 1
    for i, e in enumerate(edges):
        rr = t + i
        rows.append([f"{int(e / 1000)}k", int(e), f'=COUNTIFS({PR},">="&B{rr},{PR},"<"&B{rr}+20000)'])
        exp[(i, 2)] = float(cnt[i])
    h0, h1 = b.table(["Bucket start", "From ($)", "Trials"], rows, fmt={1: "#,##0", 2: "0"}, expect=exp)
    b.bar_chart_from_table("Distribution of simulated profit", 1, [3], h0, h1, anchor="H44", x_title="profit bucket start ($)", y_title="trials")

    b.answers([
        ("Base-case profit using average inputs", f"={r_base}",
         f"${base:,.0f}: 10,000 units x ($27 - $15) - $90,000. It looks like a safe launch."),
        ("Expected profit from the simulation, and its gap to the base case", f"={r_mean}",
         f"${prof.mean():,.0f}, which is ${base - prof.mean():,.0f} below the base case. Because production is capped at 11,000 units, "
         f"good-demand trials cannot make up for bad-demand ones: a non-linear model's average output is not its output at the average input."),
        ("Probability of a loss", f"={r_pl}",
         f"{ploss:.1%} of the {N:,} trials lost money ({int((prof < 0).sum())} trials) - roughly 1 launch in {1 / ploss:.0f}, hidden by the positive base case."),
        ("5th-percentile profit (VaR level) and expected shortfall", f"={r_var}",
         f"In 95% of trials profit is above -${-var5:,.0f}; in the worst 5% the average outcome is -${-cvar5:,.0f}."),
        ("Probability of reaching the $50,000 target", f"={r_pt}",
         f"{(prof >= TARGET).mean():.1%}: reaching the target is less likely than not."),
        ("Monte Carlo error: standard error and 95% interval for expected profit", f"={r_se}",
         f"SE = ${se_mean:,.0f}; interval [${prof.mean() - 1.96 * se_mean:,.0f}, ${prof.mean() + 1.96 * se_mean:,.0f}]. "
         f"The interval is for the model's expected value; it says nothing about whether the assumptions are right."),
        ("Convergence of the running mean and P(loss)", f"=Analysis!C{c1}",
         f"The running mean goes from ${prof[:100].mean():,.0f} (N=100) to ${prof.mean():,.0f} (N={N}); P(loss) from {(prof[:100] < 0).mean():.0%} to {ploss:.1%}. "
         f"The error shrinks like 1/sqrt(N): 4x the trials halves it."),
        ("Two batches of 1000 trials", f"=Analysis!C{bt0}",
         f"P(loss) {(prof[:1000] < 0).mean():.1%} vs {(prof[1000:] < 0).mean():.1%} and mean ${prof[:1000].mean():,.0f} vs ${prof[1000:].mean():,.0f}: "
         f"same model, different draws, different answers - report the uncertainty of the simulation."),
        ("Trials needed for P(loss) within +-1 pp", f"={r_nreq}",
         f"About {np.ceil(1.96 ** 2 * ploss * (1 - ploss) / 0.01 ** 2):,.0f} trials, more than the {N:,} used. Tail quantiles (1%, 0.1%) need even more."),
        ("Does the launch meet management's rule? Limitations", "text",
         f"No: P(loss) = {ploss:.1%} against a 10% limit, and the 5th percentile is -${-var5:,.0f} against a -$20,000 limit. The result is only as good as the input distributions (normal demand, uniform price, independent inputs are assumptions); "
         "if price and demand were negatively correlated, the risk would differ. With only 2,000 draws the 5th percentile is estimated from 100 trials."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-20-monte-carlo", "20 · Monte Carlo simulation",
             "Profit of a product launch with uncertain demand, price and cost: 2,000 simulated outcomes, risk measures and convergence.")
    d.stat("Profit risk ($)", {"base case": base, "expected profit": prof.mean(), "5th percentile": var5, "worst-5% average": cvar5},
           "The base case ignores variability and the capacity cap; the simulation shows the downside.", unit="currencyUSD", decimals=0,
           w=14, thresholds=[(None, "blue")])
    d.stat("Probabilities", {"P(loss)": ploss, "P(profit >= $50k)": float((prof >= TARGET).mean())},
           "Share of the 2,000 trials.", unit="percentunit", decimals=1, w=10, thresholds=[(None, "blue")])
    step = 20000
    e = np.arange(np.floor(prof.min() / step) * step, prof.max() + step, step)
    neg = prof[prof < 0]
    pos = prof[prof >= 0]
    cn, _ = np.histogram(neg, bins=np.r_[e, e[-1] + step])
    cp, _ = np.histogram(pos, bins=np.r_[e, e[-1] + step])
    hist = pd.DataFrame({"profit_from_$k": [f"{int(a / 1000)}k" for a in e], "loss": np.where(cn > 0, cn, np.nan),
                         "profit": np.where(cp > 0, cp, np.nan)})
    d.bars("Distribution of simulated profit ($20k buckets)", hist, "2,000 trials. The red bars are losing trials.",
           stacking="normal", w=12)
    d.panels[-1]["options"]["showValue"] = "never"
    d.panels[-1]["fieldConfig"]["overrides"] = [
        {"matcher": {"id": "byName", "options": n}, "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": c}}]}
        for n, c in (("loss", "#E15759"), ("profit", "#59A14F"))]
    ns = np.arange(20, N + 1, 20)
    conv = pd.DataFrame({"trials": ns, "running_mean": [prof[:k].mean() for k in ns], "base_case": base,
                         "lower_95": [prof[:k].mean() - 1.96 * prof[:k].std(ddof=1) / np.sqrt(k) for k in ns],
                         "upper_95": [prof[:k].mean() + 1.96 * prof[:k].std(ddof=1) / np.sqrt(k) for k in ns]})
    d.xy("Convergence: running mean profit ($)", conv, "trials", ["running_mean", "lower_95", "upper_95", "base_case"],
         "The running average settles with a shrinking +-1.96 SE band, and settles below the base case.",
         lines=["running_mean", "lower_95", "upper_95", "base_case"], w=12)
    for o in d.panels[-1]["fieldConfig"]["overrides"]:
        if o["matcher"]["options"] in ("lower_95", "upper_95"):
            o["properties"][0]["value"]["fixedColor"] = "#9AA5B1"
        if o["matcher"]["options"] == "base_case":
            o["properties"][0]["value"]["fixedColor"] = "#E15759"
    pl = pd.DataFrame({"trials": ns, "P(loss) %": [(prof[:k] < 0).mean() * 100 for k in ns]})
    d.xy("Convergence: P(loss) in %", pl, "trials", ["P(loss) %"], "Early estimates are noisy; it takes thousands of trials to pin P(loss) down to +-1 pp.",
         lines=["P(loss) %"], w=8)
    sc = pd.DataFrame({"demand": dem[:400], "units_sold": sold[:400]})
    d.xy("Why the average misleads: units sold vs demand (400 trials)", sc, "demand", ["units_sold"],
         "Sales follow demand until the 11,000-unit capacity, then go flat: good luck is capped, bad luck is not.", w=8)
    tab = pd.DataFrame({"measure": ["trials", "expected profit ($)", "std dev ($)", "MC standard error ($)", "P(loss)", "P(profit >= $50k)",
                                    "5th percentile ($)", "worst-5% average ($)", "worst ($)"],
                        "value": [N, prof.mean(), prof.std(ddof=1), se_mean, ploss, float((prof >= TARGET).mean()), var5, cvar5, prof.min()]}).round(3)
    d.table("Simulation output", tab, "Values computed from all 2,000 trials.", w=8)
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: Monte Carlo simulation

## The idea

Many quantities have no formula: the profit of a project whose demand, price and cost are all uncertain; the waiting time in a queue; the
probability that a portfolio loses more than 10 %. **Monte Carlo simulation** replaces the formula by experiment: draw the uncertain inputs from assumed distributions,
push each draw through the model, and study the *distribution of outputs*. It prevents the classic planning error of computing one
"base case" from average inputs and calling it the forecast.

## From uniform numbers to any distribution

All simulation starts from uniform random numbers $U \sim \text{Uniform}(0,1)$. The **inverse transform** turns them into draws from any distribution
with CDF $F$: $X = F^{-1}(U)$.

| input distribution | draw from $u$ | spreadsheet |
|---|---|---|
| Uniform$(a,b)$ | $a + (b-a)u$ | `=a+(b-a)*u` |
| Normal$(\mu,\sigma)$ | $\mu + \sigma\,\Phi^{-1}(u)$ | `=mu+sigma*NORMSINV(u)` |
| Exponential (rate $\lambda$) | $-\ln(1-u)/\lambda$ | `=-LN(1-u)/lambda` |

Spreadsheet `RAND()` gives fresh numbers at every recalculation, so results change when you touch any cell and cannot be checked or shared.
This course **pre-generates** the uniform numbers in `data.csv` (they are inputs like any other data), which makes every answer reproducible. In code you would fix a seed.

## What you estimate

For output $Y = g(X_1,\dots,X_k)$ and $N$ simulated values $y_1,\dots,y_N$:

- expected value: $\bar y = \frac1N\sum y_i$ (law of large numbers), with **Monte Carlo standard error** $s_y/\sqrt N$;
- probability of an event: $\hat p = \#\{y_i \in A\}/N$, with standard error $\sqrt{\hat p(1-\hat p)/N}$ (e.g. $P(\text{loss})$);
- quantiles: the 5th percentile of $y$ is the profit level that 95 % of outcomes beat ("value at risk" at 95 %, usually quoted as a loss);
- **expected shortfall**: the average of the outcomes at or below that quantile - how bad it is when it is bad.

Because the error shrinks like $1/\sqrt N$, ten times more precision needs a hundred times more trials. For a probability near 0.2 the standard error with $N = 2000$ is
$\sqrt{0.2\cdot 0.8/2000} = 0.0089$ (about $\pm 1.8$ pp at 95 %), and $\pm 1$ pp needs $1.96^2 \cdot 0.16 / 0.01^2 \approx 6150$ trials. Tails are worse: a 1 % quantile is decided by 1 % of the trials.

## Worked example: the flaw of averages

Demand is 8000 or 12 000 units with equal probability, capacity is 10 000 units, the margin is \$12 per unit, fixed cost \$90 000.
The base case uses average demand: $\min(10\,000, 10\,000) \times 12 - 90\,000 = +\$30\,000$. The truth: with demand 8000 the profit is $96\,000 - 90\,000 = +6\,000$;
with 12 000 only 10 000 units can be made: $120\,000 - 90\,000 = +30\,000$; the **expected** profit is $\$18\,000$, not \$30 000. Upside is capped, the downside is not, so
$E[g(X)] \ne g(E[X])$ whenever $g$ is non-linear (caps, thresholds, queues, options). Simulation finds the gap automatically; in this lesson's
launch model the expected profit lands about \$6 000 below the base case and roughly 1 launch in 4 loses money, although the base case is positive.

One simulated trial with $u_{demand} = 0.8413$ gives $\Phi^{-1}(0.8413) = 1.000$, so demand $= 10\,000 + 2500 \cdot 1 = 12\,500$ units, capped at 11 000 sold.

## Convergence and checking a simulation

Plot the running mean (or running probability) against $N$: it should flatten inside a shrinking band. Run the experiment twice with different draws: if the answers
differ in a digit you care about, you need more trials. Always report the Monte Carlo standard error next to the estimate, and distinguish it from the *model* uncertainty, which no number of trials can reduce.

## Assumptions and pitfalls

1. **Garbage in, garbage out.** Output distributions inherit every assumption about the input distributions; fit them to data when you can and test sensitivity when you cannot.
2. **Independence.** Drawing demand and price independently ignores that they usually move together; correlated inputs change the risk (often increasing it).
3. **Too few trials**, especially for tail measures; check convergence.
4. **Impossible values**: a normal demand can go negative - truncate it (`MAX(0, ...)`) and say so.
5. **Non-reproducible spreadsheets**: `RAND()` results cannot be audited; freeze the draws.
6. **False precision**: "P(loss) = 23.4 %" from 2000 trials is really "about a quarter".

## Connections

- Percentiles as risk measures: [lesson 3](../03-percentiles-and-extreme-values/theory.md).
- The shrinking error $\sigma/\sqrt N$ is the standard error from [lesson 16](../16-sampling-distributions-and-the-clt/theory.md); the bootstrap in [lesson 17](../17-bootstrapping-and-confidence-intervals/theory.md) is a Monte Carlo experiment on the observed data and [lesson 18](../18-permutation-tests/theory.md) uses random relabelings.
- Simulated future paths give the uncertainty bands of [lesson 25](../25-prediction-intervals-and-forecast-uncertainty/theory.md).
- Repo notes: [standard error and law of large numbers](../../notes/sampling_and_sampling_distributions/standard_error_and_lln.md),
  [normal curve and z-score](../../notes/random_variables_and_distributions/normal_curve_and_z_score.md).
"""

TASK = r"""
# Task: is the product launch safe?

## Scenario

Your company plans a seasonal product launch. The finance sheet says: demand 10 000 units, price \$27, unit cost \$15, fixed launch cost \$90 000, so
**profit = \$30 000** - approve. You suspect the plan ignores uncertainty. Management accepts the launch if the probability of losing money is below
10 % and the 5th-percentile outcome is no worse than a \$20 000 loss. Build a Monte Carlo model and report whether the launch meets the rule.

Model assumptions (provided by the business):

- demand: Normal, mean 10 000, SD 2 500 units (negative values are impossible: use 0);
- the factory can make at most **11 000 units**, so units sold = MIN(demand, capacity);
- selling price: Uniform between \$24 and \$30;
- unit cost: Normal, mean \$15, SD \$1.50;
- fixed launch cost: \$90 000. Profit = units sold x (price - unit cost) - fixed cost.

## Data

`data.csv` - 2 000 trials of pre-generated uniform random numbers (so everyone gets identical results).

| column | meaning |
|---|---|
| `trial` | trial number 1-2000 |
| `u_demand` | uniform(0,1) draw used for demand: `demand = mean + sd * NORMSINV(u)` |
| `u_price` | uniform(0,1) draw used for price: `price = min + (max - min) * u` |
| `u_cost` | uniform(0,1) draw used for unit cost: `cost = mean + sd * NORMSINV(u)` |

## Questions

1. Compute the base-case profit from the average inputs.
2. Turn the draws into demand, units sold, price, unit cost and profit for all 2 000 trials. What is the **expected profit**, and how far is it from the base case? Why?
3. What is the probability of a loss (profit < 0)?
4. What are the 5th percentile of profit and the average profit in the worst 5 % of trials?
5. What is the probability of reaching a profit of \$50 000?
6. Compute the Monte Carlo standard error of the expected profit and a 95 % interval for it.
7. Using only the first 100, 200, ..., 2 000 trials, tabulate the running mean and P(loss). From about which N do they stop moving noticeably?
8. Compare trials 1-1 000 with trials 1 001-2 000 (mean, P(loss), 5th percentile). What does the difference tell you?
9. How many trials would you need to know P(loss) to within +-1 percentage point?
10. *Interpretation:* does the launch meet management's rule? Name two assumptions of the model that could change the answer.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Distribution of simulated profit", what share of the bars is red, and how does that compare with the base case?
- In "Why the average misleads", what happens to units sold as demand rises above 11 000, and why does that pull the average profit below the base case?
- In "Convergence: running mean profit", after how many trials does the running mean stay inside the band, and where is the base case relative to it?

## Deliverable

A one-page risk note with named parts: **Base case vs simulation**, **Risk measures** (P(loss), 5th percentile, expected shortfall), **Precision** (Monte Carlo error),
**Decision** against the management rule and **Assumptions to challenge**. Include the profit histogram.
"""
