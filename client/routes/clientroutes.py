from fastapi import FastAPI, APIRouter

from client.models.clientmodel import ClientModel, ClientTable\


router = APIRouter()
@router.post("/api/v1/add-client")
async def addclient(body: ClientModel):
    savedata = ClientTable(**body.dict())
    savedata.save()
    return {
        "message": "clientadded",
        "status":True
    }