"""
b_003_Intermediate_BoxplotVisualization

Boxplot Visualization
Generate 50 random integers between 10 and 100 and show a boxplot.
"""
import matplotlib.pyplot as plt
import random

lstNums = random.sample(range(10, 101), 50)

plt.figure(figsize=(4, 5))
plt.boxplot(lstNums)
plt.title("b_003_Intermediate_BoxplotVisualization")
plt.show()