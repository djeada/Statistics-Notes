# Beta Distribution - Exercises

Read [Beta distribution](../../notes/random_variables_and_distributions/continuous/beta_distribution.md) first.

## Problems

1. For $X\sim\text{Beta}(2,5)$ find the mean, variance and mode.
2. Show that $\text{Beta}(1,1)$ is the uniform distribution on $[0,1]$.
3. Write the density of $\text{Beta}(2,3)$ using $B(2,3)=\Gamma(2)\Gamma(3)/\Gamma(5)$ and verify it integrates to 1.
4. For $\text{Beta}(2,2)$ the CDF is $3x^2-2x^3$. Find $P(X<0.5)$ and $P(0.25<X<0.75)$.
5. A prior for a conversion rate is $\text{Beta}(2,2)$. After 7 successes in 10 trials find the posterior and its mean.
6. A proportion has mean 0.3 and variance 0.01. Find the beta parameters by moment matching.
7. For $\text{Beta}(2,1)$ with density $2x$ find $P(X>0.5)$ and check the mean and variance formulas by direct integration.
8. Conceptual: sketch (or describe) the shapes of $\text{Beta}(0.5,0.5)$, $\text{Beta}(1,1)$, $\text{Beta}(5,5)$ and $\text{Beta}(5,1)$.

## Solutions

### 1.
$E[X]=\tfrac{2}{7}=0.2857$.
$\operatorname{Var}(X)=\dfrac{2\cdot5}{7^2\cdot8}=\dfrac{10}{392}=0.02551$.
Mode $=\dfrac{\alpha-1}{\alpha+\beta-2}=\dfrac{1}{5}=0.2$ (valid for $\alpha,\beta>1$).

### 2.
$B(1,1)=\Gamma(1)\Gamma(1)/\Gamma(2)=1$, so $f(x)=x^0(1-x)^0/1=1$ on $[0,1]$, the Uniform(0,1) density.

### 3.
$B(2,3)=\dfrac{1!\,2!}{4!}=\dfrac{2}{24}=\tfrac1{12}$. So $f(x)=12x(1-x)^2$.
$\int_0^1x(1-2x+x^2)dx=\tfrac12-\tfrac23+\tfrac14=\tfrac{6-8+3}{12}=\tfrac1{12}$, and $12\cdot\tfrac1{12}=1$.

### 4.
$F(0.5)=3(0.25)-2(0.125)=0.75-0.25=0.5$ (as expected by symmetry).
$F(0.75)=3(0.5625)-2(0.421875)=1.6875-0.84375=0.84375$.
$F(0.25)=3(0.0625)-2(0.015625)=0.1875-0.03125=0.15625$.
$P(0.25<X<0.75)=0.84375-0.15625=0.6875$.

### 5.
Conjugacy: posterior $=\text{Beta}(\alpha+\text{successes},\beta+\text{failures})=\text{Beta}(2+7,2+3)=\text{Beta}(9,5)$.
Posterior mean $=\tfrac{9}{14}=0.6429$ (prior mean was $0.5$; the sample proportion is $0.7$).

### 6.
$\alpha+\beta=\dfrac{m(1-m)}{v}-1=\dfrac{0.3(0.7)}{0.01}-1=21-1=20$.
$\alpha=m(\alpha+\beta)=6$, $\beta=14$.
Check: $\operatorname{Var}=\dfrac{6\cdot14}{20^2\cdot21}=\dfrac{84}{8400}=0.01$.

### 7.
$P(X>0.5)=\int_{0.5}^12x\,dx=1-0.25=0.75$.
$E[X]=\int_0^12x^2dx=\tfrac23$; formula $\tfrac{2}{3}$.
$E[X^2]=\int_0^12x^3dx=\tfrac12$; $\operatorname{Var}=\tfrac12-\tfrac49=\tfrac1{18}$; formula $\dfrac{2\cdot1}{9\cdot4}=\tfrac1{18}$.

### 8.
$\text{Beta}(0.5,0.5)$: U-shaped with mass piling at 0 and 1 (density diverges at both ends). $\text{Beta}(1,1)$: flat. $\text{Beta}(5,5)$: symmetric bell with mode 0.5. $\text{Beta}(5,1)$: increasing density $5x^4$, concentrated near 1 (mean $5/6$).
