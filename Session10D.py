"""
OLA / UBER CASE STUDY 
customer can book a ride or rides
driver has a vehicle 
vehicle : reg_number, model, color, brand 
driver : name, phone, email, license_id, gender, age , rating,  vehicle_name [1 to 1]
customer: name, phone, email , address , gender, age
ride : customer, date , tolocation, fromlocation, time, distance , fare , driver [1 to 1]
i ride has 1 customer
1 ride has 1 driver
"""
#https://visualgo.net/en/sorting  | implement bubble sort HW



class Customer:
    def __init__(self, name= "NA", phone= "NA", email= "NA", address= "NA", gender= "NA", age = 18):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.gender = gender
        self.age = age

    def add_customer_details(self):
        print("***************Enter Customer Details*****************************")
        self.name = input("Enter Customers Name : ")
        self.phone = input("Enter Customers Phone: ")
        self.email = input("Enter Customers Email: ")
        self.address = input("Enter Customers Address: ")
        self.gender = input("Enter Customers Gender: ")
        self.age = input("Enter Customers Age: ")
        


    def show(self):
        print("--------------------------------CUSTOMER--------------------------------")
        print("  Name:  {}  |   Phone:  {}".format(self.name, self.phone))
        print("  Email:  {}  |   Address:  {} ".format(self.email, self.address))
        print("  Gender:  {}  |   Age:  {}".format(self.gender, self.age))
        print("------------------------------------------------------------------------")

    def to_csv(self):
        data = "{},{},{},{},{},{}\n".format(self.name, self.phone, self.email, self.address, self.gender, self.age)
        return data
"""
customer = Customer()
customer.add_customer_details()
customer.show()
"""