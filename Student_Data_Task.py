"""
**Student Data Task**:
   - Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.
"""
Student1 = {"name": "Nithin K P",
            "age": 22,
            "marks": 81.96
            }

Student2 = {"name": "Madan Gowda G R",
            "age": 20,
            "marks": 85.6
            }

Student3 = {"name": "Rahul",
            "age": 23,
            "marks": 87.86
            }

Students = [Student1, Student2, Student3]
print("STUDENT INFORMATION")
print("---------------------")
for information in Students:
    print(information)
