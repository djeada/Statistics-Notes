# Quizzes on Descriptive Statistics

This series of quizzes covers essential topics in descriptive statistics, including:

- **Measures of Central Tendency**: Test your understanding of the mean, median, and mode, and explore their applications in summarizing data.
- **Measures of Dispersion**: Explore concepts such as range, variance, and standard deviation to assess how data is spread out or clustered.
- **Data Distribution**: Learn about frequency distributions, histograms, and how to interpret the shape, skewness, and kurtosis of data.
- **Percentiles and Quartiles**: Assess your knowledge of how data can be divided into percentiles and quartiles, and how these measures are used to describe data spread.
- **Z-scores**: Understand the concept of Z-scores and how they are used to standardize data for comparison.
- **Outliers**: Learn how to identify outliers and understand their impact on data analysis.
- **Graphical Summaries**: Understand how to use charts such as bar plots, histograms, and box plots to visualize data.

## Measures of Central Tendency

<details>
<summary>What is the mean?</summary>

The **mean** (arithmetic average) is the sum of all data values divided by the number of values. For a sample:

$$\bar{x} = \frac{\sum x_i}{n}$$

where $x_i$ are the data values and $n$ is the number of values. The population mean is written $\mu$ and uses all $N$ members of the population.

</details>

<details>
<summary>What are some limitations of using the mean?</summary>

The mean uses every value, so it is pulled strongly by outliers and by the long tail of a skewed distribution. For example, the data 2, 3, 3, 4, 48 have mean 12 but median 3. For skewed data such as incomes or house prices, the median usually describes a typical value better.

</details>

<details>
<summary>What is the median?</summary>

The **median** is the middle value of the data when sorted from smallest to largest. If there is an even number of values, it is the average of the two middle values. Because it depends only on the order of the data, the median is resistant to outliers and skew.

</details>

<details>
<summary>How do you find the mode?</summary>

The **mode** is the value that occurs most often in a dataset. A dataset can have no mode (all values equally frequent), one mode (unimodal), or several modes (bimodal, multimodal). The mode is the only measure of centre that also works for nominal categorical data.

</details>

## Measures of Dispersion

<details>
<summary>What is the range?</summary>

The **range** is the difference between the largest and smallest values in a dataset:

$$\text{Range} = \text{Max} - \text{Min}$$

It is simple to compute but depends only on the two most extreme values, so a single outlier can change it a lot.

</details>

<details>
<summary>How do you calculate variance?</summary>

**Variance** measures the average squared deviation of the data from their mean. For a population of size $N$ with mean $\mu$:

$$\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$$

For a sample of size $n$ with mean $\bar{x}$, divide by $n - 1$ so that the estimate of $\sigma^2$ is unbiased:

$$s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1}$$

</details>

<details>
<summary>What is standard deviation?</summary>

The **standard deviation** is the square root of the variance, so it measures the typical distance of the data from the mean in the original units. A small standard deviation means the values cluster near the mean, and a large one means they are more spread out.

$$s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n - 1}}$$

The population version, $\sigma$, divides by $N$ and uses $\mu$.

</details>

<details>
<summary>Why is standard deviation often reported instead of variance?</summary>

The standard deviation is in the same units as the data, which makes it easier to interpret. For example, heights have an SD in cm but a variance in cm². The variance is still central in theory, because variances of independent variables add.

</details>

## Data Distribution

<details>
<summary>What is a frequency distribution?</summary>

A **frequency distribution** lists how often each value, category or interval (bin) occurs in a dataset. It can also show relative frequencies (proportions) or cumulative frequencies, and it is usually displayed as a table, a bar chart (for categories) or a histogram (for numerical bins).

</details>

<details>
<summary>What is a histogram?</summary>

A **histogram** displays the distribution of a numerical variable. The range of the data is divided into adjacent intervals (bins), and the height of each bar shows how many values fall in that bin, or, if the bins have unequal widths, their density. Histograms reveal the shape, centre, spread, skewness and modality of the data. The choice of bin width can change how the shape looks.

</details>

<details>
<summary>What is skewness in a distribution?</summary>

**Skewness** measures the asymmetry of a distribution:

- **Positively skewed** (right-skewed): the right tail is longer, and the mean is typically greater than the median.
- **Negatively skewed** (left-skewed): the left tail is longer, and the mean is typically less than the median.

A symmetric distribution, such as the normal, has skewness zero.

</details>

<details>
<summary>What is kurtosis?</summary>

**Kurtosis** measures the tail weight of a distribution, that is, how prone it is to producing extreme values. It is defined as $E[(X-\mu)^4]/\sigma^4$. A normal distribution has kurtosis 3 (excess kurtosis 0) and is called mesokurtic.

