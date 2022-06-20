from app.repo.base import CRUDBase
from app import models, schemas

from sqlalchemy.orm import Session

class NoteRepo(CRUDBase[models.Note, schemas.Note, schemas.NoteUpdate]):

    def get_notes_of_user(self, db: Session, username: str):
        return db.query(self.model).filter(self.model.owner_id == username).all()
        
note_repo = NoteRepo(models.Note)