# Chi-Square Tests and Categorical Data Analysis

The **chi-square ($\chi^2$) test** is a family of statistical tests for categorical count data. These tests compare observed frequencies with the frequencies expected under a null hypothesis.

A large difference between observed and expected counts provides evidence that the null hypothesis may not adequately explain the data.

Types of Chi-Square Tests:

1. The **goodness-of-fit test** determines whether the distribution of one categorical variable follows a specified distribution.
2. The **test of homogeneity** assesses whether several populations or groups have the same distribution of a categorical variable.
3. The **test of independence** evaluates whether two categorical variables are associated within a population.

Although these tests address different questions, they use the same basic idea:

```math
\chi^2
=
\sum
\frac{(\text{Observed}-\text{Expected})^2}
{\text{Expected}}.
```

## Categorical Data

**Categorical data** consist of observations classified into groups or categories rather than measured on a numerical scale.

Categorical variables may be:

* **nominal**, where categories have no natural ordering, or
* **ordinal**, where categories have a meaningful ordering.

For a single categorical variable, each observation belongs to one category. When several categorical variables are recorded, each observation belongs to one category for each variable.

For example, consider Titanic passengers classified by survival status and ticket class:

* **Survival status**: Survived or Died.
* **Ticket class**: First Class, Second Class, Third Class, or Crew.

Each passenger has one survival status and one ticket-class category.

## Contingency Tables

A **contingency table**, also called a cross-tabulation or crosstab, summarizes counts for combinations of categorical variables.

For example, Titanic survival data can be represented in a $2\times4$ contingency table:

|              | First Class | Second Class | Third Class | Crew | **Total** |
| ------------ | ----------: | -----------: | ----------: | ---: | --------: |
| **Survived** |         $a$ |          $b$ |         $c$ |  $d$ |       $S$ |
| **Died**     |         $e$ |          $f$ |         $g$ |  $h$ |       $D$ |
| **Total**    |         325 |          285 |         706 |  885 |     2,201 |

Here, $a$ through $h$ represent the observed counts in each cell.

The row and column totals are called **marginal totals**. They are used to calculate expected counts in tests of homogeneity and independence.

## 1. Testing Goodness-of-Fit

A chi-square goodness-of-fit test compares observed counts for one categorical variable with the counts expected under a specified distribution.

### Hypotheses

* The **null hypothesis ($H_0$)** states that the population follows the specified categorical distribution.
* The **alternative hypothesis ($H_A$)** states that the population distribution differs from the specified distribution in at least one category.

The observed and expected counts do not need to match exactly under $H_0$; some difference is expected because of sampling variation.

### Example: M&M Color Distribution

Suppose we want to compare an M&M color sample with the six reference proportions below, labeled as a 2008 distribution in this teaching example. Treat these numbers as the specified null model. They should not be assumed to describe current products, all factories, or every product type.

**2008 Expected Color Distribution**:

| Color  | Percentage (%) |
| ------ | -------------: |
| Blue   |             24 |
| Orange |             20 |
| Green  |             16 |
| Yellow |             14 |
| Red    |             13 |
| Brown  |             13 |

**Observed Counts**: From a sample of 410 M&Ms:

| Color  | Count |
| ------ | ----: |
| Blue   |   105 |
| Orange |    91 |
| Green  |    70 |
| Yellow |    50 |
| Red    |    45 |
| Brown  |    49 |

The hypotheses are:

```math
H_0:
(p_{\text{blue}},p_{\text{orange}},p_{\text{green}},
p_{\text{yellow}},p_{\text{red}},p_{\text{brown}})
=
(0.24,0.20,0.16,0.14,0.13,0.13)
```

versus the alternative that at least one population proportion differs.

### Calculating Expected Counts

For each category, the expected count is:

```math
E_i=Np_i
```

where:

* $N$ is the total sample size,
* $p_i$ is the expected proportion for category $i$.

For blue M&Ms:

```math
E_{\text{blue}}
=
410(0.24)
=
98.4.
```

The complete expected counts are:

| Color  | Observed $O_i$ | Expected $E_i$ |
| ------ | -------------: | -------------: |
| Blue   |            105 |           98.4 |
| Orange |             91 |           82.0 |
| Green  |             70 |           65.6 |
| Yellow |             50 |           57.4 |
| Red    |             45 |           53.3 |
| Brown  |             49 |           53.3 |