- **Leptokurtic** (excess kurtosis > 0): heavier tails and more outliers, as with financial returns.
- **Platykurtic** (excess kurtosis < 0): lighter tails, as with the uniform distribution.

</details>

## Percentiles and Quartiles

<details>
<summary>What is a percentile?</summary>

The $p$-th **percentile** is a value at or below which about $p\%$ of the data fall. For example, a score at the 90th percentile is higher than about 90% of the scores. Percentiles show where an individual value stands relative to the rest of the data.

</details>

<details>
<summary>What are quartiles?</summary>

**Quartiles** split sorted data into four parts that each contain about 25% of the observations:

- $Q_1$ is the 25th percentile,
- $Q_2$ is the median (50th percentile),
- $Q_3$ is the 75th percentile.

Software and textbooks use slightly different interpolation rules. The notes place the $P$-th percentile at position $1 + (n-1)P/100$ in the sorted data.

</details>

<details>
<summary>What is the interquartile range (IQR)?</summary>

The **interquartile range** is the spread of the middle 50% of the data:

$$\text{IQR} = Q_3 - Q_1$$

Because it ignores the lowest and highest 25% of values, it is resistant to outliers. It is the basis of the $1.5 \times \text{IQR}$ outlier rule used in box plots.

</details>

## Z-scores

<details>
<summary>What is a Z-score?</summary>

A **Z-score** tells you how many standard deviations a value lies from the mean:

$$Z = \frac{X - \mu}{\sigma}$$

where $X$ is the value, $\mu$ is the mean and $\sigma$ is the standard deviation. For example, a score of 85 when the mean is 70 and the SD is 10 has $Z = 1.5$. Standardised values have mean 0 and SD 1.

</details>

<details>
<summary>Why are Z-scores useful?</summary>

Z-scores put values on a common, unit-free scale, so you can compare observations from distributions with different means and standard deviations. For example, you can compare exam scores across subjects. If the data are approximately normal, Z-scores can also be converted into percentiles with the standard normal table.

</details>

<details>
<summary>What does a positive or negative Z-score indicate?</summary>

A **positive Z-score** means the value is above the mean, and a **negative Z-score** means it is below the mean. A Z-score of 0 means the value equals the mean. The magnitude gives the distance in standard deviations, so $Z = -2$ is two SDs below the mean.

</details>

## Outliers

<details>
<summary>What is an outlier?</summary>

An **outlier** is an observation that lies unusually far from the bulk of the data. Outliers can come from measurement or recording errors, from a different population, or from genuine rare events. They can strongly affect the mean, standard deviation, range and regression fits.

</details>

<details>
<summary>How do you identify outliers?</summary>

Common rules of thumb are:

- **IQR rule**: values below $Q_1 - 1.5 \times \text{IQR}$ or above $Q_3 + 1.5 \times \text{IQR}$ are flagged as potential outliers.
- **Z-score rule**: values with $|Z| > 3$ are flagged, which works best for roughly normal data.

Plots such as box plots and scatter plots help too. A flagged point should be investigated, not automatically deleted.

</details>

<details>
<summary>What is the impact of outliers on data analysis?</summary>

Outliers can distort non-resistant statistics: they pull the mean towards themselves, inflate the standard deviation and range, and can change a regression line substantially. Resistant measures such as the median and IQR are much less affected. Investigate each outlier: correct genuine errors, but keep real extreme values and consider robust methods.

</details>

## Graphical Summaries

<details>
<summary>What is a bar chart?</summary>

A **bar chart** displays categorical data. Each category gets a separate bar whose length shows its count or proportion. The bars are separated by gaps, and the order of the categories can be changed without losing information. Bar charts are useful for comparing groups.

</details>

<details>
<summary>What is a box plot?</summary>

A **box plot** (box-and-whisker plot) summarises a numerical distribution:

- the box runs from $Q_1$ to $Q_3$, with a line at the median,
- the whiskers extend to the most extreme observations within $1.5 \times \text{IQR}$ of the quartiles,
- points beyond the whiskers are plotted individually as potential outliers.

Box plots make it easy to compare the centre, spread and skew of several groups side by side.

</details>

<details>
<summary>How does a histogram differ from a bar chart?</summary>

A **histogram** shows the distribution of a numerical variable. Its bars cover adjacent intervals of the number line, so they touch, and the bin order is fixed. A **bar chart** shows counts for categories. Its bars are separate and can be reordered. In a histogram the area of a bar represents frequency, so the bin width matters.

</details>
