from dotenv.main import load_dotenv,find_dotenv
import os
import pprint
from pymongo import MongoClient,errors as MongoErrorHandlers
from flask import Flask
from flask_bcrypt import Bcrypt
#app
app = Flask(__name__)

load_dotenv(find_dotenv())

connection_uri = os.getenv("MONGO_URI")

bcrypt = Bcrypt(app)

try:
    client = MongoClient(connection_uri)
    print("MongoDB connected successfully")
    
    #db
    db = client["STARTER"]
    
except MongoErrorHandlers.ConnectionFailure as err:
    print('Database connection failed',err)


