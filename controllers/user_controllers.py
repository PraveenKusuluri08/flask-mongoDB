from flask import request, jsonify
from models import User
from utils import UserUtils
import json

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

        # checking if user exists or not if user exists then return already exists message if not continue with the next process
        if (UserUtils._is_user_email_exists(email)):
            return jsonify({"message": "User already exists","status":400})
        
        if(UserUtils._is_user_username_exists(username)):
            return jsonify({"message":"Username Already Exists", "status": 400})
        
        hashedPassword = UserUtils.hashPassword(password)

        user = User(username=username, email=email, password=hashedPassword)

        user.save()

        return jsonify({"messsage": "User Saved successfully"})
    

    def SignIn(self):
        # form data is in the json string so parsing it
        
        data =request.get_json()
        print(data["password"])
        if len(data["email"]):
            if data["email"] and not UserUtils._is_user_email_exists(data["email"]):
                return jsonify({"message":"User with email address is not exists","status":404})
        
        user = User._get_collection().find({"email":data["email"]})
        
        if not user:
            return jsonify({"message":"User not exists please try again with proper email or username","status":404})
        
        email =""
        password= ""
        username=""
        #iterating throuh the cursor
        for u in user:
            email = u["email"]
            password = u["password"]
            username = u["username"]
        print("Email",email,password)
        if not UserUtils.verifyPassword(data["password"],password):
            return jsonify({"message":"Password is incorrect","status":404})
        
        token = UserUtils.generateToken({"email":email,"username":username})
        
        # request.cookies.add("token",token)
        return jsonify({"token":token,"status":200})
        
            
        
        
        
        
        
