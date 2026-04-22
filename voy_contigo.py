from fastapi import APIRouter
from models import DeviationCheck

router = APIRouter()

@router.post("/voy_contigo/start")
def start_tracking():
    return {"message": "Modo 'Voy contigo' activado"}

@router.post("/voy_contigo/check")
def check_status(data: DeviationCheck):
    if data.deviation:
        return {"alert": "Prealerta generada"}
    return {"status": "Todo correcto"}