"""
 **Bitwise Operator Task**:
   Given two integers, write a Python program that:
   - Prints the result of `a & b`, `a | b`, and `a ^ b`.
   - Shifts the bits of `a` two positions to the left (`a << 2`).
   - Shifts the bits of `b` one position to the right (`b >> 1`).
"""
a = int(input("Enter First Integer >> "))
b = int(input("Enter Second Integer >> "))

print(f"The of (a & b) is {a & b}")
print(f"The of (a | b) is {a | b}")
print(f"The of (a ^ b) is {a ^ b}")
print(f"After Shifting the bits of `a` two positions to the left {a << 2}")
print(f"After Shifting the bits of `b` one positions to the right {b >> 1}")

