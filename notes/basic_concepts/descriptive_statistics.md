# Descriptive Statistics

Descriptive statistics offer a summary of the main characteristics of a dataset or sample. They facilitate the understanding and interpretation of data by providing measures of central tendency, dispersion, and shape. In this section, we will discuss the essential concepts and measures in descriptive statistics.

## Measures of Central Tendency

Measures of central tendency provide an idea of the average or central value of the dataset.

* **Arithmetic Mean:** Suitable for characterizing symmetric distributions without outliers.

  $$\mu_{X} = \frac{1}{n} \sum x$$

* **Weighted Mean:** Takes into account the importance or weight of each value in the dataset.

  $$\mu_{X} = \frac{\sum w_ix_i}{\sum w_i}$$

* **Geometric Mean:** Ideal for averaging ratios or handling multiplicative data. Always smaller than the arithmetic mean.

  $$\text{mean} =\sqrt[n]{a_{1}a_{2}...a_{n}}$$

* **Median:** The precise middle value among a dataset when sorted in ascending order. Suitable for skewed distributions or data with outliers.

* **Mode:** The most frequently occurring element in a dataset.

### Example

Measures of central tendency help us identify the middle value in a dataset. Let's consider a dataset representing the number of sales per day for a store during a week:

| Day       | Sales       |
|-----------|-------------|
| Monday    | 17          |
| Tuesday   | 21          |
| Wednesday | 17          |
| Thursday  | 35          |
| Friday    | 23          |
| Saturday  | 14          |
| Sunday    | 24          |

We can use different measures to determine the central value: mean, median, and mode.

#### Mean

The mean (or average) is the sum of all values divided by the number of values. In this example:

$$
\text{Mean} = \frac{17 + 21 + 17 + 35 + 23 + 14 + 24}{7} \approx 21.57
$$

#### Median

The median is the middle value in the sorted dataset. For our example, after sorting:

| Sales      |
|------------|
| 14         |
| 17         |
| 17         |
| 21         |
| 23         |
| 24         |
| 35         |

The median value is 21.

#### Mode

The mode is the most frequently occurring value. In our example, the mode is 17, as it occurs twice:

| Sales      |
|------------|
| 14         |
|**17**      |
|**17**      |
| 21         |
| 23         |
| 24         |
| 35         |

Each measure of central tendency can provide different insights into the dataset. In this example, the mean is slightly affected by the larger sales number on Thursday, while the median and mode give a more typical representation of the central value.


## Measures of Dispersion

Dispersion measures indicate the spread or variability of the data in the dataset.

* **Range:** The difference between the maximum and minimum values in the dataset.

* **Interquartile Range (IQR):** The difference between the first quartile (Q1) and the third quartile (Q3). Represents the range encompassing the central 50% of the data.

* **Variance:** The average of the squared differences from the mean.

  $$V = \frac{\sum (x_i - \overline{x})^2}{N-1}$$ (for a sample)

  $$V = \frac{\sum (x_i - \overline{x})^2}{N}$$ (for a population)

* **Standard Deviation:** The square root of the variance. Indicates the degree to which individual elements deviate from the mean.

  $$\sigma = \sqrt{\frac{\sum (x_i - \overline{x})^2}{N-1}}$$ (for a sample)

  $$\sigma = \sqrt{\frac{\sum (x_i - \overline{x})^2}{N}}$$ (for a population)

### Understanding Variance

Variance is an intrinsic aspect of the universe.
Obtaining identical results after repeated observations of the same event is impossible due to random noise or error. Variance can be attributed to sampling or measurement errors. In some cases, variance results from the random fluctuations of the universe.

### Example

Measures of dispersion help us understand the spread or variability of data in a dataset. Continuing with the store sales dataset:

| Day       | Sales       |
|-----------|-------------|
| Monday    | 17          |
| Tuesday   | 21          |
| Wednesday | 17          |
| Thursday  | 35          |
| Friday    | 23          |
| Saturday  | 14          |
| Sunday    | 24          |

We can use different measures to determine the dispersion: range, variance, and standard deviation.

