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
