from flask import request,jsonify
from models import User
from utils import UserUtils
class UserControllers:
    def __init__(self):
        pass
    
    def test(self):
        return "Test endpoint" 
      
    def Create(self):
         data = request.get_json()
         username = data["username"]
         email = data["email"]
         password = data["password"]
         
         hashedPassword=UserUtils.hashPassword(password)
         print(hashedPassword)
         user =User(username=username,email=email)
         user.password = hashedPassword
         user.save()
         
         return "User saved successfully"
        
         
         
         
         
         
        