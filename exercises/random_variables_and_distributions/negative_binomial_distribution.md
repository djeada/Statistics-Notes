# Negative Binomial Distribution - Exercises

Read [Negative binomial distribution](../../notes/random_variables_and_distributions/discrete/negative_binomial_distribution.md) first. $X$ is the trial number of the $r$-th success; $X\in\{r,r+1,\dots\}$.

## Problems

1. $X\sim\text{NegBinomial}(r=3,p=0.4)$. Find $P(X=7)$.
2. Find $E[X]$ and $\operatorname{Var}(X)$ for $r=3$, $p=0.4$.
3. Find $P(X\le5)$ for $r=3$, $p=0.4$ directly from the pmf.
4. Check the answer to problem 3 using the identity $P(X\le k)=P(\text{Binomial}(k,p)\ge r)$ and explain why it holds.
5. Show that $X$ is a sum of $r$ independent Geometric($p$) variables and use this to obtain the mean and variance.
6. `scipy.stats.nbinom(r, p)` counts failures $Y=X-r$. Express $P(X=7)$ for $r=3,p=0.4$ in these terms and give $E[Y]$.
7. A factory inspects items with defect probability 0.1 until 5 defectives are found. Find $P(X=20)$ (the note's example) and the mean and standard deviation of the number inspected.
8. A basketball player makes each shot with probability 0.7 independently. Find the probability that her 4th made shot occurs exactly on her 6th attempt, and the expected number of attempts needed.

## Solutions

### 1.
$P(X=7)=\binom{6}{2}(0.4)^3(0.6)^4=15(0.064)(0.1296)=0.1244$.
(The 7th trial is a success, and exactly 2 of the first 6 are successes.)

### 2.
$E[X]=\dfrac rp=\dfrac{3}{0.4}=7.5$.
$\operatorname{Var}(X)=\dfrac{r(1-p)}{p^2}=\dfrac{3(0.6)}{0.16}=\dfrac{1.8}{0.16}=11.25$.

### 3.
$P(X=3)=\binom22(0.4)^3=0.064$.
$P(X=4)=\binom32(0.4)^3(0.6)=3(0.064)(0.6)=0.1152$.
$P(X=5)=\binom42(0.4)^3(0.6)^2=6(0.064)(0.36)=0.13824$.
$P(X\le5)=0.064+0.1152+0.13824=0.31744$.

### 4.
$X\le5$ iff at least 3 successes occur in the first 5 trials. With $B\sim\text{Binomial}(5,0.4)$:
$P(B=3)=10(0.064)(0.36)=0.2304$, $P(B=4)=5(0.0256)(0.6)=0.0768$, $P(B=5)=0.01024$.
Sum $=0.2304+0.0768+0.01024=0.31744$, matching problem 3.

### 5.
Let $G_i$ be the number of trials from the $(i-1)$-th success to the $i$-th. By the independence of trials these are i.i.d. Geometric($p$), and $X=G_1+\dots+G_r$.
$E[X]=r\cdot\tfrac1p$ and $\operatorname{Var}(X)=r\cdot\tfrac{1-p}{p^2}$ (variances of independent summands add). For $r=1$ this is the geometric distribution.

### 6.
$X=7\iff Y=4$ failures: $P(Y=4)=\binom{4+3-1}{4}(0.4)^3(0.6)^4=\binom64(0.064)(0.1296)=15(0.064)(0.1296)=0.1244$. Same number.
$E[Y]=E[X]-r=7.5-3=4.5=\dfrac{r(1-p)}{p}=\dfrac{3(0.6)}{0.4}$.
In code: `nbinom.pmf(4, 3, 0.4)`.

### 7.
$P(X=20)=\binom{19}{4}(0.1)^5(0.9)^{15}=3876(10^{-5})(0.20589)=0.00798\approx0.0080$.
$E[X]=\tfrac50.1=50$; $\operatorname{Var}(X)=\tfrac{5(0.9)}{0.01}=450$; $\text{SD}=\sqrt{450}=21.2$.

### 8.
$r=4$, $p=0.7$, exactly 6 attempts: $\binom{5}{3}(0.7)^4(0.3)^2=10(0.2401)(0.09)=0.2161$.
$E[X]=\tfrac{4}{0.7}=5.714$ attempts.
