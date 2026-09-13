# Introduction to Statistics

Statistics is the science of learning from data. It provides methods for collecting, summarizing, analyzing, and interpreting observations so that we can describe patterns, quantify uncertainty, and make informed decisions.

This guide introduces the main ideas used throughout statistical analysis.

### Key Concepts in Statistics

* **Descriptive statistics** summarize the main features of a dataset using measures such as the mean, median, mode, standard deviation, and graphical displays.
* **Inferential statistics** use sample data to learn about a larger population. Common tools include confidence intervals, hypothesis tests, and statistical models.
* **Regression analysis** models relationships between a response variable and one or more explanatory variables. It can be used for prediction, estimation, and studying associations.

Descriptive statistics tell us what the observed data look like, while inferential methods help us reason beyond the observed sample.

### Real-World Importance of Statistics

* In **decision making**, companies analyze customer and market data to guide choices such as whether to launch a new product.
* In **healthcare**, statistical methods are used to evaluate diagnostic tests, compare treatments, and analyze patient outcomes.
* In **quality control**, manufacturers use statistical methods to monitor production processes and detect unusual variation.
* In **economic policy**, governments analyze data on employment, inflation, production, and other indicators when evaluating economic conditions and policy options.

Statistics does not make decisions automatically. It provides evidence and measures of uncertainty that can support better decisions.

### Applied Statistical Methods

* **Experimental design** involves planning experiments so that effects can be estimated reliably. Randomized controlled trials are an important example in clinical research.
* In **market research**, statistical analysis of consumer data helps businesses understand purchasing behavior, preferences, and market trends.
* **Operational analysis** uses statistical models and process-control methods to study efficiency, logistics, and system performance.
* **Risk assessment** uses probability models and statistical analysis to quantify uncertainty and evaluate potential losses or adverse outcomes.

### Statistical Tools in Action

* In **education**, test scores and other data can be analyzed to evaluate teaching methods and student outcomes.
* **Sports analytics** uses player and game data to evaluate performance and support strategic decisions.
* **Environmental studies** analyze measurements such as pollution levels, temperature, and biodiversity to understand environmental conditions and changes.
* In **technology and AI**, many machine-learning methods rely on ideas from probability, statistics, optimization, and statistical inference.

### Population and Sample

* The **population** is the entire group of individuals, objects, measurements, or outcomes that a study aims to understand.

```text
# @ * ! % * # ! @
* ! % # @ ! % @ *
@ # ! % * @ # % #
! % @ * # ! @ * !
% * # @ ! % @ * #
```

* A **sample** is the subset of the population that is actually observed or measured.

```text
@ !
* %
```

Researchers often study a sample because collecting data from the entire population may be too expensive, slow, or impractical.

The goal is usually to use information from the sample to learn about the population.

#### Illustrative Scenarios

1. In a poll of 1,200 registered voters, 45% prefer candidate A over candidate B.

   * The **population** is the group of registered voters that the poll is intended to represent.
   * The **sample** is the 1,200 registered voters who were surveyed.
   * The observed 45% is a sample statistic used to estimate the corresponding population proportion.

2. An educational researcher surveys 100 teachers across 20 schools to study remote learning.

   * The **population** is the broader group of teachers the researcher wants to draw conclusions about.
   * The **sample** consists of the 100 teachers who were surveyed.

3. Researchers interview 250 gym members to study how often gym members in a city use gym facilities.

   * The **population** is the relevant population of gym members in that city.
   * The **sample** consists of the 250 members who were interviewed.

Notice that the population is determined by the research question. A sample cannot reliably support conclusions about a broader population than the one it was designed to represent.

* A **representative sample** reflects important features of the target population well enough to support the intended inference.

Representativeness is not achieved simply by making every demographic percentage in the sample identical to the population. The sampling method matters because hidden differences between sampled and unsampled individuals can still introduce bias.

#### Population Distribution (Gender Example)

Suppose a population contains equal numbers of individuals in two categories, **F** and **M**:

```text
| F | F | M | M | F | M |
```

A sample with the same overall balance might look like:

```text
| F | M | F | M |
```

Matching the population proportions can be desirable, but representativeness also depends on how the sample was selected.

#### Types of Biases

Bias refers to a systematic tendency for a measurement, estimate, or study design to favor certain outcomes.

* **Selection bias** occurs when the process used to include individuals in a study systematically favors some members of the target population over others.
* **Sampling bias** occurs when the sampling procedure systematically underrepresents or overrepresents parts of the population. It can be viewed as a form of selection bias.
* **Non-response bias** occurs when people who do not respond differ systematically from those who do respond in ways relevant to the study.
* **Measurement bias** occurs when the measurement process systematically produces values that differ from the quantity being measured, for example because of a poorly calibrated instrument.
* **Observer bias** occurs when a researcher's expectations or judgments systematically influence measurements or recorded outcomes. Blinding observers to treatment assignments can help reduce this problem.
* **Survivorship bias** occurs when analysis focuses only on individuals or objects that remain visible after a selection process while ignoring those that did not "survive." Studying only successful companies is a common example.
* **Confirmation bias** occurs when people favor evidence that supports an existing belief while giving less attention to contradictory evidence.
* **Recall bias** occurs when participants systematically remember past events inaccurately, particularly when different groups recall them differently.
* **Publication bias** occurs when studies with statistically significant, positive, or otherwise notable findings are more likely to be published than studies with null or less striking results.

