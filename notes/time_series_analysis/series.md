## Sequences and Series

### Sequences

A **sequence** is an ordered list of numbers that can be viewed as a function mapping each natural number $n$ to a specific value $a_n$. More formally, a sequence $\{a_n\}$ is a function whose domain is the set of natural numbers, and the values are called the terms of the sequence:

$$
a_1, a_2, a_3, \dots, a_n, \dots
$$

A sequence can either approach a particular value, in which case it is said to **converge**, or it can increase or oscillate indefinitely, in which case it **diverges**.

A sequence $\{a_n\}$ **converges** to a limit $a$ if, as $n$ becomes very large, the values of $a_n$ get arbitrarily close to $a$. Mathematically, this is expressed as:

$$
\lim_{n \to \infty} a_n = a
$$

This means for any small number $\epsilon > 0$, there exists a large number $N$ such that for all $n > N$, the distance between $a_n$ and $a$ is smaller than $\epsilon$. If no such limit exists, the sequence **diverges**.

#### Examples of Sequences

1. **Convergent Sequence:**

Consider the sequence $a_n = \frac{n}{n+2}$. This gives the sequence:

$$
\frac{1}{3}, \frac{2}{4}, \frac{3}{5}, \dots
$$

As $n \to \infty$, the terms of the sequence approach 1:

$$
\lim_{n \to \infty} \frac{n}{n+2} = 1
$$

Therefore, this sequence converges to 1.

2. **Divergent Sequence:**

Now consider the sequence $a_n = 4^n$. This gives the sequence:

$$
4, 16, 64, \dots
$$

As $n \to \infty$, the terms of the sequence grow without bound, meaning this sequence diverges.

3. **Another Divergent Sequence:**

Another example of a divergent sequence is $a_n = n + 1$, which gives:

$$
2, 3, 4, \dots
$$

As $n \to \infty$, the sequence grows indefinitely, and hence it diverges.

4. **Convergent Sequence:**

Consider the sequence $a_n = \frac{1}{n^3}$, which gives:

$$
1, \frac{1}{8}, \frac{1}{27}, \dots
$$

As $n \to \infty$, the terms of this sequence get smaller and smaller, approaching 0:

$$
\lim_{n \to \infty} \frac{1}{n^3} = 0
$$

Hence, this sequence converges to 0.

### Partial Sums

The **partial sum** $s_n$ of a sequence $\{a_n\}$ is the sum of the first $n$ terms of the sequence:

$$
s_n = a_1 + a_2 + \dots + a_n
$$

Partial sums are used to analyze the behavior of series, where the idea is to observe whether the sum of the terms converges to a specific value as more terms are added. For example, consider the following partial sums:

- $s_1 = a_1$
- $s_2 = a_1 + a_2$
- $s_3 = a_1 + a_2 + a_3$
- $\dots$

A series formed by a sequence is said to converge if the sequence of partial sums converges as $n \to \infty$.

### Series

A **series** is the sum of the terms of a sequence. If the sequence of partial sums $\{s_n\}$ converges to a limit $s$, the series is said to **converge** to that limit $s$. Mathematically, the infinite series is written as:

$$
\sum_{k=1}^{\infty} a_k = \lim_{n \to \infty} s_n = \lim_{n \to \infty} (a_1 + a_2 + \dots + a_n) = s
$$

If the partial sums do not approach a finite limit as $n$ increases, then the series is said to be **divergent**.

### Geometric Series and Rational Functions

A **geometric series** is a series of the form:

$$
\sum_{k=0}^{\infty} r^k = \frac{1}{1 - r}, \quad \text{for } |r| < 1
$$

This result can be used to represent certain rational functions as infinite series. For example:

$$
\frac{1}{1 - x} = \sum_{k=0}^{\infty} x^k, \quad \text{for } |x| < 1
$$

This is useful in time series analysis when dealing with autoregressive models and other representations involving rational functions.

### Examples of Convergent Series

I. **Geometric Series**:

A geometric series is a series where each term is a constant multiple (called the common ratio) of the previous term. A simple example is the following geometric series:

