# F Distribution Exercises

Read the note first: [F Distribution](../../notes/sampling_and_sampling_distributions/f_distribution.md). Solutions are at the end of this file.

## Problems

1. Independent $U\sim\chi^2(6)$ and $V\sim\chi^2(12)$ take the values $U=15$ and $V=18$. Compute $F=(U/6)/(V/12)$ and state its distribution.
2. Find the mean and variance of $F(5,10)$.
3. Given $F_{0.95}(4,9)=3.633$, find the $5\%$ lower-tail critical value of $F(9,4)$.
4. Wheat variety 1 has $n_1=15$, $s_1^2=20$ and variety 2 has $n_2=12$, $s_2^2=30$. Test $H_0:\sigma_1^2=\sigma_2^2$ two-sided at $5\%$ using $F_{0.025}(14,11)=0.3231$ and $F_{0.975}(14,11)=3.359$.
5. Using the same data, give a $95\%$ confidence interval for $\sigma_1^2/\sigma_2^2$.
6. A one-way ANOVA has $3$ groups of $10$ observations, $SSB=48$ and $SSW=270$. Compute the $F$ statistic and its degrees of freedom, and the p-value (the $5\%$ critical value is $3.354$).
7. A two-sided t-test gives $t=2.5$ with $20$ degrees of freedom. Show that $F=t^2$ has an $F(1,20)$ distribution with the same p-value.
8. Does $F(3,3)$ have a finite mean and variance? What does this mean for large observed values?

## Solutions

**1.** $F=\dfrac{15/6}{18/12}=\dfrac{2.5}{1.5}=1.667$, and $F\sim F(6,12)$ (numerator df $6$, denominator df $12$).

**2.** Mean: $\dfrac{d_2}{d_2-2}=\dfrac{10}{8}=1.25$. Variance: $\dfrac{2d_2^2(d_1+d_2-2)}{d_1(d_2-2)^2(d_2-4)}=\dfrac{2\cdot100\cdot13}{5\cdot64\cdot6}=\dfrac{2600}{1920}=1.354$.

**3.** If $F\sim F(d_1,d_2)$ then $1/F\sim F(d_2,d_1)$. So $P(F(4,9)\le3.633)=0.95$ means $P(F(9,4)\ge1/3.633)=0.95$, i.e. $F_{0.05}(9,4)=1/3.633=0.2752$.

**4.** $F=s_1^2/s_2^2=20/30=0.667$ with $df=(14,11)$. The acceptance region is $[0.3231,3.359]$; $0.667$ lies inside, so do not reject (two-sided p-value $\approx2\times0.235=0.47$). No evidence of a difference in variability.

**5.** $\left(\dfrac{s_1^2/s_2^2}{F_{0.975}(14,11)},\dfrac{s_1^2/s_2^2}{F_{0.025}(14,11)}\right)=\left(\dfrac{0.667}{3.359},\dfrac{0.667}{0.3231}\right)=(0.199,\,2.063)$. It contains $1$, consistent with the test.

**6.** $df_B=3-1=2$, $df_W=30-3=27$. $MSB=48/2=24$, $MSW=270/27=10$, $F=24/10=2.4$ on $F(2,27)$. Since $2.4<3.354$, p-value $\approx0.110$; do not reject equality of the group means at $5\%$.

**7.** $t=Z/\sqrt{V/20}$ with $Z\sim N(0,1)$, so $t^2=Z^2/(V/20)=(Z^2/1)/(V/20)$ with $Z^2\sim\chi^2(1)$ independent of $V\sim\chi^2(20)$: an $F(1,20)$ variable. $F=2.5^2=6.25$ and $P(F(1,20)>6.25)=0.0212$, equal to the two-sided $2P(t_{20}>2.5)=0.0212$. ✓

**8.** $d_2=3$. The mean exists for $d_2>2$ and equals $d_2/(d_2-2)=3$. The variance requires $d_2>4$, so it is infinite for $d_2=3$. Heavy right tail: occasional very large $F$ values occur, and sample variances of $F$ draws do not stabilize.
