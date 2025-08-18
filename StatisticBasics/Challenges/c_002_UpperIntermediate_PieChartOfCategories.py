"""
c_002_UpperIntermediate_PieChartOfCategories

Pie Chart of Categories
Given categories ['A', 'B', 'C', 'A', 'B', 'A'], plot their distribution as a pie chart.
"""
import matplotlib.pyplot as plt
import collections

lstChars = ['A', 'B', 'C', 'A', 'B', 'A']

counts = collections.Counter(lstChars)
print(counts)

lstLabels = list(counts.keys())
lstSizes = list(counts.values())

plt.figure(figsize=(4, 5))
plt.pie(lstSizes, labels=lstLabels, autopct='%1.1f%%', startangle=90)
plt.title("c_002_UpperIntermediate_PieChartOfCategories")
plt.show()