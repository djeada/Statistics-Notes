# Sampling Distributions Exercises

Read the note first: [Sampling Distributions](../../notes/sampling_and_sampling_distributions/sampling_distributions.md). Solutions are at the end of this file.

## Problems

1. A normal population has $\mu=50$ and $\sigma=10$. For samples of size $n=25$, give the mean and standard error of $\bar X$ and compute $P(\bar X>52)$.
2. The estimator $\hat\sigma^2=\frac1n\sum(X_i-\bar X)^2$ satisfies $E[\hat\sigma^2]=\frac{n-1}{n}\sigma^2$. For $n=10$ and $\sigma^2=25$, find its bias. How would you remove the bias?
3. Estimator $T_1$ is unbiased with variance $4$. Estimator $T_2$ has bias $0.5$ and variance $1$. Compare their mean squared errors ($\mathrm{MSE}=\mathrm{Var}+\mathrm{Bias}^2$).
4. In a population $40\%$ have a trait. For a sample of $n=100$, find the mean and standard error of the sample proportion $\hat p$ and approximate $P(\hat p>0.5)$.
5. A population takes values $1,2,3$ with equal probability. List the sampling distribution of $\bar X$ for samples of size $n=2$ drawn with replacement, then verify $E[\bar X]=\mu$ and $\operatorname{Var}(\bar X)=\sigma^2/n$.
6. Now draw $n=2$ without replacement from $\{1,2,3,4\}$. Enumerate the six samples, find $\operatorname{Var}(\bar X)$ and compare with $\sigma^2/n$ and with $\frac{\sigma^2}{n}\cdot\frac{N-n}{N-1}$.
7. A skewed population is sampled with $n=2$ and with $n=200$. Which features of the sampling distribution of $\bar X$ change with $n$, and which stay the same? Does the histogram of one observed sample have to look like the sampling distribution?
8. For a normal population with $\sigma^2=4$ and $n=11$, find $E[S^2]$, $\operatorname{Var}(S^2)$ and $P(S^2>6)$. (Use $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$.)
9. Describe a simulation that approximates the standard error of the sample median for a given population model.

## Solutions

**1.** $E[\bar X]=50$, $SE=10/\sqrt{25}=2$. Because the population is normal, $\bar X\sim N(50,2^2)$ exactly. $z=(52-50)/2=1$, so $P(\bar X>52)=1-\Phi(1)=0.1587$.

**2.** $E[\hat\sigma^2]=\frac{9}{10}\cdot25=22.5$, so $\operatorname{Bias}=22.5-25=-2.5$ (it underestimates). Multiplying by $n/(n-1)$ gives the unbiased sample variance $S^2=\frac1{n-1}\sum(X_i-\bar X)^2$.

**3.** $\mathrm{MSE}(T_1)=4+0=4$. $\mathrm{MSE}(T_2)=1+0.5^2=1.25$. The biased estimator has far smaller MSE, illustrating that unbiasedness alone does not make an estimator better.

**4.** $E[\hat p]=0.4$, $SE=\sqrt{0.4\cdot0.6/100}=\sqrt{0.0024}=0.0490$. $z=(0.5-0.4)/0.0490=2.04$, $P(\hat p>0.5)\approx1-\Phi(2.04)=0.0206$ (normal approximation, no continuity correction).

**5.** The 9 equally likely ordered samples give means: $1$ (once: $(1,1)$), $1.5$ (twice), $2$ (three times), $2.5$ (twice), $3$ (once). So $P(\bar X=1,1.5,2,2.5,3)=\tfrac19,\tfrac29,\tfrac39,\tfrac29,\tfrac19$.
$E[\bar X]=\frac{1+3+6+5+3}{9}=2=\mu$. $E[\bar X^2]=\frac{1+4.5+12+12.5+9}{9}=\frac{39}{9}$, so $\operatorname{Var}=\frac{39}{9}-4=\frac{3}{9}=\frac13$. Population: $\mu=2$, $\sigma^2=\frac{(1+0+1)}{3}=\frac23$, and $\sigma^2/n=\frac13$. ✓

**6.** Population: $\mu=2.5$, $\sigma^2=\frac{2.25+0.25+0.25+2.25}{4}=1.25$. Sample means: $(1,2)\to1.5$, $(1,3)\to2$, $(1,4)\to2.5$, $(2,3)\to2.5$, $(2,4)\to3$, $(3,4)\to3.5$. Mean of the means $=15/6=2.5$. Squared deviations: $1,0.25,0,0,0.25,1$, sum $2.5$, so $\operatorname{Var}(\bar X)=2.5/6=0.4167$. Compare: $\sigma^2/n=0.625$; with correction $0.625\cdot\frac{4-2}{4-1}=0.625\cdot\frac23=0.4167$ ✓. Sampling without replacement from a finite population reduces the variance.

**7.** The location ($E[\bar X]=\mu$) stays the same. The spread ($\sigma/\sqrt n$) shrinks with $n$, and the shape moves toward normal (CLT): visibly skewed for $n=2$, nearly symmetric for $n=200$. A histogram of one sample estimates the population distribution (which does not change with $n$ and stays skewed); it is not the sampling distribution of $\bar X$.

**8.** $E[S^2]=\sigma^2=4$. $\operatorname{Var}(S^2)=\frac{2\sigma^4}{n-1}=\frac{2\cdot16}{10}=3.2$ (SD $1.79$). For $P(S^2>6)$: $(n-1)S^2/\sigma^2=10\cdot6/4=15$, so $P=P(\chi^2_{10}>15)\approx0.132$.

**9.** Choose a population model (e.g. $N(0,1)$ or an estimated distribution). Repeat $B$ times (say $B=10{,}000$): draw a sample of size $n$, compute its median. The standard deviation of the $B$ medians approximates $SE(\text{median})$; their histogram approximates the sampling distribution. (For $N(0,1)$ this is close to $1.253/\sqrt n$.)
