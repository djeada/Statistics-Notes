## The Normal Curve and Z-Scores

#### The Normal Curve
- **Definition**: Many datasets exhibit a bell-shaped distribution, often referred to as the *normal distribution* or *normal curve*.
    - Examples: Heights, weights, IQ scores typically follow a normal distribution.
    - However, some data such as incomes and house prices may not follow the normal curve.

#### The Empirical Rule (68-95-99.7 Rule)
- **Description**: For data that follows the normal distribution:
    - About 68% of data falls within one standard deviation (σ) of the mean (μ).
    - About 95% of data falls within two standard deviations of the mean.
    - About 99.7% of data falls within three standard deviations of the mean.
- Example: If the mean height (μ) is 68.3 inches and the standard deviation (σ) is 1.8 inches, approximately 95% of the data falls between 64.7 inches and 71.9 inches (μ ± 2σ).

#### Standardizing Data and Z-Scores
- **Definition**: The process of standardizing data transforms raw values into z-scores, making it possible to compare values across different datasets.
    - Formula: 
      \[
      z = \frac{{\text{{height}} - \mu}}{\sigma}
      \]
      where:
        - μ is the mean,
        - σ is the standard deviation.
    - A z-score indicates how many standard deviations a value is from the mean. For example:
        - \( z = 2 \) means the value is 2 standard deviations above the mean.
        - \( z = -1.5 \) means the value is 1.5 standard deviations below the mean.

- **Standard Normal Distribution**: After standardizing, the data follows a standard normal curve with mean 0 and standard deviation 1.

#### Normal Approximation
- **Finding Areas Under the Normal Curve**: To determine the proportion of data within a specific range, standardize the data points and look up the corresponding areas (probabilities) in a z-table or use statistical software.
    - Example: To find the proportion of fathers with heights between 67.4 inches and 71.9 inches:
        - \( z_{67.4} = \frac{{67.4 - 68.3}}{1.8} = -0.5 \)
        - \( z_{71.9} = \frac{{71.9 - 68.3}}{1.8} = 2 \)
        - Using a z-table or software: \( P(71.9 \geq height \geq 67.4) = 97.7\% - 30.9\% = 66.8\% \).

#### Computing Percentiles
- **Percentiles**: To compute the percentile of a normal distribution, use the z-score corresponding to the desired percentile.
    - Example: The 30th percentile of fathers' heights corresponds to a z-score of \( z = -0.52 \), which translates to a height of:
      \[
      height = \mu + z\sigma = 68.3 - (0.52)(1.8) = 67.4 \text{ inches}.
      \]


