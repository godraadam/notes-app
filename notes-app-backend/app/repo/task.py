from app.repo.base import CRUDBase
from app import models, schemas

from sqlalchemy.orm import Session

class TaskRepo(CRUDBase[models.Task, schemas.Task, schemas.TaskUpdate]):

    def get_tasks_of_user(self, db: Session, username: str):
        return db.query(self.model).filter(self.model.owner_id == username).all()
        
task_repo = TaskRepo(models.Task)