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

### Example: Random Number Generation

A developer is creating a simulation game where an event should happen at a random time between 2 and 4 seconds after a specific action. The time until the event is modeled using a continuous uniform distribution.

a) What is the probability that the event happens within 2.5 seconds after the action?
b) What is the expected value and variance of the time until the event happens?

For a continuous uniform distribution $U(a, b)$:

$$f(x; a, b) = \frac{1}{b - a} \text{ for } a \leq x \leq b$$

Given: $a = 2$ seconds, $b = 4$ seconds

a) Probability of happening within 2.5 seconds:

$$P(X < 2.5) = \frac{2.5 - 2}{4 - 2} = 0.25$$

b) Expected value and variance:

- Expected value: $E[X] = \frac{a + b}{2} = \frac{2 + 4}{2} = 3$ seconds
- Variance: $\text{Var}(X) = \frac{(b - a)^2}{12} = \frac{(4 - 2)^2}{12} = \frac{1}{3} \text{ seconds}^2$

### Applications

Uniform distributions are often used as a simple model when all possible outcomes are equally likely, such as in random number generators or when sampling from a finite set of values.
