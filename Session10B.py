"""
OLA / UBER CASE STUDY 
customer can book a ride or rides
driver has a vehicle 
vehicle : reg_number, model, color, brand 
driver : name, phone, email, license_id, gender, age , rating,  vehicle_name [1 to 1]
customer: name, phone, email , address ,ride, gender, age
ride : customer, date , tolocation, fromlocation, time, distance , fare , driver [1 to 1]
i ride ahs 1 customer
1 ride has 1 driver

"""

class Vehicle:
    def __init__(self, reg_number = "NA", brand = "NA",model = "NA", color = "white"):
        self.reg_number = reg_number
        self.brand = brand
        self.model = model
        self.color = color

    def add_vehicle_details(self):
        print("***************Enter Vehicle Details*****************************")
        self.reg_number = input("Enter the Vehicle Registeration Number: ")
        self.brand = input("Enter the Vehicle Brand: ")
        self.model = input("Enter the Vehicle Model: ")
        self.color = input("Enter the Vehicle Color: ")

    def show(self):
        print("--------------------------------VEHICLE--------------------------------")
        print("  Number:  {}  |   Brand:  {}".format(self.reg_number, self.brand))
        print("  Model:  {}  |   Color:  {}".format(self.model, self.color))
        print("------------------------------------------------------------------------")
"""
vehicle = Vehicle()
vehicle.add_vehicle_details()
vehicle.show()
"""