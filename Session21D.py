from Session21C import MongoDBhelper
from Session21A import User


def main():
    print("WELCOME TO TEST APP")
    dbhelper = MongoDBhelper()
 
    #user = User()
    #user.add_user_details()
    #document = vars(user)
    #dbhelper.insert(document)
    
    users = dbhelper.fetch()
    for user in users:
        print(user)

if __name__ == "__main__":
    main()