## Beta Distribution (Continuous)

A continuous random variable X follows a beta distribution if it is used to model the behavior of random variables that are constrained to intervals of finite length, often [0,1]. The beta distribution is characterized by two shape parameters, $\alpha$ and $\beta$, and is denoted as $X \sim \text{Beta}(\alpha, \beta)$.

### Probability Density Function (PDF)

The PDF of a beta distribution is given by:

$$f(x; \alpha, \beta) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)}$$

for $0 \le x \le 1$ and $\alpha, \beta > 0$, where $B(\alpha, \beta)$ is the beta function.

![output(3)](https://github.com/user-attachments/assets/55124c97-5633-4356-a807-13f1c0369034)

### Cumulative Distribution Function (CDF)

The CDF of a beta distribution, $F(x; \alpha, \beta)$, does not have a simple closed-form expression but is the integral of the PDF over its domain.

![output(4)](https://github.com/user-attachments/assets/8fec2c6f-a124-4254-8f2b-0b0d9e7a9555)

### Expected Value and Variance

The expected value (mean) of a beta distribution is:

$$E[X] = \frac{\alpha}{\alpha + \beta}$$

The variance of a beta distribution is:

$$\text{Var}(X) = \frac{\alpha \beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}$$

### Example: Quality Control in Manufacturing

In a manufacturing process, the proportion of defective items produced is assumed to follow a beta distribution with $\alpha = 2$ and $\beta = 5$.

Given:

- $\alpha = 2$
- $\beta = 5$

Using the beta distribution formulas:

I. What is the expected proportion of defective items?

Expected proportion of defective items:

$$E[X] = \frac{2}{2 + 5} \approx 0.2857$$

II. What is the variance of this proportion?

Variance of the proportion:

$$\text{Var}(X) = \frac{2 \times 5}{(2 + 5)^2(2 + 5 + 1)} \approx 0.0408$$

### Applications

Beta distributions are widely used in Bayesian statistics, project management for modeling the completion time of tasks, and in reliability engineering to model the failure rate of systems. It is also used in genetics and ecology to model variability in proportions and rates.
