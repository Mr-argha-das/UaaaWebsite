from mongoengine import Document, StringField
from pydantic import BaseModel

class ServiceTable(Document):
    title = StringField(required=True)

class ServiceModel(BaseModel):
    title : str