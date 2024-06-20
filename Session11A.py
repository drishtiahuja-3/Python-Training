#.csv is an excel file 
name = input("\nEnter Customer Name: ")
phone = input("Enter Customer Phone: ")
email = input("Enter Customer Email: ")


customer_details = "{} , {} , {}\n ".format(name, phone, email)

file = open("customer.csv","a")
file.write(customer_details)
print("Customer Data Saved.....")
file.close()
