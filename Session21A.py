import datetime
import hashlib 

class User:
    def __init__(self , name = "", phone = "", email = "", password = "", age = "", gender = ""):
        self.name = name 
        self.phone = phone 
        self.email = email 
        self.password = password 
        self.age = age 
        self.gender = gender 
        self.created_on = datetime.datetime.now()

    def add_user_details(self):
        self.name = input("Enter name:")
        self.phone = input("Enter phone:")
        self.email = input("Enter email:")
        self.password = input("Enter password:").encode('utf-8')
        self.password = hashlib.sha256(self.password).hexdigest()
        self.age = int(input("Enter age:"))
        self.gender = input("Enter gender:")

#user = User()
#user.add_user_details()
#print(vars(user))