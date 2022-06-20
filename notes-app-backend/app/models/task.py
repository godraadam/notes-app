from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    time_created = Column(DateTime, nullable=False)
    time_edited = Column(DateTime, nullable=True)
    priority = Column(Integer, nullable=True)
    due_date = Column(Integer, nullable=True)
    completed = Column(Boolean, nullable=True, default=False)
    owner_id = Column(String, ForeignKey("users.username"))
    
    owner = relationship("User", back_populates="tasks")