Different biases arise at different stages of a study, so no single procedure eliminates all forms of bias.

#### Strategies to Counteract Bias

* **Simple random sampling** gives each member of a finite population an equal chance of selection and can reduce systematic sampling bias when implemented correctly.
* **Stratified sampling** divides a population into relevant groups, or strata, and samples within each group. This can improve representation and statistical precision.
* **Systematic sampling** selects units according to a regular interval after choosing a starting point. It can work well, but hidden periodic patterns in the population may create bias.
* **Cluster sampling** divides the population into clusters, randomly selects some clusters, and then observes either all units or a sample of units within those clusters. It is often useful when populations are geographically dispersed.
* **Random assignment** is different from random sampling. In an experiment, random assignment allocates sampled participants to treatment conditions and helps balance confounding variables between groups.
* **Blinding** can reduce observer and participant-related biases when people involved in a study do not know which treatment was assigned.

Sampling determines **who enters the study**; random assignment determines **which treatment they receive**. These ideas serve different purposes.

### Variables and Data

* A **variable** is a characteristic that can take different values across individuals, objects, or observations. Examples include age, height, income, and blood type.
* **Data** are the observed values recorded for one or more variables.
* The **population** is the complete set of units or outcomes about which we want to draw conclusions.
* A **parameter** is a numerical quantity describing a population or statistical model.
* A **sample** is the subset of observations actually collected.
* A **statistic** is a numerical quantity calculated from sample data.

A statistic can be used to estimate a parameter, but the two are not the same.

#### Visualization of Data Collection from a Group

Imagine a group of individuals:

```text
   O   O   O   O   O
  /|\ /|\ /|\ /|\ /|\
  / \ / \ / \ / \ / \
```

Each person may have several measured characteristics, such as height or weight, as well as recorded categorical characteristics.

A possible data table is:

| Name  | Gender | Weight | Height |
| ----- | ------ | -----: | -----: |
| Alice | Female |    135 |   5'6" |
| Bob   | Male   |    180 |   6'0" |
| Carol | Female |    140 |   5'5" |
| David | Male   |    175 |  5'11" |
| Eve   | Female |    150 |   5'7" |

Here, each **row** represents an observational unit, while each **column** represents a recorded variable.

`Name` may function mainly as an identifier rather than as a variable of statistical interest. Gender is categorical, while weight and height are numerical.

#### Parameter vs. Statistic

* A **parameter** describes a population or model.
* The **population mean**, $\mu$, is a parameter describing the mean of a numerical variable in the population.
* The **population standard deviation**, $\sigma$, is a parameter describing population variability.
* A **statistic** is calculated from a sample.
* The **sample mean**, $\bar{x}$, is a statistic commonly used to estimate $\mu$.
* The **sample standard deviation**, $s$, is a statistic commonly used to estimate population variability.

The notation helps distinguish population quantities from sample quantities:

| Population                   | Sample                  |
| ---------------------------- | ----------------------- |
| Mean: $\mu$                  | Mean: $\bar{x}$         |
| Standard deviation: $\sigma$ | Standard deviation: $s$ |
| Proportion: $p$              | Proportion: $\hat p$    |

#### Example: Application of Parameters and Statistics

1. Researchers want to estimate the average income of all adults in a city. The **population** consists of the adults included in the target population, and the population mean income is the **parameter** of interest.

2. Because measuring every adult may be impractical, the researchers collect a sample of 500 adults.

3. They calculate the sample mean income:

```math id="xk2hnc"
\bar{x}
=
\frac{1}{n}\sum_{i=1}^{n}x_i.
```

This sample mean is a **statistic**.

4. The statistic can then be used as an estimate of the unknown population mean $\mu$.

Using sample statistics to learn about unknown population parameters is one of the central ideas of inferential statistics.

#### Classification of Variables

Variables are commonly divided into numerical and categorical types:

```text
                  All Variables
                   /          \
             Numerical      Categorical
             /      \        /       \
       Discrete  Continuous Nominal  Ordinal
```

This classification is useful because the type of variable affects which summaries, visualizations, and statistical methods are appropriate.

#### Numerical Variables

* **Numerical variables** take numerical values for which arithmetic operations can be meaningful.

* A **discrete numerical variable** takes values from a countable set. Counts are common examples. The number of children in a family might take values $0,1,2,\ldots$.

* A **continuous numerical variable** is modeled as being able to take any value within an interval. Measurements such as exact height, mass, or temperature are commonly treated as continuous.

