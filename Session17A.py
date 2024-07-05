"""
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
    create table consultation(
        cid int primary key auto_increment,
        pid int,
        remarks varchar(256),
        medicines varchar(256),
        next_followup datetime,
        created_on datetime,
        FOREIGN KEY (pid) REFERENCES Patient(pid)
    );
"""
class Consultation:
    def __init__(self,cid=0,pid = 0, remarks="", medicines="", next_followup=""):
        self.cid = cid
        self.pid = pid
        self.remarks = remarks
        self.medicines = medicines
        self.next_followup = next_followup
        self.created_on = datetime.datetime.now()

    def add_consultation_details(self):
        self.pid = input("Enter Patient ID: ")
        self.remarks = input("Enter Patient remarks: ")
        self.medicines = input("Enter Patient medicines: ")
        self.next_followup = input("Enter Patient next follow up(yy-mm-dd  hh:mm:ss): ")
        # we will not get input for created_on
        # created_on is a system date time stamp


    def show(self):
        print("~~~~~~~~~~~~CONSULTATION~~~~~~~~~~~~~")
        consultation= """
        {cid} | {pid} 
        {remarks} |{medicines}
        {next_followup} |{created_on}
        """.format_map(vars(self))

        print(consultation)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
