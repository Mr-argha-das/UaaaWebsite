from mongoengine import Document, StringField
from pydantic import BaseModel

class UserTable(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    phone = StringField(required=True)
    couuntry_code = StringField(required=True)
    password = StringField(required=True)
    role_id = StringField(required=True)


class UserModel(BaseModel):
    name:str
    email:str
    phone:str
    couuntry_code:str
    password: str
    role_id : str
    
class UserLoginModel(BaseModel):
    email :str
    password:str