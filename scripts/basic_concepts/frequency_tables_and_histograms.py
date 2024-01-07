import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_frequency_table(data):
    """
    This function takes a list of data points and returns a frequency table as a Pandas DataFrame.
    """
    # Convert the list to a Pandas Series for convenience
    data_series = pd.Series(data)

    # Calculate frequency
    frequency = data_series.value_counts().sort_index()

    # Convert to DataFrame for better formatting and readability
    frequency_table = frequency.reset_index()
    frequency_table.columns = ['Value', 'Frequency']

    return frequency_table

def plot_bar_chart(frequency_table):
    """
    This function takes a frequency table and plots a bar chart.
    """
    # Plotting
    plt.bar(frequency_table['Value'], frequency_table['Frequency'])
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Bar Chart of Frequencies')
    plt.show()

def plot_histogram(data, bins):
    """
    This function plots a histogram for continuous data.
    """
    # Plotting
    plt.hist(data, bins=bins, edgecolor='black')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Data')
    plt.show()

# Example Data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Create Frequency Table
freq_table = create_frequency_table(data)

# Display Frequency Table
print("Frequency Table:")
print(freq_table)

# Plot Bar Chart
plot_bar_chart(freq_table)

# For Histogram Example: Continuous Data
heights = [170.2, 165.5, 172.3, 168.7, 171.6, 167.4, 169.5, 174.2, 166.1, 173.5]

# Plot Histogram for Height Data
plot_histogram(heights, bins=5)

