# Normal (Gaussian) Distribution

The normal distribution is a symmetric continuous model with a center and a scale. Write $X\sim\mathcal N(\mu,\sigma^2)$, where $\mu$ is the mean and $\sigma>0$ is the standard deviation. Increasing $\mu$ shifts the distribution; increasing $\sigma$ spreads its probability over a wider range.

Its support is the entire real line. Extremely distant values have small probability, but there is no finite boundary. This makes the normal useful for approximately symmetric measurements and for suitable approximations to standardized sums, while also limiting its suitability for inherently bounded or strongly skewed observations.

## Density and probability

The density is

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}
e^{-(x-\mu)^2/(2\sigma^2)}.
$$

The exponent depends on the squared distance from $\mu$ in standard-deviation units, giving symmetry about the mean. The normalizing factor ensures that the area is 1 as the width changes. A narrower curve is taller because its probability occupies a smaller horizontal range.

![Normal densities with a symmetric bell shape](https://github.com/user-attachments/assets/92c0b044-9b2d-4755-b14d-8e7d9068691c)

Probabilities are areas under this curve. In particular, $P(X=x)=0$ for any exact value; the density height $f(x)$ is not that point probability.

## CDF and standardization

Standardizing gives $Z=(X-\mu)/\sigma\sim\mathcal N(0,1)$. Thus every normal CDF can be calculated from the standard normal CDF $\Phi$:

$$
F(x)=\Phi\left(\frac{x-\mu}{\sigma}\right)
=\frac12\left[1+\operatorname{erf}\left(\frac{x-\mu}{\sigma\sqrt2}\right)\right].
$$

The error function is another way to express the same integral; it does not mean the probability equals the density formula. For an interval, standardize both endpoints and subtract their left-tail probabilities.

![Normal CDF increasing most rapidly near the center](https://github.com/user-attachments/assets/7963d182-5904-4849-9c17-698b2d5982ee)

## Why the expected value is the center

The mean is obtained by weighting each value by its density:

$$
E[X]=\int_{-\infty}^{\infty}x f(x)\,dx
=\int_{-\infty}^{\infty}x\frac{1}{\sigma\sqrt{2\pi}}
e^{-(x-\mu)^2/(2\sigma^2)}\,dx.
$$

Let $u=(x-\mu)/(\sqrt2\sigma)$. Then $x=\mu+\sqrt2\sigma u$ and $dx=\sqrt2\sigma\,du$, giving

$$
E[X]=\frac1{\sqrt\pi}\int_{-\infty}^{\infty}
(\mu+\sqrt2\sigma u)e^{-u^2}\,du.
$$

Split the constant and centered parts:

$$
E[X]=\frac{\mu}{\sqrt\pi}\int_{-\infty}^{\infty}e^{-u^2}\,du
+\frac{\sqrt2\sigma}{\sqrt\pi}\int_{-\infty}^{\infty}u e^{-u^2}\,du.
$$

The first integral is $\sqrt\pi$. The second is zero: $u e^{-u^2}$ is odd, so its negative and positive contributions cancel over the symmetric domain. Therefore

$$
E[X]=\mu.
$$

This calculation formalizes the symmetry argument. For the normal distribution, the mean, median, and density's mode all coincide at $\mu$.

## Variance, MGF, and moments

The variance and standard deviation are

$$
\operatorname{Var}(X)=\sigma^2,\qquad \operatorname{SD}(X)=\sigma.
$$

Completing the square in $tx-(x-\mu)^2/(2\sigma^2)$ produces a shifted normal density times a constant. Integrating the density leaves the MGF

$$
M_X(t)=E[e^{tX}]=e^{\mu t+\sigma^2t^2/2},\qquad t\in\mathbb R.
$$

The general derivative rule is

$$
E[X^n]=\frac{d^nM_X(t)}{dt^n}\Bigg|_{t=0}.
$$

Since $M'_X(t)=(\mu+\sigma^2t)M_X(t)$, the first two raw moments are

$$
E[X]=\mu,\qquad E[X^2]=\sigma^2+\mu^2.
$$

The second raw moment measures squared distance from zero. Subtracting $\mu^2$ changes the reference point to the mean and gives the variance.

## The 68–95–99.7 rule

For a normal variable, about 68% of the probability lies within one standard deviation of the mean, 95% within two, and 99.7% within three. The more precise values are 68.27%, 95.45%, and 99.73%.

These are probability statements under the normal model, not exact percentages that every finite sample must contain. A central interval with 95% probability uses about $\mu\pm1.96\sigma$, whereas $\mu\pm2\sigma$ contains about 95.45%.

## Example: standardizing test scores

Suppose scores are modeled as normal with mean 70 and standard deviation 10. For a score of 85,

$$
z=\frac{X-\mu}{\sigma},\qquad
z=\frac{85-70}{10}=1.5.
$$

The score is 1.5 standard deviations above the mean. Its model percentile comes from $\Phi(1.5)\approx0.9332$, placing it near the 93rd percentile. That is a distribution-based comparison, not an exact rank among a particular finite class.

The probability of a score above 85 is the complementary upper tail, $1-\Phi(1.5)\approx0.0668$. Standardization preserves order: larger raw scores have larger z-scores because the divisor $\sigma$ is positive.

## Applications and interpretation

The normal family is used for some measurements and errors and as an approximation to sampling distributions under suitable central-limit conditions. A sum becoming approximately normal does not make each summand normal. Likewise, a normally shaped histogram does not by itself establish independence or justify every normal-theory inference procedure. For bounded scores, the normal is an approximation whose usefulness depends on how much probability it assigns beyond the feasible range.

**Practice:** [Exercises with worked solutions](https://github.com/djeada/Statistics-Notes/blob/main/exercises/random_variables_and_distributions/normal_distribution.md)
