from models import Rooms, RoomMemebers
from bson import ObjectId
from utils import UserUtils
import uuid

uid=uuid.uuid4().hex

chat_room_collection = Rooms._get_collection()
chat_room_collection_members = RoomMemebers._get_collection()


def save_room(room_name, created_by, isGroup, isRoomAdmin):
    roomId = chat_room_collection.insert_one(
        {"name": room_name, "created_by": created_by, "isGroup": isGroup})
    add_member_room(room_id=ObjectId(roomId.inserted_id), room_name=room_name, isGroup=isGroup, username=created_by,
                    addedBy=created_by if isGroup else created_by, isRoomAdmin=isRoomAdmin,roomcode=uid)
    return roomId


def add_member_room(room_id, room_name, isGroup, username, addedBy, isRoomAdmin,roomcode=uid):
     chat_room_collection_members.insert_one(
        {"_id": {"room_id": room_id, "username": username}, "room_name": room_name,
            "added_by": addedBy, "isGroup": isGroup, "is_room_admin": isRoomAdmin,"roomcode":roomcode}
    )


def add_members_to_room(room_id, room_name, isGroup, users, addedBy, isRoomAdmin):
    chat_room_collection_members.insert_many(
        [{'_id': {'room_id': ObjectId(room_id), 'username': username}, 'room_name': room_name, 'added_by': addedBy,
        "isGroup":isGroup, 'is_room_admin': isRoomAdmin,"roomcode":uid} for username in users if UserUtils._is_user_username_exists(username)])
    

def _is_user_already_having_room(username):
    pass

def is_room_exists(room_name):
    filter ={"name":room_name}
    chat_room=chat_room_collection.find_one(filter)
    if chat_room:
        return True
    else:
        return False

def get_room(room_id):
    filter = {"_id": ObjectId(room_id)}
    chat_room = chat_room_collection.find_one(filter)
    return chat_room

def update_room(room_id,room_name):
    filter = {"_id": ObjectId(room_id)}
    update = {"$set": {"name": room_name}}
    chat_room_collection.update_one(filter, update)
    chat_room_collection_members.update_many({"_id.room_id":ObjectId(room_id)},{"$set":{"room_name":room_name}})
    
