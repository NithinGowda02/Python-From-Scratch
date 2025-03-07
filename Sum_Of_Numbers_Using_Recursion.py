"""
**Recursive Function**: Write a recursive function that calculates the sum of the first `n` numbers.
"""
def Recurssion(n):
    if n==1:
        return 1
    return n + Recurssion(n-1)
print(f"Sum of n Number using Recursion >>{Recurssion(5)}")