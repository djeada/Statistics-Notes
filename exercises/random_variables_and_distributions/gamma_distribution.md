# Gamma Distribution - Exercises

Read [Gamma distribution](../../notes/random_variables_and_distributions/continuous/gamma_distribution.md) first. Parametrization: shape $\alpha$ and **rate** $\beta$ (scale $=1/\beta$).

## Problems

1. $X\sim\text{Gamma}(\alpha=3,\beta=2)$. Find the mean, variance and standard deviation.
2. Show that $\text{Gamma}(1,\beta)$ is the exponential distribution and find its density.
3. For $\text{Gamma}(2,\beta=0.5)$ find $P(X>4)$ using the Poisson-sum identity for integer shape.
4. Show the identity used in problem 3: for integer $\alpha$, $P(X>x)=e^{-\beta x}\sum_{k=0}^{\alpha-1}\frac{(\beta x)^k}{k!}$, for $\alpha=2$ by integration by parts.
5. Derive $E[X]=\alpha/\beta$ from the gamma integral $\int_0^\infty x^{s-1}e^{-\beta x}dx=\Gamma(s)/\beta^s$.
6. Three independent exponential waiting times each have rate $1/4$ per day. Identify the distribution of their sum, with mean and variance.
7. Flood intervals are $\text{Gamma}(2,\beta=1/3)$ per year. Find the probability that an interval exceeds 9 years.
8. A positive variable has mean 10 and variance 20. Find the gamma parameters by matching moments, and write the corresponding scipy call.

## Solutions

### 1.
$E[X]=\tfrac\alpha\beta=\tfrac32=1.5$. $\operatorname{Var}(X)=\tfrac{\alpha}{\beta^2}=\tfrac34=0.75$. $\text{SD}=0.866$.

### 2.
$f(x;1,\beta)=\dfrac{\beta^1}{\Gamma(1)}x^{0}e^{-\beta x}=\beta e^{-\beta x}$ since $\Gamma(1)=1$. This is the Exp($\beta$) density.

### 3.
$\alpha=2$, $\beta x=0.5\cdot4=2$:
$P(X>4)=e^{-2}\left(1+2\right)=3e^{-2}=3(0.13534)=0.4060$.

### 4.
$P(X>x)=\int_x^\infty\beta^2te^{-\beta t}dt$ (since $\Gamma(2)=1$). By parts: $=\big[-\beta te^{-\beta t}\big]_x^\infty+\int_x^\infty\beta e^{-\beta t}dt=\beta xe^{-\beta x}+e^{-\beta x}=e^{-\beta x}(1+\beta x)$, which equals the sum with $k=0,1$.

### 5.
$E[X]=\dfrac{\beta^\alpha}{\Gamma(\alpha)}\int_0^\infty x^{\alpha}e^{-\beta x}dx=\dfrac{\beta^\alpha}{\Gamma(\alpha)}\cdot\dfrac{\Gamma(\alpha+1)}{\beta^{\alpha+1}}=\dfrac{\alpha\Gamma(\alpha)}{\beta\Gamma(\alpha)}=\dfrac\alpha\beta$.

### 6.
The MGF of each is $\left(1-\tfrac{t}{1/4}\right)^{-1}$; the product of three is $\left(1-4t\right)^{-3}$, the MGF of $\text{Gamma}(\alpha=3,\beta=\tfrac14)$.
Mean $=\tfrac{3}{1/4}=12$ days; variance $=\tfrac{3}{(1/4)^2}=48$ days$^2$.

### 7.
$\beta x=\tfrac13\cdot9=3$, $\alpha=2$: $P(X>9)=e^{-3}(1+3)=4e^{-3}=4(0.049787)=0.1991$.

### 8.
Mean $=\alpha/\beta=10$, variance $=\alpha/\beta^2=20$. Dividing: $\tfrac{\text{var}}{\text{mean}}=\tfrac1\beta=2\Rightarrow\beta=0.5$, then $\alpha=10\beta=5$.
In scipy: `scipy.stats.gamma(a=5, scale=2)` (scale $=1/\beta=2$).
