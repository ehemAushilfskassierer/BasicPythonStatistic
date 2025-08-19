"""
a_003_Beginner_CountPlotOfPassengerClass

Count Plot of Passenger Class
Load titanic and create a countplot of passengers grouped by class.
"""
import seaborn as sns
import matplotlib.pyplot as plt

dfTitanic = sns.load_dataset("titanic")

print(dfTitanic.head())
print(f"{dfTitanic.columns = }")
sns.countplot(data=dfTitanic, x="who", hue="class")

plt.title("Countplot of passengers grouped by class\nTitanic Dataset")
plt.show()