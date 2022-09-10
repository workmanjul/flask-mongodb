from flask import Flask,render_template, request, url_for, redirect
from pymongo import MongoClient

# Initializing flask
app = Flask(__name__)

# Initializing MongoClient
# This can be better handled by configuring it through a properties file
client = MongoClient('localhost', 27017)

db = client.flask_mongodb

# Defining users collection
users = db.users

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/createUser', methods=["POST"])
def createUser():

    #Capturing Token from Bearer
    headers = request.headers
    bearer = headers.get('Authorization')
    token = bearer.split()[1]

    # Validating token [Can be compared within the database as well]
    if token == "B1n0FlddHVnfBLeAkC": # Hardcoded for now
        data = request.get_json()

        #Validating data types
        if not isinstance(data['username'],str):
            return "Username can only be string."
        if not isinstance(data['password'],str):
            return "Password can only be string."
        if not isinstance(data['age'],int):
            return "Age can only be integer."

        users.insert_one(data) # Insert into users collection
        return "Succesfully created the entry for user"
    else:
        return "Invalid Request. Cannot Validate token"
    
app.run(debug=True)
