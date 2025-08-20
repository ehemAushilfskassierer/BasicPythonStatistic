"""
b_004_Intermediate_TipPercentageDistribution

Tip Percentage Distribution
In tips, calculate tip_pct = tip / total_bill, and plot its distribution with KDE.
"""
import seaborn as sns
import matplotlib.pyplot as plt

dfTips = sns.load_dataset("tips")

print(dfTips.head())

dfTips["tip_pct"] = dfTips.tip / dfTips.total_bill

sns.kdeplot(data=dfTips, x="tip_pct", fill=True)
plt.title("Tip percentage distribution with KDE")
plt.xlabel("Tip % of Total Bill")
plt.ylabel("Density")
plt.show()