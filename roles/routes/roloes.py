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