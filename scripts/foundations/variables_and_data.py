import pandas as pd


def build_dataframe():
    """Builds the small example data table used in the note."""
    data = {
        "Name": ["Alice", "Bob", "Carol", "David", "Eve"],
        "Age": [28, 35, 42, 31, 26],
        "Height (inches)": [64, 70, 62, 68, 66],
        "Income ($)": [50000, 75000, 60000, 80000, 45000],
        "Education Level": [
            "High School",
            "Bachelor's",
            "Master's",
            "Ph.D.",
            "Associate's",
        ],
        "Marital Status": ["Married", "Single", "Married", "Single", "Married"],
    }
    return pd.DataFrame(data)


def main():
    df = build_dataframe()

    print("Sample Data:")
    print(df)

    # Education level is ordinal, so its categories have a meaningful order
    # (the mode of an ordinal variable is still a valid summary).
    print("\nStatistics:")
    print("Mean Age:", df["Age"].mean())
    print("Median Income:", df["Income ($)"].median())
    print("Mode of Marital Status:", df["Marital Status"].mode().iloc[0])

    numerical_variables = ["Age", "Height (inches)", "Income ($)"]
    nominal_variables = ["Marital Status"]
    ordinal_variables = ["Education Level"]

    print("\nNumerical Variables:", numerical_variables)
    print("Nominal Variables:", nominal_variables)
    print("Ordinal Variables:", ordinal_variables)


if __name__ == "__main__":
    main()
