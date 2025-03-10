"""
**Inheritance**:
   - Create a base class `Vehicle` with a `start` method. Then create a subclass `Bike` with an additional `ride()` method.
   - Demonstrate how the `Bike` can use both `start` and `ride`.
"""
class Vehicle:
    def start(self):
        print("Engine Started..")
class Bike(Vehicle):
    def ride(self):
        print("Riding the Bike..")  
bike = Bike()
bike.start()              
bike.ride()
