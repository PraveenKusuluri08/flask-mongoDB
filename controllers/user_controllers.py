from flask import request, jsonify
from models import User
from utils import UserUtils
import os
from flask import render_template
import jwt
import datetime
from utils import Email


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
        firstName = data["firstName"]
        lastName = data["lastName"]

        # checking if user exists or not if user exists then return already exists message if not continue with the next process
        if (UserUtils._is_user_email_exists(email)):
            return jsonify({"message": "User already exists", "status": 400})

        if (UserUtils._is_user_username_exists(username)):
            return jsonify({"message": "Username Already Exists", "status": 400})

        hashedPassword = UserUtils.hashPassword(password)

        user = User(username=username.lower(), email=email,
                    password=hashedPassword, firstname=firstName, lastname=lastName)

        user.save()

        return jsonify({"messsage": "User Saved successfully"})

    def SignIn(self):
        # form data is in the json string so parsing it

        data = request.get_json()
        print(data["password"])
        if len(data["email"]):
            if data["email"] and not UserUtils._is_user_email_exists(data["email"]):
                return jsonify({"message": "User with email address is not exists", "status": 404})

        user = User._get_collection().find({"email": data["email"]})

        if not user:
            return jsonify({"message": "User not exists please try again with proper email or username", "status": 404})

        email = ""
        password = ""
        username = ""
        _id = ""
        # iterating throuh the cursor
        for u in user:
            email = u["email"]
            password = u["password"]
            username = u["username"]
            _id = u["_id"]
        print("Email", _id)
        if not UserUtils.verifyPassword(data["password"], password):
            return jsonify({"message": "Password is incorrect", "status": 404})

        token = UserUtils.generateToken(
            {"email": email, "username": username, "_id": str(_id), "exp": datetime.datetime.utcnow()+datetime.timedelta(hours=24)})

        # request.cookies.add("token",token)
        return jsonify({"token": token, "status": 200})

    def GenerateForgotPasswordLink(self):
        data = request.get_json()
        if not data:
            return jsonify({"message": "Please enter your email address"})
        email = data["email"]
        if not UserUtils._is_email_valid(email):
            return jsonify({"message": "Please enter the valid email address"})

        filter = {"email": email}
        user = User._get_collection().find_one(filter)
        token_expiry = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

        token = jwt.encode({"email": email, "exp": token_expiry}, os.getenv(
            "SECRET_KEY"), algorithm="HS512")
        domainLink = os.getenv("DOMAIN_URL")
        forgot_password_link = f"{domainLink}/forgotpassword/{token}"

        html = f"""\
            <html>
                <body>
                    <p>This is reset passsword link please click and reset password <span>{forgot_password_link}</span></p>
                </body>
            </html>
            """
        subject = "Reset Password"

        if not user:
            return jsonify({"message": f"Email address is not available {email}"})
        Email.send_email_to_user(email, subject, html)

        return jsonify({"message": "Reset password link generated successfully"})
