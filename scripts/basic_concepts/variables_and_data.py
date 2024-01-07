import pandas as pd
import numpy as np

# Create a DataFrame with sample data
data = {
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Age': [28, 35, 42, 31, 26],
    'Height (inches)': [64, 70, 62, 68, 66],
    'Income ($)': [50000, 75000, 60000, 80000, 45000],
    'Education Level': ["High School", "Bachelor's", "Master's", "Ph.D.", "Associate's"],
    'Marital Status': ["Married", "Single", "Married", "Single", "Married"]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Sample Data:")
print(df)

# Calculate basic statistics
mean_age = df['Age'].mean()
median_income = df['Income ($)'].median()
mode_education = df['Education Level'].mode().iloc[0]

# Display calculated statistics
print("\nStatistics:")
print("Mean Age:", mean_age)
print("Median Income:", median_income)
print("Mode of Education Level:", mode_education)

# Categorize variables
numerical_variables = ['Age', 'Height (inches)', 'Income ($)']
categorical_variables = ['Education Level', 'Marital Status']

# Display variable categorization
print("\nNumerical Variables:", numerical_variables)
print("Categorical Variables:", categorical_variables)
