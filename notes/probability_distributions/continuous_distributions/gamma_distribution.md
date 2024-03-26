## Gamma Distribution (Continuous)

A continuous random variable X follows a gamma distribution if it is used to model the time until an event occurs a specific number of times. The gamma distribution is a two-parameter family of continuous probability distributions and is often denoted as $X \sim \text{Gamma}(\alpha, \beta)$, where $\alpha$ (shape parameter) and $\beta$ (rate parameter) are positive real numbers.

### Probability Density Function (PDF)

The PDF of a gamma distribution is given by:

$$f(x; \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}$$

for $x > 0$, $\alpha > 0$, $\beta > 0$, and where $\Gamma(\alpha)$ is the gamma function.

### Cumulative Distribution Function (CDF)

The CDF of a gamma distribution, denoted as $F(x; \alpha, \beta)$, does not have a simple closed-form expression but is defined as the integral of the PDF.

### Expected Value and Variance

The expected value (mean) of a gamma distribution is:

$$E[X] = \frac{\alpha}{\beta}$$

The variance of a gamma distribution is:

$$\text{Var}(X) = \frac{\alpha}{\beta^2}$$

### Moment Generating Function (MGF)

The moment generating function (MGF) of a gamma distribution is:

$$M_X(t) = (1 - \frac{t}{\beta})^{-\alpha}, \text{ for } t < \beta$$

### Example: Flood Frequency Study

A hydrologist is analyzing flood intervals in a specific area. The intervals, measured in years, follow a gamma distribution characterized by a shape parameter (α) and a rate parameter (β).

- Shape parameter, $\alpha = 2$
- Rate parameter, $\beta = \frac{1}{3}$ per year

The study aims to determine:

I. The average time between floods.

The mean of a gamma distribution is given by $E[X] = \frac{\alpha}{\beta}$.

$$ E[X] = \frac{2}{\frac{1}{3}} = 6 \text{ years} $$

II. The variability (variance) of this interval.

The variance of a gamma distribution is $\text{Var}(X) = \frac{\alpha}{\beta^2}$.

$$ \text{Var}(X) = \frac{2}{\left(\frac{1}{3}\right)^2} = 18 \text{ years}^2 $$

### Applications

Gamma distributions are used in various fields such as hydrology for modeling flood events, in finance for modeling the time until default, and in health sciences for modeling the time until death or failure of a biological organ or system.
