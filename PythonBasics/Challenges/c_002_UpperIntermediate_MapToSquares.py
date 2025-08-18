"""
002_UpperIntermediate_MapToSquares

Map to Squares
Use map() to square each number in [1, 2, 3, 4].
"""
lstNums = [1, 2, 3, 4]

print(lstNums)

print(f"{list(map(lambda x: x**2, lstNums)) = }")