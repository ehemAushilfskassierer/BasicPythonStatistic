"""
d_001_Challenging_RollingAverageVisualization

Rolling Average Visualization
Generate 100 random integers between 1 and 50, compute a rolling average (window=5) using pandas, and plot it.
"""
import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

lstNums = [random.randint(1, 50) for _ in range(100)]
print(lstNums)

df = pd.DataFrame(lstNums, columns=["Random values"])

df["Rolling average"] = df["Random values"].rolling(window=5).mean()

plt.figure(figsize=(5, 6))
plt.plot(df["Random values"], label="Original data", alpha=0.7)
plt.plot(df["Rolling average"], label="Rolling average (window=5)",
         color="green", linewidth=2, linestyle="dashed")
plt.title("d_001_Challenging_RollingAverageVisualization")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()