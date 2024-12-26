import shutil
from fastapi import FastAPI, APIRouter, File, Form, UploadFile
from pathlib import Path  # Explicit import from pathlib
from order.models.ordermodel import OrderIdTable, OrderTable


router = APIRouter()
UPLOAD_DIRECTORY = "uploads/"
Path(UPLOAD_DIRECTORY).mkdir(parents=True, exist_ok=False)
@router.post("/api/v1/add-order")
async def add_order(
    client: str,
    service: str,
    deadline: str,
    module_name: str,
    module_code: str,
    wordcount: str,
    totalorderamount: int,
    clientpaidAmount: int,
    currency_type: str,
    message: str,
    filepath: str
):
    try:
        # Save to the database
        orderIdData = len(OrderTable.objects.all())
        count = 000000 + orderIdData
        savedata = OrderTable(
            orderNoID=f'order-{count+1}',
            clintId=client,
            serviceId=service,
            deadline=deadline,
            module_name=module_name,
            module_code=module_code,
            wordcount=wordcount,
            totalorderamount=totalorderamount,
            clientpaidAmount=clientpaidAmount,
            currency_type=currency_type,
            message=message,
            filepath=filepath
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
        return {"message": f"File '{file.filename}' uploaded successfully!", "path": str(file_location)}
    except Exception as e:
        return {"error": str(e)}