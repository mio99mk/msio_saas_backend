
from fastapi import APIRouter

router = APIRouter()

@router.get("/my")
def get_signals():
    return {"signals": ["BTC long", "ETH short"]}
