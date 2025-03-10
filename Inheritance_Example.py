class Family:
    def __init__(self, surname):
        self.surname = surname
class child(Family):
    def __init__(self, surname, name):
        super().__init__(surname)
        self.name = name  

obj = child("Gowda","Nithin")
print(f"{obj.name} {obj.surname}")                  
