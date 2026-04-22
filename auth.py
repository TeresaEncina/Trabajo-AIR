from fastapi import APIRouter, HTTPException
from models import User
from database import users_db

router = APIRouter()

@router.post("/login")
def login(user: User):
    if user.username in users_db and users_db[user.username] == user.password:
        return {"message": "Login correcto"}
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")