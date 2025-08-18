"""
003_UpperIntermediate_FilterEvenNumbers

Filter Even Numbers
Use filter() to extract even numbers from [10, 15, 20, 25].
"""
lstNums = [10, 15, 20, 25]

print(lstNums)

print(f"{list(filter(lambda x : x & 1 == False, lstNums)) = }")