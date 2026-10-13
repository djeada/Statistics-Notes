# Null and Alternative Hypotheses: Exercises

These problems accompany the note **[Null and Alternative Hypotheses](../../notes/hypothesis_testing_and_confidence_intervals/null_hypothesis.md)**. Worked solutions are in the [Solutions](#solutions) section; numerical answers were checked in Python (see `scripts/hypothesis_testing_and_confidence_intervals/null_hypothesis.py`).

## Problems

**1. Marble bags.** Bag A has 5 white and 5 black marbles; Bag B has only black. You draw with replacement and test $H_0$: "Bag A".
(a) What is the p-value if $n=4$ draws are all black?
(b) What is the smallest $n$ giving $p\le0.05$? And $p\le0.01$?

**2. Exact binomial test (two-sided).** A coin lands heads 9 times in 10 tosses. Test $H_0:p=0.5$ against $H_a:p\ne0.5$. Give the p-value and decision at $\alpha=0.05$.

**3. Exact binomial test (one-sided).** In a taste test, 15 of 20 people prefer product X. Test $H_0:p=0.5$ against $H_a:p>0.5$.

**4. From statistic to p-value.** A $z$ test statistic equals $-1.8$. Give the p-value for a left-tailed, right-tailed, and two-tailed test.

**5. Critical values.** Give the standard-normal critical values for (a) two-sided $\alpha=0.05$, (b) two-sided $\alpha=0.01$, (c) right-tailed $\alpha=0.05$, (d) right-tailed $\alpha=0.01$.

**6. Language.** A researcher obtains $p=0.30$ and writes "we have proved the drug has no effect." Rewrite the conclusion correctly and explain the error.

**7. Misinterpretation check.** A test of $H_0:\mu=50$ gives $p=0.04$. Is it correct to say the probability that $H_0$ is true is $0.04$? What does $0.04$ mean?

**8. Tests and intervals.** A two-sided 95% confidence interval for a mean difference is $(0.4,\ 3.1)$. What does this imply for the test of $H_0:\mu_1-\mu_2=0$ at $\alpha=0.05$? What if the interval were $(-0.4,\ 3.1)$?

## Solutions

**1.**
(a) Under $H_0$ each draw is black with probability $0.5$, so $p=(0.5)^4=0.0625$.
(b) We need $(0.5)^n\le0.05$. $(0.5)^4=0.0625>0.05$ and $(0.5)^5=0.03125\le0.05$, so $n=5$. For $0.01$: $(0.5)^6=0.0156>0.01$ and $(0.5)^7=0.0078\le0.01$, so $n=7$.

**2.** $P(X\ge9)=P(9)+P(10)=\frac{10+1}{1024}=0.01074$. By symmetry the two-sided p-value is

$$
2(0.01074)=0.0215.
$$

Since $0.0215<0.05$, reject $H_0$: there is evidence the coin is not fair.

**3.** $P(X\ge15)=\sum_{k=15}^{20}\binom{20}{k}(0.5)^{20}=\frac{15504+4845+1140+190+20+1}{1{,}048{,}576}=\frac{21700}{1{,}048{,}576}=0.0207$. Since $0.0207<0.05$, reject $H_0$: there is evidence that more than half prefer X.

**4.**
Left-tailed: $P(Z\le-1.8)=0.0359$.
Right-tailed: $P(Z\ge-1.8)=1-0.0359=0.9641$.
Two-tailed: $2(0.0359)=0.0719$.

**5.**
(a) $1.960$. (b) $2.576$. (c) $1.645$. (d) $2.326$.
Two-sided tests split $\alpha$ between tails, so use $z_{1-\alpha/2}$; one-sided tests use $z_{1-\alpha}$.

**6.** A p-value of $0.30$ means data like these would not be unusual if the drug had no effect. We "fail to reject $H_0$"; there is insufficient evidence of an effect. It does not show that the effect is zero, because a small study may simply lack power, and the data may be equally compatible with a modest real effect.

**7.** No. The p-value is $P(\text{data this extreme or more}\mid H_0)$, not $P(H_0\mid\text{data})$. Here, if $\mu=50$ were true, about 4% of samples would give a test statistic at least as extreme as the one observed. Computing $P(H_0\mid\text{data})$ requires a prior, which is outside the frequentist test.

**8.** The interval $(0.4,3.1)$ excludes $0$, so the two-sided test rejects $H_0$ at $\alpha=0.05$. The interval $(-0.4,3.1)$ contains $0$, so $H_0$ is not rejected. This duality holds for standard two-sided tests and their matching intervals.
