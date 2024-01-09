# Expected Values of Joint Densities

Suppose \( f(x,y) \) is a joint distribution

\( E[g(X)h(Y)] \)

\[
= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x)h(x)f(x,y) \,dx \,dy
\]

\[
= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x)h(x)f_X(x)f_Y(y) \,dx \,dy
\]

\[
= \int_{-\infty}^{\infty} h(y)f_Y(y) \,dy \int_{-\infty}^{\infty} g(x)f_X(x) \,dx
\]

\[
= E[h(Y)]E[g(X)]
\]

# Variance of Sum of Random Variables

\( \text{Var}(X + Y) = E[(X + Y - E[X + Y])^2] \)

\[
= E[(X + Y - E[X] - E[Y])^2]
\]

\[
= E[((X - E[X]) + (Y - E[Y]))^2]
\]

\[
= E[(X - E[X])^2] + E[(Y - E[Y])^2] + 2E[(X - E[X])(Y - E[Y])]
\]

\[
= E[(X - E[X])^2] + E[(Y - E[Y])^2] + 2\text{Cov}(X, Y)
\]

\[
\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y)
\]


