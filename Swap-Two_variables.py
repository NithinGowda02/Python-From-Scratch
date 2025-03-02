"""
**Swap Two Variables:**
   Write a Python program that swaps the values of two variables with and without using a third variable.
"""

Name1 = "M S DHONI"
Name2 = "VIRAT KOHLI"
print(f"Before swapping two variables \nName1 >> {Name1}\nName2 >> {Name2}")
Name1,Name2=Name2,Name1
print(f"After swapping two variables \nName1 >> {Name1}\nName2 >> {Name2}")
