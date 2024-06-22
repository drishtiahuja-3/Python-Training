"""
Customer: name, phone, email, address, number_of_orders 
Order: id, number_of_dishes,customer, amount
Dish: name, price, rating


1 customer can place many orders
1 order can have many dishes
"""
class Customer:
    def __init__(self, name="NA", phone=0, email="", address=""):
        self.name = name 
        self.phone = phone
        self.email = email
        self.address = address

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~CUSTOMER~~~~~~~~~~~~~~~~~~~~~")
        print("Name: {} | Phone: {} ".format(self.name, self.phone))
        print("Email: {} | Address: {} ".format(self.email, self.address))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


