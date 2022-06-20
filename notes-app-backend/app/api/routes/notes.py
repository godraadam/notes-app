from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from app import models, schemas, repo
from app.api.dependecies import get_current_user, get_db

from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/")
def get_notes_of_user(user: models.User = Depends(get_current_user)):
    return user.notes


@router.get("/{note_id}")
def get_note_by_id(
    note_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    note_from_db = repo.note_repo.get(db=db, id=note_id)
    if not note_from_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if note_from_db.owner != user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return note_from_db


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


@router.put("/{note_id}")
def update_note_for_user(
    note_id: int,
    payload: schemas.NoteUpdate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    note_from_db = repo.note_repo.get(db=db, id=note_id)
    if not note_from_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if note_from_db.owner != user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    
    return repo.note_repo.update(db=db, db_obj=note_from_db, obj_in={**payload.dict(exclude_unset=True), "time_edited":datetime.now()})


@router.delete("/{note_id}")
def remove_note_of_user(
    note_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    note_from_db = repo.note_repo.get(db=db, id=note_id)
    if not note_from_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if note_from_db.owner != user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return repo.note_repo.remove(db=db, id=note_id)
