"""
b_005_Intermediate_CorrelationHeatmap

Correlation Heatmap
Load iris and compute a correlation matrix of numerical variables, visualize with sns.heatmap.
"""
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

dfIris = sns.load_dataset("iris")

print(dfIris.head())

correlationMatrix = dfIris.corr(numeric_only=True)
print(correlationMatrix)

sns.heatmap(correlationMatrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Iris Dataset")
plt.show()