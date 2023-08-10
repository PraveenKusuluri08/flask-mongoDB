from flask import Blueprint
from flask import request
from controllers.user_controllers import UserControllers

userBluePrint = Blueprint("users",__name__)

userController = UserControllers()

@userBluePrint.route("/test")
def test():
    if request.method=="GET":
        return "userController.test"
    else:
        return "method_not_allowed"
    

@userBluePrint.route("/signup",methods=["POST"])
def create():
    if request.method=="POST":
        return userController.Create()
    else:
        return "method_not_allowed"
    
@userBluePrint.route("/signin",methods=["POST"])
def signIn():
    if request.method=="POST":
        return userController.SignIn()
    else:
        return "method_not_allowed"
