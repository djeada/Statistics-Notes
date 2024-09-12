# Descriptive Statistics

Descriptive statistics offer a summary of the main characteristics of a dataset or sample. They facilitate the understanding and interpretation of data by providing measures of central tendency, dispersion, and shape. In this section, we will discuss the essential concepts and measures in descriptive statistics.

## Frequencies and Frequency Tables

- The **frequency** refers to the number of times a specific value or category appears in a dataset. For example, if 3 individuals report having 1 sibling, the frequency for "1 sibling" is 3.
  
- The **relative frequency** represents the proportion of times a particular value occurs relative to the total number of observations. It is calculated as:

$$\text{Relative Frequency} = \frac{\text{Frequency}}{\text{Total Observations}}$$

- The **cumulative relative frequency** is the sum of the relative frequencies up to a specific category, showing the proportion of observations up to and including that category. It is calculated as:
  
$$\text{Cumulative Relative Frequency} = \sum_{i=1}^{n} \text{Relative Frequency}_i$$

Be careful cumulative frequencies don't make sense when the data doesn't have natural order!

### Example: List of People and Their Sibling Count

Consider a dataset of people and their corresponding number of siblings:

1. Alice - 2 siblings  
2. Bob - 0 siblings  
3. Charlie - 1 sibling  
4. Dana - 3 siblings  
5. Elliot - 1 sibling  
6. Fatima - 2 siblings  
7. George - 0 siblings  
8. Hina - 4 siblings  
9. Ivan - 1 sibling  
10. Julia - 2 siblings  

This dataset can be organized into a frequency distribution table based on the number of siblings:

| Number of Siblings | Frequency | Relative Frequency | Cumulative Relative Frequency |
|--------------------|-----------|--------------------|-------------------------------|
| 0                  | 2         | 20%                | 20%                           |
| 1                  | 3         | 30%                | 50%                           |
| 2                  | 3         | 30%                | 80%                           |
| 3                  | 1         | 10%                | 90%                           |
| 4                  | 1         | 10%                | 100%                          |

Explanation:

- **Number of Siblings** represents the possible values for the number of siblings a person has.
- The **frequency** column shows how many people have a given number of siblings. For example, 2 people have 0 siblings, 3 people have 1 sibling, and so on.
- The **relative frequency** is the proportion of people in each category, expressed as a percentage. It is calculated as:

$$
\text{Relative Frequency} = \frac{\text{Frequency}}{\text{Total Number of People}} \times 100
$$
  
In this case, the total number of people is 10. So, for 0 siblings, the relative frequency is $\frac{2}{10} \times 100 = 20\% $.

- **Cumulative Relative Frequency** represents the cumulative sum of the relative frequencies as we move down the table. It shows the percentage of people with a number of siblings less than or equal to the current value. For example, 50% of the people have 1 or fewer siblings.

### Continuous data

Continuous data can take any value within a range, making it impractical to calculate frequency for each exact number. For example, consider measuring the heights of a group of people. Heights can vary infinitely within a range (e.g., 170.1 cm, 170.2 cm, 170.25 cm), making it unfeasible to have a frequency for each distinct measurement.

Instead, we group continuous data into intervals or ranges and then calculate frequencies for these intervals. This approach simplifies the data and makes it more interpretable.

### Example: Height Measurements (in cm) of a Group of People

I. Raw Data (Continuous):

- 170.2, 165.5, 172.3, 168.7, 171.6, 167.4, 169.5, 174.2, 166.1, 173.5

II Grouped into Ranges:

- 165-167,
- 168-170,
- 171-173,
- 174-176

| Height Range (cm) | Frequency |
|-------------------|-----------|
| 165 - 167         | 2         |
| 168 - 170         | 3         |
| 171 - 173         | 3         |
| 174 - 176         | 2         |

