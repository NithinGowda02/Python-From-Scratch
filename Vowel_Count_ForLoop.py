"""
 **Count Vowels in a String**:
   - Write a program that counts how many vowels are in a given string using a `for` loop.

"""
vowels = ['a','e','i','o','u']
vowels_count = 0
Given_String = input("Enter a String >> ")

for i in Given_String:
    if i in vowels:
        vowels_count +=1
print(vowels_count)    