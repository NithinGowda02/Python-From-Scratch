## Polymorphism Example...

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Barking")

class Cat(Animal):
    def make_sound(self):
        print("Meow") 

animals = [Dog(),Cat()]   
for animal in animals:
    animal.make_sound()           