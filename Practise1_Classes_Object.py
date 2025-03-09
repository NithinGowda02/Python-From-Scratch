"""
**Create a Class**:
   - Write a class `Mobile` with attributes `brand` and `price`.
   - Create two objects of the class and display their attributes using a method.
"""
class Mobile:
    def __init__(self,brand, price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f"{self.brand} has {self.price} price")  
Samsung = Mobile("Samsung S23",50999)
iphone = Mobile("iPhone 16",69999)
Samsung.display()
iphone.display()