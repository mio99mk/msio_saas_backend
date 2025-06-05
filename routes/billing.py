
from fastapi import APIRouter
router = APIRouter()

@router.get("/status")
def billing_status(): return {"plan": "free", "active": True}
