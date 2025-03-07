"""
**Find Largest Number**: Write a largest() function. Call this function with different values.
"""
def largest(a, b, c):
    if a >= b and a >= c:
        print(f"{a} is the Largest Number...")
    elif b >= a and b >= c:
        print(f"{b} is the Largest Number...")
    else:
        print(f"{c} is the Largest Number...")    

largest(12,34,74)
