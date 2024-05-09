import numpy as np
import pandas as pd

df = pd.read_csv("C:\\Users\\ASUS\\OneDrive - ADA University\\Desktop\\Data and Information Engineering(Spring2024)\\Team Project\\Movie Dataset.csv")

df['Vote_Count'] = pd.to_numeric(df['Vote_Count'], errors='coerce')  # Convert to int64
df['Vote_Average'] = pd.to_numeric(df['Vote_Average'], errors='coerce')  # Convert to float64

print(df.describe(include=[float, int]))


df['Popularity'] = df['Popularity'].fillna(df['Popularity'].median())  # Fill with the mean
df['Vote_Count'] = df['Vote_Count'].fillna(df['Vote_Count'].median())  # Fill with the median
df['Vote_Average'] = df['Vote_Average'].fillna(df['Vote_Average'].mean())  # Fill with a specific value

print("Data after custom imputation:")
print(df.describe(include=[float, int]))

def replace_outliers_with_cap(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return series.apply(lambda x: np.clip(x, lower_bound, upper_bound))

# Apply the outlier replacement function to relevant columns
df['Popularity'] = replace_outliers_with_cap(df['Popularity'])
df['Vote_Count'] = replace_outliers_with_cap(df['Vote_Count'])
df['Vote_Average'] = replace_outliers_with_cap(df['Vote_Average'])

print("DataFrame after replacing outliers:")
print(df.describe(include=[float, int]))


