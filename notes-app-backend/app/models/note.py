from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    time_created = Column(DateTime, nullable=False)
    time_edited = Column(DateTime, nullable=True)
    content = Column(String, nullable=False, default="", index=True)
    owner_id = Column(String, ForeignKey("users.username"))
    
    owner = relationship("User", back_populates="notes")