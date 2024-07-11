from flask import *
import datetime
from Session21C import MongoDBhelper
import hashlib


#create an object of flask which represents web application
web_app = Flask("Doctor's App")
db = MongoDBhelper()

@web_app.route("/")#decorator
#/ means root or home page
def index():
    #message = "Welcome to Patient Management System. Its {}".format(datetime.datetime.now())
    message = """ 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Doctor's App</title>
        </head>
        <body>
            <center>
                <h1>Welcome to Doctor's App</h1>
            </center>
        </body>
        </html>
    """
    return render_template("index.html")
@web_app.route("/register")#decorator
def register():
    return render_template("register.html")

@web_app.route("/add-user", methods = ["POST"])#decorator
def add_user_in_db():
    # create a dictionary with data from html register form 
    user_data ={
        "name": request.form["name"],
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "created_on": datetime.datetime.now()
    }
    
    result = db.insert(user_data)
#write data in session object this data can now be used in html files 
    session['user_id'] = str(result.inserted_id)
    session['name'] = user_data['name']
    session['email'] = user_data['email']
    #message = "WELCOME TO HOME PAGE\n user id is {}".format(result.inserted_id)
    #return message
    return render_template("Home.html", name = session['name'])

@web_app.route("/fetch-user", methods=["POST"])
def fetch_user_from_db():

    # Create a Dictionary with Data from HTML Register Form
    user_data = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }

    # Fetch user in DataBase i.e. MongoDB
    result = db.fetch(query=user_data)
    
    if len(result)>0:
         return render_template("Home.html", email = session['email'])
    else:
        return "User Not Found. Please Try Again"

    
def main():
    web_app.secret_key = "doctors-app-key-v1"
    web_app.run()
    #web_app.run(port=5001)
    #to run the app infinitely untill user won't quit 
    #u can optionally give a port number

if __name__=="__main__":
    main()