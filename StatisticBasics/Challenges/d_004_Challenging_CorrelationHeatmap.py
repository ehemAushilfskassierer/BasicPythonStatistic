"""
d_004_Challenging_CorrelationHeatmap

Correlation Heatmap
Generate a pandas.DataFrame with 3 numeric columns, compute correlations, and visualize with seaborn.heatmap().
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    'A': np.random.rand(100),
    'B': np.random.rand(100),
    'C': np.random.rand(100)
})

corr_matrix = df.corr()

sns.set(style='white')
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
