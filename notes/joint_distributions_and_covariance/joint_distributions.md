# Joint Distributions

A univariate distribution describes one random variable. A **joint distribution** describes several random variables simultaneously and therefore contains the information needed to reason about dependence, conditional behavior, and functions of multiple variables.

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

Probabilities are obtained by summing or integrating over regions. For example,

$$
P(X\le a,Y\le b)=F_{X,Y}(a,b),
$$

where $F_{X,Y}$ is the joint CDF.

## Marginal Distributions

A **marginal distribution** describes one variable after the other variable has been summed or integrated out.

For discrete variables,

$$
p_X(x)=\sum_y p_{X,Y}(x,y),
$$

and for continuous variables,

$$
f_X(x)=\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy.
$$

The same construction gives the marginal distribution of $Y$.

A useful way to think about this is that the joint distribution contains the full two-variable model, while each marginal distribution is only one projection of that model.

## Conditional Distributions

Conditioning asks how the distribution of one variable changes after another variable is known.

For discrete variables with $P(Y=y)>0$,

$$
p_{X\mid Y}(x\mid y)=\frac{p_{X,Y}(x,y)}{p_Y(y)}.
$$

For continuous variables with $f_Y(y)>0$,

$$
f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}.
$$

This is the random-variable analogue of conditional probability introduced earlier. Regression later builds on exactly this idea by modeling a conditional mean or conditional probability.

## Independence

Random variables $X$ and $Y$ are independent when their joint distribution factors into their marginals. In the discrete case,

$$
p_{X,Y}(x,y)=p_X(x)p_Y(y)
$$

for all relevant $x$ and $y$. In the continuous case,

$$
f_{X,Y}(x,y)=f_X(x)f_Y(y).
$$

If this factorization fails, the variables are dependent.

Independence is stronger than zero covariance. Two variables can be dependent in a nonlinear way while having covariance zero.

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
\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y].
$$

That identity is developed in **[Covariance](covariance.md)**.

## Why This Chapter Comes Before Regression

Regression does not merely ask whether two variables are related. It models the conditional behavior of a response given predictors. Joint and conditional distributions therefore provide the probability language that makes regression concepts such as $E[Y\mid X=x]$ meaningful.

Continue with **[Covariance](covariance.md)** and **[Correlation](correlation.md)** before moving to sampling distributions or regression.
