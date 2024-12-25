from mongoengine import Document, StringField, IntField
from pydantic import BaseModel

class RolesTable(Document):
    name = StringField(required=True)
    v = IntField(required=True)

class RolesModel(BaseModel):
    name : str
    v : str