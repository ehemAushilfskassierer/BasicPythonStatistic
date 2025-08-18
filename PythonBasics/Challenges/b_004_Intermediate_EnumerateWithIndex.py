"""
004_Intermediate_EnumerateWithIndex

Enumerate with Index
Use enumerate() to print each item of ['apple', 'banana', 'cherry'] with its index.
"""
lstFruits = ['apple', 'banana', 'cherry']

print(lstFruits)

for index, fruit in enumerate(lstFruits):
    print(f"Index {index}: {fruit}")