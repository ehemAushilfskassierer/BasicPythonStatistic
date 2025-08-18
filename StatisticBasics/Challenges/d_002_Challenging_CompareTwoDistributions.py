"""
d_002_Challenging_CompareTwoDistributions

Compare Two Distributions
Create two sets of 100 random values, plot both as overlapping histograms with transparency.
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Create two sets of 100 random values
# Dist A: mean 0, std 1
a = rng.normal(loc=0, scale=1, size=100)
# Dist B: mean 1, std 1.5
b = rng.normal(loc=1, scale=1.5, size=100)

plt.figure(figsize=(7, 5))
plt.hist(a, bins="auto", alpha=0.6, density=True, label="Dist A (μ=0, σ=1)")
plt.hist(b, bins="auto", alpha=0.6, density=True, label="Dist B (μ=1, σ=1.5)")
plt.title("d_002_Challenging_CompareTwoDistributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)
plt.show()
