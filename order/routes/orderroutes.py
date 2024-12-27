import shutil
from fastapi import FastAPI, APIRouter, File, Form, Request, UploadFile
from pathlib import Path  # Explicit import from pathlib
from order.models.ordermodel import OrderIdTable, OrderModel, OrderTable


router = APIRouter()
UPLOAD_DIRECTORY = "uploads/"
Path(UPLOAD_DIRECTORY).mkdir(parents=True, exist_ok=True)

@router.post("/api/v1/add-order")
async def add_order(request: Request, body: OrderModel):
    try:
        # Save to the database
        userData = request.session.get('userdata')
        orderIdData = len(OrderTable.objects.all())
        count = 000000 + orderIdData
        savedata = OrderTable(
            orderNoID=f'order-{count+1}',
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
            filepath=body.filepath
        )
        # Commit to the database
        savedata.save()
        return {"message": "Order added successfully"}
    except Exception as e:
        return {"message": str(e)}, 400





  # Use pathlib's Path here

@router.post("/api/v1/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_location = Path(UPLOAD_DIRECTORY) / file.filename
        with file_location.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"message": f"File '{file.filename}' uploaded successfully!", "path": file.filename}
    except Exception as e:
        return {"error": str(e)}