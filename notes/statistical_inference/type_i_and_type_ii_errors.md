## Errors in Hypothesis Testing

When conducting hypothesis tests, we face two main types of errors: Type I and Type II errors. These errors are critical to understand for accurate interpretation of test results and informed decision-making.

### Type I and Type II Errors

|                     | Reject $H_0$ (Accept $H_a$) | Fail to Reject $H_0$ (Insufficient Evidence for $H_a$) |
|---------------------|:---------------------:|:-----------------------------------------------:|
| **$H_0$ is True**      | Type I Error          | Correct Decision                                |
| **$H_0$ is False**     | Correct Decision      | Type II Error                                   |

#### Example: Court Trial Hypotheses

In the realm of hypothesis testing, real-world scenarios can often provide vivid illustrations of abstract concepts. One such scenario is a court trial, where the decision-making process mirrors the principles of statistical hypothesis testing. In this context, the determination of a suspect's guilt or innocence is akin to testing a hypothesis with the potential for two types of errors: Type I and Type II errors. 

- **Null Hypothesis ($H_0$):** The suspect is innocent.
- **Alternative Hypothesis ($H_a$):** The suspect is guilty.

**Type I Error:** Convicting an innocent person.
**Type II Error:** Acquitting a guilty person.

### Type I Error (False Positive)

- **Symbol:** $\alpha$ (alpha)
- **Description:** Rejecting a true $H_0$, implying a false detection of an effect.
- **Probability:** Corresponds to the test's significance level. For a 0.05 level, there's a 5% chance of a Type I error.
- **Example:** In a drug trial, erroneously concluding a new drug is effective when it isn't.

![type_i_error](https://github.com/djeada/Statistics-Notes/assets/37275728/cf55385c-a4b9-4d56-9a70-52b0da6fe106)

Type I Error Illustration: Here, both the control and experimental groups have the same mean (100), representing the scenario where the null hypothesis is true (there is no actual difference between the groups). The dashed lines show the means of each group. The p-value indicates the probability of observing the data assuming the null hypothesis is true. A small p-value (typically less than 0.05) would lead to incorrectly rejecting a true null hypothesis, which is a Type I error. In this specific run, whether a Type I error occurs depends on the randomly generated data and the chosen alpha level.

### Type II Error (False Negative)

- **Symbol:** $\beta$ (beta)
- **Description:** Failing to reject a false $H_0$, missing a real effect.
- **Power of a Test:** (1 - $\beta$), representing the test's ability to correctly reject a false $H_0$.
- **Example:** Missing the effectiveness of a new drug due to inadequate trial results.

![type_ii_error](https://github.com/djeada/Statistics-Notes/assets/37275728/f511bccb-4126-484f-9e44-143e3e4cad1a)

Type II Error Illustration: For this plot, the mean of the experimental group is shifted to 110, while the control group remains the same. This setup simulates a scenario where the null hypothesis is false (there is a real difference). If the statistical test fails to detect this difference (i.e., we do not reject the null hypothesis when we should), it results in a Type II error. Again, the occurrence of a Type II error depends on the data and the sensitivity of the test (which can be influenced by sample size, effect size, and chosen alpha level).

### Balancing Type I and Type II Errors

- **Trade-Off:** Decreasing $\alpha$ (Type I errors) typically increases $\beta$ (Type II errors), and vice versa.
- **Power:** High power means less Type II errors, but can increase Type I errors.
- **Context-Specific Balance:** The optimal balance varies depending on the scenario and the consequences of each error type.

In mathematical terms, these relationships can be represented as:

- Probability of Type I Error: $P(\text{Type I Error}) = \alpha$
- Probability of Type II Error: $P(\text{Type II Error}) = \beta$
- Power of the test: $\text{Power} = 1 - \beta$

These relationships highlight the inverse nature of the two errors and the importance of considering both when designing and interpreting hypothesis tests.
