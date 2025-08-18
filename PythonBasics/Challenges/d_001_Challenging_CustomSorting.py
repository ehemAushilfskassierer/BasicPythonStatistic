"""
001_Challenging_CustomSorting

Custom Sorting
Use sorted() with key=len to sort ['pear', 'apple', 'banana', 'fig'] by word length.
"""
lstFruits = ['pear', 'apple', 'banana', 'fig']

print(lstFruits)

print(f"{sorted(lstFruits, key=len) = }")