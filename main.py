# Week 1: Water Quality Dataset - Initial Analysis

import pandas as pd

# 1. Load the dataset
data = pd.read_csv("water_quality.csv", sep=';')

# 2. Display first 5 rows
print("🔹 First 5 Rows:")
print(data.head())

# 3. Show structure of the dataset
print("\n🔹 Dataset Info:")
print(data.info())

# 4. Summary statistics
print("\n🔹 Summary Statistics:")
print(data.describe())

# 5. Check for missing values
print("\n🔹 Missing Values:")
print(data.isnull().sum())

# 6. Drop rows with missing values
data = data.dropna()
print(f"\n🔹 Dataset shape after dropping nulls: {data.shape}")

# 7. Drop columns not needed for analysis
data = data.drop(['id', 'date'], axis=1)
print(f"\n🔹 Final columns used for analysis: {list(data.columns)}")
