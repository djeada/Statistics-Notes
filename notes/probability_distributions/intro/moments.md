## Moments, Moment‐Generating Functions, and Their Connections

In both statistics and mechanics the word *moment* measures how much "leverage" the values of a quantity exert about a chosen reference point.  In statistics the leverage is exerted by probability mass, in mechanics by physical mass, but the mathematics is identical: take a distance from the reference point, square or otherwise power it, weight it, and sum or integrate.

### Statistical moments

For a real‐valued random variable $X$ with mean $\mu = E[X]$, the **$n$th raw moment** is $\mu'_n = E[X^{n}]$.  The **$n$th central moment** shifts the origin to the mean so that only the *shape* of the distribution enters:

$$
\mu_n = E[(X-\mu)^{n}].
$$

The first central moment is always zero.  The second central moment, $\mu_2$, is the familiar **variance** $\sigma^{2} = E[(X-\mu)^2]$; its square root is the standard deviation.  Higher‐order central moments refine the description: the third captures skewness (asymmetry) and the fourth describes kurtosis (tail weight).

### The moment–generating function (MGF)

Whenever $E[e^{tX}]$ exists in an open interval around $t = 0$, we may define the **moment–generating function**

$$
M_X(t) = E[e^{tX}].
$$

Expanding $e^{tX}$ as a power series and exchanging expectation with the series term‐by‐term shows that $M_X$ collects every raw moment:

$$
M_X(t) = 1 + \mu'_1 t + \frac{\mu'_2}{2!}t^2 + \cdots.
$$

Consequently

$$
\mu'_n = M_X^{(n)}(0) = \left.\frac{d^{n}}{dt^{n}}M_X(t)\right|_{t=0}.
$$

The mean is the first derivative at zero, and the variance is the second derivative minus the square of the first:

$$
E[X] = M_X^{\,(1)}(0),\quad
Var(X) = M_X^{\,(2)}(0) - \bigl(M_X^{\,(1)}(0)\bigr)^2.
$$

Because differentiation is often easier than direct integration, the MGF is a powerful computational shortcut; it also uniquely determines the distribution whenever it exists in a neighbourhood of the origin.

### Mechanical moments: the moment of inertia

In classical mechanics the **moment of inertia** of a body about a fixed axis measures its resistance to rotational acceleration.  For a continuous body with density $\rho(\mathbf r)$ the moment of inertia about the axis is

$$
I = \int r^{2} \, dm = \int r^{2}\, \rho(\mathbf r)\, dV,
$$

where $r$ is the perpendicular distance from the axis.  For a system of point masses the integral reduces to the sum $I = \sum_i m_i r_i^{2}$.

### Variance and moment of inertia: a shared formula

Both variance and moment of inertia are weighted sums of squared distances.  Replace mass $m_i$ with probability weight $1/N$ and the distance to the axis with the deviation from the mean, and the formulas coincide.  This is why early statisticians, led by Karl Pearson, borrowed the mechanical term *moment* to describe sums of powered deviations in probability theory.

### Principal‑component analysis (PCA) as a "rotational" problem

Principal‑component analysis diagonalises the covariance matrix

$$
\Sigma_{jk} = E\bigl[(X_j-\mu_j)(X_k-\mu_k)\bigr],
$$

thereby finding orthogonal directions in which the variance—and hence the statistical moment of inertia—is extremal.  In mechanics the same eigen‑problem arises when one seeks the axes about which a rigid body’s physical moment of inertia is minimal or maximal.  PCA is thus the statistical analogue of aligning a rigid body with its principal axes.

### Historical remarks

Pafnuty Chebyshev and his students used powered deviations in probabilistic inequalities during the 1860s–1880s but did not employ the term *moment*.  Karl Pearson introduced that name in an 1893 *Nature* letter and, in 1901, formalised the **method of moments** for parameter estimation by equating sample moments with their theoretical counterparts.  The unifying physics analogy he invoked remains the standard intuition today.
