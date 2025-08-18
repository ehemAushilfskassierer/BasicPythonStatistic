"""
b_005_Intermediate_correlationCalculation

Correlation Calculation
Use numpy.corrcoef() to find the correlation between [1, 2, 3, 4] and [2, 4, 6, 8].
"""
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

# https://en.wikipedia.org/wiki/Correlation_coefficient
corr_matrix = np.corrcoef(x, y)

print(f"{x = }\n{y = }")
print(f"Correlation matrix:\n{corr_matrix}")
print(f"Correlation between x and y = {corr_matrix[0,1]}")

# Optional visualization
plt.plot(x, y, linestyle='dashed', marker='o')
plt.title("b_005_Intermediate_correlationCalculation")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()