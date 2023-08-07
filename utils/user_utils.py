from app import bcrypt

class UserUtils:
    # def __init__(self):
    # @staticmethod
    # def isUserExist(email: str) -> bool:
    #     users = Users
    #     filter = {"email": email}
    #     if users.find_one(filter) is not None:
    #         return True
    #     return False
    # def isUserNameExists(userName:str)->bool:
    #     users = Users.g
    #     filter = {"username": userName}
    #     if users.find_one(filter) is not None:
    #         return True
    #     return False

    @staticmethod
    def hashPassword(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def verifyPassword(password, hashed_password):
        return bcrypt.check_password_hash(hashed_password, password)
