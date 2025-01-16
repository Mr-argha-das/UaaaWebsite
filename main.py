from datetime import datetime
import os

from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from mongoengine import connect

from attendance.routes import attendanceroutes
from client.routes import clientroutes
from currency.routes import currencyroutes
from order.routes import orderroutes    
from roles.routes import roloes
from services.routes import serviceroutes
from user.routes import userroutes

from pages.admin import addcurrency, addorder, addrole, clientList, login, dashboard, adduser, addclient,addservice, orderlist, userlist, addattendance
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY not found in .env file")
else:
    print("found" + SECRET_KEY)

connect('UAAWebsite', host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/UAAWebsite")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY,
    max_age=604800,
    session_cookie="your_session_cookie",
)
app.include_router(clientroutes.router, tags=["Clients"])
app.include_router(currencyroutes.router, tags=["Currency"])
app.include_router(roloes.router, tags=["roles"])
app.include_router(serviceroutes.router, tags=["service"])
app.include_router(userroutes.router, tags=["user"])
app.include_router(login.router, tags=["admin router"])
app.include_router(dashboard.router, tags=["admin router"])
app.include_router(adduser.router, tags=["admin router"])
app.include_router(addservice.router, tags=["admin router"])
app.include_router(addclient.router, tags=["admin router"])
app.include_router(addrole.router, tags=["admin router"])
app.include_router(addcurrency.router, tags=["admin router"])
app.include_router(clientList.router, tags=["admin router"])
app.include_router(userlist.router, tags=["admin router"])
app.include_router(addorder.router, tags=["admin router"])
app.include_router(orderroutes.router, tags=['order route'])
app.include_router(orderlist.router, tags=['order route'])
app.include_router(addattendance.router, tags=['admin router'])
app.include_router(attendanceroutes.router, tags=['admin'])
employee_status = {}

templates = Jinja2Templates(directory="admintemplates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("employeattendance.html", {"request": request, "employee_status": employee_status})


@app.post("/check-in")
async def check_in(employee_id: str = Form(...)):
    current_time = datetime.now().strftime("%d-%m-%Y")
    employee_status[employee_id] = {
        "status": "checked-in",
        "check_in_time": current_time,
        "check_out_time": None,
        "duration": 0
    }
    return {"message": f"Employee {employee_id} has checked in!"}

# Endpoint to check-out employee
@app.post("/check-out")
async def check_out(employee_id: str = Form(...)):
    if employee_id in employee_status and employee_status[employee_id]["status"] == "checked-in":
        check_in_time = employee_status[employee_id]["check_in_time"]
        check_out_time = datetime.now()
        duration = (check_out_time - check_in_time).seconds // 60  # Duration in minutes
        employee_status[employee_id]["check_out_time"] = check_out_time
        employee_status[employee_id]["status"] = "checked-out"
        employee_status[employee_id]["duration"] = duration
        return {"message": f"Employee {employee_id} has checked out! Duration: {duration} minutes."}
    return {"message": f"Employee {employee_id} is not checked in."}

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)