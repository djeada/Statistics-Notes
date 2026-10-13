# Point Estimation: Exercises

These problems accompany the note **[Point Estimation](../../notes/estimation/point_estimation.md)**. Try each problem before opening the solution. Worked solutions are in the [Solutions](#solutions) section, and numerical answers were checked with Python (`scripts/estimation/point_estimation.py` covers a related simulation).

## Problems

**1. Estimator or estimate?** A researcher draws $X_1,\ldots,X_{25}$ from a population with mean $\mu$ and computes $\bar X=\frac1{25}\sum X_i$. The observed value is $\bar x=48.2$.
(a) Which of $\bar X$ and $48.2$ is the estimator, and which is the estimate?
(b) Is it meaningful to ask whether $48.2$ is "unbiased"? Explain.

**2. Comparing two unbiased estimators.** Let $X_1,X_2$ be independent with mean $\mu$ and variance $\sigma^2$. Consider $T=\frac13X_1+\frac23X_2$ and $\bar X=\frac12(X_1+X_2)$.
(a) Show that both are unbiased for $\mu$.
(b) Compute both variances and say which is preferable.

**3. Bernoulli MLE.** Out of 20 independent trials, 7 were successes.
(a) Write the log-likelihood and derive $\hat p_{\mathrm{MLE}}$.
(b) Compute the estimate and its estimated standard error.

**4. Exponential rate.** Six waiting times (minutes) from an exponential distribution with rate $\lambda$ are $2.1,\ 0.8,\ 1.5,\ 3.2,\ 0.9,\ 1.3$.
(a) Find the method-of-moments estimate of $\lambda$.
(b) Show that the MLE is the same.
(c) The estimator $1/\bar X$ has $E[1/\bar X]=\frac{n}{n-1}\lambda$. Compute the bias-corrected estimate.

**5. Normal variance: divisor $n$ or $n-1$.** The data $4,\ 7,\ 5,\ 9,\ 6$ come from a normal population.
(a) Compute $\hat\mu$ and the MLE of $\sigma^2$.
(b) Compute the unbiased sample variance $S^2$.
(c) Explain why the two differ and by what factor.

**6. MSE comparison.** For normal data with $n=10$ and $\sigma^2=4$, $\mathrm{Var}(S^2)=\frac{2\sigma^4}{n-1}$. Compare the MSE of $S^2$ with the MSE of the MLE $\hat\sigma^2=\frac{n-1}{n}S^2$.

**7. Uniform$(0,\theta)$.** A sample is $3.1,\ 4.7,\ 2.2,\ 5.9,\ 3.6$ from Uniform$(0,\theta)$.
(a) Find the method-of-moments estimate of $\theta$.
(b) Find the maximum-likelihood estimate of $\theta$.
(c) Comment on what the two estimates reveal about each method.

**8. Poisson mean and precision.** Counts of emails per hour over six hours were $2,\ 0,\ 3,\ 1,\ 4,\ 2$ (Poisson with mean $\lambda$).
(a) Give the MLE of $\lambda$.
(b) Estimate its standard error using $\mathrm{SE}(\bar X)=\sqrt{\lambda/n}$.
(c) Why is an estimate without a standard error incomplete?

## Solutions

**1.**
(a) $\bar X$ is a random variable defined before the data are observed, so it is the estimator. The number $48.2$ is its realized value, the estimate.
(b) No. Bias, $E[\hat\theta]-\theta$, is a property of the estimator's sampling distribution across repeated samples. A single number is not biased or unbiased.

**2.**
(a) $E[T]=\frac13\mu+\frac23\mu=\mu$ and $E[\bar X]=\frac12\mu+\frac12\mu=\mu$. Both are unbiased.
(b)

$$
\mathrm{Var}(T)=\left(\tfrac19+\tfrac49\right)\sigma^2=\tfrac59\sigma^2\approx0.556\,\sigma^2,
\qquad
\mathrm{Var}(\bar X)=\left(\tfrac14+\tfrac14\right)\sigma^2=\tfrac12\sigma^2.
$$

Since $0.5<0.556$, $\bar X$ is preferable: among unbiased estimators of this linear form, equal weights minimize variance.

**3.**
(a) With $S=\sum x_i=7$ and $n=20$,

$$
\ell(p)=S\log p+(n-S)\log(1-p).
$$

Setting the derivative to zero: $\frac{S}{p}-\frac{n-S}{1-p}=0\Rightarrow S(1-p)=(n-S)p\Rightarrow \hat p=\frac{S}{n}$.

(b) $\hat p=7/20=0.35$ and

$$
\widehat{\mathrm{SE}}=\sqrt{\frac{0.35(0.65)}{20}}=\sqrt{0.011375}\approx0.107.
$$

**4.**
(a) $E[X]=1/\lambda$, so set $\bar x=1/\hat\lambda$. The sum is $9.8$, so $\bar x=9.8/6\approx1.633$ and $\hat\lambda_{\mathrm{MoM}}=1/1.633\approx0.612$.
(b) The log-likelihood is $\ell(\lambda)=n\log\lambda-\lambda\sum x_i$. Then $\ell'(\lambda)=n/\lambda-\sum x_i=0$ gives $\hat\lambda=n/\sum x_i=1/\bar x\approx0.612$, the same.
(c) $\frac{n-1}{n}\cdot\frac1{\bar x}=\frac56(0.612)\approx0.510$.

**5.**
(a) $\hat\mu=\bar x=31/5=6.2$. The squared deviations are $4.84,\ 0.64,\ 1.44,\ 7.84,\ 0.04$, with sum $14.8$. So $\hat\sigma^2_{\mathrm{MLE}}=14.8/5=2.96$.
(b) $S^2=14.8/4=3.70$.
(c) The MLE divides by $n$ and $S^2$ divides by $n-1$, so $S^2=\frac{n}{n-1}\hat\sigma^2_{\mathrm{MLE}}=\frac54(2.96)=3.70$. The MLE is biased low because deviations are measured from $\bar x$, which is fitted to the same data and sits closer to the observations than $\mu$ does.

**6.** $S^2$ is unbiased, so

$$
\mathrm{MSE}(S^2)=\mathrm{Var}(S^2)=\frac{2(16)}{9}\approx3.556.
$$

For $\hat\sigma^2=\frac{9}{10}S^2$: the variance is $\left(\frac{9}{10}\right)^2(3.556)=0.81(3.556)=2.88$, and the bias is $-\sigma^2/n=-0.4$. So

$$
\mathrm{MSE}(\hat\sigma^2)=2.88+0.4^2=3.04.
$$

The biased MLE has the smaller MSE ($3.04<3.56$), showing that unbiasedness is not the only criterion.

**7.**
(a) $E[X]=\theta/2$, so $\bar x=\hat\theta/2$. Here $\bar x=19.5/5=3.9$ and $\hat\theta_{\mathrm{MoM}}=7.8$.
(b) The likelihood is $\theta^{-n}$ for $\theta\ge\max x_i$ and zero otherwise, which is decreasing in $\theta$, so the maximum is at the smallest allowed value: $\hat\theta_{\mathrm{MLE}}=\max x_i=5.9$.
(c) The estimates differ a lot. The MoM estimator $2\bar X$ is unbiased but can give values below the sample maximum, which is impossible for $\theta$. The MLE can never fall below the maximum, but it is biased downward ($E[\max]=\frac{n}{n+1}\theta$). For $n=5$ the MSEs are $\theta^2/(3n)=0.0667\theta^2$ for MoM and $\frac{2}{(n+1)(n+2)}\theta^2=0.0476\theta^2$ for the MLE, so the MLE is more efficient despite its bias.

**8.**
(a) For Poisson data, $\hat\lambda_{\mathrm{MLE}}=\bar x=12/6=2$.
(b) $\widehat{\mathrm{SE}}=\sqrt{2/6}=\sqrt{0.3333}\approx0.577$.
(c) A point estimate alone does not show how much it would vary across samples. The same estimate based on $n=6$ or $n=600$ looks identical, but its precision differs by a factor of 10 in standard error.
