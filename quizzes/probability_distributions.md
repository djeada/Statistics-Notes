# Probability Distributions Quiz

Notes: [Introduction to Distributions](../notes/random_variables_and_distributions/introduction_to_distributions.md), [Binomial](../notes/random_variables_and_distributions/discrete/binomial_distribution.md), [Poisson](../notes/random_variables_and_distributions/discrete/poisson_distribution.md), [Geometric](../notes/random_variables_and_distributions/discrete/geometric_distribution.md), [Negative Binomial](../notes/random_variables_and_distributions/discrete/negative_binomial_distribution.md), [Uniform](../notes/random_variables_and_distributions/continuous/uniform_distribution.md), [Normal](../notes/random_variables_and_distributions/continuous/normal_distribution.md), [Exponential](../notes/random_variables_and_distributions/continuous/exponential_distribution.md), [Log-Normal](../notes/random_variables_and_distributions/continuous/log_normal_distribution.md), [Beta](../notes/random_variables_and_distributions/continuous/beta_distribution.md), [Normal Curve and Z-Scores](../notes/random_variables_and_distributions/normal_curve_and_z_score.md), [Central Limit Theorem](../notes/sampling_and_sampling_distributions/central_limit_theorem.md)

Check your understanding of common discrete and continuous distributions, their parameters and when to use them.

#### Q. Which statement describes a **continuous uniform distribution** on the interval $[a, b]$?

* [x] Its density is constant on $[a, b]$, so equal-length subintervals are equally likely
* [ ] Its density peaks at the midpoint $(a+b)/2$ and falls towards the ends
* [ ] It can only describe variables that take a finite number of values
* [ ] It is skewed to the right, with a long tail towards $b$

> **Explanation:** The uniform density is $1/(b-a)$ everywhere on $[a, b]$, so the probability of a subinterval depends only on its length. It is symmetric, with mean $(a+b)/2$.

#### Q. If X follows a **log-normal distribution**, which statement is true?

* [x] $\ln X$ is normally distributed and X takes only positive values
* [ ] X is symmetric, so its mean equals its median
* [ ] X can take negative values in its left tail
* [ ] $e^X$ is normally distributed and X is bounded above

> **Explanation:** By definition $X = e^Y$ with $Y$ normal, so $X > 0$. The distribution is right-skewed, so its mean exceeds its median. This is why it is used for prices and incomes.

#### Q. Which property holds for a **Poisson distribution** with parameter $\lambda$?

* [x] Its mean and its variance both equal $\lambda$
* [ ] Its variance equals $\lambda^2$
* [ ] It applies to continuous random variables
* [ ] It counts successes in a fixed number of trials

> **Explanation:** For $X \sim \text{Poisson}(\lambda)$, $E[X] = \text{Var}(X) = \lambda$. Counting successes in a fixed number of trials describes the binomial distribution.

#### Q. Which property characterises the **exponential distribution**?

* [x] It has a constant hazard rate, so it is memoryless
* [ ] It is symmetric about its mean $1/\lambda$
* [ ] It is defined for negative as well as positive values
* [ ] Its variance equals its mean $1/\lambda$

> **Explanation:** The exponential distribution satisfies $P(T > s + t \mid T > s) = P(T > t)$ because its failure rate $\lambda$ is constant. Its variance is $1/\lambda^2$, not $1/\lambda$.

#### Q. A help desk receives calls independently at an average rate of 4 per hour. Which distribution best models the **number of calls in one hour**?

* [ ] Normal distribution
* [x] Poisson distribution
* [ ] Exponential distribution
* [ ] Geometric distribution

> **Explanation:** Counts of independent events occurring at a constant average rate in a fixed interval follow a Poisson distribution, here with $\lambda = 4$. The exponential would model the waiting time between calls.

#### Q. For $X \sim \text{Binomial}(n, p)$ with fixed $0 < p < 1$, what happens to the shape of the distribution as **n grows large**?

* [ ] It becomes more and more skewed
* [x] It becomes approximately normal
* [ ] It becomes approximately uniform
* [ ] It becomes approximately exponential

