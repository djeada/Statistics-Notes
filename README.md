# Statistics

This repository contains notes, explanations, and code snippets related to essential statistics concepts and techniques. The materials cover a range of topics, from basic probability and descriptive statistics to more advanced concepts like hypothesis testing and confidence intervals.

## Requirements

The programming examples in this repository are primarily implemented in Python due to its simplicity, versatility, and the robustness of its scientific computing ecosystem. The code exploits various widely-used libraries such as NumPy for numerical computing, SciPy for advanced scientific computations, and pandas for data manipulation and analysis. As a result, a basic understanding of Python programming and its scientific libraries would be beneficial for comprehending and utilizing the code snippets.

To ensure you can run the code snippets and notebooks seamlessly, please make sure your environment fulfills the Python dependencies. We recommend setting up a virtual environment to avoid any package conflicts.

You can set up a virtual environment using the following steps:

```bash
# Create a virtual environment
python3 -m venv env
```

To activate the virtual environment, the command differs based on your operating system:

```bash
# On Windows, use:
env\Scripts\activate

# On Unix or MacOS, use:
source env/bin/activate
```

Once the virtual environment is activated, install the necessary packages using pip:

```bash
pip install -r requirements.txt
```

Now, you should be ready to run the code in this repository.

```bash
# Here's an example of how you can run a Python script
python src/basic_concepts/basic_concepts.py
```

Remember to replace 'src/basic_concepts/basic_concepts.py' with the actual name of the script you wish to run.

When you're done working, you can deactivate the virtual environment by simply running the deactivate command.

```bash
deactivate
```

## Topics

### Basic Concepts

Concept | Notes | Implementation | Examples
------ | ----- | -------------- | --------
Introduction to Probability | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/introduction_to_probability.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/basic_concepts/basic_concepts.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/basic_concepts/basic_concepts.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Conditional Probability and Independence | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/conditional_probability_and_independence.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/basic_concepts/basic_concepts.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/basic_concepts/basic_concepts.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Introduction to Statistics | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/introduction_to_statistics.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/basic_concepts/basic_concepts.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/basic_concepts/basic_concepts.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Descriptive Statistics | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/descriptive_statistics.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/basic_concepts/basic_concepts.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/basic_concepts/basic_concepts.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Bayesian vs Frequentist | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/basic_concepts/bayesian_vs_frequentist.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/basic_concepts/basic_concepts.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/basic_concepts/basic_concepts.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>

### Probability Distributions

Concept | Notes | Implementation | Examples
------ | ----- | -------------- | --------
General Distributions | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/distributions.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/probability_distributions/distributions.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/probability_distributions/distributions.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Binomial Distribution | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/discrete/binomial.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/probability_distributions/discrete/binomial.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/probability_distributions/discrete/binomial.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Poisson Distribution | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/discrete/poisson.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/probability_distributions/discrete/poisson.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/probability_distributions/discrete/poisson.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Uniform Distribution | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous/uniform.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/probability_distributions/continuous/uniform.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/probability_distributions/continuous/uniform.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Normal Distribution | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous/normal.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/probability_distributions/continuous/normal.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/probability_distributions/continuous/normal.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Exponential Distribution | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous/exponential.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/probability_distributions/continuous/exponential.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/probability_distributions/continuous/exponential.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Chi Square Distribution | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous/chi_square.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/probability_distributions/continuous/chi_square.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/probability_distributions/continuous/chi_square.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Student's t-Distribution | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous/student_t.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/probability_distributions/continuous/student_t.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/probability_distributions/continuous/student_t.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
F-Distribution | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/probability_distributions/continuous/f_distribution.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/probability_distributions/continuous/f_distribution.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/probability_distributions/continuous/f_distribution.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>

### Hypothesis Testing and Confidence Intervals

