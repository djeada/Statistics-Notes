# Beta Distribution

The beta distribution models a continuously varying quantity confined to the unit interval, such as an uncertain probability or an underlying proportion. Write $X\sim\operatorname{Beta}(\alpha,\beta)$, where both shape parameters are positive. Unlike a normal model, it assigns no probability outside the permitted range.

Its shape is flexible. Equal parameters give symmetry about $1/2$; two parameters greater than 1 give an interior peak; a parameter below 1 can concentrate density near the corresponding endpoint. When $\alpha=\beta=1$, the distribution is uniform on $[0,1]$. These are density shapes, not point probabilities at 0 or 1: a beta variable has zero probability of equaling either endpoint exactly.

## Density and normalization

The density on the interior is

$$
f(x;\alpha,\beta)=\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)},
\qquad 0<x<1.
$$

It is zero outside the unit interval. The denominator is the area under the unnormalized shape:

$$
B(\alpha,\beta)=\int_0^1 u^{\alpha-1}(1-u)^{\beta-1}\,du
=\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}.
$$

Dividing by this constant makes the total density integrate to 1. For parameters below 1 the density can grow without bound near an endpoint, but its integral is still finite. The value assigned to the density at the endpoint itself does not change any probability.

![Beta densities illustrating different shapes on the unit interval](https://github.com/user-attachments/assets/55124c97-5633-4356-a807-13f1c0369034)

## Cumulative probabilities

The CDF accumulates density from the lower boundary to the threshold:

$$
F(x;\alpha,\beta)=\frac{1}{B(\alpha,\beta)}
\int_0^x u^{\alpha-1}(1-u)^{\beta-1}\,du,
\qquad 0\le x\le1.
$$

Below 0 it is zero; above 1 it is one. The general calculation uses the regularized incomplete beta function, although particular parameter choices have elementary formulas. For an interval, subtract CDF values: $P(a<X<b)=F(b)-F(a)$ when $0\le a<b\le1$.

![Beta CDFs accumulating the density over the unit interval](https://github.com/user-attachments/assets/8fec2c6f-a124-4254-8f2b-0b0d9e7a9555)

## Mean, variance, and the role of the parameters

Multiplying the density by $x$ raises the first exponent by one. Consequently, $E[X]=B(\alpha+1,\beta)/B(\alpha,\beta)$, which simplifies to

$$
E[X]=\frac{\alpha}{\alpha+\beta}.
$$

Likewise, $E[X^2]=\alpha(\alpha+1)/[(\alpha+\beta)(\alpha+\beta+1)]$. Subtracting the squared mean gives

$$
\operatorname{Var}(X)=
\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}.
$$

The ratio of the parameters sets the mean, while their total controls concentration around that mean. With $m=\alpha/(\alpha+\beta)$ and $\kappa=\alpha+\beta$, the variance is $m(1-m)/(\kappa+1)$. Increasing both parameters proportionally keeps the mean fixed and reduces spread.

## Example: manufacturing defect proportions

Suppose an underlying defect proportion varies between manufacturing batches, or is uncertain before a batch is examined, and is modeled by $X\sim\operatorname{Beta}(2,5)$.

### Expected underlying proportion

$$
E[X]=\frac2{2+5}\approx0.2857.
$$

The model's average underlying proportion is about 28.57%.

### Variance of the underlying proportion

$$
\operatorname{Var}(X)=\frac{2\times5}{(2+5)^2(2+5+1)}
=\frac{10}{392}\approx0.0255.
$$

An observed fraction of defects in a finite sample is not itself continuously distributed: it takes values such as $0/n,1/n,\ldots,n/n$. Conditional on a particular underlying proportion, a binomial count can describe independent sampled outcomes. The beta model here describes the underlying proportion, keeping that uncertainty separate from finite-sample counting variation.

## Other intervals and applications

For a bounded quantity on $[a,b]$ with $a<b$, use $Y=a+(b-a)X$. Its mean is $a+(b-a)E[X]$, and its variance is $(b-a)^2\operatorname{Var}(X)$. Rescaling the variable must therefore rescale the moments as well.

Beta models are used for probabilities and proportions in Bayesian analysis, reliability, genetics, and ecology. Shifted and scaled beta families also appear in project-duration models such as PERT. In each use, identify whether the random quantity is an underlying continuous rate or an observed finite count.

**Practice:** [Exercises with worked solutions](https://github.com/djeada/Statistics-Notes/blob/main/exercises/random_variables_and_distributions/beta_distribution.md)
