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

from Session10D import Customer
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("WELCOME TO CUSTOMER MANAGEMENT SYSTEM")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("1. Add customer details ")
print("2. View customer details ")
print("3. Exit")

while True:
    choice = int(input("Enter The choice:"))
    if choice == 1:
        file = open("customer.csv", "a")
        customer = Customer()
        customer. add_customer_details()
        customer.show()

        data = customer.to_csv()
        file.write(data)
        print("Data written...", data)


    elif choice ==2 :
        file = open("customer.csv","r")
        lines = file.readlines()
        for line in lines:
            print(line)

    elif choice == 3:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("THANK U FOR USING CUSTOMER MANAGEMENT SYSTEM")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        file.close()
        break
    else: 
        print("Invalid choice...")
        break
