from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from client.models.clientmodel import ClientTable
from user.models.usermodel import UserTable

router = APIRouter()

templates = Jinja2Templates(directory="admintemplates")

@router.get("/admin/dashboard", response_class=HTMLResponse)
async def read_index(request: Request):
    usercount = len(UserTable.objects.all())
    
    clientscount = len(ClientTable.objects.all())
    userData = request.session.get('userdata')
    if userData['role']['name'] != 'Admin':
        clientscount = len(ClientTable.objects(userid=str(userData['data']['_id']['\u0024oid'])).all())
    return templates.TemplateResponse("dashboard.html", {"request": request, "userdata": userData, "usercount": usercount, "clientcount": clientscount})