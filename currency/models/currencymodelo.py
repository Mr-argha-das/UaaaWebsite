from mongoengine import Document,StringField
from pydantic import BaseModel

class CurrencyTable(Document):
    name = StringField(required=True)
    symbol = StringField(required=True)

class CurrencyModel(BaseModel):
    name:str
    symbol:str

