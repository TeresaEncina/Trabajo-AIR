from fastapi import APIRouter
from models import Incident
from database import incidents_db

router = APIRouter()

@router.post("/incident")
def report_incident(incident: Incident):
    incidents_db.append(incident)
    return {
        "message": "Incidencia registrada",
        "total": len(incidents_db)
    }