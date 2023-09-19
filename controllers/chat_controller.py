from flask import request, jsonify
from utils import save_room, add_members_to_room,is_room_exists
from utils import UserUtils


class ChatController:
    def __init__(self):
        pass

    def create_room(self, data, user):
        message = ""
        print(data)

        room_name = data["room_name"]
        
        if is_room_exists(room_name):
            return jsonify({"error":"room name already exists"})

        users = [username.strip() for username in data["users"]]
        print(users)
        if len(room_name) and len(users):
            roomId = save_room(
                room_name, user["username"], isGroup=data["isGroup"], isRoomAdmin=True)
            
            # checking if current user is already exists in users array then remove current user
            if user["username"] in users: 
                users.remove(user["username"])
            # check for the evaluate the user is exists in the database
            print("users😍 ",users)
            addedBy=user["username"]
            for user in users:
                if UserUtils._is_user_username_exists(user):
                    add_members_to_room(room_id=roomId.inserted_id, room_name=room_name,
                             isGroup=data["isGroup"], users=users, addedBy=addedBy, isRoomAdmin=True)

        else:
            message = "failed to create room"
        return jsonify({"message": f"{message if len(message)>0 else 'Room created successfully'}"})
