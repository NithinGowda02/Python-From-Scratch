#### **Real-World Example in Code:**

## ABSTRACTION

class Car:
    def start_engine(self):
        print("Engine started")

    def accelerate(self):
        print("Car accelerating")

    def brake(self):
        print("Car stopping")

car = Car()
car.start_engine()  # Abstracts complex internal workings
car.accelerate()
car.brake()


#Here, `Car` abstracts internal functions like ignition and fuel management, presenting only basic methods for interaction.
