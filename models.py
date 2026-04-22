from pydantic import BaseModel

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