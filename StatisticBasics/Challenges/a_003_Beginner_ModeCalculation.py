"""
a_003_Beginner_ModeCalculation

Mode Calculation
Use statistics.mode() to find the most common number in [1, 2, 2, 3, 3, 3, 4].
"""
import statistics

lstNums = [1, 2, 2, 3, 3, 3, 4]

print(lstNums)

print(f"{statistics.mode(lstNums) = }")