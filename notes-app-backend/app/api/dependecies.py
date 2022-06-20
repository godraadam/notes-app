import logging
import traceback
from fastapi import Depends, HTTPException
from jose import JWTError
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.database import SessionLocal
from app.config import settings
from app import repo
from jose import jwt

logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/verify-token")

def get_db():
    session: Session = SessionLocal()
    try:
        yield session
    except Exception as ex:
        logger.error(f"Exception occurred:\n{str(ex)}")
        logger.error(traceback.format_exc())
        session.rollback()
    finally:
        session.close()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = repo.user_repo.get_by_username(db=db, username=username)
    if user is None:
        raise credentials_exception
    return user
