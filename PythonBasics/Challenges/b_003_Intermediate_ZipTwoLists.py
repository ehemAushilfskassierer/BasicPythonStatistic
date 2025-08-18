"""
003_Intermediate_ZipTwoLists

Zip Two Lists
Given [1, 2, 3] and ['a', 'b', 'c'], use zip() to combine them into pairs.
"""
lstNums = [1, 2, 3]
lstChar = ['a', 'b', 'c']

print(f"{lstNums = }")
print(f"{lstChar = }")

print(f"{zip(lstNums, lstChar) = }")
print(f"{list(zip(lstNums, lstChar)) = }")
