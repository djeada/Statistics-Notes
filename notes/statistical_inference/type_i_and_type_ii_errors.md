## Errors in Hypothesis Testing

When conducting hypothesis tests, we face two main types of errors: Type I and Type II errors. These errors are critical to understand for accurate interpretation of test results and informed decision-making.

### Type I and Type II Errors

|                     | Reject $H_0$ (Accept $H_a$) | Fail to Reject $H_0$ (Insufficient Evidence for $H_a$) |
|---------------------|:---------------------:|:-----------------------------------------------:|
| **$H_0$ is True**      | Type I Error          | Correct Decision                                |
| **$H_0$ is False**     | Correct Decision      | Type II Error                                   |

#### Example: Court Trial Hypotheses
- **Null Hypothesis ($H_0$):** The suspect is innocent.
- **Alternative Hypothesis ($H_a$):** The suspect is guilty.

**Type I Error:** Convicting an innocent person.
**Type II Error:** Acquitting a guilty person.

### Type I Error (False Positive)
- **Symbol:** $\alpha$ (alpha)
- **Description:** Rejecting a true $H_0$, implying a false detection of an effect.
- **Probability:** Corresponds to the test's significance level. For a 0.05 level, there's a 5% chance of a Type I error.
- **Example:** In a drug trial, erroneously concluding a new drug is effective when it isn't.

### Type II Error (False Negative)
- **Symbol:** $\beta$ (beta)
- **Description:** Failing to reject a false $H_0$, missing a real effect.
- **Power of a Test:** (1 - $\beta$), representing the test's ability to correctly reject a false $H_0$.
- **Example:** Missing the effectiveness of a new drug due to inadequate trial results.

### Balancing Type I and Type II Errors
- **Trade-Off:** Decreasing $\alpha$ (Type I errors) typically increases $\beta$ (Type II errors), and vice versa.
- **Power:** High power means less Type II errors, but can increase Type I errors.
- **Context-Specific Balance:** The optimal balance varies depending on the scenario and the consequences of each error type.

In mathematical terms, these relationships can be represented as:

- Probability of Type I Error: $P(\text{Type I Error}) = \alpha$
- Probability of Type II Error: $P(\text{Type II Error}) = \beta$
- Power of the test: $\text{Power} = 1 - \beta$

These relationships highlight the inverse nature of the two errors and the importance of considering both when designing and interpreting hypothesis tests.
