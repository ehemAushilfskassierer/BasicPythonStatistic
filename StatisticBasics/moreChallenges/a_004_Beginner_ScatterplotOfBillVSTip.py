"""
a_004_Beginner_ScatterplotOfBillVSTip

Scatterplot of Bill vs. Tip
Use tips to plot total_bill vs. tip and add a regression line with sns.regplot().
"""
import seaborn as sns
import matplotlib.pyplot as plt

dfTips = sns.load_dataset("tips")

print(dfTips.head())

plt.scatter(data=dfTips, x="total_bill", y="tip", label="raw data")
plt.title("Scatterplot of Bill vs. Tip")
sns.regplot(data=dfTips, x="total_bill", y="tip", label="regression line")
plt.legend()
plt.grid()
plt.show()