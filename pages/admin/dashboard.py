import json
from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from attendance.models.attendancemodel import AttendanceTable
from client.models.clientmodel import ClientTable
from order.models.ordermodel import OrderTable
from user.models.usermodel import UserTable

router = APIRouter()
from datetime import datetime
templates = Jinja2Templates(directory="admintemplates")

@router.get("/admin/dashboard", response_class=HTMLResponse)
async def read_index(request: Request):
    usercount = len(UserTable.objects.all())
    wordcount = 0
    totalbookedamount = 0
    totalpenddingamount = 0
    ordercount = 0
    clientscount = len(ClientTable.objects.all())
    userData = request.session.get('userdata')
    todaysattendance = json.loads(AttendanceTable.objects(date=f"{datetime.now().strftime("%d-%m-%Y")}",userId=str(userData['data']['_id']['\u0024oid']) ).to_json())
    print(todaysattendance)
    if userData['role']['v'] != 4 :
        clientscount = len(ClientTable.objects(userid=str(userData['data']['_id']['\u0024oid'])).all())
        orders = OrderTable.objects(userId = str(userData['data']['_id']['\u0024oid'])).all()
        ordercount = len(orders)
        print('hey')
        for order in orders:
            totalbookedamount = totalbookedamount + order.totalorderamount
            pending = order.totalorderamount - order.clientpaidAmount
            totalpenddingamount = totalpenddingamount + pending
            wordcount = wordcount + int(order.wordcount)
    else:
        orders = OrderTable.objects.all()
        ordercount = len(orders)
        for order in orders:
            totalbookedamount = totalbookedamount + order.totalorderamount
            pending = order.totalorderamount - order.clientpaidAmount
            totalpenddingamount = totalpenddingamount + pending
            wordcount = wordcount + int(order.wordcount)
    return templates.TemplateResponse("dashboard.html", {"request": request, "context":userData, "userdata": userData, "usercount": usercount, "clientcount": clientscount, "totalbooked": totalbookedamount, "totalpending": totalpenddingamount, "ordercount": ordercount, "wordcount": wordcount, "todaysattendance":todaysattendance})

