# Gamma Distribution

The gamma family models positive quantities with flexible right-skewed shapes. Write $X\sim\operatorname{Gamma}(\alpha,\beta)$, where $\alpha>0$ is the **shape** and $\beta>0$ is the **rate**. This note uses a rate, not a scale; the corresponding scale is $\theta=1/\beta$.

For an integer shape $\alpha=k$, one construction is a sum of $k$ independent exponential waits with rate $\beta$. It is therefore the wait to the $k$-th event of a constant-rate Poisson process, also called an Erlang distribution. Noninteger shapes define valid gamma distributions too, but do not literally count a fractional number of events.

## Density and shape

The density is

$$
f(x;\alpha,\beta)=\frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x},
\qquad x>0.
$$

It is zero for negative $x$. The gamma function normalizes the shape:

$$
\Gamma(\alpha)=\int_0^\infty u^{\alpha-1}e^{-u}\,du.
$$

Substituting $u=\beta x$ verifies that the density integrates to 1. When $\alpha=1$, the power of $x$ disappears and the model reduces to an exponential distribution. Shapes above 1 have an interior peak; shapes below 1 concentrate density near zero. A high or unbounded density there does not assign positive probability to the exact value zero.

![Gamma densities showing changes in shape and positive support](https://github.com/user-attachments/assets/a438d0a3-850e-4727-a1bb-ba3e7e3b8179)

## Cumulative distribution function

The CDF is

$$
F(x;\alpha,\beta)=\frac{1}{\Gamma(\alpha)}
\int_0^{\beta x}u^{\alpha-1}e^{-u}\,du,\qquad x\ge0.
$$

Below zero it is zero. The general expression uses the regularized incomplete gamma function; it is not simply the density evaluated at the threshold. Integer shapes have a finite-sum expression:

$$
F(x;k,\beta)=1-e^{-\beta x}\sum_{j=0}^{k-1}\frac{(\beta x)^j}{j!}.
$$

The complement says that waiting beyond $x$ means fewer than $k$ Poisson events have arrived by $x$.

![Gamma CDFs accumulating probability over positive waiting times](https://github.com/user-attachments/assets/d624e0d1-1080-4619-8917-e975254c7b03)

## Mean, variance, and MGF

With an integer shape, adding the independent exponential means and variances gives $k/\beta$ and $k/\beta^2$. The same moment formulas hold for every positive real shape:

$$
E[X]=\frac{\alpha}{\beta},\qquad
\operatorname{Var}(X)=\frac{\alpha}{\beta^2}.
$$

For a fixed shape, doubling the rate halves the mean and divides the variance by four. This is why substituting a scale for a rate changes the answer substantially.

Multiplying the density by $e^{tx}$ replaces its exponential decay rate $\beta$ with $\beta-t$. Comparing the resulting integral with the gamma normalization gives

$$
M_X(t)=\left(1-\frac{t}{\beta}\right)^{-\alpha},\qquad t<\beta.
$$

Differentiation at zero recovers the mean. The second raw moment is $\alpha(\alpha+1)/\beta^2$; subtracting the squared mean recovers the variance. In software using scale, set `scale = 1 / beta` while keeping the same shape.

## Example: modeled intervals between floods

Suppose a hydrologist models positive flood intervals in years by a gamma distribution with shape $\alpha=2$ and rate $\beta=1/3$ per year. This is an assumed interval distribution, not a consequence of knowing the average interval alone.

### Average interval

$$
E[X]=\frac{2}{1/3}=6\text{ years}.
$$

### Variance of the interval

$$
\operatorname{Var}(X)=\frac{2}{(1/3)^2}=18\text{ years}^2.
$$

The standard deviation is $\sqrt{18}\approx4.24$ years. The squared units distinguish variance from an ordinary time interval.

For this integer shape, $F(x)=1-e^{-x/3}(1+x/3)$. At the mean of 6 years it gives $F(6)=1-3e^{-2}\approx0.5940$, illustrating that the mean is not generally the median of a skewed distribution.

If the flood arrivals themselves formed a constant-rate Poisson process, ordinary consecutive-event waits would be exponential. The integer-shape gamma construction instead describes a wait across several such events. A gamma model for single flood intervals therefore needs its own empirical or physical justification.

## Applications

Gamma models are used for positive waiting times, accumulated durations, hydrological quantities, and some survival or financial-duration models. Their usefulness depends on the shape and mechanism of the quantity studied; positivity alone does not select a gamma family over other positive distributions.

**Practice:** [Exercises with worked solutions](https://github.com/djeada/Statistics-Notes/blob/main/exercises/random_variables_and_distributions/gamma_distribution.md)
