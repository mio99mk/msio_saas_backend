
from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def billing_status():
    return {"plan": "FREE", "limit": 5}
