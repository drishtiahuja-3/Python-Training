class book():
    def __init__(self, name, location, contact, openingHours, closingHours, category):
        self.name = name
        self.location = location
        self.contact = contact
        self.openingHours = openingHours
        self.closingHours = closingHours
        self.category = category

    def show(self):
        print("\n\n\t\tRestaurant : ")
        print("*****************************************************")
        print("Name of the restaurant: ", self.name)
        print("Location of the restaurant: ", self.location)
        print("Contact of the restaurant: ", self.contact)
        print("Opening time of the restaurant: ", self.openingHours)
        print("Closing time of the restaurant: ", self.closingHours)
        print("Category of the restaurant: ", self.category)
        print("*****************************************************")



while True:
    i = int(input("Enter 1 to fill restaurant information or 0 to exit :"))
    if i == 1 :
        name = input("\nEnter Name of Restaurant: ")
        location = input("Enter Location of Restaurant: ")
        contact = int(input("Enter Contact of Restaurant: "))
        openingHours = int(input("Enter the opening time in Hours: "))
        closingHours = int(input("Enter the closing time in Hours: "))
        category = input("Enter the Category of Restaurant: ")
        restaurant = book(name, location, contact, openingHours, closingHours, category)
        restaurant.show()

    else:
        print("No information filled...")
        break
    