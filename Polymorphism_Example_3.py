"""
**Polymorphism**:
   - Implement a `Shape` class and derive `Circle` and `Rectangle` classes with a method `calculate_area`. Each class should calculate area differently based on its shape.
   - Create a loop to calculate areas for both `Circle` and `Rectangle` objects.
"""

class Shape:
    pass
class Circle(Shape):
    def calculate_area(self, radius, pi=3.142):
        self.radius = radius
        print(f"Area of Circle >> {pi*self.radius*self.radius}")

class Rectangle(Shape):
    def calculate_area(self, length, breadth):
        self.length = length
        self.breadth = breadth
        print(f"Area of Rectangle >> {self.length * self.breadth}")

areas = [Circle(), Rectangle()]
for area in areas:
    
    area.calculate_area(3,4)