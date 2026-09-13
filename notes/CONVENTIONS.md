# Conventions for the Statistics Notes

These conventions are intended to make independently written chapters feel like parts of one set of notes. They are guidelines for new material and for gradual cleanup of existing material, not a requirement to rewrite every historical chapter at once.

## Document Structure

- Each standalone Markdown note should have exactly one level-one heading (`#`) naming the topic.
- Use level-two headings (`##`) for major sections and deeper levels for subsections.
- Section `README.md` files should explain prerequisites, reading order, scope, and links to adjacent sections rather than duplicate chapter content.
- Prefer relative links within the repository so navigation is branch-independent.

## Population and Sample Notation

Unless a chapter defines another convention:

| Quantity | Population | Sample / estimate |
|---|---|---|
| Mean | $\mu$ | $\bar{x}$ |
| Variance | $\sigma^2$ | $s^2$ |
| Standard deviation | $\sigma$ | $s$ |
| Correlation | $\rho$ | $r$ |
| Generic parameter | $\theta$ | $\hat{\theta}$ |

Use uppercase letters such as $X$ and $Y$ for random variables and lowercase letters such as $x$, $y$, or $x_i$ for realized values or observations when that distinction matters.

## Probability, Mass, Density, and Distribution

- For a discrete random variable, a PMF gives point probabilities such as $P(X=x)$.
- For a continuous random variable, a PDF is a density. The value $f(x)$ is not itself the probability of observing exactly $x$; for an absolutely continuous distribution, $P(X=x)=0$.
- A CDF is valid for both discrete and continuous random variables: $F(x)=P(X\le x)$.
- The counting formula $P(A)=|A|/|S|$ applies to finite sample spaces whose elementary outcomes are equally likely; it is not the general definition of probability.

## Models, Errors, and Residuals

- An **error term** such as $\varepsilon_i$ is an unobserved random component of a statistical model.
- A **residual** such as $e_i=y_i-\hat{y}_i$ is computed after fitting a model.
- Avoid using “error” and “residual” interchangeably when the distinction matters for estimation or diagnostics.

## Assumptions and Inference

State what an assumption is needed for. For example:

- Pearson's correlation can be computed without assuming marginal normality; distributional assumptions enter classical confidence intervals and tests.
- Ordinary least squares coefficients can be computed without normally distributed errors; normality is relevant to exact small-sample t/F inference under the classical model.
- Independence assumptions concern how observations are generated, not merely the visual shape of a histogram.

Separating definition, estimation, and inference prevents assumptions from appearing stronger than they are.

## Association, Prediction, and Causation

Use these terms deliberately:

- **association** describes statistical dependence;
- **prediction** concerns performance for unknown outcomes;
- **causation** requires a causal design or justified causal assumptions beyond association alone.

Do not describe correlation, regression coefficients, Granger predictability, or a good predictive model as causal evidence without additional justification.

## Parameterizations

Some distributions have multiple common parameterizations. State the convention before using formulas. In these notes, for example, the gamma chapter uses shape $\alpha$ and **rate** $\beta$, so $E[X]=\alpha/\beta$. A library using a scale parameter instead will have different-looking formulas.

## Examples and Numerical Results

- Label toy or synthetic examples as such when their purpose is hand calculation rather than realistic modeling.
- Keep units attached to interpretations.
- Prefer enough significant digits to reproduce the conclusion without implying false precision.
- When a result depends on software conventions, name the convention or parameterization rather than presenting it as universal.