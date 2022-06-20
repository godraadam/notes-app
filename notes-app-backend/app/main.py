from operator import index
from fastapi import FastAPI

from app.database import engine, Base
from app.api import index

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(index.router, prefix="/api")

@app.get("/")
async def root():
    return {"Notes app by godraadam"}