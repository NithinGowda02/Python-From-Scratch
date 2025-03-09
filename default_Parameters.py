"""
**Add Default Parameters**:
   - Create a class `Employee` with attributes `name`, `designation`, and `salary` (default value of `salary` is 30,000).
   - Write a method that displays the details of each employee.
   - Create multiple `Employee` objects with different values for `name` and `designation`, and test the default `salary` behavior.
"""

class Employee:
    def __init__(self, name, designation, salary = 30000):
        self.name = name
        self.designation = designation
        self.salary = salary
    def display_details(self):
        print(f"{self.name} is a {self.designation} with {self.salary} Salary")   

emp = Employee("Nithin K P","Full Stack Developer")       
emp.display_details()  