$$
\sum_{k=0}^{\infty} \frac{1}{3^k}
$$

This series converges to:

$$
\sum_{k=0}^{\infty} \frac{1}{3^k} = \frac{1}{1 - \frac{1}{3}} = \frac{3}{2}
$$

II. **P-Series** (convergent for $p > 1$):

A **p-series** is of the form:

$$
\sum_{k=1}^{\infty} \frac{1}{k^p}
$$

For $p = 2$, the series converges to:

$$
\sum_{k=1}^{\infty} \frac{1}{k^2} = \frac{\pi^2}{6}
$$

III. **Alternating Series**:

An alternating series is a series where the signs of the terms alternate between positive and negative. A famous example is:

$$
\sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k}
$$

This series converges to:

$$
\sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k} = \ln(2)
$$

### Examples of Divergent Series

I. **Geometric Series with growth factor greater than 1**:

Consider the geometric series:

$$
\sum_{k=1}^{\infty} 4^k = 4 + 16 + 64 + \dots
$$

Since the ratio between successive terms is greater than 1, this series diverges as the partial sums grow without bound.

II. **Arithmetic Series**:

In an arithmetic series, the difference between successive terms is constant. For example:

$$
\sum_{k=1}^{\infty} (2k + 3) = 5 + 7 + 9 + \dots
$$

The terms grow linearly, and the series diverges as $n \to \infty$.

III. **Harmonic Series**:

The harmonic series is:

$$
\sum_{k=1}^{\infty} \frac{1}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \dots
$$

Although the terms $\frac{1}{k}$ approach 0 as $k \to \infty$, the sum of the terms grows without bound. Hence, the harmonic series diverges.

### Absolute Convergence

A series is **absolutely convergent** if the series of the absolute values of its terms is convergent:

$$
\sum_{k=1}^{\infty} |a_k|
$$

**Absolute convergence** implies **convergence**. This is a stronger condition than regular convergence, as a series can converge without being absolutely convergent (for example, alternating series).

### Convergence Tests

When dealing with infinite series, it’s important to determine whether the series converges (approaches a finite value) or diverges (grows without bound or oscillates without settling). To do this, mathematicians use various convergence tests, each suited for different types of series. Below are some of the most commonly used tests for determining whether an infinite series converges or diverges:

I. **Integral Test**:

The integral test compares a series to the integral of a continuous, positive, decreasing function. Suppose $\{a_n\}$ is a sequence and $f(x)$ is a continuous, positive, decreasing function such that $f(n) = a_n$ for all $n \geq 1$. If the integral of $f(x)$ from 1 to infinity converges, then the series converges. Otherwise, the series diverges.

$$
\sum_{n=1}^{\infty} a_n \quad \text{converges if and only if} \quad \int_1^{\infty} f(x) \, dx \quad \text{converges}.
$$

**Example**: Consider the series $\sum_{n=1}^{\infty} \frac{1}{n^2}$. Compare this to the integral $\int_1^{\infty} \frac{1}{x^2} \, dx$, which converges to 1. Hence, the series converges.

II. **Comparison Test**:

The comparison test compares the given series to a known convergent or divergent series. If the terms of the series $\{a_n\}$ are smaller than the terms of a known convergent series $\{b_n\}$, and all terms are positive, then the series $\sum a_n$ also converges. Similarly, if the terms are larger than those of a known divergent series, the series $\sum a_n$ diverges.

$$
0 \leq a_n \leq b_n \quad \text{and} \quad \sum b_n \quad \text{converges} \quad \Rightarrow \quad \sum a_n \quad \text{converges}.
$$

**Example**: To check if $\sum_{n=1}^{\infty} \frac{1}{n^3 + 2}$ converges, compare it to $\sum_{n=1}^{\infty} \frac{1}{n^3}$, which is a convergent p-series with $p > 1$. Since the terms of $\frac{1}{n^3 + 2}$ are smaller, the series converges by comparison.

III. **Limit Comparison Test**:

The limit comparison test is useful when the terms of the series are not directly comparable to a known series but have similar behavior as $n \to \infty$. If the limit of the ratio between the terms of two series is a finite, positive constant, both series either converge or diverge together.

