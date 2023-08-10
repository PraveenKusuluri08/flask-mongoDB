from app import bcrypt
import jwt
import os
from models.user_models import User

class UserUtils:
    @staticmethod
    def _is_user_email_exists(email):
        filter = {"email": email}
        user = User._get_collection().find_one(filter)
        if user:
            return True
        else:
            return False
    
    @staticmethod
    def _is_user_username_exists(username):
        filter = {'username': username }
        user = User._get_collection().find_one(filter)
        if user:
            return True
        else :
            return  False

    @staticmethod
    def hashPassword(password):
        
        return bcrypt.generate_password_hash(password).decode('utf-8')
    
    @staticmethod
    def verifyPassword(password, hashed_password):
        return bcrypt.check_password_hash(hashed_password,password)

    @staticmethod
    def generateToken(user) -> str:
        return jwt.encode(user, os.getenv("SECRET_KEY"), algorithm="HS256")
