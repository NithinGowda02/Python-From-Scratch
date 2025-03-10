class user:
    def __init__(self, Username, Password):
        self.Username = Username
        self.__password = Password
    def get_username(self):
        return self.Username  

    def check_Password(self, password):
        if self.__password == password:
            print(f"Password is correct Login Successful....")
        else:
            print(f"Incorect Password..!")    

user = user("NITHIN","Nit_02@2002") 
print(user.get_username())

user.check_Password("Nit_02@2002")  
            