$$
\lim_{n \to \infty} \frac{a_n}{b_n} = c \quad \text{where} \quad 0 < c < \infty.
$$

**Example**: Consider the series $\sum_{n=1}^{\infty} \frac{n^2 + 1}{2n^2 + 3}$. Compare it to $\sum_{n=1}^{\infty} \frac{1}{n^2}$. The limit of the ratio of terms is:

$$
\lim_{n \to \infty} \frac{\frac{n^2 + 1}{2n^2 + 3}}{\frac{1}{n^2}} = \frac{1}{2}.
$$

Since the comparison series $\sum \frac{1}{n^2}$ converges, the original series also converges.

IV. **Alternating Series Test (Leibniz's Test)**:

This test is used for series where the terms alternate in sign. For an alternating series $\sum (-1)^{n} a_n$, if the absolute value of the terms $a_n$ decreases monotonically (i.e., $a_{n+1} \leq a_n$) and $\lim_{n \to \infty} a_n = 0$, then the series converges.

**Example**: Consider the alternating harmonic series $\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}$, which is of the form $(-1)^{n+1} \frac{1}{n}$. Since $\frac{1}{n}$ decreases and approaches 0 as $n \to \infty$, the series converges.

V. **Ratio Test**:

The ratio test is particularly useful for series involving factorials or exponential terms. To apply the ratio test, compute the limit of the absolute value of the ratio of successive terms:

$$
L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|.
$$

- If $L < 1$, the series converges.
- If $L > 1$, the series diverges.
- If $L = 1$, the test is inconclusive.

**Example**: For the series $\sum_{n=1}^{\infty} \frac{n!}{n^n}$, applying the ratio test gives:

$$
L = \lim_{n \to \infty} \left| \frac{(n+1)!/(n+1)^{n+1}}{n!/n^n} \right| = \lim_{n \to \infty} \frac{(n+1)}{n+1} \cdot \left(\frac{n}{n+1}\right)^n = 0.
$$

Since $L = 0$, the series converges.

VI. **Root Test**:

The root test, or Cauchy's root test, involves taking the $n$-th root of the absolute value of the terms of the series. Let:

$$
L = \lim_{n \to \infty} \sqrt[n]{|a_n|}.
$$

- If $L < 1$, the series converges.
- If $L > 1$, the series diverges.
- If $L = 1$, the test is inconclusive.

**Example**: For the series $\sum_{n=1}^{\infty} \left(\frac{3}{4}\right)^n$, applying the root test gives:

$$
L = \lim_{n \to \infty} \sqrt[n]{\left|\frac{3}{4}\right|^n} = \frac{3}{4}.
$$

Since $L = \frac{3}{4} < 1$, the series converges.

### Mean-Square Convergence

In the context of stochastic processes, mean-square convergence is an important concept for analyzing the behavior of sequences of random variables. Suppose $X_1, X_2, X_3, \dots$ is a sequence of random variables representing a stochastic process. We say that $X_n$ converges to a random variable $X$ in the **mean-square sense** if the expected value of the squared difference between $X_n$ and $X$ approaches zero as $n$ becomes large. Formally, this is expressed as:

$$
\mathbb{E}[(X_n - X)^2] \to 0 \quad \text{as} \quad n \to \infty
$$

This definition means that as $n \to \infty$, the random variables $X_n$ become increasingly close to $X$ in the sense of the expected value of their squared differences, providing a measure of convergence in a probabilistic sense.

#### Inverting the MA(1) Model

Consider the **MA(1)** (Moving Average of order 1) model, which is commonly used in time series analysis. In this model, the process $X_t$ at time $t$ is defined as:

$$
X_t = Z_t + \beta Z_{t-1}
$$

where $Z_t$ represents white noise, which is a sequence of independent, identically distributed random variables with zero mean and constant variance $\sigma_Z^2$. The parameter $\beta$ is a constant that defines the relationship between the current observation and the previous white noise term.

