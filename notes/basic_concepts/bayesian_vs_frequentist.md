## Bayesian vs Frequentist Statistics

Bayesian and frequentist statistics are two distinct approaches to statistical inference. Both approaches aim to make inferences about an underlying population based on sample data. However, the way they interpret probability and handle uncertainty is fundamentally different.

### Frequentist Statistics

- Frequentist statistics operates under the assumption that parameters in a population are fixed but unknown, such as the true mean, which remains constant even though its value is not directly observed.  
- Confidence intervals are constructed by procedures that *cover* the true parameter value a known proportion of the time in repeated sampling. For example, a 95 % confidence interval means that if an experiment were repeated many times, 95 % of the intervals produced by the same method would capture the true parameter value. (The parameter itself is fixed; it is the interval that varies from sample to sample.)  
- Null hypothesis testing is a core component of frequentist analysis. It tests observed data against a null hypothesis, which typically asserts no effect or no difference, such as the hypothesis that two groups do not differ significantly.  

#### Mathematical Foundations

- Frequentist probability is defined in terms of long-run frequency. This interpretation suggests that, in a large number of trials, the probability of an event—like getting heads in a coin toss—reflects its relative frequency over time.  
- Test statistics are used to measure how unusual the observed data are compared to what would be expected under the null hypothesis. The extremeness of the data is quantified by the p-value, which indicates the probability of obtaining such data if the null hypothesis is true. A small p-value suggests the observed data are inconsistent with the null hypothesis.  

#### Advantages

- Frequentist methods are known for their simplicity and accessibility, making them easier for non-experts to understand and apply in practical settings.  
- These methods are well-suited for large sample sizes, often yielding highly reliable results when ample data are available.  
- Frequentist statistics offer standardized methods, supported by extensive tables and procedures, which have been widely adopted in fields like medicine and social sciences.  

#### Limitations

- One major limitation is that frequentist methods can produce misleading results when applied to small sample sizes or complex data structures, potentially leading to inaccurate conclusions.  
- Frequentist statistics do not incorporate prior knowledge or beliefs about the parameters; they rely solely on the data at hand, potentially missing valuable context.  
- The binary decision-making process, where one either rejects or fails to reject the null hypothesis, can be overly simplistic, often ignoring the nuance and depth of the data, leading to a lack of deeper interpretation.  

#### Example

Let's assume we have a population of ten items, where **X** represents the attribute we are looking for and **O** represents the absence of this attribute.

Population:

```
O O X O O O X X O X
```

We take a sample of 4 randomly from this population:

```
Sample:
X O O X
```

A frequentist would report the **sample proportion** of the attribute, which is 50 % (2 out of 4), as the maximum-likelihood **point estimate** of the population proportion. They might also calculate its standard error and construct a confidence interval before applying the resulting estimate to future inference.

| Step                           | Equation                                                    | Plugging the numbers                                                                  |
|--------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------|
| **Point estimate**             | $\hat p = x/n$                                            | $\hat p = 2/4 = 0.50$                                                               |
| **Standard error**             | $SE(\hat p) = \sqrt{\hat p(1-\hat p)/n}$                  | $\sqrt{0.5,(1-0.5)/4} = \sqrt{0.0625} = 0.25$                                      |
| **95 % confidence interval**<br>(Wald large-sample) | $\hat p \pm z_{0.975},SE(\hat p)$, $z_{0.975}=1.96$ | $0.50 \pm 1.96\times0.25 = 0.50 \pm 0.49$  ⇒ **CI ≈ [0.01, 0.99]**                      |
| **Null-hypothesis test**<br>($H_0: p = p_0$)      | $z = (\hat p - p_0)/\sqrt{p_0(1-p_0)/n}$                  | For $p_0=0.5$:<br>$z = (0.50-0.50)/\sqrt{0.5\cdot0.5/4} = 0$<br>p-value = 1 (fail to reject) |

### Bayesian Statistics

- Bayesian statistics treats parameters as random variables with associated probability distributions, reflecting the uncertainty about their true values rather than considering them fixed.  
- A **prior distribution** represents pre-existing knowledge or beliefs about a parameter, formulated as a probability distribution that captures this initial understanding before observing new data.  
- The **likelihood function** expresses the probability of observing the data given different parameter values. This function plays a key role in updating beliefs as new data become available.  
- The **posterior distribution** is the updated probability distribution after combining the prior distribution and the likelihood. It forms the core of Bayesian inference, offering a new perspective on the parameter based on the data.  

#### Mathematical Framework

**Bayes' Theorem** serves as the foundation of Bayesian analysis. It mathematically updates the prior belief in light of new evidence by using the formula:   

$\text{Posterior} \propto \text{Likelihood} \times \text{Prior}$

reflecting how new data influence prior knowledge.  

In Bayesian statistics, probability is interpreted as a **degree of belief** or certainty about an event or parameter, rather than as a long-run frequency of occurrence as in frequentist statistics.  

#### Incorporating Prior Knowledge

- Bayesian methods allow for the use of general-knowledge priors, even without specific domain expertise. For example, in a study on snake lifespans, a prior could favor a lifespan around 10 years, rather than something implausible like 1000 years, based on biological understanding.  
- As new data are collected, Bayesian inference updates the prior to form the posterior, which reflects the combined influence of prior knowledge and new observations. For instance, if new research suggests that certain snakes live longer than expected, the posterior distribution adjusts to reflect this new evidence alongside previous beliefs.  

