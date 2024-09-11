#### Categorical Data and Contingency Tables
- **Categorical Data**: Involves data counts in fixed categories, like survival rates by ticket class on the Titanic.
    - Example: Titanic survival data can be organized into a 2x4 contingency table (2 categories: "Survived" and "Died," across 4 ticket classes: First, Second, Third, Crew).
  
- **Contingency Table**: A table that displays the frequency counts of categorical data, often used to analyze relationships between two or more categories.

#### Chi-Square Tests: Overview
Chi-square (\( \chi^2 \)) tests are used to analyze categorical data and test hypotheses about how well observed data fit expected distributions. There are three main types of chi-square tests:
1. **Goodness-of-fit**: Tests whether an observed distribution matches a known distribution.
2. **Homogeneity**: Tests whether several populations share the same distribution of a categorical variable.
3. **Independence**: Tests whether two categorical variables are independent.

---

#### 1. Testing Goodness-of-Fit
- **Example**: M&M color distribution (2008 vs. recent observations).
    - **Null Hypothesis (H0)**: The color distribution of M&Ms has not changed since 2008.
    - **Alternative Hypothesis (HA)**: The color distribution has changed.
  
- **Method**: Compare observed counts to expected counts under H0. The chi-square statistic (\( \chi^2 \)) is calculated as:
  \[
  \chi^2 = \sum \frac{(\text{observed} - \text{expected})^2}{\text{expected}}
  \]
    - Example: For 410 M&Ms in total, we expect 98.4 blue M&Ms based on the 2008 distribution (24%). The chi-square statistic measures the difference across all colors.
  
- **Degrees of Freedom (df)**: For goodness-of-fit, df = number of categories - 1.
    - In this example, df = 6 - 1 = 5.
  
- **Chi-Square Test Result**: Large values of \( \chi^2 \) indicate evidence against H0, and the p-value is used to determine statistical significance.

---

#### 2. Testing Homogeneity
- **Example**: Titanic survival by ticket class.
    - **Null Hypothesis (H0)**: The probability of survival is the same for all ticket classes.
    - **Alternative Hypothesis (HA)**: The survival probability differs across ticket classes.
  
- **Method**: Pool the data to estimate the overall survival probability and calculate expected counts for each category (e.g., 32% of passengers survived, so expected survivors in First Class = 32% × 325).
  
- **Chi-Square Statistic**: Calculated across all cells in the contingency table:
  \[
  \chi^2 = \sum \frac{(\text{observed} - \text{expected})^2}{\text{expected}}
  \]
  
- **Degrees of Freedom (df)**: For homogeneity tests, df = (number of rows - 1) × (number of columns - 1).
    - Example: df = (4 - 1) × (2 - 1) = 3.
  
- **Interpretation**: Large values of \( \chi^2 \) indicate that survival probability differs across ticket classes.

---

#### 3. Testing Independence
- **Example**: Relationship between gender and voting preference.
    - **Null Hypothesis (H0)**: Gender and voting preference are independent.
    - **Alternative Hypothesis (HA)**: There is an association between gender and voting preference.
  
- **Method**: Record counts in a 2x2 table for gender (male/female) and voting preference (liberal/conservative). Calculate the chi-square statistic using the same formula as in the homogeneity test.
  
- **Degrees of Freedom (df)**: For independence tests, df = (number of rows - 1) × (number of columns - 1).
    - In a 2x2 table, df = (2 - 1) × (2 - 1) = 1.
  
- **Interpretation**: If the p-value is low, we reject H0 and conclude that gender and voting preference are associated.

---

#### Comparing Homogeneity and Independence Tests
- **Chi-square test of homogeneity**: Compares the distribution of one categorical variable across different samples or populations.
    - Example: Do M&M colors have the same distribution for milk, peanut, and caramel M&Ms?

- **Chi-square test of independence**: Examines whether two categorical variables are related within the same sample.
    - Example: Is there an association between gender and voting preference?

Both tests use the same chi-square statistic but address different research questions.

