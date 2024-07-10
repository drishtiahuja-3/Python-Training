from Session21C import MongoDBhelper
from Session21A import User
from bson.objectid import ObjectId
import datetime
from tabulate import tabulate 

def main():
    print("WELCOME TO TEST APP")
    dbhelper = MongoDBhelper()
 
 #to create
    #user = User()
    #user.add_user_details()
    #document = vars(user)
    #dbhelper.insert(document)

    #query = {"email":"ben@example.com"}
    #document_to_update = {"name":"benny", "age":30}
    #dbhelper.update(document=document_to_update,query=query)
    
   # query = {"email":"john@example.com"}
    # dbhelper.delete(query)

#to fetch on basis of object id 
    #query ={"_id":ObjectId('6687e391702ad6130fdaeffc')}

  #to fetch selective query
    #users = dbhelper.fetch(query)
    users = dbhelper.fetch()
    #for user in users:
    #   print(user)
    print(tabulate(users, tablefmt='grid'))

if __name__ == "__main__":
    main()