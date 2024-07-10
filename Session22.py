from flask import *
import datetime

#create an object of flask which represents web application
web_app = Flask("Doctor's App")

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
def main():
    web_app.run()
    #web_app.run(port=5001)
    #to run the app infinitely untill user won't quit 
    #u can optionally give a port number

if __name__=="__main__":
    main()