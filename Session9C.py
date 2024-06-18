#PRACTICE FILE OF SESSION 9,9A,9B

"""
    Code 3 Objects
    1. Dish : name, price, rating
    2. Menu : name, number_of_dishes, dishes 
        1 Menu can have many Dishes (1 to many)
    3. Restaurant : name, phone, email, address, operating_hours, ratings, menu
        1 Restaurant can have 1 Meny (1 to 1)
"""
class Dish:
    def __init__(self, name = "NA", price = 0, rating = 1.5):
        self.name = name
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("DISHES: {}   |   {}  |   {}  ".format(self.name, self.price, self.rating))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

"""
dishes = [
            Dish(),
            Dish("Dal Makhani", 250, 4.5),
            Dish("Shahi Paneer", 300, 4.7)
        ]

for idx in range(len(dishes)):
    dishes[idx].show()
"""
class Menu:
    def __init__(self, name = "NA", number_of_dishes = "NA", menu_dishes =[]):
        self.name = name 
        self.number_of_dishes = number_of_dishes 
        self.menu_dishes = menu_dishes 


    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("MENU:   {}   |Number of Dishes:   {}   ".format(self.name, self.number_of_dishes))
        for idx in range(3):
            self.menu_dishes[idx].show()
        
"""
menu = Menu(
    name = "Veggie Delight", 
    number_of_dishes = 3,
    menu_dishes = [
            Dish(),
            Dish("Dal Makhani", 250, 4.5),
            Dish("Shahi Paneer", 300, 4.7)
        ]
)
menu.show()
"""
class Restaurant:
    def __init__(self, name = "NA", phone = "NA", email = "NA", address = "NA", operating_hours = "10 to 11:30", ratings = 3, menu =[] ):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.operating_hours = operating_hours 
        self.ratings = ratings
        self.menu = menu

    def show(self):
        print("*****************************************************")
        print("RESTAURANT NAME :   {}\nPHONE:   {}\nEMAIL:   {}\nADDRESS:   {}\nOPERATING HOURS:   {}\nRATINGS:   {} ".format(self.name, self.phone, self.email,self.address,self.operating_hours, self.ratings))
        self.menu.show()
        print("*******************************************************\n")

restaurant = Restaurant(name="Ludhiana Veggie Delight",
                        phone="+91 99999 11111",
                        email="veggies@abc.com",
                        address="Krishna Nagar", 
                        ratings=4.5,
                        menu=Menu(
                            name="Indian Veggie Delight", 
                            number_of_dishes=3, 
                            menu_dishes=[
                                        Dish(), 
                                        Dish("Dal Makhani", 250, 4.5),
                                        Dish(name="Paneer Masala", price=350, rating=4.5)
                                    ])
                        )
restaurant.show()