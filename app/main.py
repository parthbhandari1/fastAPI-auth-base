from fastapi import FastAPI
from app.api import auth
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

API_VERSION = "/api/v1"

app.include_router(auth.router, prefix=f"{API_VERSION}/auth", tags=["auth"])
