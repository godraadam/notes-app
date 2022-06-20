from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Note(BaseModel):
    title: str
    content: str
    time_created: datetime
    time_edited: Optional[datetime]

    class Config:
        orm_mode = True


class NoteInDB(Note):
    id: int


class NoteCreate(BaseModel):
    title: str
    content: str


class NoteUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
