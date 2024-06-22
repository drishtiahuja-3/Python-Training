"""
Customer: name, phone, email, address, number_of_orders 
Order: id, amount, number_of_dishes
Dish: name, price, rating


1 customer can place many orders
1 order can have many dishes
"""
class Dish:
    def __init__(self, name="NA", price=0, rating=1.5):
        self.name = name 
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~~~DISH~~~~~~~~~~~~~~~~~~")
        print("Dish: {} | {} | {}".format(self.name, self.price, self.rating))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



