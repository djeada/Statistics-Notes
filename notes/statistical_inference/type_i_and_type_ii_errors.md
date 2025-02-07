## Errors in Hypothesis Testing

Hypothesis testing is a core concept in statistics that allows researchers to evaluate assumptions about a population by examining sample data. In this process, we start with a null hypothesis, denoted by $H_0$, which represents a baseline or default position, and an alternative hypothesis, $H_a$, which challenges that assumption. Even with careful planning, the process is prone to mistakes, and understanding these potential missteps is necessary for drawing reliable conclusions. Two main errors, known as Type I and Type II errors, can occur, and balancing these is key to designing strong experiments and interpreting results correctly.

### Overview of Hypothesis Testing Errors

When performing hypothesis tests, our decisions are influenced by thresholds such as the significance level. A helpful way to summarize the possible outcomes is to consider the following table, which shows how decisions interact with the true state of nature:

|                          | Reject $H_0$ (Accept $H_a$)            | Fail to Reject $H_0$ (Insufficient Evidence for $H_a$) |
|--------------------------|:---------------------------------------:|:----------------------------------------------------------:|
| $H_0$ is True          | Type I Error                          | Correct Decision                                           |
| $H_0$ is False         | Correct Decision                      | Type II Error                                            |

This table highlights that if the null hypothesis is true and we mistakenly reject it, we incur a Type I error, while failing to reject a false null hypothesis results in a Type II error. Each of these outcomes carries its own implications for research findings and subsequent decisions.

### The Court Trial Analogy

A vivid way to understand these errors is by considering the analogy of a court trial. Imagine that the null hypothesis is the assertion that a suspect is innocent, and the alternative hypothesis is that the suspect is guilty. In this scenario, a conviction corresponds to rejecting the null hypothesis, whereas an acquittal means failing to reject it. If the court convicts an innocent person, it commits a Type I error, much like a false positive in statistics. Conversely, if a guilty person is acquitted because the evidence was insufficient, that mirrors a Type II error, or a false negative. This analogy serves to illustrate how statistical decisions can have real-world consequences, emphasizing the importance of carefully weighing the risks associated with each type of error.

### Understanding Type I Error (False Positive)

A Type I error occurs when we reject a true null hypothesis, resulting in what is commonly known as a false positive. The probability of committing this error is symbolized by $\alpha$, which is also referred to as the significance level of the test. For instance, if $\alpha$ is set to 0.05, there is a 5% chance of incorrectly rejecting $H_0$ even when it is true. 

Consider a scenario in which researchers are testing the effectiveness of a new drug; if the analysis erroneously concludes that the drug is effective when it is not, the study has committed a Type I error.

The following diagram offers a visual representation of this concept. In the diagram, the bell-shaped curve represents the distribution of the test statistic under the null hypothesis, and the important region (corresponding to the significance level) is marked to indicate the area where data would lead to a rejection of $H_0$:

```
         Important Region (α)
                │
                ▼
         _______________
        /               \
       /                 \
      |   True Null       |   ← Distribution under $H_0$
      |   ($μ_0$)       |
       \                 /
        \_______________/
```

The diagram shows that even if the data comes from a distribution where the null hypothesis holds true (centered at $μ_0$), random variations might produce a result that falls within the important region, leading to a false positive decision.

![type_i_error](https://github.com/djeada/Statistics-Notes/assets/37275728/cf55385c-a4b9-4d56-9a70-52b0da6fe106)

Here, both the control and experimental groups have the same mean (100), representing the scenario where the null hypothesis is true (there is no actual difference between the groups). The dashed lines show the means of each group. The p-value indicates the probability of observing the data assuming the null hypothesis is true. A small p-value (typically less than 0.05) would lead to incorrectly rejecting a true null hypothesis, which is a Type I error. In this specific run, whether a Type I error occurs depends on the randomly generated data and the chosen alpha level.

### Understanding Type II Error (False Negative)

A Type II error happens when we fail to reject a false null hypothesis, resulting in a false negative. 

This error is represented by the symbol $\beta$, and its probability can be influenced by factors such as sample size and effect size. The ability of a test to correctly detect an effect when one exists is measured by the test’s power, defined mathematically as $1 - \beta$. 

For example, if a drug is genuinely effective but the study does not detect this effect—perhaps due to an insufficient sample size—the result is a Type II error.

The following diagram provides an illustration of how a Type II error can occur. In this diagram, two overlapping distributions are depicted: one for the null hypothesis (centered at $μ_0$) and one for the alternative hypothesis (centered at $μ_1$). The important threshold is set based on the $H_0$ distribution, and if the true effect does not push the observed value beyond this threshold, the test fails to reject $H_0$, thereby committing a Type II error:

```
              H0 Distribution              H1 Distribution
             (Centered at $μ_0$)          (Centered at $μ_1$)
                    ____                         ____
                   /    \                       /    \
                  /      \                     /      \
                 |  $μ_0$ |                   |  $μ_1$ |
                  \      /                     \      /
                   \____/                       \____/
                       │
                       ▼  (Important Threshold)
          Failure to reject $H_0$ leads to a Type II error
```

This visualization underscores the challenge of distinguishing between a true absence of effect and a failure to detect a real effect due to limitations in the study design or data variability.

![type_ii_error](https://github.com/djeada/Statistics-Notes/assets/37275728/f511bccb-4126-484f-9e44-143e3e4cad1a)

For this plot, the mean of the experimental group is shifted to 110, while the control group remains the same. This setup simulates a scenario where the null hypothesis is false (there is a real difference). If the statistical test fails to detect this difference (i.e., we do not reject the null hypothesis when we should), it results in a Type II error. Again, the occurrence of a Type II error depends on the data and the sensitivity of the test (which can be influenced by sample size, effect size, and chosen alpha level).

### Balancing Type I and Type II Errors

The relationship between Type I and Type II errors is inherently a balancing act. Lowering the significance level $\alpha$ reduces the risk of committing a Type I error; however, this typically comes at the expense of increasing $\beta$, which is the probability of a Type II error. In other words, a more conservative test that minimizes false positives may inadvertently miss true effects. The power of the test, defined as $1 - \beta$, captures the test’s ability to correctly identify real differences or effects. Enhancing the power may involve increasing the sample size or improving the measurement precision, both of which help reduce the likelihood of a Type II error.

Mathematically, these relationships are expressed as follows:

$$P(\text{Type I Error}) = \alpha$$

$$P(\text{Type II Error}) = \beta$$

$$\text{Power} = 1 - \beta$$

These formulas provide a clear framework for understanding the trade-offs inherent in hypothesis testing. Researchers must carefully consider these relationships when designing studies, as the optimal balance depends on the context and the consequences of making either type of error.
