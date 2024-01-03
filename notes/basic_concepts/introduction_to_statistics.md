# Introduction to Statistics

Statistics is the science of collecting, organizing, analyzing, interpreting, and presenting data. It helps us understand and make informed decisions based on data. In this section, we will introduce essential terms and concepts in statistics and provide a general overview of the subject and its applications.

## Key Terms and Concepts

* **Population:** The complete set of all elements or individuals in a study.


* **Parameter:** A numerical characteristic of a population, such as its mean, median, or standard deviation.

* **Statistic:** A numerical characteristic of a sample, used to estimate a population parameter.

* **Descriptive Statistics:** Techniques for summarizing and describing the main features of a dataset or sample, including measures of central tendency, dispersion, and shape.

* **Inferential Statistics:** Techniques for making generalizations about a population based on a sample. Inferential statistics include hypothesis testing, confidence intervals, and regression analysis.

* **Random Variable:** A variable whose values depend on the outcomes of a random phenomenon.

* **Probability Distribution:** A mathematical function that describes the likelihood of different outcomes for a random variable. Probability distributions can be discrete or continuous.

* **Discrete Distribution:** A probability distribution for a discrete random variable, which can take on a finite or countable number of values.

* **Continuous Distribution:** A probability distribution for a continuous random variable, which can take on an infinite number of values within a specified range.

* **Covariance and Correlation:** Measures that describe the relationship between two variables. Covariance measures the degree to which two variables change together, while correlation measures the strength and direction of a linear relationship between variables.

## Importance of Statistics

Statistics plays a crucial role in various fields, including natural and social sciences, business, finance, and engineering. The importance of statistics stems from its ability to:

1. **Summarize and describe data:** Descriptive statistics help us understand the essential features of a dataset, such as its central tendency, dispersion, and shape.

2. **Make informed decisions:** Inferential statistics enable us to draw conclusions about a population based on sample data, which can guide decision-making in various contexts.

3. **Test hypotheses and make predictions:** Statistical techniques, such as hypothesis testing and regression analysis, allow us to test assumptions, explore relationships between variables, and make predictions.

4. **Quantify uncertainty:** Probability and statistics help us quantify uncertainty, which is essential when making decisions based on incomplete or imperfect information.

## Applications of Statistics

Statistics has numerous applications across various domains, including:

* **Natural and Social Sciences:** Researchers use statistics to design experiments, analyze data, and draw conclusions in fields such as biology, psychology, and sociology.

* **Business and Finance:** Businesses use statistics for market analysis, quality control, financial forecasting, and risk management.

* **Public Policy:** Government agencies rely on statistics to make data-driven decisions, allocate resources, and evaluate the effectiveness of policies and programs.

* **Healthcare and Medicine:** Medical professionals use statistics to analyze clinical trial data, identify risk factors, and evaluate treatment effectiveness.

* **Sports and Gaming:** Coaches and analysts apply statistical techniques to assess player performance, devise game strategies, and make predictions.

* **Machine Learning and Artificial Intelligence:** Machine learning algorithms use statistical techniques to recognize patterns, make predictions, and improve performance based on data.


## Variables and Data

* variables: when we collect data, we make, mesurments, observation. characteristics we choos to measure, observe are called variablse.

* data: the values of variables

* **Sample:** A subset of the population selected for analysis. Samples are used to make inferences about the population.

```
   O   O   O   O   O
  /|\ /|\ /|\ /|\ /|\
  / \ / \ / \ / \ / \
```

Each one of those guy wil have it's own weight, heigh, gender


+-------+--------+--------+--------+
| Name  | Gender | Weight | Height |
+-------+--------+--------+--------+
| Alice | Female |  135   |  5'6"  |
| Bob   |  Male  |  180   |  6'0"  |
| Carol | Female |  140   |  5'5"  |
| David |  Male  |  175   |  5'11" |
| Eve   | Female |  150   |  5'7"  |
+-------+--------+--------+--------+

```
                  All Variables
                   /            \
            Numerical       Categorical
           /        \       
   Discrete  Continuous 
```

- "Numerical" refers to data that consists of numbers.

  - "Discrete" represents data with separate, distinct values (e.g., number of siblings).
  - "Continuous" represents data with a range of values (e.g., height or weight).

-  "Categorical" represents data that falls into categories or groups.

 
 ere's a list ofrandom categories (variables) with their corresponding types:

