# Descriptive Statistics Quiz

Notes: [Introduction to Statistics](../notes/foundations/introduction_to_statistics.md), [Descriptive Statistics](../notes/foundations/descriptive_statistics.md), [Statistical Moments](../notes/random_variables_and_distributions/statistical_moments.md), [Standard Error and the LLN](../notes/sampling_and_sampling_distributions/standard_error_and_lln.md)

Check your understanding of data types, measures of centre and spread, shape, z-scores and graphical summaries.

#### Q. Which measure is most appropriate for comparing the **relative spread** of datasets measured in different units?

* [ ] Standard deviation
* [ ] Variance
* [ ] Range
* [x] Coefficient of variation

> **Explanation:** The coefficient of variation $s/\bar{x}$ is unit-free, so it can compare, say, spread in heights (cm) with spread in weights (kg). The other measures carry the units of the data.

#### Q. What is the relationship between the **variance** and the **standard deviation**?

* [ ] The variance is the square root of the standard deviation
* [x] The variance is the square of the standard deviation
* [ ] The variance is twice the standard deviation
* [ ] The variance is the standard deviation divided by n

> **Explanation:** The standard deviation is defined as $\sqrt{\text{variance}}$, which puts it back in the original units of the data.

#### Q. What is the main difference between a **sample mean** and a **population mean**?

* [ ] The sample mean is always larger than the population mean
* [x] The sample mean is computed from a subset, while the population mean uses every member
* [ ] The population mean can only be used for hypothesis testing
* [ ] The sample mean ignores outliers, while the population mean does not

> **Explanation:** $\bar{x}$ is a statistic computed from observed data and varies from sample to sample. $\mu$ is a fixed, usually unknown parameter that $\bar{x}$ estimates.

#### Q. What is the **median** of a dataset?

* [ ] The most frequent value in the dataset
* [x] The middle value of the sorted data, or the mean of the two middle values
* [ ] The arithmetic average of all values in the dataset
* [ ] The midpoint between the minimum and the maximum

> **Explanation:** Sort the data and take the central value; with an even count, average the two central values. The midpoint of the min and max is the midrange.

#### Q. What happens to the **standard error of the mean** as the sample size increases?

* [ ] It increases
* [x] It decreases
* [ ] It stays the same
* [ ] It increases and then decreases

> **Explanation:** $SE = \sigma/\sqrt{n}$, so larger samples give more precise estimates of the mean. Quadrupling $n$ halves the standard error.

#### Q. You want to show how many cars of each **model** are in a parking lot. Which graph is most appropriate?

* [ ] Line graph
* [ ] Histogram
* [x] Bar chart
* [ ] Scatter plot

> **Explanation:** Car model is a categorical variable, and a bar chart displays the count for each category. Histograms are for binned numerical data.

#### Q. Which of the following is a **continuous** variable?

* [ ] The number of heads in 10 coin flips
* [ ] The outcome of rolling a die
* [x] The height of students in a class
* [ ] The number of students in a class

> **Explanation:** Height can take any value in an interval. The other three are counts or outcomes with a finite set of possible values, so they are discrete.

#### Q. Which measure of **centre** is least sensitive to outliers?

* [ ] Mean
* [x] Median
* [ ] Midrange
* [ ] Weighted mean

> **Explanation:** The median depends only on the middle of the sorted data, so moving an extreme value does not change it. The mean and midrange both shift with extreme values.

#### Q. What does the **interquartile range (IQR)** measure?

* [ ] The distance between the largest and smallest values
* [x] The spread of the middle 50% of the data, $Q_3 - Q_1$
* [ ] The average squared distance from the mean
* [ ] The distance between the mean and the median

> **Explanation:** The IQR is the difference between the third and first quartiles, so it ignores the most extreme 25% at each end. The first option is the range.

#### Q. What is a **box plot** mainly used for?

* [ ] Showing the relationship between two numerical variables
* [x] Summarising a distribution with its median, quartiles, whiskers and outliers
* [ ] Showing the share of each category in a whole
* [ ] Showing how a variable changes over time

> **Explanation:** A box plot draws the box from $Q_1$ to $Q_3$ with a line at the median, extends whiskers to the most extreme points within $1.5 \times IQR$, and plots points beyond as potential outliers.

#### Q. Which of the following is a measure of **central tendency**?

* [ ] Standard deviation
* [ ] Variance
* [x] Median
* [ ] Range

> **Explanation:** Mean, median and mode describe where the data are centred. Standard deviation, variance and range describe spread.