![image](https://github.com/djeada/Statistics-Notes/assets/37275728/5619116b-f65b-47fc-a1cf-a5bfa0640353)

## Measures of Central Tendency

Measures of central tendency provide an idea of the average or central value of the dataset.

- The **arithmetic mean** is useful for characterizing symmetric distributions without outliers and represents the balancing point of a distribution. It is calculated as:

$$\mu_{X} = \frac{1}{n} \sum x$$

- The **weighted mean** accounts for the importance or weight of each value in the dataset, giving more influence to values with higher weights. It is calculated as:

$$\mu_{X} = \frac{\sum w_ix_i}{\sum w_i}$$

- The **geometric mean** is ideal for averaging ratios or handling multiplicative data. It is always smaller than the arithmetic mean and is calculated as:

$$\text{mean} =\sqrt[n]{a_{1}a_{2}...a_{n}}$$

- The **median** is the middle value of a dataset when sorted in ascending order and is particularly suitable for skewed distributions or datasets with outliers.
- The **mode** refers to the most frequently occurring value in a dataset, making it a measure of the most common observation.

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

![image](https://github.com/djeada/Statistics-Notes/assets/37275728/8b59fddf-4218-4365-a345-24075da9326f)

### Choosing Between Mean and Median

- You should **use the median** when minimizing the impact of outliers is important. Since the median is less sensitive to extreme values, it serves as a reliable measure of central tendency, particularly in skewed distributions.
- **Opt for the mean** when it is important to include every value, including outliers, in the calculation. The mean considers all data points, making it useful in situations where each value is equally significant.
- **Be cautious with the mean in skewed data**, as it can provide a misleading sense of central tendency. In skewed distributions, the median often offers a more accurate representation of the typical value in the dataset.
  
#### Example 1: Evaluating Salaries in a Tech Company

Alice is researching salaries of graphic designers at a well-known tech firm. The company has several top-level designers whose salaries are substantially higher than the rest. To get a realistic expectation of her potential earnings, should Alice consider the mean or the median salary?

**Answer**: The median salary would be more indicative of what Alice might earn. It diminishes the impact of the exceptionally high salaries of a few top-level designers, presenting a more typical salary level for a graphic designer at that company.

#### Example 2: Reporting Average Customer Spending in a Bookstore

Tom, managing a small bookstore, needs to report the average spending per customer. While most customers spend about $20, occasionally there are significant purchases of over $500. For an accurate report of average spending, should Tom use the mean or the median?

**Answer**: Tom should use the median for his report. The infrequent, high-value transactions are outliers that would disproportionately inflate the mean, creating a misleading impression of the typical customer spending. The median, less affected by these outliers, would provide a more accurate reflection of regular customer expenditures.

## Measures of Dispersion

Dispersion measures indicate the spread or variability of the data in the dataset.
- The **range** is the difference between the maximum and minimum values in a dataset, providing a basic measure of spread.
  
- The **interquartile range (IQR)** is the difference between the first quartile (Q1) and the third quartile (Q3), capturing the range of the central 50% of the data and reducing the influence of outliers.

- **Variance** measures the average of the squared differences from the mean, indicating the spread of data points around the mean. It is calculated as:

$$V = \frac{\sum (x_i - \overline{x})^2}{N-1}$$ (for a sample)

$$V = \frac{\sum (x_i - \overline{x})^2}{N}$$ (for a population)

- The **standard deviation** is the square root of the variance, giving a direct interpretation of how much the values in a dataset deviate from the mean. It is calculated as:

$$\sigma = \sqrt{\frac{\sum (x_i - \overline{x})^2}{N-1}}$$ (for a sample)

$$\sigma = \sqrt{\frac{\sum (x_i - \overline{x})^2}{N}}$$ (for a population)
### Example: Comparing Athletic Performances

Consider that Chloe swam the 100m freestyle in 53 seconds at a regional competition, and Liam completed a marathon in 2 hours and 55 minutes at a city event. Who performed more exceptionally compared to typical results?

Given Data:

I. For the 100m freestyle:

- Average time (μ) = 60 seconds
- Standard Deviation (σ) = 4 seconds
  
II. For the marathon:

- Average time (μ) = 4 hours
- Standard Deviation (σ) = 30 minutes

Analysis:

I. Chloe's Performance: 

- Chloe's swim time is 53 seconds.
- Calculation of standard deviations from the mean:

$$
\text{Number of SDs} = \frac{60 - 53}{4} = 1.75
$$

- Chloe's time is 1.75 standard deviations better (faster) than the average.

II. Liam's Performance:

- Liam's marathon time is 2 hours and 55 minutes (175 minutes).
- Conversion of average time to minutes: 4 hours = 240 minutes.
- Calculation of standard deviations from the mean:

$$
\text{Number of SDs} = \frac{240 - 175}{30} = 2.17
$$

- Liam's time is 2.17 standard deviations better (faster) than the average.

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

![2a2f7449-2a21-4c44-8ce9-438d7b85135e](https://github.com/djeada/Statistics-Notes/assets/37275728/8a18e3bd-e1cd-44c4-ac04-61f027e10882)

## Percentiles and Quartiles

Percentiles and quartiles provide a way to understand the distribution of values in a dataset, going beyond the range. The range is not always helpful, as it doesn't give much information about how values are distributed around the mean or about the comparative position of an individual value within the distribution.

### Percentiles

A percentile tells us where a given value is ranked in the overall distribution. For example, 25% of the data in a distribution has a value lower than the 25th percentile; 75% of the data has a value lower than the 75th percentile, and so on. The 50th percentile is also the median.

To calculate the percentile for a given value, use the following equation:

$$
\frac{\text{Number of values less than the given value}}{\text{Total number of values}} \times 100
$$

#### Example: Exam Scores

Consider a dataset of exam scores $S = [40, 30, 15, 24, 20, 22, 35]$. We aim to calculate the 30th percentile of this dataset.

**Step 1: Sort the Dataset**

First, sort the dataset $S$ in ascending order:

$$
S_{sorted} = [15, 20, 22, 24, 30, 35, 40]
$$

The dataset contains $n = 7$ elements.

**Step 2: Calculate the Rank Index for the 30th Percentile**

To find the position $i_P$ corresponding to the $P$-th percentile, we use the formula:

$$
i_P = \frac{P \times (n + 1)}{100}
$$

where $P = 30$ (the desired percentile) and $n = 7$ (the number of data points).

Substituting in the values:

$$
i_{30} = \frac{30 \times (7 + 1)}{100} = \frac{240}{100} = 2.4
$$

Since $i_{30} = 2.4$, the position is not an integer. This means the 30th percentile lies between the 2nd and 3rd values in the sorted dataset, requiring interpolation.

**Step 3: Interpolation**

To perform interpolation, let:

- $\lfloor i_P \rfloor = 2$ (the integer part, corresponding to the 2nd value in the sorted dataset, $S_{sorted}[2] = 20$),
- $\lceil i_P \rceil = 3$ (the next integer, corresponding to the 3rd value, $S_{sorted}[3] = 22$),
- $r = i_P - \lfloor i_P \rfloor = 0.4$ (the fractional part).

Now apply linear interpolation using the formula:

$$
\text{Interpolated value} = (1 - r) \times S_{sorted}[\lfloor i_P \rfloor] + r \times S_{sorted}[\lceil i_P \rceil]
$$

Substitute the values:

$$
\text{Interpolated value} = (1 - 0.4) \times 20 + 0.4 \times 22
$$

$$
= 0.6 \times 20 + 0.4 \times 22 = 12 + 8.8 = 20.8
$$

![5ea8e097-b512-40b2-8959-b9d88f4657af](https://github.com/djeada/Statistics-Notes/assets/37275728/f940e95e-4e08-4696-ab10-618cdb49b6da)

### Quartiles

Quartiles divide the data into four equal parts using percentiles. The first quartile contains the values from the minimum to the 25th percentile, the second from the 25th percentile to the 50th percentile (which is the median), the third from the 50th percentile to the 75th percentile, and the fourth from the 75th percentile to the maximum.

To find the quartile thresholds, use the following quantiles:

- First Quartile: $0.25$
- Second Quartile (Median): $0.5$
- Third Quartile: $0.75$

#### Example: Exam Scores

Consider a dataset of exam scores $S = [40, 30, 15, 24, 20, 22, 35]$. To calculate the quartiles, we need to compute the 25th percentile ($Q_1$), the 50th percentile (median, $Q_2$), and the 75th percentile ($Q_3$).

**Step 1: Sort the Dataset**

First, sort the dataset $S$ in ascending order:

$$
S_{sorted} = [15, 20, 22, 24, 30, 35, 40]
$$

The dataset contains $n = 7$ elements.

**Step 2: Calculate the Position Index for Each Quartile**

For a dataset of size $n$, the position index $i_q$ for the $q$-th percentile is calculated using the formula:

$$
i_q = \frac{q \times (n + 1)}{100}
$$

where $q$ is the desired percentile, and $n$ is the number of data points.

**First Quartile (Q1)**

For $q = 25$ (first quartile, $Q_1$):

$$
i_1 = \frac{25 \times (7 + 1)}{100} = \frac{200}{100} = 2
$$

Since $i_1 = 2$, which is an integer, the first quartile corresponds exactly to the 2nd value in the sorted dataset:

$$
Q_1 = S_{sorted}[2] = 20
$$

**Second Quartile (Q2)**

For $q = 50$ (second quartile, or median, $Q_2$):

$$
i_2 = \frac{50 \times (7 + 1)}{100} = \frac{400}{100} = 4
$$

Since $i_2 = 4$ is an integer, the second quartile corresponds to the 4th value in the sorted dataset:

$$
Q_2 = S_{sorted}[4] = 24
$$

**Third Quartile (Q3)**

For $q = 75$ (third quartile, $Q_3$):

$$
i_3 = \frac{75 \times (7 + 1)}{100} = \frac{600}{100} = 6
$$

Since $i_3 = 6$ is an integer, the third quartile corresponds to the 6th value in the sorted dataset:

$$
Q_3 = S_{sorted}[6] = 35
$$

**Visualization**

The boxplot below provides a visual summary of the distribution of the dataset:

![b0f49b50-ef84-4a8c-908f-e57b69fcd874](https://github.com/djeada/Statistics-Notes/assets/37275728/5b77b42b-4b08-4e69-b33e-7bb36e4d2aae)

- The **first quartile (Q1)** is 21.0, indicating that 25% of the data points are less than or equal to this value.
- The **median** is 24.0, meaning that 50% of the data points are less than or equal to this value, and 50% are greater.
- The **third quartile (Q3)** is 32.5, showing that 75% of the data points are less than or equal to this value.
- The **minimum value** in the dataset is approximately 15, as indicated by the left whisker.
- The **maximum value** is around 40, as indicated by the right whisker.
- The **interquartile range (IQR)** is 11.5, calculated as \(32.5 - 21.0$, representing the spread of the middle 50% of the data.
- The **distribution** appears slightly skewed to the right, as the range from the median to the maximum is larger than the range from the median to the minimum.
- There are **no visible outliers**, as no points fall outside the whiskers on either side of the box.
