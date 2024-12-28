from mongoengine import Document, StringField, IntField
from pydantic import BaseModel


class OrderTable(Document):
    orderNoID = StringField(required=True)
    userId = StringField(required=True)
    clintId = StringField(required=True)
    serviceId = StringField(required=True)
    deadline = StringField(required=True)
    module_code = StringField(required=True)
    module_name = StringField(required=True)
    wordcount = StringField(required=True)
    message = StringField(required=True)
    payment_type = StringField(require=True)
    currency_type = StringField(required=True)
    totalorderamount = IntField(required=True)
    clientpaidAmount = IntField(required=True)
    filepath = StringField(required=True)
    status = StringField(required=True)
    cr_date = StringField(required=True)

class OrderModel(BaseModel):
    clintId : str
    serviceId : str
    deadline : str
    module_code : str
    module_name : str
    wordcount : str
    message : str
    payment_type : str
    currency_type : str
    totalorderamount : int
    clientpaidAmount : int
    filepath : str
    
    
class OrderIdTable(Document):

    orderNo = StringField(required=True)
    
    