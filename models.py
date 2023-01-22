
from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from async_database import Base


class Diary(Base):
    __tablename__ = "diary"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(10), nullable= False)
    contents = Column(Text(300), default="", nullable=False)
    user = relationship("User", backref=backref("diaries"))

class User(Base):
    
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(10), nullable=False)
    email = Column(String(30), nullable=True)
    diary_id = Column(Integer, ForeignKey("diaray.id"))
    
    
    
    
    