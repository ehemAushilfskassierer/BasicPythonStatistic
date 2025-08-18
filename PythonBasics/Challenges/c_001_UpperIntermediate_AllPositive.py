"""
001_UpperIntermediate_AllPositive

All Positive
Use all() to check if all numbers in [3, 5, 7, 9] are positive.
"""
lstNums = [3, 5, 7, 9]

print(lstNums)

print(f"{all(lstNums) = }")

lstNegNums = [-1 * num for num in lstNums]

print(lstNegNums)

print(f"{all(lstNegNums) = }")

lstNegNums.append(0)

print(lstNegNums)

print(f"{all(lstNegNums) = }") # no zero element allowed

print(f"{any(lstNegNums) = }") # at least one non-zero element has to be found

lstBool = [False, False, False, True]

print(lstBool)

print(f"{all(lstBool) = }")

print(f"{any(lstBool) = }")