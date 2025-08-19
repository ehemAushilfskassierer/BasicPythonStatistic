"""
a_005_Beginner_PairplotOfPenguins

Pairplot of Penguins
Load penguins and create a pairplot (sns.pairplot) of numeric features, color by species.
"""
import seaborn as sns
import matplotlib.pyplot as plt

dfPenguins = sns.load_dataset("penguins")

print(dfPenguins.head())

# Drop missing values (important for pairplot)
dfPenguins = dfPenguins.dropna()

g = sns.pairplot(data=dfPenguins, hue="species")
g.fig.suptitle("Pairplot of numeric features by species\nPenguins Dataset",
               y=1.02, fontsize=14)

plt.show()