from app.repo.base import CRUDBase
from app import models, schemas
from sqlalchemy.orm import Session

class UserRepo(CRUDBase[models.user.User, schemas.user.UserBase, schemas.user.UserUpdate]):
    def get_by_username(self, db: Session, username: str):
        return db.query(self.model).filter(self.model.username == username).first()
        
    def get_by_email(self, db: Session, email: str):
        return db.query(self.model).filter(self.model.email == email).first()

user_repo = UserRepo(models.user.User)