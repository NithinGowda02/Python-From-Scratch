"""
**Logical Operator Practice**:
   Write a Python program that takes two numbers as input from the user and checks if:
   - Both numbers are greater than 10 (using `and`).
   - At least one of the numbers is less than 5 (using `or`).
   - The first number is not greater than the second (using `not`).
   """
First_number =  int(input("Enetr the First Number >> "))
Second_number =  int(input("Enetr the Second Number >> "))

print(f"AND >>{First_number >10 and Second_number>10} ")
print(f"OR >>{First_number <5 or Second_number>5} ")
print(f"NOT >>{not(First_number > Second_number)} ")      