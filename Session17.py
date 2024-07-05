"""

AC service app
technician -> use of application
customer , ac

laptop service app

Doctor App 

user is a doctor
should be able to add patients 
should be able to add consultation of patients 

doctor -> use of application
patient : pid, name,phone,email, dob, gender, created_on
Consultation: cid, pid, remarks, medicines, next_followup, created_on

"""
import datetime


"""
    create table patient(
        pid int primary key auto_increment,
        name varchar(256),
        phone varchar(15),
        email varchar(256),
        dob date,
        gender varchar(20),
        created_on datetime
    );
"""
class Patient:
    def __init__(self,pid=0, name="", phone="", email="", dob="", gender=""):
        self.pid = pid
        self.name = name
        self.phone = phone
        self.email = email
        self.dob = dob
        self.gender = gender
        self.created_on = datetime.datetime.now()

    def add_patient_details(self):
        self.name = input("Enter Patient Name: ")
        self.phone = input("Enter Patient Phone: ")
        self.email = input("Enter Patient Email: ")
        self.dob = input("Enter Patient DOB(yy-mm-dd): ")
        self.gender = input("Enter Patient Gender: ")
        # we will not get input for created_on
        # created_on is a system date time stamp

    def update_patient_details(self):
        name = input("Enter Patient Name: ")
        if len(name) != 0:
            self.name = name

        phone = input("Enter Patient Phone: ")
        if len(phone) != 0:
            self.phone = phone

        email = input("Enter Patient Email: ")
        if len(email) != 0:
            self.email = email
        
        age = input("Enter Patient Dob(yy-mm-dd): ")
        if len(dob) != 0:
            self.dob = dob

        gender = input("Enter Patient Gender: ")
        if len(gender) != 0:
            self.gender = gender

    def show(self):
        print("~~~~~~~~~~~~PATIENT~~~~~~~~~~~~~")
        patient= """
        {pid} | {name} |{phone}
        {email} |{dob}
        {gender} |{created_on}
        """.format_map(vars(self))

        print(patient)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
