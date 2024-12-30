from mongoengine import Document, StringField
from pydantic import BaseModel

class AttendanceTable(Document):
    userId = StringField(required=True)
    status = StringField(required=True)
    date = StringField(required=True)