Concept | Notes | Implementation | Examples
------ | ----- | -------------- | --------
Null Hypothesis | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/hypothesis_testing_and_confidence_intervals/null_hypothesis.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/hypothesis_testing_and_confidence_intervals/hypothesis_testing_and_confidence_intervals.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/hypothesis_testing_and_confidence_intervals/hypothesis_testing_and_confidence_intervals.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Hypothesis Testing | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/hypothesis_testing_and_confidence_intervals/hypothesis_testing.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/hypothesis_testing_and_confidence_intervals/hypothesis_testing_and_confidence_intervals.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/hypothesis_testing_and_confidence_intervals/hypothesis_testing_and_confidence_intervals.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Type I and Type II Errors | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/hypothesis_testing_and_confidence_intervals/type_i_and_type_ii_errors.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/hypothesis_testing_and_confidence_intervals/hypothesis_testing_and_confidence_intervals.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/hypothesis_testing_and_confidence_intervals/hypothesis_testing_and_confidence_intervals.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Confidence Intervals | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/hypothesis_testing_and_confidence_intervals/confidence_intervals.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/hypothesis_testing_and_confidence_intervals/hypothesis_testing_and_confidence_intervals.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/hypothesis_testing_and_confidence_intervals/hypothesis_testing_and_confidence_intervals.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Multiple Comparisons | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/hypothesis_testing_and_confidence_intervals/multiple_comparisons.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/hypothesis_testing_and_confidence_intervals/hypothesis_testing_and_confidence_intervals.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/hypothesis_testing_and_confidence_intervals/hypothesis_testing_and_confidence_intervals.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>

### Correlation and Regression

Concept | Notes | Implementation | Examples
------ | ----- | -------------- | --------
Correlation | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/correlation_and_regression/correlation.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/correlation_and_regression/correlation_and_regression.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/correlation_and_regression/correlation_and_regression.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Simple Linear Regression | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/correlation_and_regression/simple_linear_regression.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/correlation_and_regression/correlation_and_regression.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/correlation_and_regression/correlation_and_regression.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Multiple Regression | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/correlation_and_regression/multiple_regression.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/correlation_and_regression/correlation_and_regression.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/correlation_and_regression/correlation_and_regression.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Logistic Regression | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/correlation_and_regression/logistic_regression.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/correlation_and_regression/correlation_and_regression.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/correlation_and_regression/correlation_and_regression.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Metrics | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/correlation_and_regression/metrics.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/correlation_and_regression/correlation_and_regression.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/correlation_and_regression/correlation_and_regression.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>

### Time Series Analysis

Concept | Notes | Implementation | Examples
------ | ----- | -------------- | --------
Time Series | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/time_series_analysis/time_series.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/time_series_analysis/time_series_analysis.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/time_series_analysis/time_series_analysis.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Seasonality and Trends | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/time_series_analysis/seasonality_and_trends.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/time_series_analysis/time_series_analysis.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/time_series_analysis/time_series_analysis.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Autoregressive Models | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/time_series_analysis/autoregressive_models.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/time_series_analysis/time_series_analysis.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/time_series_analysis/time_series_analysis.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Moving Average Models | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/time_series_analysis/moving_average_models.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/time_series_analysis/time_series_analysis.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/time_series_analysis/time_series_analysis.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Forecasting | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/time_series_analysis/forecasting.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/time_series_analysis/time_series_analysis.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/time_series_analysis/time_series_analysis.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>

### Spatial Statistics

Concept | Notes | Implementation | Examples
------ | ----- | -------------- | --------
Point Processes | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/spatial_statistics/point_processes.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/spatial_statistics/spatial_statistics.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/spatial_statistics/spatial_statistics.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Spatial Autocorrelation | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/spatial_statistics/spatial_autocorrelation.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/spatial_statistics/spatial_statistics.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/spatial_statistics/spatial_statistics.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>
Geostatistics | <a href="https://github.com/djeada/Statistics-Notes/blob/master/notes/spatial_statistics/geostatistics.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/src/spatial_statistics/spatial_statistics.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /></a> | <a href="https://github.com/djeada/Statistics-Notes/blob/master/examples/spatial_statistics/spatial_statistics.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /></a>

## Refrences

* https://projects.iq.harvard.edu/stat110
* https://www.edx.org/course/fundamentals-of-statistics
* https://allendowney.github.io/ThinkBayes2/
* https://link.springer.com/book/10.1007/978-0-387-21736-9
* https://link.springer.com/book/10.1007/978-1-4614-7138-7
* https://github.com/wzchen/probability_cheatsheet
* http://allendowney.blogspot.com/2016/06/there-is-still-only-one-test.html
* https://saylordotorg.github.io/text_introductory-statistics/index.html
* https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/probability-main-index/

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