#### Range

The range is the difference between the maximum and minimum values in the dataset. In this example:

$$
\text{Range} = 35 - 14 = 21
$$

#### Variance

Variance measures the average squared difference of each value from the mean. For our example, first, we need to calculate the mean:

$$
\text{Mean} \approx 21.57
$$

Now, we can calculate the variance:

$$
\text{Variance} = \frac{(17 - 21.57)^2 + (21 - 21.57)^2 + (17 - 21.57)^2 + (35 - 21.57)^2 + (23 - 21.57)^2 + (14 - 21.57)^2 + (24 - 21.57)^2}{7} \approx 47.39
$$

#### Standard Deviation

The standard deviation is the square root of the variance. In our example:

$$
\text{Standard Deviation} = \sqrt{47.39} \approx 6.88
$$

Each measure of dispersion provides different information about the spread of the dataset. The range gives us an overall view of the spread, but it can be influenced by extreme values. The variance and standard deviation give a more detailed representation of the dispersion and are less sensitive to outliers.

## Percentiles and Quartiles

Percentiles and quartiles provide a way to understand the distribution of values in a dataset, going beyond the range. The range is not always helpful, as it doesn't give much information about how values are distributed around the mean or about the comparative position of an individual value within the distribution.

### Percentiles

A percentile tells us where a given value is ranked in the overall distribution. For example, 25% of the data in a distribution has a value lower than the 25th percentile; 75% of the data has a value lower than the 75th percentile, and so on. The 50th percentile is also the median.

To calculate the percentile for a given value, use the following equation:

\begin{equation}
\frac{\text{Number of values less than the given value}}{\text{Total number of values}} \times 100
\end{equation}

### Quartiles

Quartiles divide the data into four equal parts using percentiles. The first quartile contains the values from the minimum to the 25th percentile, the second from the 25th percentile to the 50th percentile (which is the median), the third from the 50th percentile to the 75th percentile, and the fourth from the 75th percentile to the maximum.

To find the quartile thresholds, use the following quantiles:

- First Quartile: 0.25
- Second Quartile (Median): 0.5
- Third Quartile: 0.75


### Example

Consider a dataset of exam scores: [15, 20, 22, 24, 30, 35, 40].

#### Percentiles

Let's calculate the 30th percentile of this dataset.

Sort the dataset in ascending order: [15, 20, 22, 24, 30, 35, 40].

Calculate the rank (i) using the formula:

$$i = \frac{P \times (n + 1)}{100}$$

Where P is the percentile (in our case, 30) and n is the total number of values (7).

$$i = \frac{30 \times (7 + 1)}{100} = 2.4$$

Since i is not an integer, interpolate between the two nearest values in the sorted dataset:

$$value = (1 - r) \times value_i + r \times value_{i+1}$$

Where r is the decimal part of i, and $value_i$ and $value_{i+1}$ are the neighboring data points.

$$value = (1 - 0.4) \times 20 + 0.4 \times 22 = 20.8$$

So, the 30th percentile of the dataset is 20.8.

#### Quartiles

To calculate quartiles, follow these steps:

Calculate the 25th, 50th (median), and 75th percentiles using the same method as above.

For the 25th percentile (Q1):

$$i = \frac{25 \times (7 + 1)}{100} = 2$$

Since i is an integer, the value is the average of the 2nd and 3rd values in the sorted dataset:

$$Q1 = \frac{20 + 22}{2} = 21$$

For the 50th percentile (Q2):

$$i = \frac{50 \times (7 + 1)}{100} = 4$$

Since i is an integer, the value is the average of the 4th and 5th values in the sorted dataset:

$$Q2 = \frac{24 + 30}{2} = 27$$

For the 75th percentile (Q3):

$$i = \frac{75 \times (7 + 1)}{100} = 6$$

Since i is an integer, the value is the average of the 6th and 7th values in the sorted dataset:

$$Q3 = \frac{35 + 40}{2} = 37.5$$

So, the quartiles of the dataset are Q1 = 21, Q2 = 27, and Q3 = 37.5.

