"""
005_Intermediate_CheckAnyTrue

Check Any True
Use any() to check if any number in [0, 0, 3, 0] is non-zero.
"""
lstNums = [0, 0, 3, 0]

print(lstNums)

print(f"{any(lstNums) = }") # True if True or non-zero element in list

lstBool = [False, False, False, True]

print(lstBool)

print(f"{any(lstBool) = }")