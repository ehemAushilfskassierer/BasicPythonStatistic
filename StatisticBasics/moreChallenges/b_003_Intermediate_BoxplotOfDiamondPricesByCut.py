"""
b_003_Intermediate_BoxplotOfDiamondPricesByCut

Boxplot of Diamond Prices by Cut
Load diamonds and create a boxplot comparing price distributions by cut.
"""
import seaborn as sns
import matplotlib.pyplot as plt

dfDiamonds = sns.load_dataset("diamonds")

print(dfDiamonds.head())

sns.boxplot(data=dfDiamonds, x="cut", y="price")
plt.title("Diamonds price by cut")
plt.show()

