from flask import request,jsonify
from utils import save_room,add_memebers_room

class ChatController:
    def __init__(self):
        pass
    
    def create_room(self,data,user):
        message = ""
        print(data)
        
        room_name = data["room_name"]
        
        users = [username.strip() for username in data["users"]]
        print(users)
        if len(room_name) and len(users):
            roomId = save_room(room_name,user["username"],isGroup=data["isGroup"],isRoomAdmin=True,addedBy=data["addedBy"])
            if user["username"] in users:
                users.remove(user["username"])
                return jsonify({"room_id":roomId})
        else:
            message="failed to create room"
        return jsonify({"error":message})