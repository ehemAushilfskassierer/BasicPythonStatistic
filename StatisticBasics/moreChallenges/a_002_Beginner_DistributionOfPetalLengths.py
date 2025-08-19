"""
a_002_Beginner_DistributionOfPetalLengths

Distribution of Petal Lengths
Load iris and plot a histogram of petal_length.
"""
import seaborn as sns
import matplotlib.pyplot as plt

dfIris = sns.load_dataset("iris")

print(dfIris.head())

dfIris["petal_length"].hist()
plt.title("Histogram of 'petal_length' for iris")
plt.xlabel("petal length")
plt.ylabel("count")
plt.show()