#### Advantages

- One of the key strengths of Bayesian statistics is its ability to incorporate prior knowledge or expertise into the analysis, making it particularly valuable in situations where data are limited or difficult to obtain.  
- Bayesian methods often lead to more intuitive and direct interpretations, especially in scenarios where the data are complex or the sample size is small, as the results are framed in terms of probabilities and uncertainties.  
- Bayesian analysis provides a **probabilistic** understanding of estimates, allowing for a more nuanced and detailed interpretation of uncertainty around the parameter estimates (credible intervals give the probability that the parameter lies in a specified range).  
- These methods offer great flexibility in handling complex models and uncertainty, making them well-suited for sophisticated models and smaller datasets.  

#### Limitations

- Bayesian analysis is computationally intensive, requiring significant resources to calculate posterior distributions—particularly when dealing with complex hierarchical models or large datasets—although Markov-chain Monte Carlo and variational inference have made many such analyses practical.  
- The choice of prior can heavily influence the results, potentially introducing bias if the prior is not carefully selected or justified based on solid reasoning.  
- Implementing Bayesian methods requires a more advanced understanding of statistical principles, making them harder to apply and interpret without specialized knowledge.  

#### Example

Assume we have a **Beta(1, 1)** prior, which is uniform on the interval $[0,1]$, expressing equal belief in any value of the probability of a coin landing heads (H) or tails (T).

```
Prior:
H: 0.5, T: 0.5
```

Now we flip the coin 3 times and observe all heads:

```
Data:
H H H
```

Updating the Beta(1, 1) prior with these data yields the posterior **Beta(4, 1)**. The posterior mean is $4/5 = 0.8$:

```
Posterior:
H: 0.8, T: 0.2
```

This demonstrates how the Bayesian approach systematically updates beliefs (probabilities) based on new data.

| Step                      | Equation                                                                                 | Plugging the numbers                      |
|---------------------------|------------------------------------------------------------------------------------------|-------------------------------------------|
| **Prior density**         | $f(p)=dfrac{\Gamma(a+b)}{\Gamma(a),\Gamma(b)},p^{a-1}(1-p)^{b-1}$                   | $a=b=1\implies f(p)=1$ for $p\in[0,1]$ |
| **Likelihood**            | $L(p)=\binom{n}{x}p^x(1-p)^{n-x}$                                                      | $\binom{3}{3}p^3(1-p)^0=p^3$             |
| **Posterior**             | $p\mid\mathrm{data}\sim\mathrm{Beta}(a+x,b+n-x)$                                     | $\mathrm{Beta}(1+3,1+0)=\mathrm{Beta}(4,1)$ |
| **Posterior mean**        | $\mathbb{E}[p\mid\mathrm{data}]=\frac{a+x}{a+b+n}$                       | $\frac{4}{5}=0.8$                       |
| **95 % credible interval** | Central interval between the 0.025 and 0.975 quantiles of $\mathrm{Beta}(4,1)$         | $\approx[0.50,0.97]$                  |

### Bayesian vs Frequentist Convergence

As the sample size increases, Bayesian and frequentist methods often produce similar numerical results—*provided the prior is non-informative or weakly informative*. When using uninformed or non-informative priors (indicating a lack of strong prior knowledge), the results from Bayesian and frequentist approaches are frequently comparable, if not identical. However, the **interpretation** of these results can still differ between the two frameworks: a frequentist 95 % confidence interval has 95 % coverage in repeated sampling, whereas a Bayesian 95 % credible interval contains the parameter with 95 % posterior probability.

#### When Do They Diverge?

- In cases involving complex models or smaller sample sizes, Bayesian and frequentist methods may produce significantly different outcomes. Bayesian approaches may perform better in these scenarios because they can incorporate prior information, which helps when data are limited or the model is sophisticated.  
- The specific context of the problem—such as the presence of strong prior information or a complicated data structure—can also lead to divergence between the two methods. Bayesian methods might yield more nuanced results in certain situations where frequentist methods may struggle.

#### Example: Frequentist vs. Bayesian Mean Estimation

1. We generated synthetic data consisting of 100 random values drawn from a normal distribution with a mean of 5 and a standard deviation of 2. This dataset simulates real-world measurements with inherent variability around the central value of 5. The goal was to compare how the frequentist and Bayesian approaches estimate the mean and uncertainty of this data.  
2. Using the **frequentist approach**, we calculated the sample mean and constructed a 95 % confidence interval (CI). The mean came out to be approximately 4.79, and the confidence interval was between 4.44 and 5.15. This interval suggests that, if we repeated this experiment many times, 95 % of the calculated intervals would contain the true population mean.  
3. In the **Bayesian approach**, we incorporated prior knowledge about the data by assuming a prior mean of 5 and a prior variance of 1. Combining this prior belief with the observed data, we calculated a posterior mean of 4.80. The 95 % credible interval, which reflects where the true mean is likely to lie *given both the prior and observed data*, ranged from 4.42 to 5.18. This interval accounts for both the prior information and the variability in the data.  

![output(11)](https://github.com/user-attachments/assets/4ba1be0a-21d3-4627-ad7e-f357f5453487)

The analysis results are as follows:

- **Frequentist Mean:** 4.79, with a 95 % confidence interval of (4.44, 5.15).  
- **Bayesian Mean:** 4.80, with a 95 % credible interval of (4.42, 5.18).  
