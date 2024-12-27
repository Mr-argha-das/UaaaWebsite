import os
from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI
from mongoengine import connect
from client.routes import clientroutes
from currency.routes import currencyroutes
from order.routes import orderroutes
from roles.routes import roloes
from services.routes import serviceroutes
from user.routes import userroutes
from pages.admin import addcurrency, addorder, addrole, clientList, login, dashboard, adduser, addclient,addservice, orderlist, userlist
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

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)