from flask import Blueprint
from flask import request,jsonify
from endpoint import middleware
from controllers.user_controllers import UserControllers

userBluePrint = Blueprint("users",__name__)

userController = UserControllers()

@userBluePrint.route("/test")
@middleware
def test():
    print("😂",request.user)
    if request.method=="GET":
        return test()
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
    
@userBluePrint.route("/generateforgotpasswordlink",methods=["POST"])
def generateForgotPasswordLink():
    if request.method=="POST":
        return userController.GenerateForgotPasswordLink()
    else:
        return "method_not_allowed"
    
    
def test():
    return jsonify({"message":"test"})