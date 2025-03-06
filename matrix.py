"""
**Nested List Challenge**:
   Write a Python program that takes a list of lists (a 2D list) as input and:
   - Prints the entire matrix row by row.
   - Prints the sum of each row in the matrix.
"""
mat1=int(input("enter the element >> "))
mat2=int(input("enter the element >> "))
matrix=[]
for i in range(mat1):
    row=[]
    for  j in  range(mat2):
        x=int(input("enter the element to matrix >> "))
        row.append(x)
    matrix.append(row)
print(matrix)        