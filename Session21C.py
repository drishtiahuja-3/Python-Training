from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class MongoDBhelper:
    def __init__(self, collection="users"):
        uri = "mongodb+srv://diya:1234@cluster0.srfvaua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        #accessing the database 
        #use database;
        self.db = client['python']
        self.collection = self.db[collection]

    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document is inserted in Collection:", self.collection.name)
        #print("Result is:",result, result.__inserted_id)
        return result 
    
    def fetch(self, query=""):
        documents = self.collection.find(query)
        return list(documents)
    
    def delete(self,query="" ):
        result = self.collection.delete_one(query)
        print("Result is:", result)

    def update(self, document, query="" ):
        document_to_update = {'$set':document}
        result = self.collection.update_one(query, document_to_update)
        print("Result is:", result)