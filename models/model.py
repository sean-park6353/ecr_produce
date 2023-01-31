
from sqlalchemy import Column, Integer, Text, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Diary(Base):
    __tablename__ = "diary"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(10), nullable= False)
    contents = Column(Text(300), default="", nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    user_id = Column(Integer, ForeignKey("user.id"))
    
class User(Base):
    
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(10), nullable=False)
    email = Column(String(30), nullable=True)
    diary_id = Column(Integer, ForeignKey("diary.id"))
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    
    
    
    
    