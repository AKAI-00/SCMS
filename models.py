from sqlalchemy import Column, INTEGER, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from backend.db.database import Base
from .database import Base
import datetime

class User(Base):
    __tablename__ ="users"
    id = Column(INTEGER, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String, default="student")
    
    attendence = relationship("Attendance",back_populates="user") 

class Attendence(Base):
    __tablename__ = "attendence"
    id  =Column(INTEGER , primary_key=True, index=True)
    user_id = Column(INTEGER, ForeignKey("users.id"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)


    present = Column(Boolean, default=False)

    user = relationship("User", back_populates="attendence")
    