# Joint Distributions

A univariate distribution describes a single random variable. A **joint distribution** describes several random variables simultaneously and contains the information needed to reason about dependence, conditional behavior, and functions of multiple variables.

## Joint Probability Models

For two discrete random variables $X$ and $Y$, the joint probability mass function is

$$
p_{X,Y}(x,y)=P(X=x,Y=y).
$$

It satisfies

$$
p_{X,Y}(x,y)\ge 0
$$

and

$$
\sum_x\sum_y p_{X,Y}(x,y)=1.
$$

For two continuous random variables, a joint probability density function $f_{X,Y}(x,y)$ satisfies

$$
f_{X,Y}(x,y)\ge 0
$$

and

$$
\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dx\,dy=1.
$$

Probabilities are obtained by summing or integrating the joint distribution over the relevant region. For example,

$$
P(X\le a,Y\le b)=F_{X,Y}(a,b),
$$

where $F_{X,Y}$ is the joint cumulative distribution function (CDF).

## Marginal Distributions

A **marginal distribution** describes one variable after the other has been summed or integrated out.

For discrete variables,

$$
p_X(x)=\sum_y p_{X,Y}(x,y),
$$

and for continuous variables,

$$
f_X(x)=\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy.
$$

The same construction gives the marginal distribution of $Y$.

### A joint table makes the operations concrete

Suppose $X$ and $Y$ indicate whether two products are purchased:

| $X$ | $Y=0$ | $Y=1$ | Marginal $p_X(x)$ |
|---|---|---|---|
| 0 | 0.4 | 0.1 | 0.5 |
| 1 | 0.2 | 0.3 | 0.5 |
| Marginal $p_Y(y)$ | 0.6 | 0.4 | 1.0 |

The four interior probabilities sum to one. Adding across the first row gives $P(X=0)=0.5$; adding down the second probability column gives $P(Y=1)=0.4$. Neither marginal alone tells us that both products are purchased with probability $0.3$. A model with the same marginals could allocate different mass to that joint event.

A useful way to think about this is that the joint distribution contains the full two-variable model, while each marginal distribution describes only one variable on its own.

## Conditional Distributions

Conditioning asks how the distribution of one variable changes when the value of another variable is known.

For discrete variables with $P(Y=y)>0$,

$$
p_{X\mid Y}(x\mid y)=\frac{p_{X,Y}(x,y)}{p_Y(y)}.
$$

For continuous variables with $f_Y(y)>0$,

$$
f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}.
$$

This is the random-variable analogue of conditional probability introduced earlier. Regression later builds on the same idea by modeling a conditional mean or conditional probability.

In the table, restricting attention to $Y=1$ retains total probability $0.4$. Dividing the retained joint masses by $0.4$ gives $P(X=1\mid Y=1)=0.3/0.4=0.75$ and $P(X=0\mid Y=1)=0.25$. The normalized probabilities sum to one. For a continuous $Y$, the density ratio defines a conditional density rather than dividing by $P(Y=y)$, which is zero at a single point. More generally conditional distributions are defined almost everywhere with respect to the marginal law.

## Independence

Random variables $X$ and $Y$ are independent when their joint distribution factors into the product of their marginal distributions. In the discrete case,

$$
p_{X,Y}(x,y)=p_X(x)p_Y(y)
$$

for all relevant $x$ and $y$. In the continuous case,

$$
f_{X,Y}(x,y)=f_X(x)f_Y(y).
$$

If this factorization does not hold, the variables are dependent.

For the purchase table, independence would require $P(X=1,Y=1)=P(X=1)P(Y=1)=0.5(0.4)=0.2$. The actual joint probability is $0.3$, so independence fails. Equivalently, learning that $Y=1$ changes the chance of $X=1$ from $0.5$ to $0.75$. Checking one unequal pair is enough to disprove factorization; proving independence requires the equality throughout the support, or an equivalent event-level argument.

Independence is stronger than zero covariance. Two variables can be dependent in a nonlinear way while still having covariance zero.

## Expectations of Functions of Several Variables

Once a joint distribution is known, expectations involving both variables can be computed directly. For discrete variables,

$$
E[g(X,Y)] = \sum_x\sum_y g(x,y)p_{X,Y}(x,y),
$$

and for continuous variables,

$$
E[g(X,Y)] = \int\!\!\int g(x,y)f_{X,Y}(x,y)\,dx\,dy.
$$

Important special cases include $E[X]$, $E[Y]$, and $E[XY]$. These lead directly to covariance:

$$
\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y].
$$

That identity is developed in **[Covariance](https://github.com/djeada/Statistics-Notes/blob/main/notes/joint_distributions_and_covariance/covariance.md)**.

## Conditional Means and Regression

Regression does not simply ask whether two variables are related. It models the conditional behavior of a response given one or more predictors. Joint and conditional distributions therefore provide the probability language needed to make expressions such as $E[Y\mid X=x]$ meaningful.

In the table, $E[XY]=0.3$, because the product is one only in the bottom-right interior cell. Thus $\operatorname{Cov}(X,Y)=0.3-0.5(0.4)=0.1$. The joint model supplies the probabilities from which covariance is computed; the single covariance value does not allow us to reconstruct an arbitrary joint model.
