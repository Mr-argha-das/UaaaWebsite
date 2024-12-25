from fastapi import APIRouter, FastAPI
from mongoengine import connect
from client.routes import clientroutes
from currency.routes import currencyroutes
from roles.routes import roloes
from services.routes import serviceroutes
from user.routes import userroutes
connect('UAAWebsite', host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/UAAWebsite")
app = FastAPI()

app.include_router(clientroutes.router, tags=["Clients"])
app.include_router(currencyroutes.router, tags=["Currency"])
app.include_router(roloes.router, tags=["roles"])
app.include_router(serviceroutes.router, tags=["service"])
app.include_router(userroutes.router, tags=["user"])
