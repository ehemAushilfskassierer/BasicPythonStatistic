"""
c_001_UpperIntermediate_StandardDeviation

Standard Deviation
Use statistics.stdev() to calculate the standard deviation of [10, 12, 23, 23, 16, 23, 21, 16].
"""
import statistics

lstNums = [10, 12, 23, 23, 16, 23, 21, 16]

print(lstNums)

# https://en.wikipedia.org/wiki/Standard_deviation
print(f"{statistics.stdev(lstNums) = }")