> **Explanation:** A binomial count is a sum of $n$ independent Bernoulli trials, so by the central limit theorem it approaches $N(np, np(1-p))$. A common rule of thumb is $np \ge 10$ and $n(1-p) \ge 10$.

#### Q. For a normal distribution, approximately what percentage of values lie **within one standard deviation** of the mean?

* [ ] 50%
* [x] 68%
* [ ] 95%
* [ ] 99.7%

> **Explanation:** The empirical rule gives about 68% within $\pm 1\sigma$, 95% within $\pm 2\sigma$ and 99.7% within $\pm 3\sigma$.

#### Q. If $X \sim \text{Binomial}(10, 0.3)$, what are its **mean and variance**?

* [x] Mean 3, variance 2.1
* [ ] Mean 3, variance 3
* [ ] Mean 3, variance 0.21
* [ ] Mean 0.3, variance 2.1

> **Explanation:** For a binomial, $E[X] = np = 10 \times 0.3 = 3$ and $\text{Var}(X) = np(1-p) = 10 \times 0.3 \times 0.7 = 2.1$.

#### Q. What does the **Central Limit Theorem (CLT)** state?

* [ ] Any sufficiently large sample of raw data is normally distributed
* [x] The sampling distribution of the sample mean approaches normal as n grows
* [ ] The population mean of any variable is normally distributed
* [ ] Larger samples have sampling distributions that are more skewed

> **Explanation:** For i.i.d. observations with finite variance $\sigma^2$, $\bar{X}$ is approximately $N(\mu, \sigma^2/n)$ for large $n$, whatever the population shape. The raw data themselves keep the population's shape.

#### Q. Exam scores are normally distributed with mean 70 and standard deviation 10. Approximately what fraction of students score **above 90**?

* [x] About 2.3%
* [ ] About 5%
* [ ] About 16%
* [ ] About 0.15%

> **Explanation:** $z = (90 - 70)/10 = 2$ and $P(Z > 2) \approx 0.0228$. About 5% lie beyond $\pm 2\sigma$ in total, so only half of that is in the upper tail.

#### Q. The **binomial distribution** models:

* [ ] The waiting time until the next event in a Poisson process
* [x] The number of successes in a fixed number of independent trials
* [ ] The number of events in an interval with no fixed upper limit
* [ ] The number of trials needed to obtain the first success

> **Explanation:** A binomial count needs a fixed $n$, independent trials and a constant success probability $p$. The number of trials until the first success is geometric.

#### Q. Which of the following is a **continuous** distribution?

* [ ] Poisson distribution
* [ ] Binomial distribution
* [x] Normal distribution
* [ ] Geometric distribution

> **Explanation:** The normal distribution has a density over the whole real line. Poisson, binomial and geometric variables take only integer values.

#### Q. The **cumulative distribution function (CDF)** $F(x)$ of a random variable X gives:

* [ ] $P(X = x)$, the probability of exactly the value x
* [x] $P(X \le x)$, the probability of a value at most x
* [ ] $P(X > x)$, the probability of a value above x
* [ ] $f(x)$, the height of the density at x

> **Explanation:** By definition $F(x) = P(X \le x)$. The survival function is $1 - F(x) = P(X > x)$, and for a continuous variable the density is the derivative of $F$.

#### Q. Which statement is true for every **normal distribution**?

* [ ] It is skewed to the right
* [x] It is bell-shaped and symmetric about its mean
* [ ] It is used to model counts of events in an interval
* [ ] It is restricted to non-negative values

> **Explanation:** A normal density is symmetric about $\mu$, so its mean, median and mode coincide and its skewness is zero. It is defined on the whole real line.

#### Q. A help desk receives calls independently at an average rate of 4 per hour. Which distribution models the **waiting time until the next call**?

* [ ] Normal distribution
* [ ] Binomial distribution
* [x] Exponential distribution
* [ ] Poisson distribution

> **Explanation:** In a Poisson process the time between events is exponential with rate $\lambda = 4$ per hour, so the mean wait is $1/4$ hour. The Poisson distribution models the count, not the time.

#### Q. If $X \sim \text{Poisson}(2)$, what is $P(X = 0)$?

