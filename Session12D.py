from Session12A import Dish
from Session12C import Customer
from Session12B import Order

dish_menu = [Dish(name = "Dal makhani", price = 250, rating = 4.5),
            Dish(name = "Paneer makhani", price = 290, rating = 4.2),
            Dish(name = "Noodles", price = 100, rating = 3.5),
            Dish(name = "Pizza", price = 150, rating = 4.0),
            Dish(name = "Burger", price = 50, rating = 4.5)]

customer1 = Customer(name= "john", phone="+91 99999 11111", email = "john@example.com", address="Redwood Shores")
customer2 = Customer(name= "fionna", phone="+91 99999 22222", email = "fionna@example.com", address="Country Homes")

#order1 = Order(id = "1",dishes = [dish_menu[0], dish_menu[3]], customer= customer1 , total= 400)
#order2 = Order(id = "2",dishes = [dish_menu[2], dish_menu[1]], customer= customer1 , total= 390)
order1 = Order(id="1")
order1.show()
order2.show()