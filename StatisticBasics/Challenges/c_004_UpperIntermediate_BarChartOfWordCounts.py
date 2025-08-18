"""
c_004_UpperIntermediate_BarChartOfWordCounts

Bar Chart of Word Counts
Given text = "the cat sat on the mat", count each word and visualize using plt.bar().
"""
import matplotlib.pyplot as plt
import collections

strText = "the cat sat on the mat"
counts = collections.Counter(strText.split())
print(counts)

lstWords = list(counts.keys())
lstSizes = list(counts.values())

plt.figure(figsize=(4, 6))
plt.bar(lstWords, lstSizes)
plt.title("c_004_UpperIntermediate_BarChartOfWordCounts")
plt.show()