The expected counts also sum to 410.

### Computing the Chi-Square Statistic

The goodness-of-fit statistic is:

```math
\chi^2
=
\sum_{i=1}^{k}
\frac{(O_i-E_i)^2}{E_i}
```

where:

* $O_i$ is the observed count,
* $E_i$ is the expected count,
* $k$ is the number of categories.

For these data the six terms are $0.44,\,0.99,\,0.30,\,0.95,\,1.29,\,0.35$, so:

```math
\chi^2\approx4.32.
```

Each term measures the difference between an observed count and its expected value. Larger differences contribute more to the total statistic.

### Degrees of Freedom

When all expected proportions are specified in advance (none are estimated from the data):

```math
df=k-1.
```

In a regular multinomial model with $m$ identifiable parameters estimated efficiently from the same category counts, the usual asymptotic adjustment is $k-1-m$. Additional constraints, boundary parameters, or a different estimation scheme can require another calibration. Here no probabilities are estimated from the sample, so for six colors:

```math
df=6-1=5.
```

### Decision Rule

Suppose the significance level is:

```math
\alpha=0.05.
```

Using the chi-square distribution with $df=5$, the critical value is approximately:

```math
\chi^2_{0.95,5}\approx11.07.
```

Large values of $\chi^2$ indicate poor agreement with $H_0$, so the test is right-tailed. Reject $H_0$ if:

```math
\chi^2_{\text{observed}}>11.07.
```

Equivalently, using a p-value, reject $H_0$ when:

```math
p\le\alpha.
```

### Interpretation

For this example:

* **Chi-square statistic**: 4.32
* **p-value**: approximately 0.5045
* **Critical value**: approximately 11.07
* **Decision**: Fail to reject $H_0$

Because the p-value is greater than 0.05, the sample does not provide sufficient evidence that the color distribution differs from the specified 2008 proportions.

Failing to reject $H_0$ does not prove that the distribution is unchanged. It means that the observed differences are not large enough to provide evidence against the specified distribution at the chosen significance level.

### Visualization

