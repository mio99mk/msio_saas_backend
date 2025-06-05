
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/register")
def register_user():
    return {"msg": "user registered"}

@router.post("/login")
def login_user():
    return {"msg": "JWT token returned"}
