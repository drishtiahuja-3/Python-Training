from Session10D import Customer
from Session10B import Vehicle
from Session10C import Driver
from Session10F import Ride

#driver application
driver = Driver()
driver.add_driver_details()

#customer application
customer = Customer()
customer.add_customer_details()


#ride application
ride = Ride()
ride.add_ride_details()

ride.link_customer(customer)
ride.link_driver(driver)
print("Ride booked...")
ride.show()
