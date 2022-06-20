from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from app import repo, schemas
from sqlalchemy.orm import Session
from app.api.dependecies import get_db
from app.api.security import get_password_hash

router = APIRouter()


@router.post("")
def create_user(payload: schemas.user.UserCreate, db: Session = Depends(get_db)):
    user_from_db = repo.user_repo.get_by_username(db=db, username=payload.username)
    if user_from_db:
        # if user with given username exists...
        raise HTTPException(status_code=409, detail="Username already taken!")
    user_from_db = repo.user_repo.get_by_email(db=db, email=payload.email)
    if user_from_db:
        # if user with given email exists...
        raise HTTPException(status_code=409, detail="Email already taken!")
    user_from_db = repo.user_repo.get_by_email(db=db, email=payload.email)
    user = schemas.user.UserBase(**payload.dict(), date_joined=datetime.now())
    user.password = get_password_hash(payload.password)
    repo.user_repo.create(db=db, obj_in=user)
    