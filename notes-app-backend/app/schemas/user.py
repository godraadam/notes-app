from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    email: str
    date_joined: datetime
    
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    password: str
    email: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    password: Optional[str]
    email: Optional[str]