# Normal Distribution - Exercises

Read [Normal distribution](../../notes/random_variables_and_distributions/continuous/normal_distribution.md) first.

## Problems

1. For $X\sim N(\mu,\sigma^2)$ find the density at the mean. Evaluate it for $\sigma=2$ and $\sigma=0.1$ and explain why the second value exceeds 1.
2. Use the MGF $M(t)=e^{\mu t+\sigma^2t^2/2}$ to derive $E[X]$ and $E[X^2]$, and hence $\operatorname{Var}(X)$.
3. Test scores are $N(70,10^2)$. Find the percentile of a score of 85, and the score at the 25th percentile.
4. Scores in course X are $N(70,10^2)$ and in course Y are $N(65,8^2)$, independent. Find $P(X>Y)$ for a random student from each.
5. A sample of $n=25$ items from $N(70,10^2)$ is averaged. What is the distribution of $\bar X$ and $P(\bar X>73)$?
6. Show that for $X\sim N(\mu,\sigma^2)$, $P(|X-\mu|<1.96\sigma)\approx0.95$ by writing it with $\Phi$, and explain how it relates to the empirical rule's "95%".
7. Let $X\sim\text{Binomial}(100,0.5)$. Approximate $P(X\le45)$ with a normal distribution using a continuity correction, and compare with the exact value.
8. If $X\sim N(\mu,\sigma^2)$ and $Y=aX+b$ with $a<0$, state the distribution of $Y$ and show $P(Y\le y)$ in terms of $\Phi$.

## Solutions

### 1.
At $x=\mu$ the exponent is 0: $f(\mu)=\dfrac{1}{\sigma\sqrt{2\pi}}\approx\dfrac{0.3989}{\sigma}$.
$\sigma=2$: $0.3989/2=0.1995$. $\sigma=0.1$: $0.3989/0.1=3.989$.
Density is probability per unit length. A very narrow distribution packs probability 1 into a short interval, so the density can exceed 1 even though areas never do. The density at the mean exceeds 1 whenever $\sigma<0.3989$.

### 2.
$M'(t)=(\mu+\sigma^2t)M(t)\Rightarrow E[X]=M'(0)=\mu$.
$M''(t)=\sigma^2M(t)+(\mu+\sigma^2t)^2M(t)\Rightarrow E[X^2]=\sigma^2+\mu^2$.
$\operatorname{Var}(X)=\sigma^2+\mu^2-\mu^2=\sigma^2$.

### 3.
$z=\dfrac{85-70}{10}=1.5$, $\Phi(1.5)=0.9332$: the 93rd percentile.
25th percentile: $z=-0.6745$, score $=70-6.745=63.26$.

### 4.
$D=X-Y$ is normal with mean $70-65=5$ and variance $10^2+8^2=164$ (independent, so variances add), sd $=12.806$.
$P(D>0)=1-\Phi\!\left(\dfrac{0-5}{12.806}\right)=\Phi(0.390)=0.652$.

### 5.
$\bar X\sim N\!\left(70,\ \tfrac{10^2}{25}\right)=N(70,2^2)$.
$z=\dfrac{73-70}{2}=1.5$, so $P(\bar X>73)=1-0.9332=0.0668$.

### 6.
$P(|X-\mu|<1.96\sigma)=P(-1.96<Z<1.96)=\Phi(1.96)-\Phi(-1.96)=0.9750-0.0250=0.9500$.
The empirical rule's "$\pm2\sigma$ contains 95%" is the rounded version: $P(|Z|<2)=0.9545$.

### 7.
Mean $np=50$, variance $np(1-p)=25$, sd 5.
Continuity correction: $P(X\le45)\approx P(Y\le45.5)$, $z=\dfrac{45.5-50}{5}=-0.9$, $\Phi(-0.9)=0.1841$.
Exact binomial: $0.1841$ (to four digits, $0.18410$ vs $0.18406$). The approximation is excellent here because $p=0.5$ and $n=100$.

### 8.
$Y\sim N(a\mu+b,\ a^2\sigma^2)$.
$P(Y\le y)=P(aX+b\le y)=P\!\left(X\ge\dfrac{y-b}{a}\right)$ (the inequality flips since $a<0$)
$=1-\Phi\!\left(\dfrac{(y-b)/a-\mu}{\sigma}\right)=\Phi\!\left(\dfrac{y-(a\mu+b)}{|a|\sigma}\right)$, using $\Phi(-z)=1-\Phi(z)$ and $|a|=-a$.