* [x] About 0.135
* [ ] About 0.271
* [ ] About 0.500
* [ ] About 0.018

> **Explanation:** $P(X = k) = e^{-\lambda}\lambda^k/k!$, so $P(X = 0) = e^{-2} \approx 0.135$. The value 0.271 is $P(X = 1) = 2e^{-2}$.

#### Q. For a **Poisson distribution**, as the rate parameter $\lambda$ increases, the distribution becomes:

* [ ] More right-skewed
* [x] More symmetric and bell-shaped
* [ ] Concentrated at zero
* [ ] Narrower, with smaller variance

> **Explanation:** The skewness of a Poisson distribution is $1/\sqrt{\lambda}$, which shrinks as $\lambda$ grows, so it approaches a normal shape. Its variance $\lambda$ grows, so it gets wider.

#### Q. In the notes' convention, what does a **geometric** random variable count?

* [ ] The number of successes in a fixed number of trials
* [ ] The waiting time between events in continuous time
* [x] The number of trials up to and including the first success
* [ ] The number of trials needed to obtain r successes

> **Explanation:** The notes define $X \sim \text{Geometric}(p)$ on $\{1, 2, 3, \dots\}$ as the trial on which the first success occurs. Waiting for $r$ successes gives the negative binomial.

#### Q. Each trial succeeds independently with probability 0.2. What is the probability that the **first success occurs on the third trial**?

* [ ] 0.008
* [x] 0.128
* [ ] 0.488
* [ ] 0.200

> **Explanation:** The first two trials must fail and the third succeed: $P(X = 3) = (1-p)^2 p = 0.8^2 \times 0.2 = 0.128$.

#### Q. Which statement about the **variance of a binomial distribution** is true?

* [ ] It always equals the number of trials n
* [x] It depends on both n and p, through $np(1-p)$
* [ ] It does not depend on the success probability p
* [ ] It is always less than 1

> **Explanation:** $\text{Var}(X) = np(1-p)$, which for fixed $n$ is largest at $p = 0.5$. For example, $n = 100, p = 0.5$ gives variance 25.

#### Q. A fair coin is tossed 5 times. What is the probability of getting **exactly 2 heads**?

* [ ] 0.2000
* [ ] 0.4000
* [x] 0.3125
* [ ] 0.0625

> **Explanation:** $P(X = 2) = \binom{5}{2}(0.5)^2(0.5)^3 = 10/32 = 0.3125$.

#### Q. A **Bernoulli** random variable can take which two values?

* [ ] −1 and 1
* [x] 0 and 1
* [ ] 0 and any positive integer
* [ ] Any two real numbers

> **Explanation:** A Bernoulli variable records a single trial as 1 for success (probability $p$) and 0 for failure, so its mean is $p$ and its variance is $p(1-p)$.

#### Q. Which distribution counts the **number of trials needed to obtain r successes** in independent Bernoulli trials?

* [ ] Geometric distribution
* [x] Negative binomial distribution
* [ ] Binomial distribution
* [ ] Poisson distribution

> **Explanation:** The negative binomial generalises the geometric (which is the case $r = 1$). The binomial does the opposite: it fixes the number of trials and counts the successes.

#### Q. You want to model a **proportion** that varies between batches, such as the fraction of defective items, which must lie between 0 and 1. Which family is the natural choice?

* [ ] Normal distribution
* [ ] Exponential distribution
* [x] Beta distribution
* [ ] Log-normal distribution

> **Explanation:** The beta distribution is defined on $[0, 1]$ and its two shape parameters can make it flat, skewed or peaked. The other families give positive probability to values above 1.

#### Q. If waiting times are exponential with rate $\lambda = 0.5$ per minute, what is the probability of waiting **more than 3 minutes**?

* [x] About 0.22
* [ ] About 0.78
* [ ] About 0.50
* [ ] About 0.05

> **Explanation:** For an exponential variable $P(T > t) = e^{-\lambda t} = e^{-0.5 \times 3} = e^{-1.5} \approx 0.223$. The value 0.78 is $P(T \le 3)$.
