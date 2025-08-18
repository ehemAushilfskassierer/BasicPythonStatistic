"""
b_002_Intermediate_HistogramOfAges

Histogram of Ages
Given ages [12, 15, 20, 20, 22, 22, 25, 30], create a histogram using matplotlib.pyplot.hist().
"""
import matplotlib.pyplot as plt

lstAges = [12, 15, 20, 20, 22, 22, 25, 30]

plt.figure(figsize=(4, 5))
plt.hist(lstAges)
plt.title("b_002_Intermediate_HistogramOfAges")
plt.show()
