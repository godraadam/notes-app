from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: Optional[str]
    priority: Optional[int]
    time_created: datetime
    time_edited: Optional[datetime]
    owner_id: str

    class Config:
        orm_mode = True


class TaskInDB(Task):
    id: int


class TaskCreate(BaseModel):
    title: str
    description: Optional[str]
    priority: Optional[int]


class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    priority: Optional[int]
