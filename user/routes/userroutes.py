import json
from bson import ObjectId
from fastapi import FastAPI, APIRouter

from user.models.usermodel import UserLoginModel, UserModel, UserTable
from roles.models.rolesmodel import RolesModel, RolesTable

router = APIRouter()

@router.post("/api/v1/add-user")
async def addClient(body: UserModel):
    savedata = UserTable(**body.dict())
    savedata.save()
    return {
        "message": "useradded",
        "status": True
    }

@router.post("/api/v1/login-user")
async def loginUser(body:UserLoginModel):
    finduser = UserTable.objects(email=body.email).first()
    if finduser :
        if (finduser.password == body.password):
            tojson = finduser.to_json()
            fromjson = json.loads(tojson)
            role = RolesTable.objects.get(id=ObjectId(str(finduser.role_id)))
            roletojson = role.to_json()
            rolefromjson = json.loads(roletojson)
            return {
                "message": "Login succes",
                "status": 200,
                "data": fromjson,
                "role": rolefromjson
            }
        else:
            return {
                "message": "Login faild",
                "status": 403,
                "data": None,
                "role": None
            }
    else:
        return {
                "message": "Login succes",
                "status": 404,
                "data": None,
                "role": None
            }