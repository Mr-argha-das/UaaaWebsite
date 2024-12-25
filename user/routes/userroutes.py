from fastapi import FastAPI, APIRouter

from user.models.usermodel import UserModel, UserTable


router = APIRouter()

@router.post("/api/v1/add-client")
async def addClient(body: UserModel):
    savedata = UserTable(**body.dict())
    savedata.save()
    return {
        "message": "useradded",
        "status": True
    }


