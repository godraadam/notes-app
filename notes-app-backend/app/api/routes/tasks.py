from datetime import datetime
from fastapi import APIRouter, Depends
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
