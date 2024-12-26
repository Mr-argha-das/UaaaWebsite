import shutil
from fastapi import FastAPI, APIRouter, File, Form, UploadFile
from pathlib import Path  # Explicit import from pathlib
from order.models.ordermodel import OrderTable


router = APIRouter()
UPLOAD_DIRECTORY = "uploads/"
Path(UPLOAD_DIRECTORY).mkdir(parents=True, exist_ok=False)
@router.post("/api/v1/add-order")
async def add_order(
    client: str = Form(...),
    service: str = Form(...),
    deadline: str = Form(...),
    module_name: str = Form(...),
    module_code: str = Form(...),
    wordcount: str = Form(...),
    totalorderamount: int = Form(...),
    clientpaidAmount: int = Form(...),
    currency_type: str = Form(...),
    message: str = Form(...),
    filepath: str = Form(...)
):
    try:
        # Save to the database
        savedata = OrderTable(
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
        session.add(savedata)
        session.commit()
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