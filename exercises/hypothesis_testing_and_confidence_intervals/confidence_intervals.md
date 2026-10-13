# Confidence Intervals: Exercises

These problems accompany the note **[Confidence Intervals](../../notes/hypothesis_testing_and_confidence_intervals/confidence_intervals.md)**. Worked solutions are in the [Solutions](#solutions) section, and all numbers were checked in Python (see `scripts/hypothesis_testing_and_confidence_intervals/confidence_intervals.py` for a coverage simulation).

## Problems

**1. Known $\sigma$.** Exam scores are normally distributed with known $\sigma=9$. A sample of $n=36$ has mean $82$. Construct a 95% confidence interval for $\mu$.

**2. Unknown $\sigma$.** A sample of $n=16$ battery lifetimes has $\bar x=24.3$ hours and $s=3.2$ hours. Construct a 95% confidence interval for the mean lifetime. ($t_{0.975,15}=2.131$.)

**3. Proportion.** In a poll of 800 voters, 312 support a proposal. Construct a 95% interval for the population proportion using the normal approximation.

**4. Sample size for a proportion.** How many voters are needed so that a 95% interval has margin of error at most $0.03$, assuming nothing about $p$ in advance?

**5. Sample size for a mean.** Machine fill weights have $\sigma=15$ g. How many items must be weighed to estimate the mean fill to within $\pm2$ g with 99% confidence?

**6. Interpretation.** A 95% interval for a mean is $(4.1,\ 7.9)$. Decide whether each statement is correct and justify.
(a) There is a 95% probability that $\mu$ lies in $(4.1,7.9)$.
(b) If the procedure were repeated on many random samples, about 95% of the intervals would contain $\mu$.
(c) 95% of individual observations lie between 4.1 and 7.9.
(d) A two-sided test at $\alpha=0.05$ of $H_0:\mu=8$ would reject, while one of $H_0:\mu=5$ would not.

**7. Width.** (a) By what factor must $n$ increase to halve the width of an interval? (b) By what factor does the width change when moving from 90% to 99% confidence with $n$ and $\sigma$ fixed?

**8. Confidence versus prediction.** A sample of $n=25$ has $\bar x=50$ and $s=10$. Compute a 95% confidence interval for the mean and a 95% prediction interval for one new observation. ($t_{0.975,24}=2.064$.)

## Solutions

**1.** $SE=\sigma/\sqrt n=9/6=1.5$. The margin of error is $1.96(1.5)=2.94$, so

$$
82\pm2.94=(79.06,\ 84.94).
$$

**2.** $SE=3.2/\sqrt{16}=0.8$. The margin is $2.131(0.8)=1.705$, so

$$
24.3\pm1.705=(22.59,\ 26.01).
$$

The $t$ critical value is used because $\sigma$ is estimated by $s$.

**3.** $\hat p=312/800=0.39$. $SE=\sqrt{0.39(0.61)/800}=\sqrt{0.00029738}=0.01724$. The margin is $1.96(0.01724)=0.0338$, so

$$
0.39\pm0.0338=(0.356,\ 0.424).
$$

**4.** The margin is $z^*\sqrt{p(1-p)/n}\le0.03$. The worst case is $p=0.5$, where $p(1-p)=0.25$:

$$
n\ge\left(\frac{1.96}{0.03}\right)^2(0.25)=4268.4(0.25)\approx1067.1.
$$

Round up: $n=1068$.

**5.** The margin is $z^*\sigma/\sqrt n\le2$ with $z^*=2.576$:

$$
n\ge\left(\frac{2.576(15)}{2}\right)^2=(19.32)^2\approx373.2,
$$

so $n=374$.

**6.**
(a) Incorrect. After the interval is computed, $\mu$ is either in it or not. The 95% refers to the procedure.
(b) Correct. This is the repeated-sampling meaning of confidence.
(c) Incorrect. A confidence interval is about the mean, not the spread of individual observations; individual values vary much more.
(d) Mostly correct. $8$ lies outside the interval, so $H_0:\mu=8$ would be rejected at the 5% level; $5$ lies inside, so $H_0:\mu=5$ would not be rejected (for the same two-sided $t$ procedure).

**7.**
(a) The width is proportional to $1/\sqrt n$. Halving it needs $\sqrt n$ to double, so $n$ must be multiplied by $4$.
(b) The width is proportional to $z^*$: $2.576/1.645\approx1.566$. The 99% interval is about 57% wider.

**8.** $SE=10/\sqrt{25}=2$. The confidence interval has margin $2.064(2)=4.13$:

$$
50\pm4.13=(45.87,\ 54.13).
$$

For the prediction interval the standard error is $s\sqrt{1+1/n}=10\sqrt{1.04}=10.198$, giving a margin $2.064(10.198)=21.05$:

$$
50\pm21.05=(28.95,\ 71.05).
$$

The prediction interval is far wider because it includes the variability of an individual observation, which does not shrink as $n$ grows.
