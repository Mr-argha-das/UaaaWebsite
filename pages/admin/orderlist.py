import json
from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from services.models.serviocemodels import ServiceTable
from user.models.usermodel import UserTable

router = APIRouter()

templates = Jinja2Templates(directory="admintemplates")

@router.get("/admin/orderlist", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("orderslist.html", {"request": request,})