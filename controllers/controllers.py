from flask import request
from models.Users import Users
class Controllers:
    def __init__(self):
        pass
    def Create(self):
         data = request.get_json()
         username = data["username"]
         email = data["email"]
         password = data["password"]
         
        