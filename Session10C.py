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
from Session10B import Vehicle

class Driver:
    def __init__(self, name= "NA", phone= "NA", email= "NA", license_id= "NA", rating = 1.5, gender= "NA", age = 18, vehicle = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.license_id = license_id
        self.rating = rating
        self.gender = gender
        self.age = age
        self.vehicle = vehicle

    def add_driver_details(self):
        print("***************Enter Driver Details*****************************")
        self.name = input("Enter the Driver Name : ")
        self.phone = input("Enter the Driver Phone: ")
        self.email = input("Enter the Driver Email: ")
        self.license_id = input("Enter the Driver License Number: ")
        self.rating = input("Enter the Driver Ratings: ")
        self.gender = input("Enter the Driver Gender: ")
        self.age = input("Enter the Driver Age: ")
        
    
        self.vehicle = Vehicle() #object constructor 
        self.vehicle.add_vehicle_details()


    def show(self):
        print("--------------------------------DRIVER--------------------------------")
        print("  Name:  {}  |   Phone:  {}".format(self.name, self.phone))
        print("  Email:  {}  |   License:  {}".format(self.email, self.license_id))
        print("  Rating:  {}  |   Gender:  {}  |  Age:  {}".format(self.rating, self.gender, self.age))
        print("------------------------------------------------------------------------")

        self.vehicle.show()

"""
driver = Driver()
driver.add_driver_details()
driver.show()
"""