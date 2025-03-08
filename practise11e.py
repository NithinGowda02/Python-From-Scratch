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