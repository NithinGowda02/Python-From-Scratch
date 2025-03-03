"""
**Simple Eligibility Check**:
   - Write a program that checks whether a person is eligible for a library membership. If they are under 18, they get a student membership. If they are 60 or older, they get a senior citizen membership. Otherwise, they get a regular membership.
"""

Person_age = int(input("Enter Your Age >> "))
if Person_age < 18:
    print("They get a student membership")
elif Person_age >=60:
    print("They get a senior citizen membership")
else:
    print("They get a regular membership")        
