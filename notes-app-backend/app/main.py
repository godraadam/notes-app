from operator import index
from fastapi import FastAPI

from app.api import index

app = FastAPI()

app.include_router(index.router, prefix="/api")

@app.get("/")
async def root():
    return {"Notes app by godraadam"}