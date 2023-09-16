from flask import request, jsonify
import jwt
import os
from bson import ObjectId
from models import User


def middleware(func):
    def check_token():
        try:
            token = request.headers.get('Authorization').split(' ')[1]
            print(token)
            if not token or len(token) == 0:
                return jsonify({"code": "token_not_found", "error": "Please login again"})
            
            decoded = jwt.decode(token, os.getenv(
                "SECRET_KEY"), algorithms=["HS256"])
            
            print("decoded ", decoded)
            

            if not decoded:
                raise Exception("token_corrupted")

            id = ObjectId(decoded["_id"])

            user = User._get_collection().find_one({"_id": id})
            print("🥰",user)
            if not user:
                return jsonify({"error": "User not found"})

            request.user = {
                "_id": user["_id"],
                "username": user["username"],
                "email": user["email"],
            }
            return func()

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Sign error please login", "status": 401})

        except Exception as e:
            print("😅", e)
            return jsonify({"error": "Please check with the token. Token currupted"})

    return check_token
