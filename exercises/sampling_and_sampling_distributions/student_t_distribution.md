# Student's t Distribution Exercises

Read the note first: [Student's t Distribution](../../notes/sampling_and_sampling_distributions/student_t_distribution.md). Solutions are at the end of this file.

## Problems

1. A sample of $n=16$ has $\bar x=52$ and $s=8$. Test $H_0:\mu=50$ (two-sided, $5\%$) and give a $95\%$ confidence interval. Use $t_{0.975}(15)=2.131$.
2. Diet A: $n_1=20$, mean $120$, $s_1=8$. Diet B: $n_2=25$, mean $130$, $s_2=10$. Compute the Welch $t$ statistic and Welch-Satterthwaite degrees of freedom.
3. Find $\operatorname{Var}(T)$ for $\nu=5$. What happens for $\nu=2$ and $\nu=1$?
4. For $\nu=5$, $P(T>2)=0.0510$. Compare with the normal value $P(Z>2)$, and compare $t_{0.975}(5)=2.571$ with $1.96$. Explain the difference.
5. $Z=1.2$ and $V=7.5$ are independent draws from $N(0,1)$ and $\chi^2(5)$. Compute $T=Z/\sqrt{V/5}$ and its distribution.
6. Six paired differences (after minus before) are $2,3,-1,4,1,3$. Test $H_0:\mu_d=0$ at $5\%$ and compute a $95\%$ CI ($t_{0.975}(5)=2.571$).
7. Two groups of $n=10$ have means $5.2$ and $4.1$ and SDs $1.5$ and $1.7$. Perform the pooled-variance $t$ test ($df=18$, critical value $2.101$).
8. List $t_{0.975}(\nu)$ for $\nu=2,10,30,\infty$ ($4.303$, $2.228$, $2.042$, $1.960$). What does the pattern say about using $z$ instead of $t$?

## Solutions

**1.** $SE=8/\sqrt{16}=2$, $t=(52-50)/2=1.0$ on $15$ df. $|t|<2.131$ so do not reject (two-sided p-value $0.333$). CI: $52\pm2.131\cdot2=(47.74,\,56.26)$, which contains $50$.

**2.** $s_1^2/n_1=64/20=3.2$, $s_2^2/n_2=100/25=4.0$, sum $7.2$, $SE=\sqrt{7.2}=2.683$. $t=(120-130)/2.683=-3.73$. Degrees of freedom: $\dfrac{7.2^2}{\frac{3.2^2}{19}+\frac{4^2}{24}}=\dfrac{51.84}{0.5389+0.6667}=\dfrac{51.84}{1.2056}=43.0$. Two-sided p-value $\approx0.0006$.

**3.** $\operatorname{Var}=\nu/(\nu-2)=5/3=1.667$ for $\nu=5$. For $\nu=2$ the variance is infinite ($1<\nu\le2$). For $\nu=1$ (Cauchy) the mean does not exist and the variance is undefined.

**4.** $P(Z>2)=0.0228$, less than half of $0.0510$. The critical value $2.571$ exceeds $1.96$. The $t$ distribution has heavier tails because the estimated standard deviation adds extra variability; intervals and tests must be wider/more conservative to keep the same error rate.

**5.** $T=1.2/\sqrt{7.5/5}=1.2/\sqrt{1.5}=1.2/1.2247=0.980$, and $T\sim t(5)$.

**6.** $\bar d=12/6=2$. Deviations: $0,1,-3,2,-1,1$; squares sum $0+1+9+4+1+1=16$; $s=\sqrt{16/5}=1.789$. $SE=1.789/\sqrt6=0.730$. $t=2/0.730=2.74$ on $5$ df; $2.74>2.571$, reject (p-value $0.041$). CI: $2\pm2.571\cdot0.730=(0.12,\,3.88)$.

**7.** $s_p^2=\frac{9(2.25)+9(2.89)}{18}=2.57$. $SE=\sqrt{2.57(1/10+1/10)}=\sqrt{0.514}=0.717$. $t=1.1/0.717=1.53$. Since $1.53<2.101$ (p-value $0.142$), do not reject.

**8.** The critical value falls from $4.30$ to $1.96$ as $\nu$ grows; for $\nu\ge30$ it is within about $4\%$ of $z$. Using $z$ for small samples understates uncertainty (too-narrow intervals), whereas for large samples the difference is negligible.
