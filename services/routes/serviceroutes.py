from fastapi import FastAPI, APIRouter

from services.models.serviocemodels import ServiceModel, ServiceTable

router = APIRouter()
@router.post("/api/v1/add-service")
async def addService(body: ServiceModel):
    savedata = ServiceTable(**body.dict())
    savedata.save()
    return {
        "message": "service added",
        "status" : True
    }
