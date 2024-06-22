"""
Customer: name, phone, email, address, number_of_orders 
Order: id, amount, number_of_dishes
Dish: name, price, rating


1 customer can place many orders
1 order can have many dishes
"""
class Order:
    def insertion(self , id = "NA",dishes = None, customer= None , total= 0):
        self.id = id 
        self.dishes = dishes 
        self.customer = customer
        self.total = total
         

    def show(self):
        print("~~~~~~~~~~~~~~~~ORDER~~~~~~~~~~~~~~~~~~")
        print("Dish: {} | {} ".format(self.id, self.total))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print("Order Placed by: ")
        self.customer.show()
        
        print("Dishes:")
        for dish in self.dishes:
            dish.show()

    def link_dishes(self, dishes):
        pass

    def link_customer(self, customer):
        self.customer