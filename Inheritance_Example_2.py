#Inheritance Example

class user:
    def __init__(self, username):
        self.username = username
    def user_login(self):
        print(f"{self.username} logged in..")

class Admin(user):
    def delete_user(self, user):
        print(f"Admin {self.username} deleted {user}")  

admin = Admin("Nithin K P")
admin.user_login()  
admin.delete_user("user@123")                