from flask import request, jsonify
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

        # checking if user exists or not if user exists then return already exists message if not continue with the next process
        if (UserUtils._is_user_email_exists(email)):
            return jsonify({"message": "User already exists","status":400})
        
        if(UserUtils._is_user_username_exists(username)):
            return jsonify({"message":"Username Already Exists", "status": 400})
        
        hashedPassword = UserUtils.hashPassword(password)

        user = User(username=username, email=email, password=hashedPassword)

        user.save()

        return jsonify({"messsage": "User Saved successfully"})