![Figure for Visualization](https://github.com/user-attachments/assets/fc347693-1fbb-468a-bfac-0ac9e0ce5095)

Analysis Results:

* **Chi-square statistic**: 4.32
* **p-value**: 0.5045
* **Critical value**: 11.07
* **Decision**: Fail to reject the null hypothesis.

Based on this sample, there is insufficient evidence to conclude that the M&M color distribution differs from the specified 2008 distribution.

The terms can be written as squared Pearson residuals, $r_i=(O_i-E_i)/\sqrt{E_i}$. This scaling matters: a discrepancy of ten is more striking against an expectation of five than against an expectation of a thousand. Squaring removes direction, so the total statistic detects departures but does not say which categories are enriched or depleted. Inspecting individual residuals can explain the departure, while formal follow-up tests introduce additional multiplicity.

## 2. Testing Homogeneity

A chi-square test of homogeneity compares the distribution of a categorical variable across several populations or groups.

### Hypotheses

* **Null Hypothesis ($H_0$)**: The categorical variable has the same distribution in all populations or groups.
* **Alternative Hypothesis ($H_A$)**: At least one population or group has a different distribution.

### Example: Titanic Survival by Ticket Class

Suppose we want to test whether survival rates are the same across Titanic ticket classes.

**Data Summary**:

|              | Survived |  Died | **Total** |
| ------------ | -------: | ----: | --------: |
| First Class  |      203 |   122 |       325 |
| Second Class |      118 |   167 |       285 |
| Third Class  |      178 |   528 |       706 |
| Crew         |      212 |   673 |       885 |
| **Total**    |      711 | 1,490 |     2,201 |

The null hypothesis is that the survival distribution is the same across all four groups.

### Calculating Expected Counts

If the survival distribution were the same across groups, the expected count in cell $(i,j)$ would be:

```math
E_{ij}
=
\frac{
(\text{Row Total}_i)
(\text{Column Total}_j)
}{
\text{Grand Total}
}.
```

For First Class survivors:

```math
E_{11}
=
\frac{325(711)}{2201}
\approx104.99.
```

The observed number of First Class survivors is 203, which is much larger than this expected count.

The expected-count formula follows from fitting a common survival probability, $\hat p=711/2201$. Multiplying $\hat p$ by the First Class total gives $325\hat p\approx104.99$. In an independence formulation the fitted joint cell probability is the product of the empirical row and column proportions, giving the same formula. These expectations are fitted null values, not a claim that every cell should equal its expectation exactly.

### Computing the Chi-Square Statistic

The statistic is:

```math
\chi^2
=
\sum_{i=1}^{r}
\sum_{j=1}^{c}
\frac{(O_{ij}-E_{ij})^2}{E_{ij}}.
```

Here:

* $r=4$ groups,
* $c=2$ survival outcomes.

Summing across all eight cells gives:

```math
\chi^2\approx190.40.
```

### Degrees of Freedom

For a contingency table:

```math
df=(r-1)(c-1).
```

Therefore:

```math
df
=
(4-1)(2-1)
=
3.
```

### Decision Rule

At:

```math
\alpha=0.05,
```

the critical value for $df=3$ is approximately:

```math
\chi^2_{0.95,3}=7.81.
```

Because:

```math
190.40>7.81,
```

we reject the null hypothesis.

The p-value is also extremely small:

```math
p\approx5.0\times10^{-41}.
```

### Interpretation

The data provide very strong evidence that survival rates were not the same across the four Titanic groups.

In other words, survival and ticket-class group are associated in these data. The chi-square test does not explain why the groups differ.

The historical table is close to a census of the recorded people on that voyage, rather than a random sample of independent voyages. Its association can be described directly: survival fractions are about 62.5%, 41.4%, 25.2%, and 24.0% for the four rows. A superpopulation interpretation of the tiny p-value requires an additional model, and shared family or evacuation circumstances can violate simple individual independence. The table also cannot isolate a causal effect of ticket class from age, sex, location, or other factors.

### Visualization

![Figure for Visualization](https://github.com/user-attachments/assets/443f3e86-d52a-46b0-b427-5d12a7561a0a)

Analysis Results:

* **Chi-square statistic**: 190.40
* **p-value**: approximately $5.0\times10^{-41}$
* **Critical value**: 7.81
* **Decision**: Reject the null hypothesis.

The data provide strong evidence that survival rates differed among First Class, Second Class, Third Class, and Crew.

## 3. Testing Independence

A chi-square test of independence examines whether two categorical variables are associated within a population.

### Hypotheses

* The **null hypothesis ($H_0$)** states that the two categorical variables are independent.
* The **alternative hypothesis ($H_A$)** states that the variables are associated.

If two variables are independent, knowing the value of one does not change the distribution of the other.

### Example: Gender and Voting Preference

Suppose we survey individuals to investigate whether gender is associated with voting preference.

**Data Summary**:

|           | Liberal | Conservative | **Total** |
| --------- | ------: | -----------: | --------: |
| Male      |      40 |           60 |       100 |
| Female    |      70 |           30 |       100 |
| **Total** |     110 |           90 |       200 |

If the variables were independent, both gender groups would have the same voting-preference distribution apart from sampling variation.

### Calculating Expected Counts

Under independence:

```math
E_{ij}
=
\frac{
(\text{Row Total}_i)
(\text{Column Total}_j)
}{
\text{Grand Total}
}.
```

For Male/Liberal:

```math
E_{11}
=
\frac{100(110)}{200}
=
55.
```

The expected counts are therefore:

|        | Liberal | Conservative |
| ------ | ------: | -----------: |
| Male   |      55 |           45 |
| Female |      55 |           45 |

### Computing the Chi-Square Statistic

The Pearson chi-square statistic is:

```math
\chi^2
=
\sum_{i=1}^{2}
\sum_{j=1}^{2}
\frac{(O_{ij}-E_{ij})^2}{E_{ij}}.
```

For these data:

```math
\chi^2\approx18.18.
```

### Degrees of Freedom

```math
df
=
(2-1)(2-1)
=
1.
```

### Yates' Correction for Continuity (Optional)

For a $2\times2$ table, Yates' continuity correction may be applied:

```math
\chi^2_{\text{Yates}}
=
\sum
\frac{\left[\max\{0,|O_{ij}-E_{ij}|-0.5\}\right]^2}{E_{ij}}.
```

For these data:

```math
\chi^2_{\text{Yates}}
\approx16.99.
```

with:

```math
p\approx3.76\times10^{-5}.
```

Without the correction, the Pearson test gives:

```math
\chi^2\approx18.18,
\qquad
p\approx2.01\times10^{-5}.
```

Both lead to the same conclusion.

### Decision Rule

At:

```math
\alpha=0.05,
```

the chi-square critical value with one degree of freedom is approximately:

```math
3.84.
```

Using either statistic:

```math
\chi^2>3.84,
```

so we reject $H_0$.

### Interpretation

The data provide strong evidence of an association between gender and voting preference in the sampled population.

This indicates association, not necessarily causation.

### Visualization

![Figure for Visualization](https://github.com/user-attachments/assets/3465e92f-5782-4e2f-a73b-08c1077054f5)

Analysis Results:

Using Yates' continuity correction:

* **Chi-square statistic**: 16.99
* **p-value**: $3.76\times10^{-5}$
* **Critical value**: 3.84
* **Decision**: Reject the null hypothesis.

There is strong evidence of an association between gender and voting preference in the observed data.

## Comparing Homogeneity and Independence Tests

The chi-square tests of homogeneity and independence use the same test statistic and expected-count formula. Their main difference lies in the research question and how the data are collected.

### Chi-Square Test of Homogeneity

* The **objective** is to determine whether several populations or groups have the same distribution of a categorical variable.
* The **data structure** typically involves separate samples or predefined groups.
* An **example** is comparing the distribution of M&M colors across different product types, such as milk chocolate, peanut, and caramel.

### Chi-Square Test of Independence

* The **objective** is to determine whether two categorical variables are associated within a population.
* The **data structure** typically consists of one sample in which each observation is classified by both variables.
* An **example** is examining the relationship between gender and voting preference in a survey.

### Key Differences

The **population structure** differs:

* In a **homogeneity test**, distributions are compared across populations or groups.
* In an **independence test**, two variables are studied within one population.

The **research question** also differs:

* A **homogeneity test** asks whether the distribution of a categorical variable is the same across groups.
* An **independence test** asks whether two categorical variables are associated.

The calculations are otherwise essentially the same once the contingency table has been constructed.

The degrees of freedom also have a useful counting interpretation. An $r\times c$ table has $rc-1$ free proportions after its total is fixed. The independence model uses $(r-1)+(c-1)$ free marginal parameters. Subtracting gives $(rc-1)-(r+c-2)=(r-1)(c-1)$. For independent samples within fixed groups, the homogeneity model leads to the same remaining number of distributional contrasts.

## Assumptions and Conditions

For chi-square tests to be valid, several conditions should be checked:

1. **The data are counts.** The test is applied to observed frequencies in categories.

2. **Categories are mutually exclusive.** Each observation contributes to one relevant category or table cell.

3. **The underlying observational units follow the assumed sampling model.** Counts in a multinomial table are dependent because they sum to a fixed total; that is already part of the test. The independence requirement concerns the sampled people, rolls, or items, not independence of the cell counts. Repeated responses by the same person or clustered sampling can require a different method.

4. **The sampling design should support the intended inference.**

5. **Expected counts should not be too small.** A common rule of thumb is that expected counts should generally be at least 5.

These conditions help ensure that the chi-square distribution provides a reasonable approximation to the sampling distribution of the test statistic.

## Practical Application Steps

1. **State the hypotheses** and identify the appropriate chi-square test.
2. **Organize the observed counts** into a frequency table or contingency table.
3. **Calculate the expected counts** under the null hypothesis.
4. **Check the assumptions**, especially independence and expected counts.
5. **Compute the chi-square statistic**:

```math
\chi^2
=
\sum\frac{(O-E)^2}{E}.
```

6. **Determine the degrees of freedom**.
7. **Find the p-value or critical value** using the appropriate chi-square distribution.
8. **Make a decision** by comparing the p-value with $\alpha$, or the test statistic with the critical value.
9. **Interpret the result** in the context of the research question.

A chi-square test tells us whether the observed differences are larger than would reasonably be expected under the null hypothesis. It does not, by itself, explain why an association exists or establish causation.


For sparse tables, a chi-square approximation may be inaccurate even when the total sample is large. An exact or Monte Carlo procedure can be preferable when justified by the sampling design. Combining categories merely to meet a count threshold changes the question and should be scientifically defensible. Structural zeros also require special handling: a combination that cannot occur is not an ordinary sampling zero, and its restriction changes the model and potentially the degrees of freedom.
