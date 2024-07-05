#python file is also called module 

""" 
**introduction to mysql
**sql commands 
    ~varchar variable character string 
    ~ORM technique - Object Relational mapping
    #show databases;
    #create database python;
    #use python;
    #show tables;

    #create table Customer(
    cid int primary key auto_increment,
    name varchar(256), 
    phone varchar(15), 
    email varchar(256),  
    age int,
    gender varchar(10)
    );
     
    #describe customer
    
    #insert into customer value(null, 'john', '+91 99999 11111', 'john@example.com', 20, 'male');
    #select * form customer;
    #select name, phone from Customer where cid = 2;
    #select * from Customer where gender = 'male' and age >= 18;
    # update customer set name = 'Johnathon', email= 'jj@example.com' where cid = 1;
    #create table Address(
    aid int primary key auto_increment,
    Houseno varchar(256), 
    addressline varchar(15), 
    city varchar(256),  
    state varchar(256),
    zipCode int,
    landmark varchar(256)
    );


**virtual environment 
python -m venv myenv
.myenv/Scripts/activate 
pip install mysql-connector-python

**driver installation 
**sql connection with python
"""

#Structured query language 
#CRUD operations - create 
"""
customer: name, phone, email, gender, age etc...
Address: Houseno , addressline1, addressline2, city, state, zipCode, landmark 
"""

class Customer:
    def __init__(self, name="NA", phone=" ", email="", gender="",age = 18):
        self.name = name 
        self.phone = phone
        self.email = email
        self.gender = gender
        self.age = age
    
    def add_customer_details(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")
        self.age = int(input("Enter Customer Age: "))
        self.gender = input("Enter Customer Gender: ")

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~CUSTOMER~~~~~~~~~~~~~~~~~~~~~")
        print("Name: {} | Phone: {} ".format(self.name, self.phone))
        print("Email: {} | ".format(self.email))
        print("Gender: {} | Age: {} ".format(self.gender, self.age))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

"""
class Address:
    def __init__(self, Houseno , addressline, city, state, zipCode, landmark):
        self.Houseno = Houseno 
        self.addressline = addressline
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.landmark = landmark

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~CUSTOMER~~~~~~~~~~~~~~~~~~~~~")
        print("Name: {} | Phone: {} ".format(self.name, self.phone))
        print("Email: {} | Address: {} ".format(self.email, self.address))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
"""
customer1 = Customer(name="John", phone= "+91 99999 11111", email="john@example.com", gender="Male",age = 28)
customer1.show()