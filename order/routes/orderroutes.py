import json
import shutil
from datetime import datetime
from bson import ObjectId

from pydantic import BaseModel
from fastapi import FastAPI, APIRouter, File, Form, UploadFile
from pathlib import Path  # Explicit import from pathlib
from order.models.ordermodel import OrderIdTable, OrderModel, OrderTable

from starlette.requests import Request
router = APIRouter()
UPLOAD_DIRECTORY = "uploads/"
Path(UPLOAD_DIRECTORY).mkdir(parents=True, exist_ok=True)

def generate_order_number(order_count):
    return f"order_{order_count:06d}"

@router.post("/api/v1/add-order")
async def add_order(request: Request, body: OrderModel):
    try:
        # Save to the database
        userData = request.session.get('userdata')
        orderIdData = len(OrderTable.objects.all())
        count = 000000 + orderIdData
        cr_date = datetime.now().strftime("%d-%m-%Y")
        savedata = OrderTable(
            orderNoID=f'{generate_order_number(count+1)}',
            clintId=body.clintId,
            userId=str(userData['data']['_id']['\u0024oid']),
            serviceId=body.serviceId,
            deadline=body.deadline,
            module_name=body.module_name,
            module_code=body.module_code,
            wordcount=body.wordcount,
            totalorderamount=body.totalorderamount,
            clientpaidAmount=body.clientpaidAmount,
            currency_type=body.currency_type,
            message=body.message,
            filepath=body.filepath,
            status="Pending",
            cr_date=f"{cr_date}"
        )
        # Commit to the database
        savedata.save()
        return {"message": "Order added successfully"}
    except Exception as e:
        return {"message": str(e)}, 400

class OrderPaymentModel(BaseModel):
    orderId : str
    amount : int

class OrderStatusModel(BaseModel):
    orderId : str
    status : str

@router.put("/api/v1/update-order-payment")
async def upDateOrderPayment(body: OrderPaymentModel):
    findata = OrderTable.objects.get(id=ObjectId(str(body.orderId)))
    findata.clientpaidAmount = findata.clientpaidAmount + body.amount
    findata.save()
    return {
        "message": "order payment updated",
        "status": True
    }
    
@router.put("/api/v1/update-order-status")
async def upDateOrderStatus(body: OrderStatusModel):
    findata = OrderTable.objects.get(id=ObjectId(str(body.orderId)))
    findata.status =  body.status
    findata.save()
    return {
        "message": "order status updated",
        "status": True
    }




@router.get("/api/v1/get-orders")
async def getOrders():
    findata = OrderTable.objects.all()
    data = findata.to_json()
    fromjson = json.loads(data)
    return {
        "message": fromjson
    }

  # Use pathlib's Path here

@router.delete("/api/v1/get-delet")
async def getOrders():
    findata = OrderTable.objects.delete()

    return {
        "message": "done"
    }

@router.post("/api/v1/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_location = Path(UPLOAD_DIRECTORY) / file.filename
        with file_location.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"message": f"File '{file.filename}' uploaded successfully!", "path": file.filename}
    except Exception as e:
        return {"error": str(e)}