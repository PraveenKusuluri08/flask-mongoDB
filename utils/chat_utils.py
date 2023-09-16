from models import Room, RoomMemebers
from bson import ObjectId
chat_room_collection = Room._get_collection()
chat_room_collection_members = RoomMemebers._get_collection()


def save_room(room_name, created_by, isGroup, isRoomAdmin, addedBy):
    roomId = chat_room_collection.insert_one(
        {"name": room_name, "created_by": created_by, "isGroup": isGroup})
    add_memebers_room(room_id=ObjectId(roomId.inserted_id), room_name=room_name, isGroup=isGroup, username=created_by,
                      addedBy=addedBy if isGroup else created_by, isRoomAdmin=isRoomAdmin)
    return roomId


def add_memebers_room(room_id, room_name, isGroup, username, addedBy, isRoomAdmin):
    chat_room_collection_members.insert_one(
        {"_id": {"room_id": room_id, "username": username}, "room_name": room_name,
            "added_by": addedBy, "isGroup": isGroup, "is_room_admin": isRoomAdmin}
    )
