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
