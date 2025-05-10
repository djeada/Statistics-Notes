## Moments, Moment‐Generating Functions, and Their Connections

In both statistics and mechanics the word *moment* measures how much "leverage" the values of a quantity exert about a chosen reference point.  In statistics the leverage is exerted by probability mass, in mechanics by physical mass, but the mathematics is identical: take a distance from the reference point, square or otherwise power it, weight it, and sum or integrate.

### Statistical moments

For a real‐valued random variable $X$ with mean $\mu = E[X]$, the **nth raw moment** is $\mu'_n = E[X^{n}]$.  The **$n$th central moment** shifts the origin to the mean so that only the *shape* of the distribution enters:

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
\mu_n' = M_X^{(n)}(0) = \frac{d^n M_X(t)}{dt^n}\big|_{t=0}
$$

The mean is the first derivative at zero, and the variance is the second derivative minus the square of the first:

$$
E[X] = M_X^{\,(1)}(0)
$$

$$
Var(X) = M_X^{\,(2)}(0) - \bigl(M_X^{\,(1)}(0)\bigr)^2
$$

Because differentiation is often easier than direct integration, the MGF is a powerful computational shortcut; it also uniquely determines the distribution whenever it exists in a neighbourhood of the origin.

![output](https://github.com/user-attachments/assets/feda891e-146f-4372-84f3-a54469641239)

**What the figure shows**

* **Solid curve** – the exact MGF $M_X(t)=\lambda/(\lambda-t)$ for an exponential with rate $\lambda=1$ (valid for $t<\lambda=1$).
* **Dots** – Monte-Carlo estimates $\hat M(t)=\frac1N\sum_{i=1}^N e^{tX_i}$ from $N=10{,}000$ simulated draws.

Because $\hat M(t)$ is an unbiased estimator of $M_X(t)$, the scatter hugs the curve; sampling noise widens a bit as $t\uparrow1$ where the variance of $e^{tX}$ blows up.  Zooming near $t=0$ (not shown) the slope of the curve equals the mean $E[X]=1$, its curvature gives $E[X^2]=2$, and so on—illustrating how successive derivatives at $t=0$ generate the raw moments.

### Mechanical moments: the moment of inertia

In classical mechanics the **moment of inertia** of a body about a fixed axis measures its resistance to rotational acceleration.  For a continuous body with density $\rho(\mathbf r)$ the moment of inertia about the axis is

$$
I = \int r^{2} \, dm = \int r^{2}\, \rho(\mathbf r)\, dV,
$$

where $r$ is the perpendicular distance from the axis.  For a system of point masses the integral reduces to the sum $I = \sum_i m_i r_i^{2}$.

### Variance and moment of inertia: a shared formula

Both variance and moment of inertia are weighted sums of squared distances.  Replace mass $m_i$ with probability weight $1/N$ and the distance to the axis with the deviation from the mean, and the formulas coincide.  This is why early statisticians, led by Karl Pearson, borrowed the mechanical term *moment* to describe sums of powered deviations in probability theory.

![output(1)](https://github.com/user-attachments/assets/43ebb827-73a6-42af-bb6f-070143c5db6f)

* **Points** – a cloud of 200 synthetic observations drawn from a bivariate normal distribution (mean ≈ (2, −1), isotropic unit variance).
* **× symbol** – the sample mean $\hat\mu$.
* **Dashed circles** – one and two “standard-deviation radii,” where

$$
\sigma_r = \sqrt{\tfrac1n\sum_{i=1}^n\|X_i-\hat\mu\|^2}
$$

They play the same geometric role that $\sigma$ does on a 1-D number line.

Squaring the radial distances and averaging (then halving in physics) gives the **statistical moment of inertia**—identical in algebra to the physical moment of inertia but with probability mass instead of physical mass.  Visually, you can see that most points fall within the $1\sigma$ circle, and the spread of the cloud determines the circle’s radius.

### Principal‑component analysis (PCA) as a "rotational" problem

Principal‑component analysis diagonalises the covariance matrix

$$
\Sigma_{jk} = E\bigl[(X_j-\mu_j)(X_k-\mu_k)\bigr]
$$

thereby finding orthogonal directions in which the variance—and hence the statistical moment of inertia—is extremal.  In mechanics the same eigen‑problem arises when one seeks the axes about which a rigid body’s physical moment of inertia is minimal or maximal.  PCA is thus the statistical analogue of aligning a rigid body with its principal axes.

![output(2)](https://github.com/user-attachments/assets/e370fc52-664e-4e3e-9c7d-d2bfb7d78f66)

* **Crosses** – 300 correlated points drawn from a 2-D normal distribution with unequal variances.
* **Black arrows** – the principal-component directions (eigenvectors of the sample covariance matrix) emanating from the sample mean.
* **Labels** – the eigenvalues $\lambda_1 \approx 3.36$ and $\lambda_2 \approx 0.28$, i.e. the variances captured along each axis.

The long arrow shows where variance—and thus the statistical moment of inertia—is greatest; the short arrow shows the direction of minimal variance.  Conceptually, PCA has “rotated” the coordinate system to align with these axes, mirroring how a rigid body is aligned with its principal axes of rotation to reveal its physical moments of inertia.

### Historical remarks

Pafnuty Chebyshev and his students used powered deviations in probabilistic inequalities during the 1860s–1880s but did not employ the term *moment*.  Karl Pearson introduced that name in an 1893 *Nature* letter and, in 1901, formalised the **method of moments** for parameter estimation by equating sample moments with their theoretical counterparts.  The unifying physics analogy he invoked remains the standard intuition today.
