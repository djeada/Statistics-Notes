# Chi-Square Distribution Exercises

Read the note first: [Chi-Square Distribution](../../notes/sampling_and_sampling_distributions/chi_square_distribution.md). Solutions are at the end of this file.

## Problems

1. Find the mean, variance and standard deviation of $\chi^2(8)$.
2. Three independent standard normal values are $0.5$, $-1.2$ and $1.5$. Compute $Q=\sum Z_i^2$, state its distribution, and find $P(\chi^2(3)\ge Q)$ given the critical value $\chi^2_{0.95}(3)=7.815$.
3. A die is rolled $120$ times with counts $(25,17,15,23,24,16)$. Test fairness with a chi-square goodness-of-fit test at the $5\%$ level (critical value $11.07$).
4. A $2\times2$ table has counts $\begin{pmatrix}30&20\\20&30\end{pmatrix}$. Test independence at the $5\%$ level (critical value $3.84$).
5. A sample of $n=16$ from a normal population has $s^2=25$. Give a $95\%$ confidence interval for $\sigma^2$ using $\chi^2_{0.975}(15)=27.488$ and $\chi^2_{0.025}(15)=6.262$.
6. Test $H_0:\sigma^2=16$ against $H_1:\sigma^2>16$ at the $5\%$ level for $n=21$, $s^2=25$ (critical value $\chi^2_{0.95}(20)=31.41$).
7. Use the normal approximation $\chi^2(k)\approx N(k,2k)$ to estimate $P(\chi^2(50)>67.5)$. The exact value is $0.0500$ (67.5 is the 95th percentile). Comment.
8. Derive $E[X]$ and $E[X^2]$ for $X\sim\chi^2(k)$ from the MGF $M(t)=(1-2t)^{-k/2}$.
9. If $U\sim\chi^2(3)$ and $V\sim\chi^2(4)$ are independent, what is the distribution, mean and variance of $U+V$?

## Solutions

**1.** $E=k=8$, $\operatorname{Var}=2k=16$, SD $=4$.

**2.** $Q=0.25+1.44+2.25=3.94$, and $Q\sim\chi^2(3)$. Since $3.94<7.815$ it is below the 95th percentile; the tail probability is $P(\chi^2(3)\ge3.94)=0.268$.

**3.** $E=120/6=20$. $\chi^2=\frac{(25-20)^2+(17-20)^2+(15-20)^2+(23-20)^2+(24-20)^2+(16-20)^2}{20}=\frac{25+9+25+9+16+16}{20}=\frac{100}{20}=5.0$, with $df=6-1=5$. Since $5.0<11.07$ (p-value $0.416$), do not reject: no evidence the die is unfair.

**4.** Row and column totals are $50$, grand total $100$, so each expected count is $50\cdot50/100=25$. Each of the four cells deviates by $\pm5$ from its expected count, contributing $5^2/25=1$, so $\chi^2=4\cdot1=4$. With $df=(2-1)(2-1)=1$ and $4>3.84$ (p-value $0.0455$), reject independence at $5\%$.

**5.** $\left(\dfrac{(n-1)s^2}{\chi^2_{0.975}},\dfrac{(n-1)s^2}{\chi^2_{0.025}}\right)=\left(\dfrac{15\cdot25}{27.488},\dfrac{15\cdot25}{6.262}\right)=(13.64,\,59.88)$. The interval is asymmetric because the chi-square is skewed.

**6.** $\chi^2=\dfrac{(n-1)s^2}{\sigma_0^2}=\dfrac{20\cdot25}{16}=31.25$, $df=20$. Since $31.25<31.41$ (p-value $0.052$), do not reject at $5\%$, though it is borderline.

**7.** $z=(67.5-50)/\sqrt{100}=1.75$, $P\approx0.040$. The exact $0.050$ is larger: the chi-square is right-skewed, so the normal approximation underestimates the upper tail even at $k=50$.

**8.** $M'(t)=k(1-2t)^{-k/2-1}$, so $E[X]=M'(0)=k$. $M''(t)=k(k+2)(1-2t)^{-k/2-2}$, so $E[X^2]=M''(0)=k(k+2)=k^2+2k$. Hence $\operatorname{Var}=k^2+2k-k^2=2k$. ✓

**9.** Sums of independent chi-squares add degrees of freedom: $U+V\sim\chi^2(7)$ with mean $7$ and variance $14$ (equals $3+4$ and $6+8$).
