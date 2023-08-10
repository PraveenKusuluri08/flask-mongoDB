from mongoengine import *
from datetime import datetime

class User(Document):
    username = StringField(required=True,max_length=50)
    email = EmailField(sparse=True,required=True,unique=True)
    password = StringField(required=True)
    createdAt = DateTimeField(default = datetime.now())
    
    # meta = {'allow_inheritance': True,"abstract":True}

# class Todos(Users):
#     uid = ReferenceField(Users)
#     title = StringField(required=True,unique=True,max_length=150)
#     description = StringField(required=True)
#     isCompleted = BooleanField(required=True)
#     created = DateTimeField(required=True,default=datetime.now())
    
#     meta = {
#         'indexes': ['uid']
#     }