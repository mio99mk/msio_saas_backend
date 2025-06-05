from fastapi import APIRouter, Request, HTTPException
from pymongo import MongoClient
from utils.jwt_handler import create_token
import hashlib, os

router = APIRouter()
client = MongoClient(os.getenv("MONGO_URI"))
users = client["msio"]["users"]

def hash_password(pw): return hashlib.sha256(pw.encode()).hexdigest()

@router.post("/register")
async def register(req: Request):
    data = await req.json()
    if users.find_one({"email": data["email"]}):
        raise HTTPException(status_code=409, detail="Email already registered")
    users.insert_one({
        "username": data["username"],
        "email": data["email"],
        "password": hash_password(data["password"]),
        "plan": "free",
        "active": True
    })
    return {"status": "registered"}

@router.post("/login")
async def login(req: Request):
    data = await req.json()
    user = users.find_one({"email": data["email"]})
    if not user or user["password"] != hash_password(data["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token(str(user["_id"]))
    return {"access_token": token}

from fastapi import APIRouter
router = APIRouter()

@router.post("/register")
def register(): return {"msg": "registered"}

@router.post("/login")
def login(): return {"msg": "token"}