#### Q. Which statistic measures the typical **spread** of data around the mean, in the original units?

* [ ] Mean
* [ ] Median
* [x] Standard deviation
* [ ] Mode

> **Explanation:** The standard deviation is the square root of the average squared deviation from the mean. The variance measures the same spread but in squared units.

#### Q. A dataset is strongly **right-skewed**. Which measure of centre is pulled furthest towards the long tail?

* [x] Mean
* [ ] Median
* [ ] Mode
* [ ] 10% trimmed mean

> **Explanation:** The mean uses every value, so a few large values pull it up. The trimmed mean discards the extremes and the median and mode are barely affected.

#### Q. Test scores have mean 70 and standard deviation 10. What is the **z-score** of a score of 85?

* [ ] 0.85
* [ ] 15
* [x] 1.5
* [ ] −1.5

> **Explanation:** $z = (x - \mu)/\sigma = (85 - 70)/10 = 1.5$, so the score is 1.5 standard deviations above the mean.

#### Q. Which of the following is **not** a measure of dispersion?

* [ ] Variance
* [ ] Standard deviation
* [x] Mean
* [ ] Interquartile range

> **Explanation:** The mean measures the centre of the data. Variance, standard deviation and IQR all describe how spread out the values are.

#### Q. For the data 2, 3, 3, 4, 48, what are the **mean** and **median**?

* [x] Mean 12, median 3
* [ ] Mean 3, median 12
* [ ] Mean 12, median 4
* [ ] Mean 3, median 3

> **Explanation:** The mean is $60/5 = 12$ and the median (third sorted value) is 3. The single outlier 48 drags the mean far above every other value while the median ignores it.

#### Q. If the **mean and median** of a unimodal dataset are equal, the distribution is most likely:

* [ ] Left-skewed
* [ ] Right-skewed
* [x] Symmetric

> **Explanation:** In a symmetric distribution the mean and median coincide, while skew pulls the mean towards the long tail. Equality is not proof of symmetry, but it is what you would expect.

#### Q. How many **modes** does the dataset 1, 2, 2, 3, 3, 4 have?

* [ ] None
* [ ] One
* [x] Two
* [ ] Four

> **Explanation:** The values 2 and 3 both occur twice, more often than any other value, so the dataset is bimodal with modes 2 and 3.

#### Q. What is the **population standard deviation** of the data 2, 4, 4, 4, 5, 5, 7, 9?

* [ ] 4.0
* [x] 2.0
* [ ] 2.14
* [ ] 5.0

> **Explanation:** The mean is 5 and the squared deviations sum to $9+1+1+1+0+0+4+16 = 32$. Dividing by $n = 8$ gives variance 4, so $\sigma = 2$. Dividing by $n - 1 = 7$ would give the sample SD, 2.14.

#### Q. In a **bimodal** distribution, how many peaks does the histogram have?

* [ ] One
* [x] Two
* [ ] Three
* [ ] None

> **Explanation:** Bimodal means two distinct peaks. This often means two subgroups are mixed together, such as the heights of adult men and women.

#### Q. Which variable is **categorical**?

* [ ] Height of students
* [ ] Number of hours worked
* [x] Type of fruit sold
* [ ] Temperature of a city

> **Explanation:** Fruit type places each observation in a named group with no numerical meaning. The other three are numerical measurements.

#### Q. A distribution has a long tail to the **right**. What is the typical relationship between the mean and the median?

* [ ] The mean is less than the median
* [ ] The mean equals the median
* [x] The mean is greater than the median
* [ ] The mean and median have no typical ordering

> **Explanation:** The large values in the right tail pull the mean upwards while the median stays near the bulk of the data, so typically mean > median.

#### Q. Which plot is most useful for showing the relationship between **two continuous variables**?

* [ ] Pie chart
* [ ] Histogram
* [x] Scatter plot
* [ ] Box plot

> **Explanation:** A scatter plot puts one variable on each axis, so it shows direction, form, strength and outliers in the relationship. Histograms and box plots show one variable at a time.

#### Q. You know only the number of households and one summary of their incomes, and you need to recover the **total income**. Which summary must it be?

* [x] Mean
* [ ] Median
* [ ] Mode
* [ ] Interquartile range

> **Explanation:** Total $= n \times \bar{x}$, so only the mean lets you reconstruct the sum. The median is often better for a typical household when incomes are skewed, but it does not determine the total.

#### Q. Which measure of **spread** is least affected by outliers?

