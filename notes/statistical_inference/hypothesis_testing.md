## Hypothesis Testing

A hypothesis is a statement that might be true.

Hypothesis testing is a key tool in the field of statistics and forms the backbone of scientific research. It helps us make decisions about population parameters using sample data. Hypothesis testing is used across a wide variety of fields - from testing the effectiveness of a new drug in medical trials, to understanding customer behavior in business analytics.

### Inputs and Outputs of Hypothesis Testing

The primary inputs to a hypothesis test are the null and alternative hypotheses, the significance level, and the sample data. 

* Alternative Hypothesis (H1): the claim we are testing.

* Null Hypothesis (H0): The opposite of the claim we are testing. It is also status quo, something we would assume is the case without any additional evidences.

* Significance Level (α): This is the threshold below which we will reject the null hypothesis. Often set at 0.05, it denotes a 5% risk of concluding that an effect exists when it does not.

* Sample data: This is the data collected from your study or experiment. The data is used to calculate a test statistic, which in turn gives us a p-value.

The primary output of a hypothesis test is the p-value. This is the probability that we would see the observed data, or something more extreme, assuming the null hypothesis is true.

### An Overview of Hypothesis Testing Steps

The goal is to determine wheter we have enough evidence to reject the Null hypothesis.

1. Formulate the Null and Alternative Hypotheses: This involves defining the population parameters and stating the null and alternative hypotheses in context of the question being addressed.

2. Choose a Significance Level: This is typically set to α = 0.05. However, it can be adjusted depending on the field of study or the specific experiment.

3. Data Collection: This involves gathering data in a methodologically sound way to ensure the results are representative and unbiased.

4. Calculate Test Statistic: This involves calculating a test statistic that is appropriate for the type of data and the specific hypothesis being tested. The test statistic is a function of the sample data.

5. Determine the P-Value: This is the probability of obtaining a test statistic as extreme as, or more extreme than, the observed test statistic under the null hypothesis.

6. Make a Decision: If the p-value is less than the chosen significance level (α), we reject the null hypothesis in favor of the alternative. If not, we fail to reject the null hypothesis.

7. Interpret the Results: Finally, we interpret the result of the hypothesis test in the context of the question being studied. Remember, failing to reject the null hypothesis doesn't prove it's true. It simply means that the data does not provide strong enough evidence against it.

## Example: Marbe Bags
Consider two identical bags, each containing 10 marbles. Bag A contains 5 white and 5 black marbles. Bag B contains only black marbles.

```
  Bag A            Bag B
  _____            _____
 / • •  \         / O O  \
|  • •  |        |  O O  |    O = White Marble
|  O O  |        |  O O  |    • = Black Marble
|  O O  |        |  O O  |    
|  • O  |        |  O O  |
 \_____/          \_____/
```

You are handed one of these bags and suspect it is Bag B.

- Null Hypothesis ($H_0$): Your bag is Bag A
- Alternative Hypothesis ($H_a$): Your bag is Bag B

To test this hypothesis, you draw n marbles from your bag. They are all black. How strong is this evidence that your bag is Bag B? Test this for n=2,3,5 marbles.

To solve this, we can use the concept of the p-value, which is the probability of obtaining the observed results, or more extreme, given that the null hypothesis is true.

For Bag A (the null hypothesis), the probability of drawing a black marble is 0.5. The probability of drawing `n` black marbles in a row from Bag A is (0.5)^n.

- For n=2, the probability (p-value) is (0.5)^2 = 0.25.
- For n=3, the probability (p-value) is (0.5)^3 = 0.125.
- For n=5, the probability (p-value) is (0.5)^5 = 0.03125.

The smaller the p-value, the stronger the evidence against the null hypothesis. In this case, as `n` increases, the evidence that your bag is Bag B (containing only black marbles) becomes stronger.

## Choosing the Right Statistical Test

Selecting an appropriate statistical test for your data is a crucial part of hypothesis testing. The choice depends on several factors:

* **Type of Data**: The nature of your data (categorical, ordinal, interval, or ratio) can influence your choice of test. 

* **Number of Variables**: The number of variables you are analyzing affects the choice of test. There are tests designed for one variable (univariate), two variables (bivariate), or more than two variables (multivariate).

* **Distribution of the Data**: Some tests (parametric tests) assume that your data follows a certain distribution, typically a normal distribution. If your data doesn't meet this assumption, you may need to choose a non-parametric test.

* **Study Design**: The design of your study, such as whether you are comparing two groups or measuring one group at different times, can influence your test choice.

For instance, a t-test is a parametric test used when you want to compare the means of two groups and you have interval or ratio data. If your data is not normally distributed, or if you're working with ordinal data, you might choose a non-parametric equivalent, like the Mann-Whitney U test.

In a different scenario, if you wanted to compare the means of more than two groups, an Analysis of Variance (ANOVA) test would be appropriate. For categorical data, a chi-square test would be a good choice to test for differences in proportions.

This table covers some of the most common tests:

| Test                     | Data Type           | Number of Groups | Assumptions                                        |
|--------------------------|---------------------|------------------|----------------------------------------------------|
| T-Test                   | Interval/Ratio      | Two              | Normally distributed, independent samples          |
| Paired T-Test            | Interval/Ratio      | Two              | Normally distributed, dependent samples            |
| One-way ANOVA            | Interval/Ratio      | More than Two    | Normally distributed, independent samples          |
| Two-way ANOVA            | Interval/Ratio      | More than Two    | Normally distributed, independent samples          |
| Chi-Square Test          | Categorical         | Two or more      | Independence between variables                     |
| Pearson Correlation      | Interval/Ratio      | Two              | Normally distributed, linear relationship          |
| Spearman Correlation     | Ordinal             | Two              | Non-parametric, monotonic relationship             |
| Mann-Whitney U Test      | Ordinal/Continuous  | Two              | Non-parametric, independent samples                |
| Kruskal-Wallis H Test    | Ordinal/Continuous  | More than Two    | Non-parametric, independent samples                |
| Wilcoxon Signed-Rank Test| Ordinal/Continuous  | Two              | Non-parametric, dependent samples                  |
| Friedman Test            | Ordinal/Continuous  | More than Two    | Non-parametric, dependent samples                  |

### Example: One-Sample T-Test

Suppose we want to test if the average height of adult males in a city is different from the known national average. 

* Null Hypothesis (H0): The average height of adult males in the city is equal to the national average.
* Alternative Hypothesis (H1): The average height of adult males in the city is different from the national average.

After gathering a representative sample of adult males in the city, we calculate the sample mean and sample standard deviation. These, along with the sample size, are used to compute the test statistic. The p-value is then calculated from the test statistic using the t-distribution. If the p-value is less than our pre-defined significance level, we reject the null hypothesis, concluding that the average height of adult males in the city is different from the national average.
