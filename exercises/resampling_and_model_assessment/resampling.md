# Resampling and Simulation: Exercises

Read [Simulations in Statistical Inference](../../notes/resampling_and_model_assessment/resampling.md) first. Scripts: [resampling.py](../../scripts/resampling_and_model_assessment/resampling.py), [resampling_linear_regression_slope_estimates.py](../../scripts/resampling_and_model_assessment/resampling_linear_regression_slope_estimates.py).

## Problems

1. A population is normal with $\sigma=15$. What is the exact standard error of the sample mean for $n=30$? The Monte Carlo script with $B=1000$ reported 2.7208; what is the relative difference, and why is it not zero?
2. The sample is $(2,4,6,8)$. Compute the plug-in (bootstrap) standard error of the mean, $\sqrt{\hat\sigma^2_{\text{plug-in}}/n}$, where $\hat\sigma^2_{\text{plug-in}}$ divides by $n$.
3. A bootstrap with $B=2000$ gives $\hat\theta=10$, 2.5th percentile 8.5, 97.5th percentile 13.0, and bootstrap SE 1.2. Give the 95% normal, percentile and pivotal intervals.
4. A sample has $\bar x=50$, $s=10$, $n=16$. Compute the 95% interval with $z$ and with $t$. Which is preferable and why?
5. Data $x=(1,2,3,4)$, $y=(2.1,3.9,6.2,7.8)$. (a) Fit OLS and compute residuals. (b) Perform one residual-resampling replicate that draws residuals $(3,1,4,3)$ (1-based indices) and give $\hat b^*$.
6. Using the same data, compute $\hat b^*$ for one pairs (case) replicate that draws observations $(1,2,2,4)$.
7. Using the same data, compute $\hat b^*$ for one wild-bootstrap replicate with Rademacher multipliers $\eta=(+1,-1,-1,+1)$. Why do the multipliers need mean 0 and variance 1?
8. Which of residual, pairs and wild bootstrap would you choose when the error variance grows with $x$? Why?
9. Show that the probability an original observation is absent from a bootstrap sample tends to $e^{-1}$, and evaluate it for $n=10$.
10. Name two situations in which the ordinary i.i.d. bootstrap is unreliable and say what to do instead.

## Solutions

**1.** $SE=\sigma/\sqrt n=15/\sqrt{30}=2.7386$. Relative difference $=(2.7386-2.7208)/2.7386\approx0.65\%$. The Monte Carlo SE is itself an estimate from $B=1000$ replicates, with relative standard error roughly $1/\sqrt{2(B-1)}\approx2.2\%$, so a difference of this size is expected.

**2.** Deviations from $\bar x=5$: $-3,-1,1,3$; squares $9,1,1,9$; $\hat\sigma^2_{\text{plug-in}}=20/4=5$. $SE_{\text{boot}}=\sqrt{5/4}=1.118$ (the exact value for infinitely many resamples; the usual $s/\sqrt n=\sqrt{(20/3)/4}=1.291$ differs by the $n$ vs $n-1$ divisor).

**3.** Normal: $10\pm1.96\cdot1.2=[7.65,\,12.35]$. Percentile: $[8.5,\,13.0]$. Pivotal: $[2\cdot10-13.0,\;2\cdot10-8.5]=[7.0,\,11.5]$. The bootstrap distribution is right-skewed, so the pivotal interval moves left while the percentile interval extends right.

**4.** $SE=10/\sqrt{16}=2.5$. With $z$: $50\pm1.96\cdot2.5=[45.1,\,54.9]$. With $t_{15,0.975}=2.131$: $50\pm5.33=[44.67,\,55.33]$. The $t$ interval is preferable because $\sigma$ is estimated and $n$ is small; it is wider to compensate.

**5.** (a) $\bar x=2.5$, $\bar y=5$, $S_{xx}=2.25+0.25+0.25+2.25=5$. $S_{xy}=(-1.5)(-2.9)+(-0.5)(-1.1)+(0.5)(1.2)+(1.5)(2.8)=4.35+0.55+0.6+4.2=9.7$. $\hat b=9.7/5=1.94$, $\hat a=5-1.94\cdot2.5=0.15$. Fitted $(2.09,4.03,5.97,7.91)$; residuals $(0.01,-0.13,0.23,-0.11)$, which sum to 0. (b) Drawn residuals $(0.23,0.01,-0.11,0.23)$. Because $\hat b^*=\hat b+\sum(x_i-\bar x)e^*_i/S_{xx}$: $\sum=(-1.5)(0.23)+(-0.5)(0.01)+(0.5)(-0.11)+(1.5)(0.23)=-0.06$, so $\hat b^*=1.94-0.06/5=1.928$.

**6.** Points $(1,2.1),(2,3.9),(2,3.9),(4,7.8)$. $\bar x=2.25$, $\bar y=4.425$, $S_{xx}=1.5625+0.0625+0.0625+3.0625=4.75$. $S_{xy}=(-1.25)(-2.325)+2(-0.25)(-0.525)+(1.75)(3.375)=2.90625+0.2625+5.90625=9.075$. $\hat b^*=9.075/4.75=1.911$.

**7.** $e^*_i=\hat e_i\eta_i=(0.01,0.13,-0.23,-0.11)$. $\sum(x_i-\bar x)e^*_i=(-1.5)(0.01)+(-0.5)(0.13)+(0.5)(-0.23)+(1.5)(-0.11)=-0.36$, so $\hat b^*=1.94-0.36/5=1.868$. Mean 0 keeps the bootstrap errors centred (no induced bias); variance 1 makes $\operatorname{Var}(e^*_i\mid\text{data})=\hat e_i^2$, so each observation keeps its own squared residual as variance, preserving heteroscedasticity.

**8.** Wild or pairs bootstrap. Residual resampling mixes residuals from all $x$ values, so it assigns the same error distribution everywhere and gives wrong variability for $\hat b$ under heteroscedasticity. Wild keeps $\hat e_i$ attached to its $x_i$; pairs resamples whole observations.

**9.** The probability one draw misses a given observation is $1-1/n$; over $n$ independent draws, $(1-1/n)^n\to e^{-1}\approx0.368$. For $n=10$: $0.9^{10}=0.349$. So a bootstrap sample contains about 63% of the distinct observations.

**10.** (i) Dependent data (time series, spatial): resampling single observations destroys dependence; use block or model-based bootstrap. (ii) Extreme-value statistics such as the sample maximum, or very small $n$: the bootstrap distribution is discrete and does not approximate the sampling distribution; use parametric or other methods.
