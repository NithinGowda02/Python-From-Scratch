class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects
person1 = Person("Arjun", 30)
person2 = Person("Megha", 25)

person1.greet()
person2.greet()