Whether a recorded variable appears discrete can depend on measurement precision. For example, age recorded only in completed years takes integer values, while exact age is naturally modeled as continuous.

#### Categorical Variables

* **Categorical variables** place observations into groups or categories rather than measuring quantities on a numerical scale.

* A **nominal variable** has categories with no natural ranking. Examples include blood type, animal species, or car manufacturer.

* An **ordinal variable** has categories with a meaningful order, but the distances between categories are not necessarily equal. Examples include satisfaction levels such as *poor*, *fair*, *good*, and *excellent*, or education levels.

A variable can sometimes be encoded with numbers without becoming numerical. For example, assigning `1 = poor`, `2 = fair`, and `3 = good` does not imply that the difference between poor and fair is quantitatively equal to the difference between fair and good.

#### Data Table Example with Variable Types

| Name  | Age | Height (inches) | Income ($) | Education Level | Marital Status |
| ----- | --: | --------------: | ---------: | --------------- | -------------- |
| Alice |  28 |              64 |      50000 | High School     | Married        |
| Bob   |  35 |              70 |      75000 | Bachelor's      | Single         |
| Carol |  42 |              62 |      60000 | Master's        | Married        |
| David |  31 |              68 |      80000 | Ph.D.           | Single         |
| Eve   |  26 |              66 |      45000 | Associate's     | Married        |

Explanation of Variables in the Table:

* **Name** is primarily an identifier. It could technically be treated as a nominal categorical variable, but it is usually not analyzed as a substantive variable.
* **Age** is recorded here in whole years, so the observed values are discrete. Exact age, however, is conceptually continuous.
* **Height** is a continuous numerical variable, even if it has been rounded to whole inches in this table.
* **Income** is numerical. In many statistical models it is treated as continuous, although actual recorded monetary values occur in discrete currency units.
* **Education Level** is an ordinal categorical variable because the categories have a meaningful ordering.
* **Marital Status** is a nominal categorical variable because its categories have no natural numerical ordering.

The distinction between the underlying variable and the way it is recorded is important. Rounding a continuous measurement does not necessarily change the conceptual type of the variable.

#### Explanatory and Response Variables

Explanatory Variable:

* An **explanatory variable** is a variable used to explain or predict variation in another variable.
* It is often denoted by $X$.
* In an experiment, the explanatory variable may be deliberately manipulated.
* In an observational study, it may simply be observed rather than controlled.

For example, when studying the relationship between study time and exam performance, study time may be treated as the explanatory variable.

Response Variable:

* A **response variable** is the outcome being explained or predicted.
* It is often denoted by $Y$.
* In the study-time example, the exam score is the response variable.

The terms **independent variable** and **dependent variable** are also widely used, but **explanatory** and **response** are often clearer because they do not imply statistical independence.

Practical Illustration:

* Researchers at Elmswood University study the relationship between study duration and exam scores.
* The **explanatory variable** is study time.
* The **response variable** is exam score.

If the researchers only observe existing study habits, the study can identify an association between study time and exam performance.

If they randomly assign students to different study-duration conditions under an appropriate experimental design, they have a stronger basis for investigating a causal effect.

### Observational Studies and Experiments

Observational studies and experiments differ mainly in whether researchers assign or manipulate the explanatory variable.

| **Aspect**    | **Observational Studies**                                                                                                                               | **Experiments**                                                                                                                          |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**   | Study variables as they naturally occur.                                                                                                                | Study responses to deliberately assigned interventions or conditions.                                                                    |
| **Control**   | Researchers do not assign the exposure or treatment; control over confounding is therefore more limited.                                                | Researchers assign treatments and can often use randomization, control groups, and blinding.                                             |
| **Causation** | Can provide strong evidence of association, but causal interpretation requires additional assumptions and careful design.                               | Well-designed randomized experiments can provide strong evidence for causal effects because random assignment helps control confounding. |
| **Examples**  | Cross-sectional studies, cohort studies, case-control studies, surveys.                                                                                 | Randomized clinical trials, laboratory experiments, field experiments.                                                                   |
| **Ethics**    | Ethical requirements depend on the type of data and study design. Observational research involving people may still require consent and ethical review. | Interventions involving human or animal participants may require informed consent, risk assessment, and formal ethical oversight.        |

The distinction between association and causation is important.

If an observational study finds that people who study longer tend to receive higher exam scores, several explanations are possible. Study time may affect performance, but other variables—such as prior preparation, motivation, or course difficulty—may influence both.

These additional variables are called **confounders**.

A randomized experiment helps address this problem by assigning treatments independently of participants' pre-existing characteristics. When randomization is successful and the study is otherwise well designed, differences between treatment groups can more credibly be attributed to the treatment itself.

Even randomized experiments do not establish causation automatically. Poor adherence, missing data, measurement problems, inappropriate analysis, or lack of external validity can still limit the conclusions.

Statistics therefore depends not only on calculations, but also on how the data were collected, what population they represent, and what assumptions are required to interpret them.
