from fastapi import APIRouter

router = APIRouter(tags=["Pachu Service"])

@router.get("/")
async def root():
    api_response = {
        "status" : "OK" ,
        "Message" : "Landing Page"
        }
    return api_response

@router.get("/pachuu")
async def Pachu():
    music = {
        "song" : "Pachu Ree",
        "lines" : "pachu re pachu re, pachu re pachu re, tomar gondho sukhe nilo, pachu re pachu re"
    }
    return music