# Hypothesis Testing: Exercises

These problems accompany the note **[Hypothesis Testing](../../notes/hypothesis_testing_and_confidence_intervals/hypothesis_testing.md)**. Worked solutions are in the [Solutions](#solutions) section, and every number was checked in Python (see `scripts/hypothesis_testing_and_confidence_intervals/t_test.py` and `p_value.py`).

## Problems

**1. Setting up hypotheses.** State $H_0$ and $H_a$ (and whether the test is left-, right-, or two-tailed) for:
(a) A bakery claims loaves weigh 500 g on average; an inspector suspects they are underweight.
(b) A teacher wants to know whether a new curriculum changes the mean score from the historical 72.
(c) A website owner wants evidence that a redesign raises the conversion rate above 4%.

**2. One-sample z-test.** IQ scores in a population have $\sigma=15$. A sample of $n=36$ students has mean $104.5$. Test $H_0:\mu=100$ against $H_a:\mu\ne100$ at $\alpha=0.05$.

**3. One-sample t-test (left-tailed).** A delivery service promises a mean of 10 minutes. In $n=12$ deliveries the mean was $9.2$ minutes with $s=1.5$. Test $H_0:\mu=10$ against $H_a:\mu<10$ at $\alpha=0.05$. ($t_{0.05,11}=-1.796$.)

**4. Two-sample t-test and effect size.** Group 1 ($n_1=15$) has $\bar x_1=52$, $s_1=8$; group 2 ($n_2=15$) has $\bar x_2=47$, $s_2=10$. Assume equal variances.
(a) Test $H_0:\mu_1=\mu_2$ against a two-sided alternative at $\alpha=0.05$ ($t_{0.975,28}=2.048$).
(b) Compute Cohen's $d$.

**5. Paired t-test.** Eight patients' systolic blood pressure dropped by $3,\ 5,\ -1,\ 4,\ 2,\ 6,\ 0,\ 3$ mmHg after treatment (before minus after). Test whether the mean drop is different from zero at $\alpha=0.05$ ($t_{0.975,7}=2.365$).

**6. Two proportions.** In a trial, 45 of 200 users on design A and 30 of 180 on design B clicked. Test $H_0:p_A=p_B$ against the two-sided alternative using the pooled $z$-test.

**7. Statistical versus practical significance.** A study of $n=10{,}000$ finds a sample mean $0.5$ units above $\mu_0$, with $s=10$. Test $H_0:\mu=\mu_0$ two-sided and compute the effect size. Interpret.

**8. Interpretation.** A one-sided test yields $p=0.03$. Which statements are valid?
(a) The probability that $H_0$ is true is $3\%$.
(b) If $H_0$ were true, results at least this extreme would occur about 3% of the time.
(c) The effect must be large.
(d) At $\alpha=0.01$ we would not reject.

## Solutions

**1.**
(a) $H_0:\mu=500$ (or $\mu\ge500$), $H_a:\mu<500$. Left-tailed.
(b) $H_0:\mu=72$, $H_a:\mu\ne72$. Two-tailed.
(c) $H_0:p=0.04$ (or $p\le0.04$), $H_a:p>0.04$. Right-tailed.

**2.** The standard error is $15/\sqrt{36}=2.5$ and

$$
z=\frac{104.5-100}{2.5}=1.80.
$$

The two-sided p-value is $2P(Z\ge1.80)=2(0.0359)=0.0719$. Since $0.0719>0.05$ (equivalently $1.80<1.96$), we fail to reject $H_0$: the data do not provide sufficient evidence at the 5% level that the mean differs from 100.

**3.** $SE=1.5/\sqrt{12}=0.4330$ and

$$
t=\frac{9.2-10}{0.4330}=-1.848,\qquad df=11.
$$

Since $-1.848<-1.796$, we reject $H_0$. The left-tail p-value is $P(T_{11}\le-1.848)\approx0.046$. There is evidence at the 5% level that the mean delivery time is below 10 minutes (the result is borderline).

**4.**
(a) The pooled standard deviation is

$$
s_p=\sqrt{\frac{14(64)+14(100)}{28}}=\sqrt{82}=9.055.
$$

Then $SE=s_p\sqrt{2/15}=9.055(0.3651)=3.307$ and

$$
t=\frac{52-47}{3.307}=1.512,\qquad df=28.
$$

Since $1.512<2.048$, we fail to reject $H_0$ (two-sided $p\approx0.142$).

(b) $d=\dfrac{5}{9.055}=0.552$, a medium effect by convention. The study simply lacks power to detect it with 15 per group.

**5.** The differences have mean $\bar d=22/8=2.75$ and standard deviation $s_d=2.375$. Then $SE=2.375/\sqrt8=0.840$ and

$$
t=\frac{2.75}{0.840}=3.274,\qquad df=7.
$$

Since $3.274>2.365$, we reject $H_0$ (two-sided $p\approx0.014$): the mean change in blood pressure is different from zero.

**6.** $\hat p_A=0.225$, $\hat p_B=0.1667$, pooled $\hat p=75/380=0.1974$. Then

$$
SE=\sqrt{0.1974(0.8026)\left(\tfrac1{200}+\tfrac1{180}\right)}=0.0409,
\qquad
z=\frac{0.225-0.1667}{0.0409}=1.43.
$$

The two-sided p-value is $2P(Z\ge1.43)\approx0.154>0.05$. We fail to reject $H_0$: no convincing evidence that the click rates differ.

**7.** $SE=10/\sqrt{10000}=0.1$, so $t=0.5/0.1=5.0$ with 9,999 degrees of freedom and $p\approx6\times10^{-7}$. Highly significant. But Cohen's $d=0.5/10=0.05$, far below the "small" benchmark of $0.2$. With a huge sample even a trivial shift is statistically significant; whether $0.5$ units matters is a substantive question.

**8.**
(a) Invalid. The p-value is computed assuming $H_0$ and is not the probability that $H_0$ is true.
(b) Valid. This is the definition of a p-value.
(c) Invalid. A small p-value reflects both effect size and sample size.
(d) Valid. Since $0.03>0.01$, we fail to reject at $\alpha=0.01$.
