from mongoengine import *
from datetime import datetime

class User(Document):
    username = StringField(required=True,max_length=50)
    email = EmailField(sparse=True,required=True,unique=True)
    password = StringField(required=True)
    createdAt = DateTimeField(default = datetime.now())
    firstname=StringField(required=True)
    lastname=StringField(required=True)
    isVerified=BooleanField(required=True)
    
    # meta = {'allow_inheritance': True,"abstract":True}
    