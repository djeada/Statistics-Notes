# Introduction to Statistics

Statistics is the science of collecting, organizing, analyzing, interpreting, and presenting data. It helps us understand and make informed decisions based on data. In this section, we will introduce essential terms and concepts in statistics and provide a general overview of the subject and its applications.

## Key Terms and Concepts


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


## Population vs Sample

* **Population:** The complete set of all elements or individuals in a study.


```
# @ * ! % * # ! @
* ! % # @ ! % @ *
@ # ! % * @ # % #
! % @ * # ! @ * !
% * # @ ! % @ * #
```

* **Sample:** A subset of the population selected for analysis. Samples are used to make inferences about the population.
  
```
@ !
* % 
```
Scenario :
A poll of 1,200 registered voters in a country found that 45% prefer candidate A over candidate B in the upcoming election.

    Population: All registered voters in the country.
    Sample: The 1,200 registered voters who were polled.

Scenario :
To understand the impact of remote learning, an educational researcher surveyed 100 teachers from across 20 different schools.

    Population: All teachers who are conducting remote learning.
    Sample: The 100 teachers from 20 different schools who were surveyed.

Scenario :
Researchers studying exercise patterns interviewed 250 gym members from a city to estimate how often residents use the gym facilities.

    Population: All gym members in the city.
    Sample: The 250 gym members who were interviewed for the study.

A representative sample is a subset of a population that accurately reflects the members of the entire population. It is designed to be a miniature version of the population, capturing the same variations, groups, and proportions as would be found in the population itself. This ensures that any statistics derived from the sample are likely to closely match the true values from the entire population.

For example, if a population consists of 50% females and 50% males, a representative sample would reflect these same proportions.

Here's an ASCII representation of a representative sample:

markdown

Population: 50% Female, 50% Male
-------------------------
| F | F | M | M | F | M |
-------------------------

Representative Sample: 50% Female, 50% Male
-------------
| F | M | F |
-------------

In this ASCII diagram:

    "Population" is shown as a larger group with an equal number of "F" (females) and "M" (males).
    "Representative Sample" is a smaller group but maintains the same proportion of females to males as the entire population.



Bias in statistics refers to systematic errors that can lead to incorrect conclusions about the population from which a sample is drawn. Bias can occur at any stage of the research process, including the design, data collection, analysis, and interpretation stages. Here are some common types of biases in statistics:

    Selection Bias: This occurs when the sample is not representative of the population. It often happens due to non-random selection of participants. For example, if a survey is conducted online, it may exclude those without internet access.

    Sampling Bias: A type of selection bias that occurs when some members of the intended population are less likely to be included in the sample than others.

    Non-response Bias: This occurs when individuals selected for the sample do not respond. Their non-response may be related to the attribute being measured, which can bias the results. For example, busy people might be less likely to respond to a survey about work-life balance.

    Measurement Bias: This occurs when data collection methods yield results that are systematically different from the true value, often due to faulty measuring instruments or procedures.

    Observer Bias: This occurs when researchers' expectations, beliefs, or preferences influence the data they collect or the way they interpret it. This can also include the placebo effect in clinical trials.

    Survivorship Bias: This is the logical error of focusing on aspects that support surviving a process and casually overlooking those that did not because of their lack of visibility. For instance, considering only successful companies for analysis while ignoring the ones that failed.

    Confirmation Bias: This happens when researchers give more weight to evidence that supports their hypothesis and ignore evidence that contradicts it.

    Recall Bias: This occurs in retrospective studies when participants do not remember previous events accurately or omit details, leading to errors in the data.

    Publication Bias: This arises when the likelihood that research is published is influenced by the nature and direction of its results. Studies with positive findings are more likely to be published than those with negative or inconclusive results.

To avoid bias in sampling, researchers can take several measures:

    Random Sampling: One of the most effective methods to avoid bias is to use a random sampling method where every member of the population has an equal chance of being selected. This can be done through simple random sampling or more complex techniques like stratified random sampling, where the population is divided into strata, and samples are taken from each stratum proportionally.

    Stratified Sampling: This involves dividing the population into subgroups (strata) that share similar characteristics and then randomly sampling from each stratum. This ensures that each subgroup is adequately represented in the sample.

    Systematic Sampling: Here, researchers select samples by following a systematic approach, like choosing every 10th person on a list. It can be biased if there is a pattern in the population that corresponds to the selection interval, but it's more straightforward to implement than random sampling.

    Cluster Sampling: When a population is spread across a wide area or is not easily accessible, cluster sampling can be useful. In this method, the population is divided into clusters, a random sample of clusters is selected, and then all members of the chosen clusters are sampled.
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


## Anecdotal evidence

    Subjectivity: Anecdotal evidence is subjective and based on personal opinions, perceptions, or recollections. It does not follow a standardized or rigorous methodology.

    Small Sample Size: It typically involves a small number of individual cases or instances. These cases are not necessarily representative of a larger population or a broader trend.

    Lack of Control: Anecdotal evidence lacks control over variables, making it susceptible to various biases, including selection bias, confirmation bias, and recall bias.

    Limited Generalizability: Anecdotal evidence cannot be easily generalized to a wider population or used to make broad conclusions because it does not involve a systematic study of a representative sample.

    Informal Nature: It is often shared informally through personal stories, social media posts, testimonials, or casual conversations.

Example
    A friend claims that taking a particular vitamin supplement cured their chronic headaches, but there is no scientific evidence supporting this claim.
    Someone attributes their weight loss to a specific diet plan without considering other factors that may have contributed to the weight loss.

    Product reviews on a website where individuals share their personal experiences with a product. While these reviews can be helpful, they may not represent the overall performance of the product for a wider range of users.


    
