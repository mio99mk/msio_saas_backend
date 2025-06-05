# JWT encode/decode logicimport jwt, datetime, os

SECRET = os.getenv("JWT_SECRET", "top_secret")

def create_token(user_id: str):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload["user_id"]
    except:
        return None
