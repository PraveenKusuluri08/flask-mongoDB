from flask import Blueprint
from flask import request
from controllers import ChatController
from endpoint import middleware

chatBlueprint = Blueprint("chat",__name__)

chatController = ChatController()

@chatBlueprint.route("/create-room",methods=["GET","POST"])
@middleware
def createRoom():
    data =request.get_json(force=True)
    user = request.user
    print(data["room_name"],user)
    return chatController.create_room(data,user)