* [ ] Range
* [ ] Variance
* [ ] Standard deviation
* [x] Interquartile range

> **Explanation:** The IQR uses only the quartiles, so extreme values at either end do not change it. The range depends entirely on the extremes, and the variance squares large deviations.

#### Q. If every value in a dataset is **multiplied by 3**, what happens to the mean?

* [ ] It stays the same
* [ ] It decreases by 3
* [ ] It increases by 3
* [x] It is multiplied by 3

> **Explanation:** The mean is linear: $\text{mean}(3x) = 3\,\text{mean}(x)$. The standard deviation is also multiplied by 3, and the variance by 9.

#### Q. Which measure of centre is usually most appropriate for a **strongly skewed** distribution?

* [ ] Mean
* [ ] Mode
* [x] Median
* [ ] Midrange

> **Explanation:** The median is resistant to the long tail, so it represents a typical value better. This is why median income or median house price is usually reported.

#### Q. Which variable is **ordinal**?

* [ ] Brand of phone owned
* [ ] Exact weight in kilograms
* [x] Customer satisfaction rated low, medium or high
* [ ] Country of birth

> **Explanation:** Ordinal categories have a natural order but no fixed distance between levels. Brand and country are nominal (no order), and weight is a continuous numerical variable.

#### Q. What is the **range** of the dataset 4, 8, 15, 16, 23, 42?

* [ ] 16
* [x] 38
* [ ] 42
* [ ] 15.5

> **Explanation:** Range = maximum − minimum = $42 - 4 = 38$. The value 15.5 is the median.

#### Q. What is the **mode** of the dataset 5, 7, 7, 9, 9, 9, 11?

* [ ] 5
* [ ] 7
* [x] 9
* [ ] 8.14

> **Explanation:** 9 appears three times, more often than any other value. The mean of the data is about 8.14.

#### Q. Using the notes' quartile method, what is the **IQR** of 3, 5, 5, 5, 8, 10, 10, 10, 14?

* [ ] 11
* [x] 5
* [ ] 8
* [ ] 3

> **Explanation:** With $n = 9$, $Q_1$ sits at position $1 + 8(0.25) = 3$, giving 5, and $Q_3$ at position $1 + 8(0.75) = 7$, giving 10. So $IQR = 10 - 5 = 5$. The range would be 11.

#### Q. If you **add 10** to every value in a dataset, what happens to the standard deviation?

* [ ] It increases by 10
* [ ] It decreases by 10
* [x] It stays the same
* [ ] It is multiplied by 10

> **Explanation:** Adding a constant shifts every value and the mean by the same amount, so the deviations from the mean, and therefore the SD, do not change.

#### Q. Which kind of data is a **pie chart** best suited to?

* [x] Shares of a whole across a few categories
* [ ] A continuous variable such as height
* [ ] The relationship between two numerical variables
* [ ] Values recorded at regular points in time

> **Explanation:** A pie chart shows how a total is split among categories, and it works best with only a few. Continuous data suit histograms, bivariate data suit scatter plots, and time series suit line graphs.

#### Q. Why does the **sample variance** divide by $n - 1$ instead of $n$?

* [ ] To make the variance less sensitive to outliers
* [x] To make it an unbiased estimator of the population variance
* [ ] To convert the variance into the original units
* [ ] To make the variance equal to the squared mean

> **Explanation:** Deviations are measured from $\bar{x}$ rather than the unknown $\mu$, which makes them slightly too small. Dividing by $n - 1$ corrects this, so $E[s^2] = \sigma^2$.

#### Q. What is the **sample variance** of the data 1, 2, 3, 4, 5?

* [ ] 2.0
* [x] 2.5
* [ ] 1.58
* [ ] 10

> **Explanation:** The mean is 3 and the squared deviations sum to $4+1+0+1+4 = 10$. Dividing by $n - 1 = 4$ gives 2.5. Dividing by $n = 5$ gives the population variance, 2.0.

#### Q. A distribution has **excess kurtosis** well above zero. What does this indicate compared with a normal distribution?

* [ ] It is skewed to the left
* [x] It has heavier tails, so extreme values are more common
* [ ] It has lighter tails, so extreme values are rarer
* [ ] It has a larger standard deviation

> **Explanation:** Kurtosis measures tail weight. A normal distribution has kurtosis 3, which is excess kurtosis 0. Positive excess (leptokurtic) means heavier tails, as with financial returns. Kurtosis says nothing about scale or skew direction.
