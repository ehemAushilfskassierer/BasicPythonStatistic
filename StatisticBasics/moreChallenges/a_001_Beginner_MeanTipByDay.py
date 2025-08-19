"""
a_001_Beginner_MeanTipByDay

Mean Tip by Day
Load the tips dataset and calculate the average tip given on each day of the week.
"""
import seaborn as sns

dfTips = sns.load_dataset("tips")

print(dfTips.head())

print(f"\nAverage tip per day:")
print(dfTips.groupby("day", observed=True)["tip"].mean())