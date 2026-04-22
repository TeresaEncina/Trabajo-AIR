from fastapi import APIRouter
from database import incidents_db

router = APIRouter()

@router.get("/stats")
def get_stats():
    return {
        "total_incidents": len(incidents_db)
    }