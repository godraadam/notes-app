from datetime import datetime
from fastapi import APIRouter, Depends
from app import models, schemas, repo
from app.api.dependecies import get_current_user, get_db

from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/")
def get_notes_of_user(user: models.User = Depends(get_current_user)):
    return user.notes
    
@router.post("/")
def add_note_for_user(
    payload: schemas.NoteCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    note = schemas.Note(
        **payload.dict(), time_created=datetime.now(), owner_id=user.username
    )
    return repo.note_repo.create(db=db, obj_in=note)