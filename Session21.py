""" 
    mongo db crud operations 
    1. connect driver 
    driver installer 
    pip install "pymongo[srv]"
    
    iff SSL  error 
    pip install certifi

    import ceritfi
    ca = certifi.where()
    client = MongoClient(uri, tlsCAFile= ca, server_api=ServerApi('1'))
"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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
db = client['python']

#get the collection names 
#show tables;
collections = db.list_collection_names()

for collection in collections:
    print(collection)

documents = db['users'].find()
print(documents)

for document in documents:
    print(document)