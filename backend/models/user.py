# MongoDB model placeholderfrom pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str
    plan: str = "free"
    active: bool = True
