import pandas as pd
# Sample data for demonstration
data = {
    'A': [10, 20, 30, 40, 50],
    'B': [5, 15, 25, 35, 45],
    'C': [12, 22, 32, 42, 52]
}
# Create a DataFrame from the data
df = pd.DataFrame(data)

# Function to perform various statistical measures
def perform_statistics(df):
    print("Data:")
    print(df)

    # Mean of each column
    print("\nMean of each column:")
    print(df.mean())

    # Median of each column
    print("\nMedian of each column:")
    print(df.median())

    # Standard deviation of each column
    print("\nStandard deviation of each column:")
    print(df.std())

    # Variance of each column
    print("\nVariance of each column:")
    print(df.var())

    # Minimum value of each column
    print("\nMinimum value of each column:")
    print(df.min())

    # Maximum value of each column
    print("\nMaximum value of each column:")
    print(df.max())

    # Correlation between columns
    print("\nCorrelation between columns:")
    print(df.corr())

    # Description of the dataset (includes mean, std, min, 25%, 50%, 75%, max)
    print("\nSummary statistics (including mean, std, min, 25%, 50%, 75%, max):")
    print(df.describe())

# Call the function to perform statistical measures
perform_statistics(df)