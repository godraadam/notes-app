from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from app import models, repo, schemas
from app.api.dependecies import get_current_user
from app.api.dependecies import get_db

from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/")
def get_tasks_of_user(user: models.User = Depends(get_current_user)):
    return user.tasks


@router.post("/")
def add_task_for_user(
    payload: schemas.TaskCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    task = schemas.Task(
        **payload.dict(), time_created=datetime.now(), owner_id=user.username
    )
    return repo.task_repo.create(db=db, obj_in=task)
    
@router.get("/{task_id}")
def get_task_by_id(
    task_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    task_from_repo = repo.task_repo.get(db=db, id=task_id)
    if not task_from_repo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if task_from_repo.owner != user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return task_from_repo


@router.post("/")
def add_task_for_user(
    payload: schemas.NoteCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    task = schemas.Note(
        **payload.dict(), time_created=datetime.now(), owner_id=user.username
    )
    return repo.task_repo.create(db=db, obj_in=task)


@router.put("/{task_id}")
def update_note_for_user(
    task_id: int,
    payload: schemas.NoteUpdate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    task_from_repo = repo.task_repo.get(db=db, id=task_id)
    if not task_from_repo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if task_from_repo.owner != user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    
    return repo.task_repo.update(db=db, db_obj=task_from_repo, obj_in={**payload.dict(exclude_unset=True), "time_edited":datetime.now()})


@router.delete("/{task_id}")
def remove_task_of_user(
    task_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    task_from_repo = repo.task_repo.get(db=db, id=task_id)
    if not task_from_repo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if task_from_repo.owner != user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return repo.task_repo.remove(db=db, id=task_id)
