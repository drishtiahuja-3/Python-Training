from Session17 import Patient
from Session17A import Consultation
from Session15A import Database
from tabulate import tabulate 


def main():
    print("======DOCTOR'S APP=====")
    print("WELCOME TO DOCTOR'S APP")
    print("=======================")

    db = Database()

    while True:
        print("1: Add New Patient")
        print("2: Update Existing Patient")
        print("3: Delete Existing Patient")
        print("4: View Patient By Phone")
        print("5: View Patient By CID")
        print("6: View All Patients")
        print("7: Add Consultation For Patients")
        print("8: View All Consultations")
        print("9: View All Consultation Of a Patient")
        print("0: To Quit App")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            patient = Patient()
            patient.add_patient_details()
            sql = "insert into Patient values(null, '{name}', '{phone}', '{email}', '{dob}', '{gender}', '{created_on}')".format_map(vars(patient))
            # sql = "insert into Patient values(null, '{}', '{}', '{}', {}, '{}', null)".format(patient.name, patient.phone, patient.email, patient.dob, patient.gender)
            db.write(sql)
            print("Patient created")
        
        elif choice == 2:
            pid = int(input("Enter Patient ID to Update: "))
            sql = "select * from Patient where pid = {}".format(pid)
            rows = db.read(sql)
            print(rows)
            
            patient = Patient(pid=rows[0][0], name=rows[0][1], phone=rows[0][2], email=rows[0][3], dob=rows[0][4], gender=rows[0][5])

            print("Patient to Update:")
            patient.show()
            patient.update_patient_details()

            sql = "update Patient set name = '{name}', phone='{phone}', email='{email}', dob={dob}, gender='{gender}', created_on='{created_on}' where pid = {pid}".format_map(vars(patient))

            db.write(sql)

            patient.show()
            

        elif choice == 3:
            pid = int(input("Enter Patient ID to be Deleted: "))
            sql = "delete from Patient where pid = {}".format(pid)

            ask = input("Are you sure to delete? (yes/no): ")
            if ask == "yes":
                db.write(sql)
                print( pid, "Deleted from DataBase")
            else:
                print("Delete Operation Skipped")

        elif choice == 4:
            phone = input("Enter Patients Phone Number: ")
            sql = "select * from Patient where phone = '{}'".format(phone)
            rows = db.read(sql)

            columns = ["pid", "name", "phone", "email", "dob", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))

        elif choice == 5:
            pid = int(input("Enter Patients ID: "))
            sql = "select * from Patient where pid = {}".format(pid)
            rows = db.read(sql)

            columns = ["pid", "name", "phone", "email", "dob", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
        elif choice == 6:
            sql = "select * from patient"
            rows = db.read(sql)

            columns = ["pid", "name", "phone", "email", "dob", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))

        elif choice == 7:
            consultation = Consultation()
            consultation.add_consultation_details()
            sql = "insert into consultation values(null, '{pid}', '{remarks}', '{medicines}', '{next_followup}','{created_on}')".format_map(vars(consultation))
            # sql = "insert into Patient values(null, '{}', '{}', '{}', {}, '{}', null)".format(patient.name, patient.phone, patient.email, patient.dob, patient.gender)
            db.write(sql)
            print("Consultation created")

        elif choice == 8:
            sql = "select * from consultation"
            rows = db.read(sql)

            columns = ["cid","pid", "remarks", "medicines", "next_followup", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))

        elif choice == 9:
            pid = int(input("Enter Patients ID: "))
            sql = "select * from consultation where pid = {}".format(pid)
            rows = db.read(sql)

            columns = ["cid","pid", "name", "phone", "email", "dob", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))

        elif choice == 0:
            break
        else:
            print("Invalid Choice", choice)

if __name__ == "__main__":
    main()