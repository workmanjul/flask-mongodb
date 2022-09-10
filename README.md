Sample Application with Python and MongoDB to create users via a POST request

# Pre-requisites

- Python
- Virtualenvironment
- MongoDB

# Configuration
> Navigate to main.py (line: 8) and configure the host and port for mongo instance

client = MongoClient('localhost', 27017)

# Setup

> Clone this project and navigate to the main directory (flask-mongodb)

    cd flask-mongodb

> Create and activate new virtual environment

	python3 -m venv env
    source env/bin/activate

> Install the pacakage required
	
	pip install -r requirements.txt

> Run the application: Navigate to the app folder and run the project

	python main.py

# Test Project
> Test the project: Send a POST request with bearer token
    Example:

    POST /createUser

    Authorization: Bearer B1n0FlddHVnfBLeAkC 
    {"username": "manjulb", "password": "manjulb", "age": 32}

>