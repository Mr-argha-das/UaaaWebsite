from mongoengine import Document, StringField
from pydantic import BaseModel

class AttendanceTable(Document):
    userId = StringField(required=True)
    duration = StringField(required=True)
    date = StringField(required=True)
    intime=StringField(required=True)
    outtime=StringField(required=True)