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

from Session10D import Customer
from Session10B import Vehicle
from Session10C import Driver

class Ride:
    def __init__(self, customer= None, date="20th June 2024", time= "12:00", fromlocation= "Home", tolocation = "work", distance= 4, fare= 200, driver = None):
        self.customer = customer
        self.date = date
        self.time = time
        self.fromlocation = fromlocation
        self.tolocation = tolocation
        self.distance = distance
        self.fare = fare
        self.driver = driver

    def add_ride_details(self):
        print("***************Enter Ride Details*****************************")
        self.fromlocation = input("Enter From location: ")
        self.tolocation = input("Enter To location: ")

    def link_customer(self, customer):
        self.customer = customer

    def link_driver(self, driver):
        self.driver = driver

    def show(self):

        self.customer.show()
        print("--------------------------------RIDE--------------------------------")
        print("  From:  {}  |   To:  {}".format(self.fromlocation, self.tolocation))
        print("  Distance:  {}  |   Fare:  {} ".format(self.distance, self.fare))
        print("  Date:  {}  |   Time:  {}".format(self.date, self.time))
        print("------------------------------------------------------------------------")
        self.driver.show()


