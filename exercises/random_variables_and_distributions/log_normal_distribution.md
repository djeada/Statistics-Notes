# Log-Normal Distribution - Exercises

Read [Log-normal distribution](../../notes/random_variables_and_distributions/continuous/log_normal_distribution.md) first. $\mu,\sigma$ are the mean and sd of $\ln X$.

## Problems

1. For $\ln X\sim N(0,0.1^2)$ find $E[X]$ and $\operatorname{Var}(X)$ (the note's stock-price example).
2. For $\mu=0,\sigma=1$ find $P(X>2)$.
3. For $\mu=2,\sigma=0.5$ find the median, mean and mode, and order them.
4. For $\mu=1,\sigma=0.8$ find $P(X<5)$.
5. Use the normal MGF to derive $E[X]=e^{\mu+\sigma^2/2}$.
6. A positive quantity has mean 10 and variance 20. Find the log-normal $\mu$ and $\sigma$ by moment matching.
7. $X_1\sim LN(1,0.3^2)$ and $X_2\sim LN(0.5,0.4^2)$ are independent. Find the distribution of $X_1X_2$ and its median.
8. Conceptual: why does multiplying many small independent positive random effects lead to a log-normal rather than a normal shape?

## Solutions

### 1.
$E[X]=e^{0+0.01/2}=e^{0.005}=1.00501$.
$\operatorname{Var}(X)=(e^{0.01}-1)e^{0.01}=(0.010050)(1.010050)=0.01015\approx0.0102$.

### 2.
$P(X>2)=P(\ln X>\ln2)=P(Z>0.693)=1-\Phi(0.69)=1-0.7549=0.2451$ (exact $0.2441$).

### 3.
Median $=e^\mu=e^2=7.389$.
Mean $=e^{\mu+\sigma^2/2}=e^{2.125}=8.373$.
Mode $=e^{\mu-\sigma^2}=e^{1.75}=5.755$.
Order: mode $<$ median $<$ mean (right-skewed).

### 4.
$z=\dfrac{\ln5-1}{0.8}=\dfrac{1.6094-1}{0.8}=0.762$. $\Phi(0.76)=0.7764$ (exact $0.7769$).

### 5.
$\ln X=Y\sim N(\mu,\sigma^2)$, $X=e^Y$, so $E[X]=E[e^{1\cdot Y}]=M_Y(1)=e^{\mu\cdot1+\sigma^2\cdot1^2/2}=e^{\mu+\sigma^2/2}$.
Similarly $E[X^2]=M_Y(2)=e^{2\mu+2\sigma^2}$, so $\operatorname{Var}=e^{2\mu+2\sigma^2}-e^{2\mu+\sigma^2}=(e^{\sigma^2}-1)e^{2\mu+\sigma^2}$.

### 6.
$\dfrac{\text{var}}{m^2}=e^{\sigma^2}-1\Rightarrow\sigma^2=\ln\!\left(1+\dfrac{20}{100}\right)=\ln1.2=0.1823$, $\sigma=0.427$.
$\mu=\ln m-\tfrac{\sigma^2}2=\ln10-0.0912=2.3026-0.0912=2.2114$.

### 7.
$\ln(X_1X_2)=\ln X_1+\ln X_2$ is a sum of independent normals: mean $1+0.5=1.5$, variance $0.09+0.16=0.25$.
So $X_1X_2\sim LN(1.5,0.5^2)$ with median $e^{1.5}=4.482$.

### 8.
$\ln$ turns a product into a sum, and the central limit theorem makes a sum of many small independent terms approximately normal, so $\ln X$ is approximately normal and $X$ is log-normal. Sums of effects give normal shapes; products of effects give log-normal shapes (right-skewed, positive).
