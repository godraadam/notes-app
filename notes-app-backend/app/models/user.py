from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    date_joined = Column(DateTime, nullable=False)
    
    notes = relationship("Note", back_populates="owner")
    tasks = relationship("Task", back_populates="owner")
    