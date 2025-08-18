"""
d_003_Challenging_OutlierDetectionWithIQR

Outlier Detection with IQR
Write code that finds outliers in a dataset using the interquartile range (IQR).
"""
import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")

print(tips.head())

# calculate Q1, Q3 and IQR
Q1 = tips["tip"].quantile(0.25)
Q3 = tips["tip"].quantile(0.75)
IQR = Q3 - Q1

# Define bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = tips[(tips["tip"] < lower_bound) | (tips["tip"] > upper_bound)]
non_outliers = tips[(tips["tip"] >= lower_bound) & (tips["tip"] <= upper_bound)]

print("Outliers:")
print(outliers)
print(f"{outliers.shape = }")

print("\nNon-Outliers:")
print(non_outliers)