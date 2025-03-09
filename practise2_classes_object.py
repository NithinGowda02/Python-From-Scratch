"""
**Method Definition**:
   - Define a class `Student` with attributes `name` and `marks`.
   - Write a method `display_info()` that prints the student's name and marks.
   - Create multiple objects of the `Student` class and call the method on each.
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display_info(self):
        print(f"{self.name} has Scored >> {self.marks}")  

student1 = Student("Nithin K P",90)
student2 = Student("Madan Gowda G R",85)

student1.display_info()
student2.display_info()