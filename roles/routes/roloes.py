import json
from fastapi import FastAPI, APIRouter

from roles.models.rolesmodel import RolesModel, RolesTable

router = APIRouter()

@router.post("/api/v1/add-roles")
async def addRoles(body: RolesModel):
    dataSave = RolesTable(**body.dict())
    dataSave.save()
    return {
        "message" : "Roles Added",
        "status": True
    }
    
@router.get("/api/v1/get-all-roles")
async def getAllRoles():
    data = RolesTable.objects.all()
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
     "data": fromjson
    }