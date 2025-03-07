"""
**Multiplication Tables**: Write a function that prints the Tables of given function. Call this function with different values.
"""
def Tables(num):
    for i in range(1,11):
        print(f"{num}X{i}={num*i}")
Tables(99)        
