from fastapi import FastAPI, APIRouter

from currency.models.currencymodelo import CurrencyModel, CurrencyTable

router = APIRouter()

@router.post("/api/v1/add-currency")
async def addCurrency(body: CurrencyModel):
    savedata = CurrencyTable(**body.dict())
    savedata.save()
    return {
        "message": "curency added",
        "status":True
    }