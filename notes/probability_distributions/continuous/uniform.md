## Uniform Distribution

A continuous random variable X follows a uniform distribution over an interval [a, b] if it has a constant probability density over that interval. The uniform distribution is denoted as $X \sim \text{Uniform}(a, b)$.

### Probability Density Function (PDF)

The PDF of a uniform distribution is given by:

$$f(x) =
\begin{cases}
  \frac{1}{b-a}, & \text{if}\ a \le x \le b \\
  0, & \text{otherwise}
\end{cases}
$$

### Cumulative Distribution Function (CDF)

The CDF of a uniform distribution is given by:

$$F(x) =
\begin{cases}
  0, & \text{if}\ x < a \\
  \frac{x-a}{b-a}, & \text{if}\ a \le x \le b \\
  1, & \text{if}\ x > b
\end{cases}
$$

### Expected Value and Variance

The expected value (mean) of a uniform distribution is the midpoint of the interval [a, b]:

$$E[X] = \frac{a+b}{2}$$

The variance of a uniform distribution is given by:

$$\text{Var}(X) = \frac{(b-a)^2}{12}$$

### Moment Generating Functions and Moments

The moment generating function (MGF) of a uniform distribution is:

$$M_X(t) = E[e^{tX}] = \frac{e^{tb} - e^{ta}}{t(b-a)}$$

To find the n-th moment, we take the n-th derivative of the MGF with respect to t and then evaluate it at t=0:

$$E[X^n] = \frac{d^n M_X(t)}{dt^n}\Bigg|_{t=0}$$

* **First Moment (Mean):**

$$E[X] = \frac{a+b}{2}$$

* **Second Moment (Variance + Mean^2):**

$$E[X^2] = \frac{a^2 + ab + b^2}{3}$$

### Applications

Uniform distributions are often used as a simple model when all possible outcomes are equally likely, such as in random number generators or when sampling from a finite set of values.
