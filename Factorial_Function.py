"""
**Factorial Function : Write function Factorial() that prints factorial of a given number.
"""

def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)
    
print(Factorial(6))    