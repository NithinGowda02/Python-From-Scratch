"""
** Prime Number ** : write a function that Checks weather the given number is prime or not.
"""
def Prime_Number(n):
    if n <= 1:
        return f"{n} is not a Prime Number..."
    elif n % 2 == 0:
        return f"{n} is not a Prime Number..."
    return f"{n} is a Prime Number..."

print(Prime_Number(7))
print(Prime_Number(4))