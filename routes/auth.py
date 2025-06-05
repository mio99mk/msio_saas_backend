
from fastapi import APIRouter
router = APIRouter()

@router.post("/register")
def register(): return {"msg": "registered"}

@router.post("/login")
def login(): return {"msg": "token"}
