from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

# =========================
# MODELOS
# =========================

class User(BaseModel):
    username: str
    password: str

class RouteRequest(BaseModel):
    origin: str
    destination: str

class Incident(BaseModel):
    type: str
    location: str

class DeviationCheck(BaseModel):
    deviation: bool


# =========================
# BASE DE DATOS SIMULADA
# =========================

users_db = {
    "user@urjc.es": "1234"
}

incidents_db = []


# =========================
# AUTENTICACIÓN (RF-01 a RF-04)
# =========================

@app.post("/login")
def login(user: User):
    if user.username in users_db and users_db[user.username] == user.password:
        return {"message": "Login correcto"}
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")


# =========================
# RUTAS SEGURAS (RF-05 a RF-10)
# =========================

def calcular_indice_seguridad():
    return random.randint(1, 100)

@app.post("/routes")
def get_routes(request: RouteRequest):
    routes = []

    for i in range(3):  # RF-06: hasta 3 rutas
        route = {
            "id": i,
            "path": f"{request.origin} -> {request.destination} (ruta {i})",
            "security_index": calcular_indice_seguridad()
        }
        routes.append(route)

    # RF-09: ordenar por seguridad
    routes.sort(key=lambda x: x["security_index"], reverse=True)

    return {"routes": routes}


# =========================
# MODO "VOY CONTIGO" (RF-15 a RF-19)
# =========================

@app.post("/voy_contigo/start")
def start_tracking():
    return {"message": "Modo 'Voy contigo' activado"}

@app.post("/voy_contigo/check")
def check_status(data: DeviationCheck):
    if data.deviation:
        return {"alert": "Prealerta generada"}
    return {"status": "Todo correcto"}


# =========================
# INCIDENCIAS (RF-27, RF-28)
# =========================

@app.post("/incident")
def report_incident(incident: Incident):
    incidents_db.append(incident)
    return {
        "message": "Incidencia registrada",
        "total": len(incidents_db)
    }


# =========================
# ESTADÍSTICAS (RF-29)
# =========================

@app.get("/stats")
def get_stats():
    return {
        "total_incidents": len(incidents_db)
    }


# =========================
# ROOT (opcional)
# =========================

@app.get("/")
def root():
    return {"message": "API Senda URJC funcionando"}