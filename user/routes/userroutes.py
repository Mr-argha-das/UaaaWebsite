import json
from bson import ObjectId
from fastapi import FastAPI, APIRouter, Request

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
async def loginUser(request: Request, body:UserLoginModel):
    finduser = UserTable.objects(email=body.email).first()
    if finduser :
        if (finduser.password == body.password):
            tojson = finduser.to_json()
            fromjson = json.loads(tojson)
            role = RolesTable.objects.get(id=ObjectId(str(finduser.role_id)))
            roletojson = role.to_json()
            rolefromjson = json.loads(roletojson)
            request.session["userdata"] = {
                "message": "Login succes",
                "status": 200,
                "data": fromjson,
                "role": rolefromjson
            }
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
        
@router.get("/api/user/list")
async def userList():
    userlist = UserTable.objects.all()
    tojson = userlist.to_json()
    fromjson = json.loads(tojson)
    return {
        "data": fromjson
    }
    
@router.get("/api/user/logout")
async def userList(requests: Request):
     requests.session.clear()
     return {
         "messsdaax"
     }
    