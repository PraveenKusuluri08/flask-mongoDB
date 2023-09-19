from dotenv.main import load_dotenv, find_dotenv
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO
from mongoengine import connect, errors


app = Flask(__name__)

load_dotenv(find_dotenv(".env"))

connection_uri = os.getenv("MONGO_URI")

bcrypt = Bcrypt(app)

socketIO = SocketIO(app)

try:
    connect(host=connection_uri)
    print("Conneted to mongodb")

except errors as err:
    print('Database connection failed', err)
