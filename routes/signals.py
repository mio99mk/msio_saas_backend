
from fastapi import APIRouter
router = APIRouter()

@router.get("/my")
def get_signals(): return {"signals": ["BTC long", "ETH short"]}
from fastapi import APIRouter, Request
from pymongo import MongoClient
import os, datetime

router = APIRouter()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["msio"]
signals = db["signals"]

@router.post("/push")
async def push_signal(req: Request):
    data = await req.json()
    data["timestamp"] = datetime.datetime.utcnow()
    signals.insert_one(data)
    return {"status": "stored", "data": data}
