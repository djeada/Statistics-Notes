# Statistics

This repository contains notes, explanations, and code snippets covering essential statistics concepts and techniques. Topics range from basic probability and descriptive statistics to more advanced concepts such as hypothesis testing and confidence intervals.

<img width="1254" height="1254" alt="stats" src="https://github.com/user-attachments/assets/c552ab19-2c31-4405-910c-8f03a89945fd" />

## Requirements

The programming examples are implemented in **Python** for its simplicity, versatility, and rich scientific computing ecosystem. The code makes use of widely used libraries such as:

* **NumPy** for numerical computing
* **SciPy** for advanced scientific computations
* **pandas** for data manipulation and analysis

A basic understanding of Python and its scientific libraries will help you make the most of the code examples.

### Setting up your environment

We recommend using a virtual environment to avoid package conflicts.

```bash
# Create a virtual environment
python3 -m venv env
```

Activate the environment:

```bash
# On Windows
env\Scripts\activate

# On Unix or macOS
source env/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Now you’re ready to run the scripts:

```bash
python scripts/basic_concepts/basic_concepts.py
```

Replace `scripts/basic_concepts/basic_concepts.py` with the actual path to the script you want to run.

When finished, deactivate the environment:

```bash
deactivate
```

## Topics

### Basic Concepts

Concept                                 | Notes                                                                                                         | Implementation                                                                                                | Examples                                                                                                  |
--------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
Introduction to Statistics             | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/introduction_to_statistics.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/basic_concepts/population_sample.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/basic_concepts/variables_and_data.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/basic_concepts/introduction_to_statistics.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
Descriptive Statistics | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/descriptive_statistics.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/basic_concepts/averages.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/basic_concepts/frequency_tables_and_histograms.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/basic_concepts/quartiles.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/basic_concepts/standard_deviation.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/basic_concepts/descriptive_statistics.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
Introduction to Probability             | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/introduction_to_probability.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | N/A |  N/A  |
Geometric Probability                   | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/geometric_probability.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/basic_concepts/geometric_probability.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/basic_concepts/geometric_probability.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
Axioms of Probability                   | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/axioms_of_probability.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | N/A | N/A |
Conditional Probability and Independence | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/conditional_probability_and_independence.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | N/A  | N/A |
Bayes Theorem                           | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/bayes_theorem.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/basic_concepts/venn_diagram_bayes_theorem.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/basic_concepts/bayes_theorem.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
Probability Trees                        | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/probability_tree.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | N/A  | N/A |
Total Probability                       | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/total_probability.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | N/A | N/A |
Bayesian vs Frequentist                | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/bayesian_vs_frequentist.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/basic_concepts/bayesian_vs_frequentist.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/basic_concepts/bayesian_vs_frequentist.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |

### Probability Distributions

| Concept                               | Notes                                                                                                   | Implementation                                                                                        | Examples                                                                                              |
|---------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Introduction to Distributions         | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/introduction_to_distributions.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/introduction_to_distributions.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/introduction_to_distributions.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Central Limit Theorem                 | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/central_limit_theorem.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/central_limit_theorem.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/central_limit_theorem.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Beta Distribution                    | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous_distributions/beta_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/beta_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/beta_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Chi-Square Distribution              | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous_distributions/chi_square_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/chi_square_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/chi_square_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Exponential Distribution             | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous_distributions/exponential_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/exponential_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/exponential_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| F Distribution                       | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous_distributions/f_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/f_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/f_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Gamma Distribution                   | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous_distributions/gamma_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/gamma_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/gamma_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Log-Normal Distribution              | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous_distributions/log_normal_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/log_normal_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/log_normal_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Normal Distribution                  | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous_distributions/normal_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/normal_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/normal_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Student t Distribution               | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous_distributions/student_t_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/student_t_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/student_t_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Uniform Distribution                 | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous_distributions/uniform_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/uniform_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/uniform_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Binomial Distribution                | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/discrete_distributions/binomial_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/binomial_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/binomial_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Geometric Distribution               | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/discrete_distributions/geometric_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/geometric_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/geometric_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Negative Binomial Distribution       | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/discrete_distributions/negative_binomial_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/negative_binomial_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/negative_binomial_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Poisson Distribution                 | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/discrete_distributions/poisson_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/scripts/probability_distributions/poisson_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/main/notebooks/probability_distributions/poisson_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |

### Hypothesis Testing and Confidence Intervals

| Concept                  | Notes                                                                                               | Implementation                                                                                        | Examples                                                                                              |
|--------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Null Hypothesis           | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/statistical_inference/null_hypothesis.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/statistical_inference/null_hypothesis.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/statistical_inference/statistical_inference.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Hypothesis Testing        | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/statistical_inference/hypothesis_testing.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/statistical_inference/p_value.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/statistical_inference/hypothesis_testing.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Type I and Type II Errors | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/statistical_inference/type_i_and_type_ii_errors.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/statistical_inference/type_i_and_type_ii_errors.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/statistical_inference/type_i_and_type_ii_errors.md.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Confidence Intervals      | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/statistical_inference/confidence_intervals.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/statistical_inference/confidence_intervals.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/statistical_inference/confidence_intervals.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Multiple Comparisons      | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/statistical_inference/multiple_comparisons.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/statistical_inference/multiple_comparisons.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/statistical_inference/multiple_comparisons.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Analysis of Variance (ANOVA) | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/statistical_inference/analysis_of_variance.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/statistical_inference/analysis_of_variance.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/statistical_inference/analysis_of_variance.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Analysis of Categorical Data | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/statistical_inference/analysis_of_categorical_data.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/statistical_inference/analysis_of_categorical_data.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/statistical_inference/analysis_of_categorical_data.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |
| Resampling                | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/statistical_inference/resampling.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/statistical_inference/resampling.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/statistical_inference/resampling.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a> |

### Correlation and Regression

Concept | Notes | Implementation | Examples
------ | ----- | -------------- | --------
Correlation | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/correlation_and_regression/correlation.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/correlation_and_regression/correlation.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/correlation_and_regression/correlation.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Covariance | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/correlation_and_regression/covariance.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/correlation_and_regression/covariance.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/correlation_and_regression/covariance.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Simple Linear Regression | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/correlation_and_regression/simple_linear_regression.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/correlation_and_regression/linear_regression.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/correlation_and_regression/linear_regression.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Multiple Regression | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/correlation_and_regression/multiple_regression.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/correlation_and_regression/multiple_regression.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/correlation_and_regression/multiple_regression.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Logistic Regression | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/correlation_and_regression/logistic_regression.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/correlation_and_regression/logistic_regression.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/correlation_and_regression/logistic_regression.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Metrics | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/correlation_and_regression/metrics.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/correlation_and_regression/metrics.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/correlation_and_regression/metrics.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>

### Time Series Analysis

The time-series material now has a dependency-first curriculum. Start with the [time-series learning path](notes/time_series_analysis/README.md), then use the companion code and exercises as you progress.

| Area | Notes | Implementation / Practice |
|---|---|---|
| Foundations | [Stochastic processes and white noise](notes/time_series_analysis/stochastic_processes_and_white_noise.md), [stationarity](notes/time_series_analysis/stationarity.md), [ACF/PACF](notes/time_series_analysis/autocorrelation_function.md) | [white noise script](scripts/time_series_analysis/white_noise.py) |
| Classical models | [AR models](notes/time_series_analysis/autoregressive_models.md), [MA models](notes/time_series_analysis/moving_average_models.md), [ARIMA/SARIMA](notes/time_series_analysis/arima_models.md) | [AR script](scripts/time_series_analysis/autoregressive_model.py), [ARIMA example](scripts/time_series_analysis/arima_inflation.py) |
| Forecasting | [Forecasting](notes/time_series_analysis/forecasting.md), [forecast evaluation](notes/time_series_analysis/forecast_evaluation.md) | [rolling-origin backtesting](scripts/time_series_analysis/forecast_backtesting.py) |
| Dynamic regression | [Dynamic regression](notes/time_series_analysis/dynamic_regression.md) | [dynamic regression example](scripts/time_series_analysis/dynamic_regression.py) |
| Multivariate series | [VAR, Granger predictability, cointegration, VECM](notes/time_series_analysis/multivariate_time_series.md) | [VAR/VECM example](scripts/time_series_analysis/var_and_cointegration.py) |
| State space | [State-space models and Kalman filter](notes/time_series_analysis/state_space_models.md) | [Kalman filter example](scripts/time_series_analysis/kalman_filter.py) |
| Frequency domain | [Frequency-domain analysis](notes/time_series_analysis/frequency_domain_analysis.md) | [periodogram example](scripts/time_series_analysis/frequency_domain.py) |
| Practice | [Exercises](exercises/time_series_analysis/README.md), [extension flashcards](flashcards/time_series_extensions.md), [extension quiz](quizzes/time_series_extensions.md) | Run the examples with the pinned dependencies in `requirements.txt` |

### Spatial Statistics

Concept | Notes | Implementation | Examples
------ | ----- | -------------- | --------
Point Processes | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/spatial_statistics/point_processes.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/spatial_statistics/point_processes.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/spatial_statistics/point_processes.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Spatial Autocorrelation | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/spatial_statistics/spatial_autocorrelation.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/spatial_statistics/spatial_autocorrelation.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/spatial_statistics/spatial_autocorrelation.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Geostatistics | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/spatial_statistics/geostatistics.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/scripts/spatial_statistics/spatial_statistics.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notebooks/spatial_statistics/geostatistics.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>

## How to Contribute

We encourage contributions that enhance the repository's value. To contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## References

### Online Courses and Educational Platforms
- [Harvard University's Introduction to Probability](https://projects.iq.harvard.edu/stat110)
- [edX: Fundamentals of Statistics](https://www.edx.org/course/fundamentals-of-statistics)

### Books

- [The Signal and the Noise: Why So Many Predictions Fail--but Some Don't](https://amzn.to/41CE57B)
- [The Black Swan: The Impact of the Highly Improbable](https://amzn.to/4fu9MG1)
Antifragile: Things That Gain from Disorder https://amzn.to/4mhWf7e
- [Naked Statistics: Stripping the Dread from the Data](https://amzn.to/3JahNUE)
- [How Not to Be Wrong: The Power of Mathematical Thinking](https://amzn.to/45aIWzf)
- [Antifragile: Things That Gain from Disorder](https://amzn.to/4mhWf7e)
- [Fooled by Randomness: The Hidden Role of Chance in Life and in the Markets](https://amzn.to/4mfiBGq)
- [SpringerLink: An Introduction to Statistical Learning](https://link.springer.com/book/10.1007/978-1-4614-7138-7)
- [SpringerLink: The Elements of Statistical Learning](https://link.springer.com/book/10.1007/978-0-387-21736-9)

### Open Source eBooks

- [Think Bayes by Allen Downey](https://allendowney.github.io/ThinkBayes2/)
- [Online Statistics Education: An Interactive Multimedia Course](https://onlinestatbook.com/2/index.html)
- [OpenStax: Introductory Statistics 2e](https://openstax.org/books/introductory-statistics-2e)
- [Introduction to Probability by Charles M. Grinstead and J. Laurie Snell (PDF)](https://people.math.umass.edu/%7Elavine/Book/book.pdf)

### Resources and Cheat Sheets
- [Probability Cheatsheet on GitHub](https://github.com/wzchen/probability_cheatsheet)
- [Allen Downey's Blog on Probability and Bayesian Stats](http://allendowney.blogspot.com/2016/06/there-is-still-only-one-test.html)
- [Saylor Academy: Introductory Statistics](https://saylordotorg.github.io/text_introductory-statistics/index.html)
- [Statistical Learning with Sparsity by Hastie, Tibshirani, and Wainwright](https://hastie.su.domains/CASI/)
- [Statistics How To: Probability and Statistics Main Index](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/probability-main-index/)

### Video Lectures and Playlists
- [Oxford Playlist on Probability and Statistics](https://youtube.com/playlist?list=PL4d5ZtfQonW0B3qW24yAj1u1SuOvgKfP5&si=8nQpv13gbZEWuuqe)

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.