"""
b_004_Intermediate_ScatterPlot

Scatter Plot
Plot a scatter chart of x = [1,2,3,4,5] and y = [2,4,5,4,5] using matplotlib.pyplot.scatter().
"""
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,5,4,5]

plt.figure(figsize=(4, 5))
plt.scatter(x, y)
plt.title("b_004_Intermediate_ScatterPlot")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()