Fruits (Categorical)
Car Brands (Categorical)
Temperature in Degrees Celsius (Numerical - Continuous)
Animal Species (Categorical)
Shoe Sizes (Categorical)
Ages of People (Numerical - Continuous)
Book Genres (Categorical)
Wind Speed in mph (Numerical - Continuous)
Movie Ratings (Categorical)
Types of Beverages (Categorical)
Number of Children in a Family (Numerical - Discrete)
Number of Bedrooms in a House (Numerical - Discrete)
Count of Emails Received in a Day (Numerical - Discrete)
Number of Cars in a Parking Lot (Numerical - Discrete)
Quantity of Books on a Shelf (Numerical - Discrete)

|   Name   | Age | Height (inches) | Income ($) | Education Level | Marital Status |
|----------|-----|-----------------|------------|-----------------|----------------|
|   Alice  |  28 |      64         |   50000    |   High School   |     Married    |
|   Bob    |  35 |      70         |   75000    |   Bachelor's    |     Single     |
|   Carol  |  42 |      62         |   60000    |   Master's      |     Married    |
|   David  |  31 |      68         |   80000    |   Ph.D.         |     Single     |
|   Eve    |  26 |      66         |   45000    |   Associate's   |     Married    |
Variable Explanations:
    Name: Categorical variable representing individuals' names.
    Age: Numerical variable (Numerical - Discrete) representing individuals' ages.
    Height (inches): Numerical variable (Numerical - Continuous) representing individuals' heights in inches.
    Income ($): Numerical variable (Numerical - Continuous) representing individuals' income in dollars.
    Education Level: Categorical variable representing the educational attainment of individuals.
    Marital Status: Categorical variable representing the marital status of individuals.

## Explanatory vs Response

    Explanatory Variable (Independent Variable):
        The explanatory variable is the one that is intentionally manipulated or selected in a study to examine its effect on another variable.
        It is often denoted as "X" in statistical equations.
        Researchers believe that changes in the explanatory variable may lead to changes in the response variable.
        In experimental research, the researcher controls and manipulates the explanatory variable to observe its impact on the response variable.
        In observational studies, the explanatory variable is observed naturally, and the goal is to understand how it might influence the response variable.
        For example, in a study examining the effect of different study durations (explanatory variable) on exam scores (response variable), study duration is the explanatory variable that researchers manipulate or observe.

    Response Variable (Dependent Variable):
        The response variable is the outcome or the variable of interest that is affected by changes in the explanatory variable.
        It is often denoted as "Y" in statistical equations.
        The response variable is measured or observed to understand how it changes in response to variations in the explanatory variable.
        It represents the outcome or result that researchers are trying to explain or predict.
        In the example mentioned earlier, exam scores are the response variable because they are expected to change based on the different study durations (explanatory variable).

## Observational studies and experiments 
        
Observational studies and experiments are two common research methods used in various fields such as social sciences, medicine, and natural sciences. They differ in their approach to data collection, control over variables, and the ability to establish causation. Here's a comparison of observational studies and experiments:

Observational Studies:

    Purpose:
        Observational studies aim to observe and gather data on naturally occurring events, situations, or phenomena.
        Researchers do not manipulate variables; they merely observe and analyze what is happening.

    Control:
        Researchers have limited control over the variables being studied. They can only observe and record existing conditions.
        Confounding variables (uncontrolled variables that might affect the outcome) can be a concern in observational studies.

    Causation:
        Observational studies can identify associations or correlations between variables, but they cannot establish causation. Correlation does not imply causation.

    Examples:
        Cross-sectional studies, cohort studies, case-control studies, and surveys are common types of observational studies.
        Examples include studying the relationship between smoking and lung cancer by observing individuals' behaviors over time or analyzing survey data.

    Ethics:
        Observational studies are often less intrusive and may not require informed consent for data collection if they involve public observations or existing data.

Experiments:

    Purpose:
        Experiments are designed to investigate cause-and-effect relationships by manipulating one or more variables and observing the resulting changes.
        Researchers actively intervene and control the conditions.

    Control:
        Researchers have a high level of control over variables. They manipulate the independent variable(s) while keeping other variables constant (holding them as constants or using control groups).
        Confounding variables are minimized through experimental control.

    Causation:
        Experiments can establish causation because researchers manipulate the independent variable(s) and directly observe the impact on the dependent variable(s).

    Examples:
        Clinical trials, laboratory experiments, and field experiments are common types of experiments.
        Examples include testing a new drug's efficacy in a clinical trial, studying the effects of temperature on plant growth in a controlled environment, or investigating the impact of a teaching method on student performance in an educational experiment.

    Ethics:
        Experiments often require informed consent, and ethical considerations are crucial, especially when human or animal subjects are involved.