We are interested in expressing $Z_t$ as an infinite sum involving the past values of $X_t$. Through algebraic manipulation, we can express $Z_t$ as:

$$
Z_t = \sum_{k=0}^{\infty} (-\beta)^k X_{t-k}
$$

This infinite sum can be shown to **converge in the mean-square sense**, provided certain conditions on $\beta$ are satisfied. Specifically, we need to ensure that the sum of these terms remains bounded as $n \to \infty$, which ensures that the approximation $\sum_{k=0}^{n} (-\beta)^k X_{t-k}$ becomes increasingly close to $Z_t$.

#### Autocovariance Function of the MA(1) Process

The **autocovariance function** $\gamma(k)$ of a stochastic process measures the covariance between $X_t$ and $X_{t+k}$ for different time lags $k$. For the MA(1) process, the autocovariance function is relatively simple due to the limited memory of the process, which only depends on the current and previous white noise terms.

The autocovariance function for the MA(1) process is given by:

$$
\gamma(k) = 
\begin{cases}
(1 + \beta^2) \sigma_Z^2, & \text{if } k = 0 \\
\beta \sigma_Z^2, & \text{if } k = 1 \\
0, & \text{if } k > 1
\end{cases}
$$

For negative values of $k$, the autocovariance function is symmetric, meaning that $\gamma(-k) = \gamma(k)$.

This shows that the MA(1) process has non-zero autocovariances only for the first lag (i.e., between $X_t$ and $X_{t-1}$), and beyond that, the covariance is zero due to the white noise properties of $Z_t$.

#### Series Convergence in Mean-Square Sense

To investigate the convergence of the infinite series expression for $Z_t$, consider the partial sum of the first $n$ terms:

$$
\sum_{k=0}^{n} (-\beta)^k X_{t-k}
$$

We want to ensure that this sum converges to $Z_t$ in the mean-square sense. In other words, we need:

$$
\mathbb{E}\left[\left(\sum_{k=0}^{n} (-\beta)^k X_{t-k} - Z_t \right)^2\right] \to 0 \quad \text{as} \quad n \to \infty
$$

This expression represents the expected value of the squared difference between the partial sum and the true value of $Z_t$, and we aim to show that this difference diminishes as more terms are added to the sum.

Expanding this expression:

$$
\mathbb{E}\left[\left(\sum_{k=0}^{n} (-\beta)^k X_{t-k}\right)^2 - 2\mathbb{E}\left(\sum_{k=0}^{n} (-\beta)^k X_{t-k} Z_t \right) + \mathbb{E}[Z_t^2]\right]
$$

Breaking this down into individual terms:
- The first term involves the expected value of the squared partial sum: $\mathbb{E}\left[\sum_{k=0}^{n} \beta^{2k} X_{t-k}^2\right]$.
- The second term represents the cross terms between the partial sum and $Z_t$.
- The third term is the variance of $Z_t$, which is $\sigma_Z^2$.

To achieve mean-square convergence, the total expression must approach 0 as $n \to \infty$.

#### Condition for Convergence

For the series to converge in the mean-square sense, we require that the individual terms involving powers of $\beta$ decay sufficiently fast. Specifically, we need:

$$
\sigma_Z^2 \beta^{2(n+2)} \to 0 \quad \text{as} \quad n \to \infty
$$

This will only occur if:

$$
|\beta| < 1
$$

When $|\beta| < 1$, the powers of $\beta$ diminish as $n$ increases, ensuring that the sum remains bounded and that the partial sums converge to $Z_t$.

#### Invertibility Condition

The condition $|\beta| < 1$ is also known as the **invertibility condition** for the MA(1) process. This condition guarantees that the moving average process can be expressed as an infinite autoregressive (AR) process. In terms of the polynomial $\beta(B) = 1 + \beta B$ (where $B$ is the backshift operator), the invertibility condition states that the root of the polynomial must lie **outside the unit circle** in the complex plane, meaning:

$$
|\beta| < 1
$$

Thus, the invertibility condition ensures that the MA(1) process can be uniquely represented as an **AR(∞)** process, which is crucial for the identification and estimation of time series models.
