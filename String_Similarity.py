string1=input("enter the string 1: ")
string2=input("enter the string 2: ")

similarity = sum(a == b for a,b in zip(string1,string1))/max(len(string1),len(string2))

print("original string :")
print(string1)
print(string2)
print("similarity between two said string is:",similarity)