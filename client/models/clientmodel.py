from mongoengine import Document, StringField
from pydantic import BaseModel

class ClientTable(Document):
    userid = StringField(required=True)
    name = StringField(required=True)
    email = StringField(required=True)
    phone = StringField(required=True)
    country_code = StringField(required=True)
    uni_name = StringField(required=True)

class ClientModel(BaseModel):
    userid: str
    name : str
    email : str
    phone : str
    country_code : str
    uni_name : str