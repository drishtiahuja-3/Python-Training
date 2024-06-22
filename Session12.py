#Sorting objects 
# selection insertion and merge sort homework
# swap operation a[j],a[j+1]=a[j+1],a[j]


class Dish:
    def __init__(self, name="NA", price=0, rating=1.5):
        self.name = name 
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~~~DISH~~~~~~~~~~~~~~~~~~")
        print("Dish: {} | {} | {}".format(self.name, self.price, self.rating))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def sort(lst):
    n = len(lst)
    for i in range(n):
    
        for idx in range(n-i-1):
            if lst[idx].price > lst[idx+1].price:
                #if lst[idx].rating < lst[idx+1].rating:
                lst[idx],lst[idx+1] = lst[idx+1],lst[idx]
#list of dish objects


dishes = [Dish(name = "Dal makhani", price = 250, rating = 4.5),
            Dish(name = "Paneer makhani", price = 290, rating = 4.2),
            Dish(name = "Noodles", price = 100, rating = 3.5),
            Dish(name = "Pizza", price = 150, rating = 4.0),
            Dish(name = "Burger", price = 50, rating = 4.5)]


for dish in dishes:
    dish.show()

sort(dishes)
print("\n\n~~~~~~~~~~~~~SORTED DISHES~~~~~~~~~~~~~~~")
for dish in dishes:
    dish.show()