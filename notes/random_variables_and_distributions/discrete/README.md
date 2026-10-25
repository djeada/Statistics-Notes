# Discrete Distributions

A discrete distribution assigns positive probability masses to a finite or countably infinite set of possible values. The families here model integer counts, but their experiment structures differ. State what is fixed in advance, what ends the experiment, and what the recorded number counts before choosing a formula.

| Modeling question | Distribution | Variable used in these notes |
|---|---|---|
| How many successes occur in $n$ independent trials with a common success probability? | [Binomial](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/discrete/binomial_distribution.md) | Success count from 0 through $n$ |
| How many trials are needed for the first success? | [Geometric](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/discrete/geometric_distribution.md) | Total trials, starting at 1 |
| How many trials are needed for the $r$-th success? | [Negative binomial](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/discrete/negative_binomial_distribution.md) | Total trials, starting at $r$ |
| How many events occur in a specified exposure under a constant-rate Poisson process? | [Poisson](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/discrete/poisson_distribution.md) | Event count, starting at 0 |

## Connections between the models

Geometric waiting is the $r=1$ negative binomial case. Waiting for $r$ successes adds $r$ independent first-success waits under the Bernoulli assumptions. A Poisson distribution instead arises as a limit of binomial counts when trials become numerous and individually rare while $np$ stays fixed.

“Success” is only a label. A defect can be counted as a success without changing the experimental structure. Relabeling the event changes its probability from $p$ to $1-p$, so the parameter must change with the label.

## Counts, thresholds, and conventions

“More than 3” excludes the count 3, whereas “at least 3” includes it. A CDF difference must respect this endpoint mass. Likewise, software that counts failures before a success uses a shifted variable: subtract 1 from a geometric total-trial wait, or $r$ from a negative binomial total-trial wait. Shifting changes the mean and event thresholds but leaves variance unchanged.

For Poisson counts, the parameter is the expected count over the stated exposure. If an arrival rate is given per hour, multiply it by the number of hours before calculating the count probabilities.
