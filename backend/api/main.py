
from fastapi import FastAPI
from backend.routes import auth, signals, billing

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(signals.router, prefix="/signals")
app.include_router(billing.router, prefix="/billing")

@app.get("/")
def root():
    return {"status": "SaaS API Live"}
