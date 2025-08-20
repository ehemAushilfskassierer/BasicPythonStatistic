"""
b_001_Intermediate_GenderSurvivalRate

Gender Survival Rate (Titanic)
Use titanic to calculate survival rate by gender. Visualize with a bar chart.
"""
import seaborn as sns
import matplotlib.pyplot as plt

dfTitanic = sns.load_dataset("titanic")

print(dfTitanic.head())

survivalrateByGender = dfTitanic.groupby("sex")["survived"].mean()

sns.barplot(data=survivalrateByGender)
plt.title("Survivalrate Titanic grouped by gender")
plt.show()