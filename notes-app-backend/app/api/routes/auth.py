from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, repo, models
from app.api.dependecies import get_db
from app.api import security

router = APIRouter()


@router.post("/login")
def login(payload: schemas.user.UserLogin, db: Session = Depends(get_db)):
    user: models.user.User = repo.user_repo.get_by_username(db=db, username=payload.username)
    if not user:
        # User not found
        raise HTTPException(status_code=404, detail="No such user found!")
    if not security.verify_password(payload.password, user.password):
        # Password incorrecr
        raise HTTPException(status_code=403, detail="Password incorrect")
    access_token = security.create_access_token({"username":user.username})
    return {"access_token": access_token, "token_type": "bearer"}