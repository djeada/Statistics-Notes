# Type I and Type II Errors: Exercises

These problems accompany the note **[Type I and Type II Errors](../../notes/hypothesis_testing_and_confidence_intervals/type_i_and_type_ii_errors.md)**. Worked solutions are in the [Solutions](#solutions) section; numbers were checked in Python (see `scripts/hypothesis_testing_and_confidence_intervals/type_i_and_type_ii_errors.py`).

## Problems

**1. Identify the error.** For each scenario, say whether an error is Type I or Type II.
(a) A spam filter flags a legitimate email as spam ($H_0$: email is legitimate).
(b) A trial fails to detect that a drug works ($H_0$: no effect).
(c) A quality test passes a defective batch ($H_0$: batch is acceptable).

**2. Expected false positives.** A lab runs 1,000 independent tests at $\alpha=0.05$ and all null hypotheses are true. How many rejections are expected? What does this say about interpreting a single "significant" result in such a screen?

**3. Power of a one-sided z-test.** $H_0:\mu=100$ against $H_a:\mu>100$, with $\sigma=15$, $n=36$, $\alpha=0.05$. The true mean is $105$. Compute the rejection threshold for $\bar x$, the power, and $\beta$.

**4. Two-sided power.** Repeat Problem 3 for the two-sided test $H_a:\mu\ne100$ at $\alpha=0.05$ (include the small opposite-tail contribution when computing power).

**5. Effect of $\alpha$.** Repeat Problem 4 with $\alpha=0.01$. What happens to power and why?

**6. Sample size.** Two groups have common $\sigma=10$. How many observations per group are needed to detect a true difference of $\Delta=4$ with a two-sided $\alpha=0.05$ test and power $0.90$?

**7. Increasing power.** List four design choices that raise power and say which carries a cost in Type I error.

**8. Choosing $\alpha$.** For a cancer screening test, argue whether the Type I or the Type II error is more costly and how that should influence the threshold.

## Solutions

**1.**
(a) Type I: rejecting a true $H_0$ (false positive).
(b) Type II: failing to reject a false $H_0$ (false negative).
(c) Type II: the batch is defective ($H_0$ false) but not rejected.

**2.** Expected rejections $=1000(0.05)=50$. With this many tests, around 50 "significant" results appear even when nothing is real, so a single significant result among many tests is weak evidence unless a multiplicity adjustment is used.

**3.** $SE=15/\sqrt{36}=2.5$. Reject when

$$
\bar x>100+1.645(2.5)=104.11.
$$

Under $\mu=105$:

$$
\text{Power}=P\left(Z>\frac{104.11-105}{2.5}\right)=P(Z>-0.355)=0.639,
$$

so $\beta=1-0.639=0.361$.

**4.** The two-sided upper threshold is $100+1.96(2.5)=104.9$. Under $\mu=105$:

$$
P(\bar x>104.9)=P(Z>-0.04)=0.516.
$$

The lower threshold is $95.1$, and $P(\bar x<95.1)=P(Z<-3.96)\approx0.00004$, which is negligible. Power $\approx0.516$ and $\beta\approx0.484$. A two-sided test has less power than the one-sided test (0.639) for an effect in the specified direction.

**5.** The upper threshold is $100+2.576(2.5)=106.44$:

$$
\text{Power}=P\left(Z>\frac{106.44-105}{2.5}\right)=P(Z>0.576)=0.282.
$$

Power falls from $0.516$ to $0.282$ because a stricter $\alpha$ moves the threshold farther from $\mu_0$, making rejection harder even when $H_0$ is false.

**6.**

$$
n=\frac{2\sigma^2(z_{0.975}+z_{0.90})^2}{\Delta^2}
=\frac{2(100)(1.960+1.282)^2}{16}
=\frac{200(10.51)}{16}\approx131.3,
$$

so $n=132$ per group.

**7.** Larger $n$; smaller variability $\sigma$ (better measurement, blocking, pairing); a larger true effect (stronger intervention); a larger $\alpha$ or a one-sided test. Only raising $\alpha$ (and using a one-sided test when the direction was not justified in advance) costs Type I error control. The others carry no Type I cost, though they cost money or time.

**8.** A missed cancer (Type II, false negative) delays treatment and is usually the more severe error, so the screening threshold is set to be sensitive, accepting more false positives, which are followed by confirmatory tests. The right balance depends on the costs of follow-up and the prevalence of the disease.
