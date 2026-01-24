"""
004_Challenging_BinaryConversion

Binary Conversion
Use bin() to convert 12 into binary.
"""

intValue = 12

print(intValue)

print(f"{bin(intValue) = }")

print(f"{int(bin(intValue), 2) = }")

a, b = 8, 9

print(f"{bin(a) = }\t{bin(b) = }")

print(f"{bin(a & b) = }\t{a & b = }")

print(f"{bin(a | b) = }\t{a | b = }")