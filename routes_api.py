from fastapi import APIRouter
from models import RouteRequest
import random

router = APIRouter()

def calcular_indice_seguridad():
    return random.randint(1, 100)

@router.post("/routes")
def get_routes(request: RouteRequest):
    routes = []

    for i in range(3):
        routes.append({
            "id": i,
            "path": f"{request.origin} -> {request.destination} (ruta {i})",
            "security_index": calcular_indice_seguridad()
        })

    routes.sort(key=lambda x: x["security_index"], reverse=True)

    return {"routes": routes}