import json
from bson import ObjectId
from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from attendance.models.attendancemodel import AttendanceTable
from client.models.clientmodel import ClientTable
from user.models.usermodel import UserTable

router = APIRouter()

templates = Jinja2Templates(directory="admintemplates")

@router.get("/admin/addattendance", response_class=HTMLResponse)
async def read_index(request: Request):
    userDATA = []
    userData = request.session.get('userdata')
    services = UserTable.objects.all()
    for user in services:
        todaysattendance = AttendanceTable.objects.filter(date=True, userId=True).exclude(userId=ObjectId(user.id), date=datetime.now().strftime("%d-%m-%Y"))

        if (todaysattendance) :
            tojson = user.to_json()
            fromjson = json.loads(tojson)
            userDATA.append({
                "user": fromjson,
                "status": "P"
            })
            print(userDATA)
        else:
            tojson = user.to_json()
            fromjson = json.loads(tojson)
            userDATA.append({
                "user": fromjson,
                "status": "Mark"
            })
            print(userDATA)
    
    return templates.TemplateResponse("addattendace.html", {"request": request, "userlist": userDATA, "context":userData})
    
